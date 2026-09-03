#!/usr/bin/env python3
"""Source-level consistency checks for the mathematical proof corpus."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
TEX_REFERENCE_RE = re.compile(
    r"\\(?:eqref|ref|pageref|cref|Cref|autoref|zcref|zcpageref)"
    r"\*?(?:\[[^\]]*\])?\{([^}]+)\}"
)


def fail(message: str) -> None:
    ERRORS.append(message)


def active_tex(text: str) -> str:
    text = re.sub(r"(?m)(?<!\\)%.*$", "", text)
    inactive = re.compile(r"\\iffalse\b(?:(?!\\iffalse\b|\\fi\b).)*\\fi\b", re.S)
    previous = None
    while text != previous:
        previous = text
        text = inactive.sub("", text)
    return text


def tex_reference_labels(text: str) -> list[str]:
    labels: list[str] = []
    for raw in TEX_REFERENCE_RE.findall(text):
        labels.extend(label.strip() for label in raw.split(",") if label.strip())
    return labels


def resolve_input(source: Path, raw: str) -> Path:
    target = Path(raw)
    if not target.suffix:
        target = target.with_suffix(".tex")
    candidates = [
        source.parent / target,
        ROOT / "arrange/paper_draft" / target,
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    return candidates[0].resolve()


def tex_closure(entry: Path) -> set[Path]:
    seen: set[Path] = set()

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in seen:
            return
        if not path.is_file():
            fail(f"missing TeX input: {path.relative_to(ROOT)}")
            return
        seen.add(path)
        text = active_tex(path.read_text(encoding="utf-8", errors="replace"))
        for raw in re.findall(r"\\input\{([^}]+)\}", text):
            visit(resolve_input(path, raw))

    visit(entry)
    return seen


allowed_directories = {".git", ".github", "proof", "arrange", "interactive", "prompts"}
for path in ROOT.iterdir():
    if path.is_dir() and path.name not in allowed_directories:
        fail(f"unexpected top-level directory: {path.name}")

for required in [
    "README.md",
    "LICENSE",
    ".gitignore",
    "AGENTS.md",
    ".github/workflows/ci.yml",
    "arrange/paper_draft/main.tex",
    "arrange/paper_draft/main.pdf",
    "interactive/readable_proof_dependency_graph.html",
    "proof/0XXX_main/0003_reusable_lemma_catalog.md",
    "proof/2XXX_geometric_lemmas/24XX_area_loss/2400_zero_gap_area_loss_interface.md",
    "proof/2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md",
    "proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md",
]:
    if not (ROOT / required).is_file():
        fail(f"missing required file: {required}")

for forbidden in [
    "formalization",
    "tools",
    "release",
    ".vscode",
    "arrange/readable_paper",
    "arrange/CURRENT_VERIFICATION_SUMMARY.txt",
    "proof/ACTIVE_DEPENDENCIES.txt",
    "proof/ACTIVE_DEPENDENCY_GRAPH.json",
    "proof/MANIFEST.txt",
    "interactive/readable_proof_dependency_data.json",
]:
    if (ROOT / forbidden).exists():
        fail(f"obsolete auxiliary path remains: {forbidden}")

for forbidden in [
    "arrange/paper_draft/04_boundary_propagation.tex",
    "arrange/paper_draft/04_strategy2_verification.tex",
    "arrange/paper_draft/04_strategy2_optimization_map.tex",
    "arrange/paper_draft/04d_strategy2_parameter_bridges.tex",
    "arrange/paper_draft/04f_strategy2_pure_theorems.tex",
    "proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2111_strategy2_pure_optimization_registry.md",
]:
    if (ROOT / forbidden).exists():
        fail(f"formalization compatibility file remains: {forbidden}")

closures = {"canonical": tex_closure(ROOT / "arrange/paper_draft/main.tex")}
for name, closure in closures.items():
    labels: dict[str, Path] = {}
    references: list[tuple[str, Path]] = []
    for path in closure:
        text = active_tex(path.read_text(encoding="utf-8", errors="replace"))
        for label in re.findall(r"\\label\{([^}]+)\}", text):
            if label in labels:
                fail(
                    f"duplicate {name} TeX label {label}: "
                    f"{labels[label].relative_to(ROOT)} and {path.relative_to(ROOT)}"
                )
            labels[label] = path
        for reference in tex_reference_labels(text):
            references.append((reference, path))
    for reference, path in references:
        if reference not in labels:
            fail(f"unresolved {name} TeX reference {reference} in {path.relative_to(ROOT)}")

canonical = closures["canonical"]
for required in [
    "02_structure_and_common_geometry.tex",
    "02_reader_framework.tex",
    "03_trace_bounds.tex",
    "03_strategy1_reader.tex",
    "05_area_loss_full.tex",
    "05_strategy3_reader.tex",
    "06_finite_enclosure_full.tex",
    "06_finite_enclosure_reader.tex",
    "06_zero_gap_reader.tex",
    "06_strategy4_reader.tex",
    "07_exhaustive_assembly.tex",
    "A_structural_shared_signed_optimization.tex",
    "B_trace_length_optimization.tex",
    "C_area_loss_optimization.tex",
    "D_nonzero_gap_finite_enclosure_optimization.tex",
    "E_zero_gap_nine_point_optimization.tex",
    "A_zero_gap_exact_certificate.tex",
]:
    path = (ROOT / "arrange/paper_draft" / required).resolve()
    if path not in canonical:
        fail(f"canonical TeX closure omits required source: {required}")

main_inputs = re.findall(
    r"\\input\{([^}]+)\}",
    active_tex((ROOT / "arrange/paper_draft/main.tex").read_text(encoding="utf-8")),
)
expected_appendix_inputs = [
    "A_structural_shared_signed_optimization",
    "B_trace_length_optimization",
    "C_area_loss_optimization",
    "D_nonzero_gap_finite_enclosure_optimization",
    "E_zero_gap_nine_point_optimization",
    "A_zero_gap_exact_certificate",
]
if main_inputs[-len(expected_appendix_inputs) :] != expected_appendix_inputs:
    fail(
        "canonical appendix order must be A structural/shared/signed, B trace, "
        "C area, D nonzero-gap, E zero-gap, F exact certificate"
    )

for path in canonical:
    if path.name.startswith("04_strategy2_") or path.name in {
        "04_boundary_propagation.tex",
        "04_strategy2_verification.tex",
    }:
        fail(f"canonical manuscript compiles obsolete source: {path.relative_to(ROOT)}")
    if path.name in {
        "06h_trace_exact_ab_atlas_appendix.tex",
        "06i_trace_exact_ab_atlas.tex",
    }:
        fail(f"canonical manuscript compiles the illustrative atlas: {path.relative_to(ROOT)}")
    if re.search(
        r"\\tag\*?\s*\{6\.",
        active_tex(path.read_text(encoding="utf-8", errors="replace")),
    ):
        fail(
            "canonical manuscript retains a relocated numeric 6.xx equation tag: "
            f"{path.relative_to(ROOT)}"
        )

for path in (ROOT / "proof").rglob("*.md"):
    if "9XXX_failed_ideas" in path.parts:
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for raw in re.findall(r"\[[^\]]*\]\(([^)]+\.md)(?:#[^)]+)?\)", text):
        if "://" in raw:
            continue
        target = (path.parent / raw).resolve()
        if not target.is_file():
            fail(f"broken proof Markdown link in {path.relative_to(ROOT)}: {raw}")

active_interfaces = {
    "proof/2XXX_geometric_lemmas/24XX_area_loss/2400_zero_gap_area_loss_interface.md": "Status: Proven",
    "proof/2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md": "Status: Proven",
    "proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md": "Status: Proven",
}
for raw, marker in active_interfaces.items():
    text = (ROOT / raw).read_text(encoding="utf-8", errors="replace")
    if marker not in text.splitlines()[:6]:
        fail(f"active interface lacks Proven status: {raw}")

main_text = (ROOT / "proof/0XXX_main/0000_main_theorem.md").read_text(
    encoding="utf-8", errors="replace"
)
for interface in [
    "2400_zero_gap_area_loss_interface.md",
    "2531_length_budget_corollaries.md",
    "2610_finite_enclosure_terminal_interfaces.md",
]:
    if interface not in main_text:
        fail(f"main theorem does not route through active interface: {interface}")

length_wrappers = [
    "proof/4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md",
    "proof/4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md",
    "proof/4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md",
    "proof/4XXX_CE1CE2/41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md",
    "proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md",
    "proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md",
    "proof/4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md",
]
for raw in length_wrappers:
    text = (ROOT / raw).read_text(encoding="utf-8", errors="replace")
    if "2531_length_budget_corollaries.md" not in text:
        fail(f"length compatibility wrapper does not invoke 2531: {raw}")
    if "Status: Proven" not in text.splitlines()[:6]:
        fail(f"length compatibility wrapper lost Proven status: {raw}")

provenance = (
    ROOT
    / "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/"
    "3105X_self_contained_direct_Vd0_nine_point/3105X_computation/"
    "certificate_provenance.json"
)
if not provenance.is_file():
    fail("missing colocated exact-certificate provenance file")

for required in [
    "verify_mixed_overlap_core_derivation.py",
    "verify_global_core_positivity.py",
    "mixed_overlap_core_polynomials.py",
]:
    if not (provenance.parent / required).is_file():
        fail(f"missing exact-certificate component: {required}")

for path in [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "arrange/README.md",
    ROOT / "interactive/README.md",
    ROOT / ".github/workflows/ci.yml",
]:
    text = path.read_text(encoding="utf-8", errors="replace")
    for pattern in [
        r"formalization/strategy2_optimization",
        r"leanprover/lean-action",
        r"lake-manifest",
        r"intentional `?sorry",
        r"requirements-proof\.txt",
        r"CURRENT_VERIFICATION_SUMMARY",
        r"release/RELEASE_CONTENTS",
        r"No-more-strategy-2",
    ]:
        if re.search(pattern, text, re.I):
            fail(f"stale infrastructure reference in {path.relative_to(ROOT)}: {pattern}")

result = subprocess.run(["git", "diff", "--check"], cwd=ROOT, text=True, capture_output=True)
if result.returncode:
    fail(result.stdout + result.stderr)

if ERRORS:
    print("proof/check.py: FAILED", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print(
    "proof/check.py: OK "
    f"({len(closures['canonical'])} canonical TeX sources)"
)
