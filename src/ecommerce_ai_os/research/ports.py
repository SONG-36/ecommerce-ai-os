"""Typed dependency seams between Research and execution coordination."""

from __future__ import annotations

from typing import Protocol

from ecommerce_ai_os.search.models import SearchRequest, SearchResult

from .models import ResearchCompletion, SkillDeclaration


class ResearchExecutionPort(Protocol):
    """The C2a-to-C2b seam for provider-neutral capability needs."""

    def search(self, request: SearchRequest) -> SearchResult | SearchFailure:
        """Request Search through execution-owned coordination."""
        ...


class ResearchSkill(Protocol):
    """The replaceable C2a business-method seam."""

    @property
    def declaration(self) -> SkillDeclaration:
        """Describe stable skill identity and declared dependencies."""
        ...

    def run(self, port: ResearchExecutionPort) -> ResearchCompletion:
        """Perform the business method through an execution-scoped port."""
        ...


# SearchFailure remains a postponed annotation until WI-3 implements its
# complete representation.
