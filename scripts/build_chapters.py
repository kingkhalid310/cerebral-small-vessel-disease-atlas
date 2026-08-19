#!/usr/bin/env python3
"""Render the maintained Markdown curriculum as dependency-free chapter pages."""

from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content" / "guide"
OUTPUT = ROOT / "docs" / "chapters"

CHAPTERS = [
    ("00_HOW_TO_THINK.md", "01", "How to think about cSVD", "Foundations", "8 min"),
    ("01_FIELD_PRIMER_V03.md", "02", "The field primer", "Foundations", "24 min"),
    ("06_DIAGNOSTIC_TRANSPORTABILITY.md", "03", "Diagnostic transportability", "Diagnosis", "7 min"),
    ("11_DIAGNOSTIC_PROFILES.md", "04", "Diagnostic evidence profiles", "Diagnosis", "6 min"),
    ("12_WORKED_CASES.md", "05", "Worked reasoning cases", "Reasoning", "5 min"),
    ("09_CONTRADICTION_ATLAS.md", "06", "Contradiction and falsification", "Evidence", "8 min"),
    ("08_EVIDENCE_COMPLETENESS.md", "07", "Evidence completeness", "Evidence", "6 min"),
    ("10_COHORT_LINEAGE.md", "08", "Cohort lineage", "Evidence", "4 min"),
    ("05_RESEARCH_AGENDA_V03.md", "09", "Research agenda", "Research", "10 min"),
    ("07_FROM_ARCHIVE_TO_RESEARCH_PROGRAM.md", "10", "From archive to research program", "Research", "6 min"),
    ("13_LIVING_UPDATE_WORKFLOW.md", "11", "Living update workflow", "Stewardship", "3 min"),
]


def slug(filename: str) -> str:
    return filename.lower().replace(".md", "").replace("_v03", "").replace("_", "-")


def inline(value: str) -> str:
    value = html.escape(value, quote=False)
    value = re.sub(r"\[([^]]+)\]\((https?://[^)]+)\)", r'<a href="\2" rel="noopener">\1</a>', value)
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


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    nav = []
    for filename, number, short_title, stage, reading in CHAPTERS:
        nav.append((slug(filename), number, short_title, stage, reading))
    for index, (filename, number, short_title, stage, reading) in enumerate(CHAPTERS):
        markdown = (SOURCE / filename).read_text(encoding="utf-8")
        title = re.search(r"^#\s+(.+)$", markdown, re.M).group(1)
        body, toc = render_markdown(markdown)
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
<meta name="description" content="{html.escape(title)} — a chapter in the cSVD Evidence Atlas."><title>{html.escape(title)} · cSVD Atlas</title>
<link rel="stylesheet" href="../assets/styles.css"></head><body>
<div id="site-header"></div><main id="main" class="reader-layout">
<aside class="reader-sidebar"><a class="reader-home" href="../learn.html">← Learning home</a><p class="sidebar-label">The core course</p><nav aria-label="Course chapters">{chapter_nav}</nav></aside>
<article class="reader-content"><header class="chapter-header"><p class="eyebrow">Chapter {number} · {stage}</p><h1>{html.escape(title)}</h1><div class="chapter-meta"><span>{reading} read</span><button class="text-button" data-progress="{slug(filename)}" type="button">Mark complete</button></div></header>
<div class="chapter-toc"><strong>In this chapter</strong>{''.join(f'<a href="#{a}">{html.escape(label)}</a>' for a,label in toc)}</div>
<div class="prose">{body}</div>
<nav class="chapter-pager" aria-label="Chapter navigation"><a href="{previous_link}"><small>Previous</small><strong>{html.escape(previous_label)}</strong></a><a class="next" href="{next_link}"><small>Next</small><strong>{html.escape(next_label)}</strong></a></nav>
</article></main><div id="site-footer"></div><script src="../assets/app.js"></script><script>Atlas.shell('learn','../'); Atlas.progress();</script></body></html>'''
        (OUTPUT / f"{slug(filename)}.html").write_text(page, encoding="utf-8")
    print(f"Built {len(CHAPTERS)} web-native chapters in {OUTPUT.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
