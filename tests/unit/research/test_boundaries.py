from dataclasses import FrozenInstanceError
import unittest

from ecommerce_ai_os.research.models import SkillDeclaration
from ecommerce_ai_os.research.ports import ResearchExecutionPort
from ecommerce_ai_os.search.models import SearchRequest, SearchResult


class StubResearchExecutionPort:
    def search(self, request: SearchRequest) -> SearchResult:
        return SearchResult(
            search_result_id=f"result-for-{request.query}",
            returned_item_count=0,
        )


def search_through(port: ResearchExecutionPort, request: SearchRequest) -> SearchResult:
    return port.search(request)


class ResearchBoundaryTests(unittest.TestCase):
    def test_skill_declaration_preserves_declared_capability_identity(self) -> None:
        declaration = SkillDeclaration(
            skill_id="car-vacuum-tiktok-research",
            skill_version="1",
            declared_capabilities=frozenset({"Search"}),
        )

        self.assertEqual(declaration.declared_capabilities, frozenset({"Search"}))
        with self.assertRaises(FrozenInstanceError):
            declaration.skill_version = "2"  # type: ignore[misc]

    def test_structural_port_stub_satisfies_the_callable_seam(self) -> None:
        result = search_through(
            StubResearchExecutionPort(),
            SearchRequest(query="car vacuum", market="US"),
        )

        self.assertEqual(result.search_result_id, "result-for-car vacuum")


if __name__ == "__main__":
    unittest.main()
