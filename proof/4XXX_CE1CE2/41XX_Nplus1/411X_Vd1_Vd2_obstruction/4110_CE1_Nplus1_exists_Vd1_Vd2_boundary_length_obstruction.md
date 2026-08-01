# CE1, $N_+=1$, Exists Vd1/Vd2 Boundary-Length Obstruction

Status: Proven

Assume a hypothetical cover has a CE1 center role, exactly one supercritical
vertex V triangle, and at least one Vd1 or Vd2 V triangle.

A Vd1/Vd2 V triangle is nonsupercritical, and T3-like V triangles are also
nonsupercritical.  Hence the unique supercritical V triangle is Vd0.  The boundary
caps in
[`2500`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md)
and the signed center theorem
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
give

$$
L_{\partial H}(T_C)
\le
\frac{\sqrt3}{2}-\frac34,
$$

$$
L_{\partial H}(T_{\mathrm{Vd1/Vd2}})<\frac12,
$$

and

$$
L_{\partial H}(T_{\mathrm{supercritical}})
\le
\frac2{\sqrt3}.
$$

Every remaining V triangle is nonsupercritical and has boundary contribution at most
$1$.  Therefore the total available boundary length is strictly less than

$$
\left(\frac{\sqrt3}{2}-\frac34\right)
+
\frac12
+
\frac2{\sqrt3}
+4
<6.
$$

This contradicts perimeter coverage.  Therefore the CE1, $N_+=1$,
exists-Vd1/Vd2 branch is impossible.

$$
\Box
$$
