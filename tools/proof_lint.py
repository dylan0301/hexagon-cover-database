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

EXPECTED_407_FILES = {
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4073_boundary_loss_framework.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4074_L_Full_branch.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4075_Tminus_low_lower_branch_obligations.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4078_left_L_family_completion.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4079_first_Full_branch.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407a_left_Thigh_branch_completion.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407c_rigor_completion_details.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407d_rigor_final_assembly.md",
}
COMPUTATION_3105 = (
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/"
    "3105X_self_contained_direct_Vd0_nine_point/3105X_computation/"
)
EXPECTED_3105_FILES = {
    *(COMPUTATION_3105 + f"mixed_overlap_core_data_{index:02d}.py" for index in range(6)),
    COMPUTATION_3105 + "mixed_overlap_core_polynomials.py",
    COMPUTATION_3105 + "verify_mixed_overlap_core_derivation.py",
    COMPUTATION_3105 + "verify_global_core_positivity.py",
}
EXPECTED_3105_TRANSCRIPT = (
    "dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485"
)


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


def strip_tex_comments(text: str) -> str:
    """Remove TeX comments while retaining escaped percent signs."""
    return re.sub(r"(?m)(?<!\\)%.*$", "", text)


def active_tex(text: str) -> str:
    r"""Return material visible to TeX, excluding comments and \iffalse blocks."""
    text = strip_tex_comments(text)
    inactive = re.compile(r"\\iffalse\b(?:(?!\\iffalse\b|\\fi\b).)*\\fi\b", re.S)
    previous = None
    while text != previous:
        previous = text
        text = inactive.sub("", text)
    return text


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
    text = active_tex(path.read_text(encoding="utf-8"))
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
    text = active_tex(path.read_text(encoding="utf-8"))
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

main_text = active_tex(
    (ROOT / "arrange/paper_draft/main.tex").read_text(encoding="utf-8")
)
strategy2_path = (ROOT / "arrange/paper_draft/04_strategy2_verification.tex").resolve()
if strategy2_path not in compiled:
    fail("compiled TeX graph does not use the consolidated Strategy 2 source")
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

strategy2_paths = sorted(
    path
    for path in compiled
    if path.name.startswith(("04_strategy2_", "04d_strategy2_", "04e_strategy2_", "04f_strategy2_"))
)
strategy2_text = "\n".join(
    active_tex(path.read_text(encoding="utf-8")) for path in strategy2_paths
)
short_vd_text = active_tex(
    (ROOT / "arrange/paper_draft/04c_short_Vd_placements.tex").read_text(
        encoding="utf-8"
    )
)
if "prop:signed-ce2-one-vd-placements" in strategy2_text + short_vd_text:
    fail("duplicate compact CE2 one-Vd assembly remains")
if (strategy2_text + short_vd_text).count(r"\label{prop:paper-ce2-one-vd-placements}") != 1:
    fail("the authoritative CE2 one-Vd assembly label must occur exactly once")
if "\\subsection{Placement assembly}" in short_vd_text:
    fail("04c_short_Vd_placements.tex still contains a placement assembly")

ledger_path = ROOT / "arrange/paper_draft/source_ledger.md"
ledger = ledger_path.read_text(encoding="utf-8")
ledger_visible = re.sub(r"<!--.*?-->", "", ledger, flags=re.S)
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

canonical_407_crosswalk = """
In the canonical branch crosswalk, first-`Const` followed by
right-`Const` or right-$Q_-$ is owned by `4075`; `4078` owns the remaining
first-`Const`, right-$Q_+$ family.
"""
if re.sub(r"\s+", " ", canonical_407_crosswalk).strip() not in re.sub(
    r"\s+", " ", ledger_visible
):
    fail("source ledger has regressed the canonical 4075/4078 branch ownership")

reader_body_paths = [
    ROOT / "arrange/paper_draft/01_introduction.tex",
    ROOT / "arrange/paper_draft/02_global_notation.tex",
    ROOT / "arrange/paper_draft/02_reader_framework.tex",
    ROOT / "arrange/paper_draft/03_strategy1_reader.tex",
    ROOT / "arrange/paper_draft/04_strategy2_summary.tex",
    ROOT / "arrange/paper_draft/05_strategy3_reader.tex",
    ROOT / "arrange/paper_draft/06_strategy4_reader.tex",
    ROOT / "arrange/paper_draft/07_exhaustive_assembly.tex",
]
reader_terminology_patterns = [
    (r"\broles?\b", "reader-facing role terminology"),
    (r"\bdemands?\b", "reader-facing demand terminology"),
    (r"\bdefects?\b", "reader-facing defect terminology"),
    (r"\brescuers?\b", "reader-facing rescuer terminology"),
    (r"\brecords?\b", "reader-facing record terminology"),
    (r"\bregistry\b", "reader-facing registry terminology"),
    (r"\bproof owner\b", "reader-facing proof-owner terminology"),
    (r"\bnormative\b", "reader-facing normative-interface terminology"),
    (r"\bterminals?\b", "reader-facing terminal terminology"),
    (r"\bkernels?\b", "reader-facing kernel terminology"),
    (r"\baudits?\b", "reader-facing audit terminology"),
    (r"T_\+\^\{(?:\\rm|\\mathrm)\{?hi\}?\}", "reader-facing historical high T-plus label"),
    (r"\\mathcal D_\{\\rm CE[12]\}", "noncanonical reader-facing CE domain name"),
]
for path in reader_body_paths:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"(?m)(?<!\\)%.*$", "", text)
    text = re.sub(r"\\(?:label|ref|eqref|pageref|input)\{[^}]*\}", "", text)
    for pattern, description in reader_terminology_patterns:
        if re.search(pattern, text, re.I):
            fail(f"{description} in {path.relative_to(ROOT)}")

scan_paths = active_sources | compiled
terminology_patterns = [
    (r"\bfive[- ]row\b", "geometric five-row terminology"),
    (r"\bsix[- ]row\b", "geometric six-row terminology"),
    (r"\b(?:Vd1/Vd2|T3-like|vertex|ordinary|remaining|selected|unique|supercritical) rows?\b", "geometric row terminology"),
    (r"\brows below\b", "geometric row terminology"),
    (r"\brow \$i\$", "geometric row terminology"),
    (r"\brow (?:interface|propagation|coordinates|map|completion|sums?)\b", "geometric row terminology"),
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
    lowercase_nplus_tokens = (
        r"N_+=\left\lvert\left\lbracei:a_i+b_i>1",
        r"N_+=\left\lvert\left\{i:a_i+b_i>1",
    )
    if any(token in compact for token in lowercase_nplus_tokens):
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
if set(provenance_407.get("files", {})) != EXPECTED_407_FILES:
    fail("407X provenance manifest must contain exactly the eight authenticated blobs")
strategy2_manifest = (
    ROOT
    / "arrange/paper_draft/04e_strategy2_verification_00_provenance_manifest.tex"
).read_text(encoding="utf-8")
for relative, expected in provenance_407["files"].items():
    actual = git_blob_sha(ROOT / relative)
    if actual != expected:
        fail(f"407X blob drift: {relative}: expected {expected}, found {actual}")
    if expected not in strategy2_manifest:
        fail(f"407X full blob missing from Strategy 2 TeX: {relative}")
    if expected[:12] not in ledger:
        fail(f"407X blob prefix missing from source ledger: {relative}")

provenance_3105 = json.loads((ROOT / "proof/3105X_CERTIFICATE_PROVENANCE.json").read_text(encoding="utf-8"))
if set(provenance_3105.get("files", {})) != EXPECTED_3105_FILES:
    fail("Strategy 4 provenance manifest must contain exactly six shards and three verifier files")
if provenance_3105.get("transcript_sha256") != EXPECTED_3105_TRANSCRIPT:
    fail("Strategy 4 provenance transcript digest is not the canonical exact digest")
certificate_tex = (ROOT / "arrange/paper_draft/06a_strategy4_exact_certificate.tex").read_text(encoding="utf-8")
for relative, expected in provenance_3105["files"].items():
    actual = git_blob_sha(ROOT / relative)
    if actual != expected:
        fail(f"Strategy 4 certificate blob drift: {relative}")
    if expected not in certificate_tex:
        fail(f"Strategy 4 certificate blob missing from TeX manifest: {relative}")
for path in [
    ROOT / "arrange/paper_draft/source_ledger.md",
    ROOT / "tools/generate_verification_summary.py",
]:
    if EXPECTED_3105_TRANSCRIPT not in path.read_text(encoding="utf-8"):
        fail(f"canonical Strategy 4 transcript digest missing from {path.relative_to(ROOT)}")

requirements = (ROOT / "requirements-proof.txt").read_text(encoding="utf-8").splitlines()
if requirements != ["sympy==1.14.0", "PyMuPDF==1.26.7"]:
    fail("requirements-proof.txt must pin SymPy 1.14.0 and PyMuPDF 1.26.7 exactly")


for label in [
    "thm:s2-geom-e1",
    "thm:s2-geom-e2",
    "thm:s2-geom-r1",
    "thm:s2-geom-r2",
    "thm:s2-geom-t3",
    "thm:s2-geom-sc",
    "thm:s2-geom-vd-adjacent",
    "thm:s2-geom-vd-nonadjacent",
]:
    if label not in labels:
        fail(f"missing active geometric Strategy 2 theorem owner: {label}")

source_only_paths = [
    ROOT / "arrange/paper_draft/04_strategy2_optimization_problems.tex",
    ROOT / "arrange/paper_draft/04_strategy2_optimization_core.tex",
    ROOT / "arrange/paper_draft/04_strategy2_optimization_map.tex",
    ROOT / "arrange/paper_draft/04_strategy2_optimization_domain.tex",
    ROOT / "arrange/paper_draft/04_strategy2_optimization_labels.tex",
    ROOT / "arrange/paper_draft/04_strategy2_optimization_registered.tex",
    ROOT / "arrange/paper_draft/04_strategy2_optimization_t3.tex",
    ROOT / "arrange/paper_draft/04_strategy2_optimization_rescuer.tex",
    ROOT / "arrange/paper_draft/04_strategy2_optimization_vd.tex",
    ROOT / "arrange/paper_draft/04d_strategy2_parameter_bridges.tex",
    ROOT / "arrange/paper_draft/04f_strategy2_pure_theorems.tex",
]
source_only_labels: dict[str, Path] = {}
source_only_references: list[tuple[str, Path]] = []
for path in source_only_paths:
    text = active_tex(path.read_text(encoding="utf-8"))
    for label in re.findall(r"\\label\{([^}]+)\}", text):
        if label in source_only_labels:
            fail(
                f"duplicate source-only TeX label {label}: "
                f"{source_only_labels[label].relative_to(ROOT)} and "
                f"{path.relative_to(ROOT)}"
            )
        if label in labels:
            fail(
                f"source-only TeX label collides with compiled label {label}: "
                f"{path.relative_to(ROOT)} and {labels[label].relative_to(ROOT)}"
            )
        source_only_labels[label] = path
    for reference in re.findall(
        r"\\(?:eqref|ref|pageref|cref|Cref|autoref)\{([^}]+)\}", text
    ):
        source_only_references.append((reference, path))
for reference, path in source_only_references:
    if reference not in labels and reference not in source_only_labels:
        fail(f"unresolved source-only TeX reference {reference} in {path.relative_to(ROOT)}")

for label in [
    "thm:s2-univ-e1",
    "thm:s2-univ-e2",
    "thm:s2-univ-r1",
    "thm:s2-univ-r2",
    "thm:s2-source-t3",
    "thm:s2-univ-sc",
    "thm:s2-univ-vd-adjacent",
    "thm:s2-univ-vd-nonadjacent",
]:
    if label not in source_only_labels:
        fail(f"missing source-only Strategy 2 scalar owner: {label}")

registry_path = (
    ROOT
    / "proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/"
    "2111_strategy2_pure_optimization_registry.md"
)
registry_head = "\n".join(registry_path.read_text(encoding="utf-8").splitlines()[:20])
if not re.search(r"(?m)^Status:\s*Reference\s*$", registry_head):
    fail("2111 scalar-calculation crosswalk must remain Status: Reference")

lean_root = ROOT / "formalization/strategy2_optimization"
for relative in [
    "lakefile.lean",
    "lean-toolchain",
    "Strategy2Optimization.lean",
    "Strategy2Optimization/Problems.lean",
]:
    if not (lean_root / relative).is_file():
        fail(f"missing pinned Lean scalar-statement file: {relative}")
if (lean_root / "lean-toolchain").is_file() and (lean_root / "lean-toolchain").read_text(encoding="utf-8").strip() != "leanprover/lean4:v4.32.2":
    fail("Lean scalar-statement project is not pinned to Lean 4.32.2")
if (lean_root / "lakefile.lean").is_file() and "905b95818eb32af7874a58b427f50c1711a5e96c" not in (lean_root / "lakefile.lean").read_text(encoding="utf-8"):
    fail("Lean scalar-statement project is not pinned to the audited Mathlib commit")

for required_file in [
    "LICENSE",
    "CONTRIBUTING.md",
    "REPRODUCE.md",
    ".github/CODEOWNERS",
    ".github/pull_request_template.md",
    "release/RELEASE_CONTENTS.md",
    "tools/compare_pdfs_semantically.py",
]:
    if not (ROOT / required_file).is_file():
        fail(f"missing release or review infrastructure: {required_file}")

for stale_file in [
    ".github/workflows/export-repair-snapshot.yml",
    "arrange/20260802_verification_summary.txt",
    "arrange/final_audit_repair_failure.log",
]:
    if (ROOT / stale_file).exists():
        fail(f"stale one-shot or build-status file remains: {stale_file}")

workflow_dir = ROOT / ".github/workflows"
if (workflow_dir / "refresh-proof-provenance.yml").exists():
    fail("one-shot write workflow remains in the final tree")
paper_rebuild_workflow = workflow_dir / "paper-rebuild.yml"
for workflow in workflow_dir.glob("*.yml"):
    text = workflow.read_text(encoding="utf-8")
    if re.search(r"uses:\s+[^\s@]+@(v\d+|main|master)\b", text):
        fail(f"moving GitHub Action tag in {workflow.relative_to(ROOT)}")
    requests_content_write = bool(re.search(r"contents:\s*write", text))
    if workflow == paper_rebuild_workflow:
        if not requests_content_write:
            fail("paper-rebuild workflow must request contents: write")
        if not re.search(r"actions:\s*write", text):
            fail("paper-rebuild workflow must be able to dispatch post-build verification")
        if "gh workflow run proof-ci.yml" not in text:
            fail("paper-rebuild workflow must explicitly dispatch proof-ci after artifact commit")
    elif requests_content_write:
        fail(f"permanent workflow has contents: write: {workflow.relative_to(ROOT)}")
    if workflow.name == "proof-ci.yml":
        if "compare_pdfs_semantically.py" not in text:
            fail("permanent paper workflow lacks stable semantic PDF comparison")
        if "cmp main.tracked.pdf main.pdf" in text:
            fail("permanent paper workflow regressed to unstable raw PDF byte comparison")

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
