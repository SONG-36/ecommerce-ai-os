"""The provider-neutral Search capability seam."""

from typing import Protocol

from .models import (
    SearchFailure,
    SearchInvocationContext,
    SearchRequest,
    SearchResult,
)


class SearchCapability(Protocol):
    """A C3 dependency seam, not a runtime service or runtime hop."""

    def search(
        self,
        request: SearchRequest,
        context: SearchInvocationContext,
    ) -> SearchResult | SearchFailure:
        """Return a provider-neutral Search outcome."""
        ...
