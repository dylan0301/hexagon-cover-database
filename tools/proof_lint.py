#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(msg: str) -> None:
    ERRORS.append(msg)


# Active dependency statuses.
active = ROOT / "proof/ACTIVE_DEPENDENCIES.txt"
for raw in active.read_text(encoding="utf-8").splitlines():
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        continue
    rel, expected = raw.split("|", 1)
    path = ROOT / rel
    if not path.is_file():
        fail(f"missing active dependency: {rel}")
        continue
    head = "\n".join(path.read_text(encoding="utf-8").splitlines()[:12])
    m = re.search(r"^Status:\s*(.+?)\s*$", head, re.M)
    if not m:
        fail(f"active dependency lacks status: {rel}")
    elif m.group(1) != expected:
        fail(f"status mismatch: {rel}: expected {expected}, found {m.group(1)}")
    if "/9XXX_" in rel:
        fail(f"failed/archival source listed as active: {rel}")

# Proof manifest consistency.
manifest = ROOT / "proof/MANIFEST.txt"
if manifest.is_file():
    for raw in manifest.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw or raw.startswith("#") or raw.startswith("Paths are"):
            continue
        if not (ROOT / "proof" / raw).exists():
            fail(f"manifest path does not exist: proof/{raw}")

# Recursively collect compiled TeX files.
def collect_tex(path: Path, seen: set[Path]) -> None:
    path = path.resolve()
    if path in seen:
        return
    if not path.is_file():
        fail(f"missing TeX input: {path.relative_to(ROOT)}")
        return
    seen.add(path)
    text = path.read_text(encoding="utf-8")
    for name in re.findall(r"\\input\{([^}]+)\}", text):
        child = (path.parent / name)
        if child.suffix == "":
            child = child.with_suffix(".tex")
        collect_tex(child, seen)

compiled: set[Path] = set()
collect_tex(ROOT / "arrange/paper_draft/main.tex", compiled)

# Duplicate labels and unresolved references.
labels: dict[str, Path] = {}
refs: list[tuple[str, Path]] = []
for path in compiled:
    text = path.read_text(encoding="utf-8")
    for label in re.findall(r"\\label\{([^}]+)\}", text):
        if label in labels:
            fail(f"duplicate TeX label {label}: {labels[label].relative_to(ROOT)} and {path.relative_to(ROOT)}")
        labels[label] = path
    for ref in re.findall(r"\\(?:eqref|ref|pageref)\{([^}]+)\}", text):
        refs.append((ref, path))
for ref, path in refs:
    if ref not in labels:
        fail(f"unresolved TeX reference {ref} in {path.relative_to(ROOT)}")

# Canonical source organization.
main_text = (ROOT / "arrange/paper_draft/main.tex").read_text(encoding="utf-8")
if "\\input{04_strategy2_verification}" not in main_text:
    fail("main.tex does not use consolidated Strategy 2 source")
for old in [
    "04_strategy2_reader",
    "04_strategy2_exact_demand",
    "04d_strategy2_rigor_completion",
    "04e_strategy2_placement_assembly",
    "04f_strategy2_cross_reference_closure",
    "appendix_exact_mixed_overlap",
]:
    if f"\\input{{{old}}}" in main_text:
        fail(f"obsolete input remains in main.tex: {old}")
if (ROOT / "arrange/paper_draft/appendix_exact_mixed_overlap.tex").exists():
    fail("duplicate Strategy 4 certificate file still exists")

strategy2_text = (ROOT / "arrange/paper_draft/04_strategy2_verification.tex").read_text(encoding="utf-8")
for stale in [
    "% ---- formerly 04_strategy2_verification.tex ----",
    "explicit open Vd0 axis replacements",
    "preserving every boundary and radial demand used by Proposition~\\ref{prop:nplus-zero-all-vd0}",
]:
    if stale in strategy2_text:
        fail(f"stale consolidated Strategy 2 text: {stale}")

ledger = (ROOT / "arrange/paper_draft/source_ledger.md").read_text(encoding="utf-8")
technical = ledger.split("### Technical appendices", 1)[1].split("The body-end label", 1)[0]
if technical.count("`04_strategy2_verification.tex`") != 1:
    fail("source ledger must list the consolidated Strategy 2 appendix exactly once")

ignore_text = (ROOT / ".gitignore").read_text(encoding="utf-8")
for ignored in [
    "arrange/paper_draft/main.aux",
    "arrange/paper_draft/main.fdb_latexmk",
    "arrange/paper_draft/main.fls",
    "arrange/paper_draft/main.log",
    "arrange/paper_draft/main.toc",
    "arrange/paper_draft/main.xdv",
]:
    if ignored not in ignore_text:
        fail(f"missing LaTeX-intermediate ignore rule: {ignored}")

# Terminology and notation checks on active proofs and compiled TeX.
scan_paths = {ROOT / line.split("|", 1)[0] for line in active.read_text(encoding="utf-8").splitlines() if line and not line.startswith("#")}
scan_paths |= compiled
for path in sorted(scan_paths):
    if not path.is_file():
        continue
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    for pattern, desc in [
        (r"\bfive[- ]row\b", "geometric five-row terminology"),
        (r"\bsix[- ]row\b", "geometric six-row terminology"),
        (r"\brow (?:interface|propagation|coordinates|map|completion)\b", "geometric row terminology"),
        (r"\bpositive[- ]gaps?\b", "positive gap terminology; use nonempty gap"),
    ]:
        if re.search(pattern, text, re.I):
            fail(f"{desc} in {rel}")

    # N_+ must not be defined with selected lowercase reaches.
    if re.search(
        r"N_\+\s*=\s*\\left\\lvert\s*\\left(?:\\lbrace|\\\{)\s*i\s*:\s*a_i\s*\+\s*b_i",
        text,
    ):
        fail(f"N_+ appears to be defined from selected reaches in {rel}")

# Known u/nu transcription failures.
known_bad = {
    r"Z_X=\tau\left\lVert X\right\rVert^2-\eta u": "31054 mixed residual uses u instead of nu",
    r"\nu_A<u_B": "31054 coordinate typo nu_A",
    r"T_C\cap e_{5,0}=\[x,u\]": "CE2 endpoint should be Greek nu",
    r"\nu_2<1-H": "4144 local endpoint should be Latin u",
    r"\nu_{\rm adj}": "4147 adjacent radial endpoint should be Latin u",
    r"\teq": "unexpanded TeX spacing placeholder \\teq",
    r"\tep": "unexpanded TeX spacing placeholder \\tep",
}
all_active_text = "\n".join(path.read_text(encoding="utf-8") for path in scan_paths if path.is_file())
for token, desc in known_bad.items():
    if token in all_active_text:
        fail(desc)

# Exact replacement interfaces must be present.
proof_4147 = (ROOT / "proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md").read_text(encoding="utf-8")
for token in ["X_0(x,y)", "X_1(x,y)", "cover the full skeleton", "skeleton-level all-Vd0 theorem"]:
    if token not in proof_4147:
        fail(f"4147 missing required repaired interface: {token}")
proof_4013 = (ROOT / "proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md").read_text(encoding="utf-8")
for token in ["skeleton-level form", "cover the full hexagon skeleton", "Skeleton coverage supplies the radial demands"]:
    if token not in proof_4013:
        fail(f"4013 missing skeleton strengthening: {token}")


additional_bad = {
    r"\nu=\frac{d-a-tb-1}{t}": "local radial endpoint must use Latin u",
    r"\nu=1-\frac{R_{\rm loc}}D+a": "T3-like local radial endpoint must use Latin u",
    r"\nu_2<1-H": "4144 local endpoint must be u_{1\\to2}",
    r"\nu_A<u_B": "31054 local coordinate must be u_A",
    r"\nuS": "signed CE2 endpoint product is missing a separator",
    r"\nu=\frac{\delta}{1-\lambda}": "4075 local endpoint must use Latin u",
    r"a_i+b_i\le1,\qquad i=2,3,4,5.": "4131 nonsupercritical conclusion must use actual reaches",
}
for token, description in additional_bad.items():
    if token in all_active_text:
        fail(description)

required_4131 = ROOT / "proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4131_midpoint_forcing_reduction.md"
text_4131 = required_4131.read_text(encoding="utf-8")
if r"A_i+B_i\le1,\qquad i=2,3,4,5." not in text_4131:
    fail("4131 is missing the actual-reach nonsupercritical conclusion")

if ERRORS:
    print("proof_lint: FAILED", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)
print(f"proof_lint: OK ({len(scan_paths)} active/compiled files, {len(labels)} TeX labels)")
