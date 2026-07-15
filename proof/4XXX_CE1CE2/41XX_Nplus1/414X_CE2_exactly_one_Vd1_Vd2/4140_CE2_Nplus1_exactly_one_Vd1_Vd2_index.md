# CE2, $N_+=1$, Exactly One Vd1/Vd2

Status: Proven

The full case split and final proof are in
[`4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md).

There are two exhaustive branches.

1. If any row in addition to the unique Vd1/Vd2 row has positive adjacent
   support, `414a` gives a skeleton-length contradiction.
2. Otherwise, the classification in
   [`1201`](../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md)
   makes every other row Vd0. The placement split in `4148` is then closed by
   `4143`, `4144`, `4146`, `4147`, `4149`, and the proved `4013` package.

The reusable Vd1/Vd2 geometry has been moved to the `2XXX` block: `2014`
contains the corner normal form, while `2015` contains the Vd2
neighbor-midpoint cap.

## Files

| File | Recorded status | Role |
|---|---|---|
| [`4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md`](4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md) | Empirical | Historical visual candidate; not used in the proof. |
| [`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md) | Proven | Vd1 row at $V_0$ rescuing the adjacent supercritical row. |
| [`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md) | Proven | Supercritical row at $V_0$ and adjacent Vd1/Vd2 row. |
| [`4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md`](4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md) | Proven | Supercritical row at $V_0$ and non-adjacent Vd1/Vd2 row. |
| [`4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`](4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md) | Proven | Vd1--supercritical pair replacement and radial bridge. |
| [`4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md) | Proven | Exhaustive placement assembly. |
| [`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md) | Proven | Vd2 neighbor-midpoint boundary obstruction. |
| [`414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md`](414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md) | Proven | Additional positive-support branch. |
| [`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md) | Proven | Shared Vd1/Vd2 corner normal form and half-unit boundary cap. |
| [`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2015_Vd2_neighbor_midpoint_cap.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2015_Vd2_neighbor_midpoint_cap.md) | Proven | Shared $a+b<1/3$ cap for Vd2 neighbor rescue. |
