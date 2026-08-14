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
PROJECTS_DIR = ROOT / "projects"
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
H1_HEADING = re.compile(r"^# (?!#).+", re.MULTILINE)


def project_notebooks() -> list[Path]:
    """Return project notebooks while excluding transient Jupyter checkpoints."""

    if not PROJECTS_DIR.exists():
        return []
    return sorted(
        path
        for path in PROJECTS_DIR.rglob("*.ipynb")
        if ".ipynb_checkpoints" not in path.parts
    )


def validate_structure() -> list[str]:
    errors: list[str] = []

    if not PROJECTS_DIR.is_dir():
        return ["Missing project directory: projects/"]

    root_notebooks = sorted(ROOT.glob("*.ipynb"))
    for path in root_notebooks:
        errors.append(f"Move root-level notebook into projects/: {path.name}")

    project_dirs = sorted(
        path
        for path in PROJECTS_DIR.iterdir()
        if path.is_dir() and not path.name.startswith((".", "_"))
    )
    if not project_dirs:
        errors.append("No project directories were found under projects/.")

    for project_dir in project_dirs:
        notebooks = sorted(project_dir.glob("*.ipynb"))
        if len(notebooks) != 1:
            errors.append(
                f"{project_dir.relative_to(ROOT)}: expected exactly one notebook, "
                f"found {len(notebooks)}"
            )

    for path in project_notebooks():
        if len(path.relative_to(PROJECTS_DIR).parts) != 2:
            errors.append(
                f"{path.relative_to(ROOT)}: notebook must be directly inside its "
                "project directory"
            )

    return errors


def validate_notebooks() -> list[str]:
    errors: list[str] = []
    notebooks = project_notebooks()

    if not notebooks:
        return ["No notebooks were found under projects/."]

    for path in notebooks:
        display_name = path.relative_to(ROOT)
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{display_name}: invalid notebook JSON ({exc})")
            continue

        if notebook.get("nbformat") != 4 or not isinstance(notebook.get("cells"), list):
            errors.append(
                f"{display_name}: expected a version 4 notebook with a cells list"
            )
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
            errors.append(
                f"{display_name}: first markdown cell must start with an H1 title"
            )

        markdown = "\n\n".join(
            "".join(cell.get("source", []))
            for cell in notebook["cells"]
            if cell.get("cell_type") == "markdown"
        )
        h1_headings = H1_HEADING.findall(markdown)
        if len(h1_headings) != 1:
            errors.append(
                f"{display_name}: expected exactly one H1 title, found {len(h1_headings)}"
            )

        normalized_markdown = markdown.casefold()
        if "## project snapshot" not in normalized_markdown:
            errors.append(f"{display_name}: missing a `## Project snapshot` section")
        if "## limitations and next steps" not in normalized_markdown:
            errors.append(
                f"{display_name}: missing a `## Limitations and next steps` section"
            )

        for index, cell in enumerate(notebook["cells"], start=1):
            if cell.get("cell_type") != "code":
                continue

            source = "".join(cell.get("source", []))
            try:
                ast.parse(source, filename=f"{display_name}:cell-{index}")
            except SyntaxError as exc:
                errors.append(
                    f"{display_name}: code cell {index} has invalid Python "
                    f"({exc.msg}, line {exc.lineno})"
                )

            for output in cell.get("outputs", []):
                if output.get("output_type") == "error":
                    name = output.get("ename", "Error")
                    message = output.get("evalue", "")
                    errors.append(
                        f"{display_name}: saved error output in cell {index}: "
                        f"{name}: {message}"
                    )

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
        unquote(target.split("#", 1)[0]).strip("<>")
        for target in MARKDOWN_LINK.findall((ROOT / "README.md").read_text(encoding="utf-8"))
        if target.split("#", 1)[0].endswith(".ipynb")
    }
    notebook_paths = {
        path.relative_to(ROOT).as_posix() for path in project_notebooks()
    }
    for missing in sorted(notebook_paths - linked_notebooks):
        errors.append(f"README.md: notebook is not listed: {missing}")

    return errors


def main() -> int:
    errors = [
        *validate_structure(),
        *validate_notebooks(),
        *validate_markdown_links(),
    ]
    if errors:
        print("Portfolio validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    notebook_count = len(project_notebooks())
    print(f"Portfolio validation passed for {notebook_count} notebooks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
