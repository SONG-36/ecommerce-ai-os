"""Deterministic provider-neutral Fake Search for the WI-1 executable path."""

from dataclasses import dataclass

from .models import (
    SearchInvocationContext,
    SearchRequest,
    SearchResult,
    SearchResultOccurrence,
)


@dataclass(frozen=True, slots=True)
class FakeSearchCapability:
    """Return one configured synthetic Search boundary without provider claims."""

    returned_item_count: int = 2
    search_result_id: str = "wi1-fake-search-result"
    configured_result: SearchResult | None = None

    def search(
        self,
        request: SearchRequest,
        context: SearchInvocationContext,
    ) -> SearchResult:
        """Return the deterministic Fake result for the current invocation."""
        del request, context
        if self.configured_result is not None:
            return self.configured_result
        return SearchResult(
            search_result_id=self.search_result_id,
            returned_item_count=self.returned_item_count,
            occurrences=tuple(
                SearchResultOccurrence(
                    item_ref=f"{self.search_result_id}-item-{index}",
                    source_ref=f"{self.search_result_id}-source-{index}",
                )
                for index in range(1, self.returned_item_count + 1)
            ),
        )
