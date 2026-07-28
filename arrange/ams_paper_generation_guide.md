# AMS-Style Main-Theorem Paper Generation Guide

This file is an authoring specification, not a proof source.  It maintains the
AMS-style manuscript proving the theorem in
[`0000_main_theorem.md`](../proof/0XXX_main/0000_main_theorem.md).

The proof corpus is authoritative for hypotheses, theorem statements, and
status.  The manuscript may reorganize proved material, but it may not
strengthen a result, erase a strictness condition, confuse actual reaches with
selected demands, or treat a navigation file as a proof.

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

1. Use a mathematical result as established only when its source has a
   sufficient recorded status, normally `Status: Proven`, or is an exact
   definition from a `Status: Definition` source.
2. A `Reference` or index file supplies navigation only.  Follow its links to
   the numbered proof source.
3. A `Reduction` proves only its stated reduction.  It closes no branch unless
   every terminal dependency is independently proved.
4. Never promote `Strategy`, `Empirical`, `Experiment`, `Lemma target`,
   `Practically proven`, or `Failed` material into the paper proof.
5. Preserve every hypothesis involving open versus closed triangles, interior
   membership, strict inequalities, positive-length traces, midpoint coverage,
   CE type, vertex type, and the actual count `N_+`.
6. A plot, floating-point run, or script invocation is not a proof.  Exact
   finite certificates must appear as checkable identities, sign
   decompositions, or positive-basis expansions.
7. Record reusable mathematical simplifications in `proof/` before or together
   with their manuscript use.
8. Preserve the existing Strategy 1 routing, including the Strategy 1 half of
   the exceptional CE2 one-Vd1/Vd2 row.

## 2. Reader-body contract

The manuscript is split at `\appendix` into a proof body and technical
verification modules.

### 2.1. Page budget

The body, including title, abstract, contents, definitions, figures, and the
final theorem assembly, must end on or before page 20.  The contents must be
section-only:

```latex
\setcounter{tocdepth}{1}
\tableofcontents
```

This prevents the subsection-heavy technical appendices from consuming the
reader-body page budget.  `main.tex` places

```latex
\label{page:proof-body-end}
```

immediately before `\clearpage\appendix`.  After a complete build, inspect the
page attached to this label.  A source edit that moves the label beyond page 20
must be shortened before merge.

### 2.2. Material allowed in the body

The body should contain:

- definitions of every symbol used in the proof flow;
- the role and case classifications;
- geometric intuition and explanatory figures;
- exact calculation outputs, such as the explicit admissible-set description;
- named inequality or certificate propositions with complete hypotheses;
- short conceptual proofs, additive sums, monotone-chain logic, and the final
  exhaustive assembly.

The body should not contain:

- support-line case derivations;
- polynomial expansions or coefficient lists;
- root-selection calculations;
- derivative sign audits;
- rational parametrization calculations;
- Gram determinant reductions;
- Bernstein or other positive-basis coefficient tables;
- replay scripts or machine logs.

A reader must be able to follow why every routing row is impossible without
reading an appendix.  The appendix is for checking the displayed interfaces,
not for discovering the logical structure of the proof.

## 3. Active manuscript architecture

All persistent paper artifacts live under `arrange/paper_draft/`.

### 3.1. Reader-facing body

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

Their roles are:

- `01_introduction.tex`: theorem, forced roles, notation dictionary, complete
  routing table, all-Vd0 active-gap kernel, and the four-strategy diagram.
- `02_reader_framework.tex`: structural interface, local admissible set,
  explicit minimum-side description, canonical decorated `g`-family, relaxed
  composition rule, and signed CE1/CE2 interface.
- `03_strategy1_reader.tex`: perimeter and skeleton targets, the trace-cap
  register, the two master sums, and the exact list of Strategy 1 routes.
- `04_strategy2_summary.tex`: exact row-chain semantics, all-Vd0 kernel,
  endpoint/threshold/Vd certificate register, and Strategy 2 routes.
- `05_strategy3_reader.tex`: local area-loss register and the two cyclic sums.
- `06_strategy4_reader.tex`: direct disk and three-point forcing, Newton inner
  points, cyclic cap-chain lemma, four-overlap proposition, and enclosure
  contradiction.  Do not return polynomial or Bernstein calculations to this
  file.
- `07_exhaustive_assembly.tex`: one short audit of Table `tab:routing`.

### 3.2. Technical appendices

After `\appendix`, use this order:

```text
appendix_roadmap.tex
02_structural_reductions.tex
02a_universal_calculus.tex
04a_signed_center_calculus.tex
03_strategy1_length.tex
04b_common_CE1_CE2_budgets.tex
04c_short_Vd_placements.tex
04_strategy2_reader.tex
04_strategy2_exact_demand.tex
05_strategy3_area.tex
06_strategy4_ab_core.tex
appendix_symbols.tex
```

`appendix_roadmap.tex` explains the variable domains and the output verified by
each module.  Except for the finite geometric classification, the appendices
should pass as quickly as possible from geometry to inequalities on explicit
real-variable domains.

`06_strategy4_ab_core.tex` owns its nested certificate inputs.  Do not input
those nested files directly from `main.tex`.

The existing complete proof files are retained in the appendix so that the
paper remains proof-complete while the body stays short.  When shortening an
appendix, never remove the exact component selector, strict endpoint condition,
or domain restriction that makes a squared or rationalized inequality valid.

## 4. Required `main.tex` assembly

After `\maketitle`, use the section-only contents shown above.  The active
body/appendix assembly is:

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
\input{04a_signed_center_calculus}
\input{03_strategy1_length}
\input{04b_common_CE1_CE2_budgets}
\input{04c_short_Vd_placements}
\input{04_strategy2_reader}
\input{04_strategy2_exact_demand}
\input{05_strategy3_area}
\input{06_strategy4_ab_core}
\input{appendix_symbols}
```

Place `\raggedbottom` immediately after `\begin{document}`.  A bibliography is
included only when verified external sources are actually cited.

## 5. Paper-wide notation

Use the following distinction whenever actual reaches and demands occur
together:

- `(A_i,B_i,C_i)` are actual maximal reaches of an original open role;
- `(a_i,b_i,c_i)` are selected or prescribed lower demands.

The supercritical count is always computed from actual reaches:

```text
N_+ = |{ i : A_i+B_i>1 }|.
```

Use these canonical names:

- `CE0`, `CE1`, `CE2`;
- `Vd0`, `Vd1`, `Vd2`, `T3-like`;
- `H`, `O`, `V_i`, `e_{i,i+1}`, `r_i`, `M_i`;
- `gr` for active-gap rank; never use bare `g` for this count;
- `mathcal A` for the local admissible set;
- `g_c` for the raw defect-coordinate outgoing map;
- `widehat g_c` for its nonsupercritical cap;
- `f^vee(a)=1-f(1-a)` for the incoming-reach dual;
- center-assisted subscripts for residual maps;
- `g_c^{sc}` for the free strict-supercritical envelope;
- `I` for the identity relaxation;
- `[Phi_1|...|Phi_r]` for maps listed in geometric row order, with the
  leftmost slot acting first;
- `Lambda`, `c_*`, `mathcal D_eta`, `Q_-,Q_0,Q_+`, and `A,B,C` for Strategy 4.

Technical aliases `B_c,F_c,G_c` may remain in the exact-demand appendix when
they shorten contact-cell algebra, but the body uses the canonical decorated
`g` notation.

## 6. Non-negotiable proof distinctions

The following distinctions must survive every shortening pass.

1. **Actual versus selected criticality.**  `N_+` is never inferred from a
   selected demand pair unless the strict-handoff theorem explicitly licenses
   the inference.
2. **Raw versus capped zero-radial map.**  For `0<x<1`, the raw map has
   `g_0(x)>x`, while the hatted nonsupercritical map satisfies
   `widehat g_0(x)=x`.
3. **Singleton gaps.**  Equality of adjacent open-trace endpoints still leaves
   an uncovered point.
4. **Selected algebraic component.**  Squared contact equations must retain the
   selector excluding the fake high-radial component.
5. **CE1 and CE2 one-gap endings.**  The common five-row geometry does not
   authorize replacing the CE1 affine/threshold calculation or the CE2
   two-threshold dichotomy by a stronger unproved symmetric statement.
6. **T3-like endpoint audit.**  Retain its exact four-label endpoint theorem;
   do not replace it by an unsupported universal envelope.
7. **Nonadjacent Vd terminal.**  Retain the Vd-specific radial margin.
8. **Hybrid CE2 row.**  Strategy 1 closes only its stated neighboring-midpoint
   placement; Strategy 2 closes the complementary placements.
9. **Strategy 4.**  The body may cite the four-overlap proposition, but the
   appendix must retain the exact ray order, Gram reductions, and positive
   Bernstein identities proving the mixed overlaps.

## 7. Figures

Figures in the body must explain the proof architecture, not merely decorate
it.  At minimum retain:

- the center and vertex roles;
- the perimeter/skeleton targets;
- the local demand hull `(a,b,c)`;
- one transfer-chain diagram;
- the local/global area-loss picture;
- the Strategy 4 witness configuration.

A schematic caption must say when the drawing is not to scale or is not itself
an inequality proof.

## 8. Build and verification

Run from `arrange/paper_draft/`:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

A complete verification pass requires:

1. successful XeLaTeX build;
2. no undefined references;
3. no duplicate labels;
4. no overfull boxes requiring manuscript repair;
5. `page:proof-body-end` on page 20 or earlier;
6. visual inspection of every figure and major table;
7. a check that all files after `\appendix` are genuine verification material;
8. comparison of the final routing table against the proof-tree index;
9. confirmation that `main.pdf` corresponds to the committed sources.

If the environment cannot perform the complete build, do not update
`main.pdf`, and state that limitation in the commit report and source ledger.
A source-only commit must never describe the tracked PDF as current.

## 9. Repository hygiene

Keep temporary build outputs, logs, extracted PDFs, test harnesses, and local
font copies out of the repository.  Commit only persistent manuscript sources,
figures, exact certificate data, and an actually rebuilt final PDF.
