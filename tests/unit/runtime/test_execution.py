from dataclasses import FrozenInstanceError
import unittest

from ecommerce_ai_os.runtime.execution import BusinessWorkRequest


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


if __name__ == "__main__":
    unittest.main()
