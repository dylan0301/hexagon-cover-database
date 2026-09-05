#!/usr/bin/env python3
"""Source-level consistency checks for the mathematical proof corpus."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


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
    "arrange/paper_draft/06h_trace_exact_ab_atlas_appendix.tex",
    "arrange/paper_draft/06i_trace_exact_ab_atlas.tex",
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
        for reference_list in re.findall(
            r"\\(?:eqref|ref|pageref|cref|Cref|autoref|zcref|zCref)"
            r"(?:\[[^\]]*\])?\{([^}]+)\}",
            text,
        ):
            for reference in reference_list.split(","):
                references.append((reference.strip(), path))
    for reference, path in references:
        if reference not in labels:
            fail(f"unresolved {name} TeX reference {reference} in {path.relative_to(ROOT)}")

canonical = closures["canonical"]
canonical_top_level = {
    "main.tex",
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
actual_top_level = {
    path.name for path in (ROOT / "arrange/paper_draft").glob("*.tex")
}
if actual_top_level != canonical_top_level:
    for missing in sorted(canonical_top_level - actual_top_level):
        fail(f"canonical publication source is missing: {missing}")
    for obsolete in sorted(actual_top_level - canonical_top_level):
        fail(f"superseded publication TeX remains: {obsolete}")

for required in sorted(canonical_top_level - {"main.tex"}):
    path = (ROOT / "arrange/paper_draft" / required).resolve()
    if path not in canonical:
        fail(f"canonical TeX closure omits required source: {required}")

figure_root = ROOT / "arrange/paper_draft/figures"
trace_exact_ab_stems = {
    "adjacent_vd",
    "nonadjacent_vd",
    "one_gap_n0_vd0",
    "one_gap_n1_t3",
    "one_gap_n1_vd0_ce1",
    "one_gap_n1_vd0_ce2",
    "one_t3_n0",
    "replacement_output",
    "two_gap_n1_t3",
    "two_gap_n1_vd0",
    "two_gap_t3_n0",
    "two_gap_vd0",
    "two_t3_n0",
    "vd1_rescuer",
    "zero_gap_n1_vd0",
}
expected_figures = {
    "center_interval_residual.tex",
    "geometry_roles.tex",
    "strategy1_trace_targets.tex",
    "strategy2_ce1_ce2_n0_all_vd0.png",
    "strategy3_global_area_loss.png",
    "strategy3_local_area_loss.png",
    "strategy4_core_case_example.png",
    "tikz_setup.tex",
    "transfer_V_triangle_coordinates.tex",
    *{f"finite_enclosure/fe{i:02d}_{name}.tex" for i, name in enumerate([
        "case_roadmap",
        "trace_and_gauge",
        "disk_plus_point",
        "complementary_gap",
        "ce2_short_ray",
        "k410_actual_reach",
        "neighbor_capacity",
        "ce1_reverse_path",
        "t3_rescuer",
        "vd_placements",
        "ab_frontier",
        "zero_gap_witness",
        "support_caps",
    ])},
    *{
        f"role_examples/{name}.png"
        for name in [
            "center_role_ce0_example",
            "center_role_ce1_example",
            "center_role_ce2_example",
            "vertex_role_t3_like_example",
            "vertex_role_vd0_axis_aligned_example",
            "vertex_role_vd0_nonsupercritical_example",
            "vertex_role_vd0_supercritical_example",
            "vertex_role_vd1_example",
            "vertex_role_vd2_example",
        ]
    },
    *{f"trace_exact_ab/{stem}.png" for stem in trace_exact_ab_stems},
    *{
        f"finite_enclosure/{name}.tex"
        for name in [
            "fe13_case_a_examples",
            "fe14_case_b_examples",
            "fe15_case_c_examples",
            "fe16_case_dt_examples",
            "fe17_vd_router_examples",
            "fe18_case_f_examples",
        ]
    },
}
actual_figures = {
    str(path.relative_to(figure_root))
    for path in figure_root.rglob("*")
    if path.is_file()
}
for missing in sorted(expected_figures - actual_figures):
    fail(f"required publication figure is missing: {missing}")
for obsolete in sorted(actual_figures - expected_figures):
    fail(f"obsolete publication figure remains: {obsolete}")

static_strategy4 = figure_root / "strategy4_core_case_example.png"
static_strategy4_sha256 = (
    "824e55c3e55dfb1f90334ffb18adbd6954a3b4c289c902e9a32c933784fc1d76"
)
if static_strategy4.is_file():
    actual_sha256 = hashlib.sha256(static_strategy4.read_bytes()).hexdigest()
    if actual_sha256 != static_strategy4_sha256:
        fail(
            "strategy4_core_case_example.png SHA-256 mismatch: "
            f"expected {static_strategy4_sha256}, got {actual_sha256}"
        )

for path in canonical:
    text = active_tex(path.read_text(encoding="utf-8", errors="replace"))
    for stale in [
        r"\\tag\{",
        r"I_\+",
        r"I_\{\+\}",
        r"06h_trace_exact_ab_atlas",
        r"06i_trace_exact_ab_atlas",
    ]:
        if re.search(stale, text):
            fail(f"stale publication construct in {path.relative_to(ROOT)}: {stale}")

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

# Keep the unified zero-gap theorem, the public case register, and its shared
# radial interface synchronized. These are source checks, not proof verification.
finite_source = (ROOT / "arrange/paper_draft/06_finite_enclosure_full.tex").read_text(
    encoding="utf-8"
)
zero_gap_statement = re.search(
    r"\\begin\{theorem\}\[Zero-gap obstruction\](.*?)\\end\{theorem\}",
    active_tex(finite_source), re.S,
)
if zero_gap_statement is None:
    fail("missing public zero-gap obstruction statement")
else:
    statement = zero_gap_statement.group(1)
    if "N_+=1" not in statement or "N_{\\rm gap}=0" not in statement:
        fail("zero-gap terminal lost its exact N_gap=0, N_+=1 scope")
    if "(d,t)" in statement or "Vdzero" in statement:
        fail("zero-gap terminal reintroduced a V-type restriction")

uniform_label = "cor:new-uniform-common-pair-forcing"
if finite_source.count("\\label{" + uniform_label + "}") != 1:
    fail("uniform common-pair forcing must have one public proof owner")
zero_gap_calculation = (
    ROOT / "arrange/paper_draft/E_zero_gap_nine_point_optimization.tex"
).read_text(encoding="utf-8")
if "\\zcref{" + uniform_label + "}" not in zero_gap_calculation:
    fail("zero-gap radial calculation does not use the shared forcing interface")
routing_text = (ROOT / "arrange/paper_draft/01_introduction.tex").read_text(
    encoding="utf-8"
)
if routing_text.count("$0$&$1$&") != 1:
    fail("zero-gap N_+=1 must have exactly one routing-table row")

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

# The paired transfer and determinant orientation must match the preserved
# certificate algebra. This is an exact identity check, not numerical evidence.
four_contact_checker = provenance.parent / "verify_four_contact_identities.py"
if not four_contact_checker.is_file():
    fail("missing four-contact identity checker")
else:
    result = subprocess.run([sys.executable, str(four_contact_checker)], cwd=ROOT,
                            text=True, capture_output=True)
    if result.returncode:
        fail(result.stdout + result.stderr)
    else:
        print(result.stdout.strip())
for label in ["lem:four-contact-formula", "lem:paired-radius-transfer"]:
    if "\\label{" + label + "}" not in zero_gap_calculation:
        fail(f"missing four-contact paper interface: {label}")
for stale in ["\\label{lem:reader-cap-chain}", "Put $W=C+RA$."]:
    if stale in zero_gap_calculation:
        fail(f"obsolete cap terminal remains active: {stale}")

if ERRORS:
    print("proof/check.py: FAILED", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print(
    "proof/check.py: OK "
    f"({len(closures['canonical'])} canonical TeX sources)"
)
