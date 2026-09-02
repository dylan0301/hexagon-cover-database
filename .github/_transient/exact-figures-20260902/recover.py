#!/usr/bin/env python3
from __future__ import annotations

import runpy
import subprocess
import sys
from pathlib import Path


def root(start: Path) -> Path:
    for p in (start.resolve(), *start.resolve().parents):
        if (p / "AGENTS.md").is_file():
            return p
    raise SystemExit("repository root not found")


ROOT = root(Path(__file__))
GENERATOR = ROOT / "arrange/paper_draft/figures/exact/generate.py"
ORIGINAL = ROOT / ".github/_transient/exact-figures-20260902/apply.py"

if GENERATOR.is_file() and (GENERATOR.parent / "manifest.json").is_file():
    subprocess.run([sys.executable, str(GENERATOR), "--check"], cwd=ROOT, check=True)
else:
    if not ORIGINAL.is_file():
        raise SystemExit("neither a completed exact-figure generator nor the migration payload exists")
    sys.argv = [str(ORIGINAL), "--migrate"]
    runpy.run_path(str(ORIGINAL), run_name="__main__")
