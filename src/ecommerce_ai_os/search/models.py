"""Minimal provider-neutral Search representations."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SearchInvocationContext:
    """Minimal P2 context binding a Search invocation to one Execution."""

    execution_id: str


@dataclass(frozen=True, slots=True)
class SearchRequest:
    """A minimal provider-neutral Search need for the First Slice."""

    query: str
    market: str


@dataclass(frozen=True, slots=True)
class SearchResult:
    """A minimal identified result with an explicit returned-set boundary."""

    search_result_id: str
    returned_item_count: int

    def __post_init__(self) -> None:
        if self.returned_item_count < 0:
            raise ValueError("returned_item_count must not be negative")
