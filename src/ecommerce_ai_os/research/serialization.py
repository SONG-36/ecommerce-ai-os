"""Owner-local JSON representations for retained Research values."""

from .models import ActualSampleBoundary, Evidence, ResearchResult


def serialize_actual_sample_boundary(
    boundary: ActualSampleBoundary,
) -> dict[str, object]:
    """Serialize one stable Actual Sample Boundary representation."""
    return {
        "schema_version": 1,
        "sample_boundary_id": boundary.sample_boundary_id,
        "source_search_result_id": boundary.source_search_result_id,
        "returned_item_count": boundary.returned_item_count,
    }


def serialize_evidence(evidence: Evidence) -> dict[str, object]:
    """Serialize one admitted Evidence representation without foreign payloads."""
    return {
        "schema_version": 1,
        "evidence_id": evidence.evidence_id,
        "actual_sample_boundary_id": (
            evidence.actual_sample_boundary.sample_boundary_id
        ),
        "observation": evidence.observation,
    }


def serialize_research_result(result: ResearchResult) -> dict[str, object]:
    """Serialize a Research Result using owner-local references."""
    return {
        "schema_version": 1,
        "research_result_id": result.research_result_id,
        "actual_sample_boundary_id": result.actual_sample_boundary.sample_boundary_id,
        "evidence_ids": [evidence.evidence_id for evidence in result.evidence],
        "limitations": list(result.limitations),
    }
