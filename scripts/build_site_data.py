#!/usr/bin/env python3
"""Build the dependency-free website catalog from curated CSV registries."""

from __future__ import annotations

import csv
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUT = ROOT / "docs" / "data" / "catalog.json"

DATASETS = {
    "question": ("research_questions.csv", "question_id", "question", "current_answer"),
    "claim": ("claims.csv", "claim_id", "claim", "interpretation_supported"),
    "study": ("studies.csv", "study_id", "short_name", "key_result"),
    "tool": ("tools.csv", "tool_id", "name", "target_construct"),
    "hypothesis": ("hypotheses.csv", "hypothesis_id", "hypothesis", "current_confidence"),
    "cohort": ("cohorts.csv", "cohort_id", "name", "independence_notes"),
    "diagnostic_profile": ("diagnostic_profiles.csv", "profile_id", "name", "next_validation"),
    "case": ("use_cases.csv", "case_id", "title", "scenario"),
    "source": ("source_registry.csv", "ref_id", "title", "topic"),
}


def clean(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def first(row: dict[str, str], *keys: str) -> str:
    for key in keys:
        value = clean(row.get(key))
        if value:
            return value
    return ""


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return [{key: clean(value) for key, value in row.items()} for row in csv.DictReader(handle)]


def main() -> None:
    records: list[dict[str, object]] = []
    counts: dict[str, int] = {}

    for record_type, (filename, id_field, title_field, summary_field) in DATASETS.items():
        rows = read_rows(DATA / filename)
        counts[record_type] = len(rows)
        for row in rows:
            identifier = row[id_field]
            status = first(row, "evidence_status", "status", "validation_status", "current_confidence", "clinical_status")
            state = ""
            if record_type == "question":
                state = first(row, "evidence_status")
            elif record_type == "claim":
                state = first(row, "confidence")
            elif record_type == "hypothesis":
                state = first(row, "current_confidence")
            domain = first(row, "domain", "topic", "category", "level", "cohort_type", "context")
            priority = first(row, "priority")
            title = first(row, title_field, "name", "title", "short_name")
            summary = first(row, summary_field, "key_result", "key_strength", "scenario", "topic")
            fields = [{"label": key.replace("_", " ").title(), "key": key, "value": value} for key, value in row.items() if value]
            search_text = " ".join([identifier, record_type, title, summary, status, domain, priority, *row.values()]).lower()
            records.append({
                "id": identifier,
                "type": record_type,
                "title": title,
                "summary": summary,
                "status": status,
                "state": state,
                "domain": domain,
                "priority": priority,
                "fields": fields,
                "search_text": search_text,
            })

    payload = {
        "release": "v0.5",
        "generated": date.today().isoformat(),
        "site_name": "Cerebral Small Vessel Disease Evidence Atlas",
        "counts": counts,
        "total_records": len(records),
        "records": sorted(records, key=lambda item: (str(item["type"]), str(item["id"]))),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Built {OUTPUT.relative_to(ROOT)} with {len(records)} searchable records.")


if __name__ == "__main__":
    main()
