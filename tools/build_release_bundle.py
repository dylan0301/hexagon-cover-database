#!/usr/bin/env python3
"""Build a deterministic archival bundle for the computer-assisted proof."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXED_TIME = (2000, 1, 1, 0, 0, 0)


def tree_files(root: Path) -> list[Path]:
    """Return source files while excluding interpreter/build caches."""

    return [
        path
        for path in root.rglob("*")
        if path.is_file()
        and not {"__pycache__", ".lake", ".git"}.intersection(path.parts)
        and path.suffix not in {".pyc", ".pyo"}
    ]


def files() -> list[Path]:
    paths = [
        ROOT / "LICENSE",
        ROOT / "README.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "REPRODUCE.md",
        ROOT / "requirements-proof.txt",
        ROOT / ".github/CODEOWNERS",
        ROOT / ".github/pull_request_template.md",
        ROOT / ".github/workflows/paper-rebuild.yml",
        ROOT / ".github/workflows/proof-ci.yml",
        ROOT / "arrange/CURRENT_VERIFICATION_SUMMARY.txt",
        ROOT / "arrange/ams_paper_generation_guide.md",
        ROOT / "arrange/paper_proof_crosswalk.md",
        ROOT / "release/RELEASE_CONTENTS.md",
    ]
    paths.extend(tree_files(ROOT / "proof"))
    paths.extend(tree_files(ROOT / "formalization/strategy2_optimization"))
    paths.extend(tree_files(ROOT / "tools"))

    paper = ROOT / "arrange/paper_draft"
    paper_source_suffixes = {
        ".tex", ".bib", ".sty", ".cls", ".md",
        ".png", ".jpg", ".jpeg", ".webp", ".svg",
    }
    paths.extend(
        path
        for path in tree_files(paper)
        if path.suffix.lower() in paper_source_suffixes
        or path
        in {
            paper / "main.pdf",
            paper / "statements_only" / "main.pdf",
        }
    )
    return sorted(set(paths), key=lambda path: path.relative_to(ROOT).as_posix())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path, default=ROOT / "release/hexagon-cover-proof-bundle.zip"
    )
    args = parser.parse_args()
    selected = files()
    missing = [path for path in selected if not path.is_file()]
    if missing:
        raise SystemExit("missing release inputs:\n" + "\n".join(map(str, missing)))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in selected:
            relative = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(relative, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            mode = 0o100755 if path.stat().st_mode & 0o111 else 0o100644
            info.external_attr = mode << 16
            zf.writestr(info, path.read_bytes())
    print(args.output)


if __name__ == "__main__":
    main()
