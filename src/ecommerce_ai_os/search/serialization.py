"""Owner-local JSON representations for retained Search values."""

from datetime import datetime

from .models import (
    SearchFailure,
    SearchFailureKind,
    SearchInvocationProvenance,
    SearchResult,
    SearchResultOccurrence,
)


def _serialize_time(value: datetime | None) -> str | None:
    return value.isoformat() if value is not None else None


def _serialize_occurrence(
    occurrence: SearchResultOccurrence,
) -> dict[str, object]:
    return {
        "item_ref": occurrence.item_ref,
        "source_ref": occurrence.source_ref,
        "known_missing_fields": sorted(occurrence.known_missing_fields),
        "publication_time": _serialize_time(occurrence.publication_time),
        "observation_time": _serialize_time(occurrence.observation_time),
    }


def _serialize_provenance(
    provenance: SearchInvocationProvenance,
) -> dict[str, object]:
    return {
        "resolved_provider_ref": provenance.resolved_provider_ref,
        "used_provider_ref": provenance.used_provider_ref,
        "capability_result_ref": provenance.capability_result_ref,
        "raw_result_refs": [
            {"reference_id": raw_result_ref.reference_id}
            for raw_result_ref in provenance.raw_result_refs
        ],
    }


def _serialize_failure_kind(kind: SearchFailureKind) -> str:
    return kind.value if isinstance(kind, SearchFailureKind) else str(kind)


def serialize_search_result(result: SearchResult) -> dict[str, object]:
    """Serialize the bounded provider-neutral Search result."""
    return {
        "schema_version": 1,
        "search_result_id": result.search_result_id,
        "returned_item_count": result.returned_item_count,
        "occurrences": [
            _serialize_occurrence(occurrence) for occurrence in result.occurrences
        ],
        "requested_item_count": result.requested_item_count,
        "stopping_reason": result.stopping_reason.value,
        "continuation": result.continuation.value,
        "completion": result.completion.value,
        "provider_exhaustion": result.provider_exhaustion.value,
        "global_completeness": result.global_completeness.value,
        "limitations": list(result.limitations),
        "collection_time": _serialize_time(result.collection_time),
        "provenance": _serialize_provenance(result.provenance),
    }


def serialize_search_failure(failure: SearchFailure) -> dict[str, object]:
    """Serialize one typed Search failure without creating a retained artifact."""
    return {
        "schema_version": 1,
        "kind": _serialize_failure_kind(failure.kind),
        "failure_code": failure.failure_code,
        "reason": failure.reason,
        "provenance": _serialize_provenance(failure.provenance),
    }
