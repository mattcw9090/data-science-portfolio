#!/usr/bin/env python3
"""Run fast, dependency-free checks for this notebook portfolio."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def validate_notebooks() -> list[str]:
    errors: list[str] = []
    notebooks = sorted(ROOT.glob("*.ipynb"))

    if not notebooks:
        return ["No root-level notebooks were found."]

    for path in notebooks:
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.name}: invalid notebook JSON ({exc})")
            continue

        if notebook.get("nbformat") != 4 or not isinstance(notebook.get("cells"), list):
            errors.append(f"{path.name}: expected a version 4 notebook with a cells list")
            continue

        first_markdown = next(
            (
                "".join(cell.get("source", [])).lstrip()
                for cell in notebook["cells"]
                if cell.get("cell_type") == "markdown"
                and "".join(cell.get("source", [])).strip()
            ),
            "",
        )
        if not first_markdown.startswith("# "):
            errors.append(f"{path.name}: first markdown cell must start with an H1 title")

        for index, cell in enumerate(notebook["cells"], start=1):
            if cell.get("cell_type") != "code":
                continue

            source = "".join(cell.get("source", []))
            try:
                ast.parse(source, filename=f"{path.name}:cell-{index}")
            except SyntaxError as exc:
                errors.append(
                    f"{path.name}: code cell {index} has invalid Python "
                    f"({exc.msg}, line {exc.lineno})"
                )

            for output in cell.get("outputs", []):
                if output.get("output_type") == "error":
                    name = output.get("ename", "Error")
                    message = output.get("evalue", "")
                    errors.append(f"{path.name}: saved error output in cell {index}: {name}: {message}")

    return errors


def validate_markdown_links() -> list[str]:
    errors: list[str] = []
    docs = [ROOT / "README.md", ROOT / "datasets" / "README.md"]

    for doc in docs:
        if not doc.exists():
            errors.append(f"Missing documentation file: {doc.relative_to(ROOT)}")
            continue

        text = doc.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
            parsed = urlparse(target)
            if parsed.scheme or target.startswith(("#", "mailto:")):
                continue

            relative_target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if relative_target and not (doc.parent / relative_target).resolve().exists():
                errors.append(
                    f"{doc.relative_to(ROOT)}: broken local link `{relative_target}`"
                )

    linked_notebooks = {
        unquote(target.split("#", 1)[0])
        for target in MARKDOWN_LINK.findall((ROOT / "README.md").read_text(encoding="utf-8"))
        if target.split("#", 1)[0].endswith(".ipynb")
    }
    notebook_names = {path.name for path in ROOT.glob("*.ipynb")}
    for missing in sorted(notebook_names - linked_notebooks):
        errors.append(f"README.md: notebook is not listed: {missing}")

    return errors


def main() -> int:
    errors = [*validate_notebooks(), *validate_markdown_links()]
    if errors:
        print("Portfolio validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    notebook_count = len(list(ROOT.glob("*.ipynb")))
    print(f"Portfolio validation passed for {notebook_count} notebooks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
