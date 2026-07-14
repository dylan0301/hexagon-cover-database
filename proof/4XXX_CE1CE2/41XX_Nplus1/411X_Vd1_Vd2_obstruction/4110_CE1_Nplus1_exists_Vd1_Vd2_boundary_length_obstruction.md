# CE1, $N_+=1$, Exists Vd1/Vd2 Boundary-Length Obstruction

Status: Proven

Assume a hypothetical seven-open-unit-triangle cover has role triangles

$$
T_C,T_0,\dots,T_5,
$$

with

$$
T_C\text{ is CE1},
$$

$$
N_+=\left\lvert \left\lbrace i : a_i+b_i>1 \right\rbrace \right\rvert=1,
$$

and at least one $V_i$-triangle is Vd1 or Vd2.

This CE1 branch is obstructed by boundary length, using the boundary caps in
[`../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md).

## Boundary accounting

Pass to the role closures and put

$$
L_C=\mathcal H^1(T_C\cap\partial H),
\qquad
L_i=\mathcal H^1(T_i\cap\partial H).
$$

If the open roles covered $\partial H$, then

$$
6\le L_C+\sum_{i=0}^5L_i.
$$

For a normalized CE1 center role, the full boundary trace has length at most

$$
\rho(1-\rho),\qquad \rho=\sqrt{s^2-s+1},\qquad 0<s<1.
$$

Since $\rho\ge\sqrt3/2$ and $\rho(1-\rho)$ is decreasing on
$[\sqrt3/2,1]$, this contribution is at most

$$
\frac{\sqrt3}{2}-\frac34.
$$

Choose one Vd1/Vd2 vertex role. Its full boundary trace is strictly less than
$\frac12$, so this row is not supercritical.

The boundary caps show that T3-like rows are also nonsupercritical. Therefore
the unique supercritical row is Vd0. It has boundary contribution at most
$\frac2{\sqrt3}$, and each of the other four rows contributes at most $1$.

Therefore

$$
L_C+\sum_{i=0}^5L_i
<\left(\frac{\sqrt3}{2}-\frac34\right)+\frac12+\frac2{\sqrt3}+4
=\frac{15}{4}+\frac{7}{2\sqrt3}<6.
$$

This is incompatible with covering the length-$6$ open boundary. Hence the
CE1, $N_+=1$, exists Vd1/Vd2 branch cannot occur in the open-cover proof tree.
