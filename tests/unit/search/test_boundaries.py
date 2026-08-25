from dataclasses import FrozenInstanceError, fields
from datetime import UTC, datetime, timedelta, timezone
from typing import get_type_hints
import unittest

from ecommerce_ai_os.search.fake import FakeSearchCapability
from ecommerce_ai_os.search.models import (
    ContinuationState,
    GlobalCompletenessState,
    ProviderExhaustionState,
    RawProviderResultRef,
    SearchCompletionState,
    SearchFailure,
    SearchFailureKind,
    SearchInvocationContext,
    SearchInvocationProvenance,
    SearchRequest,
    SearchResult,
    SearchResultOccurrence,
    SearchStopReason,
)
from ecommerce_ai_os.search.port import SearchCapability


class StubSearchCapability:
    def search(
        self,
        request: SearchRequest,
        context: SearchInvocationContext,
    ) -> SearchResult:
        del context
        return SearchResult(
            search_result_id=f"search-{request.market}",
            returned_item_count=2,
            occurrences=(
                SearchResultOccurrence(
                    item_ref="stub-item-1",
                    source_ref="stub-source-1",
                ),
                SearchResultOccurrence(
                    item_ref="stub-item-2",
                    source_ref="stub-source-2",
                ),
            ),
        )


def invoke_search(
    capability: SearchCapability,
    request: SearchRequest,
) -> SearchResult | SearchFailure:
    return capability.search(
        request,
        SearchInvocationContext(execution_id="execution-001"),
    )


def make_occurrences(count: int) -> tuple[SearchResultOccurrence, ...]:
    return tuple(
        SearchResultOccurrence(
            item_ref=f"item-{index}",
            source_ref=f"source-{index}",
        )
        for index in range(1, count + 1)
    )


class SearchBoundaryTests(unittest.TestCase):
    def test_request_is_frozen_provider_neutral_and_can_be_bounded(self) -> None:
        request = SearchRequest(
            query="car vacuum",
            market="US",
            platform="TikTok",
            requested_item_count=30,
        )

        self.assertEqual(request.requested_item_count, 30)
        self.assertEqual(
            {field.name for field in fields(SearchRequest)},
            {"query", "market", "platform", "requested_item_count"},
        )
        with self.assertRaises(FrozenInstanceError):
            request.market = "CA"  # type: ignore[misc]

    def test_result_preserves_bounded_retrieval_states(self) -> None:
        occurrences = make_occurrences(12)
        result = SearchResult(
            search_result_id="search-partial",
            returned_item_count=12,
            occurrences=occurrences,
            requested_item_count=30,
            stopping_reason=SearchStopReason.LIMITATION_REACHED,
            continuation=ContinuationState.UNKNOWN,
            completion=SearchCompletionState.KNOWN_INCOMPLETE,
            provider_exhaustion=ProviderExhaustionState.UNKNOWN,
            limitations=("Only the observed bounded returned set is represented.",),
        )

        self.assertNotIsInstance(result, list)
        self.assertEqual(result.occurrences, occurrences)
        self.assertEqual(result.requested_item_count, 30)
        self.assertEqual(result.returned_item_count, 12)
        self.assertEqual(result.stopping_reason, SearchStopReason.LIMITATION_REACHED)
        self.assertEqual(result.continuation, ContinuationState.UNKNOWN)
        self.assertEqual(result.completion, SearchCompletionState.KNOWN_INCOMPLETE)
        self.assertEqual(
            result.provider_exhaustion,
            ProviderExhaustionState.UNKNOWN,
        )
        self.assertEqual(result.global_completeness, GlobalCompletenessState.UNKNOWN)

    def test_fake_returns_bound_satisfied_us_result_with_more_available(self) -> None:
        request = SearchRequest(
            query="car vacuum",
            market="US",
            platform="TikTok",
            requested_item_count=30,
        )
        expected_result = SearchResult(
            search_result_id="search-bound-satisfied",
            returned_item_count=30,
            occurrences=make_occurrences(30),
            requested_item_count=30,
            stopping_reason=SearchStopReason.REQUEST_BOUND_SATISFIED,
            continuation=ContinuationState.AVAILABLE,
            completion=SearchCompletionState.COMPLETE_FOR_REQUEST,
            provider_exhaustion=ProviderExhaustionState.NOT_EXHAUSTED,
            global_completeness=GlobalCompletenessState.UNKNOWN,
            limitations=(
                "US was requested; the bounded returned set does not establish "
                "exact US population membership or complete market coverage.",
            ),
        )

        actual_result = invoke_search(
            FakeSearchCapability(configured_result=expected_result),
            request,
        )

        self.assertIs(actual_result, expected_result)
        self.assertEqual(request.market, "US")
        self.assertEqual(actual_result.requested_item_count, 30)
        self.assertEqual(actual_result.returned_item_count, 30)
        self.assertEqual(
            actual_result.stopping_reason,
            SearchStopReason.REQUEST_BOUND_SATISFIED,
        )
        self.assertEqual(actual_result.continuation, ContinuationState.AVAILABLE)
        self.assertEqual(
            actual_result.completion,
            SearchCompletionState.COMPLETE_FOR_REQUEST,
        )
        self.assertEqual(
            actual_result.provider_exhaustion,
            ProviderExhaustionState.NOT_EXHAUSTED,
        )
        self.assertEqual(
            actual_result.global_completeness,
            GlobalCompletenessState.UNKNOWN,
        )
        self.assertIn("bounded", actual_result.limitations[0])

    def test_duplicate_occurrences_remain_ordered_without_dedupe(self) -> None:
        occurrence_a = SearchResultOccurrence(
            item_ref="item-a",
            source_ref="source-a",
            known_missing_fields=frozenset({"description"}),
        )
        occurrence_b = SearchResultOccurrence(
            item_ref="item-b",
            source_ref="source-b",
        )
        expected_result = SearchResult(
            search_result_id="search-duplicates",
            returned_item_count=3,
            occurrences=(occurrence_a, occurrence_b, occurrence_a),
        )
        actual_result = invoke_search(
            FakeSearchCapability(configured_result=expected_result),
            SearchRequest(query="car vacuum", market="US"),
        )

        self.assertEqual(
            tuple(occurrence.item_ref for occurrence in actual_result.occurrences),
            ("item-a", "item-b", "item-a"),
        )
        self.assertIs(actual_result, expected_result)
        self.assertEqual(actual_result.returned_item_count, 3)
        self.assertEqual(len(actual_result.occurrences), 3)
        self.assertEqual(
            actual_result.occurrences[0].known_missing_fields,
            frozenset({"description"}),
        )
        self.assertIs(actual_result.occurrences[0], actual_result.occurrences[2])

    def test_known_missingness_is_explicit_without_a_fake_value(self) -> None:
        occurrence = SearchResultOccurrence(
            item_ref="item-a",
            source_ref="source-a",
            known_missing_fields=frozenset({"description"}),
        )

        self.assertIn("description", occurrence.known_missing_fields)
        self.assertNotIn("description", {field.name for field in fields(occurrence)})

    def test_valid_empty_result_is_not_a_search_failure(self) -> None:
        result = SearchResult(
            search_result_id="search-empty",
            returned_item_count=0,
            requested_item_count=10,
            stopping_reason=SearchStopReason.NO_MATCHES,
            continuation=ContinuationState.UNAVAILABLE,
            completion=SearchCompletionState.COMPLETE_FOR_REQUEST,
            provider_exhaustion=ProviderExhaustionState.UNKNOWN,
        )

        self.assertEqual(result.occurrences, ())
        self.assertNotIsInstance(result, SearchFailure)

    def test_provider_exhaustion_before_max_can_complete_bounded_request(self) -> None:
        result = SearchResult(
            search_result_id="search-provider-exhausted",
            returned_item_count=42,
            occurrences=make_occurrences(42),
            requested_item_count=100,
            stopping_reason=SearchStopReason.CONTINUATION_UNAVAILABLE,
            continuation=ContinuationState.UNAVAILABLE,
            completion=SearchCompletionState.COMPLETE_FOR_REQUEST,
            provider_exhaustion=ProviderExhaustionState.EXHAUSTED,
            global_completeness=GlobalCompletenessState.UNKNOWN,
        )

        self.assertEqual(result.requested_item_count, 100)
        self.assertEqual(result.returned_item_count, 42)
        self.assertEqual(
            result.stopping_reason,
            SearchStopReason.CONTINUATION_UNAVAILABLE,
        )
        self.assertEqual(result.continuation, ContinuationState.UNAVAILABLE)
        self.assertEqual(result.completion, SearchCompletionState.COMPLETE_FOR_REQUEST)
        self.assertEqual(
            result.provider_exhaustion,
            ProviderExhaustionState.EXHAUSTED,
        )
        self.assertEqual(result.global_completeness, GlobalCompletenessState.UNKNOWN)

    def test_available_continuation_rejects_exhausted_provider(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "AVAILABLE.*EXHAUSTED",
        ):
            SearchResult(
                search_result_id="search-contradictory-continuation",
                returned_item_count=0,
                continuation=ContinuationState.AVAILABLE,
                provider_exhaustion=ProviderExhaustionState.EXHAUSTED,
            )

    def test_no_matches_rejects_nonzero_returned_count(self) -> None:
        with self.assertRaisesRegex(ValueError, "NO_MATCHES.*empty"):
            SearchResult(
                search_result_id="search-contradictory-no-matches",
                returned_item_count=1,
                occurrences=(
                    SearchResultOccurrence(
                        item_ref="item-a",
                        source_ref="source-a",
                    ),
                ),
                stopping_reason=SearchStopReason.NO_MATCHES,
            )

    def test_search_failure_is_a_distinct_frozen_c3_outcome(self) -> None:
        failure = SearchFailure(
            kind=SearchFailureKind.PROVIDER_RESOLUTION,
            failure_code="PROVIDER_NOT_RESOLVED",
            reason="No provider binding was resolved.",
        )

        self.assertNotIsInstance(failure, SearchResult)
        self.assertEqual(failure.kind, SearchFailureKind.PROVIDER_RESOLUTION)
        with self.assertRaises(FrozenInstanceError):
            failure.reason = "changed"  # type: ignore[misc]

    def test_publication_observation_and_collection_times_remain_distinct(self) -> None:
        plus_eight = timezone(timedelta(hours=8))
        occurrence = SearchResultOccurrence(
            item_ref="item-a",
            source_ref="source-a",
            publication_time=datetime(2026, 8, 20, 10, tzinfo=plus_eight),
            observation_time=datetime(2026, 8, 21, 10, tzinfo=plus_eight),
        )
        result = SearchResult(
            search_result_id="search-times",
            returned_item_count=1,
            occurrences=(occurrence,),
            collection_time=datetime(2026, 8, 21, 11, tzinfo=plus_eight),
        )

        self.assertEqual(occurrence.publication_time.tzinfo, UTC)
        self.assertEqual(occurrence.observation_time.tzinfo, UTC)
        self.assertEqual(result.collection_time.tzinfo, UTC)
        self.assertNotEqual(occurrence.publication_time, occurrence.observation_time)
        self.assertNotEqual(occurrence.observation_time, result.collection_time)

    def test_time_fields_reject_naive_datetimes(self) -> None:
        with self.assertRaisesRegex(ValueError, "publication_time.*timezone-aware"):
            SearchResultOccurrence(
                item_ref="item-a",
                source_ref="source-a",
                publication_time=datetime(2026, 8, 20, 10),
            )

        with self.assertRaisesRegex(ValueError, "collection_time.*timezone-aware"):
            SearchResult(
                search_result_id="search-times",
                returned_item_count=0,
                collection_time=datetime(2026, 8, 21, 11),
            )

    def test_invocation_context_is_narrow_and_carries_opaque_capture(self) -> None:
        captured: list[object] = []

        def capture(raw_response: object) -> RawProviderResultRef:
            captured.append(raw_response)
            return RawProviderResultRef(reference_id="raw-result-001")

        context = SearchInvocationContext(
            execution_id="execution-001",
            raw_result_capture=capture,
        )

        self.assertIsNotNone(context.raw_result_capture)
        raw_ref = context.raw_result_capture(b"bounded raw response")
        self.assertEqual(raw_ref.reference_id, "raw-result-001")
        self.assertEqual(captured, [b"bounded raw response"])
        self.assertEqual(
            {field.name for field in fields(SearchInvocationContext)},
            {"execution_id", "raw_result_capture"},
        )

    def test_invocation_provenance_preserves_actual_path_facts(self) -> None:
        provenance = SearchInvocationProvenance(
            resolved_provider_ref="provider-binding-001",
            used_provider_ref="provider-invocation-001",
            capability_result_ref="search-result-001",
            raw_result_refs=(RawProviderResultRef("raw-result-001"),),
        )

        self.assertEqual(provenance.resolved_provider_ref, "provider-binding-001")
        self.assertEqual(provenance.used_provider_ref, "provider-invocation-001")
        self.assertEqual(provenance.capability_result_ref, "search-result-001")
        self.assertEqual(
            provenance.raw_result_refs,
            (RawProviderResultRef("raw-result-001"),),
        )

        with self.assertRaisesRegex(
            ValueError,
            "used_provider_ref requires resolved_provider_ref",
        ):
            SearchInvocationProvenance(used_provider_ref="provider-invocation-001")

    def test_raw_result_refs_require_an_actually_used_provider(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "raw_result_refs require used_provider_ref",
        ):
            SearchInvocationProvenance(
                raw_result_refs=(RawProviderResultRef("raw-result-001"),),
            )

    def test_raw_provider_result_ref_is_reference_only(self) -> None:
        raw_ref = RawProviderResultRef(reference_id="raw-result-001")

        self.assertEqual(
            {field.name for field in fields(RawProviderResultRef)},
            {"reference_id"},
        )
        self.assertFalse(hasattr(raw_ref, "payload"))
        self.assertFalse(hasattr(raw_ref, "path"))
        with self.assertRaises(FrozenInstanceError):
            raw_ref.reference_id = "changed"  # type: ignore[misc]

    def test_provider_mechanics_do_not_leak_into_stable_models(self) -> None:
        stable_field_names = {
            field.name
            for model in (SearchRequest, SearchResult, SearchResultOccurrence)
            for field in fields(model)
        }

        self.assertTrue(
            {
                "cursor",
                "page",
                "api_key",
                "endpoint_path",
                "provider_page_token",
                "aweme_id",
            }.isdisjoint(stable_field_names)
        )

    def test_negative_counts_and_bounds_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "requested_item_count.*positive"):
            SearchRequest(
                query="car vacuum",
                market="US",
                requested_item_count=-1,
            )

        with self.assertRaisesRegex(ValueError, "returned_item_count.*negative"):
            SearchResult(search_result_id="search-001", returned_item_count=-1)

        with self.assertRaisesRegex(ValueError, "requested_item_count.*positive"):
            SearchResult(
                search_result_id="search-001",
                returned_item_count=0,
                requested_item_count=-1,
            )

    def test_result_count_must_match_explicit_occurrences(self) -> None:
        with self.assertRaisesRegex(ValueError, "must match"):
            SearchResult(
                search_result_id="search-001",
                returned_item_count=2,
                occurrences=(
                    SearchResultOccurrence(
                        item_ref="item-a",
                        source_ref="source-a",
                    ),
                ),
            )

    def test_nonzero_result_rejects_empty_occurrences(self) -> None:
        with self.assertRaisesRegex(ValueError, "must match"):
            SearchResult(
                search_result_id="search-001",
                returned_item_count=2,
                occurrences=(),
            )

    def test_structural_search_stub_satisfies_the_callable_seam(self) -> None:
        result = invoke_search(
            StubSearchCapability(),
            SearchRequest(query="car vacuum", market="US"),
        )

        self.assertIsInstance(result, SearchResult)
        self.assertEqual(result.returned_item_count, 2)
        hints = get_type_hints(SearchCapability.search)
        self.assertEqual(hints["context"], SearchInvocationContext)
        self.assertEqual(hints["return"], SearchResult | SearchFailure)


if __name__ == "__main__":
    unittest.main()
