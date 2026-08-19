#!/usr/bin/env python3
"""Validate identifiers, relationships, website data, and the public boundary."""

from __future__ import annotations

import csv
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            self.targets.append(values["href"] or "")
        if tag in {"img", "script"} and values.get("src"):
            self.targets.append(values["src"] or "")
        if tag == "link" and values.get("href"):
            self.targets.append(values["href"] or "")


def rows(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def ids(name: str, field: str) -> set[str]:
    return {row[field].strip() for row in rows(name)}


def split_ids(value: str) -> set[str]:
    return {part.strip() for part in re.split(r"[;,]", value or "") if part.strip()}


def check_unique(name: str, field: str) -> bool:
    values = [row[field].strip() for row in rows(name)]
    return bool(values) and len(values) == len(set(values)) and all(values)


def main() -> int:
    sources = ids("source_registry.csv", "ref_id")
    studies = ids("studies.csv", "study_id")
    claims = ids("claims.csv", "claim_id")
    questions = ids("research_questions.csv", "question_id")
    tools = ids("tools.csv", "tool_id")

    checks: dict[str, bool] = {
        "unique_sources": check_unique("source_registry.csv", "ref_id"),
        "unique_studies": check_unique("studies.csv", "study_id"),
        "unique_claims": check_unique("claims.csv", "claim_id"),
        "unique_questions": check_unique("research_questions.csv", "question_id"),
        "unique_tools": check_unique("tools.csv", "tool_id"),
        "unique_hypotheses": check_unique("hypotheses.csv", "hypothesis_id"),
        "unique_cohorts": check_unique("cohorts.csv", "cohort_id"),
        "unique_profiles": check_unique("diagnostic_profiles.csv", "profile_id"),
        "unique_cases": check_unique("use_cases.csv", "case_id"),
    }

    study_rows = rows("studies.csv")
    edge_rows = rows("claim_evidence.csv")
    question_link_rows = rows("question_evidence.csv")
    tool_rows = rows("tools.csv")
    checks["study_sources_resolve"] = all(row["ref_id"] in sources for row in study_rows)
    checks["claim_edges_resolve"] = all(
        row["claim_id"] in claims and (row["evidence_id"] in studies or row["evidence_id"] in sources)
        for row in edge_rows
    )
    checks["question_links_resolve"] = all(
        row["question_id"] in questions
        and (not row.get("claim_id") or row["claim_id"] in claims)
        and (not row.get("study_id") or row["study_id"] in studies)
        for row in question_link_rows
    )
    checks["tool_sources_resolve"] = all(split_ids(row.get("key_refs", "")) <= sources for row in tool_rows)
    checks["question_design_complete"] = all(
        row.get("current_answer", "").strip()
        and row.get("critical_missing_piece", "").strip()
        and row.get("decisive_design", "").strip()
        for row in rows("research_questions.csv")
    )
    checks["claim_boundaries_complete"] = all(
        row.get("interpretation_supported", "").strip()
        and row.get("not_established", "").strip()
        and row.get("decisive_test", "").strip()
        for row in rows("claims.csv")
    )

    catalog_path = ROOT / "docs" / "data" / "catalog.json"
    checks["catalog_present"] = catalog_path.exists()
    if catalog_path.exists():
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        expected_total = sum(catalog.get("counts", {}).values())
        checks["catalog_count_consistent"] = expected_total == catalog.get("total_records") == len(catalog.get("records", []))
        checks["catalog_ids_unique"] = len({record["id"] for record in catalog["records"]}) == len(catalog["records"])

    required_site = ["index.html", "explore.html", "record.html", "learn.html", "pathways.html", "workbench.html", "methodology.html", "about.html", "assets/styles.css", "assets/app.js"]
    checks["site_complete"] = all((ROOT / "docs" / item).exists() for item in required_site)
    checks["web_chapters_complete"] = len(list((ROOT / "docs" / "chapters").glob("*.html"))) == 15
    checks["figures_present"] = len(list((ROOT / "docs" / "assets" / "figures").glob("*.png"))) == 14
    reading_edition = ROOT / "downloads" / "Cerebral_Small_Vessel_Disease_Evidence_Guide_v0.5.docx"
    checks["reading_edition_present"] = reading_edition.exists() and reading_edition.stat().st_size > 0

    broken_links: list[str] = []
    for html_path in (ROOT / "docs").rglob("*.html"):
        parser = LinkParser()
        parser.feed(html_path.read_text(encoding="utf-8"))
        for target in parser.targets:
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith(("//", "#", "mailto:")):
                continue
            local_target = unquote(parsed.path)
            if not local_target or "${" in local_target:
                continue
            resolved = (html_path.parent / local_target).resolve()
            if not resolved.exists():
                broken_links.append(f"{html_path.relative_to(ROOT)} -> {target}")
    checks["static_links_resolve"] = not broken_links

    sensitive = re.compile(r"(?i)(\bmrn\s*[:=]|\bdob\s*[:=]|id_merge|@mgh|accession[_ ]?(number|id)\s*[:=])")
    hits: list[str] = []
    scan_suffixes = {".md", ".csv", ".json", ".html", ".css", ".js", ".yml", ".yaml"}
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in scan_suffixes and ".git" not in path.parts:
            for number, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
                if sensitive.search(line):
                    hits.append(f"{path.relative_to(ROOT)}:{number}")
    checks["public_boundary_scan_clean"] = not hits

    status = "pass" if all(checks.values()) else "fail"
    result = {"status": status, "checks": checks, "sensitive_hits": hits, "broken_links": broken_links}
    print(json.dumps(result, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
