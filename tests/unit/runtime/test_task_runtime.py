import unittest
from unittest.mock import patch

from ecommerce_ai_os.research.car_vacuum_tiktok import (
    CarVacuumTikTokResearchSkill,
)
from ecommerce_ai_os.research.models import ResearchCompletion, SkillDeclaration
from ecommerce_ai_os.research.ports import ResearchExecutionPort
from ecommerce_ai_os.runtime.execution import BusinessWorkRequest, ExecutionContext
from ecommerce_ai_os.runtime.task_runtime import (
    RuntimeResearchExecutionPort,
    TaskRuntime,
    _ExecutionAbort,
)
from ecommerce_ai_os.search.models import (
    SearchFailure,
    SearchFailureKind,
    SearchInvocationContext,
    SearchInvocationProvenance,
    SearchRequest,
    SearchResult,
    SearchResultOccurrence,
)


class FakeSearchCapability:
    def __init__(self, result: SearchResult) -> None:
        self._result = result
        self.calls = 0
        self.last_request: SearchRequest | None = None
        self.last_context: SearchInvocationContext | None = None

    def search(
        self,
        request: SearchRequest,
        context: SearchInvocationContext,
    ) -> SearchResult:
        self.calls += 1
        self.last_request = request
        self.last_context = context
        return self._result


class ContractInvalidSearchOutcome:
    """Test-only object outside the reviewed Search outcome contract."""


class ContractInvalidSearchCapability:
    def __init__(self) -> None:
        self.calls = 0
        self.last_context: SearchInvocationContext | None = None

    def search(
        self,
        request: SearchRequest,
        context: SearchInvocationContext,
    ) -> ContractInvalidSearchOutcome:
        del request
        self.calls += 1
        self.last_context = context
        return ContractInvalidSearchOutcome()


class TypedFailureSearchCapability:
    def __init__(self, failure: SearchFailure) -> None:
        self.failure = failure
        self.calls = 0
        self.last_context: SearchInvocationContext | None = None

    def search(
        self,
        request: SearchRequest,
        context: SearchInvocationContext,
    ) -> SearchFailure:
        del request
        self.calls += 1
        self.last_context = context
        return self.failure


def request_search_through(
    port: ResearchExecutionPort,
    request: SearchRequest,
) -> SearchResult | SearchFailure:
    return port.search(request)


class TaskRuntimeCoordinationTests(unittest.TestCase):
    def make_context(
        self,
        declared_capabilities: frozenset[str] = frozenset({"Search"}),
    ) -> ExecutionContext:
        work_request = BusinessWorkRequest(
            request_id="request-001",
            product_context="Car Vacuum",
            market="US",
            platform="TikTok",
            business_goal="Commerce Content",
            research_question="What content patterns merit human review?",
        )
        skill_declaration = SkillDeclaration(
            skill_id="car-vacuum-tiktok-research",
            skill_version="1",
            declared_capabilities=declared_capabilities,
        )
        return ExecutionContext(
            execution_id="execution-001",
            work_request=work_request,
            skill_declaration=skill_declaration,
        )

    def test_search_traverses_runtime_and_returns_to_the_business_caller(self) -> None:
        expected_result = SearchResult(
            search_result_id="search-result-001",
            returned_item_count=2,
            occurrences=(
                SearchResultOccurrence("item-1", "source-1"),
                SearchResultOccurrence("item-2", "source-2"),
            ),
        )
        fake_search = FakeSearchCapability(expected_result)
        runtime = TaskRuntime(search_capability=fake_search)
        context = self.make_context()
        port = RuntimeResearchExecutionPort(runtime, context)
        request = SearchRequest(query="car vacuum", market="US")

        actual_result = request_search_through(port, request)

        self.assertIs(actual_result, expected_result)
        self.assertEqual(fake_search.calls, 1)
        self.assertIs(fake_search.last_request, request)
        self.assertIsInstance(fake_search.last_context, SearchInvocationContext)
        self.assertEqual(fake_search.last_context.execution_id, context.execution_id)

    def test_undeclared_search_capability_is_not_invoked(self) -> None:
        fake_search = FakeSearchCapability(
            SearchResult(
                search_result_id="unused-result",
                returned_item_count=0,
            )
        )
        runtime = TaskRuntime(search_capability=fake_search)
        port = RuntimeResearchExecutionPort(
            runtime,
            self.make_context(declared_capabilities=frozenset()),
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "bound Skill did not declare Search capability",
        ):
            port.search(SearchRequest(query="car vacuum", market="US"))

        self.assertEqual(fake_search.calls, 0)

    def test_runtime_receives_business_completion_without_terminalization(self) -> None:
        expected_result = SearchResult(
            search_result_id="search-result-001",
            returned_item_count=2,
            occurrences=(
                SearchResultOccurrence("item-1", "source-1"),
                SearchResultOccurrence("item-2", "source-2"),
            ),
        )
        fake_search = FakeSearchCapability(expected_result)
        runtime = TaskRuntime(search_capability=fake_search)
        context = self.make_context()
        request = SearchRequest(query="car vacuum", market="US")
        skill = CarVacuumTikTokResearchSkill(search_request=request)

        completion = runtime._run_research_skill(context, skill)

        self.assertIsInstance(completion, ResearchCompletion)
        self.assertIs(
            completion.research_result.actual_sample_boundary,
            completion.actual_sample_boundary,
        )
        self.assertEqual(fake_search.calls, 1)
        self.assertIs(fake_search.last_request, request)
        self.assertIsInstance(fake_search.last_context, SearchInvocationContext)
        self.assertEqual(fake_search.last_context.execution_id, context.execution_id)
        self.assertFalse(hasattr(completion, "record_ref"))
        self.assertFalse(hasattr(completion, "finalized_execution_record"))

    def test_mismatched_bound_skill_declaration_is_rejected_before_search(self) -> None:
        fake_search = FakeSearchCapability(
            SearchResult(
                search_result_id="unused-result",
                returned_item_count=0,
            )
        )
        runtime = TaskRuntime(search_capability=fake_search)
        context = self.make_context()
        context.skill_declaration = SkillDeclaration(
            skill_id="different-research-skill",
            skill_version="1",
            declared_capabilities=frozenset({"Search"}),
        )
        skill = CarVacuumTikTokResearchSkill(
            search_request=SearchRequest(query="car vacuum", market="US")
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "bound ResearchSkill declaration does not match ExecutionContext",
        ):
            runtime._run_research_skill(context, skill)

        self.assertEqual(fake_search.calls, 0)

    def test_invalid_request_failure_returns_unchanged_to_same_execution(self) -> None:
        provenance = SearchInvocationProvenance(
            resolved_provider_ref="provider-binding:test-search",
            used_provider_ref="provider-binding:test-search",
            capability_result_ref="search-failure:test-invalid-request",
        )
        failure = SearchFailure(
            kind=SearchFailureKind.INVALID_REQUEST,
            failure_code="SEARCH_REQUEST_UNSUPPORTED_BOUND",
            reason="the requested bound is unsupported by this Search path",
            provenance=provenance,
        )
        typed_failure = TypedFailureSearchCapability(failure)
        runtime = TaskRuntime(search_capability=typed_failure)
        context = self.make_context()
        port = RuntimeResearchExecutionPort(runtime, context)

        with patch.object(
            runtime,
            "_abort_execution",
            wraps=runtime._abort_execution,
        ) as observed_abort:
            returned_failure = request_search_through(
                port,
                SearchRequest(query="car vacuum", market="US"),
            )

        self.assertIs(returned_failure, failure)
        self.assertIs(returned_failure.kind, SearchFailureKind.INVALID_REQUEST)
        self.assertEqual(
            returned_failure.failure_code,
            "SEARCH_REQUEST_UNSUPPORTED_BOUND",
        )
        self.assertEqual(
            returned_failure.reason,
            "the requested bound is unsupported by this Search path",
        )
        self.assertIs(returned_failure.provenance, provenance)
        self.assertEqual(typed_failure.calls, 1)
        self.assertIsNotNone(typed_failure.last_context)
        self.assertEqual(typed_failure.last_context.execution_id, context.execution_id)
        observed_abort.assert_not_called()

    def test_provider_invocation_failure_triggers_private_execution_abort(self) -> None:
        failure = SearchFailure(
            kind=SearchFailureKind.PROVIDER_INVOCATION,
            failure_code="PROVIDER_REQUEST_FAILED",
            reason="the selected Provider invocation failed",
        )
        typed_failure = TypedFailureSearchCapability(failure)
        runtime = TaskRuntime(search_capability=typed_failure)
        context = self.make_context()
        port = RuntimeResearchExecutionPort(runtime, context)

        with self.assertRaises(_ExecutionAbort) as captured_abort:
            port.search(SearchRequest(query="car vacuum", market="US"))

        self.assertEqual(captured_abort.exception.execution_id, context.execution_id)
        self.assertEqual(captured_abort.exception.actual_capability, "Search")
        self.assertEqual(
            captured_abort.exception.failure_code,
            "PROVIDER_REQUEST_FAILED",
        )
        self.assertEqual(
            captured_abort.exception.failure_reason,
            "the selected Provider invocation failed",
        )
        self.assertEqual(typed_failure.calls, 1)
        self.assertIsNotNone(typed_failure.last_context)
        self.assertEqual(
            typed_failure.last_context.execution_id,
            context.execution_id,
        )

    def test_provider_resolution_failure_triggers_private_execution_abort(self) -> None:
        failure = SearchFailure(
            kind=SearchFailureKind.PROVIDER_RESOLUTION,
            failure_code="PROVIDER_NOT_RESOLVED",
            reason="no Provider binding resolved for the Search request",
        )
        runtime = TaskRuntime(search_capability=TypedFailureSearchCapability(failure))
        context = self.make_context()
        port = RuntimeResearchExecutionPort(runtime, context)

        with self.assertRaises(_ExecutionAbort) as captured_abort:
            port.search(SearchRequest(query="car vacuum", market="US"))

        self.assertEqual(captured_abort.exception.execution_id, context.execution_id)
        self.assertEqual(
            captured_abort.exception.failure_code,
            "PROVIDER_NOT_RESOLVED",
        )
        self.assertEqual(
            captured_abort.exception.failure_reason,
            "no Provider binding resolved for the Search request",
        )

    def test_malformed_failure_kind_uses_private_abort(self) -> None:
        failure = SearchFailure(
            kind="unsupported-search-failure-kind",  # type: ignore[arg-type]
            failure_code="MALFORMED_SEARCH_FAILURE_KIND",
            reason="Search returned an unsupported failure kind",
        )
        runtime = TaskRuntime(search_capability=TypedFailureSearchCapability(failure))
        context = self.make_context()
        port = RuntimeResearchExecutionPort(runtime, context)

        with self.assertRaises(_ExecutionAbort) as captured_abort:
            port.search(SearchRequest(query="car vacuum", market="US"))

        self.assertEqual(captured_abort.exception.execution_id, context.execution_id)
        self.assertEqual(captured_abort.exception.actual_capability, "Search")
        self.assertEqual(
            captured_abort.exception.failure_code,
            "MALFORMED_SEARCH_FAILURE_KIND",
        )
        self.assertEqual(
            captured_abort.exception.failure_reason,
            "Search returned an unsupported failure kind",
        )

    def test_contract_invalid_search_outcome_keeps_defensive_abort(self) -> None:
        invalid_search = ContractInvalidSearchCapability()
        runtime = TaskRuntime(search_capability=invalid_search)
        context = self.make_context()
        port = RuntimeResearchExecutionPort(runtime, context)

        with self.assertRaises(_ExecutionAbort) as captured_abort:
            port.search(SearchRequest(query="car vacuum", market="US"))

        self.assertEqual(captured_abort.exception.execution_id, context.execution_id)
        self.assertEqual(captured_abort.exception.actual_capability, "Search")
        self.assertEqual(
            captured_abort.exception.failure_code,
            "SEARCH_OUTCOME_NOT_RESULT",
        )
        self.assertEqual(
            captured_abort.exception.failure_reason,
            "Search invocation did not produce a contract-valid SearchResult",
        )
        self.assertEqual(invalid_search.calls, 1)
        self.assertIsNotNone(invalid_search.last_context)
        self.assertEqual(
            invalid_search.last_context.execution_id,
            context.execution_id,
        )


if __name__ == "__main__":
    unittest.main()
