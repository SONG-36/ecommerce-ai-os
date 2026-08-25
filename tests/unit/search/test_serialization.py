import json
from datetime import UTC, datetime, timedelta, timezone
import unittest

from ecommerce_ai_os.search.models import (
    ContinuationState,
    GlobalCompletenessState,
    ProviderExhaustionState,
    RawProviderResultRef,
    SearchCompletionState,
    SearchFailure,
    SearchFailureKind,
    SearchInvocationProvenance,
    SearchResult,
    SearchResultOccurrence,
    SearchStopReason,
)
from ecommerce_ai_os.search.serialization import (
    serialize_search_failure,
    serialize_search_result,
)


class SearchSerializationTests(unittest.TestCase):
    def test_rich_result_preserves_all_reviewed_search_facts(self) -> None:
        occurrence_a = SearchResultOccurrence(
            item_ref="item-a",
            source_ref="source-a",
            known_missing_fields=frozenset({"description"}),
            publication_time=datetime(
                2026,
                1,
                2,
                3,
                4,
                tzinfo=timezone(timedelta(hours=8)),
            ),
            observation_time=datetime(2026, 1, 2, 5, 6, tzinfo=UTC),
        )
        occurrence_b = SearchResultOccurrence(
            item_ref="item-b",
            source_ref="source-b",
            known_missing_fields=frozenset({"transcript", "description"}),
        )
        result = SearchResult(
            search_result_id="search-rich-serialization",
            returned_item_count=3,
            occurrences=(occurrence_a, occurrence_b, occurrence_a),
            requested_item_count=5,
            stopping_reason=SearchStopReason.LIMITATION_REACHED,
            continuation=ContinuationState.AVAILABLE,
            completion=SearchCompletionState.KNOWN_INCOMPLETE,
            provider_exhaustion=ProviderExhaustionState.NOT_EXHAUSTED,
            global_completeness=GlobalCompletenessState.UNKNOWN,
            limitations=("Only a bounded provider traversal was observed.",),
            collection_time=datetime(
                2026,
                1,
                2,
                1,
                0,
                tzinfo=timezone(timedelta(hours=-5)),
            ),
            provenance=SearchInvocationProvenance(
                resolved_provider_ref="provider-binding:search",
                used_provider_ref="provider-invocation:search",
                capability_result_ref="capability-result:search-rich-serialization",
                raw_result_refs=(
                    RawProviderResultRef("provider_raw/page-1.json"),
                    RawProviderResultRef("provider_raw/page-2.json"),
                ),
            ),
        )

        payload = serialize_search_result(result)

        self.assertEqual(
            payload,
            {
                "schema_version": 1,
                "search_result_id": "search-rich-serialization",
                "returned_item_count": 3,
                "occurrences": [
                    {
                        "item_ref": "item-a",
                        "source_ref": "source-a",
                        "known_missing_fields": ["description"],
                        "publication_time": "2026-01-01T19:04:00+00:00",
                        "observation_time": "2026-01-02T05:06:00+00:00",
                    },
                    {
                        "item_ref": "item-b",
                        "source_ref": "source-b",
                        "known_missing_fields": ["description", "transcript"],
                        "publication_time": None,
                        "observation_time": None,
                    },
                    {
                        "item_ref": "item-a",
                        "source_ref": "source-a",
                        "known_missing_fields": ["description"],
                        "publication_time": "2026-01-01T19:04:00+00:00",
                        "observation_time": "2026-01-02T05:06:00+00:00",
                    },
                ],
                "requested_item_count": 5,
                "stopping_reason": "limitation_reached",
                "continuation": "available",
                "completion": "known_incomplete",
                "provider_exhaustion": "not_exhausted",
                "global_completeness": "unknown",
                "limitations": ["Only a bounded provider traversal was observed."],
                "collection_time": "2026-01-02T06:00:00+00:00",
                "provenance": {
                    "resolved_provider_ref": "provider-binding:search",
                    "used_provider_ref": "provider-invocation:search",
                    "capability_result_ref": (
                        "capability-result:search-rich-serialization"
                    ),
                    "raw_result_refs": [
                        {"reference_id": "provider_raw/page-1.json"},
                        {"reference_id": "provider_raw/page-2.json"},
                    ],
                },
            },
        )
        self.assertEqual(
            [occurrence["item_ref"] for occurrence in payload["occurrences"]],
            ["item-a", "item-b", "item-a"],
        )
        serialized_json = json.dumps(payload)
        self.assertNotIn("raw_payload", serialized_json)
        self.assertNotIn("api_key", serialized_json)

    def test_valid_empty_result_serializes_zero_without_invented_facts(self) -> None:
        result = SearchResult(
            search_result_id="search-empty",
            returned_item_count=0,
            requested_item_count=4,
            stopping_reason=SearchStopReason.NO_MATCHES,
            continuation=ContinuationState.UNAVAILABLE,
            completion=SearchCompletionState.COMPLETE_FOR_REQUEST,
            provider_exhaustion=ProviderExhaustionState.EXHAUSTED,
        )

        payload = serialize_search_result(result)

        self.assertEqual(payload["returned_item_count"], 0)
        self.assertEqual(payload["occurrences"], [])
        self.assertEqual(payload["requested_item_count"], 4)
        self.assertEqual(payload["stopping_reason"], "no_matches")
        self.assertEqual(payload["collection_time"], None)
        self.assertEqual(
            payload["provenance"],
            {
                "resolved_provider_ref": None,
                "used_provider_ref": None,
                "capability_result_ref": None,
                "raw_result_refs": [],
            },
        )

    def test_failure_serialization_preserves_typed_facts_and_provenance(self) -> None:
        failure = SearchFailure(
            kind=SearchFailureKind.PROVIDER_INVOCATION,
            failure_code="PROVIDER_REQUEST_FAILED",
            reason="the selected Provider invocation failed",
            provenance=SearchInvocationProvenance(
                resolved_provider_ref="provider-binding:search",
                used_provider_ref="provider-invocation:search",
                capability_result_ref="capability-failure:search",
                raw_result_refs=(
                    RawProviderResultRef("provider_raw/failure-page.json"),
                ),
            ),
        )

        payload = serialize_search_failure(failure)

        self.assertEqual(
            payload,
            {
                "schema_version": 1,
                "kind": "provider_invocation",
                "failure_code": "PROVIDER_REQUEST_FAILED",
                "reason": "the selected Provider invocation failed",
                "provenance": {
                    "resolved_provider_ref": "provider-binding:search",
                    "used_provider_ref": "provider-invocation:search",
                    "capability_result_ref": "capability-failure:search",
                    "raw_result_refs": [
                        {"reference_id": "provider_raw/failure-page.json"},
                    ],
                },
            },
        )
        self.assertEqual(
            payload["provenance"]["raw_result_refs"],
            [{"reference_id": "provider_raw/failure-page.json"}],
        )
        self.assertNotIn("raw_payload", json.dumps(payload))


if __name__ == "__main__":
    unittest.main()
