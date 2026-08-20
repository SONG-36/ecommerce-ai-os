"""Static concrete assembly for the First-Slice executable path."""

from pathlib import Path

from ecommerce_ai_os.research.car_vacuum_tiktok import (
    CarVacuumTikTokResearchSkill,
)
from ecommerce_ai_os.runtime.retention import LocalJsonRetention
from ecommerce_ai_os.runtime.task_runtime import TaskRuntime
from ecommerce_ai_os.search.fake import FakeSearchCapability
from ecommerce_ai_os.search.models import SearchRequest


def build_fake_first_slice_runtime(execution_root: Path) -> TaskRuntime:
    """Wire the WI-1 Fake Search, concrete Skill, Runtime, and retention root."""
    search_capability = FakeSearchCapability()
    research_skill = CarVacuumTikTokResearchSkill(
        search_request=SearchRequest(query="car vacuum", market="US")
    )
    retention = LocalJsonRetention(execution_root)
    return TaskRuntime(
        search_capability=search_capability,
        research_skill=research_skill,
        retention=retention,
    )
