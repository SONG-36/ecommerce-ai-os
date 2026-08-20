"""Deterministic provider-neutral Fake Search for the WI-1 executable path."""

from dataclasses import dataclass

from .models import SearchInvocationContext, SearchRequest, SearchResult


@dataclass(frozen=True, slots=True)
class FakeSearchCapability:
    """Return one configured synthetic Search boundary without provider claims."""

    returned_item_count: int = 2
    search_result_id: str = "wi1-fake-search-result"

    def search(
        self,
        request: SearchRequest,
        context: SearchInvocationContext,
    ) -> SearchResult:
        """Return the deterministic Fake result for the current invocation."""
        del request, context
        return SearchResult(
            search_result_id=self.search_result_id,
            returned_item_count=self.returned_item_count,
        )
