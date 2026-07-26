# CE2, $N_+=1$, Vd2 Neighbor-Midpoint Rescue Obstruction

Status: Proven

Assume a reduced CE2, $N_+=1$ candidate has exactly one Vd1/Vd2 row, that row
is Vd2 and contains a neighboring midpoint, and every other vertex row is
Vd0.

The Vd2 neighbor-midpoint theorem
[`2015`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2015_Vd2_neighbor_midpoint_cap.md)
gives the strict boundary cap

$$
L_{\partial H}(T_{\mathrm{Vd2}})<\frac13.
$$

The common center-budget theorem
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
and the vertex caps in
[`2500`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md)
give

$$
L_{\partial H}(T_C)<\frac12,
$$

$$
L_{\partial H}(T_{\mathrm{supercritical}})
\le
\frac2{\sqrt3},
$$

and a contribution at most $1$ from each of the other four nonsupercritical
rows.  Therefore the total available boundary length is strictly less than

$$
\frac12+\frac13+\frac2{\sqrt3}+4<6.
$$

The final inequality is equivalent to $12<7\sqrt3$, and follows after
squaring from $144<147$.  This contradicts perimeter coverage, so the Vd2
neighbor-midpoint rescue branch is impossible.

$$
\Box
$$
