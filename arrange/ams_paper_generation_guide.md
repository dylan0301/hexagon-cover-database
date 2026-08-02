# AMS-Style Main-Theorem Paper Generation Guide

This is an authoring specification, not a proof source. The numbered proof
package is authoritative for hypotheses, theorem statements, and status. The
paper may reorganize proved material, but it may not strengthen a result,
erase a strictness condition, confuse actual reaches with selected demands, or
treat a navigation file as a proof.

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

Apply these rules.

1. Use a result as established only when its numbered source has sufficient
   status, normally `Status: Proven`, or is an exact definition.
2. A `Reference` or index file supplies navigation only.
3. A `Reduction` closes no branch without proved terminal dependencies.
4. Never promote `Strategy`, `Empirical`, `Experiment`, `Lemma target`,
   `Practically proven`, or `Failed` material into the proof.
5. Preserve every open/closed, interior, strictness, positive-trace, midpoint,
   center-type, vertex-type, and actual-`N_+` hypothesis.
6. A plot or floating-point computation is not a proof.
7. An exact computer-assisted certificate is allowed only when its mathematical
   reduction, exact arithmetic model, complete input, authentication data, and
   verifier are formally incorporated.
8. Record reusable mathematical corrections in `proof/` as well as the paper.
9. Preserve all existing Strategy 1 assignments.

## 2. Proof layers and body policy

The complete proof consists of:

1. the reader-facing body;
2. the TeX verification appendices;
3. the exact electronic supplements formally incorporated by path, Git blob,
   and transcript digest.

The body should make the whole contradiction understandable but is not
independently responsible for every long calculation.

There is no fixed page cap for the reader-facing body.  Definitions and
hexagon-skeleton figures should remain in the body when they materially clarify
the proof interface; long algebraic verification remains in the appendices.
Use

```latex
\setcounter{tocdepth}{1}
\tableofcontents
```

and place

```latex
\label{page:proof-body-end}
```

immediately before `\clearpage\appendix`.  A complete build must still verify
that the label occurs immediately before the appendix transition.

The body may contain definitions, role classifications, figures, exact
calculation outputs, fully stated terminal propositions, short conceptual
arguments, and final routing. It should not contain large support-line case
calculations, polynomial expansions, root-selection audits, derivative tables,
Gram reductions, Bernstein data, code listings, or run logs.

## 3. Active manuscript architecture

### 3.1 Reader-facing body

```text
01_introduction.tex
02_reader_framework.tex
02c_strategy2_skeleton_atlas.tex
03_strategy1_reader.tex
04_strategy2_summary.tex
05_strategy3_reader.tex
06_strategy4_reader.tex
07_exhaustive_assembly.tex
```

- `01_introduction.tex`: theorem, roles, notation, routing table, proof flow.
- `02_reader_framework.tex`: structural interface, explicit admissible set,
  corrected transfer alphabet, signed center interface.
- `02c_strategy2_skeleton_atlas.tex`: modular full-skeleton figures for every
  transfer and signed-center definition.
- `03_strategy1_reader.tex`: trace register, complete master-deficit
  hypotheses, Strategy 1 routes.
- `04_strategy2_summary.tex`: exact endpoint and five-V-triangle certificates,
  center-free path conditions, T3-like and Vd terminals.
- `05_strategy3_reader.tex`: local area losses and cyclic sums.
- `06_strategy4_reader.tex`: direct forcing, Newton reduction, cap chain, and
  the exact mixed-overlap certificate interface.
- `07_exhaustive_assembly.tex`: exhaustive audit of every routing entry.

### 3.2 Technical appendices

Use this order after `\appendix`:

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
04_strategy2_verification.tex
04_strategy2_verification.tex
04_strategy2_verification.tex
04_strategy2_verification.tex
05_strategy3_area.tex
06_strategy4_ab_core.tex
06a_strategy4_exact_certificate.tex
appendix_symbols.tex
```

The roles of the added verification files are:

- `02b`: complete support derivation, polynomial cells, selectors, radial
  envelope;
- `04d`: formally incorporated complete `407X` branch audit and full Vd1 axis
  replacement;
- `04e`: authoritative CE2 exactly-one-Vd1/Vd2 placement assembly;
- `04f`: declares the later complete Strategy 2 propositions authoritative for
  the earlier compact summary statements;
- `06a`: exact mixed-overlap reduction, certificate manifest, positive-basis
  verification, and residual-to-cap geometry.

`06_strategy4_ab_core.tex` owns its nested caliper and preliminary mixed
reduction inputs. Do not input those nested files separately from `main.tex`.

## 4. Required `main.tex` assembly

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
\input{04f_strategy2_cross_reference_closure}
\input{05_strategy3_area}
\input{06_strategy4_ab_core}
\input{06a_strategy4_exact_certificate}
\input{appendix_symbols}
```

Place `\raggedbottom` after `\begin{document}`. Include a bibliography only for
verified external citations.

## 5. Paper-wide notation

Whenever both occur:

- `(A_i,B_i,C_i)` are actual maximal reaches;
- `(a_i,b_i,c_i)` are selected lower demands.

Always compute

```text
N_+ = |{i : A_i+B_i>1}|.
```

Canonical names are:

- `CE0`, `CE1`, `CE2`;
- `Vd0`, `Vd1`, `Vd2`, `T3-like`;
- `H`, `O`, `V_i`, `e_{i,i+1}`, `r_i`, `M_i`;
- `gr` for active-gap rank;
- `mathcal A` for the local admissible set;
- `g_c`, `widehat g_c`, `f^vee`, and `mathcal R_J` for transfers;
- `d_i^C` for a center exit and `c_i^C=1-d_i^C` for its complementary
  vertex-side demand; lowercase `c_i` remains a selected V triangle demand;
- `m_3=d_3^C` for the local CE1 affine-slot scalar; bare `m` remains the
  paper-wide count of non-Vd0 roles;
- `mathcal I_R,mathcal I_L` for geometric center traces and `I_R,I_L` for
  their scalar parameter intervals in residual calculations;
- `g_c^{sc}` for the strict-supercritical outgoing envelope;
- `I` for the identity relaxation;
- `[Phi_1|...|Phi_r]` for geometric V-triangle order, leftmost first;
- `Lambda`, `c_*`, `mathcal D_eta`, `Q_-,Q_0,Q_+`, and `A,B,C` for Strategy 4.

Technical aliases `B_c,F_c,G_c` may remain in exact-demand calculations.

## 6. Non-negotiable proof distinctions

1. **Actual versus selected criticality.** Never infer `N_+` from selected
   demands except through strict-handoff selection.
2. **Raw versus capped zero-radial map.** `g_0(x)>x`, while
   `widehat g_0(x)=x` for `0<x<1`.
3. **Outgoing versus following demand.** `B<g_c^{sc}` is unconditional for a
   strict-supercritical V triangle; `A_next>1-g_c^{sc}` additionally requires a
   center-free outgoing edge.
4. **Path budgets.** Every internal path edge must exclude center and
   nonincident positive-length traces. Endpoint external components must be
   included in the residuals.
5. **Singleton gaps.** A common endpoint of two open traces remains uncovered.
6. **Algebraic component selection.** Keep selectors excluding fake high
   components.
7. **One-gap endings.** Keep the CE1 affine/threshold argument and the CE2
   at-least-one-threshold dichotomy.
8. **Terminal coordinates.** The exact five-V-triangle target is `Z>1-H`; the dual
   three-map target is `>1-X`.
9. **T3-like audit.** Keep all four labels and the incorporated `407X`
   supplement.
10. **Vd terminals.** Keep the nonadjacent own-radial margin and the adjacent
    direct quarter separation; do not substitute an unsupported universal map.
11. **Vd1 replacement.** Keep both ordered halves, all strict margins, and the
    explicit open two-chart replacements.
12. **Strategy 4.** Keep ray order, adjacent overlaps, rational radial
    envelopes, Gram reduction, authenticated sparse data, and exact Bernstein
    verification.

## 7. Exact electronic supplements

### 7.1 T3-like endpoint supplement

`04_strategy2_verification.tex` records the complete `407X` source paths,
full blob identifiers, and exhaustive branch table. The difficult polynomial
selectors and high-sheet inequalities remain in those exact proof-package
objects and are not replaced by a partial TeX derivation. A status-bearing
final assembly and every terminal branch object must remain present.

### 7.2 Strategy 4 certificate

`06a_strategy4_exact_certificate.tex` must record:

- all six sparse-data shard blob SHAs;
- the loader and both verifier blob SHAs;
- the canonical transcript SHA-256 digest;
- denominator nonvanishing;
- the residual-to-cap-intersection implication;
- chart domains and the Bernstein conversion formula;
- the exact arithmetic model and absence of interval/floating computation.

A claimed `PASS` output alone is insufficient. The incorporated exact code and
authenticated data are the certificate; executing them is a reproducibility
check.

## 8. Figures

The body should retain figures for the role geometry, perimeter/skeleton
targets, local demand hull, transfer chain, area loss, and Strategy 4 witness.
The modular Strategy 2 notation atlas belongs directly after the transfer and
signed-center definitions in the body.  Every Strategy 2 notation panel should
use the full hexagon skeleton as its geometric frame and remain in an
independent TikZ source so that panels can be removed separately.
A schematic caption must state when a figure is not to scale or is not itself
an inequality proof.

## 9. Build and verification

When compilation is authorized, run

```bash
cd arrange/paper_draft
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

and verify:

1. successful XeLaTeX build;
2. no undefined references or duplicate labels;
3. no material overfull boxes;
4. `page:proof-body-end` immediately before the appendix transition;
5. all figures and major tables visually;
6. routing table against the proof-tree index;
7. both exact certificate scripts in their package environment;
8. `main.pdf` corresponds to committed sources.

When compilation is not performed, do not update `main.pdf` and state that the
tracked PDF is stale. This repair task follows that rule.

## 10. Repository hygiene

Keep temporary build outputs, logs, extracted PDFs, test harnesses, and local
font copies out of the repository. Commit only persistent manuscript sources,
figures, proof-package corrections, exact certificate data, and an actually
rebuilt final PDF when compilation is authorized.
