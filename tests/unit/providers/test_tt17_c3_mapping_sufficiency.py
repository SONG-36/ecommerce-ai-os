import json
from dataclasses import fields
from datetime import UTC, datetime
from pathlib import Path
import unittest

from ecommerce_ai_os.search.models import (
    ContinuationState,
    GlobalCompletenessState,
    ProviderExhaustionState,
    RawProviderResultRef,
    SearchCompletionState,
    SearchInvocationProvenance,
    SearchRequest,
    SearchResult,
    SearchResultOccurrence,
    SearchStopReason,
)
from ecommerce_ai_os.search.serialization import serialize_search_result


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = (
    REPOSITORY_ROOT
    / "tests"
    / "fixtures"
    / "providers"
    / "scrape_creators"
    / "tt17"
    / "search_keyword"
)
FIXTURE_NAMES = (
    "region_us_page_01.json",
    "region_us_page_02.json",
)
RAW_REFERENCE_IDS = (
    "tt17:region-us:page-01:sha256:aaa15a37bd17f8e1f6cb0e648b6addf59d4fda89ed0938a12ae7fc9509f767e4",
    "tt17:region-us:page-02:sha256:f189caeb07e1197d6226025922a926feff9b8a06c23b2519ed69f4b7fa23430f",
)
EXPLICIT_LIMITATIONS = (
    "region=US is request context, not proof of exact regional effect",
    "has_more=1 proves continuation availability only",
    "provider exhaustion and pagination termination are unknown",
    "provider hard cap, global completeness, and full enumeration are unknown",
    "date_posted, sort_by, and ranking semantics or stability are unknown",
    "the recovered fixtures do not contain an exact observation timestamp",
)


class TT17C3MappingSufficiencyTests(unittest.TestCase):
    def load_pages(self) -> tuple[dict[str, object], ...]:
        return tuple(
            json.loads((FIXTURE_ROOT / name).read_text(encoding="utf-8"))
            for name in FIXTURE_NAMES
        )

    def aweme_infos(self) -> list[dict[str, object]]:
        return [
            occurrence["aweme_info"]
            for page in self.load_pages()
            for occurrence in page["search_item_list"]
        ]

    def characterize_existing_c3_projection(self) -> SearchResult:
        occurrences = tuple(
            SearchResultOccurrence(
                item_ref=aweme_info["aweme_id"],
                source_ref=aweme_info["url"],
                # Every fixture occurrence contains desc. One value is the
                # provider-observed empty string, which is not known missingness.
                known_missing_fields=frozenset(),
                publication_time=datetime.fromtimestamp(
                    aweme_info["create_time"], UTC
                ),
                # Neither fixture nor provenance contains an exact observation
                # timestamp, so the characterization must not invent one.
                observation_time=None,
            )
            for aweme_info in self.aweme_infos()
        )
        return SearchResult(
            search_result_id="tt17-fixture-c3-sufficiency",
            returned_item_count=len(occurrences),
            occurrences=occurrences,
            requested_item_count=60,
            stopping_reason=SearchStopReason.REQUEST_BOUND_SATISFIED,
            continuation=ContinuationState.AVAILABLE,
            completion=SearchCompletionState.COMPLETE_FOR_REQUEST,
            provider_exhaustion=ProviderExhaustionState.UNKNOWN,
            global_completeness=GlobalCompletenessState.UNKNOWN,
            limitations=EXPLICIT_LIMITATIONS,
            collection_time=None,
            provenance=SearchInvocationProvenance(
                resolved_provider_ref="scrape-creators",
                used_provider_ref="scrape-creators",
                capability_result_ref="tt17-fixture-c3-sufficiency",
                raw_result_refs=tuple(
                    RawProviderResultRef(reference_id=reference_id)
                    for reference_id in RAW_REFERENCE_IDS
                ),
            ),
        )

    def test_fixture_characterization_preserves_observed_provider_facts(self) -> None:
        pages = self.load_pages()
        self.assertEqual([len(page["search_item_list"]) for page in pages], [30, 30])
        self.assertEqual([page["cursor"] for page in pages], [30, 60])
        self.assertEqual([page["has_more"] for page in pages], [1, 1])

        aweme_infos = self.aweme_infos()
        item_ids = [aweme_info["aweme_id"] for aweme_info in aweme_infos]
        self.assertTrue(all(isinstance(item_id, str) for item_id in item_ids))
        self.assertEqual(
            [
                item_id
                for index, item_id in enumerate(item_ids)
                if item_id in item_ids[:index]
            ],
            [
                "7653888832630246670",
                "7670400319616027918",
                "7671336292155788576",
            ],
        )

        self.assertTrue(all("desc" in aweme_info for aweme_info in aweme_infos))
        self.assertFalse(any(aweme_info["desc"] is None for aweme_info in aweme_infos))
        self.assertEqual(
            sum(aweme_info["desc"] == "" for aweme_info in aweme_infos),
            1,
        )
        self.assertTrue(
            all(
                isinstance(aweme_info["create_time"], int)
                for aweme_info in aweme_infos
            )
        )
        self.assertTrue(
            all(
                aweme_info["statistics"]["aweme_id"]
                == aweme_info["aweme_id"]
                for aweme_info in aweme_infos
            )
        )
        self.assertTrue(
            all(
                aweme_info["aweme_id"] in aweme_info["url"]
                for aweme_info in aweme_infos
            )
        )

        self.assertTrue(
            all(
                isinstance(aweme_info["author"]["uid"], str)
                for aweme_info in aweme_infos
            )
        )
        self.assertEqual(
            sum(
                str(aweme_info["author_user_id"])
                != aweme_info["author"]["uid"]
                for aweme_info in aweme_infos
            ),
            59,
        )

    def test_current_c3_represents_required_projection_without_false_strengthening(
        self,
    ) -> None:
        request = SearchRequest(
            query="car vacuum",
            market="US",
            platform="tiktok",
            requested_item_count=60,
        )
        result = self.characterize_existing_c3_projection()
        aweme_infos = self.aweme_infos()

        self.assertEqual(request.market, "US")
        self.assertEqual(result.returned_item_count, 60)
        self.assertEqual(
            [occurrence.item_ref for occurrence in result.occurrences],
            [aweme_info["aweme_id"] for aweme_info in aweme_infos],
        )
        self.assertEqual(
            [occurrence.source_ref for occurrence in result.occurrences],
            [aweme_info["url"] for aweme_info in aweme_infos],
        )
        self.assertEqual(
            [occurrence.publication_time for occurrence in result.occurrences],
            [
                datetime.fromtimestamp(aweme_info["create_time"], UTC)
                for aweme_info in aweme_infos
            ],
        )
        self.assertTrue(
            all(
                not occurrence.known_missing_fields
                for occurrence in result.occurrences
            )
        )
        self.assertTrue(
            all(occurrence.observation_time is None for occurrence in result.occurrences)
        )
        self.assertIsNone(result.collection_time)
        self.assertIs(result.continuation, ContinuationState.AVAILABLE)
        self.assertIs(result.provider_exhaustion, ProviderExhaustionState.UNKNOWN)
        self.assertIs(result.global_completeness, GlobalCompletenessState.UNKNOWN)
        self.assertEqual(
            tuple(ref.reference_id for ref in result.provenance.raw_result_refs),
            RAW_REFERENCE_IDS,
        )

    def test_provider_only_shape_remains_behind_opaque_raw_references(self) -> None:
        result = self.characterize_existing_c3_projection()
        retained = serialize_search_result(result)
        occurrence_field_names = {field.name for field in fields(SearchResultOccurrence)}

        self.assertEqual(
            occurrence_field_names,
            {
                "item_ref",
                "source_ref",
                "known_missing_fields",
                "publication_time",
                "observation_time",
            },
        )
        provider_only_names = {
            "desc",
            "statistics",
            "author",
            "author_user_id",
            "video",
            "cursor",
            "has_more",
            "region",
        }
        self.assertTrue(provider_only_names.isdisjoint(retained))
        self.assertTrue(
            all(
                provider_only_names.isdisjoint(occurrence)
                for occurrence in retained["occurrences"]
            )
        )
        self.assertEqual(
            retained["provenance"]["raw_result_refs"],
            [{"reference_id": reference_id} for reference_id in RAW_REFERENCE_IDS],
        )


if __name__ == "__main__":
    unittest.main()
