"""Minimal C6 stable facts, finalization, and runtime-owned serialization."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import NewType
from uuid import uuid4

from .execution import BusinessWorkRequest


ExecutionRecordId = NewType("ExecutionRecordId", str)


@dataclass(frozen=True, slots=True)
class ExecutionRecordRef:
    """Target-specific reference to one published finalized C6 record."""

    execution_id: str
    relative_path: str = "execution_record.json"

    def __str__(self) -> str:
        return f"execution://{self.execution_id}/{self.relative_path}"


@dataclass(slots=True)
class StableExecutionFacts:
    """Execution-level stable facts accumulated separately from runtime state."""

    execution_id: str
    work_request_ref: str
    skill_id: str
    skill_version: str
    actual_capabilities: list[str] = field(default_factory=list)
    search_result_refs: list[str] = field(default_factory=list)
    actual_sample_boundary_ref: str | None = None
    evidence_refs: list[str] = field(default_factory=list)
    research_result_ref: str | None = None
    failure_code: str | None = None
    failure_reason: str | None = None

    def record_search_result(self, search_result_ref: str) -> None:
        """Record one actually completed Search invocation outcome."""
        self.actual_capabilities.append("Search")
        self.search_result_refs.append(search_result_ref)

    def record_research_completion(
        self,
        actual_sample_boundary_ref: str,
        evidence_refs: tuple[str, ...],
        research_result_ref: str,
    ) -> None:
        """Record stable Research references from the accepted completion."""
        self.actual_sample_boundary_ref = actual_sample_boundary_ref
        self.evidence_refs.extend(evidence_refs)
        self.research_result_ref = research_result_ref

    def record_execution_failure(
        self,
        *,
        actual_capability: str,
        failure_code: str,
        failure_reason: str,
    ) -> None:
        """Retain the bounded execution-level facts carried by a private abort."""
        if self.failure_code is not None:
            raise RuntimeError("Execution failure facts are already recorded")
        self.actual_capabilities.append(actual_capability)
        self.failure_code = failure_code
        self.failure_reason = failure_reason

    def finalize_success(self) -> FinalizedExecutionRecord:
        """Create the logically immutable terminal C6 success representation."""
        if not self.search_result_refs:
            raise RuntimeError("successful closure requires an actual Search result ref")
        if self.actual_sample_boundary_ref is None:
            raise RuntimeError("successful closure requires an ActualSampleBoundary ref")
        if self.research_result_ref is None:
            raise RuntimeError("successful closure requires a ResearchResult ref")

        return FinalizedExecutionRecord(
            record_id=ExecutionRecordId(str(uuid4())),
            execution_id=self.execution_id,
            work_request_ref=self.work_request_ref,
            skill_id=self.skill_id,
            skill_version=self.skill_version,
            actual_capabilities=tuple(self.actual_capabilities),
            search_result_refs=tuple(self.search_result_refs),
            actual_sample_boundary_ref=self.actual_sample_boundary_ref,
            evidence_refs=tuple(self.evidence_refs),
            research_result_ref=self.research_result_ref,
            terminal_outcome="SUCCEEDED",
            failure_code=None,
            failure_reason=None,
        )

    def finalize_failure(self) -> FinalizedExecutionRecord:
        """Create the minimum path-sensitive terminal C6 failure record."""
        if self.failure_code is None or self.failure_reason is None:
            raise RuntimeError("failed closure requires bounded failure facts")

        return FinalizedExecutionRecord(
            record_id=ExecutionRecordId(str(uuid4())),
            execution_id=self.execution_id,
            work_request_ref=self.work_request_ref,
            skill_id=self.skill_id,
            skill_version=self.skill_version,
            actual_capabilities=tuple(self.actual_capabilities),
            search_result_refs=tuple(self.search_result_refs),
            actual_sample_boundary_ref=None,
            evidence_refs=(),
            research_result_ref=None,
            terminal_outcome="FAILED",
            failure_code=self.failure_code,
            failure_reason=self.failure_reason,
        )


@dataclass(frozen=True, slots=True)
class FinalizedExecutionRecord:
    """The minimal logically immutable path-sensitive terminal C6 record."""

    record_id: ExecutionRecordId
    execution_id: str
    work_request_ref: str
    skill_id: str
    skill_version: str
    actual_capabilities: tuple[str, ...]
    search_result_refs: tuple[str, ...]
    actual_sample_boundary_ref: str | None
    evidence_refs: tuple[str, ...]
    research_result_ref: str | None
    terminal_outcome: str
    failure_code: str | None
    failure_reason: str | None

    @property
    def required_references(self) -> tuple[str, ...]:
        """Return every OS-controlled referent required for this C6 record."""
        references = [self.work_request_ref, *self.search_result_refs]
        if self.actual_sample_boundary_ref is not None:
            references.append(self.actual_sample_boundary_ref)
        references.extend(self.evidence_refs)
        if self.research_result_ref is not None:
            references.append(self.research_result_ref)
        return tuple(references)


def serialize_work_request(request: BusinessWorkRequest) -> dict[str, object]:
    """Serialize the runtime-owned C1 input representation."""
    return {
        "schema_version": 1,
        "request_id": request.request_id,
        "product_context": request.product_context,
        "market": request.market,
        "platform": request.platform,
        "business_goal": request.business_goal,
        "research_question": request.research_question,
    }


def serialize_finalized_execution_record(
    record: FinalizedExecutionRecord,
) -> dict[str, object]:
    """Serialize C6-owned facts and target-specific internal references."""
    actual_participation: dict[str, object] = {
        "capabilities": list(record.actual_capabilities),
    }
    if record.search_result_refs:
        actual_participation["search_result_refs"] = list(record.search_result_refs)

    payload: dict[str, object] = {
        "schema_version": 1,
        "record_id": record.record_id,
        "execution_id": record.execution_id,
        "work_request_ref": record.work_request_ref,
        "actual_skill": {
            "skill_id": record.skill_id,
            "skill_version": record.skill_version,
        },
        "actual_participation": actual_participation,
        "terminal_outcome": record.terminal_outcome,
        "required_references": list(record.required_references),
    }
    if record.actual_sample_boundary_ref is not None:
        payload["actual_sample_boundary_ref"] = record.actual_sample_boundary_ref
    if record.evidence_refs:
        payload["evidence_refs"] = list(record.evidence_refs)
    if record.research_result_ref is not None:
        payload["research_result_ref"] = record.research_result_ref
    if record.failure_code is not None and record.failure_reason is not None:
        payload["failure"] = {
            "code": record.failure_code,
            "reason": record.failure_reason,
        }
    return payload
