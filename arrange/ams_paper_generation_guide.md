# AMS-Style Main-Theorem Paper Generation Guide

This file is an authoring specification. It is not a proof source. Its purpose
is to maintain the modular AMS-style paper proving the theorem in
[`0000_main_theorem.md`](../proof/0XXX_main/0000_main_theorem.md).

The paper is organized by four named strategies rather than by the
repository's CE-first proof tree:

1. direct length-sum obstructions;
2. relaxations of raw $g$-composition chains;
3. normalized area loss;
4. the center-independent direct nine-point obstruction.

The proof corpus remains authoritative for theorem statements, hypotheses,
and status. The manuscript may reorganize and simplify that material, but it
must not strengthen a result, suppress a strictness condition, or treat a
navigation file as a proof.  The Strategy 2 reformulation does not change any
Strategy 1 theorem or routing assignment.

## 1. Source And Status Rules

Before editing the paper, read:

- [`README.md`](../README.md);
- [`0000_main_theorem.md`](../proof/0XXX_main/0000_main_theorem.md);
- [`0001_proof_tree_index.md`](../proof/0XXX_main/0001_proof_tree_index.md);
- [`0002_status_and_dependencies.md`](../proof/0XXX_main/0002_status_and_dependencies.md);
- [`0910_notation_dictionary.md`](../proof/09XX_appendices/0910_notation_dictionary.md);
- [`1006_proof_status_conventions.md`](../proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md);
- [`201d_raw_and_relaxed_g_chains.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md);
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
8. Record every reusable simplification in `proof/` before or together with
   its manuscript use.
9. Preserve the current Strategy 1 routing, including `4040`, `4041`, `4110`,
   `4111`, `4123`, `4149`, `414a`, and `4200`, even when a length bound can be
   viewed abstractly as a coarse transfer envelope.

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

The introduction is the single proof guide. Structural reduction and the
common signed center calculus precede the four mechanism sections. Complete
exact Strategy 2 and Strategy 4 calculations remain technical appendices after
the final theorem assembly.

### 2.1. Body files

- `01_introduction.tex` states the theorem, definitions, unchanged routing
  table, active-gap-rank notation, and compact proof architecture.
- `02_structural_reductions.tex` proves the exhaustive role and case
  reductions.
- `04a_signed_center_calculus.tex` proves the common signed CE1/CE2 model and
  defines the local propagation interface in the body.
- `02a_universal_calculus.tex` proves the enclosure gauge, universal radical,
  raw and capped transfer maps, center residuals, free raw-graph envelopes,
  relaxed composition, boundary-path budget, selected-$T_+$ curve, and
  threshold routing once for all later strategies.
- `03_strategy1_length.tex` contains the complete and unchanged length
  arguments.
- `04_strategy2_reader.tex` contains the master chain-signature table, the
  all-Vd0 active-gap-rank kernel, the common five-row chain and its CE1/CE2
  relaxations, free-envelope rescuer chains, and Vd terminal transfers.
- `05_strategy3_area.tex` contains the complete area-loss arguments.
- `06_strategy4_reader.tex` contains only direct witness forcing, Newton inner
  points, the cyclic cap-chain lemma, the four-overlap proposition, and the
  enclosure conclusion.
- `07_exhaustive_assembly.tex` closes every row of the routing table using the
  reader-facing terminal propositions and explicitly preserves the Strategy 1
  side of the hybrid row.

### 2.2. Technical appendices

After `\appendix`, input:

- `04c_short_Vd_placements.tex`: the quarter radial envelope, rational T3-like
  and Vd1 profiles, common adjacent rescuer, and shortened Vd placements;
- `04_strategy2_exact_demand.tex`: the proof-complete exact admissible-set
  catalogue, full terminal inequalities, and exact endpoint audits;
- `06_strategy4_ab_core.tex`: the proof-complete strict $AB$ frontier,
  fixed-line signs, Newton reduction, ray order, and four cap overlaps;
- `appendix_symbols.tex`.

`06_strategy4_ab_core.tex` owns the nested inputs
`appendix_certificates.tex` and `appendix_exact_mixed_overlap.tex`. Since its
own section is after `\appendix`, the caliper theorem, polynomial expansions,
and Bernstein identities are genuine appendix material.

The body may cite a precisely stated proved appendix lemma or proposition.
The appendix must still contain the full mathematical proof, not merely a
script command or a table of output.

## 3. Required `main.tex` Assembly

The minimum preamble is:

```latex
\documentclass{amsart}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs,graphicx}
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

The `mathrsfs` package supplies the branch-signature symbol $\mathscr C$.
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
sources control their placement. The historical half-edge $1/3$ envelope has
no standalone manuscript source and is not an active dependency.

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
- $\mathrm{gr}$ for active-gap rank; do not use bare $g$ for this count;
- $B_c$ for the exact outgoing envelope and $g_c=1-B_c$ for the raw transfer;
- $F_c=\min\{B_c,1-\mathrm{id}\}$ and
  $G_c=1-F_c=\max\{g_c,\mathrm I\}$ for the capped map;
- $\mathfrak g_{c,J}=\mathcal R_J\circ B_c$ and
  $\mathcal G_{c,J}=\mathcal R_J\circ F_c$ for center-assisted transfers;
- $A_{\rm sc},B_{\rm sc}$ for the free raw-graph envelopes;
- $\mathrm I$, $\Theta_d$, and $\mathsf L_{d,\lambda}$ for the identity,
  threshold, and affine selected-$T_+$ relaxations;
- $[\Phi_1\mid\cdots\mid\Phi_r]$ for maps listed in geometric row order;
- $\mathscr C[\mathrm{seed};\,\cdots;\,\mathrm{terminal}]$ for a branch
  signature;
- $c_*$, $\mathcal D_\eta$, $Q_-,Q_0,Q_+$, $A,B,C$, and $\Lambda$ for
  Strategy 4.

Preserve the Korean term `걸거치는` through the existing Hangul macro where it
names the recurring crossing configuration.

## 5. Strategy 2 Authoring Requirements

### 5.1. Raw map and proof-safe envelopes

The raw map is

$$
g_c(a)=1-B_c(a).
$$

It applies to every row: if an actual row has incoming reach at least $a$,
radial reach at least $c$, and outgoing reach $B$, then

$$
B\le B_c(a),
\qquad
A_{\rm next}\ge g_c(a)
$$

when no center interval intervenes.

For a nonsupercritical row,

$$
F_c(a)=\min\{B_c(a),1-a\},
\qquad
G_c(a)=1-F_c(a)=\max\{g_c(a),a\}.
$$

Thus the identity is one lower relaxation of the same row transfer. Do not say
that axis alignment proves $G_c\ge\mathrm I$; nonsupercriticality proves this.
Axis replacement is geometric preprocessing that places a row in the ordinary
nonsupercritical Vd0 class.

For $0\le c<1/2$,

$$
B_{\rm sc}(c)
=
\sup_{\{a:g_c(a)<a\}}B_c(a),
\qquad
A_{\rm sc}(c)
=
\inf_{\{a:g_c(a)<a\}}g_c(a).
$$

This is the correct common interpretation of the free-supercritical functions.
Do not identify them literally with the capped map at $c=0$: the exact formula
gives $G_0=\mathrm I$.

More generally, for any proved outgoing upper envelope $U$, the induced
center-assisted lower transfer is

$$
\mathsf T_{U,J}(a)=\mathcal R_J(U(a)).
$$

Replacing $U$ by a larger, simpler envelope makes the lower transfer smaller
and therefore proof-safe.

### 5.2. Actual-row interface and center residuals

Every formal map transition must be connected to an actual row. If an actual
nonsupercritical role satisfies

$$
A_i\ge z,
\qquad
C_i\ge c_i,
\qquad
A_i+B_i\le1,
$$

then

$$
B_i\le F_{c_i}(z),
\qquad
A_{i+1}\ge1-B_i\ge G_{c_i}(z).
$$

If a center interval $J$ intervenes, use

$$
\mathfrak g_{c,J}=\mathcal R_J\circ B_c,
\qquad
\mathcal G_{c,J}=\mathcal R_J\circ F_c.
$$

Do not write a formal composition without identifying the actual rows that
realize these inequalities. Singleton gaps remain included.

Use the boundary-path lemma instead of repeating three-row or four-row
terminal sums when the path formulation is shorter.

### 5.3. Chain and branch notation

For maps listed in geometric row order, write

$$
[\Phi_1\mid\cdots\mid\Phi_r](x)
=(\Phi_r\circ\cdots\circ\Phi_1)(x).
$$

A branch summary has the form

$$
\mathscr C[
\mathrm{seed};\,
\Phi_1\mid\cdots\mid\Phi_r;\,
\mathrm{terminal}].
$$

A relaxation table must say:

1. the exact seed or residual input;
2. the exact row chain before relaxation;
3. which slots are retained exactly;
4. which slots are replaced by $\mathrm I$, an affine chord, a threshold, or a
   branch-specific terminal envelope;
5. the terminal capacity or separation inequality.

The reader-facing master table is
`tab:strategy2-chain-signatures` in `04_strategy2_reader.tex`.

### 5.4. Active-gap-rank kernel

The all-Vd0 CE1/CE2 proof is organized by $N_+\in\{0,1\}$ and the active-gap
rank $\mathrm{gr}\in\{0,1,2\}$. The paired endpoint theorem has one common
geometric application in the two $\mathrm{gr}=2$ cells.

- $N_+=0$, $\mathrm{gr}=0$: use the strict identity cycle
  $A_{i+1}>G_{C_i}(A_i)\ge A_i$.
- $N_+=0$, $\mathrm{gr}=1$: retain the two exact endpoint maps and replace the
  three middle rows by $\mathrm I^3$.
- $N_+=0$, T3-like: use residual endpoint inputs, retain the exact four-label
  endpoint audit, and replace the three interior rows by $\mathrm I^3$.
- either $\mathrm{gr}=2$ cell: retain the paired endpoint inequality and use
  $\mathrm I^3$ internally.
- $N_+=1$, $\mathrm{gr}=0$: keep the existing Strategy 4 nine-point route.

### 5.5. Universal selected-$T_+$ curve

The authoritative reusable source is
[`2016_universal_Tplus_normal_form.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2016_universal_Tplus_normal_form.md).
For deficit $d$, input $p$, output $q=G_{1-d}(p)$, increment $\nu=q-p$, and
normalized output $x=(q-d)/(1-d)$, the selected equation reduces to

$$
x(1-x)=\nu(2-\nu).
$$

Hence

$$
\nu=\sigma(x)=1-\sqrt{1-x+x^2},
$$

$$
q=d+(1-d)x,
\qquad
p=d+(1-d)x-\sigma(x).
$$

Use $\sigma''(x)<0$ to prove strict concavity once. Do not repeat the old
implicit branch-specific differentiation.  An affine lower chord is denoted

$$
\mathsf L_{d,\lambda}(p)=p+\lambda(p-d).
$$

The optional rational parameter is

$$
x=\frac{1-2z}{1-z^2},
\qquad
\sigma(x)=\frac{z(1-2z)}{1-z^2}.
$$

In the historical `407X` notation,

$$
\beta=\frac{z(2-z)}{1-z^2},
\qquad
m_\beta=\frac{1-z+z^2}{1-z^2}.
$$

Retain $\beta,m_\beta$ when substituting $z$ would enlarge independent center
formulas.

### 5.6. Threshold routing and one-gap chains

The authoritative source is
[`2017_threshold_routing.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2017_threshold_routing.md).
Define

$$
\Theta_d(x)=
\begin{cases}
x,&x\le e(d),\\
1-e(d),&x>e(d).
\end{cases}
\qquad
\Theta_d\le G_{1-d}.
$$

The common one-gap interface starts from the exact five-row chain

$$
[G_{c_1}\mid G_{c_2}\mid G_{c_3}\mid G_{c_4}\mid G_{c_5}](X).
$$

The first and fifth slots are relaxed to $\mathrm I$, and exact duality reverses
the middle three slots.

For CE1, retain the proved hard-branch signature

$$
\mathscr C[
H;\,
\mathsf L_{\alpha,1-4\alpha}
\mid
\mathsf L_{m,1-5m}
\mid
\Theta_\delta;\,
>1-X].
$$

The authoritative branch source is
[`4106_CE1_one_gap_five_map_completion.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4106_CE1_one_gap_five_map_completion.md).
Keep its shortened $X>1/2$ concavity proof and its proved terminal estimate.
Do not restore superseded high-degree endpoint polynomials.

For CE2, retain the two-threshold dichotomy exactly. One of the signatures is

$$
\mathscr C[X;\mathrm I\mid\mathrm I\mid\mathrm I\mid
\Theta_\alpha\mid\mathrm I;>1-H]
$$

and the other is

$$
\mathscr C[X;\mathrm I\mid\Theta_\delta\mid
\mathrm I\mid\mathrm I\mid\mathrm I;>1-H].
$$

Do not replace this dichotomy by an unsupported symmetric strengthening.

### 5.7. The `407X` package

`407a` and `407c` use the universal selected-$T_+$ normalization. The
independent center radical $\rho=\sqrt{r^2-r+1}$ remains. Keep the exact
high-left envelope, center-transfer, $S>3y$, $A_C>3y$, and analytic
right-$T_-$ threshold estimates. The optional historical script remains a
cross-check only.

The abstract chain is exact endpoints plus $\mathrm I^3$ internally. Do not
replace the hard-region endpoint audit by a weaker universal formula unless a
complete proof is first added to the proof corpus.

### 5.8. Special-role terminal chains

The T3-like rescuer and adjacent Vd1 rescuer share

$$
\mathscr C[
A_{\rm sc}(c);\,
\mathrm I^3;\,
b_5<B_{\rm sc}(c)\le h].
$$

Only the local verification of the two $A_{\rm sc}$ inequalities differs.

The active `4144` proof uses interval residuals, the common small-slack bounds,
the stronger margin $\delta<H/4$, a backward identity chain, and the terminal
quarter-envelope inequality

$$
F_{1-\delta}\left(\frac12+A\right)<H,
\qquad
G_{1-\delta}\left(\frac12+A\right)>1-H.
$$

The historical half-edge $1/3$ envelope is not an active dependency.

The `4146` terminal inequality is Vd-type-specific. Do not present it as a
universal $G_c$ bound. The `4147` axis replacement is preprocessing; after it,
the ordinary all-Vd0 chain applies.

The Strategy 1 files `4149` and `414a` remain Strategy 1, and their statements
and routing must not be absorbed into the transfer table.

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
Newton points lie strictly inside the corresponding witness segments and have
coordinates rational in $a,b$ and the single radical

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

The body owns the cap-chain, enclosure, center-independent contradiction, and
terminal routing. The appendix proves the Newton placement and every component
of the four-overlap proposition without repeating those body arguments.

### 6.4. Optional disk-plus-point lemma

The proved source
[`3105a_disk_plus_point_enclosure.md`](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105a_disk_plus_point_enclosure.md)
is optional and deliberately excluded from the paper. It closes a genuine
subregion but does not replace the global Newton four-cap proof.

## 7. Final Assembly

`07_exhaustive_assembly.tex` must cite the reader-facing terminal propositions:

- `prop:length-branches` for Strategy 1;
- `prop:reader-demand-branches` for Strategy 2;
- `prop:area-branches` for Strategy 3;
- `prop:reader-ab-core-branches` for Strategy 4.

It must also cite `tab:strategy2-chain-signatures` when describing the transfer
rows. The proof must audit every routing-table row. Preserve the exhaustive
splits by center type, $N_+$, Vd0/Vd1/Vd2/T3-like pattern, and center-gap state.
No branch may disappear merely because its full algebra has moved to a
technical appendix.

In the row marked $1+2$, retain the existing Strategy 1 and Strategy 2
complementary placements. The chain reformulation does not subsume the
Strategy 1 side.

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

- `201d` is the authoritative raw and relaxed chain source;
- `2019`, `201a`, `201b`, and `201c` remain active universal-calculus
  dependencies;
- `2016` and `2017` remain the selected-$T_+$ and threshold sources;
- $A_{\rm sc},B_{\rm sc}$ are raw-graph envelopes and are not identified with
  the capped map $G_0$;
- `4106` uses the shortened $X>1/2$ proof;
- `407a` and `407c` retain the exact endpoint audit and universal selected
  curve;
- `4144` uses the quarter envelope;
- `4146` uses a Vd-specific terminal margin;
- all existing Strategy 1 routes remain unchanged;
- Newton inner points remain active;
- `3105a` is proved but excluded from the manuscript;
- the mixed-overlap Bernstein identities occur in a true appendix.

## 10. Verification

Build from `arrange/paper_draft/` with:

```text
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

After every source change:

1. compile to a fresh `main.pdf` when the environment supports the complete
   XeLaTeX build;
2. check for undefined references, duplicate labels, missing inputs, missing
   graphics, font errors, and overfull boxes;
3. confirm that all body and appendix theorem labels resolve;
4. verify that the final assembly cites only proved terminal propositions;
5. run the exact mixed-overlap derivation and global positivity replay tools
   when those sources change;
6. inspect the table of contents to confirm that the Strategy 2 and Strategy 4
   technical sections occur after `\appendix`;
7. update `source_ledger.md` and commit the regenerated `main.pdf` when a full
   build was actually performed.

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
- Do not delete full technical proofs after introducing a concise body
  statement.
- Report exactly what was compiled, replayed, and not checked.

The current paper architecture intentionally separates conceptual body proofs
from exact calculation appendices. That separation is valid only because the
appendices remain complete, rigorous, and precisely cross-referenced.
