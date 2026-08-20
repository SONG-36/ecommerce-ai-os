"""Physical placement and publication of Local JSON Execution Bundles."""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
from typing import Mapping, Sequence

from .execution_record import ExecutionRecordRef


class LocalJsonRetention:
    """Own the selected execution-bundle root and local Record Ref resolution."""

    def __init__(self, root: Path) -> None:
        self.root = root

    def begin_execution(self, execution_id: str) -> StagingExecutionBundle:
        """Create one new staging bundle for an established Execution."""
        return StagingExecutionBundle(self.root, execution_id)

    def resolve_record_ref(self, record_ref: ExecutionRecordRef) -> Path:
        """Resolve a published C6 Record Ref within this retention root."""
        path = self.root / record_ref.execution_id / record_ref.relative_path
        if not path.is_file():
            raise FileNotFoundError(f"Execution Record Ref does not resolve: {record_ref}")
        return path


class StagingExecutionBundle:
    """One execution-scoped STAGING bundle before atomic publication."""

    def __init__(self, root: Path, execution_id: str) -> None:
        self.execution_id = execution_id
        self.staging_path = root / ".staging" / execution_id
        self.final_path = root / execution_id
        self._record_ref: ExecutionRecordRef | None = None

        if self.final_path.exists() or self.staging_path.exists():
            raise FileExistsError(f"Execution bundle already exists: {execution_id}")
        self.staging_path.mkdir(parents=True)

    @property
    def record_ref(self) -> ExecutionRecordRef | None:
        """Expose no Record Ref until atomic publication has succeeded."""
        return self._record_ref

    def write_json(self, relative_ref: str, payload: Mapping[str, object]) -> str:
        """Place one owner-serialized referent in the staging bundle."""
        if self._record_ref is not None:
            raise RuntimeError("published execution bundle is immutable")
        if relative_ref == "execution_record.json":
            raise ValueError("execution_record.json must be written by publish() last")

        path = self._staging_file(relative_ref)
        path.parent.mkdir(parents=True, exist_ok=True)
        self._write_json(path, payload)
        return relative_ref

    def publish(
        self,
        execution_record_payload: Mapping[str, object],
        required_references: Sequence[str],
    ) -> ExecutionRecordRef:
        """Write C6 last, validate required refs, then atomically publish."""
        if self._record_ref is not None:
            raise RuntimeError("execution bundle is already published")

        record_path = self.staging_path / "execution_record.json"
        self._write_json(record_path, execution_record_payload)

        missing = [
            relative_ref
            for relative_ref in required_references
            if not self._staging_file(relative_ref).is_file()
        ]
        if missing:
            raise RuntimeError(
                "required execution references do not resolve: " + ", ".join(missing)
            )

        if not record_path.is_file():
            raise RuntimeError("finalized execution record was not written")
        self.staging_path.rename(self.final_path)
        self._record_ref = ExecutionRecordRef(execution_id=self.execution_id)
        return self._record_ref

    def _staging_file(self, relative_ref: str) -> Path:
        relative_path = PurePosixPath(relative_ref)
        if (
            relative_path.is_absolute()
            or not relative_path.parts
            or ".." in relative_path.parts
        ):
            raise ValueError(f"invalid execution-bundle reference: {relative_ref}")
        return self.staging_path.joinpath(*relative_path.parts)

    @staticmethod
    def _write_json(path: Path, payload: Mapping[str, object]) -> None:
        with path.open("w", encoding="utf-8") as stream:
            json.dump(payload, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write("\n")
