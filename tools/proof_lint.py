#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def run_generated_check(script: str) -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / script), "--check"],
        text=True,
        capture_output=True,
    )
    if result.returncode:
        fail((result.stdout + result.stderr).strip())


run_generated_check("tools/generate_active_dependency_graph.py")
run_generated_check("tools/generate_proof_manifest.py")

graph_path = ROOT / "proof/ACTIVE_DEPENDENCY_GRAPH.json"
if not graph_path.is_file():
    fail("missing proof/ACTIVE_DEPENDENCY_GRAPH.json")
    graph = {"nodes": {}}
else:
    graph = json.loads(graph_path.read_text(encoding="utf-8"))

active_sources: set[Path] = set()
for relative, node in graph.get("nodes", {}).items():
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing active dependency: {relative}")
        continue
    if node.get("kind") != "proof-source":
        continue
    active_sources.add(path)
    expected = node.get("status")
    head = "\n".join(path.read_text(encoding="utf-8").splitlines()[:20])
    match = re.search(r"^Status:\s*(.+?)\s*$", head, re.M)
    if not match:
        fail(f"active proof source lacks Status line: {relative}")
    elif match.group(1) != expected:
        fail(f"status mismatch: {relative}: expected {expected}, found {match.group(1)}")
    if "/9XXX_failed_ideas/" in f"/{relative}/":
        fail(f"failed source appears in active graph: {relative}")
    for dependency in node.get("dependencies", []):
        if dependency not in graph.get("nodes", {}):
            fail(f"unresolved dependency edge: {relative} -> {dependency}")


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
        child = path.parent / name
        if child.suffix == "":
            child = child.with_suffix(".tex")
        collect_tex(child, seen)


compiled: set[Path] = set()
collect_tex(ROOT / "arrange/paper_draft/main.tex", compiled)

labels: dict[str, Path] = {}
references: list[tuple[str, Path]] = []
for path in compiled:
    text = path.read_text(encoding="utf-8")
    for label in re.findall(r"\\label\{([^}]+)\}", text):
        if label in labels:
            fail(
                f"duplicate TeX label {label}: "
                f"{labels[label].relative_to(ROOT)} and {path.relative_to(ROOT)}"
            )
        labels[label] = path
    for reference in re.findall(
        r"\\(?:eqref|ref|pageref|cref|Cref|autoref)\{([^}]+)\}", text
    ):
        references.append((reference, path))
for reference, path in references:
    if reference not in labels:
        fail(f"unresolved TeX reference {reference} in {path.relative_to(ROOT)}")

main_text = (ROOT / "arrange/paper_draft/main.tex").read_text(encoding="utf-8")
if "\\input{04_strategy2_verification}" not in main_text:
    fail("main.tex does not use the consolidated Strategy 2 source")
for obsolete in [
    "04_strategy2_reader",
    "04_strategy2_exact_demand",
    "04d_strategy2_rigor_completion",
    "04e_strategy2_placement_assembly",
    "04f_strategy2_cross_reference_closure",
    "appendix_exact_mixed_overlap",
]:
    if f"\\input{{{obsolete}}}" in main_text:
        fail(f"obsolete TeX input remains: {obsolete}")
    if (ROOT / "arrange/paper_draft" / f"{obsolete}.tex").exists():
        fail(f"obsolete TeX source remains: {obsolete}.tex")

strategy2_path = ROOT / "arrange/paper_draft/04_strategy2_verification.tex"
strategy2_text = strategy2_path.read_text(encoding="utf-8")
short_vd_text = (ROOT / "arrange/paper_draft/04c_short_Vd_placements.tex").read_text(encoding="utf-8")
if "prop:signed-ce2-one-vd-placements" in strategy2_text + short_vd_text:
    fail("duplicate compact CE2 one-Vd assembly remains")
if (strategy2_text + short_vd_text).count(r"\label{prop:paper-ce2-one-vd-placements}") != 1:
    fail("the authoritative CE2 one-Vd assembly label must occur exactly once")
if "\\subsection{Placement assembly}" in short_vd_text:
    fail("04c_short_Vd_placements.tex still contains a placement assembly")

ledger_path = ROOT / "arrange/paper_draft/source_ledger.md"
ledger = ledger_path.read_text(encoding="utf-8")
for obsolete in [
    "04_strategy2_reader.tex",
    "04_strategy2_exact_demand.tex",
    "04d_strategy2_rigor_completion.tex",
    "04e_strategy2_placement_assembly.tex",
    "04f_strategy2_cross_reference_closure.tex",
]:
    if obsolete in ledger:
        fail(f"source ledger names deleted Strategy 2 source: {obsolete}")
technical = ledger.split("### Technical appendices", 1)[1].split("The body-end label", 1)[0]
if technical.count("`04_strategy2_verification.tex`") != 1:
    fail("source ledger must list the consolidated Strategy 2 appendix exactly once")

scan_paths = active_sources | compiled
terminology_patterns = [
    (r"\bfive[- ]row\b", "geometric five-row terminology"),
    (r"\bsix[- ]row\b", "geometric six-row terminology"),
    (r"\b(?:Vd1/Vd2|T3-like|vertex|ordinary|remaining) rows?\b", "geometric row terminology"),
    (r"\brows below\b", "geometric row terminology"),
    (r"\brow (?:interface|propagation|coordinates|map|completion)\b", "geometric row terminology"),
    (r"\bpositive[- ]gaps?\b", "singleton-unsafe positive-gap terminology"),
]
for path in sorted(scan_paths):
    if not path.is_file():
        continue
    text = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT)
    for pattern, description in terminology_patterns:
        if re.search(pattern, text, re.I):
            fail(f"{description} in {relative}")
    compact = re.sub(r"\s+", "", text)
    if re.search(r"N_\+=.{0,180}a_i\+b_i>1", compact):
        fail(f"N_+ is defined from selected lowercase reaches in {relative}")

all_active_text = "\n".join(
    path.read_text(encoding="utf-8") for path in scan_paths if path.is_file()
)
known_bad = {
    r"Z_X=\tau\left\lVert X\right\rVert^2-\eta u": "mixed residual uses u instead of nu",
    r"\nu_A<u_B": "local coordinate typo nu_A",
    r"T_C\cap e_{5,0}=\[x,u\]": "CE2 far endpoint must be Greek nu",
    r"\nu_2<1-H": "local adjacent endpoint must be Latin u",
    r"\nu_{\rm adj}": "local adjacent endpoint must be Latin u",
    r"\nu=\frac{d-a-tb-1}{t}": "local radial endpoint must use Latin u",
    r"\nuS": "signed endpoint product is missing a separator",
    r"\teq": "unexpanded TeX spacing placeholder",
    r"\tep": "unexpanded TeX spacing placeholder",
}
for token, description in known_bad.items():
    if token in all_active_text:
        fail(description)

proof_4147 = (
    ROOT
    / "proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md"
).read_text(encoding="utf-8")
for token in ["X_0(x,y)", "X_1(x,y)", "cover the full skeleton", "skeleton-level all-Vd0 theorem"]:
    if token not in proof_4147:
        fail(f"4147 missing repaired interface: {token}")

proof_4013 = (
    ROOT
    / "proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md"
).read_text(encoding="utf-8")
for token in ["skeleton-level form", "cover the full hexagon skeleton", "Skeleton coverage supplies the radial demands"]:
    if token not in proof_4013:
        fail(f"4013 missing skeleton strengthening: {token}")


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


provenance_407 = json.loads((ROOT / "proof/407X_PROVENANCE.json").read_text(encoding="utf-8"))
for relative, expected in provenance_407["files"].items():
    actual = git_blob_sha(ROOT / relative)
    if actual != expected:
        fail(f"407X blob drift: {relative}: expected {expected}, found {actual}")
    if expected not in strategy2_text:
        fail(f"407X full blob missing from Strategy 2 TeX: {relative}")
    if expected[:12] not in ledger:
        fail(f"407X blob prefix missing from source ledger: {relative}")

provenance_3105 = json.loads((ROOT / "proof/3105X_CERTIFICATE_PROVENANCE.json").read_text(encoding="utf-8"))
certificate_tex = (ROOT / "arrange/paper_draft/06a_strategy4_exact_certificate.tex").read_text(encoding="utf-8")
for relative, expected in provenance_3105["files"].items():
    actual = git_blob_sha(ROOT / relative)
    if actual != expected:
        fail(f"Strategy 4 certificate blob drift: {relative}")
    if expected not in certificate_tex:
        fail(f"Strategy 4 certificate blob missing from TeX manifest: {relative}")

requirements = (ROOT / "requirements-proof.txt").read_text(encoding="utf-8").splitlines()
if requirements != ["sympy==1.14.0"]:
    fail("requirements-proof.txt must pin sympy==1.14.0 exactly")

workflow_dir = ROOT / ".github/workflows"
if (workflow_dir / "refresh-proof-provenance.yml").exists():
    fail("one-shot write workflow remains in the final tree")
for workflow in workflow_dir.glob("*.yml"):
    text = workflow.read_text(encoding="utf-8")
    if re.search(r"uses:\s+[^\s@]+@(v\d+|main|master)\b", text):
        fail(f"moving GitHub Action tag in {workflow.relative_to(ROOT)}")
    if re.search(r"contents:\s*write", text):
        fail(f"permanent workflow has contents: write: {workflow.relative_to(ROOT)}")

if not (ROOT / "arrange/paper_draft/main.pdf").is_file():
    fail("tracked paper PDF is missing")

if ERRORS:
    print("proof_lint: FAILED", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)
print(
    f"proof_lint: OK ({len(active_sources)} transitive proof sources, "
    f"{len(compiled)} compiled TeX sources, {len(labels)} labels)"
)
