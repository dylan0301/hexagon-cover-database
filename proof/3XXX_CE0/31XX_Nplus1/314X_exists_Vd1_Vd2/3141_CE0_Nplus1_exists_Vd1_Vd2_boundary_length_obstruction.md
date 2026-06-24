# CE0, $N_+=1$, Exists Vd1/Vd2 Boundary-Length Obstruction

Status: Practically proven

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

The open boundary $\partial H$ has length $6$. Since $T_C$ is CE0, it
contributes no positive-length boundary interval.

Choose one Vd1/Vd2 vertex role. In the reduced boundary-length accounting, its
boundary contribution is at most $\frac12$; see
[../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md).

Among the remaining five vertex rows, at most one is supercritical. A
non-supercritical row contributes at most $1$. The possible supercritical row
has contribution at most $\frac2{\sqrt3}$ in the Vd0 case, at most $1$ in the
T3-like case, and at most $\frac12$ in the Vd1/Vd2 case. Hence the worst
remaining contribution is bounded by

$$
4+\frac2{\sqrt3}.
$$

Therefore the total boundary contribution is at most

$$
\frac12+4+\frac2{\sqrt3}=\frac92+\frac2{\sqrt3}<6.
$$

This is incompatible with covering the length-$6$ open boundary. Hence the
CE0, $N_+=1$, exists Vd1/Vd2 branch cannot occur in the open-cover proof tree,
subject to the practically proven boundary caps cited above.
