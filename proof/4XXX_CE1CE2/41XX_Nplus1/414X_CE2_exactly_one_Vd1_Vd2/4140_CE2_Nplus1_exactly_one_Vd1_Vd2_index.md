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
   gives the existing Strategy 1 skeleton contradiction.
2. Otherwise every other row is Vd0. The placement split in `4148` is closed
   by `4143`, `4144`, `4146`, `4147`, `4149`, and the proved `4013`
   package.

The Strategy 1 files `4149` and `414a` retain their current proofs and routing.

## Transfer-chain table

The canonical notation is from
[`201d`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md).

| placement | seed or residual data | relaxed ordinary slots | terminal envelope |
|---|---|---|---|
| `4143`: Vd1 rescues neighboring supercritical row | $1-g_c^{\rm sc}$ | $\mathrm I^3$ through $T_2,T_3,T_4$ | $b_5<g_c^{\rm sc}\le h$ |
| `4144`: supercritical $T_0$, adjacent Vd1/Vd2 $T_1$ | exact center residuals $A,H$ | backward identity chain through four ordinary rows | $\widehat g_{1-\delta}^\vee(1/2+A)>1-H$ |
| `4146`: supercritical $T_0$, nonadjacent Vd1/Vd2 $T_\tau$ | exact center residuals $A,H$ | identity propagation through intervening Vd0 rows | Vd-specific separation $c_\tau<1-\min\{A,H\}<1-d_\tau^C$ |
| `4147`: neither exceptional row is $T_0$ | adjacent Vd1--supercritical pair | replace by two nonsupercritical Vd0 rows | invoke the corresponding `4013` chain |

The first row is the same chain as the T3-like branch:

$$
A_2>1-g_c^{\rm sc}
\quad\xrightarrow{\ \mathrm I^3\ }\quad
A_5>1-g_c^{\rm sc},
$$

followed by

$$
b_5<g_c^{\rm sc}\le h.
$$

For the adjacent placement, the four identity slots record

$$
b_5\ge H
\Longrightarrow
b_4\ge H
\Longrightarrow
b_3\ge H
\Longrightarrow
b_2\ge H
\Longrightarrow
b_1\ge H.
$$

The terminal quarter-envelope inequality is equivalent to

$$
\widehat g_{1-\delta}\left(1-\left(\frac12+A\right)\right)<H,
$$

or, in the reach coordinate used by the chain,

$$
\widehat g_{1-\delta}^\vee\left(\frac12+A\right)>1-H.
$$

For the nonadjacent placement, the final inequality is deliberately recorded
as a Vd-type envelope rather than a universal $\widehat g_c^\vee$ bound. Its
use of the Vd1/Vd2 corner normal form is essential.

The axis replacement in `4147` is geometric preprocessing, not a new scalar
map. Once the replacement is made, both exceptional rows become ordinary
nonsupercritical Vd0 rows and the existing all-Vd0 chain applies.

## Local geometry

- [`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md)
  gives the Vd1/Vd2 corner normal form and $a+b<1/2$.
- [`2015`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2015_Vd2_neighbor_midpoint_cap.md)
  gives the $a+b<1/3$ neighboring-midpoint cap for Vd2.
- [`2018`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md)
  gives the diameter curve and the common $g_c^{\rm sc}$ rescuer chain.
- [`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
  gives the residual operator and center-assisted $g$-transfers.
- [`201b`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md)
  gives the global quarter radial envelope used by `4144`.
- [`201c`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md)
  gives both radial margins used in `4144` and `4146`.
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
| [`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md) | Proven | Vd1 profile and common $1-g_c^{\rm sc}$--identity--$g_c^{\rm sc}$ chain. |
| [`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md) | Proven | Exact residuals, backward identity chain, stronger center margin, and quarter terminal transfer. |
| [`4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md`](4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md) | Proven | Exact residuals, identity propagation, and Vd-specific terminal margin. |
| [`4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`](4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md) | Proven | Replaces the exceptional pair by two ordinary nonsupercritical Vd0 rows. |
| [`4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md) | Proven | Exhaustive placement assembly. |
| [`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md) | Proven | Existing Strategy 1 perimeter proof; unchanged. |
| [`414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md`](414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md) | Proven | Existing Strategy 1 skeleton proof; unchanged. |
