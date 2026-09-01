#!/usr/bin/env python3
"""Source-level consistency checks for the mathematical proof corpus."""

from __future__ import annotations

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
        ROOT / "arrange/readable_paper" / target,
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
    "arrange/readable_paper/main.tex",
    "arrange/readable_paper/main.pdf",
    "interactive/readable_proof_dependency_graph.html",
]:
    if not (ROOT / required).is_file():
        fail(f"missing required file: {required}")

for forbidden in [
    "formalization",
    "tools",
    "release",
    ".vscode",
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

closures = {
    "canonical": tex_closure(ROOT / "arrange/paper_draft/main.tex"),
    "readable": tex_closure(ROOT / "arrange/readable_paper/main.tex"),
}
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
        for reference in re.findall(
            r"\\(?:eqref|ref|pageref|cref|Cref|autoref)\{([^}]+)\}", text
        ):
            references.append((reference, path))
    for reference, path in references:
        if reference not in labels:
            fail(f"unresolved {name} TeX reference {reference} in {path.relative_to(ROOT)}")

canonical = closures["canonical"]
for required in [
    "06_finite_enclosure_full.tex",
    "06_direct_local_calculus.tex",
    "06a_neighbor_ray_calculus.tex",
    "06b_ce1_direct_certificate.tex",
    "06c_exceptional_direct_terminals.tex",
    "06d_detailed_direct_certificates.tex",
    "06e_direct_local_proof_details.tex",
    "06f_casewise_witness_details.tex",
    "06g_endpoint_selector_audit.tex",
    "A_zero_gap_exact_certificate.tex",
]:
    path = (ROOT / "arrange/paper_draft" / required).resolve()
    if path not in canonical:
        fail(f"canonical TeX closure omits required source: {required}")

for path in canonical:
    if path.name.startswith("04_strategy2_") or path.name in {
        "04_boundary_propagation.tex",
        "04_strategy2_verification.tex",
    }:
        fail(f"canonical manuscript compiles obsolete source: {path.relative_to(ROOT)}")

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
    f"({len(closures['canonical'])} canonical and "
    f"{len(closures['readable'])} readable TeX sources)"
)
