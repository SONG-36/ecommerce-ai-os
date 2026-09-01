import hashlib
import json
from pathlib import Path
import unittest


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
PROVENANCE_PATH = (
    REPOSITORY_ROOT
    / "docs"
    / "05_references"
    / "provider_lab"
    / "tt17"
    / "PROVENANCE.json"
)
EXPECTED_FIXTURES = {
    "region_us_page_01.json": {
        "sha256": "aaa15a37bd17f8e1f6cb0e648b6addf59d4fda89ed0938a12ae7fc9509f767e4",
        "cursor": 30,
        "has_more": 1,
        "empty_desc_count": 0,
    },
    "region_us_page_02.json": {
        "sha256": "f189caeb07e1197d6226025922a926feff9b8a06c23b2519ed69f4b7fa23430f",
        "cursor": 60,
        "has_more": 1,
        "empty_desc_count": 1,
    },
}
FORBIDDEN_SECURITY_MARKERS = (
    "x-api-key",
    "authorization",
    "bearer ",
    "access_token=",
)


class TT17FixtureIntegrityTests(unittest.TestCase):
    def load_fixture(self, name: str) -> tuple[bytes, dict[str, object]]:
        raw_bytes = (FIXTURE_ROOT / name).read_bytes()
        return raw_bytes, json.loads(raw_bytes)

    def test_fixture_hashes_match_provenance(self) -> None:
        provenance = json.loads(PROVENANCE_PATH.read_text(encoding="utf-8"))
        recorded_hashes = {
            Path(entry["canonical_fixture_path"]).name: entry[
                "canonical_fixture_sha256"
            ]
            for entry in provenance["request_sequence"]
            if entry["canonical_fixture_path"] is not None
        }

        for fixture_name, expected in EXPECTED_FIXTURES.items():
            raw_bytes = (FIXTURE_ROOT / fixture_name).read_bytes()
            observed_hash = hashlib.sha256(raw_bytes).hexdigest()
            self.assertEqual(observed_hash, expected["sha256"])
            self.assertEqual(recorded_hashes[fixture_name], observed_hash)

    def test_provider_shape_counts_pagination_and_missingness_are_preserved(
        self,
    ) -> None:
        for fixture_name, expected in EXPECTED_FIXTURES.items():
            _, payload = self.load_fixture(fixture_name)
            self.assertEqual(
                set(payload),
                {
                    "success",
                    "credits_remaining",
                    "credits_charged",
                    "search_item_list",
                    "cursor",
                    "has_more",
                },
            )
            self.assertIs(payload["success"], True)
            self.assertEqual(len(payload["search_item_list"]), 30)
            self.assertEqual(payload["cursor"], expected["cursor"])
            self.assertEqual(payload["has_more"], expected["has_more"])

            aweme_infos = [
                occurrence["aweme_info"]
                for occurrence in payload["search_item_list"]
            ]
            self.assertTrue(all("desc" in item for item in aweme_infos))
            self.assertEqual(
                sum(item["desc"] == "" for item in aweme_infos),
                expected["empty_desc_count"],
            )
            self.assertTrue(
                all(
                    "create_time" in item and item["create_time"] is not None
                    for item in aweme_infos
                )
            )

    def test_three_cross_page_duplicate_occurrences_are_preserved(self) -> None:
        _, page_1 = self.load_fixture("region_us_page_01.json")
        _, page_2 = self.load_fixture("region_us_page_02.json")
        page_1_ids = [
            occurrence["aweme_info"]["aweme_id"]
            for occurrence in page_1["search_item_list"]
        ]
        page_2_ids = [
            occurrence["aweme_info"]["aweme_id"]
            for occurrence in page_2["search_item_list"]
        ]
        duplicates = [
            item_id
            for item_id in page_1_ids
            for candidate_id in page_2_ids
            if item_id == candidate_id
        ]
        self.assertEqual(
            duplicates,
            [
                "7653888832630246670",
                "7671336292155788576",
                "7670400319616027918",
            ],
        )

    def test_no_obvious_secret_or_unsanitized_signed_url_value_remains(
        self,
    ) -> None:
        placeholders = {
            "x-signature": "REDACTED_X_SIGNATURE",
            "x-expires": "REDACTED_X_EXPIRES",
            "refresh_token": "REDACTED_REFRESH_TOKEN",
            "signaturev3": "REDACTED_SIGNATUREV3",
            "pt": "REDACTED_PT",
            "rc": "REDACTED_RC",
        }
        delimiters = ("?", "&", r"\\u0026", "%26", "%2526")
        separators = ("=", "%3D", "%253D")

        for fixture_name in EXPECTED_FIXTURES:
            text = (FIXTURE_ROOT / fixture_name).read_text(encoding="utf-8")
            lowered = text.lower()
            for marker in FORBIDDEN_SECURITY_MARKERS:
                self.assertNotIn(marker, lowered)
            for key, placeholder in placeholders.items():
                for delimiter in delimiters:
                    for separator in separators:
                        marker = f"{delimiter}{key}{separator}"
                        start = 0
                        while (index := text.find(marker, start)) != -1:
                            value_start = index + len(marker)
                            self.assertTrue(
                                text.startswith(placeholder, value_start),
                                f"unsanitized {key} in {fixture_name}",
                            )
                            start = value_start + len(placeholder)


if __name__ == "__main__":
    unittest.main()
