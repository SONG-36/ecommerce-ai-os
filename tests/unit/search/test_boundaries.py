from dataclasses import FrozenInstanceError
import unittest

from ecommerce_ai_os.search.models import SearchRequest, SearchResult
from ecommerce_ai_os.search.port import SearchCapability


class StubSearchCapability:
    def search(self, request: SearchRequest, context: object) -> SearchResult:
        del context
        return SearchResult(
            search_result_id=f"search-{request.market}",
            returned_item_count=2,
        )


def invoke_search(
    capability: SearchCapability,
    request: SearchRequest,
) -> SearchResult:
    return capability.search(request, object())


class SearchBoundaryTests(unittest.TestCase):
    def test_request_is_a_frozen_provider_neutral_value(self) -> None:
        request = SearchRequest(query="car vacuum", market="US")

        self.assertEqual(request.query, "car vacuum")
        with self.assertRaises(FrozenInstanceError):
            request.market = "CA"  # type: ignore[misc]

    def test_result_has_identity_and_returned_set_boundary(self) -> None:
        result = SearchResult(search_result_id="search-001", returned_item_count=2)

        self.assertEqual(result.search_result_id, "search-001")
        self.assertEqual(result.returned_item_count, 2)

    def test_result_rejects_a_negative_returned_item_count(self) -> None:
        with self.assertRaisesRegex(ValueError, "must not be negative"):
            SearchResult(search_result_id="search-001", returned_item_count=-1)

    def test_structural_search_stub_satisfies_the_callable_seam(self) -> None:
        result = invoke_search(
            StubSearchCapability(),
            SearchRequest(query="car vacuum", market="US"),
        )

        self.assertEqual(result.returned_item_count, 2)


if __name__ == "__main__":
    unittest.main()
