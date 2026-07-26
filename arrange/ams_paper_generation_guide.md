# AMS-Style Main-Theorem Paper Generation Guide

This file is an authoring specification. It is not a proof source. Its purpose
is to maintain the modular AMS-style paper proving the theorem in
[`0000_main_theorem.md`](../proof/0XXX_main/0000_main_theorem.md).

The paper is organized by four proof strategies rather than by the
repository's CE-first proof tree:

1. direct length-sum obstructions;
2. exact boundary--radial demand propagation;
3. normalized area loss;
4. the center-independent direct nine-point obstruction.

The proof corpus remains authoritative for theorem statements, hypotheses,
and status. The manuscript may reorganize and simplify that material, but it
must not strengthen a result, suppress a strictness condition, or treat a
navigation file as a proof.

## 1. Source And Status Rules

Before editing the paper, read:

- [`README.md`](../README.md);
- [`0000_main_theorem.md`](../proof/0XXX_main/0000_main_theorem.md);
- [`0001_proof_tree_index.md`](../proof/0XXX_main/0001_proof_tree_index.md);
- [`0002_status_and_dependencies.md`](../proof/0XXX_main/0002_status_and_dependencies.md);
- [`0910_notation_dictionary.md`](../proof/09XX_appendices/0910_notation_dictionary.md);
- [`1006_proof_status_conventions.md`](../proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md);
- `arrange/paper_draft/source_ledger.md`.

Apply the following rules.

1. Use a mathematical result as established only when its source says
   `Status: Proven`, or when it is an exact definition from a source saying
   `Status: Definition`.
2. A `Reference` or index file supplies navigation only. Follow its links to
   the numbered proof sources.
3. A `Reduction` proves only its stated reduction. It closes no branch unless
   every terminal dependency is independently proved.
4. Never promote `Practically proven`, `Lemma target`, `Strategy`,
   `Empirical`, `Experiment`, or `Failed` material into the proof.
5. Exact finite certificates and positive-basis identities must be presented
   as independently checkable mathematical arguments. A plot, floating-point
   run, or script invocation alone is not a proof.
6. Preserve every hypothesis involving open versus closed triangles,
   interior membership, strict inequalities, positive-length traces,
   midpoint coverage, CE type, vertex type, and $N_+$.
7. Repository paths belong in the private source ledger, not as substitutes
   for mathematical statements in the reader-facing paper.
8. When a reusable simplification is proved, record it in `proof/` before or
   together with its manuscript use.

## 2. Current Manuscript Architecture

All persistent paper artifacts live under `arrange/paper_draft/`.
The active source layout is:

```text
arrange/paper_draft/
|-- main.tex
|-- 01_introduction.tex
|-- 02_structural_reductions.tex
|-- 04a_signed_center_calculus.tex
|-- 02a_universal_calculus.tex
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

The introduction is the single proof guide.  Structural reduction and the
common signed center calculus precede the four mechanism sections.  Complete
exact Strategy 2 and Strategy 4 calculations remain technical appendices
after the final theorem assembly.

### 2.1. Body files

- `01_introduction.tex` states the theorem, definitions, routing table, and
  compact proof architecture.
- `02_structural_reductions.tex` proves the exhaustive role and case
  reductions.
- `04a_signed_center_calculus.tex` proves the common signed CE1/CE2 model and
  defines the local propagation interface in the body.
- `02a_universal_calculus.tex` proves the enclosure gauge, universal radical,
  interval residuals, boundary-path budget, selected-$T_+$ curve, and
  threshold routing once for all later strategies.
- `03_strategy1_length.tex` contains the complete length arguments.
- `04_strategy2_reader.tex` contains the all-Vd0 gap-rank kernel, one common
  CE2 two-gap application, the two sign-dependent one-gap clauses, and
  reader-facing branch assembly.
- `05_strategy3_area.tex` contains the complete area-loss arguments.
- `06_strategy4_reader.tex` contains only direct witness forcing, Newton
  inner points, the cyclic cap-chain lemma, the four-overlap proposition, and
  the enclosure conclusion.
- `07_exhaustive_assembly.tex` closes every row of the routing table using the
  reader-facing terminal propositions.

### 2.2. Technical appendices

After `\appendix`, input:

- `04c_short_Vd_placements.tex`: the quarter radial envelope, rational
  T3-like and Vd1 profiles, common adjacent rescuer, and shortened Vd
  placements;
- `04_strategy2_exact_demand.tex`: the proof-complete exact admissible-set
  catalogue, full terminal inequalities, and complete Strategy 2 branch audit;
- `06_strategy4_ab_core.tex`: the proof-complete strict $AB$ frontier,
  fixed-line signs, Newton reduction, ray order, and four cap overlaps;
- `appendix_symbols.tex`;
  the replay record is folded into `appendix_exact_mixed_overlap.tex`.

`06_strategy4_ab_core.tex` owns the nested inputs
`appendix_certificates.tex` and `appendix_exact_mixed_overlap.tex`. Since its
own section is after `\appendix`, the caliper theorem, polynomial expansions,
and Bernstein identities are now genuine appendix material.

The body may cite a precisely stated proved appendix lemma or proposition.
The appendix must still contain the full mathematical proof, not merely a
script command or a table of output.

## 3. Required `main.tex` Assembly

The minimum preamble is:

```latex
\documentclass{amsart}
\usepackage{amsmath,amssymb,amsthm,mathtools,graphicx}
\usepackage{fontspec}
\usepackage{booktabs,float,microtype,tikz}
\usetikzlibrary{arrows.meta,calc,positioning}
\input{figures/tikz_setup}

\newfontfamily\hangulA[Path=fonts/]{noto_sans_kr_subset_115.ttf}
\newfontfamily\hangulB[Path=fonts/]{noto_sans_kr_subset_118.ttf}
\newcommand{\straddlinghangul}{{\hangulA 걸}{\hangulB 거치는}}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
```

Place `\raggedbottom` immediately after `\begin{document}`. The required
assembly order is:

```latex
\input{01_introduction}
\input{02_structural_reductions}
\input{04a_signed_center_calculus}
\input{02a_universal_calculus}
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

Do not input `appendix_certificates.tex` or
`appendix_exact_mixed_overlap.tex` directly from `main.tex`; their owning
sources control their placement.  The historical half-edge $1/3$ envelope
has no standalone manuscript source and is not an active dependency.

A bibliography is included only when verified external sources are actually
cited. No bibliography is required for the present proof.

## 4. Paper-Wide Notation

Use the following distinction whenever actual reaches and demands occur
together:

- $(A_i,B_i,C_i)$: actual maximal reaches of an original open vertex role;
- $(a_i,b_i,c_i)$: selected or prescribed lower-bound demands.

The condition defining $N_+$ concerns the actual boundary reaches:

$$
N_+=
\left\lvert
\left\lbrace i:A_i+B_i>1\right\rbrace
\right\rvert.
$$

A local section may temporarily use lowercase variables for actual reaches
only if it announces that convention and never mixes the two meanings.

Use these established names consistently:

- CE0, CE1, CE2;
- Vd0, Vd1, Vd2, T3-like;
- $H$, $H_L$, $O$, $V_i$, $e_{i,i+1}$, $r_i$, $M_i$;
- $B_c$, $F_c$, $G_c$ for the Strategy 2 demand maps;
- $c_*$, $\mathcal D_\eta$, $Q_-,Q_0,Q_+$, $A,B,C$, and
  $\Lambda$ for Strategy 4.

Preserve the Korean term `걸거치는` through the existing Hangul macro where
it names the recurring crossing configuration.

## 5. Strategy 2 Authoring Requirements

### 5.1. Actual-row interface

Every formal map transition must be connected to an actual row. If an actual
nonsupercritical role satisfies

$$
A_i\ge z,
\qquad
C_i\ge c_i,
\qquad
A_i+B_i\le1,
$$

then the proof-safe capped map gives

$$
B_i\le F_{c_i}(z).
$$

A boundary handoff then gives

$$
A_{i+1}\ge1-B_i\ge G_{c_i}(z).
$$

Do not write a formal composition without identifying the actual rows that
realize these inequalities. Singleton gaps must remain included.

### 5.2. Interval residuals and boundary paths

Use $\mathcal R_J(p)$ for the far-side demand after an initial trace and
a center interval.  The generalized transfer is
$\mathcal G_{c,J}=\mathcal R_J\mathbin{\circ}F_c$, and
$\mathcal G_{c,\varnothing}=G_c$.  Use the boundary-path lemma instead of
repeating three-row or four-row terminal sums.

The all-Vd0 CE1/CE2 proof is organized by $N_+\in\{0,1\}$ and the
active-gap rank $g\in\{0,1,2\}$; the paired endpoint theorem has one
common geometric application in the two $g=2$ cells.

### 5.3. Universal selected-$T_+$ curve

The authoritative reusable source is
[`2016_universal_Tplus_normal_form.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2016_universal_Tplus_normal_form.md).
For deficit $d$, input $p$, output $q=G_{1-d}(p)$, increment
$\nu=q-p$, and normalized output $x=(q-d)/(1-d)$, the exact selected equation
reduces to

$$
x(1-x)=\nu(2-\nu).
$$

Hence

$$
\nu=\psi(x)=1-\sqrt{1-x+x^2},
$$

$$
q=d+(1-d)x,
\qquad
p=d+(1-d)x-\psi(x).
$$

Use

$$
\psi''(x)=-\frac{3}{4(1-x+x^2)^{3/2}}<0
$$

to prove strict concavity once. Do not repeat the old implicit
branch-specific differentiation.

The optional rational parameter is

$$
x=\frac{1-2z}{1-z^2},
\qquad
\psi(x)=\frac{z(1-2z)}{1-z^2}.
$$

In the historical $407X$ notation,

$$
\beta=\frac{z(2-z)}{1-z^2},
\qquad
m_\beta=\frac{1-z+z^2}{1-z^2}.
$$

Use this parameter when it genuinely shortens algebra. Retain
$\beta,m_\beta$ when substituting $z$ would enlarge independent center
formulas.

### 5.4. Threshold routing

The authoritative source is
[`2017_threshold_routing.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2017_threshold_routing.md).
Once an input crosses $e(d)$, the map $G_{1-d}$ produces at least
$1-e(d)$, and every later extensive map preserves the bound. After the
actual-row induction is established, discard maps that occur after the first
decisive threshold instead of evaluating them unnecessarily.

For the CE2 one-gap proof, retain the two-threshold dichotomy exactly. Do not
replace it by an unsupported symmetric strengthening.

### 5.5. CE1 one-gap proof

The authoritative branch source is
[`4106_CE1_one_gap_five_map_completion.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4106_CE1_one_gap_five_map_completion.md).
The hard selected row-$4$ branch must use the short concavity proof based on

$$
f_R(z)=w(R+z)(1-2z)-4Rz,
\qquad
f_R''(z)=-4w<0.
$$

For $R\le1/2$, check $f_R(P)>0$ through the cubic

$$
6E^3-2E^2-5E+2>0.
$$

For $R>1/2$, use

$$
A_0=\frac w2-\eta,
$$

$$
f_R(A_0)=
\frac{1-E}{2}(E+11R-3ER-5)>0.
$$

Do not restore the superseded degree-eight and degree-five endpoint
polynomials. Retain the existing proved terminal estimate unless a complete,
strictly shorter replacement is proved in the proof package.

### 5.6. The $407X$ package

`407a` and `407c` use the universal selected-$T_+$ normalization. The
independent center radical $\rho=\sqrt{r^2-r+1}$ remains. Keep the exact
high-left envelope, center-transfer, $S>3y$, $A_C>3y$, and analytic
right-$T_-$ threshold estimates. The optional historical script remains a
cross-check only.

### 5.7. The `4144` branch

The active `4144` proof uses interval residuals, the common small-slack
bounds, the stronger margin $\delta<H/4$, and the global quarter envelope
$c_{\max}(p,h)\le1-h/4$.  The historical half-edge $1/3$ envelope is not
an active manuscript dependency.

## 6. Strategy 4 Authoring Requirements

The concise reader-facing proof must contain exactly these mathematical
stages:

1. direct forcing of the centered disk and the three exact points
   $Q_-,Q_0,Q_+$;
2. replacement of the two radical outer points by Newton inner points;
3. the cyclic cap-chain lemma;
4. a proposition asserting the four required overlaps and citing their exact
   appendix proofs;
5. the enclosure and open-triangle contradiction.

### 6.1. Keep the Newton points

The exact outer points contain two independent quadratic roots. The one-step
Newton points lie strictly inside the corresponding witness segments and
have coordinates rational in $a,b$ and the single radical

$$
D=\sqrt{4(a^2+ab+b^2)-3}.
$$

Do not replace them by the exact outer roots unless a demonstrably shorter
complete mixed-overlap proof is obtained.

### 6.2. Cap-chain body proof

The universal calculus section defines the enclosure gauge $\Lambda$ once.
Strategy 4 reuses it and defines only the disk caps

$$
I(X,r)=
\left\{n\in S^1:
\langle X,n\rangle+r\ge\frac{\sqrt3}{2}
\right\}.
$$

It proves abstractly that the four consecutive overlaps

$$
I(A,2\eta)\leftrightarrow I(B,2\eta)\leftrightarrow
I(C,2\eta)\leftrightarrow I(W,\eta)\leftrightarrow I(RA,2\eta)
$$

cover one $120$-degree sector and, after rotation, the full direction circle.

### 6.3. Technical appendix

The Strategy 4 appendix must retain:

- the exact strict $AB$-union theorem;
- fixed-line and moving-circle signs;
- Newton placement and ray order;
- the two analytic adjacent overlaps;
- branchwise rational radial envelopes;
- the exact Gram factorization;
- all eight integer-polynomial signs;
- all twenty global Bernstein identities;
- exact replay commands and digests.

The body owns the cap-chain, enclosure, center-independent contradiction,
and terminal routing.  The appendix proves the Newton placement and every
component of the four-overlap proposition without repeating those body
arguments.

### 6.4. Optional disk-plus-point lemma

The proved source
[`3105a_disk_plus_point_enclosure.md`](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105a_disk_plus_point_enclosure.md)
is optional and is deliberately excluded from the paper. It closes a genuine
subregion but does not replace the global Newton four-cap proof. Do not add it
to the manuscript unless it materially reduces the remaining certificate and
the complete revised proof is supplied.

## 7. Final Assembly

`07_exhaustive_assembly.tex` must cite the reader-facing terminal
propositions:

- `prop:length-branches` for Strategy 1;
- `prop:reader-demand-branches` for Strategy 2;
- `prop:area-branches` for Strategy 3;
- `prop:reader-ab-core-branches` for Strategy 4.

The proof must audit every row of the routing table. Preserve the exhaustive
splits by center type, $N_+$, Vd0/Vd1/Vd2/T3-like pattern, and center-gap
state. No branch may disappear merely because its full algebra has moved to a
technical appendix.

## 8. Figures

Figures explain geometry but prove nothing. Every caption must say when a
picture is schematic or not to scale. No numerical relation may be inferred
from an illustrative image.

Use package-local image sources for proof-corpus figures. Paper figures and
shared TikZ styles remain under `arrange/paper_draft/figures/`. Use descriptive
ASCII filenames without spaces or shell-sensitive punctuation.

The reader-facing paper should retain figures that clarify:

- role assignment and center/vertex classifications;
- the Strategy 1 trace targets;
- the CE1/CE2 all-Vd0 demand geometry;
- local and cyclic area loss;
- the Strategy 4 radial and asymmetric witness geometry.

## 9. Source Ledger

Maintain `arrange/paper_draft/source_ledger.md` after every accepted change.
For each manuscript result, record:

- authoritative proof path;
- recorded status;
- manuscript label;
- whether it appears in the body or a technical appendix;
- whether any script is a proof dependency or only a replay/cross-check.

The ledger must state explicitly that:

- `2019`, `201a`, `201b`, and `201c` are active universal-calculus
  dependencies;
- `2016` and `2017` remain the authoritative selected-$T_+$ and threshold
  sources;
- `4106` uses the shortened $X>1/2$ proof;
- `407a` and `407c` write $\nu=\gamma_5$ directly and use the universal
  selected-$T_+$ curve;
- `4144` uses the quarter envelope;
- Newton inner points remain active;
- `3105a` is proved but excluded from the manuscript;
- the mixed-overlap Bernstein identities occur in a true appendix.

## 10. Verification

Build from `arrange/paper_draft/` with:

```text
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

After every source change:

1. compile to a fresh `main.pdf`;
2. check for undefined references, duplicate labels, missing inputs, missing
   graphics, and font errors;
3. confirm that all body and appendix theorem labels resolve;
4. verify that the final assembly cites only proved terminal propositions;
5. run the exact mixed-overlap derivation and global positivity replay tools;
6. inspect the PDF table of contents to confirm that the Strategy 2 and
   Strategy 4 technical sections occur after `\appendix`;
7. update `source_ledger.md` and commit the regenerated `main.pdf`.

The tracked PDF must correspond to the committed source. If a build cannot be
performed in the current environment, do not claim that the PDF is current;
report the unperformed build explicitly.

## 11. Repository Hygiene

Follow `AGENTS.md` for all repository edits.

- Update the authoritative proof note before or with its paper use.
- Preserve proof statuses and failed-route records.
- Keep changes surgical and grouped by mathematical purpose.
- Update local indexes, `proof/MANIFEST.txt`, status tables, and the source
  ledger when adding proof files.
- Do not alter `4144` or any other complete branch merely to pursue an
  incomplete simplification.
- Do not delete the full technical proofs after introducing a concise body
  statement.
- Report exactly what was compiled, replayed, and not checked.

The current paper architecture intentionally separates conceptual body proofs
from exact calculation appendices. That separation is valid only because the
appendices remain complete, rigorous, and precisely cross-referenced.
