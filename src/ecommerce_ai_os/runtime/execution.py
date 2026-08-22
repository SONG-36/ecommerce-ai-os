"""Stable input and return representations at the execution boundary."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, TypeAlias

from ecommerce_ai_os.research.models import ResearchResult, SkillDeclaration

if TYPE_CHECKING:
    from .execution_record import ExecutionRecordRef


@dataclass(frozen=True, slots=True)
class BusinessWorkRequest:
    """A typed C1 business request before any Execution is established."""

    request_id: str
    product_context: str
    market: str
    platform: str
    business_goal: str
    research_question: str


@dataclass(frozen=True, slots=True)
class PreExecutionRejection:
    """C1 rejection returned before any Execution identity exists."""

    reason: str


@dataclass(slots=True)
class ExecutionContext:
    """Mutable execution-scoped state used for runtime coordination."""

    execution_id: str
    work_request: BusinessWorkRequest
    skill_declaration: SkillDeclaration


@dataclass(frozen=True, slots=True)
class TerminalReturn:
    """C1 terminal return for an already-established Execution."""

    execution_id: str
    execution_outcome: str
    business_result: ResearchResult | None
    record_ref: ExecutionRecordRef | None


TaskExecutionResponse: TypeAlias = PreExecutionRejection | TerminalReturn
