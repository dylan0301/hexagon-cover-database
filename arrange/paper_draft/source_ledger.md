# Paper Source Ledger

This ledger records the exact relationship between the reader-facing paper,
the technical TeX appendices, the proof-package sources, and the exact
electronic certificates. It is a provenance and audit document, not itself a
proof.

## 1. What constitutes the paper proof

The proof consists of three layers.

1. **Reader-facing body.** Definitions, geometric mechanisms, exact terminal
   statements, and exhaustive case assembly.
2. **Technical TeX appendices.** Complete structural, analytic, placement, and
   area arguments needed to establish the terminal statements.
3. **Formally incorporated electronic supplements.** The complete `407X`
   four-label branch algebra and the exact Strategy 4 sparse-polynomial
   certificate, identified by repository path, Git blob, and transcript hash.

The body alone explains the logical flow but is not claimed to prove every
calculation lemma without the appendices and incorporated supplements.

## 2. Active manuscript artifacts

### 2.1 Reader-facing body

| File | Function |
|---|---|
| `main.tex` | AMS assembly and body/appendix split |
| `01_introduction.tex` | theorem, roles, definitions, routing table, proof-flow figures |
| `02_reader_framework.tex` | structural, admissible-set, transfer, and signed-center interfaces |
| `03_strategy1_reader.tex` | trace-cap register and terminal trace sums |
| `04_strategy2_summary.tex` | complete branch hypotheses and terminal certificate register |
| `05_strategy3_reader.tex` | area-loss register and cyclic sums |
| `06_strategy4_reader.tex` | geometric nine-point proof and cap-chain reduction |
| `07_exhaustive_assembly.tex` | final exhaustive audit |

### 2.2 Technical appendices

| File | Function |
|---|---|
| `appendix_roadmap.tex` | verification-module guide and proof-layer disclaimer |
| `02_structural_reductions.tex` | role classification, reaches, gaps, strict handoffs, routing |
| `02a_universal_calculus.tex` | enclosure gauge, corrected transfers, residuals, center-free path budget |
| `02b_admissible_set_derivation.tex` | full support derivation, polynomial cells, selectors, radial envelope |
| `04a_signed_center_calculus.tex` | signed CE1/CE2 equations, traces, exits, one-gap interface |
| `03_strategy1_length.tex` | perimeter and skeleton trace calculations |
| `04b_common_CE1_CE2_budgets.tex` | master deficit, short-role count, common budgets |
| `04c_short_Vd_placements.tex` | quarter envelope, local profiles, adjacent and nonadjacent radial separations |
| `04_strategy2_reader.tex` | proof-complete row chains and corrected terminal coordinates |
| `04_strategy2_exact_demand.tex` | contact cells, endpoint inequalities, CE1 scalar calculation |
| `04d_strategy2_rigor_completion.tex` | incorporated `407X` audit and complete Vd1 axis replacement |
| `04e_strategy2_placement_assembly.tex` | authoritative CE2 exactly-one-Vd placement assembly |
| `05_strategy3_area.tex` | local area inequalities and cyclic certificates |
| `06_strategy4_ab_core.tex` | strict frontier, direct forcing, Newton reduction, adjacent overlaps |
| `06a_strategy4_exact_certificate.tex` | exact mixed-overlap reduction, certificate manifest, geometric implication |
| `appendix_symbols.tex` | notation cross-reference |

The label `page:proof-body-end` remains immediately before `\appendix`. The
present source-only repair did not compile the manuscript and makes no new page
count claim.

## 3. Corrections made after the validity audit

### 3.1 Center-free transfer hypotheses

The outgoing strict-supercritical bound

```text
B < g_c^{sc}
```

is unconditional, but the complementary following demand

```text
A_next > 1-g_c^{sc}
```

is valid only on a center-free outgoing edge. This distinction is now explicit
in both `02_reader_framework.tex` and `02a_universal_calculus.tex`.

The same correction was made in the authoritative proof-package source

```text
proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/
2019_interval_component_and_path_budget.md
```

for the boundary-path budget: every center or nonincident contribution on an
internal edge must be excluded, and endpoint contributions must be absorbed
into the external residual quantities.

### 3.2 CE2 threshold language

The CE2 inequalities prove that **at least one** of the two threshold slots
fires. They do not prove uniqueness, and both may be available. All body and
appendix statements now use the correct formulation.

### 3.3 Exact versus reversed one-gap targets

For the exact five-row chain,

```text
Z = [g_1^vee|...|g_5^vee](X),
```

the direct contradiction is `Z>1-H`. The inequality `>1-X` belongs to the
reversed three-map chain after capped-map duality. The Strategy 2 tables and
proof now distinguish these two statements.

### 3.4 Vd1 replacement

The former short sketch was not used as the final proof. The complete argument
in `04d_strategy2_rigor_completion.tex` now includes:

- the two ordered halves of the half-square admissibility lemma;
- all strict local margins;
- the center-handoff radial inequality;
- explicit axis triangles;
- the translations making both replacements open and nonsupercritical;
- preservation of the shared boundary and both radial demands.

The final assembly uses `prop:paper-vd1-pair-replacement` and the authoritative
placement proposition `prop:paper-ce2-one-vd-placements`.

### 3.5 T3-like endpoint audit

The complete `407X` proof is formally incorporated. The paper reproduces the
principal high-sheet envelope, right-`T_-` bounds, and analytic threshold, and
pins the complete branch files by Git blob. The active supplement is:

```text
proof/4XXX_CE1CE2/40XX_Nplus0/
407X_T3_like_no_Vd1Vd2/
```

with the following exact objects:

| File | Blob prefix |
|---|---|
| `4073_boundary_loss_framework.md` | `f3f0395748f5` |
| `4074_L_Full_branch.md` | `880b59ec8d3c` |
| `4075_Tminus_low_lower_branch_obligations.md` | `ebe2b65f8840` |
| `4078_left_L_family_completion.md` | `f1323325b069` |
| `4079_first_Full_branch.md` | `c66eea05277d` |
| `407a_left_Thigh_branch_completion.md` | `aa5cb1a6dc63` |
| `407c_rigor_completion_details.md` | `c80243f67124` |
| `407d_rigor_final_assembly.md` | `a6ef81f787c4` |

### 3.6 Admissible-set derivation

`02b_admissible_set_derivation.tex` now supplies the omitted calculation:

- the explicit triangular-hull enclosing equilateral triangle;
- the four edge-normal support values;
- the active support patterns;
- derivation of `F_L`, `F_T`, and `F_S`;
- the selected connected-component conditions `c<=2M` and `c<=1/2`;
- the exact radial envelope.

### 3.7 Strategy 4 certificate

The mixed-overlap certificate is no longer described as an optional replay.
`06a_strategy4_exact_certificate.tex` formally incorporates:

- the six sparse-data shards;
- the canonical transcript hash
  `dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485`;
- the exact rational-function derivation verifier;
- the exact global Bernstein verifier;
- the denominator nonvanishing conditions;
- the missing geometric implication from residual positivity to common tangent
  support and cap intersection.

The certificate uses exact integers, rationals, and `Q(sqrt(3))`. No
floating-point or interval computation is an active dependency.

## 4. Body-interface provenance

### 4.1 Structural reduction

`prop:body-structural-reduction` summarizes:

- distinct center and vertex roles;
- exhaustive CE0/CE1/CE2 classification;
- exhaustive Vd0/Vd1/Vd2/T3-like classification;
- actual maximal reaches and the definition of `N_+`;
- singleton-gap convention;
- strict handoff selection preserving exact-one or at-least-two criticality;
- unique center midpoint in CE1/CE2;
- short-role identity `q=N_++m`;
- the exhaustive routing table.

These are proved in `02_structural_reductions.tex` and the `1XXX`, `2109`, and
`2530` proof packages.

### 4.2 Local enclosure and transfers

The body’s explicit minimum-side formula is proved in
`02b_admissible_set_derivation.tex` and agrees with
`proof/.../2004_admissible_set.md`.

The canonical transfer notation comes from `201d`:

```text
g_c(x)=max{y:(1-x,y,c) in A},
widehat g_c(x)=min{g_c(x),x},
f^vee(a)=1-f(1-a).
```

The corrected center-free and center-assisted statements are in `02a` and the
repaired `2019` source.

### 4.3 Signed center

The variables

```text
0<R<1, W=1-R,
E=sqrt(1-RW), eta=1-E, P=E(1-E),
Delta_R=P-alpha-W delta,
Delta_L=P-R alpha-delta
```

and all trace, exit, midpoint, and boundary-contribution formulas are proved in
`04a_signed_center_calculus.tex` and proof source `2109`.

## 5. Strategy provenance and audit status

### Strategy 1

Active sources:

- `2500_boundary_length_bounds.md`;
- `2510_skeleton_length_bounds.md`;
- `2530_common_CE1_CE2_budget_lemmas.md`;
- `03_strategy1_length.tex`;
- `04b_common_CE1_CE2_budgets.tex`.

Audit result: the terminal sums are valid. The reader master deficit now states
the previously omitted hypothesis that every unlisted row has contribution at
most one.

### Strategy 2

Active sources include `2004`, `2010`--`2019`, `2107`--`2110`, `4013`, the
complete `407X` supplement, `4105`--`4107`, `413X`, and `4143`--`4149`.

Audit result: the endpoint formulas and scalar inequalities are consistent with
the proof package. The paper now preserves:

- actual versus selected criticality;
- center-free path hypotheses;
- exact endpoint residuals;
- the CE1 affine/threshold ending;
- the CE2 at-least-one-threshold dichotomy;
- all four T3 labels;
- the Vd-specific radial margin;
- explicit open replacements.

### Strategy 3

Active sources: `3175`, `3205`, `3208`, and `05_strategy3_area.tex`.

Audit result: the two orientation normal forms, local square losses, reflection
normalization, and both cyclic sums are complete and valid.

### Strategy 4

Active sources: the `3105X_self_contained_direct_Vd0_nine_point` package,
`06_strategy4_ab_core.tex`, and `06a_strategy4_exact_certificate.tex`.

Audit result: the direct forcing, Newton placement, cap chain, and adjacent
overlaps are analytic. The two mixed overlaps are exact computer-assisted
claims with authenticated input and exact verification algorithms. The source
review found no arithmetic-model or Bernstein-conversion defect. The verifier
was not executed during this edit, so reproducibility is documented rather
than newly certified by a run log.

## 6. Assembly invariants

The final proof retains all of the following.

1. `N_+` is computed from actual maximal reaches.
2. Selected handoffs are lower demands.
3. Singleton gaps are retained.
4. Center-assisted handoffs use residual maps.
5. Every path-budget internal edge is center-free.
6. The raw zero-radial map is not confused with its capped identity.
7. The CE1 and CE2 one-gap scalar endings remain different.
8. The T3-like endpoint theorem keeps all four exact labels.
9. The nonadjacent Vd route keeps its own-radial margin.
10. The CE2 one-Vd branch uses the complete placement assembly.
11. The Strategy 4 mixed overlaps use the authenticated exact certificate.

## 7. Build and PDF status

The requested repair was source-only. No XeLaTeX or PDF compilation was
performed. `main.pdf` was not modified and must be treated as stale relative to
this branch. The body-page label remains in the source, but the 20-page limit
must be rechecked in a later authorized build.
