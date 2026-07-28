# AMS-Style Main-Theorem Paper Generation Guide

This file is an authoring specification, not a proof source.  It maintains the
modular AMS-style manuscript proving
[`0000_main_theorem.md`](../proof/0XXX_main/0000_main_theorem.md).

The paper retains four named strategies:

1. direct length-sum obstructions;
2. relaxations of $g$-composition chains;
3. normalized area loss;
4. the center-independent direct nine-point obstruction.

The proof corpus is authoritative for hypotheses, theorem statements, and
status.  The manuscript may reorganize proved material but may not strengthen
it, suppress strictness, or promote an empirical or failed source.

## 1. Required reading and status rules

Before changing the paper, read:

- `README.md`;
- `proof/0XXX_main/0000_main_theorem.md`;
- `proof/0XXX_main/0001_proof_tree_index.md`;
- `proof/0XXX_main/0002_status_and_dependencies.md`;
- `proof/09XX_appendices/0910_notation_dictionary.md`;
- `proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md`;
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md`;
- `arrange/paper_draft/source_ledger.md`.

Apply these rules.

1. Use a result as established only when its source has a sufficient recorded
   status.
2. A `Reference` file supplies navigation, not a proof.
3. A `Reduction` closes no branch unless every terminal dependency is proved.
4. Never promote `Strategy`, `Empirical`, `Experiment`, `Lemma target`, or
   `Failed` material.
5. Preserve all open/closed, strict/weak, midpoint, center-class, vertex-type,
   and $N_+$ hypotheses.
6. Numerical or graphical output is not a proof unless an independently
   checkable exact certificate is recorded.
7. Record every reusable mathematical simplification in `proof/` before or
   together with its manuscript use.
8. Preserve every present Strategy 1 route, including `4040`, `4041`, `4110`,
   `4111`, `4123`, `4149`, `414a`, and `4200`.

## 2. Active manuscript layout

```text
arrange/paper_draft/
|-- main.tex
|-- 01_introduction.tex
|-- 02_structural_reductions.tex
|-- 02a_universal_calculus.tex
|-- 04a_signed_center_calculus.tex
|-- 03_strategy1_length.tex
|-- 04b_common_CE1_CE2_budgets.tex
|-- 04_strategy2_reader.tex
|-- 05_strategy3_area.tex
|-- 06_strategy4_reader.tex
|-- 07_exhaustive_assembly.tex
|-- 04c_short_Vd_placements.tex
|-- 04_strategy2_exact_demand.tex
|-- 06_strategy4_ab_core.tex
|-- appendix_certificates.tex
|-- appendix_exact_mixed_overlap.tex
|-- appendix_symbols.tex
|-- source_ledger.md
|-- fonts/
|-- figures/
`-- main.pdf
```

The conceptual transfer calculus precedes the signed center calculus so that
every later chain uses established notation.

### Reader-facing body

- `01_introduction.tex`: theorem, dictionary, routing table, active-gap kernel,
  and strategy overview.
- `02_structural_reductions.tex`: exhaustive structural reduction.
- `02a_universal_calculus.tex`: enclosure gauge and the canonical decorated
  $g$-family.
- `04a_signed_center_calculus.tex`: signed CE1/CE2 model and exact one-gap row
  interface.
- `03_strategy1_length.tex`: complete trace budgets.
- `04b_common_CE1_CE2_budgets.tex`: common perimeter and short-role budgets.
- `04_strategy2_reader.tex`: one table of all Strategy 2 chains and their
  relaxations.
- `05_strategy3_area.tex`: complete area-loss proof.
- `06_strategy4_reader.tex`: direct witnesses, Newton points, cap chain,
  overlap proposition, and enclosure.
- `07_exhaustive_assembly.tex`: final routing audit.

### Technical appendices

After `\appendix`, input:

- `04c_short_Vd_placements.tex`;
- `04_strategy2_exact_demand.tex`;
- `06_strategy4_ab_core.tex`;
- `appendix_symbols.tex`.

`06_strategy4_ab_core.tex` owns the nested certificate inputs.  The exact
Strategy 2 appendix may retain the technical aliases $B_c,F_c,G_c$, and the
short Vd appendix may retain $A_{\rm sc},B_{\rm sc}$ only when their alias
status is explicit.

## 3. Required `main.tex` assembly

The minimum preamble is

```latex
\documentclass{amsart}
\usepackage{amsmath,amssymb,amsthm,mathtools,graphicx}
\usepackage{fontspec}
\usepackage{booktabs,float,microtype,tikz}
\usetikzlibrary{arrows.meta,calc,positioning}
\input{figures/tikz_setup}
```

Do not load `mathrsfs`; the branch-signature symbol $\mathscr C$ is no longer
used.  The body order is

```latex
\input{01_introduction}
\input{02_structural_reductions}
\input{02a_universal_calculus}
\input{04a_signed_center_calculus}
\input{03_strategy1_length}
\input{04b_common_CE1_CE2_budgets}
\input{04_strategy2_reader}
\input{05_strategy3_area}
\input{06_strategy4_reader}
\input{07_exhaustive_assembly}

\appendix
\input{04c_short_Vd_placements}
\input{04_strategy2_exact_demand}
\input{06_strategy4_ab_core}
\input{appendix_symbols}
```

Do not input the nested Strategy 4 certificate files directly.

## 4. Paper-wide notation

Use

- $(A_i,B_i,C_i)$ for actual maximal reaches;
- $(a_i,b_i,c_i)$ for selected lower-bound demands;
- $\mathrm{gr}$ for active-gap rank;
- bare $g$ only for transfer maps.

The actual supercritical count is

$$
N_+=
\left\lvert\left\{i:A_i+B_i>1\right\}\right\rvert.
$$

### Canonical transfer notation

For incoming defect $x=1-a$ and radial demand $c$, define

$$
g_c(x)=\max\{y:(1-x,y,c)\in\mathcal A\}.
$$

The nonsupercritical cap is

$$
\widehat g_c(x)=\min\{g_c(x),x\}.
$$

For any map $f$, define

$$
f^\vee(a)=1-f(1-a).
$$

Therefore

- $g_c^\vee$: raw incoming-reach lower transfer;
- $\widehat g_c^\vee$: nonsupercritical extensive transfer;
- $g_{c,J}^\vee$, $\widehat g_{c,J}^\vee$: center-assisted variants;
- $g_c^{\rm sc}$: free strict-supercritical outgoing envelope;
- $1-g_c^{\rm sc}$: complementary next-incoming threshold;
- $\widehat g_{1-d}^{\vee,\lambda}$: affine selected-$T_+$ lower
  relaxation;
- $\widehat g_{1-d}^{\vee,\rm th}$: threshold lower relaxation.

At zero radial demand,

$$
g_0(x)>x\quad(0<x<1),
\qquad
\widehat g_0(x)=x.
$$

The identity belongs to the hatted map.

The technical aliases are

$$
B_c(a)=g_c(1-a),
\qquad
F_c(a)=\widehat g_c(1-a),
\qquad
G_c(a)=\widehat g_c^\vee(a),
$$

$$
B_{\rm sc}(c)=g_c^{\rm sc},
\qquad
A_{\rm sc}(c)=1-g_c^{\rm sc}.
$$

Use them only when they shorten exact algebra.  Do not reintroduce separate
permanent letters for affine or threshold relaxations.

## 5. Strategy 2 authoring requirements

### 5.1. Actual-row interface

For an actual row with

$$
A_i\ge a,
\qquad
C_i\ge c,
$$

the raw outgoing bound is

$$
B_i\le g_c(1-a).
$$

A center-free handoff gives

$$
A_{i+1}\ge g_c^\vee(a).
$$

If the row is nonsupercritical, then

$$
B_i\le\widehat g_c(1-a),
$$

and

$$
A_{i+1}\ge\widehat g_c^\vee(a)\ge a.
$$

With a center interval $J$, use the subscripted maps
$g_{c,J}^\vee$ and $\widehat g_{c,J}^\vee$.  Every formal composition must be
connected to the actual rows realizing these inequalities.  Singleton gaps
remain included.

### 5.2. Composition notation

For maps listed in geometric row order,

$$
[\Phi_1\mid\cdots\mid\Phi_r](x)
=(\Phi_r\circ\cdots\circ\Phi_1)(x).
$$

The Strategy 2 master table must list separately:

1. branch and seed data;
2. exact chain skeleton;
3. relaxed slots;
4. terminal capacity or separation inequality.

Do not use a separate branch-signature operator.

### 5.3. All-Vd0 kernel

Use $N_+\in\{0,1\}$ and $\mathrm{gr}\in\{0,1,2\}$.

- $N_+=0$, $\mathrm{gr}=0$: strict cyclic identity relaxation.
- $N_+=0$, $\mathrm{gr}=1$: two exact hatted endpoint caps and interior
  $\mathrm I^3$.
- either $\mathrm{gr}=2$ cell: paired exact endpoint caps and interior
  $\mathrm I^3$.
- $N_+=1$, $\mathrm{gr}=1$: one exact five-row $\widehat g^\vee$ chain, then
  CE1 or CE2 decorated relaxations.
- $N_+=1$, $\mathrm{gr}=0$: retain Strategy 4.

### 5.4. CE1 one-gap clause

The common exact target is

$$
[\widehat g_{1-\alpha}^\vee
 \mid\widehat g_{1-m}^\vee
 \mid\widehat g_{1-\delta}^\vee](H)>1-X.
$$

On the hard selected branch use

$$
[\widehat g_{1-\alpha}^{\vee,1-4\alpha}
 \mid\widehat g_{1-m}^{\vee,1-5m}
 \mid\widehat g_{1-\delta}^{\vee,\rm th}](H)>1-X.
$$

Retain the shortened exact terminal estimate in `4106`.  Do not restore the
superseded high-degree endpoint polynomials.

### 5.5. CE2 one-gap clause

Retain the two-threshold dichotomy exactly.  One threshold-decorated slot is
decisive and every other slot is replaced by $\mathrm I$.  Do not replace the
dichotomy by an unsupported symmetric strengthening.

### 5.6. T3-like endpoint package

The three interior rows are identity relaxations, but the hard endpoint sum
remains the exact four-label audit in `407X`.  Preserve its selected high-sheet,
center-transfer, and analytic threshold estimates.

### 5.7. Supercritical rescuer chain

The T3-like and adjacent Vd1 profiles both prove

$$
a\le1-g_c^{\rm sc},
\qquad
\frac{a}{a+1-u}\le1-g_c^{\rm sc}.
$$

The common chain is

$$
A_2>1-g_c^{\rm sc}
\quad\xrightarrow{\ \mathrm I^3\ }\quad
A_5>1-g_c^{\rm sc},
$$

followed by

$$
b_5<g_c^{\rm sc}\le h.
$$

### 5.8. Vd terminal placements

- `4144`: exact residuals, backward identity chain, and
  $$
  \widehat g_{1-\delta}^\vee(1/2+A)>1-H.
  $$
- `4146`: retain the Vd-specific terminal radial margin; do not call it a
  universal $\widehat g_c^\vee$ inequality.
- `4147`: axis replacement is geometric preprocessing, followed by the
  appropriate all-Vd0 chain.
- `4149` and `414a`: remain Strategy 1.

## 6. Strategy 4 requirements

The reader-facing proof contains:

1. direct forcing of the disk and $Q_-,Q_0,Q_+$;
2. Newton inner points;
3. the cyclic cap-chain lemma;
4. the four-overlap proposition;
5. enclosure and the open-triangle contradiction.

The technical appendix retains every exact sign, radial envelope, Gram
factorization, polynomial, Bernstein identity, and replay record.  The optional
disk-plus-point lemma remains excluded unless it replaces a complete part of
the proof.

## 7. Final assembly

`07_exhaustive_assembly.tex` must cite:

- `prop:length-branches`;
- `prop:reader-demand-branches`;
- `prop:area-branches`;
- `prop:reader-ab-core-branches`;
- `tab:strategy2-chain-signatures` when describing the transfer rows.

Audit every routing-table row.  In the hybrid $1+2$ row, preserve the present
complementary Strategy 1 and Strategy 2 placements.

## 8. Source ledger and verification

After accepted changes, update `source_ledger.md` with:

- authoritative proof source and status;
- manuscript label and placement;
- exact versus reader-facing notation;
- whether a script is a proof dependency or a cross-check.

Build with

```text
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Check:

1. undefined references and duplicate labels;
2. missing inputs, graphics, and fonts;
3. overfull boxes, especially the Strategy 2 table;
4. that all exact technical sections occur after `\appendix`;
5. that the final assembly cites only proved terminal propositions;
6. exact replay tools whenever certificate sources change.

If the full build is unavailable, do not claim that `main.pdf` is current.
Report precisely which isolated checks were performed.

## 9. Repository hygiene

Follow `AGENTS.md`.

- Keep changes grouped by mathematical purpose.
- Update indexes, status tables, and the source ledger when notation or
  dependencies change.
- Preserve failed-route records.
- Do not delete complete technical proofs after introducing a concise body
  statement.
- Do not alter a complete branch merely to pursue an unproved simplification.
