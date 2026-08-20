import unittest

from ecommerce_ai_os.research.car_vacuum_tiktok import (
    CarVacuumTikTokResearchSkill,
)
from ecommerce_ai_os.research.models import ResearchCompletion
from ecommerce_ai_os.search.models import SearchRequest, SearchResult


class StubResearchExecutionPort:
    def __init__(self, result: SearchResult) -> None:
        self._result = result
        self.calls = 0
        self.last_request: SearchRequest | None = None

    def search(self, request: SearchRequest) -> SearchResult:
        self.calls += 1
        self.last_request = request
        return self._result


class FirstSliceResearchSkillTests(unittest.TestCase):
    def test_forms_synthetic_business_completion_from_bounded_search(self) -> None:
        request = SearchRequest(query="car vacuum", market="US")
        port = StubResearchExecutionPort(
            SearchResult(
                search_result_id="search-result-001",
                returned_item_count=2,
            )
        )
        skill = CarVacuumTikTokResearchSkill(search_request=request)

        completion = skill.run(port)

        self.assertIsInstance(completion, ResearchCompletion)
        self.assertEqual(skill.declaration.declared_capabilities, frozenset({"Search"}))
        self.assertEqual(port.calls, 1)
        self.assertIs(port.last_request, request)
        self.assertEqual(
            completion.actual_sample_boundary.source_search_result_id,
            "search-result-001",
        )
        self.assertEqual(completion.actual_sample_boundary.returned_item_count, 2)
        self.assertEqual(len(completion.admitted_evidence), 1)
        self.assertIn(
            "WI-1 Fake Search returned a bounded result",
            completion.admitted_evidence[0].observation,
        )
        self.assertIs(
            completion.research_result.actual_sample_boundary,
            completion.actual_sample_boundary,
        )
        self.assertIs(
            completion.research_result.evidence,
            completion.admitted_evidence,
        )
        self.assertTrue(
            any(
                "Synthetic / Fake execution evidence only" in limitation
                for limitation in completion.research_result.limitations
            )
        )

    def test_empty_search_is_insufficient_evidence_not_execution_failure(self) -> None:
        port = StubResearchExecutionPort(
            SearchResult(
                search_result_id="empty-search-result",
                returned_item_count=0,
            )
        )
        skill = CarVacuumTikTokResearchSkill(
            search_request=SearchRequest(query="car vacuum", market="US")
        )

        completion = skill.run(port)

        self.assertIsInstance(completion, ResearchCompletion)
        self.assertEqual(completion.admitted_evidence, ())
        self.assertEqual(completion.research_result.evidence, ())
        self.assertTrue(
            any(
                "evidence is insufficient for a substantive research conclusion"
                in limitation
                for limitation in completion.research_result.limitations
            )
        )


if __name__ == "__main__":
    unittest.main()
