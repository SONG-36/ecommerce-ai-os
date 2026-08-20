"""Owner-local JSON representations for retained Search values."""

from .models import SearchResult


def serialize_search_result(result: SearchResult) -> dict[str, object]:
    """Serialize the bounded provider-neutral Search result."""
    return {
        "schema_version": 1,
        "search_result_id": result.search_result_id,
        "returned_item_count": result.returned_item_count,
    }
