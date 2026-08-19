"""Stable input representations at the execution boundary."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BusinessWorkRequest:
    """A typed C1 business request before any Execution is established."""

    request_id: str
    product_context: str
    market: str
    platform: str
    business_goal: str
    research_question: str
