# Private source ledger

This is an authoring and verification record, not a reader-facing proof. Paths
are relative to the repository root. Only sources with their own recorded
proof status may support a manuscript theorem.

## Persistent manuscript artifacts

| Artifact | Role |
|---|---|
| `arrange/paper_draft/main.tex` | AMS preamble, metadata, body assembly, and appendix assembly. |
| `arrange/paper_draft/01_introduction.tex` | Theorem statement, definitions, routing table, and single compact proof guide. |
| `arrange/paper_draft/02_structural_reductions.tex` | Common geometry and exhaustive structural reductions. |
| `arrange/paper_draft/03_strategy1_length.tex` | Complete Strategy 1 body proof. |
| `arrange/paper_draft/04_strategy2_reader.tex` | Reader-facing Strategy 2 proof with one signed five-row chain and two scalar clauses. |
| `arrange/paper_draft/04a_signed_center_calculus.tex` | Body proof of the signed center model, common one-gap interface, and short CE2 threshold result. |
| `arrange/paper_draft/04b_common_CE1_CE2_budgets.tex` | Common perimeter deficit, small CE2 slack, total slack, and three-short-role theorem. |
| `arrange/paper_draft/04c_short_Vd_placements.tex` | Complete shortened adjacent and nonadjacent one-Vd1/Vd2 placements and common adjacent rescuer. |
| `arrange/paper_draft/04_strategy2_exact_demand.tex` | Exact admissible-set catalogue, CE1 terminal algebra, T3-like branches, and retained local replacement lemmas. |
| `arrange/paper_draft/04a_strategy2_half_edge_envelope.tex` | Half-edge radial envelope, exact domain counterexample, and compatibility reference to the signed adjacent proof. |
| `arrange/paper_draft/05_strategy3_area.tex` | Complete Strategy 3 proof with one cyclic area-loss certificate. |
| `arrange/paper_draft/06_strategy4_reader.tex` | Strategy 4 cap-chain, enclosure, contradiction, and terminal routing. |
| `arrange/paper_draft/06_strategy4_ab_core.tex` | Exact Strategy 4 frontier, forcing, Newton-placement, ray-order, and overlap proofs. |
| `arrange/paper_draft/07_exhaustive_assembly.tex` | Compact final routing-table assembly. |
| `arrange/paper_draft/appendix_symbols.tex` | Compact table of nonstandard cross-section symbols. |
| `arrange/paper_draft/appendix_exact_mixed_overlap.tex` | Mixed-overlap proof, exact Bernstein identities, digest, and replay record. |
| `arrange/paper_draft/main.pdf` | Derived manuscript; rebuild whenever the LaTeX assembly changes. |

Build from `arrange/paper_draft` with

```text
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

No bibliography is required. Every figure is explanatory; no proof depends
on visual inspection.

## Common structural sources

| Source | Status | Principal manuscript use |
|---|---|---|
| `proof/0XXX_main/0000_main_theorem.md` | Proven | `thm:main` and final assembly. |
| `proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md` | Proven | open/closed/scaled equivalence. |
| `proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md` | Proven | exhaustive CE0/CE1/CE2 classification. |
| `proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md` | Proven | exhaustive Vd0/Vd1/Vd2/T3-like classification and T3-like translation. |
| `proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md` | Proven | strict handoffs and selected-row preservation. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md` | Proven | self-midpoint forcing. |
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md` | Proven | exact unique center midpoint. |

## Strategy 1 sources

| Source | Status | Principal manuscript use |
|---|---|---|
| `proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md` | Proven | boundary trace table. |
| `proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md` | Proven | center, positive-support, no-support, and supercritical skeleton caps. |
| `proof/2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md` | Proven | retained historical result; no longer used by the manuscript proof. |
| `proof/2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md` | Proven | `lem:signed-perimeter-deficit`, `lem:signed-small-slack`, `lem:signed-endpoints-dominate-slack`, and `thm:three-short-roles`. |
| `proof/4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md` and `4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md` | Proven | common perimeter-budget corollaries. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md` and `4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md` | Proven | common perimeter-budget corollaries. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md` | Proven | three-short-role corollary. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md` | Proven | Vd2 one-third-cap perimeter corollary. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md` | Proven | three-short-role mixed branch. |
| `proof/4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md` | Proven | two supercritical rows force a third short rescuer. |

## Strategy 2 local calculus

| Source | Status | Principal manuscript use |
|---|---|---|
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md` | Proven | `prop:exact-admissible-set` and radial envelope. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md` | Proven | outgoing fibers and universal diameter upper bound. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md` | Proven | strict supercritical envelope. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md` | Proven | four-label capped map, monotonicity, extensivity, and duality. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md` | Proven | low-root bounds, threshold trigger, and half-edge radial envelope. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2013_T3_like_side_tradeoff.md` | Proven | T3-like local normal form and side tradeoff. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md` | Proven | Vd1/Vd2 corner normal form and $a+b<1/2$. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2015_Vd2_neighbor_midpoint_cap.md` | Proven | Vd2 neighboring-midpoint $a+b<1/3$. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2016_universal_Tplus_normal_form.md` | Proven | universal selected-$T_+$ curve and chord estimates. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2017_threshold_routing.md` | Proven | one-hit and two-threshold routing. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md` | Proven | `lem:signed-diameter-transfer` and `lem:signed-adjacent-rescuer`. |

## Signed CE1/CE2 center and gap sources

| Source | Status | Principal manuscript use |
|---|---|---|
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md` | Proven | `prop:signed-center-normal-form` and `cor:signed-center-boundary`. |
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md` | Proven | CE1 legacy-variable adapter. |
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md` | Proven | CE2 legacy-variable adapter and automatic coupling. |
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md` | Proven | common one-active-gap endpoint loss. |
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2108_CE2_two_endpoint_capped_loss.md` | Proven | genuinely coupled two-gap endpoint loss. |
| `proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md` | Proven | signed no-gap/one-gap/two-gap $N_+=0$ proof. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4105_CE1_CE2_one_gap_five_row_interface.md` | Proven | `prop:signed-one-gap-interface`. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4106_CE1_one_gap_five_map_completion.md` | Proven | CE1 selected-$T_+$ scalar clause and terminal algebra. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4107_CE2_one_gap_five_map_completion.md` | Proven | `lem:signed-ce2-two-threshold` and short CE2 scalar clause. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4102_CE2_two_gap_completion.md` | Proven | CE2 rank-two two-gap completion. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md` | Proven | signed gap-pattern assembly and `prop:nplus-one-all-vd0`. |

## T3-like and Vd1/Vd2 placement sources

| Source | Status | Principal manuscript use |
|---|---|---|
| `proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4131_midpoint_forcing_reduction.md` and `4132_CE1CE2_exactly_one_T3_like_boundary_obstruction.md` | Proven | local T3-like input to the common adjacent-rescuer theorem. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md` | Proven | local Vd1 input to the common adjacent-rescuer theorem. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md` | Proven | `lem:signed-vd-adjacent-placement`; long outer-ratio calculation replaced by common slack bounds. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md` | Proven | `lem:signed-vd-nonadjacent-placement`; CE2 comparison polynomial replaced by total slack and diameter transfer. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md` | Proven | Vd1 pair replacement. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md` | Proven | `prop:signed-ce2-one-vd-placements`. |

## Strategies 3 and 4

The proved local square-loss source `3205_unconditional_local_square_loss.md`
supports `thm:local-square-loss`.  The T3-like translation in `1201` and the
direct loss source `3175_direct_T3_like_area_loss.md` support
`thm:t3-direct-loss`.  The proved cyclic certificates `3174` and `3208` are
presented together as `lem:cyclic-area-loss`, with terminal routing in
`prop:area-branches`.

The active Strategy 4 source remains the self-contained direct nine-point
package
`proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/`,
with the strict supercritical $AB$ frontier in
`proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md`.
The body owns `lem:reader-cap-chain`, `thm:reader-witness-enclosure`,
`thm:reader-zero-gap-obstruction`, and `prop:reader-ab-core-branches`.
The technical appendix owns `lem:technical-newton-reduction`,
`prop:technical-four-overlaps`, and `lem:exact-mixed-cap-overlaps`; the replay
scripts are exact verification interfaces rather than additional hypotheses.
The older `3103X` and `3104X` routes remain proven predecessors but are not
active manuscript dependencies.

## Deliberate nondependencies

No theorem depends on a source recorded as Strategy, Empirical, Experiment,
Lemma target, or Failed. In particular:

- the CE2 two-gap theorem is not replaced by two independent one-gap calls;
- the CE1 scalar one-gap proof is not replaced by the CE2 two-threshold lemma;
- the half-edge radial envelope is never used outside its stated
  $p\ge1/2$ domain;
- the optional reduction `4104` is not used;
- the failed May 25 CE1/CE2 five-point route and the false global skeleton
  claim are excluded;
- numerical scripts are cross-checks unless a proved exact certificate is
  recorded in a source theorem.
