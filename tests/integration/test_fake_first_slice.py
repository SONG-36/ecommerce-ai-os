import json
from pathlib import Path
import tempfile
import unittest

from ecommerce_ai_os.composition import build_fake_first_slice_runtime
from ecommerce_ai_os.runtime.execution import BusinessWorkRequest, TerminalReturn
from ecommerce_ai_os.runtime.retention import LocalJsonRetention


class FakeFirstSliceIntegrationTests(unittest.TestCase):
    def test_successful_fake_execution_publishes_resolvable_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            execution_root = Path(temporary_directory) / "executions"
            runtime = build_fake_first_slice_runtime(execution_root)
            request = BusinessWorkRequest(
                request_id="request-integration-001",
                product_context="Car Vacuum",
                market="US",
                platform="TikTok",
                business_goal="Commerce Content",
                research_question="What content patterns merit human review?",
            )

            terminal_return = runtime.execute(request)

            self.assertIsInstance(terminal_return, TerminalReturn)
            self.assertEqual(terminal_return.execution_outcome, "SUCCEEDED")
            self.assertIsNotNone(terminal_return.business_result)
            self.assertIsNotNone(terminal_return.record_ref)

            retention = LocalJsonRetention(execution_root)
            record_path = retention.resolve_record_ref(terminal_return.record_ref)
            final_bundle = record_path.parent
            staging_bundle = (
                execution_root / ".staging" / terminal_return.execution_id
            )

            self.assertTrue(final_bundle.is_dir())
            self.assertFalse(staging_bundle.exists())
            self.assertTrue(record_path.is_file())
            self.assertEqual(len(list((final_bundle / "inputs").glob("*.json"))), 1)
            self.assertEqual(
                len(list((final_bundle / "search_results").glob("*.json"))),
                1,
            )
            self.assertEqual(
                len(list((final_bundle / "sample_boundaries").glob("*.json"))),
                1,
            )
            self.assertEqual(len(list((final_bundle / "evidence").glob("*.json"))), 1)
            self.assertEqual(
                len(list((final_bundle / "research_results").glob("*.json"))),
                1,
            )
            self.assertFalse((final_bundle / "provider_raw").exists())

            record = json.loads(record_path.read_text(encoding="utf-8"))
            self.assertEqual(record["terminal_outcome"], "SUCCEEDED")
            self.assertEqual(record["actual_participation"]["capabilities"], ["Search"])
            for relative_ref in record["required_references"]:
                self.assertTrue((final_bundle / relative_ref).is_file())

            retained_json = "\n".join(
                path.read_text(encoding="utf-8")
                for path in final_bundle.rglob("*.json")
            )
            self.assertNotIn("Scrape Creators", retained_json)
            self.assertNotIn("TT-17", retained_json)

            second_return = runtime.execute(
                BusinessWorkRequest(
                    request_id="request-integration-002",
                    product_context=request.product_context,
                    market=request.market,
                    platform=request.platform,
                    business_goal=request.business_goal,
                    research_question=request.research_question,
                )
            )
            self.assertNotEqual(
                second_return.execution_id,
                terminal_return.execution_id,
            )


if __name__ == "__main__":
    unittest.main()
