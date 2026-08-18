# Strategy 2 Scalar-Calculation Crosswalk

Status: Reference

This file identifies the long scalar calculations used by the geometric
Strategy 2 proof. It is a navigation and specification crosswalk, not an
additional universal theorem and not a proof supplied by the Lean statement
project. The numbered geometric sources remain the theorem owners.

## Calculation owners

| Calculation | Geometric hypotheses and proved source |
|---|---|
| One-side CE1/CE2 endpoint loss | The signed center variables and endpoint hypotheses of [`2107`](2107_one_side_capped_loss.md). |
| Paired CE2 endpoint loss | The exact CE2 interval and endpoint hypotheses of [`2108`](2108_CE2_two_endpoint_capped_loss.md), applied geometrically in [`2110`](2110_common_CE2_two_gap_application.md). |
| CE1 returned demand | The signed domain and realized five-V-triangle chain of [`4105`](../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4105_CE1_CE2_one_gap_five_V_triangle_interface.md), with the long scalar calculation in [`4106`](../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4106_CE1_one_gap_five_map_completion.md). |
| CE2 returned demand | The corresponding realized chain in `4105`, with the scalar threshold calculation in [`4107`](../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4107_CE2_one_gap_five_map_completion.md). |
| T3 endpoint audit | The support-isolated geometric branch of [`4071`](../../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md)--[`4073`](../../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4073_boundary_loss_framework.md), with its exact four-label proof in `4074`--`407d` and canonical wrapper [`407e`](../../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407e_pure_finite_cell_theorem.md). |
| Adjacent rescuer | The realized T3-like or Vd1 normal form and center-hiding hypotheses in [`2018`](../20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md), [`4132`](../../4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md), and `4143`. |
| Adjacent and nonadjacent Vd margins | The Vd1/Vd2 corner graph of [`2014`](../20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md), the radial margins of [`201c`](../20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md), and their applications `4144` and `4146`. |

## Scope of the formalization interface

The source-only TeX and Lean files expose machine-checkable statements for
the necessary long scalar calculations. Their role is deliberately narrow:
they do not formalize the open/closed setup, classifications, geometric
realization of the variables, branch exhaustiveness, or the global covering
theorem. The ten Lean theorem bodies are intentionally admitted; successful
elaboration checks the statement interface only.

In particular, this crosswalk makes no claim that an arbitrary point of a
separately extracted T3 real-variable cell union satisfies every geometric
hypothesis used in the authenticated `407X` proof. The theorem used by the
covering argument is the geometric consequence recorded in `407e`.
