#!/usr/bin/env python3
"""Static integrity checks for the self-contained interactive pages."""

from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "interactive/readable_proof_dependency_graph.html"

if not HTML.is_file():
    raise SystemExit("missing readable proof dependency graph")

text = HTML.read_text(encoding="utf-8")
for marker in [
    'id="graphSvg"',
    'id="routingTable"',
    'id="caseCards"',
    'id="reportBody"',
    'id="indexTable"',
    "Reader-oriented hexagon-cover proof graph",
]:
    if marker not in text:
        raise SystemExit(f"missing interactive HTML marker: {marker}")

for stale in ["No-more-strategy-2", "original files untouched", "formalization/strategy2_optimization"]:
    if stale in text:
        raise SystemExit(f"stale interactive metadata remains: {stale}")

script = re.search(r"<script>(.*)</script>", text, re.S)
if not script:
    raise SystemExit("interactive HTML has no inline script")

with tempfile.TemporaryDirectory() as td:
    js = Path(td) / "graph.js"
    js.write_text(script.group(1), encoding="utf-8")
    subprocess.run(["node", "--check", str(js)], check=True)

for required in [
    "interactive/trace_exact_ab_envelope_explorer.html",
    "interactive/trace_exact_ab_presets.json",
    "interactive/zero_gap_nine_point_demo.html",
]:
    if not (ROOT / required).is_file():
        raise SystemExit(f"missing interactive deliverable: {required}")

for obsolete in [
    "interactive/strategy2demo.html",
    "interactive/strategy2notation.html",
    "interactive/strategy4demo.html",
    "interactive/readable_proof_dependency_data.json",
]:
    if (ROOT / obsolete).exists():
        raise SystemExit(f"obsolete interactive file remains: {obsolete}")

print("interactive/check.py: OK")
