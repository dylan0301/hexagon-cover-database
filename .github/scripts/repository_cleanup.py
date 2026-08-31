#!/usr/bin/env python3
"""One-shot cleanup after removal of the abandoned Lean formalization.

The file deletes itself and its trigger workflow before the final squashed
commit is created.
"""

from __future__ import annotations

import re
import shutil
import stat
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def remove(relative: str) -> None:
    path = ROOT / relative
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def move(source_relative: str, target_relative: str) -> None:
    source = ROOT / source_relative
    target = ROOT / target_relative
    if not source.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        remove(target_relative)
    shutil.move(str(source), str(target))


def write(relative: str, content: str, *, executable: bool = False) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    if executable:
        path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def patch(relative: str, replacements: list[tuple[str, str]]) -> None:
    path = ROOT / relative
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    revised = text
    for old, new in replacements:
        revised = revised.replace(old, new)
    if revised != text:
        path.write_text(revised, encoding="utf-8")


def replace_in_text_tree(replacements: list[tuple[str, str]]) -> None:
    suffixes = {".md", ".tex", ".py", ".sh", ".yml", ".yaml", ".json", ".html", ".txt"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "prompts" in path.parts:
            continue
        if path.name != ".gitignore" and path.suffix.lower() not in suffixes:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        revised = text
        for old, new in replacements:
            revised = revised.replace(old, new)
        if revised != text:
            path.write_text(revised, encoding="utf-8")


# Remove root-level auxiliary infrastructure.
for relative in [
    "CONTRIBUTING.md",
    "REPRODUCE.md",
    "requirements-proof.txt",
    ".github/CODEOWNERS",
    ".github/pull_request_template.md",
    ".github/workflows/paper-rebuild.yml",
    ".github/workflows/proof-ci.yml",
    ".github/workflows/readable-paper-rebuild.yml",
    "release",
    ".vscode",
]:
    remove(relative)


# Retain useful generators and PDF auditors next to the content they support.
move("tools/compare_pdfs_semantically.py", "arrange/_support/compare_pdfs_semantically.py")
move("tools/verify_pdf_render.py", "arrange/_support/verify_pdf_render.py")
move("tools/build_proof_free_paper.sh", "arrange/_support/build_proof_free_paper.sh")
move("tools/generate_readable_dependency_graph.py", "interactive/_support/generate_dependency_graph.py")
move("tools/generate_trace_exact_ab_assets.py", "interactive/_support/generate_trace_assets.py")

for relative in [
    "arrange/_support/compare_pdfs_semantically.py",
    "arrange/_support/verify_pdf_render.py",
    "interactive/_support/generate_dependency_graph.py",
    "interactive/_support/generate_trace_assets.py",
]:
    patch(relative, [("ROOT = Path(__file__).resolve().parents[1]", "ROOT = Path(__file__).resolve().parents[2]")])

patch(
    "arrange/_support/build_proof_free_paper.sh",
    [('REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd -P)"', 'REPO_ROOT="$(cd -- "$SCRIPT_DIR/../.." && pwd -P)"')],
)

patch(
    "interactive/_support/generate_dependency_graph.py",
    [
        ('REPORT = READABLE / "IMPLEMENTATION_REPORT.md"', 'REPORT = ROOT / "arrange" / "README.md"'),
        ('BRANCH = "No-more-strategy-2"', 'BRANCH = "main"'),
        ('SOURCE_HEAD = "048320ccade291fc828c1b51fff167ebb7cb29cc"', 'SOURCE_HEAD = "main"'),
        ("original files untouched", "self-contained publication graph"),
        ("additive reader-facing publication layer", "reader-facing publication layer"),
        ("additive readable paper", "readable paper"),
    ],
)
remove("tools")


# Remove formalization-only and retired scalar-compatibility sources.
for relative in [
    "arrange/paper_draft/04_boundary_propagation.tex",
    "arrange/paper_draft/04_strategy2_optimization_core.tex",
    "arrange/paper_draft/04_strategy2_optimization_domain.tex",
    "arrange/paper_draft/04_strategy2_optimization_labels.tex",
    "arrange/paper_draft/04_strategy2_optimization_map.tex",
    "arrange/paper_draft/04_strategy2_optimization_problems.tex",
    "arrange/paper_draft/04_strategy2_optimization_registered.tex",
    "arrange/paper_draft/04_strategy2_optimization_rescuer.tex",
    "arrange/paper_draft/04_strategy2_optimization_t3.tex",
    "arrange/paper_draft/04_strategy2_optimization_vd.tex",
    "arrange/paper_draft/04_strategy2_summary.tex",
    "arrange/paper_draft/04_strategy2_verification.tex",
    "arrange/paper_draft/04d_strategy2_parameter_bridges.tex",
    "arrange/paper_draft/04e_strategy2_verification_00_provenance_manifest.tex",
    "arrange/paper_draft/04e_strategy2_verification_01_registered_applications.tex",
    "arrange/paper_draft/04e_strategy2_verification_02_exact_local_demand_calculus.tex",
    "arrange/paper_draft/04e_strategy2_verification_03_cyclic_propagation_in_the_all_vdzero_cases.tex",
    "arrange/paper_draft/04e_strategy2_verification_04_nonsupercritical_t3_like_and_vd1_vd2_demand_branches.tex",
    "arrange/paper_draft/04e_strategy2_verification_05_exact_endpoint_and_replacement_verification.tex",
    "arrange/paper_draft/04e_strategy2_verification_06_authoritative_ce2_one_vd_placement_assembly.tex",
    "arrange/paper_draft/04f_strategy2_pure_theorems.tex",
    "proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2111_strategy2_pure_optimization_registry.md",
]:
    remove(relative)

for relative in [
    "arrange/CURRENT_VERIFICATION_SUMMARY.txt",
    "arrange/ams_paper_generation_guide.md",
    "arrange/paper_proof_crosswalk.md",
    "arrange/update_log",
    "arrange/paper_draft/source_ledger.md",
    "arrange/paper_draft/20260728_body_appendix_validity_repair_audit.md",
    "arrange/paper_draft/appendix_certificates.tex",
    "arrange/paper_draft/appendix_roadmap.tex",
    "arrange/paper_draft/appendix_symbols.tex",
    "arrange/paper_draft/proof_free.pdf",
    "arrange/readable_paper/IMPLEMENTATION_REPORT.md",
    "arrange/readable_paper/ORIGINAL_SOURCE_MANIFEST.json",
    "arrange/readable_paper/SOURCE_CROSSWALK.md",
    "arrange/readable_paper/README.md",
    "arrange/readable_paper/build.sh",
    "proof/ACTIVE_DEPENDENCIES.txt",
    "proof/ACTIVE_DEPENDENCY_GRAPH.json",
    "proof/MANIFEST.txt",
    "proof/407X_PROVENANCE.json",
]:
    remove(relative)

# Remove generated logs and compiled side-products from the proof tree.
for path in (ROOT / "proof").rglob("*"):
    if not path.is_file():
        continue
    if path.suffix.lower() in {".log", ".aux", ".out", ".toc", ".xdv", ".pdf"} or path.name.endswith(".synctex.gz"):
        path.unlink()

# Colocate the active exact-certificate provenance with its code and data.
provenance_source = ROOT / "proof/3105X_CERTIFICATE_PROVENANCE.json"
provenance_target = (
    ROOT
    / "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/"
    "3105X_self_contained_direct_Vd0_nine_point/3105X_computation/"
    "certificate_provenance.json"
)
if provenance_source.is_file():
    provenance_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(provenance_source), str(provenance_target))

# Remove stale lines that pointed only to the deleted compatibility interface.
for path in (ROOT / "proof").rglob("*.md"):
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = []
    for line in text.splitlines():
        if any(
            token in line
            for token in [
                "2111_strategy2_pure_optimization_registry",
                "formalization/strategy2_optimization",
                "04_strategy2_optimization_",
                "04_strategy2_verification",
            ]
        ):
            continue
        lines.append(line)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


# Normalize historical Strategy-4 filenames to the current three-method paper.
move("arrange/paper_draft/06a_strategy4_exact_certificate.tex", "arrange/paper_draft/A_zero_gap_exact_certificate.tex")
move("arrange/paper_draft/06_strategy4_ab_core.tex", "arrange/paper_draft/06_zero_gap_ab_core.tex")
move("arrange/paper_draft/06_strategy4_completion.tex", "arrange/paper_draft/06_zero_gap_completion.tex")
move("interactive/strategy4demo.html", "interactive/zero_gap_nine_point_demo.html")

replace_in_text_tree(
    [
        ("06a_strategy4_exact_certificate", "A_zero_gap_exact_certificate"),
        ("06_strategy4_ab_core", "06_zero_gap_ab_core"),
        ("06_strategy4_completion", "06_zero_gap_completion"),
        ("strategy4demo.html", "zero_gap_nine_point_demo.html"),
        (
            "proof/3105X_CERTIFICATE_PROVENANCE.json",
            "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/certificate_provenance.json",
        ),
    ]
)


# Remove obsolete interactive pages and the duplicated companion JSON.
for relative in [
    "interactive/strategy2demo.html",
    "interactive/strategy2notation.html",
    "interactive/readable_proof_dependency_data.json",
]:
    remove(relative)


# Archive the flat prompt history by month.
prompts = ROOT / "prompts"
prompts.mkdir(exist_ok=True)
archive = prompts / "archive"
active = prompts / "active"
archive.mkdir(exist_ok=True)
active.mkdir(exist_ok=True)
for path in list(prompts.iterdir()):
    if not path.is_file() or path.name == "README.md":
        continue
    match = re.match(r"^(20\d{2})(\d{2})", path.name)
    destination = (
        archive / f"{match.group(1)}-{match.group(2)}" / path.name
        if match
        else archive / "undated" / path.name
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(path), str(destination))


write(
    "README.md",
    r"""
# Hexagon Covering Proof Corpus

This repository contains the proof that seven open unit equilateral triangles
do not cover a regular hexagon of side length one.

\[
\boxed{\text{The regular unit hexagon cannot be covered by seven open unit
 equilateral triangles.}}
\]

The authoritative mathematical material is maintained in four content
directories:

- [`proof/`](proof/): numbered proof sources, exact certificates, and status
  information;
- [`arrange/`](arrange/): the canonical manuscript, the reader-oriented
  manuscript, and publication support;
- [`interactive/`](interactive/): self-contained visual explanations and
  dependency navigation;
- [`prompts/`](prompts/): research prompts and their dated archive.

No proof-assistant formalization is maintained at present. The former partial
Lean statement project was deleted because it did not prove the geometric
argument and is no longer part of the repository contract.

## Main entry points

- Main theorem and exhaustive assembly:
  [`proof/0XXX_main/0000_main_theorem.md`](proof/0XXX_main/0000_main_theorem.md)
- Proof-tree index:
  [`proof/0XXX_main/0001_proof_tree_index.md`](proof/0XXX_main/0001_proof_tree_index.md)
- Current status:
  [`proof/0XXX_main/0002_status_and_dependencies.md`](proof/0XXX_main/0002_status_and_dependencies.md)
- Canonical paper:
  [`arrange/paper_draft/main.pdf`](arrange/paper_draft/main.pdf)
- Reader-oriented paper:
  [`arrange/readable_paper/main.pdf`](arrange/readable_paper/main.pdf)
- Interactive proof dependency graph:
  [`interactive/readable_proof_dependency_graph.html`](interactive/readable_proof_dependency_graph.html)
- Trace-exact \(AB\)-envelope explorer:
  [`interactive/trace_exact_ab_envelope_explorer.html`](interactive/trace_exact_ab_envelope_explorer.html)
- Zero-gap nine-point demonstration:
  [`interactive/zero_gap_nine_point_demo.html`](interactive/zero_gap_nine_point_demo.html)

## Proof architecture

Seven distinguished points canonically identify one C triangle and six V
triangles. The C triangle is classified as CE0, CE1, or CE2. Each V triangle
is classified as Vd0, Vd1, Vd2, or T3-like. Every hypothetical cover is routed
to one of three methods:

1. trace-length or skeleton-length contradiction;
2. normalized area-loss contradiction;
3. a direct finite equilateral-enclosure contradiction.

For a V triangle, uppercase \((A_i,B_i,C_i)\) denotes actual maximal reaches.
Lowercase \((a_i,b_i,c_i)\) denotes selected lower bounds. In particular,
\(N_+\) is defined from the uppercase actual reaches. Singleton boundary gaps
remain gaps because the covering triangles are open.

The difficult zero-gap nine-point overlap calculation is an exact certificate
over integers, rationals, and \(\mathbb Q(\sqrt3)\). Floating-point scans are
not proof dependencies.

## Validation

```bash
python -m pip install -r arrange/_support/requirements.txt
python proof/check.py
python interactive/generate.py --dependency-graph --check
python interactive/check.py
python arrange/build.py --all
```

GitHub Actions runs the same source, exact-certificate, interactive, and paper
checks on every branch and pull request. Generated verification summaries,
release ZIP files, dependency manifests, and LaTeX intermediates are not
tracked.
""",
)

write(
    "AGENTS.md",
    r"""
# Repository instructions

## Mathematical authority

A mathematical claim is established by a numbered source under `proof/` whose
status supports the claim, or by an exact certificate explicitly incorporated
by the paper. Navigation files, interactive pages, prompts, experiments, and
failed approaches are not proof authorities.

## Non-negotiable conventions

- Use **C triangle** and **V triangle**.
- Let the original open triangles be \(U_C,U_0,\ldots,U_5\), with
  \(O\in U_C\) and \(V_i\in U_i\). Put \(T_C=\overline{U_C}\) and
  \(T_i=\overline{U_i}\). Use closed classifications on the \(T\)'s and retain
  the \(U\)'s whenever openness matters.
- Uppercase \((A_i,B_i,C_i)\) denotes actual maximal reaches.
- Lowercase \((a_i,b_i,c_i)\) denotes selected lower bounds and must be
  introduced by an explicit inequality such as \(a_i\le A_i\).
- Define \(N_+\) only from \(A_i+B_i>1\).
- Preserve singleton boundary gaps.
- Preserve the CE1/CE2 distinction, all endpoint strictness, actual V-type
  restrictions on neighboring support, connected-component selectors, and
  both charts in the Vd1 replacement.
- Do not replace the exact zero-gap certificate by numerical evidence.

## Repository layout

- `proof/`: proof sources and certificate code.
- `arrange/`: canonical and reader-oriented papers.
- `interactive/`: generated and hand-authored visual explanations.
- `prompts/`: research prompt archive.

Do not recreate a top-level `tools`, `release`, `.vscode`, or formalization
directory. Put support code next to the content it validates.

## Required checks

```bash
python -m pip install -r arrange/_support/requirements.txt
python proof/check.py
python interactive/generate.py --dependency-graph --check
python interactive/check.py
python arrange/build.py --all
```

Run the two exact zero-gap certificate programs whenever their source,
provenance, or dependent theorem changes.
""",
)

write(
    ".gitignore",
    r"""
__pycache__/
*.pyc
.venv/
.venv-*/
arrange/_build/
interactive/readable_proof_dependency_data.json

# LaTeX intermediates.
arrange/paper_draft/*.aux
arrange/paper_draft/*.fdb_latexmk
arrange/paper_draft/*.fls
arrange/paper_draft/*.log
arrange/paper_draft/*.out
arrange/paper_draft/*.toc
arrange/paper_draft/*.xdv
arrange/paper_draft/*.synctex.gz
arrange/paper_draft/proof_free.pdf

arrange/readable_paper/*.aux
arrange/readable_paper/*.fdb_latexmk
arrange/readable_paper/*.fls
arrange/readable_paper/*.log
arrange/readable_paper/*.out
arrange/readable_paper/*.toc
arrange/readable_paper/*.xdv
arrange/readable_paper/*.synctex.gz

# Generated proof navigation.
proof/ACTIVE_DEPENDENCIES.txt
proof/ACTIVE_DEPENDENCY_GRAPH.json
proof/MANIFEST.txt
""",
)

write(
    "arrange/README.md",
    r"""
# Manuscripts and publication support

`arrange/` contains two presentations of the same proof.

## Canonical manuscript

`paper_draft/main.tex` is the self-contained publication source. Its body has
three proof methods:

1. trace length;
2. area loss;
3. direct finite enclosure.

The appendix `A_zero_gap_exact_certificate.tex` records the exact
mixed-overlap certificate required by the zero-gap nine-point theorem.

## Reader-oriented manuscript

`readable_paper/main.tex` reorganizes the same mathematics for navigation. It
separates the local finite-enclosure toolkit, the universal nonzero-gap
terminals, the named nonzero-gap cases, and the zero-gap nine-point
obstruction.

The numbered files under `proof/` remain the authority for theorem status and
hypotheses. The two manuscripts are publication layers, not competing proof
owners.

## Section-to-proof map

| Manuscript component | Principal proof material |
|---|---|
| Introduction and routing | `0000`, `1003`, `1101`, `1201`, `1214`, `2530` |
| Common geometry | `1001`-`1214`, `2004`, `2008`, `2100`, `2109` |
| Trace-length method | `2500`, `2510`, `2520`, `2530` and routed terminals |
| Area-loss method | `317X`, `320X` |
| Nonzero-gap finite enclosure | `2608`, `4013_new`, `4070_new`, `4101_new`, `4102_new`, `4130_new`, `4140_new` |
| Zero-gap nine-point theorem | `31050`-`31059` and `3105X_computation` |
| Exhaustive completion | `0000` |

## Commands

```bash
python -m pip install -r arrange/_support/requirements.txt
python arrange/build.py --canonical
python arrange/build.py --readable
python arrange/build.py --all
arrange/_support/build_proof_free_paper.sh
```

The build command uses a temporary source copy, so LaTeX intermediates do not
pollute the source directories. The tracked PDFs are publication artifacts.
CI compares clean rebuilds against them by stable PDF semantics and rendered
pixels.
""",
)

write(
    "interactive/README.md",
    r"""
# Interactive explanations

The files in this directory are explanatory interfaces, not proof
certificates.

- `readable_proof_dependency_graph.html`: clickable formal-statement graph,
  routing table, case cards, and embedded figures;
- `trace_exact_ab_envelope_explorer.html`: trace-exact \(AB\)-envelopes,
  actual gaps, and finite witnesses;
- `trace_exact_ab_presets.json`: deterministic visualization presets;
- `zero_gap_nine_point_demo.html`: zero-gap finite-enclosure mechanism.

```bash
python interactive/generate.py --dependency-graph
python interactive/generate.py --dependency-graph --check
python interactive/check.py
```

The generated companion JSON is intentionally ignored because the HTML already
contains the complete data payload and offers it as a download.
""",
)

write(
    "prompts/README.md",
    r"""
# Research prompts

Existing prompts are stored chronologically under `archive/YYYY-MM/`.
`active/` is reserved for prompts currently being developed.

Prompt files document research directions and editorial requests. They do not
establish theorem status. Accepted mathematical results must be transferred to
numbered sources under `proof/`, and accepted presentation changes must be
transferred to `arrange/` or `interactive/`.
""",
)

write(
    "prompts/active/README.md",
    r"""
# Active prompts

Place current research or editorial prompts here. Move completed prompts to the
appropriate `../archive/YYYY-MM/` directory.
""",
)

write(
    "arrange/_support/requirements.txt",
    """
sympy==1.14.0
PyMuPDF==1.26.7
mistune==3.1.3
""",
)

write(
    "proof/check.py",
    r'''#!/usr/bin/env python3
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
''',
    executable=True,
)

write(
    "arrange/build.py",
    r'''#!/usr/bin/env python3
"""Build the canonical and reader-oriented manuscripts in temporary copies."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARRANGE = ROOT / "arrange"


def ignore_source(directory: str, names: list[str]) -> set[str]:
    ignored = {"_build", "__pycache__"}
    for name in names:
        if name.endswith((".aux", ".fdb_latexmk", ".fls", ".log", ".out", ".toc", ".xdv", ".synctex.gz")):
            ignored.add(name)
        if name in {"main.pdf", "proof_free.pdf"}:
            ignored.add(name)
    return ignored


def check_log(log: Path) -> None:
    text = log.read_text(encoding="utf-8", errors="replace")
    if re.search(
        r"LaTeX Warning: (Reference .* undefined|There were undefined references|Label .* multiply defined)",
        text,
    ):
        raise SystemExit(f"undefined or multiply-defined references in {log}")
    overfull = re.findall(r"Overfull \\[hv]box.*", text)
    if overfull:
        raise SystemExit("overfull boxes found:\n" + "\n".join(overfull))


def build_one(source_name: str, output: Path) -> None:
    with tempfile.TemporaryDirectory(prefix=f"hexagon-cover-{source_name}-") as td:
        workspace = Path(td) / "arrange"
        shutil.copytree(ARRANGE, workspace, ignore=ignore_source)
        source = workspace / source_name
        env = os.environ.copy()
        env.update({"SOURCE_DATE_EPOCH": "946684800", "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        subprocess.run(
            [
                "latexmk",
                "-xelatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                "main.tex",
            ],
            cwd=source,
            env=env,
            check=True,
        )
        pdf = source / "main.pdf"
        log = source / "main.log"
        if not pdf.is_file() or not log.is_file():
            raise SystemExit(f"{source_name} build did not produce main.pdf and main.log")
        check_log(log)
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf, output)


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--canonical", action="store_true")
    group.add_argument("--readable", action="store_true")
    group.add_argument("--all", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "arrange/_build")
    args = parser.parse_args()

    if not (args.canonical or args.readable or args.all):
        args.all = True

    if args.canonical or args.all:
        build_one("paper_draft", args.output_dir / "canonical.pdf")
        print(args.output_dir / "canonical.pdf")
    if args.readable or args.all:
        build_one("readable_paper", args.output_dir / "readable.pdf")
        print(args.output_dir / "readable.pdf")


if __name__ == "__main__":
    main()
''',
    executable=True,
)

write(
    "interactive/generate.py",
    r'''#!/usr/bin/env python3
"""Regenerate interactive publication assets."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEPENDENCY = ROOT / "interactive/_support/generate_dependency_graph.py"
TRACE = ROOT / "interactive/_support/generate_trace_assets.py"
HTML = ROOT / "interactive/readable_proof_dependency_graph.html"
JSON_DATA = ROOT / "interactive/readable_proof_dependency_data.json"


def run(script: Path) -> None:
    subprocess.run([sys.executable, str(script)], cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dependency-graph", action="store_true")
    parser.add_argument("--trace-assets", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if not args.dependency_graph and not args.trace_assets:
        args.dependency_graph = True

    if args.dependency_graph:
        run(DEPENDENCY)
        if JSON_DATA.exists():
            JSON_DATA.unlink()
        if args.check:
            subprocess.run(
                ["git", "diff", "--exit-code", "--", str(HTML.relative_to(ROOT))],
                cwd=ROOT,
                check=True,
            )

    if args.trace_assets:
        run(TRACE)
        if args.check:
            subprocess.run(
                [
                    "git",
                    "diff",
                    "--exit-code",
                    "--",
                    "interactive/trace_exact_ab_envelope_explorer.html",
                    "interactive/trace_exact_ab_presets.json",
                    "arrange/paper_draft/06i_trace_exact_ab_atlas.tex",
                    "arrange/paper_draft/figures/trace_exact_ab",
                ],
                cwd=ROOT,
                check=True,
            )


if __name__ == "__main__":
    main()
''',
    executable=True,
)

write(
    "interactive/check.py",
    r'''#!/usr/bin/env python3
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
''',
    executable=True,
)

write(
    "proof/0XXX_main/0002_status_and_dependencies.md",
    r"""
# Status and Active Dependencies

Status: Reference

This file records the active three-method proof interfaces. It does not
upgrade the status of any listed source.

## Foundations and shared geometry

| Item | Source | Status |
|---|---|---|
| Open/closed/scaled equivalence | [`1003`](../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md) | Proven |
| Center classification | [`1101`](../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md) | Proven |
| Vertex classification | [`1201`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) | Proven |
| Strict handoff selection | [`1214`](../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) | Proven |
| Exact own-ray admissible set | [`2004`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md) | Proven |
| Exact neighboring-ray capacity | [`2008`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md) | Proven |
| Signed CE1/CE2 normal form | [`2109`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md) | Proven |
| Common trace and skeleton budgets | [`2500`](../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md), [`2530`](../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md) | Proven |
| Radial-witness and gap-enclosure lemmas | [`2608`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md) | Proven |

## Active branch terminals

| Branch | Source | Status |
|---|---|---|
| Zero-gap all-Vd0 exact-one | [`31058`](../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md) | Proven |
| Nonzero-gap, \(N_+=0\), all Vd0 | [`4013_new`](../4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md) | Proven |
| Nonzero-gap, \(N_+=0\), one or two T3-like roles | [`4070_new`](../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md) | Proven |
| Nonzero-gap, \(N_+=1\), all Vd0 | [`4101_new`](../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4101_new_all_Vd0_finite_enclosure.md), [`4102_new`](../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4102_new_CE1_direct_radial_certificate.md) | Proven |
| Nonzero-gap, \(N_+=1\), exactly one T3-like role | [`4130_new`](../4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) | Proven |
| CE2 nonzero-gap, \(N_+=1\), exactly one Vd1/Vd2 role | [`4140_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md) | Proven |

The trace-length method retains the terminals `4040`, `4041`, `4110`,
`4111`, `4123`, `4149`, `414a`, and `4200`. The area-loss method retains the
zero-gap certificates `317X` and `320X`.

## Exact certificate

The zero-gap nine-point mixed overlaps are established by the exact
`3105X_computation` package. Its source, sparse data, derivation check,
positivity check, and provenance record are colocated with the theorem.

No proof-assistant formalization is currently maintained. The complete
mathematical arguments are the numbered proof sources and the two manuscript
presentations.
""",
)

write(
    ".github/workflows/ci.yml",
    r"""
name: Proof and publication checks

on:
  push:
  pull_request:
  workflow_dispatch:

permissions:
  contents: read

concurrency:
  group: proof-publication-${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

env:
  SOURCE_DATE_EPOCH: '946684800'
  FORCE_SOURCE_DATE: '1'
  TZ: UTC

jobs:
  source:
    name: Proof, certificate, and interactive sources
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@f548e57e544e1ff5a4c46bf1e1b8685f8e4a348a
        with:
          fetch-depth: 0

      - uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97
        with:
          python-version: '3.12'

      - uses: actions/setup-node@49933ea5288caeca8642d1e84afbd3f7d6820020
        with:
          node-version: '22'

      - name: Install pinned audit dependencies
        run: python -m pip install --disable-pip-version-check -r arrange/_support/requirements.txt

      - name: Check proof and manuscript source interfaces
        run: python proof/check.py

      - name: Replay exact zero-gap derivation and positivity certificates
        working-directory: proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation
        run: |
          python verify_mixed_overlap_core_derivation.py
          python verify_global_core_positivity.py

      - name: Check generated dependency graph
        run: python interactive/generate.py --dependency-graph --check

      - name: Audit self-contained interactive pages
        run: python interactive/check.py

      - name: Check repository whitespace
        run: git diff --check

  papers:
    name: Clean manuscript rebuilds
    needs: source
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@f548e57e544e1ff5a4c46bf1e1b8685f8e4a348a

      - uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97
        with:
          python-version: '3.12'

      - name: Install pinned PDF-audit dependencies
        run: python -m pip install --disable-pip-version-check -r arrange/_support/requirements.txt

      - name: Build both papers in pinned TeX Live 2025
        uses: xu-cheng/texlive-action@22c04326a5d855880f9d39bb955138bf11c6df80
        with:
          docker_image: >-
            ghcr.io/xu-cheng/texlive-historic-debian:2025@sha256:d3e42adc0c8d84bc913bfc33571feaf7037616260a771bb6f027504661568bf6
          run: |
            set -euo pipefail
            python3 arrange/build.py --all --output-dir arrange/_build

      - name: Compare rebuilt papers with tracked publication artifacts
        run: |
          python arrange/_support/compare_pdfs_semantically.py \
            arrange/paper_draft/main.pdf arrange/_build/canonical.pdf --dpi 144
          python arrange/_support/compare_pdfs_semantically.py \
            arrange/readable_paper/main.pdf arrange/_build/readable.pdf --dpi 144
          python arrange/_support/verify_pdf_render.py arrange/_build/canonical.pdf
          python arrange/_support/verify_pdf_render.py arrange/_build/readable.pdf
          python - <<'PY'
          from pathlib import Path
          import fitz

          bounds = {
              Path("arrange/_build/canonical.pdf"): (84, 104),
              Path("arrange/_build/readable.pdf"): (85, 110),
          }
          for path, (lower, upper) in bounds.items():
              pages = fitz.open(path).page_count
              print(f"{path}: {pages} pages")
              if not lower <= pages <= upper:
                  raise SystemExit(
                      f"unexpected page count for {path}: {pages}; expected {lower}-{upper}"
                  )
          PY

      - uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a
        with:
          name: verified-publication-artifacts
          path: |
            arrange/_build/canonical.pdf
            arrange/_build/readable.pdf
            interactive/readable_proof_dependency_graph.html
          if-no-files-found: error
""",
)

# Remove the temporary cleanup machinery before the final tree is committed.
remove(".github/workflows/repository-cleanup.yml")
remove(".github/scripts/repository_cleanup.py")

print("repository cleanup applied")
