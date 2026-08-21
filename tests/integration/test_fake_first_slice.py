import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from ecommerce_ai_os.composition import build_fake_first_slice_runtime
from ecommerce_ai_os.research.car_vacuum_tiktok import (
    CarVacuumTikTokResearchSkill,
)
from ecommerce_ai_os.runtime.execution import (
    BusinessWorkRequest,
    PreExecutionRejection,
    TerminalReturn,
)
from ecommerce_ai_os.runtime.retention import LocalJsonRetention
from ecommerce_ai_os.runtime.task_runtime import TaskRuntime, _ExecutionAbort
from ecommerce_ai_os.search.models import (
    SearchInvocationContext,
    SearchRequest,
)


class ControlledSearchFailure:
    """Test-only non-result outcome for the established failure path."""


class ControlledFailureSearchCapability:
    def __init__(self) -> None:
        self.calls = 0
        self.last_context: SearchInvocationContext | None = None

    def search(
        self,
        request: SearchRequest,
        context: SearchInvocationContext,
    ) -> ControlledSearchFailure:
        del request
        self.calls += 1
        self.last_context = context
        return ControlledSearchFailure()


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

            with patch.object(
                runtime,
                "_run_research_skill",
                wraps=runtime._run_research_skill,
            ) as observed_skill_run:
                terminal_return = runtime.execute(request)

            self.assertIsInstance(terminal_return, TerminalReturn)
            established_context = observed_skill_run.call_args.args[0]
            self.assertIs(established_context.work_request, request)
            self.assertEqual(
                established_context.execution_id,
                terminal_return.execution_id,
            )
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

            serialized_record = json.dumps(record, sort_keys=True)
            self.assertNotIn("returned_item_count", serialized_record)
            self.assertNotIn("observation", serialized_record)
            self.assertNotIn("limitations", serialized_record)

            research_result = json.loads(
                (final_bundle / record["research_result_ref"]).read_text(
                    encoding="utf-8"
                )
            )
            self.assertIn("evidence_ids", research_result)
            self.assertNotIn("observation", research_result)

            retained_json = "\n".join(
                path.read_text(encoding="utf-8")
                for path in final_bundle.rglob("*.json")
            )
            self.assertNotIn("Scrape Creators", retained_json)
            self.assertNotIn("TT-17", retained_json)
            for secret_marker in (
                "SCRAPE_CREATORS_API_KEY",
                "Authorization",
                "Cookie",
                "api_key",
            ):
                self.assertNotIn(secret_marker, retained_json)

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

    def test_incomplete_request_is_rejected_before_execution_establishment(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            execution_root = Path(temporary_directory) / "executions"
            runtime = build_fake_first_slice_runtime(execution_root)
            request = BusinessWorkRequest(
                request_id="request-rejected-001",
                product_context="",
                market="US",
                platform="TikTok",
                business_goal="Commerce Content",
                research_question="What content patterns merit human review?",
            )

            with (
                patch.object(
                    runtime,
                    "_run_research_skill",
                    wraps=runtime._run_research_skill,
                ) as observed_skill_run,
                patch.object(
                    runtime,
                    "_invoke_search",
                    wraps=runtime._invoke_search,
                ) as observed_search_invocation,
            ):
                response = runtime.execute(request)

            self.assertIsInstance(response, PreExecutionRejection)
            self.assertFalse(hasattr(response, "execution_id"))
            self.assertFalse(hasattr(response, "record_ref"))
            observed_skill_run.assert_not_called()
            observed_search_invocation.assert_not_called()
            self.assertFalse(execution_root.exists())

    def test_established_failure_unwinds_privately_to_task_runtime_owner(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            execution_root = Path(temporary_directory) / "executions"
            controlled_failure = ControlledFailureSearchCapability()
            skill = CarVacuumTikTokResearchSkill(
                search_request=SearchRequest(query="car vacuum", market="US")
            )
            runtime = TaskRuntime(
                search_capability=controlled_failure,
                research_skill=skill,
                retention=LocalJsonRetention(execution_root),
            )
            request = BusinessWorkRequest(
                request_id="request-established-failure-001",
                product_context="Car Vacuum",
                market="US",
                platform="TikTok",
                business_goal="Commerce Content",
                research_question="What content patterns merit human review?",
            )

            with (
                patch.object(
                    runtime,
                    "_run_research_skill",
                    wraps=runtime._run_research_skill,
                ) as observed_skill_run,
                patch.object(
                    runtime,
                    "_abort_execution",
                    wraps=runtime._abort_execution,
                ) as observed_abort,
                self.assertRaisesRegex(
                    RuntimeError,
                    "failure reached TaskRuntime; failure terminalization is not "
                    "implemented in P2",
                ) as captured_owner_boundary,
            ):
                runtime.execute(request)

            established_context = observed_skill_run.call_args.args[0]
            self.assertTrue(established_context.execution_id)
            self.assertIs(established_context.work_request, request)
            self.assertEqual(controlled_failure.calls, 1)
            self.assertIsNotNone(controlled_failure.last_context)
            self.assertEqual(
                controlled_failure.last_context.execution_id,
                established_context.execution_id,
            )
            observed_abort.assert_called_once_with(established_context)
            self.assertNotIsInstance(captured_owner_boundary.exception, _ExecutionAbort)
            self.assertIsNone(captured_owner_boundary.exception.__context__)

            staging_bundle = (
                execution_root / ".staging" / established_context.execution_id
            )
            final_bundle = execution_root / established_context.execution_id
            self.assertTrue(staging_bundle.is_dir())
            self.assertEqual(len(list((staging_bundle / "inputs").glob("*.json"))), 1)
            self.assertFalse((staging_bundle / "execution_record.json").exists())
            self.assertFalse(final_bundle.exists())

    def test_sequential_executions_are_isolated_with_deterministic_fake_id(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            execution_root = Path(temporary_directory) / "executions"
            runtime = build_fake_first_slice_runtime(execution_root)
            request_a = BusinessWorkRequest(
                request_id="request-isolation-a",
                product_context="Car Vacuum A",
                market="US",
                platform="TikTok",
                business_goal="Commerce Content",
                research_question="Which fake patterns belong to execution A?",
            )
            request_b = BusinessWorkRequest(
                request_id="request-isolation-b",
                product_context="Car Vacuum B",
                market="US",
                platform="TikTok",
                business_goal="Commerce Content",
                research_question="Which fake patterns belong to execution B?",
            )

            with patch.object(
                runtime,
                "_run_research_skill",
                wraps=runtime._run_research_skill,
            ) as observed_skill_run:
                result_a = runtime.execute(request_a)
                result_b = runtime.execute(request_b)

            contexts = [call.args[0] for call in observed_skill_run.call_args_list]
            self.assertEqual(len(contexts), 2)
            self.assertIsNot(contexts[0], contexts[1])
            self.assertIs(contexts[0].work_request, request_a)
            self.assertIs(contexts[1].work_request, request_b)
            self.assertEqual(contexts[0].execution_id, result_a.execution_id)
            self.assertEqual(contexts[1].execution_id, result_b.execution_id)

            self.assertNotEqual(result_a.execution_id, result_b.execution_id)
            self.assertNotEqual(result_a.record_ref, result_b.record_ref)

            retention = LocalJsonRetention(execution_root)
            record_path_a = retention.resolve_record_ref(result_a.record_ref)
            record_path_b = retention.resolve_record_ref(result_b.record_ref)
            bundle_a = record_path_a.parent
            bundle_b = record_path_b.parent
            self.assertNotEqual(bundle_a, bundle_b)
            self.assertTrue(bundle_a.is_dir())
            self.assertTrue(bundle_b.is_dir())
            self.assertFalse((execution_root / ".staging" / result_a.execution_id).exists())
            self.assertFalse((execution_root / ".staging" / result_b.execution_id).exists())

            record_a = json.loads(record_path_a.read_text(encoding="utf-8"))
            record_b = json.loads(record_path_b.read_text(encoding="utf-8"))
            self.assertIn(request_a.request_id, record_a["work_request_ref"])
            self.assertNotIn(request_b.request_id, record_a["work_request_ref"])
            self.assertIn(request_b.request_id, record_b["work_request_ref"])
            self.assertNotIn(request_a.request_id, record_b["work_request_ref"])

            resolved_refs_a = {
                bundle_a / relative_ref
                for relative_ref in record_a["required_references"]
            }
            resolved_refs_b = {
                bundle_b / relative_ref
                for relative_ref in record_b["required_references"]
            }
            self.assertTrue(all(path.is_file() for path in resolved_refs_a))
            self.assertTrue(all(path.is_file() for path in resolved_refs_b))
            self.assertTrue(resolved_refs_a.isdisjoint(resolved_refs_b))

            expected_fake_ref = "search_results/wi1-fake-search-result.json"
            self.assertEqual(
                record_a["actual_participation"]["search_result_refs"],
                [expected_fake_ref],
            )
            self.assertEqual(
                record_b["actual_participation"]["search_result_refs"],
                [expected_fake_ref],
            )
            self.assertNotEqual(
                bundle_a / expected_fake_ref,
                bundle_b / expected_fake_ref,
            )
            self.assertNotEqual(
                record_a["actual_sample_boundary_ref"],
                record_b["actual_sample_boundary_ref"],
            )
            self.assertTrue(
                set(record_a["evidence_refs"]).isdisjoint(record_b["evidence_refs"])
            )
            self.assertNotEqual(
                record_a["research_result_ref"],
                record_b["research_result_ref"],
            )


if __name__ == "__main__":
    unittest.main()
