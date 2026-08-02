from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def path(rel: str) -> Path:
    return ROOT / rel


def read(rel: str) -> str:
    return path(rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    p = path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    if text and not text.endswith("\n"):
        text += "\n"
    p.write_text(text, encoding="utf-8")


def replace_required(rel: str, old: str, new: str, count: int | None = None) -> None:
    text = read(rel)
    actual = text.count(old)
    if actual == 0:
        raise RuntimeError(f"{rel}: required text not found: {old!r}")
    if count is not None and actual != count:
        raise RuntimeError(f"{rel}: expected {count} copies, found {actual}: {old!r}")
    write(rel, text.replace(old, new))


def regex_required(rel: str, pattern: str, replacement: str) -> None:
    text = read(rel)
    new_text, actual = re.subn(pattern, lambda _m: replacement, text, count=1, flags=re.S)
    if actual != 1:
        raise RuntimeError(f"{rel}: expected one regex match: {pattern}")
    write(rel, new_text)


# 1. Final notation corrections in the authoritative proof and compiled TeX.
replace_required(
    "proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md",
    r"\nu_{\rm adj}",
    r"u_{\rm adj}",
    count=2,
)

strategy2_rel = "arrange/paper_draft/04_strategy2_verification.tex"
strategy2 = read(strategy2_rel)
strategy2 = strategy2.replace(r"\teq", r"\qquad")
strategy2 = strategy2.replace(r"\tep", r"\quad")
strategy2 = strategy2.replace(
    "explicit open Vd0 axis replacements",
    "explicit open Vd0 two-chart replacements",
)
strategy2 = strategy2.replace(
    "preserving every boundary and radial demand used by Proposition~\\ref{prop:nplus-zero-all-vd0}",
    "preserving full skeleton coverage required by Proposition~\\ref{prop:nplus-zero-all-vd0}",
)
strategy2 = strategy2.replace(
    "the resulting all-Vd0 configuration is impossible",
    "the resulting full-skeleton all-Vd0 configuration is impossible",
)
old_comment = "% ---- formerly 04_strategy2_verification.tex ----"
module_comments = [
    "% ---- Strategy 2 chain overview ----",
    "% ---- Exact local demand calculus ----",
    "% ---- Complete 407X audit and two-chart replacement ----",
    "% ---- CE2 exactly-one-Vd placement assembly ----",
]
if strategy2.count(old_comment) != len(module_comments):
    raise RuntimeError(
        f"{strategy2_rel}: expected {len(module_comments)} stale module comments, "
        f"found {strategy2.count(old_comment)}"
    )
for comment in module_comments:
    strategy2 = strategy2.replace(old_comment, comment, 1)
write(strategy2_rel, strategy2)

# Reader-facing wording follows the corrected proof interface.
for rel in [
    "arrange/paper_draft/04_strategy2_summary.tex",
    "arrange/paper_draft/04c_short_Vd_placements.tex",
]:
    text = read(rel)
    text = text.replace("axis replacements", "two-chart replacements")
    text = text.replace("axis replacement", "two-chart replacement")
    text = text.replace(
        "preserving every boundary and radial demand used by Proposition~\\ref{prop:nplus-zero-all-vd0}",
        "preserving full skeleton coverage required by Proposition~\\ref{prop:nplus-zero-all-vd0}",
    )
    text = text.replace(
        "preserving every boundary and radial demand",
        "preserving full skeleton coverage",
    )
    write(rel, text)

# 2. Replace stale duplicated architecture tables with the canonical layout.
ledger_table = r'''### Technical appendices

| File | Function |
|---|---|
| `appendix_roadmap.tex` | verification guide and proof-layer disclaimer |
| `02_structural_reductions.tex` | classifications, reaches, gaps, handoffs, routing |
| `02a_universal_calculus.tex` | transfers, residuals, center-free path budget |
| `02b_admissible_set_derivation.tex` | support derivation, cells, selectors, radial envelope |
| `04a_signed_center_calculus.tex` | signed CE1/CE2 equations, traces, exits, one-gap interface |
| `03_strategy1_length.tex` | perimeter and skeleton trace calculations |
| `04b_common_CE1_CE2_budgets.tex` | master deficit, short-role count, common budgets |
| `04c_short_Vd_placements.tex` | quarter envelope, rescuer profiles, radial separations |
| `04_strategy2_verification.tex` | consolidated Strategy 2 chains, exact endpoint calculus, complete `407X` audit, two-chart replacement, and CE2 one-Vd assembly |
| `05_strategy3_area.tex` | local area inequalities and cyclic certificates |
| `06_strategy4_ab_core.tex` | frontier, forcing, Newton reduction, adjacent overlaps |
| `06a_strategy4_exact_certificate.tex` | sole mixed-overlap certificate source: reduction, manifest, Bernstein proof, cap geometry |
| `appendix_symbols.tex` | notation cross-reference |

The body-end label'''
regex_required(
    "arrange/paper_draft/source_ledger.md",
    r"### Technical appendices\n\n.*?\nThe body-end label",
    ledger_table,
)

technical_guide = r'''### 3.2 Technical appendices

Use this order after `\\appendix`:

```text
appendix_roadmap.tex
02_structural_reductions.tex
02a_universal_calculus.tex
02b_admissible_set_derivation.tex
04a_signed_center_calculus.tex
03_strategy1_length.tex
04b_common_CE1_CE2_budgets.tex
04c_short_Vd_placements.tex
04_strategy2_verification.tex
05_strategy3_area.tex
06_strategy4_ab_core.tex
06a_strategy4_exact_certificate.tex
appendix_symbols.tex
```

The consolidated `04_strategy2_verification.tex` is the sole detailed
Strategy 2 appendix source. It contains the chain overview, exact local demand
calculus, complete incorporated `407X` audit, corrected two-chart Vd1
replacement, and authoritative CE2 exactly-one-Vd placement assembly.

`06a_strategy4_exact_certificate.tex` is the sole source for the mixed cap
overlap certificate. `06_strategy4_ab_core.tex` contains the analytic witness
geometry and cites that certificate; it must not input a duplicate certificate
file.

## 4. Required `main.tex` assembly'''
regex_required(
    "arrange/ams_paper_generation_guide.md",
    r"### 3\.2 Technical appendices\n\n.*?\n## 4\. Required `main\.tex` assembly",
    technical_guide,
)

main_assembly = r'''## 4. Required `main.tex` assembly

```latex
\\input{01_introduction}
\\input{02_reader_framework}
\\input{03_strategy1_reader}
\\input{04_strategy2_summary}
\\input{05_strategy3_reader}
\\input{06_strategy4_reader}
\\input{07_exhaustive_assembly}
\\label{page:proof-body-end}

\\clearpage
\\appendix
\\input{appendix_roadmap}
\\input{02_structural_reductions}
\\input{02a_universal_calculus}
\\input{02b_admissible_set_derivation}
\\input{04a_signed_center_calculus}
\\input{03_strategy1_length}
\\input{04b_common_CE1_CE2_budgets}
\\input{04c_short_Vd_placements}
\\input{04_strategy2_verification}
\\input{05_strategy3_area}
\\input{06_strategy4_ab_core}
\\input{06a_strategy4_exact_certificate}
\\input{appendix_symbols}
```

Place `\\raggedbottom` after `\\begin{document}`. Include a bibliography only
for verified external citations.

## 5. Paper-wide notation'''
regex_required(
    "arrange/ams_paper_generation_guide.md",
    r"## 4\. Required `main\.tex` assembly\n\n.*?\n## 5\. Paper-wide notation",
    main_assembly,
)

# Crosswalk metadata and a canonical-source notice.
crosswalk_rel = "arrange/paper_proof_crosswalk.md"
crosswalk = read(crosswalk_rel)
crosswalk = re.sub(r"Branch: `[^`]+`", "Branch: `main`", crosswalk, count=1)
crosswalk = re.sub(
    r"Last structural audit: \d{4}-\d{2}-\d{2}",
    "Last structural audit: 2026-08-02",
    crosswalk,
    count=1,
)
notice = '''\n### 2026-08-02 canonical-source update\n\nAll detailed Strategy 2 TeX verification now lives in\n`paper_draft/04_strategy2_verification.tex`. The corrected `4147` proof uses\nseparate charts at the two distinguished vertices and preserves the full\nskeleton; the invoked `4013` theorem is stated at skeleton-data strength.\n`06a_strategy4_exact_certificate.tex` is the only mixed-overlap certificate\nsource.\n'''
if "### 2026-08-02 canonical-source update" not in crosswalk:
    marker = "All repository links below are relative to this file in `arrange/`.\n"
    if marker not in crosswalk:
        raise RuntimeError("crosswalk insertion marker not found")
    crosswalk = crosswalk.replace(marker, marker + notice, 1)
write(crosswalk_rel, crosswalk)

# 3. Tighten the persistent source linter around the defects found in review.
lint_rel = "tools/proof_lint.py"
lint = read(lint_rel)
old_known_bad = '''known_bad = {
    r"Z_X=\\tau\\left\\lVert X\\right\\rVert^2-\\eta u": "31054 mixed residual uses u instead of nu",
    r"\\nu_A<u_B": "31054 coordinate typo nu_A",
    r"T_C\\cap e_{5,0}=\\[x,u\\]": "CE2 endpoint should be Greek nu",
    r"\\nu_2<1-H": "4144 local endpoint should be Latin u",
}'''
new_known_bad = '''known_bad = {
    r"Z_X=\\tau\\left\\lVert X\\right\\rVert^2-\\eta u": "31054 mixed residual uses u instead of nu",
    r"\\nu_A<u_B": "31054 coordinate typo nu_A",
    r"T_C\\cap e_{5,0}=\\[x,u\\]": "CE2 endpoint should be Greek nu",
    r"\\nu_2<1-H": "4144 local endpoint should be Latin u",
    r"\\nu_{\\rm adj}": "4147 adjacent radial endpoint should be Latin u",
    r"\\teq": "unexpanded TeX spacing placeholder \\\\teq",
    r"\\tep": "unexpanded TeX spacing placeholder \\\\tep",
}'''
if old_known_bad not in lint:
    raise RuntimeError("proof_lint.py: known_bad block not found")
lint = lint.replace(old_known_bad, new_known_bad, 1)
insert_after = '''if (ROOT / "arrange/paper_draft/appendix_exact_mixed_overlap.tex").exists():
    fail("duplicate Strategy 4 certificate file still exists")
'''
extra_checks = '''if (ROOT / "arrange/paper_draft/appendix_exact_mixed_overlap.tex").exists():
    fail("duplicate Strategy 4 certificate file still exists")

strategy2_text = (ROOT / "arrange/paper_draft/04_strategy2_verification.tex").read_text(encoding="utf-8")
for stale in [
    "% ---- formerly 04_strategy2_verification.tex ----",
    "explicit open Vd0 axis replacements",
    "preserving every boundary and radial demand used by Proposition~\\\\ref{prop:nplus-zero-all-vd0}",
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
'''
lint = lint.replace(insert_after, extra_checks, 1)
write(lint_rel, lint)

# 4. Ignore and remove committed LaTeX intermediates while retaining main.pdf.
gitignore = read(".gitignore")
ignore_block = '''\n# Paper build intermediates; the rebuilt PDF remains tracked.
arrange/paper_draft/main.aux
arrange/paper_draft/main.fdb_latexmk
arrange/paper_draft/main.fls
arrange/paper_draft/main.log
arrange/paper_draft/main.out
arrange/paper_draft/main.toc
arrange/paper_draft/main.xdv
arrange/paper_draft/main.synctex.gz
'''
if "# Paper build intermediates" not in gitignore:
    gitignore += ignore_block
write(".gitignore", gitignore)
for name in [
    "main.aux",
    "main.fdb_latexmk",
    "main.fls",
    "main.log",
    "main.out",
    "main.toc",
    "main.xdv",
    "main.synctex.gz",
]:
    candidate = path(f"arrange/paper_draft/{name}")
    if candidate.exists():
        candidate.unlink()

# 5. Record the independent post-commit review and leave a page-count placeholder.
audit_rel = "arrange/20260802_repair_and_reaudit.md"
audit = read(audit_rel)
section = '''\n## Independent post-commit source audit\n\nA second read of the committed tree found and repaired three nonmathematical\ndefects: the remaining `\\nu_{\\rm adj}` transcription in the Markdown source,\ntwo unexpanded TeX spacing placeholders, and stale duplicated architecture\ndocumentation. The review also removed accidentally committed LaTeX\nintermediates and strengthened the linter to reject recurrence. No new defect\nwas found in the two-chart reach calculation, skeleton preservation, the\nstrengthened `4013` rank split, `2110`, or the exhaustive `414b` placement\naudit.\n\nFinal rebuilt PDF page count: FINAL_BUILD_PAGE_COUNT.\n'''
if "## Independent post-commit source audit" not in audit:
    audit += section
else:
    audit = re.sub(
        r"## Independent post-commit source audit.*?Final rebuilt PDF page count: .*?\.\n",
        section.lstrip("\n"),
        audit,
        flags=re.S,
    )
write(audit_rel, audit)

print("final source cleanup applied")
