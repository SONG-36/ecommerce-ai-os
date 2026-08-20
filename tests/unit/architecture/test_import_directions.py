import ast
from pathlib import Path
import unittest


SOURCE_ROOT = Path(__file__).resolve().parents[3] / "src" / "ecommerce_ai_os"
CORE_PACKAGES = frozenset({"research", "search", "runtime", "providers"})


def imported_modules(source_path: Path) -> tuple[tuple[int, str], ...]:
    """Return project-local imports resolved from one source module."""
    relative_path = source_path.relative_to(SOURCE_ROOT).with_suffix("")
    module_parts = ("ecommerce_ai_os", *relative_path.parts)
    package_parts = module_parts[:-1]
    imports: list[tuple[int, str]] = []

    for node in ast.walk(ast.parse(source_path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            imports.extend(
                (node.lineno, alias.name)
                for alias in node.names
                if alias.name == "ecommerce_ai_os"
                or alias.name.startswith("ecommerce_ai_os.")
            )
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                retained_parts = len(package_parts) - (node.level - 1)
                base_parts = package_parts[:retained_parts]
                imported_module = ".".join(
                    (*base_parts, *(node.module or "").split("."))
                ).rstrip(".")
            else:
                imported_module = node.module or ""

            if imported_module == "ecommerce_ai_os" or imported_module.startswith(
                "ecommerce_ai_os."
            ):
                imports.append((node.lineno, imported_module))
                imports.extend(
                    (node.lineno, f"{imported_module}.{alias.name}")
                    for alias in node.names
                    if alias.name != "*"
                )

    return tuple(imports)


def forbidden_reason(source_family: str, imported_module: str) -> str | None:
    """Classify one forbidden reviewed dependency direction, if any."""
    imported_parts = imported_module.split(".")
    if len(imported_parts) < 2 or imported_parts[0] != "ecommerce_ai_os":
        return None

    target_family = imported_parts[1]
    target_suffix = ".".join(imported_parts[1:])

    if source_family in CORE_PACKAGES and target_family in {
        "composition",
        "application",
    }:
        return "core packages must not import composition or application"

    if source_family == "research" and (
        target_family in {"runtime", "providers"}
        or target_suffix == "search.port"
        or target_suffix.startswith("search.port.")
    ):
        return "research may use search.models but not runtime/providers/search.port"

    if source_family == "search" and target_family in {
        "runtime",
        "research",
        "providers",
    }:
        return "search must remain stdlib-only and provider-neutral"

    if source_family == "runtime" and (
        target_family == "providers"
        or target_suffix == "research.car_vacuum_tiktok"
        or target_suffix.startswith("research.car_vacuum_tiktok.")
        or target_suffix == "search.fake"
        or target_suffix.startswith("search.fake.")
    ):
        return "runtime must not import concrete Skill, Fake Search, or Provider"

    if source_family == "providers" and target_family in {"runtime", "research"}:
        return "providers must not import runtime or research"

    return None


class ImportDirectionTests(unittest.TestCase):
    def test_reviewed_import_dag_holds_for_the_current_source_tree(self) -> None:
        violations: list[str] = []

        for source_path in sorted(SOURCE_ROOT.rglob("*.py")):
            relative_path = source_path.relative_to(SOURCE_ROOT)
            source_family = relative_path.parts[0]
            if source_family not in CORE_PACKAGES:
                continue

            for line_number, imported_module in imported_modules(source_path):
                reason = forbidden_reason(source_family, imported_module)
                if reason is not None:
                    violations.append(
                        f"{relative_path}:{line_number}: {imported_module}: {reason}"
                    )

        self.assertEqual(violations, [])


if __name__ == "__main__":
    unittest.main()
