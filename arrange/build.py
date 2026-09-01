#!/usr/bin/env python3
"""Build the canonical and reader-oriented manuscripts in temporary copies."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARRANGE = ROOT / "arrange"


def ignore_source(directory: str, names: list[str]) -> set[str]:
    ignored = {"_build", "__pycache__"}
    for name in names:
        if name.endswith((".aux", ".fdb_latexmk", ".fls", ".log", ".out", ".toc", ".xdv", ".synctex.gz")):
            ignored.add(name)
        if name in {"main.pdf", "proof_free.pdf"}:
            ignored.add(name)
    return ignored


def check_log(log: Path) -> None:
    text = log.read_text(encoding="utf-8", errors="replace")
    if re.search(
        r"LaTeX Warning: (Reference .* undefined|There were undefined references|Label .* multiply defined)",
        text,
    ):
        raise SystemExit(f"undefined or multiply-defined references in {log}")
    overfull = re.findall(r"Overfull \\[hv]box.*", text)
    if overfull:
        raise SystemExit("overfull boxes found:\n" + "\n".join(overfull))


def build_one(source_name: str, output: Path) -> None:
    with tempfile.TemporaryDirectory(prefix=f"hexagon-cover-{source_name}-") as td:
        workspace = Path(td) / "arrange"
        shutil.copytree(ARRANGE, workspace, ignore=ignore_source)
        source = workspace / source_name
        env = os.environ.copy()
        env.update({"SOURCE_DATE_EPOCH": "946684800", "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        subprocess.run(
            [
                "latexmk",
                "-xelatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                "main.tex",
            ],
            cwd=source,
            env=env,
            check=True,
        )
        pdf = source / "main.pdf"
        log = source / "main.log"
        if not pdf.is_file() or not log.is_file():
            raise SystemExit(f"{source_name} build did not produce main.pdf and main.log")
        check_log(log)
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf, output)


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--canonical", action="store_true")
    group.add_argument("--readable", action="store_true")
    group.add_argument("--all", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "arrange/_build")
    args = parser.parse_args()

    if not (args.canonical or args.readable or args.all):
        args.all = True

    if args.canonical or args.all:
        build_one("paper_draft", args.output_dir / "canonical.pdf")
        print(args.output_dir / "canonical.pdf")
    if args.readable or args.all:
        build_one("readable_paper", args.output_dir / "readable.pdf")
        print(args.output_dir / "readable.pdf")


if __name__ == "__main__":
    main()
