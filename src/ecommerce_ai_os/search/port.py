"""The provider-neutral Search capability seam."""

from __future__ import annotations

from typing import Protocol

from .models import SearchRequest, SearchResult


class SearchCapability(Protocol):
    """A C3 dependency seam, not a runtime service or runtime hop."""

    def search(
        self,
        request: SearchRequest,
        context: SearchInvocationContext,
    ) -> SearchResult | SearchFailure:
        """Return a provider-neutral Search outcome."""
        ...


# SearchInvocationContext (B04) and SearchFailure remain postponed annotations
# until WI-3 selects and implements their complete representations.
