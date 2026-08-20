import unittest

from ecommerce_ai_os.research.models import SkillDeclaration
from ecommerce_ai_os.research.ports import ResearchExecutionPort
from ecommerce_ai_os.runtime.execution import BusinessWorkRequest, ExecutionContext
from ecommerce_ai_os.runtime.task_runtime import (
    RuntimeResearchExecutionPort,
    TaskRuntime,
)
from ecommerce_ai_os.search.models import (
    SearchInvocationContext,
    SearchRequest,
    SearchResult,
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


def request_search_through(
    port: ResearchExecutionPort,
    request: SearchRequest,
) -> SearchResult:
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


if __name__ == "__main__":
    unittest.main()
