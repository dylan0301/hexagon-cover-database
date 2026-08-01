# CE1, $N_+=0$, Exists Vd1/Vd2 Boundary-Length Obstruction

Status: Proven

Assume a hypothetical cover has a CE1 center role, no supercritical vertex
V triangle, and at least one Vd1 or Vd2 V triangle.

The signed center-budget theorem
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
gives

$$
L_{\partial H}(T_C)
\le
\frac{\sqrt3}{2}-\frac34
<\frac12.
$$

Choose one Vd1/Vd2 V triangle.  The boundary cap in
[`2500`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md)
gives its strict contribution bound

$$
L_{\partial H}(T_{\mathrm{Vd1/Vd2}})<\frac12.
$$

Every other vertex V triangle is nonsupercritical.  By the exhaustive type
classification, each such V triangle is Vd0, Vd1, Vd2, or T3-like, and every one of
these types has boundary contribution at most $1$.  Hence the total available
boundary length is strictly less than

$$
\frac12+\frac12+5=6.
$$

This contradicts coverage of the side-one hexagon perimeter, whose length is
$6$.  Therefore the CE1, $N_+=0$, exists-Vd1/Vd2 branch is impossible.

$$
\Box
$$
