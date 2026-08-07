# Paper Source Ledger

This ledger records the relationship between the reader-facing paper, the TeX
appendices, the numbered proof package, and the exact electronic certificates.
It is a provenance and audit document, not itself a proof.

## 1. What constitutes the proof

The complete proof consists of three layers.

1. **Reader-facing body:** definitions, geometric mechanisms, exact terminal
   statements, and exhaustive assembly.
2. **Technical TeX appendices:** complete structural, analytic, placement, and
   area arguments establishing those terminal statements.
3. **Formally incorporated electronic supplements:** the complete `407X`
   four-label algebra and the Strategy 4 sparse-polynomial certificate,
   identified by repository path, Git blob, and transcript hash.

The body explains the complete logical flow but is not claimed to prove every
calculation lemma without the appendices and incorporated supplements.

## 2. Active manuscript artifacts

### Reader-facing body

| File | Function |
|---|---|
| `main.tex` | AMS assembly and body/appendix split |
| `01_introduction.tex` | theorem, roles, definitions, routing table, role figure |
| `02_reader_framework.tex` | structural, admissible-set, transfer, signed-center interfaces |
| `02c_strategy2_skeleton_atlas.tex` | modular full-skeleton dictionary for the transfer and signed-center interfaces |
| `03_strategy1_reader.tex` | trace-cap register and terminal trace sums |
| `04_strategy2_summary.tex` | complete branch hypotheses and certificate register |
| `05_strategy3_reader.tex` | area-loss register and cyclic sums |
| `06_strategy4_reader.tex` | nine-point geometry and cap-chain reduction |
| `07_exhaustive_assembly.tex` | final exhaustive audit |

### Technical appendices

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
| `04_strategy2_verification.tex` | input-only wrapper for the split Strategy 2 verification modules |
| `05_strategy3_area.tex` | local area inequalities and cyclic certificates |
| `06_strategy4_ab_core.tex` | frontier, forcing, Newton reduction, adjacent overlaps |
| `06a_strategy4_exact_certificate.tex` | sole mixed-overlap certificate source: reduction, manifest, Bernstein proof, cap geometry |
| `appendix_symbols.tex` | notation cross-reference |

The body-end label remains immediately before `\appendix`.  The body has no
fixed page cap; its page number is recorded after each complete build.

The illustrated Strategy 2 atlas is explanatory only.  Its 32 modular panels
are grounded in the regular hexagon skeleton and occur in the reader-facing
body beside the corresponding mathematical definitions; any non-metric
placement is explicitly marked schematic.

## 3. Repairs made after the validity audit

### 3.1 Center-free hypotheses

The strict-supercritical outgoing bound

```text
B < g_c^{sc}
```

is unconditional. Its complementary following demand

```text
A_next > 1-g_c^{sc}
```

requires a center-free outgoing edge. This is now explicit in the body and in
`02a_universal_calculus.tex`.

The proof-package source

```text
proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/
2019_interval_component_and_path_budget.md
```

was repaired similarly: every internal path edge must exclude center and
nonincident positive-length traces, and all endpoint external contributions
must be absorbed into the endpoint residuals. The active applications `4013`
and `2110` were updated to verify these hypotheses explicitly.

### 3.2 Threshold and terminal coordinates

The CE2 argument proves that **at least one** of the two threshold slots fires;
it does not prove uniqueness. Both may be available.

For the exact five-V-triangle chain

```text
Z = [g_1^vee|...|g_5^vee](X),
```

the direct target is `Z>1-H`. The target `>1-X` belongs to the reversed
three-map chain after capped-map duality. The body, tables, and appendix now
distinguish these statements.

### 3.3 Strategy 1 hypothesis

The reader master perimeter deficit now states that every V triangle not assigned a
special cap contributes at most one. This hypothesis was present in the
numbered source `2530` and is satisfied in every routed application.

### 3.4 Admissible-set derivation

`02b_admissible_set_derivation.tex` now contains:

- the explicit triangular-hull enclosing equilateral triangle and barycentric
  containment of the origin;
- all four edge-normal support values;
- the active support patterns;
- derivation of `F_L`, `F_T`, and `F_S`;
- the connected-component selectors `c<=2M` and `c<=1/2`;
- the exact radial envelope.

### 3.5 T3-like endpoint audit

The complete `407X` proof is formally incorporated from the current
proof-package objects.  Full Git blob identities are recorded in
`proof/407X_PROVENANCE.json`; the current prefixes are:

| File | Blob prefix |
|---|---|
| `4073_boundary_loss_framework.md` | `910c7a8a1330` |
| `4074_L_Full_branch.md` | `7c72dfaf7eb3` |
| `4075_Tminus_low_lower_branch_obligations.md` | `ebe2b65f8840` |
| `4078_left_L_family_completion.md` | `f1323325b069` |
| `4079_first_Full_branch.md` | `c66eea05277d` |
| `407a_left_Thigh_branch_completion.md` | `aa5cb1a6dc63` |
| `407c_rigor_completion_details.md` | `c80243f67124` |
| `407d_rigor_final_assembly.md` | `e22c85c95fdd` |

CI recomputes every Git blob from the exact file bytes and verifies
both the consolidated TeX manifest and this ledger.

### 3.6 Vd1 replacement and placement assembly

The consolidated `04_strategy2_verification.tex` is the sole detailed
Strategy 2 verification source.  It contains:

- the complete four-label `407X` endpoint audit;
- separate local charts at the two distinguished replacement vertices;
- the exact shifted-template reach triples;
- the Vd0 and nonsupercritical role checks;
- preservation of the shared edge, outer boundary traces, and radial handoffs;
- preservation of the full skeleton required by strengthened `4013`;
- the single authoritative CE2 exactly-one-Vd1/Vd2 placement assembly.

`04c_short_Vd_placements.tex` now contains only reusable local lemmas
and no competing branch assembly.

### 3.7 Strategy 4 certificate

`06a_strategy4_exact_certificate.tex` formally incorporates:

- all six sparse-data shards;
- the canonical transcript digest
  `dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485`;
- the exact rational-function derivation verifier;
- the exact global Bernstein verifier;
- the positive-denominator conditions;
- the implication from residual positivity to common tangent support and cap
  intersection.

The certificate uses exact integers, rationals, and `Q(sqrt(3))`. No
floating-point or interval computation is an active dependency.

## 4. Body-interface provenance

### Structural reduction

`prop:body-structural-reduction` summarizes the distinct roles, exhaustive
center and vertex classifications, actual reaches, `N_+`, singleton gaps,
strict handoff selection, unique center midpoint, short-role identity, and
routing table. These are proved in `02_structural_reductions.tex` and the
`1XXX`, `2109`, and `2530` packages.

### Local enclosure and transfers

The explicit minimum-side formula is proved in `02b` and agrees with proof
source `2004`. The transfer notation comes from `201d`:

```text
g_c(x)=max{y:(1-x,y,c) in A},
widehat g_c(x)=min{g_c(x),x},
f^vee(a)=1-f(1-a).
```

The corrected center-free and center-assisted statements are in `02a` and the
repaired `2019` source.

### Signed center

The variables

```text
0<R<1, W=1-R,
E=sqrt(1-RW), eta=1-E, P=E(1-E),
Delta_R=P-alpha-W delta,
Delta_L=P-R alpha-delta
```

and all trace, exit, midpoint, and boundary-contribution formulas are proved in
`04a_signed_center_calculus.tex` and proof source `2109`.

## 5. Strategy audit status

### Strategy 1

Active sources are `2500`, `2510`, `2530`, `03_strategy1_length.tex`, and
`04b_common_CE1_CE2_budgets.tex`. The terminal sums are valid, and the reader
statement now includes every cap hypothesis.

### Strategy 2

Active sources include `2004`, `2010`--`2019`, `2107`--`2110`, `4013`, the
complete `407X` supplement, `4105`--`4107`, `413X`, and `4143`--`4149`.
The paper preserves:

- actual versus selected criticality;
- center-free path hypotheses;
- exact endpoint residuals;
- the CE1 affine/threshold ending;
- the CE2 at-least-one-threshold dichotomy;
- all four T3 labels;
- the adjacent quarter and nonadjacent Vd-specific radial margins;
- explicit open Vd0 replacements;
- the exhaustive one-Vd placement assembly.

### Strategy 3

Active sources are `3175`, `3205`, `3208`, and `05_strategy3_area.tex`. The two
orientation normal forms, local square losses, reflection normalization, and
both cyclic sums are complete and valid.

### Strategy 4

Active sources are the `3105X_self_contained_direct_Vd0_nine_point` package,
`06_strategy4_ab_core.tex`, and `06a_strategy4_exact_certificate.tex`. Direct
forcing, Newton placement, cap chain, and adjacent overlaps are analytic. The
two mixed overlaps are exact computer-assisted claims with authenticated input
and exact verification algorithms. Source review found no arithmetic-model,
coordinate-normalization, or Bernstein-conversion defect. The exact derivation and positivity verifiers are replayed by read-only proof CI on every change.

## 6. Assembly invariants

The final proof retains all of the following.

1. `N_+` uses actual maximal reaches.
2. Selected handoffs remain lower demands.
3. Singleton gaps remain gaps.
4. Center-assisted handoffs use residual maps.
5. Every path-budget internal edge is center-free.
6. Raw and capped zero-radial maps remain distinct.
7. CE1 and CE2 one-gap endings remain distinct.
8. The T3-like theorem retains all four exact labels.
9. Adjacent and nonadjacent Vd routes retain their correct geometric margins.
10. The CE2 one-Vd branch uses the complete placement assembly.
11. The Strategy 4 mixed overlaps use the authenticated exact certificate.

## 7. Build and PDF status

The tracked `main.pdf` is rebuilt with a fixed `SOURCE_DATE_EPOCH` and
compared byte-for-byte with a clean XeLaTeX rebuild in permanent
read-only CI.  The current source commit, workflow run, exact verifier
results, tool versions, page count, and PDF SHA-256 are recorded in
`../20260802_verification_summary.txt`.

## 2026-07-31 reader-interface revision

- Proposition 2.5 now states only the definition-level and qualitative
  properties of the admissible set; its finite-caliper equations and formula
  diagrams are in Appendix B.
- Definition 2.12 now defines the signed center geometry without reproducing
  its affine equations; the exact chart, traces, exits, sign cells, and diagrams
  are in Appendix D.
- Proposition 3.1 uses $L_{\partial H}(T_i)$ uniformly for all four V-triangle
  boundary roles.
- Table 2 displays six functions in every $g$-composition chain, retains
  point-contact center intervals in every exact slot, and states the exact
  handoff inequality represented by each identity slot.
- Canonical proved notes use “V triangle” for the geometric object; historical
  filenames and link targets containing `row` were retained for repository
  stability.

Post-edit audit repairs: the reader definition now reuses the appendix symbol
$\Delta_L$ for the signed companion trace; all six-slot words retain degenerate
center intervals; and identity slots are stated as weakened individual
handoff inequalities rather than as an unsupported order on formal
compositions.

## 2026-08-07 Strategy 2 optimization extraction

The Strategy 2 interface now has four layers.

1. `04_strategy2_summary*.tex`: reader-facing geometry and routing.
2. `04d_strategy2_parameter_bridges.tex`: the sole geometry--parameter dictionary.
3. `04_strategy2_optimization_*.tex`: explicit real-variable problem domains and objectives.
4. `04e_strategy2_verification_*.tex`: the application registry and preserved exact calculation sections.

The T3 endpoint domain is a finite union of signed-center, residual-order,
radial hit/miss, and four-label cells.  The non-symmetry trace-dominating
translation is represented by exact radical variables; the preceding \(D_6\)
normalization remains geometric.  The Vd problems use explicit component and
corner graph functions, with no placement-defined supremum.  The Lean shell in
`formalization/strategy2_optimization/` contains only problem statements with
`sorry`.

<!-- BEGIN GENERATED 407X SPLIT PROVENANCE -->
## Generated 407X split-source provenance

The split verification appendix retains the following exact proof-package objects.

| File | Git blob prefix |
|---|---|
| `4073_boundary_loss_framework.md` | `910c7a8a1330` |
| `4074_L_Full_branch.md` | `7c72dfaf7eb3` |
| `4075_Tminus_low_lower_branch_obligations.md` | `ebe2b65f8840` |
| `4078_left_L_family_completion.md` | `f1323325b069` |
| `4079_first_Full_branch.md` | `c66eea05277d` |
| `407a_left_Thigh_branch_completion.md` | `aa5cb1a6dc63` |
| `407c_rigor_completion_details.md` | `c80243f67124` |
| `407d_rigor_final_assembly.md` | `e22c85c95fdd` |
<!-- END GENERATED 407X SPLIT PROVENANCE -->
