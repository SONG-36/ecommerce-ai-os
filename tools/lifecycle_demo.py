#!/usr/bin/env python3
"""Developer-facing visualization of the verified WI-02 lifecycle."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import sys
import tempfile
from typing import Sequence
from unittest.mock import patch

from ecommerce_ai_os.composition import build_fake_first_slice_runtime
from ecommerce_ai_os.research.car_vacuum_tiktok import (
    CarVacuumTikTokResearchSkill,
)
from ecommerce_ai_os.research.models import ResearchCompletion
from ecommerce_ai_os.runtime.execution import (
    BusinessWorkRequest,
    PreExecutionRejection,
    TaskExecutionResponse,
    TerminalReturn,
)
from ecommerce_ai_os.runtime.execution_record import ExecutionRecordRef
from ecommerce_ai_os.runtime.retention import (
    LocalJsonRetention,
    StagingExecutionBundle,
)
from ecommerce_ai_os.runtime.task_runtime import TaskRuntime
from ecommerce_ai_os.search.models import SearchInvocationContext, SearchRequest


@dataclass(frozen=True, slots=True)
class SuccessScenarioResult:
    """Evidence-derived result used to render and verify the success scenario."""

    scenario: str
    execution_established: bool
    execution_id: str | None
    business_result_present: bool
    execution_outcome: str | None
    clean_closure: bool
    record_ref_present: bool
    record_ref: str | None
    record_ref_resolves: bool
    final_bundle_exists: bool
    required_reference_count: int
    required_references_resolve: bool
    c6_outcome: str | None
    c6_execution_matches: bool
    search_participated: bool
    success_staging_absent: bool
    evidence_root: Path


@dataclass(frozen=True, slots=True)
class RejectionScenarioResult:
    """Evidence-derived result used to render and verify rejection."""

    scenario: str
    response_is_rejection: bool
    response_type: str
    rejection_reason: str | None
    execution_established: bool
    execution_id_present: bool
    research_started: bool
    search_started: bool
    business_result_present: bool
    execution_outcome: str | None
    final_bundle_exists: bool
    c6_exists: bool
    record_ref_present: bool
    execution_artifacts_present: bool
    evidence_root: Path


class ControlledNonResult:
    """Demo-local outcome that is intentionally not a SearchResult."""


class ControlledFailureSearchCapability:
    """Demo-local Search double for the approved established-failure path."""

    def __init__(self) -> None:
        self.invocation_count = 0
        self.non_result_triggered = False
        self.last_context: SearchInvocationContext | None = None

    def search(
        self,
        request: SearchRequest,
        context: SearchInvocationContext,
    ) -> ControlledNonResult:
        del request
        self.invocation_count += 1
        self.non_result_triggered = True
        self.last_context = context
        return ControlledNonResult()


@dataclass(frozen=True, slots=True)
class ExecutionFailureScenarioResult:
    """Evidence-derived result used to render and verify execution failure."""

    scenario: str
    response_type: str
    execution_established: bool
    execution_id: str | None
    business_result_present: bool
    execution_outcome: str | None
    search_invocation_count: int
    controlled_non_result_observed: bool
    search_execution_matches: bool
    failure_recorded: bool
    failure_code: str | None
    failure_reason: str | None
    search_participated: bool
    c6_exists: bool
    c6_outcome: str | None
    c6_execution_matches: bool
    fabricated_research_facts: bool
    clean_closure: bool
    final_bundle_exists: bool
    record_ref_present: bool
    record_ref: str | None
    record_ref_resolves: bool
    required_reference_count: int
    required_references_resolve: bool
    failure_staging_absent: bool
    evidence_root: Path


@dataclass(frozen=True, slots=True)
class ClosureFailureScenarioResult:
    """Evidence-derived result used to render and verify closure failure."""

    scenario: str
    response_type: str
    execution_established: bool
    execution_id: str | None
    business_completed: bool
    business_result_present: bool
    business_result_preserved: bool
    business_completion_preceded_publication_failure: bool
    execution_outcome: str | None
    publication_attempt_count: int
    controlled_publication_failure_observed: bool
    attempted_c6_outcome: str | None
    attempted_research_result_matches: bool
    attempted_required_references_resolve: bool
    clean_closure: bool
    final_bundle_exists: bool
    final_execution_record_exists: bool
    staging_bundle_exists: bool
    staging_execution_record_exists: bool
    retained_input_present: bool
    retained_search_result_present: bool
    retained_sample_boundary_present: bool
    retained_evidence_present: bool
    retained_research_result_present: bool
    record_ref_present: bool
    hypothetical_record_ref_checked: bool
    hypothetical_record_ref_resolves: bool
    evidence_root: Path


DetailedScenarioResult = (
    SuccessScenarioResult
    | RejectionScenarioResult
    | ExecutionFailureScenarioResult
    | ClosureFailureScenarioResult
)


@dataclass(frozen=True, slots=True)
class ScenarioSummaryResult:
    """Compact actual result retained after temporary evidence cleanup."""

    scenario: str
    execution_established: bool
    business_result_present: bool
    execution_outcome: str | None
    record_ref_present: bool


def build_parser() -> argparse.ArgumentParser:
    """Build the currently authorized developer-tool command surface."""
    parser = argparse.ArgumentParser(
        description="Visualize an authorized WI-02 lifecycle scenario."
    )
    parser.add_argument(
        "scenario",
        help=(
            "Currently supported: success, rejection, execution-failure, "
            "closure-failure, all"
        ),
    )
    return parser


def build_success_request() -> BusinessWorkRequest:
    """Create the demo-owned valid request used by the real Runtime."""
    return BusinessWorkRequest(
        request_id="request-lifecycle-demo-success",
        product_context="Car Vacuum",
        market="US",
        platform="TikTok",
        business_goal="Commerce Content",
        research_question="What content patterns merit human review?",
    )


def build_rejection_request() -> BusinessWorkRequest:
    """Create a request that violates the existing required-context rule."""
    return BusinessWorkRequest(
        request_id="request-lifecycle-demo-rejection",
        product_context="",
        market="US",
        platform="TikTok",
        business_goal="Commerce Content",
        research_question="What content patterns merit human review?",
    )


def build_execution_failure_request() -> BusinessWorkRequest:
    """Create the valid request used for the controlled failure path."""
    return BusinessWorkRequest(
        request_id="request-lifecycle-demo-execution-failure",
        product_context="Car Vacuum",
        market="US",
        platform="TikTok",
        business_goal="Commerce Content",
        research_question="What content patterns merit human review?",
    )


def build_closure_failure_request() -> BusinessWorkRequest:
    """Create the valid request used for the controlled closure failure."""
    return BusinessWorkRequest(
        request_id="request-lifecycle-demo-closure-failure",
        product_context="Car Vacuum",
        market="US",
        platform="TikTok",
        business_goal="Commerce Content",
        research_question="What content patterns merit human review?",
    )


def build_execution_failure_runtime(
    execution_root: Path,
    controlled_search: ControlledFailureSearchCapability,
) -> TaskRuntime:
    """Compose the real Runtime with the demo-local controlled Search seam."""
    skill = CarVacuumTikTokResearchSkill(
        search_request=SearchRequest(query="car vacuum", market="US")
    )
    return TaskRuntime(
        search_capability=controlled_search,
        research_skill=skill,
        retention=LocalJsonRetention(execution_root),
    )


def derive_success_result(
    response: TaskExecutionResponse,
    execution_root: Path,
) -> SuccessScenarioResult:
    """Derive success facts from the public response and published artifacts."""
    if not isinstance(response, TerminalReturn):
        return SuccessScenarioResult(
            scenario="success",
            execution_established=False,
            execution_id=None,
            business_result_present=False,
            execution_outcome=None,
            clean_closure=False,
            record_ref_present=False,
            record_ref=None,
            record_ref_resolves=False,
            final_bundle_exists=False,
            required_reference_count=0,
            required_references_resolve=False,
            c6_outcome=None,
            c6_execution_matches=False,
            search_participated=False,
            success_staging_absent=True,
            evidence_root=execution_root,
        )

    record_ref_present = response.record_ref is not None
    record_ref_resolves = False
    final_bundle_exists = False
    required_reference_count = 0
    required_references_resolve = False
    c6_outcome: str | None = None
    c6_execution_matches = False
    search_participated = False

    if response.record_ref is not None:
        retention = LocalJsonRetention(execution_root)
        try:
            record_path = retention.resolve_record_ref(response.record_ref)
        except FileNotFoundError:
            record_path = None

        if record_path is not None:
            record_ref_resolves = record_path.is_file()
            final_bundle = record_path.parent
            final_bundle_exists = final_bundle.is_dir()
            record_payload = json.loads(record_path.read_text(encoding="utf-8"))

            c6_outcome_value = record_payload.get("terminal_outcome")
            if isinstance(c6_outcome_value, str):
                c6_outcome = c6_outcome_value

            c6_execution_matches = (
                record_payload.get("execution_id") == response.execution_id
            )
            required_references = record_payload.get("required_references")
            if isinstance(required_references, list) and all(
                isinstance(reference, str) for reference in required_references
            ):
                required_reference_count = len(required_references)
                required_references_resolve = bool(required_references) and all(
                    (final_bundle / reference).is_file()
                    for reference in required_references
                )

            actual_participation = record_payload.get("actual_participation")
            if isinstance(actual_participation, dict):
                capabilities = actual_participation.get("capabilities")
                search_participated = isinstance(capabilities, list) and (
                    "Search" in capabilities
                )

    success_staging_absent = not (
        execution_root / ".staging" / response.execution_id
    ).exists()
    clean_closure = all(
        (
            record_ref_present,
            record_ref_resolves,
            final_bundle_exists,
            required_references_resolve,
            c6_outcome == "SUCCEEDED",
            c6_execution_matches,
            success_staging_absent,
        )
    )

    return SuccessScenarioResult(
        scenario="success",
        execution_established=isinstance(response, TerminalReturn),
        execution_id=response.execution_id,
        business_result_present=response.business_result is not None,
        execution_outcome=response.execution_outcome,
        clean_closure=clean_closure,
        record_ref_present=record_ref_present,
        record_ref=str(response.record_ref) if response.record_ref is not None else None,
        record_ref_resolves=record_ref_resolves,
        final_bundle_exists=final_bundle_exists,
        required_reference_count=required_reference_count,
        required_references_resolve=required_references_resolve,
        c6_outcome=c6_outcome,
        c6_execution_matches=c6_execution_matches,
        search_participated=search_participated,
        success_staging_absent=success_staging_absent,
        evidence_root=execution_root,
    )


def success_mismatches(result: SuccessScenarioResult) -> tuple[str, ...]:
    """Compare observed facts with the reviewed success lifecycle shape."""
    expected = {
        "execution_established": True,
        "business_result_present": True,
        "execution_outcome": "SUCCEEDED",
        "clean_closure": True,
        "record_ref_present": True,
        "record_ref_resolves": True,
        "final_bundle_exists": True,
        "required_references_resolve": True,
        "c6_outcome": "SUCCEEDED",
        "c6_execution_matches": True,
        "search_participated": True,
        "success_staging_absent": True,
    }
    mismatches = []
    for field_name, expected_value in expected.items():
        observed_value = getattr(result, field_name)
        if observed_value != expected_value:
            mismatches.append(
                f"{field_name}: expected {expected_value!r}, observed {observed_value!r}"
            )
    return tuple(mismatches)


def derive_rejection_result(
    response: TaskExecutionResponse,
    execution_root: Path,
    *,
    research_started: bool,
    search_started: bool,
) -> RejectionScenarioResult:
    """Derive rejection facts from the public response and artifact root."""
    response_is_rejection = isinstance(response, PreExecutionRejection)
    execution_id = getattr(response, "execution_id", None)
    business_result = getattr(response, "business_result", None)
    execution_outcome = getattr(response, "execution_outcome", None)
    record_ref = getattr(response, "record_ref", None)

    execution_artifacts_present = execution_root.exists() and any(
        execution_root.iterdir()
    )
    final_bundle_exists = execution_root.exists() and any(
        child.is_dir() and child.name != ".staging"
        for child in execution_root.iterdir()
    )
    c6_exists = execution_root.exists() and any(
        execution_root.rglob("execution_record.json")
    )

    return RejectionScenarioResult(
        scenario="rejection",
        response_is_rejection=response_is_rejection,
        response_type=type(response).__name__,
        rejection_reason=response.reason if response_is_rejection else None,
        execution_established=isinstance(response, TerminalReturn),
        execution_id_present=bool(execution_id),
        research_started=research_started,
        search_started=search_started,
        business_result_present=business_result is not None,
        execution_outcome=execution_outcome,
        final_bundle_exists=final_bundle_exists,
        c6_exists=c6_exists,
        record_ref_present=record_ref is not None,
        execution_artifacts_present=execution_artifacts_present,
        evidence_root=execution_root,
    )


def rejection_mismatches(result: RejectionScenarioResult) -> tuple[str, ...]:
    """Compare observed facts with the reviewed pre-execution shape."""
    expected = {
        "response_is_rejection": True,
        "execution_established": False,
        "execution_id_present": False,
        "research_started": False,
        "search_started": False,
        "business_result_present": False,
        "execution_outcome": None,
        "final_bundle_exists": False,
        "c6_exists": False,
        "record_ref_present": False,
        "execution_artifacts_present": False,
    }
    mismatches = []
    for field_name, expected_value in expected.items():
        observed_value = getattr(result, field_name)
        if observed_value != expected_value:
            mismatches.append(
                f"{field_name}: expected {expected_value!r}, observed {observed_value!r}"
            )
    return tuple(mismatches)


def derive_execution_failure_result(
    response: TaskExecutionResponse,
    execution_root: Path,
    controlled_search: ControlledFailureSearchCapability,
) -> ExecutionFailureScenarioResult:
    """Derive failure facts from the public response and retained failure C6."""
    if not isinstance(response, TerminalReturn):
        return ExecutionFailureScenarioResult(
            scenario="execution-failure",
            response_type=type(response).__name__,
            execution_established=False,
            execution_id=None,
            business_result_present=False,
            execution_outcome=None,
            search_invocation_count=controlled_search.invocation_count,
            controlled_non_result_observed=controlled_search.non_result_triggered,
            search_execution_matches=False,
            failure_recorded=False,
            failure_code=None,
            failure_reason=None,
            search_participated=False,
            c6_exists=False,
            c6_outcome=None,
            c6_execution_matches=False,
            fabricated_research_facts=False,
            clean_closure=False,
            final_bundle_exists=False,
            record_ref_present=False,
            record_ref=None,
            record_ref_resolves=False,
            required_reference_count=0,
            required_references_resolve=False,
            failure_staging_absent=True,
            evidence_root=execution_root,
        )

    record_ref_present = response.record_ref is not None
    record_ref_resolves = False
    final_bundle_exists = False
    required_reference_count = 0
    required_references_resolve = False
    failure_recorded = False
    failure_code: str | None = None
    failure_reason: str | None = None
    search_participated = False
    c6_exists = False
    c6_outcome: str | None = None
    c6_execution_matches = False
    fabricated_research_facts = False

    if response.record_ref is not None:
        retention = LocalJsonRetention(execution_root)
        try:
            record_path = retention.resolve_record_ref(response.record_ref)
        except FileNotFoundError:
            record_path = None

        if record_path is not None:
            record_ref_resolves = record_path.is_file()
            c6_exists = record_path.is_file()
            final_bundle = record_path.parent
            final_bundle_exists = final_bundle.is_dir()
            record_payload = json.loads(record_path.read_text(encoding="utf-8"))
            outcome = record_payload.get("terminal_outcome")
            if isinstance(outcome, str):
                c6_outcome = outcome
            c6_execution_matches = (
                record_payload.get("execution_id") == response.execution_id
            )

            failure = record_payload.get("failure")
            if isinstance(failure, dict):
                code = failure.get("code")
                reason = failure.get("reason")
                if isinstance(code, str) and isinstance(reason, str):
                    failure_recorded = True
                    failure_code = code
                    failure_reason = reason

            actual_participation = record_payload.get("actual_participation")
            search_result_refs_present = False
            if isinstance(actual_participation, dict):
                capabilities = actual_participation.get("capabilities")
                search_participated = isinstance(capabilities, list) and (
                    "Search" in capabilities
                )
                search_result_refs_present = "search_result_refs" in actual_participation

            required_references = record_payload.get("required_references")
            if isinstance(required_references, list) and all(
                isinstance(reference, str) for reference in required_references
            ):
                required_reference_count = len(required_references)
                required_references_resolve = bool(required_references) and all(
                    (final_bundle / reference).is_file()
                    for reference in required_references
                )

            fabricated_record_keys = (
                "actual_sample_boundary_ref",
                "evidence_refs",
                "research_result_ref",
                "business_result",
                "provider",
                "provider_facts",
                "provider_raw",
            )
            fabricated_directories = (
                "search_results",
                "sample_boundaries",
                "evidence",
                "research_results",
                "provider_raw",
            )
            fabricated_research_facts = (
                search_result_refs_present
                or any(key in record_payload for key in fabricated_record_keys)
                or any(
                    (final_bundle / directory).exists()
                    for directory in fabricated_directories
                )
            )

    failure_staging_absent = not (
        execution_root / ".staging" / response.execution_id
    ).exists()
    clean_closure = all(
        (
            c6_exists,
            c6_outcome == "FAILED",
            c6_execution_matches,
            final_bundle_exists,
            record_ref_present,
            record_ref_resolves,
            required_references_resolve,
            failure_staging_absent,
        )
    )

    return ExecutionFailureScenarioResult(
        scenario="execution-failure",
        response_type=type(response).__name__,
        execution_established=True,
        execution_id=response.execution_id,
        business_result_present=response.business_result is not None,
        execution_outcome=response.execution_outcome,
        search_invocation_count=controlled_search.invocation_count,
        controlled_non_result_observed=controlled_search.non_result_triggered,
        search_execution_matches=(
            controlled_search.last_context is not None
            and controlled_search.last_context.execution_id == response.execution_id
        ),
        failure_recorded=failure_recorded,
        failure_code=failure_code,
        failure_reason=failure_reason,
        search_participated=search_participated,
        c6_exists=c6_exists,
        c6_outcome=c6_outcome,
        c6_execution_matches=c6_execution_matches,
        fabricated_research_facts=fabricated_research_facts,
        clean_closure=clean_closure,
        final_bundle_exists=final_bundle_exists,
        record_ref_present=record_ref_present,
        record_ref=str(response.record_ref) if response.record_ref is not None else None,
        record_ref_resolves=record_ref_resolves,
        required_reference_count=required_reference_count,
        required_references_resolve=required_references_resolve,
        failure_staging_absent=failure_staging_absent,
        evidence_root=execution_root,
    )


def execution_failure_mismatches(
    result: ExecutionFailureScenarioResult,
) -> tuple[str, ...]:
    """Compare observed facts with the reviewed execution-failure shape."""
    expected = {
        "response_type": "TerminalReturn",
        "execution_established": True,
        "business_result_present": False,
        "execution_outcome": "FAILED",
        "search_invocation_count": 1,
        "controlled_non_result_observed": True,
        "search_execution_matches": True,
        "failure_recorded": True,
        "failure_code": "SEARCH_OUTCOME_NOT_RESULT",
        "failure_reason": (
            "Search invocation did not produce a contract-valid SearchResult"
        ),
        "search_participated": True,
        "c6_exists": True,
        "c6_outcome": "FAILED",
        "c6_execution_matches": True,
        "fabricated_research_facts": False,
        "clean_closure": True,
        "final_bundle_exists": True,
        "record_ref_present": True,
        "record_ref_resolves": True,
        "required_reference_count": 1,
        "required_references_resolve": True,
        "failure_staging_absent": True,
    }
    mismatches = []
    for field_name, expected_value in expected.items():
        observed_value = getattr(result, field_name)
        if observed_value != expected_value:
            mismatches.append(
                f"{field_name}: expected {expected_value!r}, observed {observed_value!r}"
            )
    return tuple(mismatches)


def derive_closure_failure_result(
    response: TaskExecutionResponse,
    execution_root: Path,
    *,
    observed_completion: ResearchCompletion | None,
    lifecycle_events: Sequence[str],
    publication_attempts: Sequence[
        tuple[dict[str, object], tuple[str, ...]]
    ],
    controlled_publication_failure_observed: bool,
) -> ClosureFailureScenarioResult:
    """Derive closure-failure facts from response, patch evidence, and staging."""
    terminal_return = response if isinstance(response, TerminalReturn) else None
    execution_id = terminal_return.execution_id if terminal_return is not None else None
    business_result = (
        terminal_return.business_result if terminal_return is not None else None
    )
    business_completed = observed_completion is not None
    business_result_preserved = (
        observed_completion is not None
        and business_result is observed_completion.research_result
    )
    completion_preceded_failure = list(lifecycle_events) == [
        "business_completion",
        "publication_failure",
    ]

    attempted_c6_outcome: str | None = None
    attempted_research_result_matches = False
    attempted_required_references_resolve = False
    attempted_payload: dict[str, object] | None = None
    attempted_references: tuple[str, ...] = ()
    if publication_attempts:
        attempted_payload, attempted_references = publication_attempts[0]
        outcome = attempted_payload.get("terminal_outcome")
        if isinstance(outcome, str):
            attempted_c6_outcome = outcome

        if observed_completion is not None:
            expected_research_result_ref = (
                "research_results/"
                f"{observed_completion.research_result.research_result_id}.json"
            )
            attempted_research_result_matches = (
                attempted_payload.get("research_result_ref")
                == expected_research_result_ref
                and expected_research_result_ref in attempted_references
            )

    staging_bundle = (
        execution_root / ".staging" / execution_id
        if execution_id is not None
        else None
    )
    final_bundle = (
        execution_root / execution_id if execution_id is not None else None
    )
    staging_bundle_exists = staging_bundle is not None and staging_bundle.is_dir()
    final_bundle_exists = final_bundle is not None and final_bundle.is_dir()
    staging_execution_record_exists = (
        staging_bundle is not None
        and (staging_bundle / "execution_record.json").is_file()
    )
    final_execution_record_exists = (
        final_bundle is not None
        and (final_bundle / "execution_record.json").is_file()
    )

    if staging_bundle is not None:
        attempted_required_references_resolve = bool(attempted_references) and all(
            (staging_bundle / reference).is_file()
            for reference in attempted_references
        )
        retained_input_present = any((staging_bundle / "inputs").glob("*.json"))
        retained_search_result_present = any(
            (staging_bundle / "search_results").glob("*.json")
        )
        retained_sample_boundary_present = any(
            (staging_bundle / "sample_boundaries").glob("*.json")
        )
        retained_evidence_present = any(
            (staging_bundle / "evidence").glob("*.json")
        )
        retained_research_result_present = any(
            (staging_bundle / "research_results").glob("*.json")
        )
    else:
        retained_input_present = False
        retained_search_result_present = False
        retained_sample_boundary_present = False
        retained_evidence_present = False
        retained_research_result_present = False

    record_ref = terminal_return.record_ref if terminal_return is not None else None
    record_ref_present = record_ref is not None
    hypothetical_record_ref_checked = False
    hypothetical_record_ref_resolves = False
    if execution_id is not None:
        hypothetical_record_ref_checked = True
        hypothetical_ref = ExecutionRecordRef(execution_id=execution_id)
        try:
            LocalJsonRetention(execution_root).resolve_record_ref(hypothetical_ref)
        except FileNotFoundError:
            hypothetical_record_ref_resolves = False
        else:
            hypothetical_record_ref_resolves = True

    clean_closure = all(
        (
            final_bundle_exists,
            final_execution_record_exists,
            record_ref_present,
        )
    )

    return ClosureFailureScenarioResult(
        scenario="closure-failure",
        response_type=type(response).__name__,
        execution_established=terminal_return is not None,
        execution_id=execution_id,
        business_completed=business_completed,
        business_result_present=business_result is not None,
        business_result_preserved=business_result_preserved,
        business_completion_preceded_publication_failure=(
            completion_preceded_failure
        ),
        execution_outcome=(
            terminal_return.execution_outcome
            if terminal_return is not None
            else None
        ),
        publication_attempt_count=len(publication_attempts),
        controlled_publication_failure_observed=(
            controlled_publication_failure_observed
        ),
        attempted_c6_outcome=attempted_c6_outcome,
        attempted_research_result_matches=attempted_research_result_matches,
        attempted_required_references_resolve=(
            attempted_required_references_resolve
        ),
        clean_closure=clean_closure,
        final_bundle_exists=final_bundle_exists,
        final_execution_record_exists=final_execution_record_exists,
        staging_bundle_exists=staging_bundle_exists,
        staging_execution_record_exists=staging_execution_record_exists,
        retained_input_present=retained_input_present,
        retained_search_result_present=retained_search_result_present,
        retained_sample_boundary_present=retained_sample_boundary_present,
        retained_evidence_present=retained_evidence_present,
        retained_research_result_present=retained_research_result_present,
        record_ref_present=record_ref_present,
        hypothetical_record_ref_checked=hypothetical_record_ref_checked,
        hypothetical_record_ref_resolves=hypothetical_record_ref_resolves,
        evidence_root=execution_root,
    )


def closure_failure_mismatches(
    result: ClosureFailureScenarioResult,
) -> tuple[str, ...]:
    """Compare observed facts with the reviewed P4 closure-failure shape."""
    expected = {
        "response_type": "TerminalReturn",
        "execution_established": True,
        "business_completed": True,
        "business_result_present": True,
        "business_result_preserved": True,
        "business_completion_preceded_publication_failure": True,
        "execution_outcome": "FAILED",
        "publication_attempt_count": 1,
        "controlled_publication_failure_observed": True,
        "attempted_c6_outcome": "SUCCEEDED",
        "attempted_research_result_matches": True,
        "attempted_required_references_resolve": True,
        "clean_closure": False,
        "final_bundle_exists": False,
        "final_execution_record_exists": False,
        "staging_bundle_exists": True,
        "staging_execution_record_exists": False,
        "retained_input_present": True,
        "retained_search_result_present": True,
        "retained_sample_boundary_present": True,
        "retained_evidence_present": True,
        "retained_research_result_present": True,
        "record_ref_present": False,
        "hypothetical_record_ref_checked": True,
        "hypothetical_record_ref_resolves": False,
    }
    mismatches = []
    for field_name, expected_value in expected.items():
        observed_value = getattr(result, field_name)
        if observed_value != expected_value:
            mismatches.append(
                f"{field_name}: expected {expected_value!r}, observed {observed_value!r}"
            )
    return tuple(mismatches)


def summarize_scenario(result: DetailedScenarioResult) -> ScenarioSummaryResult:
    """Project one fully derived result into the post-cleanup matrix shape."""
    return ScenarioSummaryResult(
        scenario=result.scenario,
        execution_established=result.execution_established,
        business_result_present=result.business_result_present,
        execution_outcome=result.execution_outcome,
        record_ref_present=result.record_ref_present,
    )


def matrix_mismatches(
    results: Sequence[ScenarioSummaryResult],
) -> tuple[str, ...]:
    """Validate actual summary rows against the reviewed four-path model."""
    expected = {
        "success": {
            "execution_established": True,
            "business_result_present": True,
            "execution_outcome": "SUCCEEDED",
            "record_ref_present": True,
        },
        "rejection": {
            "execution_established": False,
            "business_result_present": False,
            "execution_outcome": None,
            "record_ref_present": False,
        },
        "execution-failure": {
            "execution_established": True,
            "business_result_present": False,
            "execution_outcome": "FAILED",
            "record_ref_present": True,
        },
        "closure-failure": {
            "execution_established": True,
            "business_result_present": True,
            "execution_outcome": "FAILED",
            "record_ref_present": False,
        },
    }
    observed_by_scenario = {result.scenario: result for result in results}
    mismatches = []
    if len(results) != len(expected) or set(observed_by_scenario) != set(expected):
        mismatches.append(
            "scenario rows: expected success, rejection, execution-failure, "
            "closure-failure exactly once"
        )

    for scenario, expected_fields in expected.items():
        result = observed_by_scenario.get(scenario)
        if result is None:
            continue
        for field_name, expected_value in expected_fields.items():
            observed_value = getattr(result, field_name)
            if observed_value != expected_value:
                mismatches.append(
                    f"{scenario}.{field_name}: expected {expected_value!r}, "
                    f"observed {observed_value!r}"
                )
    return tuple(mismatches)


def scenario_label(scenario: str) -> str:
    """Return a human-readable label without encoding lifecycle outcomes."""
    labels = {
        "success": "Success",
        "rejection": "Rejection",
        "execution-failure": "Execution Failure",
        "closure-failure": "Closure Failure",
    }
    return labels.get(scenario, scenario)


def observed_boolean_cell(value: bool) -> str:
    """Render one actual matrix boolean."""
    return "✓ YES" if value else "○ NO"


def render_summary_matrix(results: Sequence[ScenarioSummaryResult]) -> None:
    """Render a matrix whose cells come only from actual scenario summaries."""
    headers = ("Scenario", "Execution", "Biz Result", "Outcome", "Record Ref")
    rows = [
        (
            scenario_label(result.scenario),
            observed_boolean_cell(result.execution_established),
            observed_boolean_cell(result.business_result_present),
            result.execution_outcome or "N/A",
            observed_boolean_cell(result.record_ref_present),
        )
        for result in results
    ]
    widths = tuple(
        max(len(headers[index]), *(len(row[index]) for row in rows))
        for index in range(len(headers))
    )

    def border(left: str, separator: str, right: str) -> str:
        return left + separator.join("─" * (width + 2) for width in widths) + right

    def row_line(values: Sequence[str]) -> str:
        cells = [
            f" {value:<{width}} " for value, width in zip(values, widths, strict=True)
        ]
        return "│" + "│".join(cells) + "│"

    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  WI-02 FOUR-PATH SUMMARY                                     ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()
    print(border("┌", "┬", "┐"))
    print(row_line(headers))
    print(border("├", "┼", "┤"))
    for row in rows:
        print(row_line(row))
    print(border("└", "┴", "┘"))


def render_four_path_mental_model(
    results: Sequence[ScenarioSummaryResult],
) -> None:
    """Render a concise learning view from the same actual summary rows."""
    print()
    print("WI-02 FOUR-PATH MENTAL MODEL")
    for result in results:
        print()
        print(f"{scenario_label(result.scenario)}:")
        print(f"Execution = {yes_no(result.execution_established)}")
        print(f"Business Result = {yes_no(result.business_result_present)}")
        print(f"Record Ref = {yes_no(result.record_ref_present)}")


def mark(condition: bool) -> str:
    """Return an accessible status marker."""
    return "✓" if condition else "✗"


def yes_no(condition: bool) -> str:
    """Render one observed boolean without color dependence."""
    return "YES" if condition else "NO"


def render_stage(
    number: int,
    complete: bool,
    title: str,
    details: tuple[str, ...],
    source: str,
    *,
    terminal: bool = False,
) -> None:
    """Render one lifecycle learning row with one primary provenance."""
    print(f" [{number:02}] {mark(complete)} {title}")
    for detail in details:
        print(f"      │  {detail}")
    print(f"      │  source: [{source}]")
    if not terminal:
        print("      ▼")


def render_inactive_stage(
    number: int,
    marker: str,
    title: str,
    details: tuple[str, ...],
    source: str,
    *,
    terminal: bool = False,
) -> None:
    """Render one rejection-path row without changing SUCCESS markers."""
    print(f" [{number:02}] {marker} {title}")
    for detail in details:
        print(f"      │  {detail}")
    print(f"      │  source: [{source}]")
    if not terminal:
        print("      ▼")


def render_success(result: SuccessScenarioResult, mismatches: tuple[str, ...]) -> None:
    """Render the evidence-derived success timeline and final state."""
    title = "WI-02 LIFECYCLE DEMO — SUCCESS"
    width = 62
    print("╔" + "═" * width + "╗")
    print(f"║  {title:<{width - 2}}║")
    print("╚" + "═" * width + "╝")
    print()

    render_stage(
        1,
        True,
        "Business Work Request",
        ("US / Car Vacuum / TikTok Content Research",),
        "DEMO",
    )
    render_stage(
        2,
        result.execution_established,
        "Admission Passed",
        (
            "fn: TaskRuntime._pre_execution_rejection()",
            "valid-path decision is not independently instrumented",
        ),
        "SEMANTIC",
    )
    render_stage(
        3,
        result.execution_established,
        "Established Execution Confirmed",
        (
            f"execution_id = {result.execution_id or 'ABSENT'}",
            "fn: TaskRuntime.execute()",
            "confirmed by returned execution_id",
        ),
        "RUNTIME",
    )
    render_stage(
        4,
        result.business_result_present,
        "Research / Business Completion",
        (
            "fn: CarVacuumTikTokResearchSkill.run()",
            "inferred from returned Business Result; not independently observed",
        ),
        "SEMANTIC",
    )
    render_stage(
        5,
        result.search_participated,
        "Search Participation Verified",
        (
            "fn: RuntimeResearchExecutionPort.search() / TaskRuntime._invoke_search()",
            "C6 actual participation includes Search",
        ),
        "ARTIFACT",
    )
    render_stage(
        6,
        result.c6_outcome == "SUCCEEDED" and result.required_references_resolve,
        "Success C6 Verified",
        (
            "fn: StableExecutionFacts.finalize_success()",
            f"required references = {result.required_reference_count} / all resolve",
        ),
        "ARTIFACT",
    )
    render_stage(
        7,
        result.clean_closure,
        "Final Bundle Published",
        (
            "fn: StagingExecutionBundle.publish()",
            "fn: LocalJsonRetention.resolve_record_ref()",
            f"record_ref resolves = {yes_no(result.record_ref_resolves)}",
        ),
        "ARTIFACT",
    )
    render_stage(
        8,
        result.execution_outcome == "SUCCEEDED",
        "Terminal Return",
        (
            f"outcome = {result.execution_outcome or 'N/A'}",
            f"record_ref = {result.record_ref or 'ABSENT'}",
        ),
        "RUNTIME",
        terminal=True,
    )

    print()
    print("─" * 62)
    print(" FINAL STATE")
    print("─" * 62)
    print()
    print(
        f" Execution           {mark(result.execution_established)} "
        f"{yes_no(result.execution_established)}"
    )
    print(
        f" Business Result     {mark(result.business_result_present)} "
        f"{'PRESENT' if result.business_result_present else 'ABSENT'}"
    )
    print(
        f" Outcome             {mark(result.execution_outcome == 'SUCCEEDED')} "
        f"{result.execution_outcome or 'N/A'}"
    )
    print(
        f" Clean Closure       {mark(result.clean_closure)} "
        f"{yes_no(result.clean_closure)}"
    )
    print(
        f" Final Bundle        {mark(result.final_bundle_exists)} "
        f"{yes_no(result.final_bundle_exists)}"
    )
    print(
        f" Record Ref          {mark(result.record_ref_present)} "
        f"{'PRESENT' if result.record_ref_present else 'ABSENT'}"
    )
    print(
        f" Record Resolves     {mark(result.record_ref_resolves)} "
        f"{yes_no(result.record_ref_resolves)}"
    )
    print(
        f" Required Refs       {mark(result.required_references_resolve)} "
        f"{yes_no(result.required_references_resolve)}"
    )
    print()

    if mismatches:
        print(" Scenario Verification ✗ FAIL")
        print(" Observed / expected mismatches:")
        for mismatch in mismatches:
            print(f" - {mismatch}")
    else:
        print(" Scenario Verification ✓ PASS")

    print()
    print("Evidence Root")
    print(f"= {result.evidence_root}")
    print()
    print("Evidence Lifetime")
    print("= TEMPORARY / removed after process exit")


def render_rejection(
    result: RejectionScenarioResult,
    mismatches: tuple[str, ...],
) -> None:
    """Render the evidence-derived pre-execution rejection."""
    title = "WI-02 LIFECYCLE DEMO — PRE-EXECUTION REJECTION"
    width = 62
    print("╔" + "═" * width + "╗")
    print(f"║  {title:<{width - 2}}║")
    print("╚" + "═" * width + "╝")
    print()

    render_inactive_stage(
        1,
        "✓",
        "Business Work Request",
        ("intentionally invalid: product_context is empty",),
        "DEMO",
    )
    render_inactive_stage(
        2,
        "✗",
        "Admission Rejected",
        (
            f"response = {result.response_type}",
            f"reason = {result.rejection_reason or 'ABSENT'}",
            "fn: TaskRuntime._pre_execution_rejection()",
        ),
        "RUNTIME",
    )
    render_inactive_stage(
        3,
        "○",
        "Execution Not Established",
        (
            "execution_id = ABSENT"
            if not result.execution_id_present
            else "execution_id = PRESENT",
            "confirmed by public rejection response",
        ),
        "RUNTIME",
    )
    render_inactive_stage(
        4,
        "○",
        "Research / Search Not Entered",
        (
            f"research invocation observed = {yes_no(result.research_started)}",
            f"search invocation observed = {yes_no(result.search_started)}",
            "observed through demo-local wrappers around existing seams",
        ),
        "DEMO",
    )
    render_inactive_stage(
        5,
        "○",
        "C6 / Final Bundle Absent",
        (
            f"execution_record.json exists = {yes_no(result.c6_exists)}",
            f"final bundle exists = {yes_no(result.final_bundle_exists)}",
        ),
        "ARTIFACT",
    )
    render_inactive_stage(
        6,
        "○",
        "Record Ref Absent",
        ("record_ref = ABSENT",),
        "RUNTIME",
        terminal=True,
    )

    print()
    print("─" * 62)
    print(" FINAL STATE")
    print("─" * 62)
    print()
    print(f" Execution           ○ {yes_no(result.execution_established)}")
    print(
        " Execution ID        ○ "
        f"{'PRESENT' if result.execution_id_present else 'ABSENT'}"
    )
    print(f" Research Started    ○ {yes_no(result.research_started)}")
    print(
        " Business Result     ○ "
        f"{'PRESENT' if result.business_result_present else 'ABSENT'}"
    )
    print(f" Outcome             ○ {result.execution_outcome or 'N/A'}")
    print(f" C6                  ○ {'PRESENT' if result.c6_exists else 'ABSENT'}")
    print(
        " Final Bundle        ○ "
        f"{'PRESENT' if result.final_bundle_exists else 'ABSENT'}"
    )
    print(
        " Record Ref          ○ "
        f"{'PRESENT' if result.record_ref_present else 'ABSENT'}"
    )
    print()

    if mismatches:
        print(" Scenario Verification ✗ FAIL")
        print(" Observed / expected mismatches:")
        for mismatch in mismatches:
            print(f" - {mismatch}")
    else:
        print(" Scenario Verification ✓ PASS")

    print()
    print(" IMPORTANT")
    print()
    print(" ✗ Request was rejected")
    print(" ○ No Execution was established")
    print()
    print(" PreExecutionRejection ≠ Execution Failure")
    print()
    print("Evidence Root")
    print(f"= {result.evidence_root}")
    print()
    print("Evidence Lifetime")
    print("= TEMPORARY / removed after process exit")


def render_execution_failure(
    result: ExecutionFailureScenarioResult,
    mismatches: tuple[str, ...],
) -> None:
    """Render the evidence-derived established execution failure."""
    title = "WI-02 LIFECYCLE DEMO — EXECUTION FAILURE"
    width = 62
    print("╔" + "═" * width + "╗")
    print(f"║  {title:<{width - 2}}║")
    print("╚" + "═" * width + "╝")
    print()

    render_inactive_stage(
        1,
        "✓",
        "Business Work Request",
        ("US / Car Vacuum / TikTok Content Research",),
        "DEMO",
    )
    render_inactive_stage(
        2,
        mark(result.execution_established),
        "Admission Passed",
        (
            "fn: TaskRuntime._pre_execution_rejection()",
            "valid-path decision is not independently instrumented",
        ),
        "SEMANTIC",
    )
    render_inactive_stage(
        3,
        mark(result.execution_established and result.execution_id is not None),
        "Established Execution Confirmed",
        (
            f"execution_id = {result.execution_id or 'ABSENT'}",
            "fn: TaskRuntime.execute()",
            "confirmed by returned execution_id",
        ),
        "RUNTIME",
    )
    render_inactive_stage(
        4,
        mark(
            result.search_invocation_count == 1
            and result.search_execution_matches
        ),
        "Search Invoked",
        (
            "fn: RuntimeResearchExecutionPort.search() / TaskRuntime._invoke_search()",
            f"controlled Search double calls = {result.search_invocation_count}",
            "invocation bound to returned execution_id = "
            f"{yes_no(result.search_execution_matches)}",
        ),
        "DEMO",
    )
    render_inactive_stage(
        5,
        "✗" if result.controlled_non_result_observed else "○",
        "Search Did Not Produce Valid SearchResult",
        (
            "controlled non-result triggered = "
            f"{yes_no(result.controlled_non_result_observed)}",
        ),
        "DEMO",
    )
    render_inactive_stage(
        6,
        "↩" if result.failure_recorded else "○",
        "Private Execution Unwind",
        (
            "mechanism: _ExecutionAbort",
            "visibility: PRIVATE / Runtime-owned",
            "fn: TaskRuntime._abort_execution()",
            "not independently traced by the Demo",
        ),
        "SEMANTIC",
    )
    render_inactive_stage(
        7,
        mark(
            result.response_type == "TerminalReturn"
            and result.execution_outcome == "FAILED"
            and not result.business_result_present
        ),
        "Failed Execution Confirmed",
        (
            f"response = {result.response_type}",
            f"outcome = {result.execution_outcome or 'N/A'}",
            "business_result = "
            f"{'PRESENT' if result.business_result_present else 'ABSENT'}",
        ),
        "RUNTIME",
    )
    render_inactive_stage(
        8,
        mark(
            result.failure_recorded
            and result.c6_exists
            and result.c6_outcome == "FAILED"
            and result.search_participated
            and not result.fabricated_research_facts
        ),
        "Failure C6 Verified",
        (
            "fn: StableExecutionFacts.record_execution_failure()",
            "fn: StableExecutionFacts.finalize_failure()",
            f"C6 outcome = {result.c6_outcome or 'ABSENT'}",
            f"failure_code = {result.failure_code or 'ABSENT'}",
            f"failure_reason = {result.failure_reason or 'ABSENT'}",
            f"actual Search participation = {yes_no(result.search_participated)}",
            "fabricated Research facts = "
            f"{yes_no(result.fabricated_research_facts)}",
        ),
        "ARTIFACT",
    )
    render_inactive_stage(
        9,
        mark(result.final_bundle_exists and result.required_references_resolve),
        "Failure Bundle Published",
        (
            "fn: StagingExecutionBundle.publish()",
            f"required references = {result.required_reference_count}",
            "all required references resolve = "
            f"{yes_no(result.required_references_resolve)}",
        ),
        "ARTIFACT",
    )
    render_inactive_stage(
        10,
        mark(result.record_ref_present and result.record_ref_resolves),
        "Record Ref Resolved",
        (
            "fn: LocalJsonRetention.resolve_record_ref()",
            f"record_ref resolves = {yes_no(result.record_ref_resolves)}",
        ),
        "ARTIFACT",
    )
    render_inactive_stage(
        11,
        mark(
            result.response_type == "TerminalReturn"
            and result.execution_outcome == "FAILED"
            and result.record_ref_present
        ),
        "Terminal Return",
        (
            f"outcome = {result.execution_outcome or 'N/A'}",
            f"record_ref = {result.record_ref or 'ABSENT'}",
        ),
        "RUNTIME",
        terminal=True,
    )

    print()
    print("─" * 62)
    print(" FINAL STATE")
    print("─" * 62)
    print()
    print(
        f" Execution           {mark(result.execution_established)} "
        f"{yes_no(result.execution_established)}"
    )
    print(
        " Business Result     "
        f"{'○' if not result.business_result_present else '✗'} "
        f"{'PRESENT' if result.business_result_present else 'ABSENT'}"
    )
    print(
        " Outcome             "
        f"{'✗' if result.execution_outcome == 'FAILED' else '○'} "
        f"{result.execution_outcome or 'N/A'}"
    )
    print(
        f" Failure Recorded    {mark(result.failure_recorded)} "
        f"{yes_no(result.failure_recorded)}"
    )
    print(
        " Failure C6          "
        f"{mark(result.c6_exists and result.c6_outcome == 'FAILED')} "
        f"{'PRESENT' if result.c6_exists else 'ABSENT'}"
    )
    print(
        f" Clean Closure       {mark(result.clean_closure)} "
        f"{yes_no(result.clean_closure)}"
    )
    print(
        f" Final Bundle        {mark(result.final_bundle_exists)} "
        f"{'PRESENT' if result.final_bundle_exists else 'ABSENT'}"
    )
    print(
        f" Record Ref          {mark(result.record_ref_present)} "
        f"{'PRESENT' if result.record_ref_present else 'ABSENT'}"
    )
    print(
        f" Record Resolves     {mark(result.record_ref_resolves)} "
        f"{yes_no(result.record_ref_resolves)}"
    )
    print(
        " Required Refs       "
        f"{mark(result.required_references_resolve)} "
        f"{yes_no(result.required_references_resolve)}"
    )
    print()

    if mismatches:
        print(" Scenario Verification ✗ FAIL")
        print(" Observed / expected mismatches:")
        for mismatch in mismatches:
            print(f" - {mismatch}")
    else:
        print(" Scenario Verification ✓ PASS")

    print()
    print(" IMPORTANT")
    print()
    print(" ✗ Business work failed")
    print(" ✓ Failure itself was cleanly closed")
    print()
    print(" Execution Failure ≠ Runtime loss of control")
    print(" Business Failure ≠ Closure Failure")
    print()
    print("Evidence Root")
    print(f"= {result.evidence_root}")
    print()
    print("Evidence Lifetime")
    print("= TEMPORARY / removed after process exit")


def render_closure_failure(
    result: ClosureFailureScenarioResult,
    mismatches: tuple[str, ...],
) -> None:
    """Render the evidence-derived P4 closure failure."""
    title = "WI-02 LIFECYCLE DEMO — CLOSURE FAILURE"
    width = 62
    print("╔" + "═" * width + "╗")
    print(f"║  {title:<{width - 2}}║")
    print("╚" + "═" * width + "╝")
    print()

    render_inactive_stage(
        1,
        "✓",
        "Business Work Request",
        ("US / Car Vacuum / TikTok Content Research",),
        "DEMO",
    )
    render_inactive_stage(
        2,
        mark(result.execution_established),
        "Admission Passed",
        (
            "fn: TaskRuntime._pre_execution_rejection()",
            "valid-path decision is not independently instrumented",
        ),
        "SEMANTIC",
    )
    render_inactive_stage(
        3,
        mark(result.execution_established and result.execution_id is not None),
        "Established Execution Confirmed",
        (
            f"execution_id = {result.execution_id or 'ABSENT'}",
            "fn: TaskRuntime.execute()",
            "confirmed by returned execution_id",
        ),
        "RUNTIME",
    )
    render_inactive_stage(
        4,
        mark(
            result.business_completed
            and result.business_completion_preceded_publication_failure
            and result.business_result_preserved
        ),
        "Research / Business Completion",
        (
            "fn: CarVacuumTikTokResearchSkill.run()",
            "Business Completion observed before publication failure = "
            f"{yes_no(result.business_completion_preceded_publication_failure)}",
            "returned ResearchResult captured without recreation",
            "captured ResearchResult is returned Business Result = "
            f"{yes_no(result.business_result_preserved)}",
        ),
        "DEMO",
    )
    render_inactive_stage(
        5,
        mark(result.business_result_present),
        "Business Result Present",
        (
            "business_result = "
            f"{'PRESENT' if result.business_result_present else 'ABSENT'}",
        ),
        "RUNTIME",
    )
    render_inactive_stage(
        6,
        mark(
            result.publication_attempt_count == 1
            and result.attempted_c6_outcome == "SUCCEEDED"
            and result.attempted_research_result_matches
            and result.attempted_required_references_resolve
        ),
        "Closure Publication Attempted",
        (
            "fn: StagingExecutionBundle.publish()",
            f"publication attempts = {result.publication_attempt_count}",
            f"attempted C6 outcome = {result.attempted_c6_outcome or 'ABSENT'}",
            "attempted ResearchResult reference matches = "
            f"{yes_no(result.attempted_research_result_matches)}",
            "attempted required references resolve = "
            f"{yes_no(result.attempted_required_references_resolve)}",
        ),
        "DEMO",
    )
    render_inactive_stage(
        7,
        "✗" if result.controlled_publication_failure_observed else "○",
        "Publication Failed",
        (
            "controlled publication failure = "
            f"{yes_no(result.controlled_publication_failure_observed)}",
            "patch scope ended immediately after this Runtime execution",
        ),
        "DEMO",
    )
    render_inactive_stage(
        8,
        "✗" if result.execution_outcome == "FAILED" else "○",
        "Failed Terminal Outcome Confirmed",
        (f"outcome = {result.execution_outcome or 'N/A'}",),
        "RUNTIME",
    )
    retained_staging_facts = all(
        (
            result.retained_input_present,
            result.retained_search_result_present,
            result.retained_sample_boundary_present,
            result.retained_evidence_present,
            result.retained_research_result_present,
        )
    )
    render_inactive_stage(
        9,
        "○" if not result.final_bundle_exists else "✗",
        "Final Bundle Not Published",
        (
            f"final bundle exists = {yes_no(result.final_bundle_exists)}",
            "final execution_record.json exists = "
            f"{yes_no(result.final_execution_record_exists)}",
            f"staging bundle exists = {yes_no(result.staging_bundle_exists)}",
            "staging execution_record.json exists = "
            f"{yes_no(result.staging_execution_record_exists)}",
            "pre-publication business artifacts retained = "
            f"{yes_no(retained_staging_facts)}",
            "hypothetical Record Ref resolves = "
            f"{yes_no(result.hypothetical_record_ref_resolves)}",
        ),
        "ARTIFACT",
    )
    render_inactive_stage(
        10,
        "○" if not result.record_ref_present else "✗",
        "Record Ref Absent",
        (
            "record_ref = "
            f"{'PRESENT' if result.record_ref_present else 'ABSENT'}",
        ),
        "RUNTIME",
    )
    render_inactive_stage(
        11,
        mark(
            result.response_type == "TerminalReturn"
            and result.execution_outcome == "FAILED"
            and result.business_result_present
            and not result.record_ref_present
        ),
        "Terminal Return",
        (
            f"response = {result.response_type}",
            f"outcome = {result.execution_outcome or 'N/A'}",
            "business_result = "
            f"{'PRESENT' if result.business_result_present else 'ABSENT'}",
            "record_ref = "
            f"{'PRESENT' if result.record_ref_present else 'ABSENT'}",
        ),
        "RUNTIME",
        terminal=True,
    )

    print()
    print("─" * 62)
    print(" FINAL STATE")
    print("─" * 62)
    print()
    print(
        f" Execution           {mark(result.execution_established)} "
        f"{yes_no(result.execution_established)}"
    )
    print(
        f" Business Result     {mark(result.business_result_present)} "
        f"{'PRESENT' if result.business_result_present else 'ABSENT'}"
    )
    print(
        " Outcome             "
        f"{'✗' if result.execution_outcome == 'FAILED' else '○'} "
        f"{result.execution_outcome or 'N/A'}"
    )
    print(
        f" Business Completed  {mark(result.business_completed)} "
        f"{yes_no(result.business_completed)}"
    )
    print(
        " Clean Closure       "
        f"{'✓' if result.clean_closure else '✗'} "
        f"{yes_no(result.clean_closure)}"
    )
    print(
        " Final Bundle        "
        f"{'✗' if result.final_bundle_exists else '○'} "
        f"{'PRESENT' if result.final_bundle_exists else 'ABSENT'}"
    )
    print(
        " Record Ref          "
        f"{'✗' if result.record_ref_present else '○'} "
        f"{'PRESENT' if result.record_ref_present else 'ABSENT'}"
    )
    print()

    if mismatches:
        print(" Scenario Verification ✗ FAIL")
        print(" Observed / expected mismatches:")
        for mismatch in mismatches:
            print(f" - {mismatch}")
    else:
        print(" Scenario Verification ✓ PASS")

    print()
    print(" IMPORTANT")
    print()
    print(" ✓ Business work succeeded")
    print(" ✗ Execution closure failed")
    print()
    print(" Business Completion ≠ Execution Completion")
    print(" Business Result ≠ Execution Outcome")
    print(" Business Failure ≠ Closure Failure")
    print()
    print("Evidence Root")
    print(f"= {result.evidence_root}")
    print()
    print("Evidence Lifetime")
    print("= TEMPORARY / removed after process exit")


def run_success() -> tuple[ScenarioSummaryResult, tuple[str, ...]]:
    """Execute, inspect, derive, render, and verify the real Fake success path."""
    with tempfile.TemporaryDirectory(prefix="ecommerce-ai-os-lifecycle-demo-") as temp:
        execution_root = Path(temp) / "executions"
        runtime = build_fake_first_slice_runtime(execution_root)
        response = runtime.execute(build_success_request())
        result = derive_success_result(response, execution_root)
        mismatches = success_mismatches(result)
        render_success(result, mismatches)
        return summarize_scenario(result), mismatches


def run_rejection() -> tuple[ScenarioSummaryResult, tuple[str, ...]]:
    """Execute and verify the real WI-02 pre-execution rejection path."""
    with tempfile.TemporaryDirectory(prefix="ecommerce-ai-os-lifecycle-demo-") as temp:
        execution_root = Path(temp) / "executions"
        runtime = build_fake_first_slice_runtime(execution_root)
        with (
            patch.object(
                runtime,
                "_run_research_skill",
                wraps=runtime._run_research_skill,
            ) as observed_research,
            patch.object(
                runtime,
                "_invoke_search",
                wraps=runtime._invoke_search,
            ) as observed_search,
        ):
            response = runtime.execute(build_rejection_request())

        result = derive_rejection_result(
            response,
            execution_root,
            research_started=observed_research.called,
            search_started=observed_search.called,
        )
        mismatches = rejection_mismatches(result)
        render_rejection(result, mismatches)
        return summarize_scenario(result), mismatches


def run_execution_failure() -> tuple[ScenarioSummaryResult, tuple[str, ...]]:
    """Execute and verify the real WI-02 established failure path."""
    with tempfile.TemporaryDirectory(prefix="ecommerce-ai-os-lifecycle-demo-") as temp:
        execution_root = Path(temp) / "executions"
        controlled_search = ControlledFailureSearchCapability()
        runtime = build_execution_failure_runtime(execution_root, controlled_search)
        response = runtime.execute(build_execution_failure_request())
        result = derive_execution_failure_result(
            response,
            execution_root,
            controlled_search,
        )
        mismatches = execution_failure_mismatches(result)
        render_execution_failure(result, mismatches)
        return summarize_scenario(result), mismatches


def run_closure_failure() -> tuple[ScenarioSummaryResult, tuple[str, ...]]:
    """Execute and verify the real WI-02 P4 closure-failure path."""
    with tempfile.TemporaryDirectory(prefix="ecommerce-ai-os-lifecycle-demo-") as temp:
        execution_root = Path(temp) / "executions"
        runtime = build_fake_first_slice_runtime(execution_root)
        observed_completions: list[ResearchCompletion] = []
        lifecycle_events: list[str] = []
        publication_attempts: list[
            tuple[dict[str, object], tuple[str, ...]]
        ] = []
        controlled_publication_failure_observed = False
        run_research_skill = runtime._run_research_skill

        def observe_business_completion(
            *args: object,
            **kwargs: object,
        ) -> ResearchCompletion:
            completion = run_research_skill(  # type: ignore[arg-type]
                *args,
                **kwargs,
            )
            observed_completions.append(completion)
            lifecycle_events.append("business_completion")
            return completion

        def fail_publication(
            bundle: StagingExecutionBundle,
            execution_record_payload: dict[str, object],
            required_references: tuple[str, ...],
        ) -> None:
            nonlocal controlled_publication_failure_observed
            publication_attempts.append(
                (dict(execution_record_payload), tuple(required_references))
            )
            controlled_publication_failure_observed = True
            lifecycle_events.append("publication_failure")
            raise RuntimeError("controlled closure publication failure")

        with (
            patch.object(
                runtime,
                "_run_research_skill",
                side_effect=observe_business_completion,
            ),
            patch.object(
                StagingExecutionBundle,
                "publish",
                autospec=True,
                side_effect=fail_publication,
            ),
        ):
            response = runtime.execute(build_closure_failure_request())

        observed_completion = (
            observed_completions[0] if len(observed_completions) == 1 else None
        )
        result = derive_closure_failure_result(
            response,
            execution_root,
            observed_completion=observed_completion,
            lifecycle_events=lifecycle_events,
            publication_attempts=publication_attempts,
            controlled_publication_failure_observed=(
                controlled_publication_failure_observed
            ),
        )
        mismatches = closure_failure_mismatches(result)
        render_closure_failure(result, mismatches)
        return summarize_scenario(result), mismatches


def individual_exit_code(
    run_result: tuple[ScenarioSummaryResult, tuple[str, ...]],
) -> int:
    """Return the CLI status for one already-rendered scenario run."""
    _, mismatches = run_result
    return 1 if mismatches else 0


def run_all() -> int:
    """Execute the four real runners and summarize their actual results."""
    results: list[ScenarioSummaryResult] = []
    individual_mismatches: list[str] = []
    runners = (
        run_success,
        run_rejection,
        run_execution_failure,
        run_closure_failure,
    )

    for index, runner in enumerate(runners):
        if index:
            print()
        result, mismatches = runner()
        results.append(result)
        individual_mismatches.extend(
            f"{result.scenario}: {mismatch}" for mismatch in mismatches
        )

    summary_mismatches = matrix_mismatches(results)
    render_summary_matrix(results)
    render_four_path_mental_model(results)
    print()
    if individual_mismatches or summary_mismatches:
        print("All Scenario Verification ✗ FAIL")
        print("Observed / expected mismatches:")
        for mismatch in (*individual_mismatches, *summary_mismatches):
            print(f"- {mismatch}")
        return 1

    print("All Scenario Verification ✓ PASS")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Run one currently authorized lifecycle scenario."""
    args = build_parser().parse_args(argv)
    if args.scenario == "success":
        return individual_exit_code(run_success())
    if args.scenario == "rejection":
        return individual_exit_code(run_rejection())
    if args.scenario == "execution-failure":
        return individual_exit_code(run_execution_failure())
    if args.scenario == "closure-failure":
        return individual_exit_code(run_closure_failure())
    if args.scenario == "all":
        return run_all()
    print(
        f"Scenario {args.scenario!r} is not implemented; "
        "only 'success', 'rejection', 'execution-failure', and "
        "'closure-failure', and 'all' are authorized.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
