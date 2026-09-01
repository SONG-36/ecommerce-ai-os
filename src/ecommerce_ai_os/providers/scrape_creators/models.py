"""Thin provider-specific values at the Scrape Creators access boundary."""

from dataclasses import dataclass


def _require_non_empty(value: str, field_name: str) -> None:
    if not value.strip():
        raise ValueError(f"{field_name} must not be empty")


@dataclass(frozen=True, slots=True)
class ScrapeCreatorsSearchKeywordRequest:
    """Admitted TT-17 request mechanics without provider-neutral semantics."""

    query: str
    region: str
    cursor: str | None = None

    def __post_init__(self) -> None:
        _require_non_empty(self.query, "query")
        _require_non_empty(self.region, "region")
        if self.cursor is not None:
            _require_non_empty(self.cursor, "cursor")


@dataclass(frozen=True, slots=True)
class ScrapeCreatorsRawResponse:
    """Untouched provider response payload before C4b interpretation."""

    body: bytes

    def __post_init__(self) -> None:
        if not isinstance(self.body, bytes):
            raise TypeError("body must be bytes")
