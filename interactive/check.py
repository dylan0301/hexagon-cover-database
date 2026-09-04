#!/usr/bin/env python3
"""Static integrity checks for the self-contained interactive pages."""

from __future__ import annotations

import json
import re
import subprocess
import tempfile
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "interactive/readable_proof_dependency_graph.html"
TRACE_HTML = ROOT / "interactive/trace_exact_ab_envelope_explorer.html"
TRACE_PRESETS = ROOT / "interactive/trace_exact_ab_presets.json"
TRACE_PNG_DIR = ROOT / "arrange/paper_draft/figures/trace_exact_ab"

EXPECTED_TRACE_CASES = {
    "zero_gap_n1_vd0": "F",
    "one_gap_n0_vd0": "A",
    "two_gap_vd0": "B",
    "one_t3_n0": "A",
    "two_t3_n0": "A",
    "two_gap_t3_n0": "B",
    "one_gap_n1_vd0_ce1": "C",
    "one_gap_n1_vd0_ce2": "C",
    "two_gap_n1_vd0": "B",
    "one_gap_n1_t3": "D_T",
    "two_gap_n1_t3": "D_T",
    "adjacent_vd": "E_a",
    "nonadjacent_vd": "E_n",
    "vd1_rescuer": "D_V",
    "replacement_output": "R_to_A",
}

if not HTML.is_file():
    raise SystemExit("missing canonical proof dependency graph")

text = HTML.read_text(encoding="utf-8")
for marker in [
    'id="graphSvg"',
    'id="routingTable"',
    'id="caseCards"',
    'id="reportBody"',
    'id="indexTable"',
    "Canonical hexagon-cover proof graph",
    "Open trace explorer",
    "Appendix F contains the exact polynomial positivity certificate",
]:
    if marker not in text:
        raise SystemExit(f"missing interactive HTML marker: {marker}")

for stale in [
    "No-more-strategy-2",
    "original files untouched",
    "formalization/strategy2_optimization",
    "arrange/readable_paper",
]:
    if stale in text:
        raise SystemExit(f"stale interactive metadata remains: {stale}")

if not TRACE_HTML.is_file() or not TRACE_PRESETS.is_file():
    raise SystemExit("missing standalone trace-exact explorer or preset data")

trace_text = TRACE_HTML.read_text(encoding="utf-8")
preset_text = TRACE_PRESETS.read_text(encoding="utf-8")
for marker in ['id="cv"', 'id="preset"', "const PRESETS="]:
    if marker not in trace_text:
        raise SystemExit(f"missing trace-explorer marker: {marker}")

trace_script = re.search(r"<script>(.*)</script>", trace_text, re.S)
if not trace_script:
    raise SystemExit("trace-explorer HTML has no inline script")
with tempfile.TemporaryDirectory() as td:
    js = Path(td) / "trace_explorer.js"
    js.write_text(trace_script.group(1), encoding="utf-8")
    subprocess.run(["node", "--check", str(js)], check=True)

try:
    presets = json.loads(preset_text)
except json.JSONDecodeError as exc:
    raise SystemExit(f"invalid trace-explorer preset data: {exc}") from exc
if not isinstance(presets, list) or not presets:
    raise SystemExit("trace-explorer preset data must be a nonempty list")

embedded_presets = re.search(r"const PRESETS=(.*?);\nconst cv=", trace_text, re.S)
if not embedded_presets:
    raise SystemExit("trace-explorer HTML has no embedded preset registry")
if json.loads(embedded_presets.group(1)) != presets:
    raise SystemExit("trace-explorer HTML and preset JSON disagree")

exact_presets = json.loads(preset_text, parse_float=Decimal)
case_mapping = {
    preset.get("key"): preset.get("case_id")
    for preset in exact_presets
    if isinstance(preset, dict)
}
if case_mapping != EXPECTED_TRACE_CASES or len(exact_presets) != len(
    EXPECTED_TRACE_CASES
):
    raise SystemExit("trace-explorer preset keys do not match the finite-case mapping")

allowed_roles = {"Vd0", "Vd1L", "Vd1R", "Vd2", "T3L", "T3R"}
one = Decimal(1)
endpoint_tolerance = Decimal("1e-12")
for preset in exact_presets:
    key = preset["key"]
    roles = preset.get("roles")
    reaches = preset.get("actual_reaches")
    if not isinstance(roles, list) or len(roles) != 6:
        raise SystemExit(f"{key}: preset must contain six V-triangle roles")
    if set(roles) - allowed_roles:
        raise SystemExit(f"{key}: preset contains an unknown V-triangle role")
    if not isinstance(reaches, list) or len(reaches) != 6:
        raise SystemExit(f"{key}: preset must contain six actual reach pairs")
    if any(not isinstance(pair, list) or len(pair) != 2 for pair in reaches):
        raise SystemExit(f"{key}: malformed actual reach pair")

    actual_reaches = [tuple(Decimal(value) for value in pair) for pair in reaches]
    if any(
        A_i < 0 or A_i > one or B_i < 0 or B_i > one
        for A_i, B_i in actual_reaches
    ):
        raise SystemExit(f"{key}: actual reach lies outside [0,1]")

    supercritical = [
        index
        for index, (A_i, B_i) in enumerate(actual_reaches)
        if A_i + B_i > one
    ]
    expected_gaps = []
    for edge, (_, B_i) in enumerate(actual_reaches):
        A_next = actual_reaches[(edge + 1) % 6][0]
        right = one - A_next
        if B_i <= right:
            expected_gaps.append((edge, B_i, right))

    gaps = preset.get("gaps")
    if not isinstance(gaps, list) or len(gaps) != len(expected_gaps):
        raise SystemExit(
            f"{key}: gaps do not implement B_i+A_(i+1)<=1, including equality"
        )
    for gap, (edge, left, right) in zip(gaps, expected_gaps):
        if not isinstance(gap, dict) or gap.get("edge") != edge:
            raise SystemExit(f"{key}: gap edge registry is inconsistent")
        gap_left = Decimal(gap.get("left"))
        gap_right = Decimal(gap.get("right"))
        if (
            abs(gap_left - left) > endpoint_tolerance
            or abs(gap_right - right) > endpoint_tolerance
        ):
            raise SystemExit(f"{key}: gap endpoints do not match the actual reaches")

    vd_indices = [
        index
        for index, role in enumerate(roles)
        if role.startswith("Vd1") or role == "Vd2"
    ]
    t3_indices = [
        index for index, role in enumerate(roles) if role.startswith("T3")
    ]
    expected_derived = {
        "N_gap": len(expected_gaps),
        "gap_edges": [edge for edge, _, _ in expected_gaps],
        "singleton_gap_edges": [
            edge for edge, left, right in expected_gaps if left == right
        ],
        "N_plus": len(supercritical),
        "supercritical_indices": supercritical,
        "d": len(vd_indices),
        "t": len(t3_indices),
        "vd_indices": vd_indices,
        "t3_indices": t3_indices,
        "A0_plus_B0_lt_half": sum(actual_reaches[0]) < Decimal("0.5"),
    }
    if preset.get("derived") != expected_derived:
        raise SystemExit(
            f"{key}: derived case data do not match actual reaches and roles"
        )
    predicate = preset.get("predicate")
    if not isinstance(predicate, dict) or any(
        name not in expected_derived or expected_derived[name] != value
        for name, value in predicate.items()
    ):
        raise SystemExit(f"{key}: declared case predicate does not match derived data")

if not TRACE_PNG_DIR.is_dir():
    raise SystemExit("missing colocated trace-exact manuscript figures")
actual_trace_stems = {path.stem for path in TRACE_PNG_DIR.glob("*.png")}
if actual_trace_stems != set(EXPECTED_TRACE_CASES):
    raise SystemExit("trace-exact PNG stems do not match the preset registry")

for stale in [
    "06i_trace_exact_ab_atlas",
    "06h_trace_exact_ab_atlas_appendix",
    "Appendix A contains the exact mixed-overlap arithmetic",
]:
    if stale in text or stale in trace_text or stale in preset_text:
        raise SystemExit(f"deleted paper-atlas reference remains: {stale}")

embedded_graph = re.search(r"const DATA=(.*?);\nconst nodeById=", text, re.S)
if not embedded_graph:
    raise SystemExit("dependency graph HTML has no embedded graph data")
graph = json.loads(embedded_graph.group(1))
expected_groups = [
    "Body 1: introduction",
    "Body 2: common geometry",
    "Body 3: trace bounds",
    "Body 4: area loss",
    "Body 5: finite enclosure",
    "Body 6: final assembly",
    "Appendix A: shared geometry",
    "Appendix B: trace optimization",
    "Appendix C: area optimization",
    "Appendix D: nonzero-gap optimization",
    "Appendix E: zero-gap optimization",
    "Appendix F: exact certificate",
]
if graph.get("groups") != expected_groups:
    raise SystemExit("dependency graph does not use the six-body/Appendix A--F architecture")
if [row.get("id") for row in graph.get("finiteRows", [])] != [
    "A", "B", "C", "D_T", "D_V", "E_a", "E_n", "F", "R"
]:
    raise SystemExit("dependency graph finite-enclosure cards do not match the case register")

canonical_statement_sources = {
    "01_introduction.tex",
    "02_structure_and_common_geometry.tex",
    "03_trace_bounds.tex",
    "05_area_loss_full.tex",
    "06_finite_enclosure_full.tex",
    "07_exhaustive_assembly.tex",
    "A_structural_shared_local_signed_center_optimization.tex",
    "B_trace_length_optimization.tex",
    "C_area_loss_optimization.tex",
    "D_nonzero_gap_finite_enclosure_optimization.tex",
    "E_zero_gap_nine_point_optimization.tex",
    "A_zero_gap_exact_certificate.tex",
}
statement_sources = {
    Path(node["source"]).name for node in graph.get("nodes", [])
}
unexpected_sources = sorted(statement_sources - canonical_statement_sources)
if unexpected_sources:
    raise SystemExit(
        "dependency graph contains historical TeX statement sources: "
        + ", ".join(unexpected_sources)
    )

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
    "arrange/paper_draft/06h_trace_exact_ab_atlas_appendix.tex",
    "arrange/paper_draft/06i_trace_exact_ab_atlas.tex",
]:
    if (ROOT / obsolete).exists():
        raise SystemExit(f"obsolete interactive file remains: {obsolete}")

print("interactive/check.py: OK")
