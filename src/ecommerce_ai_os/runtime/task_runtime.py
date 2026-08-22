"""Execution-scoped capability invocation coordination."""

from typing import Callable, NoReturn
from uuid import uuid4

from ecommerce_ai_os.research.models import ResearchCompletion
from ecommerce_ai_os.research.serialization import (
    serialize_actual_sample_boundary,
    serialize_evidence,
    serialize_research_result,
)
from ecommerce_ai_os.research.ports import ResearchSkill
from ecommerce_ai_os.search.models import (
    SearchInvocationContext,
    SearchRequest,
    SearchResult,
)
from ecommerce_ai_os.search.port import SearchCapability
from ecommerce_ai_os.search.serialization import serialize_search_result

from .execution import (
    BusinessWorkRequest,
    ExecutionContext,
    PreExecutionRejection,
    TaskExecutionResponse,
    TerminalReturn,
)
from .execution_record import (
    StableExecutionFacts,
    serialize_finalized_execution_record,
    serialize_work_request,
)
from .retention import LocalJsonRetention


SearchResultObserver = Callable[[SearchResult], None]


class _ExecutionAbort(Exception):
    """C2b-private unwind for an established Execution that cannot continue."""

    def __init__(
        self,
        execution_id: str,
        *,
        actual_capability: str,
        failure_code: str,
        failure_reason: str,
    ) -> None:
        super().__init__(f"established Execution {execution_id} cannot continue")
        self.execution_id = execution_id
        self.actual_capability = actual_capability
        self.failure_code = failure_code
        self.failure_reason = failure_reason


class TaskRuntime:
    """Coordinate capability invocations for the current Execution."""

    def __init__(
        self,
        search_capability: SearchCapability,
        research_skill: ResearchSkill | None = None,
        retention: LocalJsonRetention | None = None,
    ) -> None:
        self._search_capability = search_capability
        self._research_skill = research_skill
        self._retention = retention

    def execute(self, work_request: BusinessWorkRequest) -> TaskExecutionResponse:
        """Admit business work, then execute the established WI-1 path."""
        if self._research_skill is None or self._retention is None:
            raise RuntimeError("TaskRuntime.execute requires composed P4 dependencies")

        rejection = self._pre_execution_rejection(work_request)
        if rejection is not None:
            return rejection

        execution_id = str(uuid4())
        # Creating the canonical context is the semantic establishment commit.
        context = ExecutionContext(
            execution_id=execution_id,
            work_request=work_request,
            skill_declaration=self._research_skill.declaration,
        )
        bundle = self._retention.begin_execution(execution_id)

        work_request_ref = bundle.write_json(
            self._artifact_ref("inputs", work_request.request_id),
            serialize_work_request(work_request),
        )
        stable_facts = StableExecutionFacts(
            execution_id=execution_id,
            work_request_ref=work_request_ref,
            skill_id=self._research_skill.declaration.skill_id,
            skill_version=self._research_skill.declaration.skill_version,
        )

        def retain_search_result(search_result: SearchResult) -> None:
            search_result_ref = bundle.write_json(
                self._artifact_ref(
                    "search_results",
                    search_result.search_result_id,
                ),
                serialize_search_result(search_result),
            )
            stable_facts.record_search_result(search_result_ref)

        try:
            completion = self._run_research_skill(
                context,
                self._research_skill,
                search_result_observer=retain_search_result,
            )
        except _ExecutionAbort as abort:
            stable_facts.record_execution_failure(
                actual_capability=abort.actual_capability,
                failure_code=abort.failure_code,
                failure_reason=abort.failure_reason,
            )
            finalized_record = stable_facts.finalize_failure()
            record_ref = bundle.publish(
                serialize_finalized_execution_record(finalized_record),
                finalized_record.required_references,
            )
            return TerminalReturn(
                execution_id=abort.execution_id,
                execution_outcome=finalized_record.terminal_outcome,
                business_result=None,
                record_ref=record_ref,
            )

        sample_boundary = completion.actual_sample_boundary
        sample_boundary_ref = bundle.write_json(
            self._artifact_ref(
                "sample_boundaries",
                str(sample_boundary.sample_boundary_id),
            ),
            serialize_actual_sample_boundary(sample_boundary),
        )
        evidence_refs = tuple(
            bundle.write_json(
                self._artifact_ref("evidence", str(evidence.evidence_id)),
                serialize_evidence(evidence),
            )
            for evidence in completion.admitted_evidence
        )
        research_result = completion.research_result
        research_result_ref = bundle.write_json(
            self._artifact_ref(
                "research_results",
                str(research_result.research_result_id),
            ),
            serialize_research_result(research_result),
        )
        stable_facts.record_research_completion(
            actual_sample_boundary_ref=sample_boundary_ref,
            evidence_refs=evidence_refs,
            research_result_ref=research_result_ref,
        )

        try:
            finalized_record = stable_facts.finalize_success()
            record_ref = bundle.publish(
                serialize_finalized_execution_record(finalized_record),
                finalized_record.required_references,
            )
        except (OSError, RuntimeError):
            return TerminalReturn(
                execution_id=execution_id,
                execution_outcome="FAILED",
                business_result=research_result,
                record_ref=None,
            )
        return TerminalReturn(
            execution_id=execution_id,
            execution_outcome=finalized_record.terminal_outcome,
            business_result=research_result,
            record_ref=record_ref,
        )

    @staticmethod
    def _pre_execution_rejection(
        work_request: BusinessWorkRequest,
    ) -> PreExecutionRejection | None:
        required_request_values = (
            work_request.request_id,
            work_request.product_context,
            work_request.market,
            work_request.platform,
            work_request.business_goal,
            work_request.research_question,
        )
        if any(not value.strip() for value in required_request_values):
            return PreExecutionRejection(
                reason="required First-Slice request context is incomplete"
            )
        return None

    def _run_research_skill(
        self,
        context: ExecutionContext,
        skill: ResearchSkill,
        search_result_observer: SearchResultObserver | None = None,
    ) -> ResearchCompletion:
        """Run the bound business method without terminalizing the Execution."""
        if skill.declaration != context.skill_declaration:
            raise RuntimeError(
                "bound ResearchSkill declaration does not match ExecutionContext"
            )

        port = RuntimeResearchExecutionPort(
            self,
            context,
            search_result_observer=search_result_observer,
        )
        return skill.run(port)

    def _invoke_search(
        self,
        context: ExecutionContext,
        request: SearchRequest,
    ) -> SearchResult:
        if "Search" not in context.skill_declaration.declared_capabilities:
            raise RuntimeError("bound Skill did not declare Search capability")

        invocation_context = SearchInvocationContext(
            execution_id=context.execution_id,
        )
        result = self._search_capability.search(request, invocation_context)
        if not isinstance(result, SearchResult):
            self._abort_execution(
                context,
                actual_capability="Search",
                failure_code="SEARCH_OUTCOME_NOT_RESULT",
                failure_reason=(
                    "Search invocation did not produce a contract-valid SearchResult"
                ),
            )

        return result

    @staticmethod
    def _abort_execution(
        context: ExecutionContext,
        *,
        actual_capability: str,
        failure_code: str,
        failure_reason: str,
    ) -> NoReturn:
        raise _ExecutionAbort(
            context.execution_id,
            actual_capability=actual_capability,
            failure_code=failure_code,
            failure_reason=failure_reason,
        )

    @staticmethod
    def _artifact_ref(directory: str, identifier: str) -> str:
        if not identifier or "/" in identifier or "\\" in identifier:
            raise ValueError(f"invalid owner-local artifact identity: {identifier}")
        return f"{directory}/{identifier}.json"


class RuntimeResearchExecutionPort:
    """Execution-scoped bridge from Research needs to runtime coordination."""

    def __init__(
        self,
        task_runtime: TaskRuntime,
        context: ExecutionContext,
        search_result_observer: SearchResultObserver | None = None,
    ) -> None:
        self._task_runtime = task_runtime
        self._context = context
        self._search_result_observer = search_result_observer

    def search(self, request: SearchRequest) -> SearchResult:
        """Return a provider-neutral Search result to the same caller."""
        result = self._task_runtime._invoke_search(self._context, request)
        if self._search_result_observer is not None:
            self._search_result_observer(result)
        return result
