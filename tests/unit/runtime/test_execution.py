from dataclasses import FrozenInstanceError
from typing import get_args
import unittest

from ecommerce_ai_os.runtime.execution import (
    BusinessWorkRequest,
    PreExecutionRejection,
    TaskExecutionResponse,
    TerminalReturn,
)
from ecommerce_ai_os.runtime.execution_record import ExecutionRecordRef


class BusinessWorkRequestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.request = BusinessWorkRequest(
            request_id="request-001",
            product_context="Car Vacuum",
            market="US",
            platform="TikTok",
            business_goal="Commerce Content",
            research_question="What content patterns merit human review?",
        )

    def test_represents_the_first_slice_business_context(self) -> None:
        self.assertEqual(self.request.product_context, "Car Vacuum")
        self.assertEqual(self.request.market, "US")
        self.assertEqual(self.request.platform, "TikTok")
        self.assertEqual(self.request.business_goal, "Commerce Content")
        self.assertFalse(hasattr(self.request, "execution_id"))

    def test_is_a_frozen_stable_value(self) -> None:
        with self.assertRaises(FrozenInstanceError):
            self.request.market = "CA"  # type: ignore[misc]

    def test_c1_response_family_distinguishes_rejection_from_terminal_return(
        self,
    ) -> None:
        rejection = PreExecutionRejection(
            reason="required First-Slice request context is incomplete"
        )

        self.assertEqual(
            set(get_args(TaskExecutionResponse)),
            {PreExecutionRejection, TerminalReturn},
        )
        self.assertIsInstance(rejection, PreExecutionRejection)
        self.assertNotIsInstance(rejection, TerminalReturn)
        self.assertFalse(hasattr(rejection, "execution_id"))
        self.assertFalse(hasattr(rejection, "record_ref"))

    def test_terminal_return_allows_failure_without_a_business_result(self) -> None:
        terminal_return = TerminalReturn(
            execution_id="execution-failed-001",
            execution_outcome="FAILED",
            business_result=None,
            record_ref=ExecutionRecordRef(execution_id="execution-failed-001"),
        )

        self.assertIsNone(terminal_return.business_result)
        self.assertEqual(terminal_return.execution_outcome, "FAILED")
        self.assertIsInstance(terminal_return, TerminalReturn)
        self.assertNotIsInstance(terminal_return, PreExecutionRejection)


if __name__ == "__main__":
    unittest.main()
