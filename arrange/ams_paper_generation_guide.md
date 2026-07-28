# AMS-Style Main-Theorem Paper Generation Guide

This file is an authoring specification, not a proof source. It maintains the
AMS-style manuscript proving the theorem in
[`0000_main_theorem.md`](../proof/0XXX_main/0000_main_theorem.md).

The proof corpus is authoritative for hypotheses, theorem statements, and
status. The paper may reorganize proved material, but it may not strengthen a
result, erase a strictness condition, confuse actual reaches with selected
demands, or treat a navigation file as a proof.

## 1. Required reading and status rules

Before changing the manuscript, read:

- [`README.md`](../README.md);
- [`0000_main_theorem.md`](../proof/0XXX_main/0000_main_theorem.md);
- [`0001_proof_tree_index.md`](../proof/0XXX_main/0001_proof_tree_index.md);
- [`0002_status_and_dependencies.md`](../proof/0XXX_main/0002_status_and_dependencies.md);
- [`0910_notation_dictionary.md`](../proof/09XX_appendices/0910_notation_dictionary.md);
- [`1006_proof_status_conventions.md`](../proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md);
- [`201d_raw_and_relaxed_g_chains.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md);
- [`source_ledger.md`](paper_draft/source_ledger.md).

Apply the following rules.

1. Use a mathematical result as established only when its numbered source has
   sufficient status, normally `Status: Proven`, or is an exact definition.
2. A `Reference` or index file supplies navigation only.
3. A `Reduction` proves only its stated reduction and closes no branch without
   proved terminal dependencies.
4. Never promote `Strategy`, `Empirical`, `Experiment`, `Lemma target`,
   `Practically proven`, or `Failed` material into the proof.
5. Preserve every hypothesis involving open versus closed triangles, interior
   membership, strict inequalities, positive-length traces, midpoint coverage,
   center type, vertex type, and actual `N_+`.
6. A plot or floating-point computation is not a proof.
7. An exact computer-assisted certificate is an allowed proof dependency only
   when its mathematical reduction, exact arithmetic model, complete input,
   authentication data, and verifier are formally incorporated and identified.
8. Record reusable mathematical corrections in `proof/` as well as in the
   manuscript.
9. Preserve the existing Strategy 1 assignments, including the length part of
   the exceptional CE2 one-Vd1/Vd2 row.

## 2. Proof layers and reader-body contract

The manuscript is split at `\appendix` into a reader-facing proof body and
technical verification modules. The complete proof consists of:

1. the body;
2. the TeX appendices;
3. any exact electronic supplements formally incorporated by path, Git blob,
   and transcript digest.

The body should make the complete contradiction understandable without forcing
the reader to follow long algebra. It is not described as independently proving
every calculation lemma.

### 2.1 Page budget

The body, including title, abstract, contents, definitions, figures, and final
assembly, should end on or before page 20. Use a section-only table of contents:

```latex
\setcounter{tocdepth}{1}
\tableofcontents
```

`main.tex` places

```latex
\label{page:proof-body-end}
```

immediately before `\clearpage\appendix`. A later authorized complete build
must inspect the page attached to this label. A source-only edit does not by
itself certify the page count.

### 2.2 Material allowed in the body

The body should contain:

- definitions of every symbol used in the proof flow;
- role and case classifications;
- geometric intuition and explanatory figures;
- exact calculation outputs, such as the admissible-set description;
- named terminal propositions with complete branch hypotheses;
- short conceptual sums, monotone-chain logic, and final routing.

The body should not contain:

- support-line case derivations;
- large polynomial expansions;
- root-selection calculations;
- derivative sign audits;
- rational parametrization calculations;
- Gram reductions;
- Bernstein coefficient data;
- code listings or run logs.

## 3. Active manuscript architecture

All persistent paper artifacts live under `arrange/paper_draft/`.

### 3.1 Reader-facing body

The required order is:

```text
01_introduction.tex
02_reader_framework.tex
03_strategy1_reader.tex
04_strategy2_summary.tex
05_strategy3_reader.tex
06_strategy4_reader.tex
07_exhaustive_assembly.tex
```

Their functions are:

- `01_introduction.tex`: theorem, roles, notation, routing table, proof flow.
- `02_reader_framework.tex`: structural interface, explicit admissible set,
  corrected transfer alphabet, signed center interface.
- `03_strategy1_reader.tex`: trace-cap register, complete master-deficit
  hypotheses, terminal routes.
- `04_strategy2_summary.tex`: exact endpoint and five-row certificates,
  center-free path conditions, T3 and Vd terminals.
- `05_strategy3_reader.tex`: local area-loss register and two cyclic sums.
- `06_strategy4_reader.tex`: direct witness forcing, Newton reduction, cap
  chain, and reference to the exact mixed-overlap certificate.
- `07_exhaustive_assembly.tex`: short audit of every routing row.

### 3.2 Technical appendices

After `\appendix`, use this order:

```text
appendix_roadmap.tex
02_structural_reductions.tex
02a_universal_calculus.tex
02b_admissible_set_derivation.tex
04a_signed_center_calculus.tex
03_strategy1_length.tex
04b_common_CE1_CE2_budgets.tex
04c_short_Vd_placements.tex
04_strategy2_reader.tex
04_strategy2_exact_demand.tex
04d_strategy2_rigor_completion.tex
04e_strategy2_placement_assembly.tex
05_strategy3_area.tex
06_strategy4_ab_core.tex
06a_strategy4_exact_certificate.tex
appendix_symbols.tex
```

`06_strategy4_ab_core.tex` owns its nested caliper and mixed-reduction inputs;
do not input those nested files separately from `main.tex`.

## 4. Required `main.tex` assembly

The active body/appendix assembly is:

```latex
\input{01_introduction}
\input{02_reader_framework}
\input{03_strategy1_reader}
\input{04_strategy2_summary}
\input{05_strategy3_reader}
\input{06_strategy4_reader}
\input{07_exhaustive_assembly}
\label{page:proof-body-end}

\clearpage
\appendix
\input{appendix_roadmap}
\input{02_structural_reductions}
\input{02a_universal_calculus}
\input{02b_admissible_set_derivation}
\input{04a_signed_center_calculus}
\input{03_strategy1_length}
\input{04b_common_CE1_CE2_budgets}
\input{04c_short_Vd_placements}
\input{04_strategy2_reader}
\input{04_strategy2_exact_demand}
\input{04d_strategy2_rigor_completion}
\input{04e_strategy2_placement_assembly}
\input{05_strategy3_area}
\input{06_strategy4_ab_core}
\input{06a_strategy4_exact_certificate}
\input{appendix_symbols}
```

Place `\raggedbottom` immediately after `\begin{document}`. Include a
bibliography only when verified external sources are cited.

## 5. Paper-wide notation

Whenever actual reaches and demands occur together:

- `(A_i,B_i,C_i)` are actual maximal reaches;
- `(a_i,b_i,c_i)` are selected lower demands.

The supercritical count is always

```text
N_+ = |{i : A_i+B_i>1}|.
```

Use:

- `CE0`, `CE1`, `CE2`;
- `Vd0`, `Vd1`, `Vd2`, `T3-like`;
- `H`, `O`, `V_i`, `e_{i,i+1}`, `r_i`, `M_i`;
- `gr` for active-gap rank;
- `mathcal A` for the local admissible set;
- `g_c` for the raw defect-coordinate outgoing map;
- `widehat g_c` for the nonsupercritical cap;
- `f^vee(a)=1-f(1-a)` for the complement dual;
- `mathcal R_J` and center-assisted subscripts for residual transfers;
- `g_c^{sc}` for the strict-supercritical outgoing envelope;
- `I` for identity relaxation;
- `[Phi_1|...|Phi_r]` for geometric row order, leftmost first;
- `Lambda`, `c_*`, `mathcal D_eta`, `Q_-,Q_0,Q_+`, `A,B,C` for Strategy 4.

Technical aliases `B_c,F_c,G_c` may remain in the exact-demand appendix.

## 6. Non-negotiable proof distinctions

1. **Actual versus selected criticality.** Never infer `N_+` from selected
   demands except through the strict-handoff theorem.
2. **Raw versus capped zero-radial map.** For `0<x<1`,
   `g_0(x)>x` but `widehat g_0(x)=x`.
3. **Outgoing versus following demand.** The bound
   `B<g_c^{sc}` is unconditional for a strict-supercritical row; the bound
   `A_next>1-g_c^{sc}` additionally requires a center-free edge.
4. **Path budgets.** Every internal path edge must have no center or
   nonincident positive-length trace. Endpoint external components must be
   included in the residual quantities.
5. **Singleton gaps.** A common endpoint of two open traces remains uncovered.
6. **Algebraic component selection.** Retain the selectors excluding fake
   high-radial components.
7. **CE1 and CE2 one-gap endings.** Preserve the CE1 affine/threshold argument
   and the CE2 at-least-one-threshold dichotomy.
8. **Exact terminal coordinates.** The exact five-row target is `Z>1-H`; the
   reversed three-map target is `>1-X`.
9. **T3-like audit.** Retain all four labels and the incorporated `407X`
   supplement.
10. **Nonadjacent Vd terminal.** Retain the Vd-specific own-radial margin.
11. **Vd1 replacement.** Retain the two ordered halves, strict margins, and
    explicit open axis replacements.
12. **Strategy 4.** Retain the exact ray order, adjacent overlaps, rational
    radial envelopes, Gram reduction, authenticated sparse data, and exact
    Bernstein verification.

## 7. Exact electronic supplements

### 7.1 T3 endpoint supplement

The complete `407X` files are part of the proof only through
`04d_strategy2_rigor_completion.tex`, which records their paths and blob
identifiers. A status-bearing final assembly and every terminal branch file
must be present.

### 7.2 Strategy 4 certificate

`06a_strategy4_exact_certificate.tex` must record:

- all six sparse-data shard blob SHAs;
- the core loader and both verifier blob SHAs;
- the canonical sparse transcript SHA-256 digest;
- the exact denominator nonvanishing argument;
- the mathematical implication from residual signs to cap overlap;
- the chart domains and Bernstein conversion formula;
- the fact that no floating-point or interval method is used.

A claimed `PASS` output alone is insufficient. The code and authenticated data
are the incorporated certificate; a later run is a reproducibility check.

## 8. Figures

Body figures should explain:

- center and vertex roles;
- perimeter and skeleton targets;
- the local demand hull;
- a transfer chain;
- local/global area loss;
- the Strategy 4 witness configuration.

A schematic caption must say when a figure is not to scale or is not itself an
inequality proof.

## 9. Build and verification

The canonical future build command is:

```bash
cd arrange/paper_draft
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

When compilation is authorized, verify:

1. successful XeLaTeX build;
2. no undefined references or duplicate labels;
3. no material overfull boxes;
4. `page:proof-body-end` on page 20 or earlier;
5. every figure and major table visually;
6. routing table against the proof-tree index;
7. exact certificate scripts in their package environment;
8. `main.pdf` corresponds to committed sources.

If compilation is not performed, do not update `main.pdf` and state that the
tracked PDF is stale. The current repair task explicitly follows that rule.

## 10. Repository hygiene

Keep temporary build outputs, logs, extracted PDFs, test harnesses, and local
font copies out of the repository. Commit only persistent manuscript sources,
figures, proof-package corrections, certificate data, and an actually rebuilt
final PDF when compilation is authorized.
