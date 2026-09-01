"""Provider-specific acquisition seam for Scrape Creators."""

from typing import Protocol

from .models import (
    ScrapeCreatorsRawResponse,
    ScrapeCreatorsSearchKeywordRequest,
)


class ScrapeCreatorsAccessError(Exception):
    """A bounded failure to acquire a Scrape Creators response."""


class ScrapeCreatorsAccess(Protocol):
    """Acquire untouched TT-17 payload bytes for one provider request."""

    def search_keyword(
        self,
        request: ScrapeCreatorsSearchKeywordRequest,
    ) -> ScrapeCreatorsRawResponse:
        """Return the untouched provider response payload."""
        ...
