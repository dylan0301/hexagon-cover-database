# CE2, $N_+=1$, Exactly One Vd1/Vd2

Status: Proven

The full placement assembly is
[`4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md).
The branch is CE2-only because the common perimeter budget in
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
eliminates CE1 before the local placement analysis.

There are two exhaustive branches.

1. If any row in addition to the unique Vd1/Vd2 row has positive adjacent
   support, the three-short-role theorem in `2530`, applied through `414a`,
   gives a skeleton-length contradiction.
2. Otherwise the classification in
   [`1201`](../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md)
   makes every other row Vd0. The placement split in `4148` is closed by
   `4143`, `4144`, `4146`, `4147`, `4149`, and the proved `4013` package.

The local geometry is organized as follows.

- [`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md)
  gives the Vd1/Vd2 corner normal form and $a+b<1/2$.
- [`2015`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2015_Vd2_neighbor_midpoint_cap.md)
  gives the $a+b<1/3$ neighboring-midpoint cap for Vd2.
- [`2018`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md)
  gives the common adjacent-edge diameter curve and the class-independent
  center-hiding and boundary-path argument used by the T3-like and Vd1 rescue
  branches.
- [`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
  gives the residual boundary-demand operator used uniformly in the adjacent
  and nonadjacent placements.
- [`201b`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md)
  gives the global quarter radial envelope used by `4144`; the historical
  half-edge $1/3$ envelope is no longer an active dependency.
- [`201c`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md)
  gives both radial margins used in `4144` and `4146`.
- [`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
  gives the surviving CE2 bounds
  $$
  \alpha+\delta<\frac1{24},
  \qquad
  \alpha+\delta<\frac{\min\{R,1-R\}}6.
  $$

## Files

| File | Recorded status | Role |
|---|---|---|
| [`4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md`](4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md) | Empirical | Historical visual candidate; not used in the proof. |
| [`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md) | Proven | Proves only the two Vd1 local profile inequalities, then invokes the common adjacent-rescuer theorem `2018`; no separate hiding or terminal sum remains. |
| [`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md) | Proven | Uses the interval residuals, proves the stronger center margin $\delta<H/4$, and closes both radial alternatives with `201b` and `201c`. |
| [`4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md`](4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md) | Proven | Uses the interval residuals and diameter transfer to put every center exit below the boundary minimum, then applies the single own-radial margin from `201c`. |
| [`4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`](4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md) | Proven | Vd1--supercritical pair replacement and radial bridge. |
| [`4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md) | Proven | Exhaustive placement assembly. |
| [`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md) | Proven | Vd2 neighbor-midpoint branch, now a direct corollary of the common perimeter budget and the $1/3$ cap. |
| [`414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md`](414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md) | Proven | Additional positive-support branch, now the three-short-role skeleton theorem. |
