# CE2, $N_+=1$, At Least Two Vd1/Vd2 Boundary-Length Obstruction

Status: Proven

Assume a hypothetical cover has a CE2 center role, exactly one supercritical
vertex V triangle, and at least two Vd1 or Vd2 V triangles.

Vd1/Vd2 and T3-like V triangles are nonsupercritical, so the unique supercritical V triangle
is Vd0.  The common center theorem
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
and the boundary caps in
[`2500`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md)
give

$$
L_{\partial H}(T_C)<\frac12,
$$

$$
L_{\partial H}(T_{\mathrm{Vd1/Vd2},j})<\frac12
\qquad(j=1,2),
$$

and

$$
L_{\partial H}(T_{\mathrm{supercritical}})
\le
\frac2{\sqrt3}.
$$

Every remaining V triangle is nonsupercritical and contributes at most $1$ to the
boundary.  Thus the total available boundary length is strictly less than

$$
\frac12+\frac12+\frac12+\frac2{\sqrt3}+3
=
\frac92+\frac2{\sqrt3}
<6.
$$

This contradicts perimeter coverage.  Therefore the CE2, $N_+=1$,
at-least-two-Vd1/Vd2 branch is impossible.

$$
\Box
$$
