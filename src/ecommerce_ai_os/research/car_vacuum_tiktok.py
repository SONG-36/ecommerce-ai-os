"""The minimal First-Slice Research business method."""

from dataclasses import dataclass, field

from ecommerce_ai_os.search.models import SearchRequest

from .models import (
    ActualSampleBoundary,
    Evidence,
    ResearchCompletion,
    ResearchResult,
    SkillDeclaration,
)
from .ports import ResearchExecutionPort


@dataclass(frozen=True, slots=True)
class CarVacuumTikTokResearchSkill:
    """Form a synthetic P3 Research result through provider-neutral Search."""

    search_request: SearchRequest
    declaration: SkillDeclaration = field(
        default=SkillDeclaration(
            skill_id="car-vacuum-tiktok-research",
            skill_version="1",
            declared_capabilities=frozenset({"Search"}),
        ),
        init=False,
    )

    def run(self, port: ResearchExecutionPort) -> ResearchCompletion:
        """Execute the minimal business method and declare Business Completion."""
        search_result = port.search(self.search_request)
        sample_boundary = ActualSampleBoundary(
            source_search_result_id=search_result.search_result_id,
            returned_item_count=search_result.returned_item_count,
        )

        limitations = [
            "Synthetic / Fake execution evidence only; no real TikTok or "
            "commerce conclusion is supported."
        ]
        if search_result.returned_item_count == 0:
            evidence: tuple[Evidence, ...] = ()
            limitations.append(
                "No fake items were returned; evidence is insufficient for a "
                "substantive research conclusion."
            )
        else:
            evidence = (
                Evidence(
                    actual_sample_boundary=sample_boundary,
                    observation=(
                        "WI-1 Fake Search returned a bounded result containing "
                        f"{search_result.returned_item_count} synthetic item(s)."
                    ),
                ),
            )

        research_result = ResearchResult(
            actual_sample_boundary=sample_boundary,
            evidence=evidence,
            limitations=tuple(limitations),
        )
        return ResearchCompletion(
            research_result=research_result,
            actual_sample_boundary=sample_boundary,
            admitted_evidence=evidence,
        )
