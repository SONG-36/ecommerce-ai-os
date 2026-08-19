"""Stable representations owned by Research."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SkillDeclaration:
    """A skill's stable identity, version, and declared dependencies."""

    skill_id: str
    skill_version: str
    declared_capabilities: frozenset[str]
