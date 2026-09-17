from __future__ import annotations

import json
from pathlib import Path

from .contracts import ExperimentRecord


class ExperimentRegistry:
    """Phase-17 experiment registry; records evidence without claiming validation."""

    REQUIRED_SPIKES = [f"SP-{number:02d}" for number in range(1, 11)]

    def __init__(self, path: str | Path = "runtime/experiments.jsonl") -> None:
        self.path = Path(path)
        self.records: dict[str, ExperimentRecord] = {}

    def register(self, record: ExperimentRecord) -> ExperimentRecord:
        self.records[record.experiment_id] = record
        return record

    def record_result(self, experiment_id: str, metrics: dict[str, float], status: str, decision: str, notes: list[str] | None = None) -> ExperimentRecord:
        record = self.records[experiment_id]
        record.metrics = metrics
        record.status = status
        record.decision = decision
        record.notes = notes or []
        self._persist(record)
        return record

    def pending_spikes(self) -> list[str]:
        return [spike for spike in self.REQUIRED_SPIKES if spike not in self.records or self.records[spike].status == "PENDING"]

    def _persist(self, record: ExperimentRecord) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record.model_dump(mode="json"), ensure_ascii=True) + "\n")
