#!/usr/bin/env python3
"""Build and verify synchronized document, repository, and website views."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "release"
CONFIG = RELEASE / "release.json"
MANIFEST = RELEASE / "sync_manifest.json"

CANONICAL_PATTERNS = (
    "content/guide/*.md",
    "data/*.csv",
    "data/*.json",
    "governance/*.md",
    "schemas/*.json",
    "scripts/build_site_data.py",
    "scripts/build_chapters.py",
    "scripts/build_reading_edition.py",
    "scripts/docx_base.py",
    "scripts/sync_release.py",
    "scripts/validate.py",
    "requirements-docs.txt",
    "release/release.json",
)


def files_for(patterns: tuple[str, ...]) -> list[Path]:
    paths: set[Path] = set()
    for pattern in patterns:
        paths.update(path for path in ROOT.glob(pattern) if path.is_file())
    return sorted(paths, key=lambda path: path.relative_to(ROOT).as_posix())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def hash_map(paths: list[Path]) -> dict[str, str]:
    return {path.relative_to(ROOT).as_posix(): sha256(path) for path in paths}


def aggregate_digest(values: dict[str, str]) -> str:
    payload = "\n".join(f"{name}\t{digest}" for name, digest in sorted(values.items()))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def output_paths(config: dict[str, object]) -> list[Path]:
    chapters = sorted((ROOT / "docs" / "chapters").glob("*.html"))
    fixed = [
        ROOT / "docs" / "index.html",
        ROOT / "docs" / "learn.html",
        ROOT / "docs" / "data" / "catalog.json",
        ROOT / str(config["document_output"]),
        ROOT / "release" / "reading_edition_summary.json",
    ]
    return sorted([path for path in fixed + chapters if path.is_file()], key=lambda path: path.relative_to(ROOT).as_posix())


def snapshot(config: dict[str, object]) -> dict[str, object]:
    source_hashes = hash_map(files_for(CANONICAL_PATTERNS))
    outputs = output_paths(config)
    output_hashes = hash_map(outputs)
    return {
        "release_version": config["release_version"],
        "product_version": config["product_version"],
        "release_date": config["release_date"],
        "chapter_count": len(list((ROOT / "docs" / "chapters").glob("*.html"))),
        "canonical_digest": aggregate_digest(source_hashes),
        "canonical_files": source_hashes,
        "published_digest": aggregate_digest(output_hashes),
        "published_files": output_hashes,
    }


def supports_document_build(executable: Path) -> bool:
    if not executable.exists():
        return False
    probe = subprocess.run(
        [str(executable), "-c", "import PIL, docx"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return probe.returncode == 0


def document_python() -> Path:
    candidates = [
        Path(os.environ["CSVD_DOCX_PYTHON"]).expanduser() if os.environ.get("CSVD_DOCX_PYTHON") else None,
        Path(sys.executable),
        ROOT / ".venv" / "bin" / "python3",
        Path.home() / ".cache" / "codex-runtimes" / "codex-primary-runtime" / "dependencies" / "python" / "bin" / "python3",
    ]
    for candidate in candidates:
        if candidate and supports_document_build(candidate):
            return candidate
    raise RuntimeError(
        "The Word builder requires Pillow and python-docx. Install requirements-docs.txt "
        "in .venv or set CSVD_DOCX_PYTHON to a compatible Python executable."
    )


def run(script: str, executable: Path | None = None) -> None:
    subprocess.run([str(executable or Path(sys.executable)), str(ROOT / "scripts" / script)], cwd=ROOT, check=True)


def check_mode(config: dict[str, object]) -> int:
    if not MANIFEST.exists():
        print("Synchronization manifest is missing. Run the full synchronizer.", file=sys.stderr)
        return 1
    expected = json.loads(MANIFEST.read_text(encoding="utf-8"))
    current = snapshot(config)
    comparable = ("release_version", "product_version", "release_date", "chapter_count", "canonical_digest", "canonical_files", "published_digest", "published_files")
    differences = [key for key in comparable if expected.get(key) != current.get(key)]
    if differences:
        print(json.dumps({"status": "drift", "different_fields": differences}, indent=2))
        return 1
    print(json.dumps({"status": "synchronized", "release_version": config["release_version"], "canonical_digest": current["canonical_digest"], "published_digest": current["published_digest"]}, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="detect drift without rebuilding")
    args = parser.parse_args()
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    if args.check:
        return check_mode(config)

    run("build_site_data.py")
    run("build_chapters.py")
    run("build_reading_edition.py", document_python())
    run("validate.py")
    result = snapshot(config)
    result["generated_at_utc"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    result["status"] = "synchronized"
    RELEASE.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "manifest": str(MANIFEST), "canonical_digest": result["canonical_digest"], "published_digest": result["published_digest"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
