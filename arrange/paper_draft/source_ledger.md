# Paper Source Ledger

This ledger records where each reader-facing claim is proved in the proof
corpus and how the compact manuscript body is connected to the technical
appendices.  It is not itself a proof.

## 1. Active manuscript artifacts

### Reader-facing body

| File | Function |
|---|---|
| `main.tex` | AMS assembly and body/appendix split |
| `01_introduction.tex` | theorem, forced roles, dictionary, routing table, proof-flow figures |
| `02_reader_framework.tex` | structural, admissible-set, transfer, and signed-center interfaces |
| `03_strategy1_reader.tex` | trace-cap register and terminal trace sums |
| `04_strategy2_summary.tex` | monotone-chain and terminal-inequality register |
| `05_strategy3_reader.tex` | area-loss register and cyclic sums |
| `06_strategy4_reader.tex` | geometric nine-point proof |
| `07_exhaustive_assembly.tex` | final routing audit |

### Technical appendices

| File | Function |
|---|---|
| `appendix_roadmap.tex` | variable-domain and verification-module guide |
| `02_structural_reductions.tex` | complete finite role/classification/routing proofs |
| `02a_universal_calculus.tex` | enclosure gauge, admissible-set transfer maps, residuals, relaxed composition |
| `04a_signed_center_calculus.tex` | signed CE1/CE2 side equations, traces, exits, and one-gap interface |
| `03_strategy1_length.tex` | complete perimeter and skeleton trace calculations |
| `04b_common_CE1_CE2_budgets.tex` | master deficit, short-role count, and common budgets |
| `04c_short_Vd_placements.tex` | quarter envelope, T3-like/Vd profiles, and shortened Vd placements |
| `04_strategy2_reader.tex` | proof-complete row chains and branch routing |
| `04_strategy2_exact_demand.tex` | contact cells, endpoint audits, and scalar certificates |
| `05_strategy3_area.tex` | affine orientation reduction and area inequalities |
| `06_strategy4_ab_core.tex` | strict frontier, Newton reduction, cap overlaps, and exact certificates |
| `appendix_symbols.tex` | notation cross-reference |

The label `page:proof-body-end` is placed immediately before `\appendix` and is
used to enforce the 20-page body limit.

## 2. Body interface provenance

### 2.1. Structural reduction

The proposition `prop:body-structural-reduction` summarizes only proved results:

- forced distinct center and vertex roles;
- exhaustive center classes CE0/CE1/CE2;
- exhaustive vertex classes Vd0/Vd1/Vd2/T3-like;
- strict boundary-handoff selection preserving the relevant actual
  supercritical pattern;
- unique center midpoint in CE1/CE2;
- short-role identity `q=N_++m`;
- exhaustive routing into Table `tab:routing`.

Principal proof sources include the `11XX` center classification, `12XX`
vertex/selection files, `2109` signed center normal form, `2510`/`2530` trace
budgets, and the proof-tree assembly files under `0XXX_main/`.

### 2.2. Local admissible set

The body defines

```text
K(a,b,c)=conv{0,au,bv,c(u+v)}
```

and states the exact minimum-side formula for the admissible set.  The complete
support-line proof and the equivalent selected algebraic cells come from:

- `2004_admissible_set.md`;
- the enclosure-gauge material in `02a_universal_calculus.tex`;
- the contact-cell catalogue in `04_strategy2_exact_demand.tex`.

The body deliberately includes the explicit description but not its projection
algebra, squaring steps, or component-selection proof.

### 2.3. Canonical transfer calculus

The body uses:

- raw `g_c`;
- hatted nonsupercritical `widehat g_c`;
- complement dual `f^vee`;
- center-assisted residual transfers;
- the free strict-supercritical envelope `g_c^{sc}`;
- pointwise lower relaxation of nondecreasing compositions.

The relevant proved sources are `2007`, `2010`, `2011`, `2016`, `2017`, `2018`,
`2019`, and `201d` in the `20XX_V_triangle_geometry` package, together with
`02a_universal_calculus.tex`.

The raw/capped zero-radial distinction is retained explicitly:

```text
g_0(x)>x,     widehat g_0(x)=x     (0<x<1).
```

### 2.4. Signed CE1/CE2 model

The body variables are

```text
0<R<1,  W=1-R,
E=sqrt(1-RW),  eta=1-E,  P=E(1-E),
Delta_R=P-alpha-W delta,
Delta_L=P-R alpha-delta.
```

The exact side equations, trace endpoints, radial exits, center-boundary
contribution, CE1/CE2 sign test, and legacy-coordinate translations are proved
in `2109_signed_CE1_CE2_center_normal_form.md` and reproduced in
`04a_signed_center_calculus.tex`.

## 3. Strategy provenance

### 3.1. Strategy 1

The body trace register is sourced from:

- center skeleton cap;
- positive-support and no-support vertex caps;
- supercritical skeleton cap;
- signed CE1/CE2 perimeter formula;
- Vd1/Vd2 and T3-like boundary caps;
- master perimeter deficit and the three-short-role theorem.

The complete proofs remain in `03_strategy1_length.tex` and
`04b_common_CE1_CE2_budgets.tex`, with proof-package sources under `25XX`.
No Strategy 1 routing assignment is removed by the transfer reformulation.

### 3.2. Strategy 2

`04_strategy2_summary.tex` states only the exact data needed to understand each
chain:

- strict identity cycle;
- one-side endpoint sum;
- CE2 paired endpoint sum;
- common one-gap five-row chain;
- CE1 affine-plus-threshold terminal;
- CE2 two-threshold dichotomy;
- exact four-label T3-like endpoint audit;
- free-envelope adjacent-rescuer chain;
- adjacent and nonadjacent Vd terminal margins.

The proof-complete row induction and slot table remain in
`04_strategy2_reader.tex`; all contact-cell and scalar verification remains in
`04_strategy2_exact_demand.tex` and `04c_short_Vd_placements.tex`.

The body notation `H_*` is the scalar denoted `H` in the exact one-gap appendix.
The body notation `H_far` is the far-side residual denoted `H` in the adjacent
Vd appendix.  These decorations prevent collision with the hexagon `H` without
changing any formula.

### 3.3. Strategy 3

The body uses only:

```text
L(a,b) >= min(a,b)^2,
L(a,b) >= max(a,b)^2 when a+b>1,
L_T3(a,b) >= 2m-4m^2 when a,b>=m.
```

The affine wedge/orientation proof, feasibility exclusions, and exact local
loss formulas remain in `05_strategy3_area.tex` and the corresponding `32XX`
proof package.

### 3.4. Strategy 4

The body remains the previously verified reader proof:

1. direct forcing of the centered disk and `Q_-,Q_0,Q_+`;
2. replacement by Newton inner points `A,B,C`;
3. cyclic cap-chain lemma;
4. one proposition asserting the four required overlaps;
5. enclosure and openness contradiction.

All strict frontier equations, moving-circle signs, rational envelopes, Gram
reductions, and Bernstein identities remain in `06_strategy4_ab_core.tex` and
its nested exact-certificate inputs.  The principal proof package is the
`3105X_self_contained_direct_Vd0_nine_point` package.

## 4. Assembly invariants

The final proof must retain all of the following.

1. `N_+` is computed from actual maximal reaches.
2. Selected handoffs are lower demands, not replacements for actual maxima.
3. Singleton gaps count as uncovered gaps.
4. The CE2 two-gap state is handled by the paired endpoint theorem.
5. The T3-like endpoint audit keeps all four exact labels.
6. The CE1 one-gap proof keeps its affine/threshold terminal argument.
7. The CE2 one-gap proof keeps its two-threshold dichotomy.
8. The nonadjacent Vd placement keeps its type-specific radial margin.
9. The hybrid CE2 row is split exactly between the existing Strategy 1 and
   Strategy 2 results.
10. The Strategy 4 mixed overlaps retain exact positive certificates.

## 5. Build status policy

The canonical build command is:

```bash
cd arrange/paper_draft
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

A body-only isolation build may be used to test page count and syntax, but it
is not a replacement for the complete build.  `main.pdf` is current only after
the complete source tree has been built and the resulting PDF has been
committed with the corresponding sources.

At the time of this architecture change, the tracked `main.pdf` is intentionally
left unchanged unless a complete repository build is performed.  Do not infer
that a source-only branch contains an updated PDF.

## 6. Deliberate nondependencies

The paper does not use:

- the obsolete half-edge `1/3` envelope as an active dependency;
- interval arithmetic or branch-and-bound in the all-Vd0 nine-point core;
- a plot as a proof of a sign inequality;
- any stronger symmetric replacement for the T3-like endpoint theorem;
- any route marked only `Strategy`, `Empirical`, `Experiment`, or `Failed`.
