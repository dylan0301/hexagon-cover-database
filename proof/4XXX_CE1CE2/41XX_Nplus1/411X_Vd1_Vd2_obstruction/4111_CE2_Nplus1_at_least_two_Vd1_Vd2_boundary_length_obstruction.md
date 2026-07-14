# CE2, $N_+=1$, At Least Two Vd1/Vd2 Boundary-Length Obstruction

Status: Proven

Assume a hypothetical seven-open-unit-triangle cover has role triangles

$$
T_C,T_0,\dots,T_5,
$$

with

$$
T_C\text{ is CE2},
$$

$$
N_+=\left\lvert \left\lbrace i : a_i+b_i>1 \right\rbrace \right\rvert=1,
$$

and at least two $V_i$-triangles are Vd1 or Vd2.

This CE2 branch is obstructed by boundary length, using the boundary caps in
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

For a normalized CE2 center role, the two full CE2 boundary intervals have
total length

$$
(u-x)+(v-y)=\frac{D(1-D)}{S},\qquad S=x+y,\qquad D=\sqrt{x^2+xy+y^2}.
$$

The $O$-containment start-domain condition gives $S>1/2$, and
$D(1-D)\le1/4$, so the CE2 center contribution is less than $\frac12$.

Choose two Vd1/Vd2 vertex roles. Each has full boundary trace strictly less
than $\frac12$.

The boundary caps show that Vd1, Vd2, and T3-like rows are nonsupercritical.
Hence the unique supercritical row is Vd0. It has boundary contribution at
most $\frac2{\sqrt3}$, and each of the other three rows contributes at most
$1$.

Therefore

$$
L_C+\sum_{i=0}^5L_i
<\frac12+\frac12+\frac12+\frac2{\sqrt3}+3
=\frac92+\frac2{\sqrt3}<6.
$$

This is incompatible with covering the length-$6$ open boundary. Hence the
CE2, $N_+=1$, at-least-two-Vd1/Vd2 branch cannot occur in the open-cover proof
tree.
