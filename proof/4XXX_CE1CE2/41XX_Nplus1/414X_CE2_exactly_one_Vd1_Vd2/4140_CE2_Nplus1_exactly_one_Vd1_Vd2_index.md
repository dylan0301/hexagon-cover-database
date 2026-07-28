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
   gives the Strategy 1 skeleton contradiction.
2. Otherwise every other row is Vd0. The placement split in `4148` is closed
   by `4143`, `4144`, `4146`, `4147`, `4149`, and the proved `4013` package.

The Strategy 1 files `4149` and `414a` retain their current proofs and routing.

## Terminal table

The canonical transfer notation is from
[`201d`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md).
The adjacent and nonadjacent Vd terminals are geometric radial separations; the
adjacent route must not be replaced by an unsupported universal transfer map.

| placement | seed or residual data | ordinary propagation | terminal certificate |
|---|---|---|---|
| `4143`: Vd1 rescues neighboring supercritical row | $1-g_c^{\rm sc}$ | center-free ordinary path through $T_2,T_3,T_4,T_5$ | $b_1<g_c^{\rm sc}\le h$ |
| `4144`: supercritical $T_0$, adjacent Vd1/Vd2 $T_1$ | exact center residuals $A,H$ | backward lower reach $H$ through four ordinary Vd0 rows | $\delta<H/4$ and both possible radial bridges end before $1-\delta$ |
| `4146`: supercritical $T_0$, nonadjacent Vd1/Vd2 $T_\tau$ | exact center residuals $A,H$ | identity propagation through intervening center-free Vd0 edges | $c_\tau<1-\min\{A,H\}<1-d_\tau^C$ |
| `4147`: neither special row is $T_0$ | adjacent Vd1--supercritical pair | explicit replacement by two open nonsupercritical Vd0 rows | invoke proved `4013` |

For `4143`, the outgoing envelope $B<g_c^{\rm sc}$ is unconditional.  The
following endpoint demand is obtained only after the proof verifies that the
intervening boundary path has no center trace on its internal edges.

For `4144`, the ordinary boundary propagation gives

$$
b_5\ge H\Longrightarrow b_4\ge H\Longrightarrow b_3\ge H
\Longrightarrow b_2\ge H\Longrightarrow b_1\ge H.
$$

The Vd cap gives $A+H<1/2$.  The exact center budget gives

$$
\delta<\frac H4.
$$

The possible Vd supported-arm endpoint is below $1-H$.  The ordinary row has
boundary demands exceeding $1/2+A$ and $H$, so the global quarter radial
envelope gives

$$
c_2\le1-\frac H4<1-\delta.
$$

The center interval begins at $1-\delta$, and neither radial bridge reaches it.
This direct separation, rather than a formal hatted-map inequality, is the
active terminal proof.

For `4146`, the final inequality is deliberately Vd-specific. Its use of the
Vd1/Vd2 corner normal form is essential.

The axis replacement in `4147` is geometric preprocessing, not a scalar map.
Once the replacement is made, both exceptional rows become open
nonsupercritical Vd0 rows and the existing all-Vd0 theorem applies.

## Local geometry

- [`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md)
  gives the Vd1/Vd2 corner normal form and $a+b<1/2$.
- [`2015`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2015_Vd2_neighbor_midpoint_cap.md)
  gives the $a+b<1/3$ neighboring-midpoint cap for Vd2.
- [`2018`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md)
  gives the diameter curve and common rescuer chain.
- [`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
  gives the residual operator and the corrected center-free path budget.
- [`201b`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md)
  gives the global quarter radial envelope used by `4144`.
- [`201c`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md)
  gives the Vd radial margins used by `4144` and `4146`.
- [`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
  gives
  $$
  \alpha+\delta<\frac1{24},
  \qquad
  \alpha+\delta<\frac{\min\{R,1-R\}}6.
  $$

## Files

| File | Recorded status | Role |
|---|---|---|
| [`4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md`](4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md) | Empirical | Historical visual candidate; not used. |
| [`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md) | Proven | Vd1 profile and common rescuer chain. |
| [`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md) | Proven | Exact residuals, center quarter margin, and two radial bridge exclusions. |
| [`4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md`](4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md) | Proven | Exact residuals and Vd-specific radial separation. |
| [`4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`](4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md) | Proven | Explicit open Vd0 replacement. |
| [`4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md) | Proven | Exhaustive placement assembly. |
| [`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md) | Proven | Strategy 1 perimeter proof. |
| [`414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md`](414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md) | Proven | Strategy 1 skeleton proof. |
