"""Stable input representations at the execution boundary."""

from dataclasses import dataclass

from ecommerce_ai_os.research.models import SkillDeclaration


@dataclass(frozen=True, slots=True)
class BusinessWorkRequest:
    """A typed C1 business request before any Execution is established."""

    request_id: str
    product_context: str
    market: str
    platform: str
    business_goal: str
    research_question: str


@dataclass(slots=True)
class ExecutionContext:
    """Mutable execution-scoped state used for runtime coordination."""

    execution_id: str
    work_request: BusinessWorkRequest
    skill_declaration: SkillDeclaration
