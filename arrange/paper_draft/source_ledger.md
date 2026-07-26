# Private source ledger

This is an authoring and verification record, not a reader-facing proof. Paths
are relative to the repository root. Only sources with their own recorded
proof status may support a manuscript theorem.

## Persistent manuscript artifacts

| Artifact | Role |
|---|---|
| `arrange/paper_draft/main.tex` | AMS preamble, metadata, body assembly, and appendix assembly. |
| `arrange/paper_draft/01_introduction.tex` | Theorem, geometric dictionary, exhaustive routing table, three certificate classes, and the all-Vd0 gap-rank matrix. |
| `arrange/paper_draft/02_structural_reductions.tex` | Common geometry and exhaustive structural reduction. |
| `arrange/paper_draft/04a_signed_center_calculus.tex` | Signed CE1/CE2 center model, common actual-row interface, and CE2 threshold clause. |
| `arrange/paper_draft/02a_universal_calculus.tex` | Enclosure gauge, universal radical, interval residuals, generalized handoffs, boundary-path budget, selected-$T_+$ curve, and threshold routing. |
| `arrange/paper_draft/03_strategy1_length.tex` | Complete trace-budget proof, using the signed variables directly. |
| `arrange/paper_draft/04b_common_CE1_CE2_budgets.tex` | Master perimeter deficit, short-role count, small CE2 slack, and three-short-role theorem. |
| `arrange/paper_draft/04_strategy2_reader.tex` | Reader-facing gap-rank kernel, common CE2 two-gap application, and the sign-dependent one-gap clauses. |
| `arrange/paper_draft/05_strategy3_area.tex` | Complete area proof with area loss denoted by $\mathcal L$, disjoint from the propagation maps $G_c$. |
| `arrange/paper_draft/06_strategy4_reader.tex` | Direct forcing, Newton inner reduction, cap chain, four-overlap certificate, and enclosure contradiction using the universal gauge $\Lambda$. |
| `arrange/paper_draft/07_exhaustive_assembly.tex` | Final routing-table assembly. |
| `arrange/paper_draft/04c_short_Vd_placements.tex` | Quarter radial envelope, rational T3-like profile, Vd1 profile, common adjacent rescuer, and shortened adjacent/nonadjacent Vd placements. |
| `arrange/paper_draft/04_strategy2_exact_demand.tex` | Exact admissible-set catalogue, CE1 terminal algebra, one-side and paired endpoint certificates, and the irreducible `407X` scalar audit. |
| `arrange/paper_draft/06_strategy4_ab_core.tex` | Exact strict $AB$ frontier, forcing signs, Newton placement, ray order, and overlap proofs. |
| `arrange/paper_draft/appendix_symbols.tex` | Compact table of cross-section symbols. |
| `arrange/paper_draft/appendix_exact_mixed_overlap.tex` | Mixed-overlap proof, exact Bernstein identities, digest, and replay record. |
| `arrange/paper_draft/main.pdf` | Derived manuscript; rebuilt after every accepted source change. |

The historical half-edge $1/3$ envelope remains proved in the proof corpus but
its former standalone manuscript source was removed.  The active adjacent Vd
proof uses the global quarter envelope instead.

Build from `arrange/paper_draft` with

```text
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

No bibliography is required. Every figure is explanatory; no proof depends on
visual inspection.

## Universal structural and local sources

| Source | Status | Principal manuscript use |
|---|---|---|
| `proof/0XXX_main/0000_main_theorem.md` | Proven | `thm:main` and final assembly. |
| `proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md` | Proven | Open/closed/scaled equivalence. |
| `proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md` | Proven | Exhaustive CE0/CE1/CE2 classification. |
| `proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md` | Proven | Exhaustive Vd0/Vd1/Vd2/T3-like classification and T3-like translation. |
| `proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md` | Proven | Strict handoffs and preservation of actual supercritical patterns. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md` | Proven | Exact local gauge sublevel set, contact cells, and radial envelope. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md` | Proven | Exact capped map, monotonicity, extensivity, duality, and four labels. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2016_universal_Tplus_normal_form.md` | Proven | Selected-$T_+$ normal form and chord bounds. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2017_threshold_routing.md` | Proven | One-hit and two-threshold routing. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md` | Proven | Diameter transfer and class-independent adjacent-rescuer theorem. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md` | Proven | Residual interval operator, generalized handoff, radial component form, and boundary-path budget. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201a_equilateral_enclosure_and_radical_calculus.md` | Proven | Common enclosure gauge, radical calculus, and four-frontier atlas. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md` | Proven | Global $c_{\max}(p,h)\le1-h/4$ estimate. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md` | Proven | Own-radial and supported-arm endpoint margins for Vd1/Vd2 roles. |
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md` | Proven | Signed center traces, class sign, boundary contribution, and six exits. |
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2110_common_CE2_two_gap_application.md` | Proven | One geometric application of the paired endpoint theorem for both all-Vd0 two-gap cells. |

## Strategy 1 sources

| Source | Status | Principal manuscript use |
|---|---|---|
| `proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md` | Proven | Boundary trace table. |
| `proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md` | Proven | Center, positive-support, no-support, and supercritical skeleton caps. |
| `proof/2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md` | Proven | Master perimeter deficit, small CE2 slack, $q=N_++m$, and three-short-role theorem. |
| `proof/4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md` | Proven | Two supercritical rows force a third short rescuer. |

The diagonal package `2520` remains proved but is not an active manuscript
dependency.

## Strategy 2 branch sources

| Source | Status | Principal manuscript use |
|---|---|---|
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md` | Proven | The rank-one $N_+=0$ all-Vd0 endpoint loss. |
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2108_CE2_two_endpoint_capped_loss.md` | Proven | The coupled scalar certificate underlying `2110`. |
| `proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md` | Proven | The $N_+=0$ all-Vd0 gap-rank row. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4105_CE1_CE2_one_gap_five_row_interface.md` | Proven | Common five-row actual induction and duality reduction. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4106_CE1_one_gap_five_map_completion.md` | Proven | CE1 selected-$T_+$ scalar clause and terminal algebra. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4107_CE2_one_gap_five_map_completion.md` | Proven | CE2 total-slack and two-threshold clause. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md` | Proven | The $N_+=1$ all-Vd0 gap-rank row. |
| `proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md` | Proven | Irreducible four-label T3-like endpoint audit. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md` | Proven | Rational T3-like local profile and common-rescuer invocation. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md` | Proven | Vd1 local profile and common-rescuer invocation. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md` | Proven | Stronger quarter center margin and global radial envelope. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md` | Proven | Interval residuals, diameter transfer, and one Vd radial margin. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md` | Proven | Vd1 pair replacement. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md` | Proven | Exhaustive one-Vd placement assembly. |

## Strategies 3 and 4

The proved local square-loss source `3205_unconditional_local_square_loss.md`
supports `thm:local-square-loss`.  The T3-like translation in `1201` and the
direct loss source `3175_direct_T3_like_area_loss.md` support
`thm:t3-direct-loss`.  The cyclic certificates `3174` and `3208` are presented
together as `lem:cyclic-area-loss`.

The active Strategy 4 source remains the self-contained direct nine-point
package
`proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/`,
with the strict supercritical $AB$ frontier in
`proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md`.
The body owns the universal enclosure gauge, the cap-chain lemma, witness
enclosure, center-independent contradiction, and terminal routing.  The
Strategy 4 appendix owns the exact frontier, moving-circle signs, Newton
placement, adjacent overlaps, Gram reduction, eight core polynomials, and all
twenty global Bernstein identities.  The replay scripts authenticate those
exact identities rather than adding hypotheses.

## Deliberate nondependencies

No theorem depends on a source recorded as Strategy, Empirical, Experiment,
Lemma target, or Failed. In particular:

- the CE2 two-gap state is not replaced by two independent one-gap calls;
- the CE1 scalar one-gap proof is not replaced by the CE2 two-threshold lemma;
- the historical half-edge $1/3$ envelope is not an active manuscript
  dependency and is never used outside its proved domain;
- the optional reduction `4104` is not used;
- the optional disk-plus-one-point Strategy 4 subregion is not used;
- the failed five-point route and the false global skeleton claim are excluded;
- numerical scripts are cross-checks unless a proved exact certificate is
  recorded in a source theorem.
