# Paper-to-Proof Crosswalk

Branch: `agent/body-appendix-separation`  
Paper root: `arrange/paper_draft/`  
Proof-package root: `proof/`  
Last structural audit: 2026-07-28

## 0. Purpose and authority

This document records, at theorem and proof-module level, which part of the
paper is supported by which numbered Markdown proof source. It is a maintenance
crosswalk, not an additional proof.

The authority order is:

1. a numbered `proof/**/*.md` source with a status sufficient for the claimed
   conclusion, normally `Status: Proven`;
2. a TeX appendix that faithfully reorganizes those numbered sources;
3. a reader-facing body statement that cites the appendix result;
4. navigation files such as indexes and this crosswalk.

The exact computer-assisted part of Strategy 4 additionally uses the code and
sparse data listed in Section 9 below. Those files are proof objects only as a
single authenticated certificate together with the mathematical reductions in
`31055` and `31056`.

### Dependency codes used below

| Code | Meaning |
|---|---|
| **P** | Primary status-bearing proof source for the stated paper result |
| **S** | Supporting lemma or calculation used by the primary source |
| **A** | Assembly source proving that listed terminal branches are exhaustive |
| **E** | Exact electronic certificate object: code, data, or authenticated transcript |
| **N** | Navigation/reference only; not itself a proof |
| **X** | Historical, optional, failed, or otherwise inactive source |

All repository links below are relative to this file in `arrange/`.

---

# 1. Paper assembly and top-level theorem

## 1.1 `paper_draft/main.tex`

**Paper function.** Defines the AMS document, loads the seven reader-facing
sections, places `page:proof-body-end`, and then loads the verification
appendices.

**Direct proof connection.** No mathematical claim is proved by `main.tex`.
It is the assembly layer for:

- [main theorem package](../proof/0XXX_main/0000_main_theorem.md) — **P/A**;
- [proof-tree index](../proof/0XXX_main/0001_proof_tree_index.md) — **N**;
- [status and dependency table](../proof/0XXX_main/0002_status_and_dependencies.md) — **N**.

**Important maintenance rule.** A TeX input must not be removed from
`main.tex` unless every body statement depending on it is either removed or
redirected to another complete proof source.

## 1.2 Abstract

The abstract's four mechanisms correspond to:

| Abstract phrase | Paper section | Primary proof packages |
|---|---|---|
| trace deficit | `03_strategy1_reader.tex` | `2500`, `2510`, `2530`, and terminal length packages |
| monotone transfer | `04_strategy2_summary.tex` | `2004`, `2010`-`2019`, `2107`-`2110`, `4013`, `407X`, `410X`, `413X`, `414X` |
| area loss | `05_strategy3_reader.tex` | `3171`, `3174`, `3175`, `3201`, `3205`, `3208` |
| nine-point support obstruction | `06_strategy4_reader.tex` | `31050`-`31059` and exact `3105X_computation` certificate |

The statement that the final mixed overlaps are exact computer-assisted
claims is supported by [31055](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31055_rational_radial_envelopes_and_mixed_reduction.md),
[31056](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31056_global_analytic_mixed_positivity.md),
and the certificate objects in Section 9 — **P/E**.

---

# 2. Reader-facing body: section-by-section map

## 2.1 `paper_draft/01_introduction.tex` — Proof Architecture

### `thm:main` — Main theorem

**Paper statement.** The side-one regular hexagon cannot be covered by seven
open unit equilateral triangles.

**Primary source.** [0000_main_theorem.md](../proof/0XXX_main/0000_main_theorem.md) — **P/A**.

**Supporting structural sources.** `1003`, `1101`, `1201`, `1214`, `2530`, and
all terminal packages listed in Sections 4-8 below — **S**.

### `cor:expanded-closed` — Expanded closed formulation

**Paper statement.** For every `L>1`, the regular side-`L` hexagon is not
covered by seven closed unit equilateral triangles.

**Primary source.** [1003_open_unit_vs_shrunken_closed_equivalence.md](../proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md) — **P**.

### Seven distinct roles

**Paper content.** The center `O` and six vertices force distinct role
triangles `T_C,T_0,...,T_5`.

**Primary source.** The opening argument of
[0000_main_theorem.md](../proof/0XXX_main/0000_main_theorem.md) — **P**.

**Supporting conventions.** [1001_geometry_objects.md](../proof/1XXX_foundations/10XX_global_conventions/1001_geometry_objects.md) — **S**.

### Finite dictionary: CE0/CE1/CE2

**Paper content.** The center role has exactly zero, one, or two
positive-length boundary traces.

**Primary source.** [1101_CE_classification.md](../proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md) — **P**.

**Supporting source.** [1100_C_triangle_overview.md](../proof/1XXX_foundations/11XX_C_triangle/1100_C_triangle_overview.md) — **N/S**.

### Finite dictionary: Vd0/Vd1/Vd2/T3-like

**Paper content.** The four exhaustive vertex-role classes are described by
the outside-vertex and adjacent-support counts `(o,n)`.

**Primary source.** [1201_V_triangle_types.md](../proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) — **P**.

**Supporting sources.**

- [1200_V_triangle_overview.md](../proof/1XXX_foundations/12XX_V_triangle/1200_V_triangle_overview.md) — **N/S**;
- [1213_T3_like_nonsupercritical.md](../proof/1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md) — **S**.

### Actual reaches, selected demands, and `N_+`

**Paper content.** `N_+` is defined from actual maximal reaches
`A_i+B_i>1`; lowercase data are selected lower demands.

**Primary sources.**

- [1202_local_coordinates_abc.md](../proof/1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md) — **P/S**;
- [1212_vertex_rows_and_Nplus.md](../proof/1XXX_foundations/12XX_V_triangle/1212_vertex_rows_and_Nplus.md) — **P/S**;
- [1214_strict_boundary_handoff_selection.md](../proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) — **P**.

### Boundary gaps and singleton gaps

**Paper content.** The missed set `[B_i,1-A_{i+1}]` is retained when it is a
singleton because the role triangles are open.

**Primary sources.**

- [1208_boundary_degeneracies.md](../proof/1XXX_foundations/12XX_V_triangle/1208_boundary_degeneracies.md) — **P/S**;
- [1214_strict_boundary_handoff_selection.md](../proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) — **S**;
- [2019_interval_component_and_path_budget.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md) — **S**.

### Short roles and `q=N_++m`

**Primary source.** [2530_common_CE1_CE2_budget_lemmas.md](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md) — **P**.

**Supporting classification sources.** `1201`, `1213`, `2014`, and `2510` — **S**.

### `tab:routing` — Exhaustive routing table

**Primary assembly source.** [0000_main_theorem.md](../proof/0XXX_main/0000_main_theorem.md) — **A**.

**Navigation cross-check.** [0001_proof_tree_index.md](../proof/0XXX_main/0001_proof_tree_index.md) — **N**.

**Branch-by-branch terminal sources.** See Section 8 of this crosswalk.

### Four mechanisms overview

This is explanatory rather than a separate theorem. Its proof content is the
union of the Strategy 1-4 packages listed below.

---

## 2.2 `paper_draft/02_reader_framework.tex` — Geometric Interfaces

### `prop:body-structural-reduction`

The proposition packages the following statements:

| Component of the proposition | Primary proof source | Role |
|---|---|---|
| seven distinct roles | [0000](../proof/0XXX_main/0000_main_theorem.md) | **P** |
| CE0/CE1/CE2 exhaustiveness | [1101](../proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md) | **P** |
| Vd0/Vd1/Vd2/T3-like exhaustiveness | [1201](../proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) | **P** |
| exact-one/at-least-two selected criticality | [1214](../proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) | **P** |
| CE1/CE2 unique radial midpoint | [2100](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md) | **P** |
| short-role identity `q=N_++m` | [2530](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md) | **P** |
| disjoint exhaustive routing | [0000](../proof/0XXX_main/0000_main_theorem.md), [0001](../proof/0XXX_main/0001_proof_tree_index.md) | **A/N** |

The full TeX derivation is in `02_structural_reductions.tex`; see Section 3.2.

### `prop:body-admissible-description`

**Paper statement.** Gives the exact least equilateral enclosure side for
`K(a,b,c)` and therefore the exact local admissible set `mathcal A`.

**Primary source.** [2004_admissible_set.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md) — **P**.

**Supporting enclosure tools.**

- [201a_equilateral_enclosure_and_radical_calculus.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201a_equilateral_enclosure_and_radical_calculus.md) — **S**;
- [2600_minimum_enclosing_triangle_tools.md](../proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2600_minimum_enclosing_triangle_tools.md) — **S**;
- [2607_minimal_enclosing_equilateral_quadrilateral_lemma.md](../proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2607_minimal_enclosing_equilateral_quadrilateral_lemma.md) — **S**.

**TeX verification.** `02b_admissible_set_derivation.tex`.

### `prop:body-transfer-interface`

The four items map as follows:

| Paper item | Primary source | Supporting sources |
|---|---|---|
| raw outgoing map and actual-V triangle bound | [2007_max_b_map.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md) | `2004`, `201d` |
| capped nonsupercritical map and complement dual | [2011_capped_demand_map.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md) | `2004`, `2007` |
| center-assisted residual transfer | [2019_interval_component_and_path_budget.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md) | `201d` |
| strict-supercritical outgoing envelope | [2010_free_supercritical_max_b.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md) | `2004`, `2007` |
| relaxed composition | [201d_raw_and_relaxed_g_chains.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md) | `2019` |

**Critical hypothesis map.** The unconditional statement is
`B<g_c^{sc}`. The complementary next-V-triangle statement requires a center-free
outgoing edge. The corrected path hypothesis is carried by `2019`.

### `prop:body-signed-center-interface`

**Primary source.** [2109_signed_CE1_CE2_center_normal_form.md](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md) — **P**.

**Supporting exact-formula sources.**

- [2105_CE1_exact_formulas.md](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md) — **S**;
- [2106_CE2_exact_formulas.md](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md) — **S**;
- [2100_CE1_CE2_exactly_one_midpoint_lemma.md](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md) — **S**;
- [2530_common_CE1_CE2_budget_lemmas.md](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md) — **S**, for the center boundary caps used later.

**TeX verification.** `04a_signed_center_calculus.tex`.

---

## 2.3 `paper_draft/03_strategy1_reader.tex` — Trace Budgets

### `prop:body-trace-register`

| Trace-cap V triangle in the paper | Primary proof source |
|---|---|
| CE1/CE2 center on the full skeleton | [2510_skeleton_length_bounds.md](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md) |
| supercritical vertex role on the skeleton | [2510_skeleton_length_bounds.md](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md) |
| positive-adjacent-support role on the skeleton | [2510_skeleton_length_bounds.md](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md) |
| nonsupercritical no-support role on the skeleton | [2510_skeleton_length_bounds.md](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md) |
| CE1/CE2 center perimeter caps | [2530_common_CE1_CE2_budget_lemmas.md](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md), using `2109` |
| supercritical Vd0 perimeter cap | [2500_boundary_length_bounds.md](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md) |
| Vd1/Vd2 perimeter cap | [2500](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md), [2014](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md) |
| nonsupercritical Vd0 cap | [2500_boundary_length_bounds.md](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md) |
| T3-like cap | [2500](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md), [1213](../proof/1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md) |

### Master perimeter deficit and three-short-role sum

**Primary source.** [2530_common_CE1_CE2_budget_lemmas.md](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md) — **P**.

**Supporting sources.** `2500`, `2510`, `2109` — **S**.

### `prop:body-length-branches`

| Paper branch | Primary terminal source | Notes |
|---|---|---|
| CE0, `N_+=0` | [3010_CE0_perimeter_length_obstruction.md](../proof/3XXX_CE0/30XX_Nplus0/3010_CE0_perimeter_length_obstruction.md) | cyclic perimeter sum |
| CE0, `N_+=1`, some Vd1/Vd2 | [3141_CE0_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md](../proof/3XXX_CE0/31XX_Nplus1/314X_exists_Vd1_Vd2/3141_CE0_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) | master deficit |
| CE1/CE2, at least three short roles | [2530](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md) | skeleton sum |
| CE1, `N_+=0`, some Vd1/Vd2 | [4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md](../proof/4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | perimeter |
| CE2, `N_+=0`, some Vd1/Vd2 | [4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md](../proof/4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | perimeter |
| CE1, `N_+=1`, one Vd1/Vd2 | [4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md](../proof/4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) | CE1 is removed before CE2 placement analysis |
| at least two Vd-type short roles, where routed separately | [4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md](../proof/4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md) | compatible with short-role routing |
| at least two T3-like roles | [4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md](../proof/4XXX_CE1CE2/41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md) | also subsumed by common budget where applicable |
| CE2 Vd2 neighboring-midpoint subcase | [4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md) | Strategy 1 part of hybrid V triangle |
| CE2 additional positive-support subcase | [414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md) | three-short-role skeleton |
| CE1/CE2, `N_+>=2` | [4200_CE1_CE2_skeleton_length_route.md](../proof/4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md) | midpoint rescue creates the extra short role |

The full calculations are reorganized in `03_strategy1_length.tex` and
`04b_common_CE1_CE2_budgets.tex`.

---

## 2.4 `paper_draft/04_strategy2_summary.tex` — Monotone Transfer Certificates

### All-Vd0 rank-zero strict cycle

**Primary source.** [4013_boundary_loss_index.md](../proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md) — **P/A**.

**Transfer support.** `2011`, `2019`, `201d` — **S**.

### `prop:body-all-vd0-endpoints`, item 1 — one active center gap

**Primary inequality.** [2107_one_side_capped_loss.md](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md) — **P**.

**Geometric application and path closure.** [4013_boundary_loss_index.md](../proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md) — **A/P**.

**Path hypothesis.** [2019_interval_component_and_path_budget.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md) — **S**.

### `prop:body-all-vd0-endpoints`, item 2 — two CE2 active gaps

**Primary inequality.** [2108_CE2_two_endpoint_capped_loss.md](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2108_CE2_two_endpoint_capped_loss.md) — **P**.

**Geometric application.** [2110_common_CE2_two_gap_application.md](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2110_common_CE2_two_gap_application.md) — **P/A**.

### `prop:body-five-row-certificate`

| Paper component | Proof source |
|---|---|
| unique supercritical V triangle and exact gap setup | [4101_CE1CE2_Nplus1_all_Vd0_strategy.md](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md) |
| actual-V triangle five-map propagation and `A_0>=Z`, `A_0<1-H` | [4105_CE1_CE2_one_gap_five_row_interface.md](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4105_CE1_CE2_one_gap_five_row_interface.md) |
| CE1 affine/threshold completion | [4106_CE1_one_gap_five_map_completion.md](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4106_CE1_one_gap_five_map_completion.md) |
| CE2 at-least-one-threshold completion | [4107_CE2_one_gap_five_map_completion.md](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4107_CE2_one_gap_five_map_completion.md) |
| selected `T_+` normal form and chords | [2016_universal_Tplus_normal_form.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2016_universal_Tplus_normal_form.md) |
| threshold routing | [2017_threshold_routing.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2017_threshold_routing.md) |
| terminal diameter comparison | [2018_diameter_transfer_and_adjacent_rescuer.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md) |

### `def:body-t3-endpoint-state` and `prop:body-t3-endpoint`

**Reduction sources.**

- [4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md) — **P/S**;
- [4072_support_isolation_after_T0_T3_like.md](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4072_support_isolation_after_T0_T3_like.md) — **P/S**;
- [4073_boundary_loss_framework.md](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4073_boundary_loss_framework.md) — **P reduction**.

**Four-label terminal sources.**

- [4074_L_Full_branch.md](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4074_L_Full_branch.md) — **P**;
- [4075_Tminus_low_lower_branch_obligations.md](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4075_Tminus_low_lower_branch_obligations.md) — **P**;
- [4078_left_L_family_completion.md](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4078_left_L_family_completion.md) — **P**;
- [4079_first_Full_branch.md](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4079_first_Full_branch.md) — **P**;
- [407a_left_Thigh_branch_completion.md](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407a_left_Thigh_branch_completion.md) — **P**;
- [407c_rigor_completion_details.md](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407c_rigor_completion_details.md) — **P/S**;
- [407d_rigor_final_assembly.md](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407d_rigor_final_assembly.md) — **A**;
- [4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md) — **N/A summary**.

**Exact map source.** [2011_capped_demand_map.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md) — **S**.

### `prop:body-special-terminal-certificates`, item 1 — adjacent rescuer

**Common geometric theorem.** [2018_diameter_transfer_and_adjacent_rescuer.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md) — **P**.

**T3-like branch.**

- [4131_midpoint_forcing_reduction.md](../proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4131_midpoint_forcing_reduction.md) — **P/S**;
- [4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md](../proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md) — **P**;
- [4130_CE1CE2_exactly_one_T3_like_index.md](../proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md) — **A/N**.

**Vd1 neighboring rescuer branch.** [4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md) — **P**.

### `prop:body-special-terminal-certificates`, item 2 — adjacent Vd placement

**Primary source.** [4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md) — **P**.

**Supporting sources.**

- [201b_quarter_radial_envelope.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md) — **S**;
- [201c_Vd_corner_radial_margins.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md) — **S**;
- [2014_Vd1_Vd2_corner_normal_form.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md) — **S**;
- [2530_common_CE1_CE2_budget_lemmas.md](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md) — **S**.

### `prop:body-special-terminal-certificates`, item 3 — nonadjacent Vd placement

**Primary source.** [4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md) — **P**.

**Supporting source.** [201c_Vd_corner_radial_margins.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md) — **S**.

### `prop:body-special-terminal-certificates`, item 4 — Vd1 axis replacement

**Primary source.** [4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md) — **P**.

**Target after replacement.** [4013_boundary_loss_index.md](../proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md) — **P**.

**TeX authoritative reproduction.** `04d_strategy2_rigor_completion.tex`.

### `prop:body-demand-branches`

**All-Vd0 assembly.** [4101](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md) and [4013](../proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md) — **A/P**.

**T3 assembly.** `407d` and `4130` — **A**.

**CE2 one-Vd assembly.**

- [4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md) — **N/A**;
- [4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md) — **A**;
- `4143`, `4144`, `4146`, `4147`, `4149`, `414a` — **P**.

---

## 2.5 `paper_draft/05_strategy3_reader.tex` — Area Loss

### `prop:body-area-register`

| Paper inequality | Primary source |
|---|---|
| `L(a,b)>=min(a,b)^2` | [3205_unconditional_local_square_loss.md](../proof/3XXX_CE0/32XX_Nplus_ge2/3205_unconditional_local_square_loss.md) |
| supercritical `L(a,b)>=max(a,b)^2` | [3205_unconditional_local_square_loss.md](../proof/3XXX_CE0/32XX_Nplus_ge2/3205_unconditional_local_square_loss.md) |
| T3-like `L>=2m-4m^2` | [3175_direct_T3_like_area_loss.md](../proof/3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3175_direct_T3_like_area_loss.md) |

**Supporting area notation.** [3202_area_function_and_monotonicity.md](../proof/3XXX_CE0/32XX_Nplus_ge2/3202_area_function_and_monotonicity.md) — **N/S**.

### Global cyclic sum for `N_+>=2`

**Primary analytic certificate.** [3208_CE0_conditional_area_certificate.md](../proof/3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md) — **P**.

**Local hypotheses discharged by.** `3205` — **P**.

**Branch assembly.** [3201_area_conjecture_index.md](../proof/3XXX_CE0/32XX_Nplus_ge2/3201_area_conjecture_index.md) — **A/N**.

### Global cyclic sum for exactly one supercritical V triangle plus T3-like role

**Primary global certificate.** [3174_CE0_one_supercritical_T3_certificate.md](../proof/3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3174_CE0_one_supercritical_T3_certificate.md) — **P**.

**Local T3 input.** `3175` — **P**.

**Branch assembly.** [3171_T3_like_area_certificate_index.md](../proof/3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3171_T3_like_area_certificate_index.md) — **A/N**.

**Selected criticality input for both global sums.** [1214](../proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) — **S**.

### `prop:body-area-branches`

- CE0, `N_+>=2` -> `3201`, `3205`, `3208` — **P/A**.
- CE0, `N_+=1`, some T3-like and no Vd1/Vd2 -> `3171`, `3174`, `3175` — **P/A**.

The full orientation calculations are in `05_strategy3_area.tex`.

---

## 2.6 `paper_draft/06_strategy4_reader.tex` — Direct Nine-Point Forcing

### Extreme handoff order and strict `(a,b)` domain

**Primary source.** [31058_center_independent_direct_nine_point_obstruction.md](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md) — **P**.

**Selected exact-one handoff input.** [1214](../proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) — **S**.

### Forced disk `mathcal D_eta`

**Primary source.** [31051_direct_radial_forcing.md](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31051_direct_radial_forcing.md) — **P**.

**Radial envelope input.** [2004_admissible_set.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md) — **S**.

### Forced points `Q_-,Q_0,Q_+`

**Fixed-line and circle signs.** [31052_fixed_line_circle_signs.md](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31052_fixed_line_circle_signs.md) — **P/S**.

**Asymmetric forcing.** [31053_direct_asymmetric_witness_forcing.md](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31053_direct_asymmetric_witness_forcing.md) — **P**.

### Newton inner points, Minkowski disks, cap chain, ray order, adjacent overlaps

**Primary source.** [31054_four_cap_enclosure_reduction.md](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31054_four_cap_enclosure_reduction.md) — **P**.

### `prop:reader-four-overlaps`: two mixed overlaps

**Exact rational reduction.** [31055_rational_radial_envelopes_and_mixed_reduction.md](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31055_rational_radial_envelopes_and_mixed_reduction.md) — **P**.

**Global positive-basis proof.** [31056_global_analytic_mixed_positivity.md](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31056_global_analytic_mixed_positivity.md) — **P/E**.

**Electronic objects.** Section 9 below — **E**.

### `thm:reader-witness-enclosure`

**Primary source.** [31057_terminal_nine_point_enclosure.md](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31057_terminal_nine_point_enclosure.md) — **P/A**.

### `thm:reader-zero-gap-obstruction`

**Primary source.** [31058_center_independent_direct_nine_point_obstruction.md](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md) — **P**.

### `prop:reader-ab-core-branches`

| Paper branch | Primary terminal source |
|---|---|
| CE0, `N_+=1`, all Vd0 | [31059_CE0_Nplus1_all_Vd0_completion.md](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31059_CE0_Nplus1_all_Vd0_completion.md) |
| CE1/CE2, `N_+=1`, all Vd0, zero active gaps | [4101_CE1CE2_Nplus1_all_Vd0_strategy.md](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md), invoking `31058` |

**Package index.** [31050_self_contained_direct_Vd0_nine_point_index.md](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31050_self_contained_direct_Vd0_nine_point_index.md) — **N/A**.

---

## 2.7 `paper_draft/07_exhaustive_assembly.tex` — Exhaustive Assembly

### Proof of `thm:main`

**Primary source.** [0000_main_theorem.md](../proof/0XXX_main/0000_main_theorem.md) — **P/A**.

**Paper dependencies used explicitly.**

- `prop:body-structural-reduction` -> Section 2.2 above;
- `prop:body-length-branches` -> Section 2.3;
- `prop:body-area-branches` -> Section 2.5;
- `prop:body-demand-branches` -> Section 2.4;
- `prop:paper-ce2-one-vd-placements` -> Section 3.11;
- `prop:reader-ab-core-branches` and `thm:paper-exact-mixed-certificate` -> Section 2.6 and Section 3.15.

**Completeness cross-check.** [0001_proof_tree_index.md](../proof/0XXX_main/0001_proof_tree_index.md) and
[0002_status_and_dependencies.md](../proof/0XXX_main/0002_status_and_dependencies.md) — **N**.

---

# 3. Technical appendix: file-by-file map

## 3.1 `paper_draft/appendix_roadmap.tex`

**Function.** Navigation and proof-layer disclaimer only.

**Proof sources.** None directly. It summarizes the dependency structure in
this crosswalk and in `source_ledger.md` — **N**.

## 3.2 `paper_draft/02_structural_reductions.tex`

**Paper results supplied.** `prop:open-closed-scaled`, `lem:distinct-roles`,
`prop:ce-classification`, `prop:vertex-classification`,
`prop:unique-center-midpoint`, `prop:strict-handoffs`,
`lem:short-role-count`, and the exhaustive structural reduction.

**Primary Markdown sources.**

- `1003_open_unit_vs_shrunken_closed_equivalence.md` — open/closed/scaled equivalence;
- `1101_CE_classification.md` — center classification;
- `1201_V_triangle_types.md` — vertex classification;
- `1214_strict_boundary_handoff_selection.md` — strict handoffs and criticality preservation;
- `2100_CE1_CE2_exactly_one_midpoint_lemma.md` — unique center midpoint;
- `2530_common_CE1_CE2_budget_lemmas.md` — short-role count and coarse routing;
- `0000_main_theorem.md` — terminal routing assembly.

**Supporting sources.** `1001`, `1002`, `1005`, `1202`, `1205`, `1208`,
`1212`, `1213` — **S**.

## 3.3 `paper_draft/02a_universal_calculus.tex`

**Paper results supplied.** Equilateral enclosure gauge, universal radical,
raw/capped `g` maps, zero-radial distinction, residual handoffs, strict
supercritical envelope, relaxed composition, corrected boundary-path budget,
selected `T_+` normal form, chord relaxations, and threshold routing.

**Primary Markdown sources.**

- `201a_equilateral_enclosure_and_radical_calculus.md`;
- `2004_admissible_set.md`;
- `2007_max_b_map.md`;
- `2010_free_supercritical_max_b.md`;
- `2011_capped_demand_map.md`;
- `2016_universal_Tplus_normal_form.md`;
- `2017_threshold_routing.md`;
- `2019_interval_component_and_path_budget.md`;
- `201d_raw_and_relaxed_g_chains.md`.

## 3.4 `paper_draft/02b_admissible_set_derivation.tex`

**Paper results supplied.** Complete support calculation for the triangular
and quadrilateral hulls, four finite calipers, polynomial cells `L,T,S`,
component selectors, down-closedness, and exact radial envelope.

**Primary source.** `2004_admissible_set.md` — **P**.

**Supporting sources.** `201a`, `2600`, `2607` — **S**.

## 3.5 `paper_draft/04a_signed_center_calculus.tex`

**Paper results supplied.** Signed `R,W,E,eta,P,alpha,delta` normal form, CE1/CE2
sign test, exact traces, radial exits, midpoint normalization, center boundary
length, and exact one-gap actual-V triangle interface.

**Primary sources.**

- `2105_CE1_exact_formulas.md`;
- `2106_CE2_exact_formulas.md`;
- `2109_signed_CE1_CE2_center_normal_form.md`;
- `4105_CE1_CE2_one_gap_five_row_interface.md`.

**Supporting source.** `2100_CE1_CE2_exactly_one_midpoint_lemma.md`.

## 3.6 `paper_draft/03_strategy1_length.tex`

**Paper results supplied.** Detailed boundary and skeleton trace atlas and the
terminal substitutions for Strategy 1.

**Primary generic sources.** `2500_boundary_length_bounds.md`,
`2510_skeleton_length_bounds.md`, `2530_common_CE1_CE2_budget_lemmas.md`.

**Terminal branch sources.** `3010`, `3141`, `4040`, `4041`, `4110`, `4111`,
`4123`, `4149`, `414a`, `4200`.

## 3.7 `paper_draft/04b_common_CE1_CE2_budgets.tex`

**Paper results supplied.** Signed center boundary formula, master perimeter
deficit, small-slack inequalities, three-short-role theorem, exact short-role
count, and routing consequences.

**Primary source.** `2530_common_CE1_CE2_budget_lemmas.md`.

**Supporting sources.** `2109`, `2500`, `2510`, `1201`, `1213`, `2014`.

## 3.8 `paper_draft/04c_short_Vd_placements.tex`

**Paper results supplied.** Vd corner normal form, neighboring-midpoint cap,
quarter radial envelope, adjacent rescuer, adjacent Vd radial separation,
nonadjacent Vd radial separation, and related Strategy 1 subcases.

**Primary/supporting sources.**

- `2014_Vd1_Vd2_corner_normal_form.md`;
- `2015_Vd2_neighbor_midpoint_cap.md`;
- `2018_diameter_transfer_and_adjacent_rescuer.md`;
- `201b_quarter_radial_envelope.md`;
- `201c_Vd_corner_radial_margins.md`;
- `2530_common_CE1_CE2_budget_lemmas.md`;
- terminal files `4132`, `4143`, `4144`, `4146`, `4149`.

## 3.9 `paper_draft/04_strategy2_reader.tex`

**Paper results supplied.** Complete `g`-composition presentation of the
all-Vd0 gap-rank kernel, common two-gap application, exact five-V-triangle chain,
separate CE1/CE2 endings, and summary of special-role branches.

**Primary sources.** `4013`, `2110`, `4101`, `4105`, `4106`, `4107`, `4130`,
`4140`, `4148`.

**Supporting sources.** `2011`, `2016`, `2017`, `2018`, `2019`, `201d`.

## 3.10 `paper_draft/04_strategy2_exact_demand.tex`

**Paper results supplied.** Exact admissible demand calculus, four-label capped
map, low-root bounds, endpoint inequalities, and detailed CE1 scalar
calculation.

**Primary sources.**

- `2004_admissible_set.md`;
- `2011_capped_demand_map.md`;
- `2012_high_radial_low_root_bounds.md`;
- `2016_universal_Tplus_normal_form.md`;
- `2017_threshold_routing.md`;
- `2107_one_side_capped_loss.md`;
- `2108_CE2_two_endpoint_capped_loss.md`;
- `4106_CE1_one_gap_five_map_completion.md`.

**Important supersession.** Any compact legacy Vd1 replacement line in this
file is superseded by the complete proof in `04d` and the explicit correction
in `04f`.

## 3.11 `paper_draft/04d_strategy2_rigor_completion.tex`

**Paper results supplied.** Formal incorporation of the complete `407X`
four-label endpoint proof and a full TeX proof of the Vd1-supercritical axis
replacement.

**Primary `407X` objects.** `4073`, `4074`, `4075`, `4078`, `4079`, `407a`,
`407c`, `407d`, with exact Git blob identifiers recorded in the TeX file.

**Primary replacement source.** `4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`.

**Supporting sources.** `2011`, `2014`, `4013`.

## 3.12 `paper_draft/04e_strategy2_placement_assembly.tex`

**Paper result supplied.** `prop:paper-ce2-one-vd-placements`, the authoritative
exhaustive CE2 exactly-one-Vd1/Vd2 assembly.

**Primary assembly sources.**

- `4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md` — navigation;
- `4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md` — exhaustive assembly.

**Terminal sources.** `4143`, `4144`, `4146`, `4147`, `4149`, `414a`, and
`4013` after replacement.

## 3.13 `paper_draft/04f_strategy2_cross_reference_closure.tex`

**Paper function.** Declares `04d` and `04e` authoritative for the compact
legacy Strategy 2 summaries and records the corrected weak comparison in the
Vd1 radial bridge.

**Primary sources.** `4147` and `4148` — **P/A**.

**Reason this file exists.** It prevents an earlier concise statement from
being treated as an independent proof dependency or as a stronger inequality
than the numbered source proves.

## 3.14 `paper_draft/05_strategy3_area.tex`

**Paper results supplied.** Two affine orientation normal forms, local
minimum-square loss, supercritical maximum-square loss, direct T3-like loss,
reflection normalization, and both cyclic area sums.

**Primary sources.** `3205`, `3208`, `3175`, `3174`.

**Assembly sources.** `3201`, `3171`.

## 3.15 `paper_draft/06_strategy4_ab_core.tex`

**Paper results supplied.** Strict exact-one handoff domain, direct radial and
asymmetric forcing, Newton inner witnesses, Minkowski disk orbits, cap-chain
reduction, ray ordering, and two adjacent cap overlaps.

**Primary sources.** `31051`, `31052`, `31053`, `31054`.

**Supporting sources.** `1214`, `2004`, `201a`, `31050`.

## 3.16 `paper_draft/06a_strategy4_exact_certificate.tex`

**Paper results supplied.** Rational radial upper envelopes, exact Gram
residuals, residual-to-cap implication, eight integer-polynomial reduction,
three global charts, exact Bernstein conversion, and certificate manifest.

**Primary mathematical sources.** `31055`, `31056`.

**Electronic sources.** Section 9 below.

## 3.17 `paper_draft/appendix_symbols.tex`

**Function.** Notation cross-reference only.

**Primary notation sources.**

- [0910_notation_dictionary.md](../proof/09XX_appendices/0910_notation_dictionary.md) — **N**;
- [201d_raw_and_relaxed_g_chains.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md) — **P/S**;
- `1202`, `2109`, and the `3105X` package — **S**.

---

# 4. Routing-V triangle crosswalk

This table is the direct connection between `tab:routing` in the paper and the
terminal proof sources.

| Routing V triangle in the paper | Reader-facing conclusion | Status-bearing terminal source(s) |
|---|---|---|
| CE0, `N_+=0` | Strategy 1 | `3010_CE0_perimeter_length_obstruction.md` |
| CE0, `N_+=1`, all Vd0 | Strategy 4 | `31058_center_independent_direct_nine_point_obstruction.md`, `31059_CE0_Nplus1_all_Vd0_completion.md` |
| CE0, `N_+=1`, some Vd1/Vd2 | Strategy 1 | `3141_CE0_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md` |
| CE0, `N_+=1`, T3-like and no Vd1/Vd2 | Strategy 3 | `3171`, `3174`, `3175` |
| CE0, `N_+>=2` | Strategy 3 | `3201`, `3205`, `3208` |
| CE1/CE2, `q>=3` | Strategy 1 | `2530`, with `2510` |
| CE1/CE2, `N_+=0`, all Vd0 | Strategy 2 | `4013`, using `2107`, `2108`, `2110` |
| CE1/CE2, `N_+=0`, some Vd1/Vd2 | Strategy 1 | `4040` or `4041` |
| CE1/CE2, `N_+=0`, T3-like and no Vd1/Vd2 | Strategy 2 | complete `407X`: `4071`-`407d` |
| CE1/CE2, `N_+=1`, all Vd0, zero gaps | Strategy 4 | `31058`, invoked through `4101` |
| CE1/CE2, `N_+=1`, all Vd0, one active gap | Strategy 2 | `4105` plus `4106` or `4107` |
| CE2, `N_+=1`, all Vd0, two active gaps | Strategy 2 | `2108`, `2110` |
| CE1/CE2, `N_+=1`, exactly one T3-like | Strategy 2 | `4130`, `4131`, `4132`, using `2018` |
| CE1, `N_+=1`, exactly one Vd1/Vd2 | Strategy 1 | `4110` |
| CE2, `N_+=1`, exactly one Vd1/Vd2 | Strategy 1 + 2 | `4143`, `4144`, `4146`, `4147`, `4149`, `414a`, assembled by `4148` and indexed by `4140` |
| CE1/CE2, `N_+>=2` | Strategy 1 | `4200`, with `2530` and `2510` |

---

# 5. Reverse index: foundational proof source to paper location

| Proof source | Main paper locations using it |
|---|---|
| `1003` | `01_introduction`: expanded closed formulation; `02_structural_reductions` |
| `1101` | `01_introduction`: center dictionary; `prop:body-structural-reduction` |
| `1201` | vertex dictionary, structural reduction, short-role routing |
| `1214` | structural reduction, Strategy 3 selected handoffs, Strategy 4 exact-one order |
| `2004` | explicit admissible set, exact-demand appendix, Strategy 4 radial envelope |
| `2007` | raw transfer map in `02_reader_framework` and `02a` |
| `2010` | strict-supercritical envelope in Strategies 2 and rescuer branches |
| `2011` | capped map, duality, four-label T3 audit, five-V-triangle chains |
| `2016` | CE1 five-V-triangle chords, `407X` high sheet, T3 rescuer rationalization |
| `2017` | CE1/CE2 threshold endings |
| `2018` | one-gap diameter terminal and common T3/Vd1 rescuer |
| `2019` | residual maps and every center-free path budget |
| `201a` | enclosure gauge and common radical notation |
| `201b` | adjacent CE2 Vd quarter radial envelope |
| `201c` | adjacent/nonadjacent Vd radial margins |
| `201d` | canonical `g` notation throughout Strategy 2 |
| `2107` | one-active-gap all-Vd0 endpoint certificate |
| `2108` | paired CE2 endpoint certificate |
| `2109` | signed center interface and CE1/CE2 boundary caps |
| `2110` | common two-active-gap application for both `N_+=0` and `N_+=1` |
| `2500` | perimeter trace register and Strategy 1 branches |
| `2510` | skeleton trace register and three-short-role contradiction |
| `2530` | master budget, small CE2 slack, `q=N_++m`, routing |

---

# 6. Reverse index: terminal proof package to paper location

| Terminal package | Reader-facing paper location |
|---|---|
| `3010` | `prop:body-length-branches`, CE0 `N_+=0` |
| `31050`-`31059` | all of `06_strategy4_reader.tex`; zero-gap V triangles in final assembly |
| `3141` | `prop:body-length-branches`, CE0 one-Vd branch |
| `3171`, `3174`, `3175` | `prop:body-area-branches`, CE0 exactly-one-supercritical T3 branch |
| `3201`, `3205`, `3208` | `prop:body-area-branches`, CE0 `N_+>=2` |
| `4013` | all-Vd0 `N_+=0` kernel and post-`4147` replacement target |
| `4040`, `4041` | Strategy 1 CE1/CE2 `N_+=0` Vd branches |
| `4070`-`407d` | `def:body-t3-endpoint-state`, `prop:body-t3-endpoint`, `04d` |
| `4101`, `4105`, `4106`, `4107` | `prop:body-five-row-certificate` and positive-gap all-Vd0 routing |
| `4110`, `4111` | Strategy 1 Vd branch routing |
| `4123` | multiple-T3 short-role routing |
| `4130`, `4131`, `4132` | exactly-one-T3-like Strategy 2 branch |
| `4140`, `4143`, `4144`, `4146`, `4147`, `4148`, `4149`, `414a` | CE2 exactly-one-Vd hybrid V triangle, `04d`, `04e`, `04f` |
| `4200` | CE1/CE2 `N_+>=2` Strategy 1 V triangle |

---

# 7. Exact Strategy 4 certificate objects

All paths in this section are relative to:

`proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/`

## 7.1 Authenticated sparse polynomial data — **E**

- `mixed_overlap_core_data_00.py`
- `mixed_overlap_core_data_01.py`
- `mixed_overlap_core_data_02.py`
- `mixed_overlap_core_data_03.py`
- `mixed_overlap_core_data_04.py`
- `mixed_overlap_core_data_05.py`
- `mixed_overlap_core_polynomials.py`

The canonical decoded transcript has SHA-256 digest:

`dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485`

## 7.2 Exact verifiers — **E**

- `verify_mixed_overlap_core_derivation.py`
  - reconstructs the Newton witnesses, rational radial envelopes, and four Gram
    residuals in exact rational-function arithmetic;
  - reduces modulo `D^2-(z^2+6U+3U^2)`;
  - removes the proved positive common factors;
  - compares every sparse coefficient with the authenticated transcript.

- `verify_global_core_positivity.py`
  - performs exact polynomial substitutions on the three global charts;
  - represents `Q(sqrt(3))` coefficients as exact rational pairs;
  - converts power coefficients to tensor Bernstein coefficients exactly;
  - verifies the required coefficient signs without floating-point or interval
    arithmetic.

## 7.3 Mathematical bridge back to the paper

The certificate is connected to `prop:reader-four-overlaps` by:

1. `31055`: derives `Q_A,Q_C` and the eight integer-polynomial cores;
2. `31056`: proves all eight cores nonnegative on the complete domain;
3. `06a_strategy4_exact_certificate.tex`: proves that `Q_A,Q_C>=0` imply the
   two common-tangent support inequalities and hence the two mixed cap overlaps;
4. `31057`: combines these overlaps with the adjacent overlaps and the cap
   chain to prove the terminal enclosure.

A verifier output without these reductions is not, by itself, the paper proof.

---

# 8. Incorporated `407X` electronic supplement

The complete four-label proof is maintained in Markdown rather than duplicated
line-for-line in the TeX appendix. The exact source objects are:

- `4073_boundary_loss_framework.md` — exact residual reduction;
- `4074_L_Full_branch.md` — `(L,Full)`;
- `4075_Tminus_low_lower_branch_obligations.md` — first-`T_-` family;
- `4078_left_L_family_completion.md` — remaining first-`L` family;
- `4079_first_Full_branch.md` — first-Full exclusion;
- `407a_left_Thigh_branch_completion.md` — first-`T_+^{hi}` family;
- `407c_rigor_completion_details.md` — analytic inequalities and thresholds;
- `407d_rigor_final_assembly.md` — exhaustive reassembly.

`04d_strategy2_rigor_completion.tex` records their exact Git blob identifiers.
The optional script under `407X_computation/` remains an experiment/cross-check,
not an active proof dependency.

---

# 9. Nondependencies and historical routes

The paper must not use the following as active proof sources:

- `9XXX_failed_ideas/908X_skeleton_cover_counterexample/` — disproves the false
  global full-skeleton shortcut;
- `9XXX_failed_ideas/962X_may21_four_point_failure/` — failed four-point route;
- `9XXX_failed_ideas/963X_may25_five_point_failure/` — failed five-point route;
- `9XXX_failed_ideas/964X_CE1_CE2_area_conjecture_failure/` — failed CE1/CE2 area route;
- `3172_full_T3_like_tangent_envelope_conjecture.md` — false global T3-like
  coordinatewise tangent envelope;
- old `3100X`-`3104X` routes — historical or optional after the canonical
  `3105X` direct nine-point proof;
- `4104_all_boundary_transfer_to_310X.md` — optional reduction, not the active
  all-Vd0 proof;
- `3105a_disk_plus_point_enclosure.md` — optional lemma not used by the paper.

Navigation files with `Status: Reference` are also not terminal proof sources.

---

# 10. Maintenance checklist

When a proof Markdown file changes, update this crosswalk if any of the
following changes:

1. a theorem hypothesis, especially open/closed, strict/non-strict,
   center-free, midpoint, or positive-length assumptions;
2. the paper label or proposition that cites the result;
3. the primary/secondary status of a proof package;
4. a branch's exhaustive placement assembly;
5. the exact Strategy 4 data blobs, verifier blobs, or transcript digest;
6. the active/nonactive status of a historical route.

When a paper TeX file changes, verify:

1. every body proposition has at least one status-bearing primary source;
2. every appendix claim agrees with the hypotheses of the Markdown source;
3. every routing-table entry still has exactly one terminal route after the
   top-to-bottom precedence rules;
4. `N_+` remains defined from actual maximal reaches;
5. singleton gaps remain included;
6. every identity-relaxed boundary path verifies that its internal edges are
   center-free and free of nonincident positive-length traces;
7. the exact five-V-triangle target remains `Z>1-H`, while the reversed dual target is
   `>1-X`;
8. the CE2 threshold language remains “at least one”, not “exactly one”;
9. the adjacent CE2 Vd terminal remains the direct quarter radial separation;
10. the nonadjacent Vd terminal remains Vd-specific;
11. `04d`, `04e`, and `04f` remain authoritative over any compact legacy
    summary they supersede.

---

# 11. Quick audit conclusion

The body-to-proof dependency spine is:

`01 introduction and routing`
-> `02 structural/local interfaces`
-> `Strategies 1-4 terminal propositions`
-> `07 exhaustive assembly`
-> `0000_main_theorem.md`.

The paper's complete proof is not the body alone. It is the body together with
the TeX verification appendices and the two formally incorporated supplements:
the complete `407X` four-label proof and the exact `3105X` mixed-overlap
certificate.
