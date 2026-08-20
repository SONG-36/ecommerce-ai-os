"""Execution-scoped capability invocation coordination."""

from typing import cast

from ecommerce_ai_os.research.models import ResearchCompletion
from ecommerce_ai_os.research.ports import ResearchSkill
from ecommerce_ai_os.search.models import (
    SearchInvocationContext,
    SearchRequest,
    SearchResult,
)
from ecommerce_ai_os.search.port import SearchCapability

from .execution import ExecutionContext


class TaskRuntime:
    """Coordinate capability invocations for the current Execution."""

    def __init__(self, search_capability: SearchCapability) -> None:
        self._search_capability = search_capability

    def _run_research_skill(
        self,
        context: ExecutionContext,
        skill: ResearchSkill,
    ) -> ResearchCompletion:
        """Run the bound business method without terminalizing the Execution."""
        if skill.declaration != context.skill_declaration:
            raise RuntimeError(
                "bound ResearchSkill declaration does not match ExecutionContext"
            )

        port = RuntimeResearchExecutionPort(self, context)
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

        # P2 exercises the Fake success path only; SearchFailure handling is deferred.
        return cast(SearchResult, result)


class RuntimeResearchExecutionPort:
    """Execution-scoped bridge from Research needs to runtime coordination."""

    def __init__(
        self,
        task_runtime: TaskRuntime,
        context: ExecutionContext,
    ) -> None:
        self._task_runtime = task_runtime
        self._context = context

    def search(self, request: SearchRequest) -> SearchResult:
        """Return a provider-neutral Search result to the same caller."""
        return self._task_runtime._invoke_search(self._context, request)
