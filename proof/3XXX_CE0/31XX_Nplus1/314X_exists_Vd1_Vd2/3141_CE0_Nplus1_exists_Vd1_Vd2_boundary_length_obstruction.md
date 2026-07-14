# CE0, $N_+=1$, Exists Vd1/Vd2 Boundary-Length Obstruction

Status: Proven

Assume a hypothetical seven-open-unit-triangle cover has role triangles

$$
T_C,T_0,\dots,T_5,
$$

with

$$
T_C\text{ is CE0},
$$

$$
N_+=\left\lvert \left\lbrace i : a_i+b_i>1 \right\rbrace \right\rvert=1,
$$

and at least one $V_i$-triangle is Vd1 or Vd2.

This branch is obstructed by boundary length.

## Boundary accounting

Pass to the closures of the seven original open roles and write

$$
L_C=\mathcal H^1(T_C\cap\partial H),
\qquad
L_i=\mathcal H^1(T_i\cap\partial H).
$$

If the open roles covered $\partial H$, subadditivity would give

$$
6\le L_C+\sum_{i=0}^5L_i.
$$

The open boundary $\partial H$ has length $6$. Since $T_C$ is CE0, it
contributes no positive-length boundary interval.

Choose one Vd1/Vd2 vertex role. Its full boundary trace is strictly less than
$\frac12$; see
[../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md).

The boundary caps also show that Vd1, Vd2, and T3-like rows are
nonsupercritical. Hence the unique supercritical row is Vd0 and lies among the
remaining five rows. Its contribution is at most $\frac2{\sqrt3}$, while each
of the other four rows contributes at most $1$. Thus the remaining
contribution is bounded by

$$
4+\frac2{\sqrt3}.
$$

Therefore

$$
L_C+\sum_{i=0}^5L_i
<\frac12+4+\frac2{\sqrt3}
=\frac92+\frac2{\sqrt3}<6.
$$

This is incompatible with covering the length-$6$ open boundary. Hence the
CE0, $N_+=1$, exists Vd1/Vd2 branch cannot occur in the open-cover proof tree.
