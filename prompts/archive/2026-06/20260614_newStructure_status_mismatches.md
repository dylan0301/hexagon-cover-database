# Historical Status Mismatches In `20260611newStructure.txt`

Status: Reference

This file preserves the status comparison made on June 14, 2026, between
proof-level claims in
[`20260611newStructure.txt`](20260611newStructure.txt) and the status recorded
at that time in `proof/`. The source links below have been
updated to their successors in the combined CE1/CE2 layout, but the status and
mismatch columns are historical rather than a live status table. For current
statuses, use
[`../proof/0XXX_main/0002_status_and_dependencies.md`](../proof/0XXX_main/0002_status_and_dependencies.md).

Under the current proof-status convention, only files marked `Status: Proven`
count as established results.

## Stronger In The Sketch Than In The Files At Audit Time

| Sketch location | Sketch claim | Successor source | Recorded status at audit time | Mismatch at audit time |
|---|---|---|---|---|
| `20260611newStructure.txt`, lines 38-39 | CE0, $N_+=1$, at least one Vd1/Vd2 is uncoverable by boundary length. | [`../proof/3XXX_CE0/31XX_Nplus1/314X_exists_Vd1_Vd2/3141_CE0_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md`](../proof/3XXX_CE0/31XX_Nplus1/314X_exists_Vd1_Vd2/3141_CE0_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) | Practically proven | Not fully proven. The older CE0 Vd1/Vd2 half-skeleton theorem is proven separately, but this boundary-length package is only practically proven. |
| `20260611newStructure.txt`, lines 40-41 | CE0, $N_+=1$, at least one T3-like and no Vd1/Vd2 has a successful max-area proof to add. | [`../proof/3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3171_T3_like_area_certificate_index.md`](../proof/3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3171_T3_like_area_certificate_index.md) | Strategy / conditional package | The current package proves only conditional analytic implications. The full T3-like tangent-envelope input and Vd0 square-loss inputs remain open. |
| `20260611newStructure.txt`, lines 51-52 | CE1, $N_+=0$, at least one Vd1/Vd2 is uncoverable by boundary length. | [`../proof/4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](../proof/4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | Practically proven | Not fully proven under the repository status conventions. |
| `20260611newStructure.txt`, lines 59-60 | CE1, $N_+=1$, at least one Vd1/Vd2 is uncoverable by boundary length. | [`../proof/4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) | Practically proven | Not fully proven under the repository status conventions. |
| `20260611newStructure.txt`, lines 61-66 | CE1, at least two T3-like and no Vd1/Vd2 cannot cover diagonals; length is not enough. | [`../proof/4XXX_CE1CE2/41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md), [`../proof/2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md`](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md) | Practically proven | Not fully proven under the repository status conventions. |
| `20260611newStructure.txt`, lines 77-87 | CE1/CE2 with $N_+\ge2$ cannot cover the hexagon skeleton, with a length proof. | [`../proof/4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md`](../proof/4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md), [`../proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md`](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md) | Practically proven | Not fully proven under the repository status conventions. |
| `20260611newStructure.txt`, lines 96-97 | CE2, $N_+=0$, at least one Vd1/Vd2 is uncoverable by boundary length. | [`../proof/4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](../proof/4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | Practically proven | Not fully proven under the repository status conventions. |
| `20260611newStructure.txt`, lines 104-105 | CE2, $N_+=1$, at least two Vd1/Vd2 is uncoverable by boundary length. | [`../proof/4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md) | Practically proven | Not fully proven under the repository status conventions. |
| `20260611newStructure.txt`, lines 108-113 | CE2, at least two T3-like and no Vd1/Vd2 cannot cover diagonals; length is not enough. | [`../proof/4XXX_CE1CE2/41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md) | Practically proven | Not fully proven under the repository status conventions. |
| `20260611newStructure.txt`, lines 124-134 | CE2 with $N_+\ge2$ uses the same skeleton-length proof. | [`../proof/4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md`](../proof/4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md), [`../proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md`](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md) | Practically proven | Not fully proven under the repository status conventions. |

## Files That Were Stronger Or Different Than The Sketch

| Sketch location | Sketch claim | Successor source | Recorded status at audit time | Mismatch at audit time |
|---|---|---|---|---|
| `20260611newStructure.txt`, lines 93-95 | CE2, $N_+=0$, all Vd0 boundary-loss proof does not work; TODO. | [`../proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`](../proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md) | Proven local lemma | The files at audit time recorded this branch as proven under the recorded assumptions. |

## Lemma Inventory Status Gaps

The `2XXX geometric lemmas` section of the sketch is mostly an organization
request, not a direct proof claim. If it is read as a list of proven reusable
lemmas, these statuses at audit time were weaker than proven:

| Sketch location | Topic | Successor source | Recorded status at audit time | Mismatch at audit time |
|---|---|---|---|---|
| `20260611newStructure.txt`, line 15 | Admissible set for V-triangles and corollaries. | [`../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md), [`../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md) | Computational formula; Practically proven | Not fully proven as a package. |
| `20260611newStructure.txt`, line 16 | Classification of maximal triangles over skeleton. | No matching current proof package found. | Missing package | Current notes explicitly warn that half-skeleton midpoint inventories are not full-skeleton maximal-triangle statements. |
| `20260611newStructure.txt`, line 17 | Classification of maximal triangles over half-skeleton. | [`../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2101_maximal_C_triangles_over_half_skeleton.md`](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2101_maximal_C_triangles_over_half_skeleton.md), [`../proof/1XXX_foundations/12XX_V_triangle/1205_midpoint_subsets.md`](../proof/1XXX_foundations/12XX_V_triangle/1205_midpoint_subsets.md) | Definition / proof target, with proven normalized CE1 and CE2 subcases; Reference | Not a fully proven general classification package. |
| `20260611newStructure.txt`, line 18 | $AB$-union curve equations. | [`../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md) | Reference / exact formula | Exact formula is recorded, but the status is not one of the proven labels. |
| `20260611newStructure.txt`, line 20 | Half-skeleton lemmas. | Mixed sources, including [`../proof/3XXX_CE0/33XX_old_Vd1_Vd2_chain_proof/3301_CE0_Vd1_Vd2_half_skeleton_theorem.md`](../proof/3XXX_CE0/33XX_old_Vd1_Vd2_chain_proof/3301_CE0_Vd1_Vd2_half_skeleton_theorem.md) and [`../proof/1XXX_foundations/12XX_V_triangle/1205_midpoint_subsets.md`](../proof/1XXX_foundations/12XX_V_triangle/1205_midpoint_subsets.md) | Mixed | Some half-skeleton results are proven, but the inventory is not a single fully proven lemma package. |

## Checked Sources

| File | Recorded status | Role |
|---|---|---|
| [`../proof/0XXX_main/0002_status_and_dependencies.md`](../proof/0XXX_main/0002_status_and_dependencies.md) | Reference | Main status table. |
| [`../proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md`](../proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md) | Definition | Status-label definitions. |
