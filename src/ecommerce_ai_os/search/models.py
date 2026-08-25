"""Stable provider-neutral Search boundary representations."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum


def _require_non_empty(value: str, field_name: str) -> None:
    if not value.strip():
        raise ValueError(f"{field_name} must not be empty")


def _utc(value: datetime | None, field_name: str) -> datetime | None:
    if value is None:
        return None
    if value.utcoffset() is None:
        raise ValueError(f"{field_name} must be timezone-aware")
    return value.astimezone(UTC)


class SearchStopReason(StrEnum):
    """Provider-neutral reason that bounded retrieval stopped."""

    REQUEST_BOUND_SATISFIED = "request_bound_satisfied"
    NO_MATCHES = "no_matches"
    CONTINUATION_UNAVAILABLE = "continuation_unavailable"
    LIMITATION_REACHED = "limitation_reached"
    UNKNOWN = "unknown"


class ContinuationState(StrEnum):
    """Whether another provider-neutral retrieval step is available."""

    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    UNKNOWN = "unknown"


class SearchCompletionState(StrEnum):
    """Completion of this bounded Search request, not global coverage."""

    COMPLETE_FOR_REQUEST = "complete_for_request"
    KNOWN_INCOMPLETE = "known_incomplete"
    UNKNOWN = "unknown"


class ProviderExhaustionState(StrEnum):
    """Known provider traversal state, distinct from Search completion."""

    EXHAUSTED = "exhausted"
    NOT_EXHAUSTED = "not_exhausted"
    UNKNOWN = "unknown"


class GlobalCompletenessState(StrEnum):
    """The only supported First-Slice claim about global completeness."""

    UNKNOWN = "unknown"


class SearchFailureKind(StrEnum):
    """Bounded C3 failure categories, not a universal error taxonomy."""

    INVALID_REQUEST = "invalid_request"
    PROVIDER_RESOLUTION = "provider_resolution"
    PROVIDER_INVOCATION = "provider_invocation"


@dataclass(frozen=True, slots=True)
class RawProviderResultRef:
    """An opaque Search-owned reference, never a raw provider payload."""

    reference_id: str

    def __post_init__(self) -> None:
        _require_non_empty(self.reference_id, "reference_id")


RawResultCapture = Callable[[object], RawProviderResultRef]


@dataclass(frozen=True, slots=True)
class SearchInvocationContext:
    """Narrow values and capabilities for one execution-scoped invocation."""

    execution_id: str
    raw_result_capture: RawResultCapture | None = None

    def __post_init__(self) -> None:
        _require_non_empty(self.execution_id, "execution_id")


@dataclass(frozen=True, slots=True)
class SearchInvocationProvenance:
    """Actual provider-neutral invocation facts known on one outcome path."""

    resolved_provider_ref: str | None = None
    used_provider_ref: str | None = None
    capability_result_ref: str | None = None
    raw_result_refs: tuple[RawProviderResultRef, ...] = ()

    def __post_init__(self) -> None:
        for field_name in (
            "resolved_provider_ref",
            "used_provider_ref",
            "capability_result_ref",
        ):
            value = getattr(self, field_name)
            if value is not None:
                _require_non_empty(value, field_name)
        if not isinstance(self.raw_result_refs, tuple):
            raise TypeError("raw_result_refs must be a tuple")
        if self.used_provider_ref is not None and self.resolved_provider_ref is None:
            raise ValueError("used_provider_ref requires resolved_provider_ref")
        if self.raw_result_refs and self.used_provider_ref is None:
            raise ValueError("raw_result_refs require used_provider_ref")


@dataclass(frozen=True, slots=True)
class SearchRequest:
    """A provider-neutral, optionally bounded First-Slice Search request."""

    query: str
    market: str
    platform: str | None = None
    requested_item_count: int | None = None

    def __post_init__(self) -> None:
        _require_non_empty(self.query, "query")
        _require_non_empty(self.market, "market")
        if self.platform is not None:
            _require_non_empty(self.platform, "platform")
        if self.requested_item_count is not None and self.requested_item_count <= 0:
            raise ValueError("requested_item_count must be positive")


@dataclass(frozen=True, slots=True)
class SearchResultOccurrence:
    """One ordered returned occurrence; repeated item refs remain valid."""

    item_ref: str
    source_ref: str
    known_missing_fields: frozenset[str] = field(default_factory=frozenset)
    publication_time: datetime | None = None
    observation_time: datetime | None = None

    def __post_init__(self) -> None:
        _require_non_empty(self.item_ref, "item_ref")
        _require_non_empty(self.source_ref, "source_ref")
        if not isinstance(self.known_missing_fields, frozenset):
            raise TypeError("known_missing_fields must be a frozenset")
        for field_name in self.known_missing_fields:
            _require_non_empty(field_name, "known missing field name")
        object.__setattr__(
            self,
            "publication_time",
            _utc(self.publication_time, "publication_time"),
        )
        object.__setattr__(
            self,
            "observation_time",
            _utc(self.observation_time, "observation_time"),
        )


@dataclass(frozen=True, slots=True)
class SearchResult:
    """A bounded C3 result with ordered occurrence and provenance facts."""

    search_result_id: str
    returned_item_count: int
    occurrences: tuple[SearchResultOccurrence, ...] = ()
    requested_item_count: int | None = None
    stopping_reason: SearchStopReason = SearchStopReason.UNKNOWN
    continuation: ContinuationState = ContinuationState.UNKNOWN
    completion: SearchCompletionState = SearchCompletionState.UNKNOWN
    provider_exhaustion: ProviderExhaustionState = ProviderExhaustionState.UNKNOWN
    global_completeness: GlobalCompletenessState = GlobalCompletenessState.UNKNOWN
    limitations: tuple[str, ...] = ()
    collection_time: datetime | None = None
    provenance: SearchInvocationProvenance = field(
        default_factory=SearchInvocationProvenance
    )

    def __post_init__(self) -> None:
        _require_non_empty(self.search_result_id, "search_result_id")
        if self.returned_item_count < 0:
            raise ValueError("returned_item_count must not be negative")
        if self.requested_item_count is not None and self.requested_item_count <= 0:
            raise ValueError("requested_item_count must be positive")
        if not isinstance(self.occurrences, tuple):
            raise TypeError("occurrences must be a tuple")
        if len(self.occurrences) != self.returned_item_count:
            raise ValueError(
                "returned_item_count must match the number of occurrences"
            )
        if not isinstance(self.limitations, tuple):
            raise TypeError("limitations must be a tuple")
        for limitation in self.limitations:
            _require_non_empty(limitation, "limitation")
        object.__setattr__(
            self,
            "collection_time",
            _utc(self.collection_time, "collection_time"),
        )


@dataclass(frozen=True, slots=True)
class SearchFailure:
    """A stable C3 failure outcome, distinct from results and exceptions."""

    kind: SearchFailureKind
    failure_code: str
    reason: str
    provenance: SearchInvocationProvenance = field(
        default_factory=SearchInvocationProvenance
    )

    def __post_init__(self) -> None:
        _require_non_empty(self.failure_code, "failure_code")
        _require_non_empty(self.reason, "reason")
