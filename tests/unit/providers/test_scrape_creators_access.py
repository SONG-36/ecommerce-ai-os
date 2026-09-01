import ast
import hashlib
from pathlib import Path
import unittest

from ecommerce_ai_os.providers.scrape_creators.access import (
    ScrapeCreatorsAccess,
    ScrapeCreatorsAccessError,
)
from ecommerce_ai_os.providers.scrape_creators.models import (
    ScrapeCreatorsRawResponse,
    ScrapeCreatorsSearchKeywordRequest,
)


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
PRODUCTION_ROOT = (
    REPOSITORY_ROOT
    / "src"
    / "ecommerce_ai_os"
    / "providers"
    / "scrape_creators"
)
PAGE_1_REQUEST = ScrapeCreatorsSearchKeywordRequest(
    query="car vacuum",
    region="US",
)
PAGE_2_REQUEST = ScrapeCreatorsSearchKeywordRequest(
    query="car vacuum",
    region="US",
    cursor="30",
)
FIXTURES = {
    PAGE_1_REQUEST: (
        "region_us_page_01.json",
        "aaa15a37bd17f8e1f6cb0e648b6addf59d4fda89ed0938a12ae7fc9509f767e4",
    ),
    PAGE_2_REQUEST: (
        "region_us_page_02.json",
        "f189caeb07e1197d6226025922a926feff9b8a06c23b2519ed69f4b7fa23430f",
    ),
}


class FixtureScrapeCreatorsAccess:
    """Test-owned access implementation backed only by canonical fixtures."""

    def search_keyword(
        self,
        request: ScrapeCreatorsSearchKeywordRequest,
    ) -> ScrapeCreatorsRawResponse:
        try:
            fixture_name, _ = FIXTURES[request]
        except KeyError as error:
            raise ScrapeCreatorsAccessError(
                f"no canonical fixture for request: {request!r}"
            ) from error
        return ScrapeCreatorsRawResponse(
            body=(FIXTURE_ROOT / fixture_name).read_bytes()
        )


def acquire(
    access: ScrapeCreatorsAccess,
    request: ScrapeCreatorsSearchKeywordRequest,
) -> ScrapeCreatorsRawResponse:
    """Exercise the structural Protocol without introducing another seam."""
    return access.search_keyword(request)


class ScrapeCreatorsAccessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.access = FixtureScrapeCreatorsAccess()

    def assert_fixture_fidelity(
        self,
        request: ScrapeCreatorsSearchKeywordRequest,
    ) -> None:
        fixture_name, expected_sha256 = FIXTURES[request]
        expected_bytes = (FIXTURE_ROOT / fixture_name).read_bytes()

        response = acquire(self.access, request)

        self.assertIs(type(response), ScrapeCreatorsRawResponse)
        self.assertIs(type(response.body), bytes)
        self.assertEqual(response.body, expected_bytes)
        self.assertEqual(
            hashlib.sha256(response.body).hexdigest(),
            expected_sha256,
        )

    def test_first_provider_request_returns_exact_page_1_bytes(self) -> None:
        self.assertIsNone(PAGE_1_REQUEST.cursor)
        self.assert_fixture_fidelity(PAGE_1_REQUEST)

    def test_observed_cursor_request_returns_exact_page_2_bytes(self) -> None:
        self.assertEqual(PAGE_2_REQUEST.cursor, "30")
        self.assert_fixture_fidelity(PAGE_2_REQUEST)

    def test_unsupported_fixture_request_is_a_controlled_access_failure(self) -> None:
        unsupported = ScrapeCreatorsSearchKeywordRequest(
            query="car vacuum",
            region="US",
            cursor="60",
        )

        with self.assertRaisesRegex(
            ScrapeCreatorsAccessError,
            "no canonical fixture for request",
        ):
            acquire(self.access, unsupported)

    def test_access_result_remains_untouched_provider_payload_bytes(self) -> None:
        response = acquire(self.access, PAGE_1_REQUEST)

        self.assertTrue(response.body.startswith(b"{"))
        self.assertIn(b'"search_item_list"', response.body)

    def test_access_boundary_does_not_import_c3_runtime_or_research(self) -> None:
        forbidden_roots = {
            "ecommerce_ai_os.search",
            "ecommerce_ai_os.runtime",
            "ecommerce_ai_os.research",
        }
        violations: list[str] = []

        for source_path in (
            PRODUCTION_ROOT / "models.py",
            PRODUCTION_ROOT / "access.py",
        ):
            tree = ast.parse(source_path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                imported_module: str | None = None
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if any(
                            alias.name == root or alias.name.startswith(f"{root}.")
                            for root in forbidden_roots
                        ):
                            violations.append(f"{source_path.name}: {alias.name}")
                elif isinstance(node, ast.ImportFrom) and node.level == 0:
                    imported_module = node.module
                if imported_module is not None and any(
                    imported_module == root
                    or imported_module.startswith(f"{root}.")
                    for root in forbidden_roots
                ):
                    violations.append(
                        f"{source_path.name}: {imported_module}"
                    )

        self.assertEqual(violations, [])
        self.assertFalse((PRODUCTION_ROOT / "adapter.py").exists())
        self.assertFalse((PRODUCTION_ROOT / "http.py").exists())
        self.assertFalse((PRODUCTION_ROOT / "fake.py").exists())


if __name__ == "__main__":
    unittest.main()
