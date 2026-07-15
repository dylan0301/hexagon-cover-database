# CE2, $N_+=1$, Vd2 Neighbor-Midpoint Rescue Obstruction

Status: Proven

## Statement

Assume a reduced CE2, $N_+=1$ candidate has exactly one Vd1/Vd2 row, that
row is Vd2 and contains a neighboring midpoint, and every other vertex row
is Vd0. Then the perimeter cannot be covered.

## Proof

The Vd2 neighbor-midpoint cap in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2015_Vd2_neighbor_midpoint_cap.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2015_Vd2_neighbor_midpoint_cap.md)
gives

$$
L_{\partial H}(T_{\mathrm{Vd2}})<\frac13.
$$

The boundary-length theorem
[`../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md)
gives the remaining caps:

$$
L_{\partial H}(T_C)<\frac12,
$$

$$
L_{\partial H}(T_{\mathrm{supercritical}})\le\frac2{\sqrt3},
$$

and each of the four nonsupercritical Vd0 rows contributes at most $1$.
Consequently the total available boundary length is strictly less than

$$
\frac12+\frac13+\frac2{\sqrt3}+4<6.
$$

The final inequality is equivalent to

$$
12<7\sqrt3,
$$

and follows by squaring: $144<147$. Since the side-one hexagon has perimeter
$6$, the seven role triangles cannot cover it.

$$
\Box
$$
