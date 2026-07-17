# Direct All-Vd0 Nine-Point Package

Status: Reference

This package gives the short active proof of the CE0, $N_+=1$, all-Vd0
branch.  It works first at the level of actual open vertex roles.  Six common
radial points are forced directly by the exact radial envelope and the Vd0
condition, while the three asymmetric points are forced by distances from
actual handoff points and the frontier of the unique supercritical row.

Thus no $AB$-union for a nonsupercritical row is used.  The older
[`3103X_residual_core`](../3103X_residual_core/31030_CE0_all_Vd0_residual_core_strategy.md)
package remains an independent proven route.

| File | Recorded status | Role |
|---|---|---|
| [`31041_direct_radial_forcing.md`](31041_direct_radial_forcing.md) | Proven | Forces six common radial witnesses into the center role using $c_{\max}$, openness, Vd0 locality, and diameter. |
| [`31042_direct_asymmetric_witness_forcing.md`](31042_direct_asymmetric_witness_forcing.md) | Proven | Forces the three asymmetric witnesses into the center role; only the unique supercritical row uses an $AB$-frontier. |
| [`31043_center_independent_direct_nine_point_obstruction.md`](31043_center_independent_direct_nine_point_obstruction.md) | Proven | Combines the nine direct witnesses with the terminal enclosure theorem. |
| [`31044_CE0_Nplus1_all_Vd0_direct_completion.md`](31044_CE0_Nplus1_all_Vd0_direct_completion.md) | Proven | Deduces the CE0, $N_+=1$, all-Vd0 branch from the center-independent theorem. |

## Dependency map

The direct route uses:

- strict exact-one handoffs from
  [`1214`](../../../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md);
- the Vd0 definition from
  [`1201`](../../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md);
- the exact radial envelope from
  [`2004`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md);
- the unique strict-row frontier from
  [`20091`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md);
- the fixed-line circle signs from
  [`31012`](../3101X_six_point/31012_core_graph_two_variable_relaxation.md);
- the exact asymmetric formulas and elementary distance inequalities from
  [`31033`](../3103X_residual_core/31033_asymmetric_witness_construction.md); and
- the terminal enclosure theorem
  [`31034`](../3103X_residual_core/31034_witness_enclosure_inequality.md).

It does not use nonsupercritical $AB$-unions, their antitonic comparison,
the symmetric or asymmetric model residual cores, the neighboring-ray
maximum theorem `2008`, or the optional six-point inequality $F_6\ge1$.
