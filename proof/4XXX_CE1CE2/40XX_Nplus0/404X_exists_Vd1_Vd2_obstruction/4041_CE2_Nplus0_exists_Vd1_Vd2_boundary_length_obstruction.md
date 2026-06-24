# CE2, $N_+=0$, Exists Vd1/Vd2 Boundary-Length Obstruction

Status: Practically proven

Assume a hypothetical seven-open-unit-triangle cover has role triangles

$$
T_C,T_0,\dots,T_5,
$$

with

$$
T_C\text{ is CE2},
$$

$$
N_+=\left\lvert \left\lbrace i : a_i+b_i>1 \right\rbrace \right\rvert=0,
$$

and at least one $V_i$-triangle is Vd1 or Vd2.

This CE2 branch is obstructed by boundary length, using the boundary caps in
[`../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md).

## Boundary accounting

The open boundary $\partial H$ has length $6$.

For a normalized CE2 center role, the two active $C$-only boundary intervals
have total length

$$
(u-x)+(v-y)=\frac{D(1-D)}{S},\qquad S=x+y,\qquad D=\sqrt{x^2+xy+y^2}.
$$

The $O$-containment start-domain condition gives $S>1/2$, and
$D(1-D)\le1/4$, so the CE2 center contribution is less than $\frac12$.

Choose one Vd1/Vd2 vertex role. In the reduced boundary-length accounting, its
boundary contribution is at most $\frac12$.

Because $N_+=0$, every remaining vertex row is nonsupercritical. Each
nonsupercritical row contributes at most $1$, so the other five vertex rows
contribute at most $5$.

Therefore the total boundary contribution is strictly less than

$$
\frac12+\frac12+5=6.
$$

This is incompatible with covering the length-$6$ open boundary. Hence the
CE2, $N_+=0$, exists Vd1/Vd2 branch cannot occur in the open-cover proof tree,
subject to the practically proven boundary caps cited above.
