#!/usr/bin/env python3
"""Check that the TeX and Lean Strategy 2 interfaces stay synchronized."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "arrange/paper_draft"
LEAN = ROOT / "formalization/strategy2_optimization/Strategy2Optimization/Problems.lean"

tex = "\n".join(
    path.read_text(encoding="utf-8")
    for path in sorted(PAPER.glob("04_strategy2_optimization_*.tex"))
)
tex += "\n" + (PAPER / "04f_strategy2_pure_theorems.tex").read_text(encoding="utf-8")
lean = LEAN.read_text(encoding="utf-8")

required_tex = {
    "S2-E1": "thm:s2-pure-e1",
    "S2-E2": "thm:s2-pure-e2",
    "S2-R1": "thm:s2-pure-r1",
    "S2-R2": "thm:s2-pure-r2",
    "S2-T3": "thm:s2-pure-t3",
    "S2-SC": "thm:s2-pure-sc",
    "S2-VD-adjacent": "thm:s2-pure-vd-adjacent",
    "S2-VD-nonadjacent": "thm:s2-pure-vd-nonadjacent",
}
required_lean = [
    "problemS2E1",
    "problemS2E2",
    "problemS2R1",
    "problemS2R2",
    "problemS2T3",
    "problemS2SCT",
    "problemS2SCV",
    "problemS2VDAdjacentSupport",
    "problemS2VDAdjacentNoSupport",
    "problemS2VDNonadjacent",
]

errors: list[str] = []
for problem, label in required_tex.items():
    if problem not in tex:
        errors.append(f"missing TeX problem identifier: {problem}")
    if rf"\label{{{label}}}" not in tex:
        errors.append(f"missing universal TeX theorem owner: {label}")
for name in required_lean:
    if not re.search(rf"\btheorem\s+{re.escape(name)}\b", lean):
        errors.append(f"missing Lean theorem shell: {name}")

for marker in [
    "structure SignedCenterInput",
    "alpha : ℝ",
    "delta : ℝ",
    "def centerRadical",
    "def centerEta",
    "def centerP",
    "def centerK",
    "def rightSurplus",
    "def leftSurplus",
    "inductive ForwardCapBranch",
    "| lin",
    "| const",
    "| qMinus",
    "| qPlus",
    "def forwardCap",
    "def propagate",
    "def strictSupercriticalForwardSupremum",
    "inductive VdPosition",
]:
    if marker not in lean:
        errors.append(f"missing canonical Lean interface marker: {marker}")

lean_branch_markers = [
    "if x ≤ 1 - c then 1 - x",
    "else if x ≤ lowerBreakpoint c then qPlus c x",
    "else if x < upperBreakpoint c then lowerBreakpoint c",
    "else if x < c then qMinus c x",
    "else if x = qPlusTransition c then qPlusTransition c",
]
for marker in lean_branch_markers:
    if marker not in lean:
        errors.append(f"missing Lean branch marker: {marker}")

compact_tex = re.sub(r"\s+", "", tex)
for marker in [
    r"0\le x\le1-c",
    r"1-c<x\le\ell(c)",
    r"\ell(c)<x<r(c)",
    r"r(c)\le x<c",
    r"x=h(c)",
]:
    if re.sub(r"\s+", "", marker) not in compact_tex:
        errors.append(f"missing TeX branch marker: {marker}")

for marker in [
    "0 < v.t",
    "vdNonLeftTraceEnd v ^ 2 + vdNonLeftTraceEnd v * (w v.center + v.center.delta)",
    "vdNonRightTraceEnd v ^ 2 + vdNonRightTraceEnd v * (v.center.r + v.center.alpha)",
]:
    if marker not in lean:
        errors.append(f"missing Lean Vd-domain marker: {marker}")

sorry_count = len(re.findall(r":= by\s+sorry\b", lean))
if sorry_count != len(required_lean):
    errors.append(
        f"expected {len(required_lean)} intentional sorry placeholders, found {sorry_count}"
    )

if errors:
    print("verify_strategy2_spec_sync: FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)
print(
    "verify_strategy2_spec_sync: PASS "
    f"({len(required_tex)} TeX theorem owners, {len(required_lean)} Lean shells)"
)
