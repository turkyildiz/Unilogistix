#!/usr/bin/env python3
"""Check foundation structure, local links, metadata, and blueprint coverage."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["README.md", "VISION.md", "MANIFESTO.md", "FOUNDER.md", "CONSTITUTION.md",
            "RULEBOOK.md", "MASTER_ARCHITECTURE.md", "MASTER_INDEX.md", "ROADMAP.md",
            "CHANGELOG.md", "GLOSSARY.md"]


def main():
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f"Missing root document: {name}")
    for name in ["agents", "workflows", "templates", "playbooks", "policies", "prompts",
                 "dashboards", "products/safe-goes", ".github/workflows", ".github/ISSUE_TEMPLATE"]:
        if not (ROOT / name).is_dir():
            errors.append(f"Missing operating area: {name}")
    files = sorted(ROOT.rglob("*.md"))
    for path in files:
        relative = path.relative_to(ROOT)
        text = path.read_text()
        if not text.endswith("\n"):
            errors.append(f"Missing final newline: {relative}")
        if relative.parts[0] in {"archive", "reference"}:
            continue  # Preserved historical inputs are not rewritten to current metadata.
        if not all(marker in text for marker in ["Version:", "Updated:", "Status:", "## Change history"]):
            errors.append(f"Incomplete document metadata: {relative}")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            local = target.split("#")[0]
            if not (path.parent / local).exists():
                errors.append(f"Broken local link: {relative} -> {target}")
    source = (ROOT / "reference/UNI_Master_Blueprint.md").read_text()
    expected_books = 0
    for section in re.split(r"(?m)^# \d+\. ", source):
        match = re.match(r"BOOK (\d+) — ", section)
        if not match:
            continue
        number = int(match.group(1))
        expected_books += 1
        toc = re.search(r"## Table of Contents\n(.*?)(?=\n## )", section, re.S)
        paths = list((ROOT / "books").glob(f"BOOK-{number:02d}-*/README.md"))
        if len(paths) != 1 or not toc or toc.group(1).strip() not in paths[0].read_text():
            errors.append(f"Missing/changed blueprint chapter coverage in book {number}")
    if expected_books != 10:
        errors.append("Expected ten blueprint books")
    for path in [ROOT / "CONSTITUTION.md", ROOT / "RULEBOOK.md", ROOT / "policies/autonomy.md",
                 *sorted((ROOT / "books").glob("*/README.md"))]:
        if "every operational human ask is a failure" not in path.read_text().lower():
            errors.append(f"Missing founder autonomy requirement: {path.relative_to(ROOT)}")
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {len(files)} Markdown files and {expected_books} book chapter lists; {len(errors)} errors.")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
