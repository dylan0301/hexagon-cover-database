#!/usr/bin/env python3
"""Finish the exact-figure migration already staged on this branch.

This file is delivery-only.  It patches either the staged migration program or
an already-generated permanent program, regenerates all formula-driven assets,
and leaves the permanent generator responsible for the full mathematical audit.
"""
from __future__ import annotations

import importlib.util
import json
import re
import runpy
import subprocess
import sys
from pathlib import Path


def repo_root(start: Path) -> Path:
    for candidate in (start.resolve(), *start.resolve().parents):
        if (candidate / "AGENTS.md").is_file() and (candidate / "arrange").is_dir():
            return candidate
    raise SystemExit("repository root not found")


ROOT = repo_root(Path(__file__))
STAGED = ROOT / ".github/_transient/exact-figures-20260902/apply.py"
PERMANENT = ROOT / "arrange/paper_draft/figures/exact/generate.py"
MANIFEST = ROOT / "arrange/paper_draft/figures/exact/manifest.json"


def patch_source(path: Path) -> None:
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    original = text

    # Store path coordinates to twelve decimal places.  Formula inputs remain
    # exact rational/algebraic data in the manifest; this controls only the PDF
    # and SVG serialization error.
    text = text.replace('return f"{value:.5f}"', 'return f"{value:.12f}"')

    # The first staged search was too narrow to guarantee a robust Vd2
    # specimen.  Search a deterministic rational grid large enough to cover all
    # normalized V classes while preserving exact, reproducible parameters.
    text = text.replace(
        "for dx_num in range(-24, 25, 2):\n            for dy_num in range(-24, 25, 2):",
        "for dx_num in range(-80, 41, 2):\n            for dy_num in range(-50, 51, 2):",
    )
    text = text.replace(
        "for dx_num in range(-20, 31, 2):\n            for dy_num in range(-26, 27, 2):",
        "for dx_num in range(-80, 41, 2):\n            for dy_num in range(-50, 51, 2):",
    )

    # figures/tikz_setup.tex is a style support file, not a paper figure.  The
    # recursive input scan must never archive or render it as an image.
    text = text.replace(
        "if candidate.is_file(): out.add(candidate.resolve())",
        "if candidate.is_file() and candidate.name != 'tikz_setup.tex':\n                    out.add(candidate.resolve())",
    )
    text = text.replace(
        "if candidate.is_file():\n                    out.add(candidate.resolve())",
        "if candidate.is_file() and candidate.name != 'tikz_setup.tex':\n                    out.add(candidate.resolve())",
    )
    text = text.replace(
        "if candidate.is_file():\n                out.add(candidate.resolve())",
        "if candidate.is_file() and candidate.name != 'tikz_setup.tex':\n                out.add(candidate.resolve())",
    )

    # Defensive final filter for either implementation spelling.
    text = re.sub(
        r"return sorted\(out\)",
        "out = {p for p in out if p.name != 'tikz_setup.tex'}\n    return sorted(out)",
        text,
        count=1,
    )

    if text == original:
        print(f"no textual hotfix required for {path.relative_to(ROOT)}")
    else:
        path.write_text(text, encoding="utf-8")
        print(f"patched {path.relative_to(ROOT)}")


def load_permanent():
    spec = importlib.util.spec_from_file_location("hexagon_exact_figures", PERMANENT)
    if spec is None or spec.loader is None:
        raise SystemExit("could not load permanent exact-figure generator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def regenerate_existing() -> None:
    module = load_permanent()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    module.generate_all(module.EXACT, manifest)
    module.finalize_manifest(manifest)
    module.write_report(manifest)
    module.check()


def migrate_from_staged() -> None:
    if not STAGED.is_file():
        raise SystemExit("neither a permanent generator nor the staged migration program exists")
    sys.argv = [str(STAGED), "--migrate"]
    runpy.run_path(str(STAGED), run_name="__main__")


def validate_manifest() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assets = data.get("assets", [])
    if not assets:
        raise SystemExit("exact-figure manifest contains no assets")
    bad = [item for item in assets if str(item.get("source", "")).endswith("tikz_setup.tex")]
    if bad:
        raise SystemExit("tikz_setup.tex was incorrectly classified as a figure")
    metric = sum(item.get("category") == "metric_exact" for item in assets)
    logical = len(assets) - metric
    if metric < 20:
        raise SystemExit(f"too few formula-driven metric figures: {metric}")
    print(f"manifest validated: {len(assets)} assets; {metric} metric; {logical} logical/nonmetric")


def main() -> None:
    patch_source(STAGED)
    patch_source(PERMANENT)

    if PERMANENT.is_file() and MANIFEST.is_file():
        regenerate_existing()
    else:
        migrate_from_staged()

    # The migration copies the staged source to the permanent location.  Apply
    # the same textual corrections once more, then regenerate the byte-stable
    # vector assets and hashes from the permanent program.
    patch_source(PERMANENT)
    regenerate_existing()
    validate_manifest()
    subprocess.run([sys.executable, str(PERMANENT), "--check"], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
