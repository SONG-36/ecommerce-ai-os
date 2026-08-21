"""Thin stdlib CLI for the WI-1 Fake First-Slice execution."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence
from uuid import uuid4

from ecommerce_ai_os.composition import build_fake_first_slice_runtime
from ecommerce_ai_os.runtime.execution import (
    BusinessWorkRequest,
    PreExecutionRejection,
)


def build_parser() -> argparse.ArgumentParser:
    """Build the narrow operator-facing First-Slice argument parser."""
    parser = argparse.ArgumentParser(description="Run the WI-1 Fake research slice")
    parser.add_argument("--request-id", default=f"request-{uuid4()}")
    parser.add_argument("--product-context", default="Car Vacuum")
    parser.add_argument("--market", default="US")
    parser.add_argument("--platform", default="TikTok")
    parser.add_argument("--business-goal", default="Commerce Content")
    parser.add_argument(
        "--research-question",
        default="What content patterns merit human review?",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("var/executions"),
        help="First-Slice execution bundle root",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Map CLI input to C1 and present the successful terminal return."""
    args = build_parser().parse_args(argv)
    work_request = BusinessWorkRequest(
        request_id=args.request_id,
        product_context=args.product_context,
        market=args.market,
        platform=args.platform,
        business_goal=args.business_goal,
        research_question=args.research_question,
    )
    runtime = build_fake_first_slice_runtime(args.output_root)
    response = runtime.execute(work_request)
    if isinstance(response, PreExecutionRejection):
        print(f"Request Rejected: {response.reason}")
        return 1

    result = response.business_result
    print(f"Execution Outcome: {response.execution_outcome}")
    print(f"Execution ID: {response.execution_id}")
    print(
        "Research Result: "
        f"{len(result.evidence)} synthetic evidence item(s); "
        f"sample size {result.actual_sample_boundary.returned_item_count}"
    )
    print(f"Record Ref: {response.record_ref}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
