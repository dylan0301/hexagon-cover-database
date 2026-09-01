#!/usr/bin/env python3
"""Regenerate interactive publication assets."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEPENDENCY = ROOT / "interactive/_support/generate_dependency_graph.py"
TRACE = ROOT / "interactive/_support/generate_trace_assets.py"
HTML = ROOT / "interactive/readable_proof_dependency_graph.html"
JSON_DATA = ROOT / "interactive/readable_proof_dependency_data.json"


def run(script: Path) -> None:
    subprocess.run([sys.executable, str(script)], cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dependency-graph", action="store_true")
    parser.add_argument("--trace-assets", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if not args.dependency_graph and not args.trace_assets:
        args.dependency_graph = True

    if args.dependency_graph:
        run(DEPENDENCY)
        if JSON_DATA.exists():
            JSON_DATA.unlink()
        if args.check:
            subprocess.run(
                ["git", "diff", "--exit-code", "--", str(HTML.relative_to(ROOT))],
                cwd=ROOT,
                check=True,
            )

    if args.trace_assets:
        run(TRACE)
        if args.check:
            subprocess.run(
                [
                    "git",
                    "diff",
                    "--exit-code",
                    "--",
                    "interactive/trace_exact_ab_envelope_explorer.html",
                    "interactive/trace_exact_ab_presets.json",
                    "arrange/paper_draft/06i_trace_exact_ab_atlas.tex",
                    "arrange/paper_draft/figures/trace_exact_ab",
                ],
                cwd=ROOT,
                check=True,
            )


if __name__ == "__main__":
    main()
