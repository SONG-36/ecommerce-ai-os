"""Stable representations owned by Research."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SkillDeclaration:
    """A skill's stable identity, version, and declared dependencies."""

    skill_id: str
    skill_version: str
    declared_capabilities: frozenset[str]


@dataclass(frozen=True, slots=True)
class ActualSampleBoundary:
    """The bounded set actually available to the research method."""

    source_search_result_id: str
    returned_item_count: int


@dataclass(frozen=True, slots=True)
class Evidence:
    """An admitted synthetic observation about the bounded Fake result."""

    actual_sample_boundary: ActualSampleBoundary
    observation: str


@dataclass(frozen=True, slots=True)
class ResearchResult:
    """A minimal human-reviewable result with explicit limitations."""

    actual_sample_boundary: ActualSampleBoundary
    evidence: tuple[Evidence, ...]
    limitations: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ResearchCompletion:
    """The in-memory C2a Business Completion handoff to the runtime."""

    research_result: ResearchResult
    actual_sample_boundary: ActualSampleBoundary
    admitted_evidence: tuple[Evidence, ...]
