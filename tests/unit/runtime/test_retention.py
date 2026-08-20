import json
from pathlib import Path
import tempfile
import unittest

from ecommerce_ai_os.runtime.retention import LocalJsonRetention


class LocalJsonRetentionTests(unittest.TestCase):
    def test_record_ref_is_available_only_after_successful_publish(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            retention = LocalJsonRetention(Path(temporary_directory) / "executions")
            bundle = retention.begin_execution("execution-001")
            required_ref = bundle.write_json(
                "inputs/request-001.json",
                {"schema_version": 1, "request_id": "request-001"},
            )

            self.assertIsNone(bundle.record_ref)

            record_ref = bundle.publish(
                {
                    "schema_version": 1,
                    "execution_id": "execution-001",
                    "terminal_outcome": "SUCCEEDED",
                    "required_references": [required_ref],
                },
                [required_ref],
            )

            self.assertIs(bundle.record_ref, record_ref)
            self.assertEqual(
                retention.resolve_record_ref(record_ref).name,
                "execution_record.json",
            )

    def test_missing_required_reference_rejects_publish(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory) / "executions"
            bundle = LocalJsonRetention(root).begin_execution("execution-002")

            with self.assertRaisesRegex(
                RuntimeError,
                "required execution references do not resolve",
            ):
                bundle.publish(
                    {
                        "schema_version": 1,
                        "execution_id": "execution-002",
                        "terminal_outcome": "SUCCEEDED",
                        "required_references": ["inputs/missing.json"],
                    },
                    ["inputs/missing.json"],
                )

            self.assertIsNone(bundle.record_ref)
            self.assertFalse((root / "execution-002").exists())
            self.assertTrue(
                (root / ".staging" / "execution-002" / "execution_record.json").is_file()
            )

    def test_terminal_c6_record_resolves_every_required_reference(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory) / "executions"
            retention = LocalJsonRetention(root)
            bundle = retention.begin_execution("execution-003")
            required_refs = (
                bundle.write_json("inputs/request.json", {"schema_version": 1}),
                bundle.write_json(
                    "search_results/result.json",
                    {"schema_version": 1},
                ),
                bundle.write_json(
                    "research_results/result.json",
                    {"schema_version": 1},
                ),
            )

            record_ref = bundle.publish(
                {
                    "schema_version": 1,
                    "execution_id": "execution-003",
                    "terminal_outcome": "SUCCEEDED",
                    "required_references": list(required_refs),
                },
                required_refs,
            )

            record_path = retention.resolve_record_ref(record_ref)
            record = json.loads(record_path.read_text(encoding="utf-8"))
            self.assertEqual(record["terminal_outcome"], "SUCCEEDED")
            for relative_ref in record["required_references"]:
                self.assertTrue((record_path.parent / relative_ref).is_file())


if __name__ == "__main__":
    unittest.main()
