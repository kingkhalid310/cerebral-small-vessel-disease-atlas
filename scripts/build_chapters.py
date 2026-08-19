#!/usr/bin/env python3
"""Render the maintained Markdown curriculum as dependency-free chapter pages."""

from __future__ import annotations

import html
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content" / "guide"
OUTPUT = ROOT / "docs" / "chapters"
RELEASE = "v0.6"


def load_sources() -> dict[str, dict[str, str]]:
    with (ROOT / "data" / "source_registry.csv").open(encoding="utf-8-sig", newline="") as handle:
        return {row["ref_id"]: row for row in csv.DictReader(handle)}


SOURCES = load_sources()

CHAPTERS = [
    ("00_HOW_TO_THINK.md", "01", "How to think about cSVD", "Foundations", "8 min"),
    ("01_FIELD_PRIMER_V03.md", "02", "The field primer", "Foundations", "24 min"),
    ("15_VESSEL_ANATOMY_AND_NEUROVASCULAR_UNIT.md", "03", "Vessel anatomy and the neurovascular unit", "Foundations", "18 min"),
    ("17_BRAIN_ARTERIOLOSCLEROSIS_DEEP_DIVE.md", "04", "Brain arteriolosclerosis", "Disease", "25 min"),
    ("16_CEREBRAL_AMYLOID_ANGIOPATHY_DEEP_DIVE.md", "05", "Cerebral amyloid angiopathy", "Disease", "24 min"),
    ("18_MRI_PHENOTYPES_AND_STRIVE_2.md", "06", "MRI phenotypes and STRIVE-2", "Imaging", "22 min"),
    ("20_NEUROPATHOLOGY_AND_REFERENCE_STANDARDS.md", "07", "Neuropathology and reference standards", "Pathology", "18 min"),
    ("02_DIAGNOSTIC_CRITERIA_AND_RATING_SYSTEMS.md", "08", "Diagnostic criteria and rating systems", "Diagnosis", "20 min"),
    ("06_DIAGNOSTIC_TRANSPORTABILITY.md", "09", "Diagnostic transportability", "Diagnosis", "7 min"),
    ("03_BIOMARKERS_AND_TOOLS.md", "10", "Biomarkers and tools", "Measurement", "16 min"),
    ("19_MIXED_PATHOLOGY_AND_COGNITIVE_ATTRIBUTION.md", "11", "Mixed pathology and cognitive attribution", "Disease", "17 min"),
    ("21_CLINICAL_SPECTRUM_AND_OUTCOMES.md", "12", "Clinical spectrum and outcomes", "Clinical", "16 min"),
    ("22_MANAGEMENT_PREVENTION_AND_SAFETY.md", "13", "Management, prevention, and safety", "Safety", "17 min"),
    ("23_MONOGENIC_AND_OTHER_SMALL_VESSEL_DISEASES.md", "14", "Monogenic and other small-vessel diseases", "Spectrum", "14 min"),
    ("04_DEBATES_HYPOTHESES_OPEN_QUESTIONS.md", "15", "Debates and open questions", "Mechanisms", "18 min"),
    ("11_DIAGNOSTIC_PROFILES.md", "16", "Diagnostic evidence profiles", "Diagnosis", "6 min"),
    ("12_WORKED_CASES.md", "17", "Worked reasoning cases", "Reasoning", "5 min"),
    ("09_CONTRADICTION_MAP.md", "18", "Contradiction and falsification", "Evidence", "8 min"),
    ("08_EVIDENCE_COMPLETENESS.md", "19", "Evidence completeness", "Evidence", "6 min"),
    ("10_COHORT_LINEAGE.md", "20", "Cohort lineage", "Evidence", "4 min"),
    ("05_RESEARCH_AGENDA_V03.md", "21", "Research agenda", "Research", "10 min"),
    ("07_FROM_ARCHIVE_TO_RESEARCH_PROGRAM.md", "22", "From archive to research program", "Research", "6 min"),
    ("13_LIVING_UPDATE_WORKFLOW.md", "23", "Living update workflow", "Stewardship", "3 min"),
    ("14_READING_PATH.md", "24", "Reading path to research fluency", "Learning", "7 min"),
]

DEEP_FILES = {
    "15_VESSEL_ANATOMY_AND_NEUROVASCULAR_UNIT.md",
    "16_CEREBRAL_AMYLOID_ANGIOPATHY_DEEP_DIVE.md",
    "17_BRAIN_ARTERIOLOSCLEROSIS_DEEP_DIVE.md",
    "18_MRI_PHENOTYPES_AND_STRIVE_2.md",
    "19_MIXED_PATHOLOGY_AND_COGNITIVE_ATTRIBUTION.md",
    "20_NEUROPATHOLOGY_AND_REFERENCE_STANDARDS.md",
    "21_CLINICAL_SPECTRUM_AND_OUTCOMES.md",
    "22_MANAGEMENT_PREVENTION_AND_SAFETY.md",
}

PARTS = [
    ("Part I", "Foundations", "See the hidden system", "Move from normal vessel biology to tissue injury without assigning disease ownership too early.", {"Foundations"}),
    ("Part II", "Diseases and pathology", "Understand the vessel-wall targets", "Study CAA, arteriolosclerosis, mixed disease, and the limitations of neuropathology as a reference.", {"Disease", "Pathology"}),
    ("Part III", "Imaging, diagnosis, and measurement", "Use observations and criteria within scope", "Learn STRIVE-2 phenotypes, diagnostic transportability, biomarkers, and validation ladders.", {"Imaging", "Diagnosis", "Measurement"}),
    ("Part IV", "Clinical spectrum and safety", "Connect biology to human outcomes", "Cover ischemic and hemorrhagic syndromes, cognition, covert disease, management evidence, and the wider cSVD spectrum.", {"Clinical", "Safety", "Spectrum"}),
    ("Part V", "Mechanisms and reasoning", "Think in competing explanations", "Work through live debates and cases while preserving mixed pathology and uncertainty.", {"Mechanisms", "Reasoning"}),
    ("Part VI", "Evidence discipline", "Learn to disagree productively", "Expose contradictions, incomplete validation, and false replication before drawing conclusions.", {"Evidence"}),
    ("Part VII", "Research and stewardship", "Convert uncertainty into work", "Prioritize gaps, design decisive studies, maintain the archive, and build a durable reading practice.", {"Research", "Stewardship", "Learning"}),
]


def slug(filename: str) -> str:
    return filename.lower().replace(".md", "").replace("_v03", "").replace("_", "-")


def inline(value: str) -> str:
    value = html.escape(value, quote=False)
    value = re.sub(r"\[([^]]+)\]\((https?://[^)]+)\)", r'<a href="\2" rel="noopener">\1</a>', value)
    def source_anchor(match: re.Match[str]) -> str:
        ref_id = match.group(1)
        source = SOURCES.get(ref_id)
        if not source or not source.get("doi_or_url"):
            return f'<span class="source-missing">{ref_id}</span>'
        title = html.escape(source["title"], quote=True)
        url = html.escape(source["doi_or_url"], quote=True)
        return f'<a class="source-citation" href="{url}" rel="noopener" title="{title}">{ref_id}<span aria-hidden="true">↗</span></a>'
    value = re.sub(r"\[\[(R\d{3})\]\]", source_anchor, value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    return value


def render_markdown(text: str) -> tuple[str, list[tuple[str, str]]]:
    lines = text.splitlines()
    out: list[str] = []
    toc: list[tuple[str, str]] = []
    paragraph: list[str] = []
    list_type = ""
    i = 0

    def flush_paragraph() -> None:
        if paragraph:
            out.append(f"<p>{inline(' '.join(part.strip() for part in paragraph))}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            out.append(f"</{list_type}>")
            list_type = ""

    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            flush_paragraph(); close_list(); i += 1; continue
        if line.startswith("# "):
            i += 1; continue
        heading = re.match(r"^(##|###)\s+(.+)$", line)
        if heading:
            flush_paragraph(); close_list()
            level = len(heading.group(1)); label = heading.group(2).strip()
            anchor = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
            if level == 2: toc.append((anchor, label))
            out.append(f'<h{level} id="{anchor}">{inline(label)}</h{level}>')
            i += 1; continue
        if line.startswith("> "):
            flush_paragraph(); close_list()
            out.append(f"<blockquote>{inline(line[2:])}</blockquote>")
            i += 1; continue
        if "|" in line and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-+", lines[i + 1]):
            flush_paragraph(); close_list()
            headers = [cell.strip() for cell in line.strip("|").split("|")]
            i += 2; rows: list[list[str]] = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                rows.append([cell.strip() for cell in lines[i].strip("|").split("|")]); i += 1
            out.append('<div class="table-wrap"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in headers) + "</tr></thead><tbody>")
            out.extend("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>" for row in rows)
            out.append("</tbody></table></div>"); continue
        bullet = re.match(r"^[-*]\s+(.+)$", line)
        numbered = re.match(r"^\d+\.\s+(.+)$", line)
        if bullet or numbered:
            flush_paragraph(); desired = "ul" if bullet else "ol"
            if list_type != desired:
                close_list(); list_type = desired; out.append(f"<{desired}>")
            out.append(f"<li>{inline((bullet or numbered).group(1))}</li>")
            i += 1; continue
        paragraph.append(line.strip()); i += 1

    flush_paragraph(); close_list()
    return "\n".join(out), toc


def build_learning_home(nav: list[tuple[str, str, str, str, str]]) -> None:
    sections = []
    for part, label, title, description, stages in PARTS:
        cards = []
        for item_slug, number, item_title, stage, reading in nav:
            if stage not in stages:
                continue
            filename = next(item[0] for item in CHAPTERS if slug(item[0]) == item_slug)
            depth = "DEEP MODULE" if filename in DEEP_FILES else "CORE MODULE"
            cards.append(f'<a class="card course-card" href="chapters/{item_slug}.html"><span class="course-number">{number}</span><div><span class="number">{html.escape(stage.upper())} · {depth} · {html.escape(reading.upper())}</span><h3>{html.escape(item_title)}</h3><p>Open the complete chapter with in-page navigation, point-of-claim sources, and a self-paced reading marker.</p></div></a>')
        sections.append(f'<section class="section{(" alt" if len(sections) % 2 else "")}"><div class="container"><div class="section-heading"><div><p class="eyebrow">{part} · {html.escape(label)}</p><h2>{html.escape(title)}</h2></div><p>{html.escape(description)}</p></div><div class="grid-3">{"".join(cards)}</div></div></section>')
    total_minutes = sum(int(re.search(r"\d+", item[4]).group()) for item in nav)
    page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="A synchronized 24-module curriculum in cerebral small vessel disease."><title>Learn · cSVD Evidence Guide</title><link rel="stylesheet" href="assets/styles.css"></head><body><div id="site-header"></div><main id="main"><section class="page-hero"><div class="container"><p class="eyebrow">The depth and coverage course · {RELEASE}</p><h1>Build a mental model, then inspect the evidence.</h1><p>Twenty-four modules move from normal vessel biology through CAA, brain arteriolosclerosis, STRIVE-2, neuropathology, mixed disease, clinical outcomes, management evidence, the wider disease spectrum, and research design. Approximately {total_minutes} minutes for a first pass; every source marker opens the verification record.</p><div class="hero-actions"><a class="button" href="chapters/{nav[0][0]}.html">Start chapter 1</a><a class="button secondary" href="https://github.com/kingkhalid310/cerebral-small-vessel-disease-evidence-guide/raw/main/downloads/Cerebral_Small_Vessel_Disease_Evidence_Guide_v0.6.docx">Download the synchronized reading edition</a><a class="button secondary" href="coverage.html">Inspect topic coverage</a></div></div></section>{''.join(sections)}</main><div id="site-footer"></div><script src="assets/app.js"></script><script>Guide.shell('learn')</script></body></html>'''
    (ROOT / "docs" / "learn.html").write_text(page, encoding="utf-8")


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    nav = []
    for filename, number, short_title, stage, reading in CHAPTERS:
        nav.append((slug(filename), number, short_title, stage, reading))
    for index, (filename, number, short_title, stage, reading) in enumerate(CHAPTERS):
        markdown = (SOURCE / filename).read_text(encoding="utf-8")
        title = re.search(r"^#\s+(.+)$", markdown, re.M).group(1)
        body, toc = render_markdown(markdown)
        cited_refs = list(dict.fromkeys(re.findall(r"\[\[(R\d{3})\]\]", markdown)))
        if cited_refs:
            source_items = "".join(
                f'<li><a href="{html.escape(SOURCES[ref]["doi_or_url"], quote=True)}" rel="noopener"><strong>{ref}</strong> · {html.escape(SOURCES[ref]["title"])}</a></li>'
                for ref in cited_refs if ref in SOURCES and SOURCES[ref].get("doi_or_url")
            )
            body += f'<section class="chapter-sources"><h2 id="chapter-sources">Sources cited in this chapter</h2><p>Open the original or authoritative record to verify wording, population, methods, and limitations.</p><ol>{source_items}</ol></section>'
        previous_link = f'{nav[index-1][0]}.html' if index else "../learn.html"
        next_link = f'{nav[index+1][0]}.html' if index + 1 < len(nav) else "../pathways.html"
        previous_label = nav[index-1][2] if index else "Learning home"
        next_label = nav[index+1][2] if index + 1 < len(nav) else "Choose a pathway"
        chapter_nav = "".join(
            f'<a href="{item_slug}.html" class="chapter-nav-item{(" current" if item_number == number else "")}"><span>{item_number}</span>{html.escape(item_title)}</a>'
            for item_slug, item_number, item_title, _, _ in nav
        )
        page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{html.escape(title)} — a chapter in the cSVD Evidence Guide."><title>{html.escape(title)} · cSVD Evidence Guide</title>
<link rel="stylesheet" href="../assets/styles.css"></head><body>
<div id="site-header"></div><main id="main" class="reader-layout">
<aside class="reader-sidebar"><a class="reader-home" href="../learn.html">← Learning home</a><p class="sidebar-label">The core course</p><nav aria-label="Course chapters">{chapter_nav}</nav></aside>
<article class="reader-content"><header class="chapter-header"><p class="eyebrow">Chapter {number} · {stage}</p><h1>{html.escape(title)}</h1><div class="chapter-meta"><span>{reading} read</span><span>{"Deep module" if filename in DEEP_FILES else "Core module"}</span><span>{len(cited_refs)} linked sources</span><button class="text-button" data-progress="{slug(filename)}" type="button">Mark complete</button></div></header>
<div class="chapter-toc"><strong>In this chapter</strong>{''.join(f'<a href="#{a}">{html.escape(label)}</a>' for a,label in toc)}</div>
<div class="prose">{body}</div>
<nav class="chapter-pager" aria-label="Chapter navigation"><a href="{previous_link}"><small>Previous</small><strong>{html.escape(previous_label)}</strong></a><a class="next" href="{next_link}"><small>Next</small><strong>{html.escape(next_label)}</strong></a></nav>
</article></main><div id="site-footer"></div><script src="../assets/app.js"></script><script>Guide.shell('learn','../'); Guide.progress();</script></body></html>'''
        (OUTPUT / f"{slug(filename)}.html").write_text(page, encoding="utf-8")
    build_learning_home(nav)
    print(f"Built {len(CHAPTERS)} web-native chapters and the synchronized course home.")


if __name__ == "__main__":
    main()
