# Maximal C-Triangles Over the Half-Skeleton

Status: Definition / proof target, with proven normalized CE1 and CE2 subcases

A $C$-triangle is a closed unit equilateral triangle constrained to contain $O$.

Maximality is measured over

$$
S_{1/2}=\partial H\cup\{O,M_0,\dots,M_5\}.
$$

## CE0

$$
T_C\cap\partial H=\varnothing.
$$

Maximality is by midpoint coverage and complementary-distance domination.

## CE1

Normalize the unique edge overlap to $e_{0,1}$:

$$
T_C\cap e_{0,1}=[s_{01},t_{01}].
$$

Maximality is interval inclusion:

$$
[s,t]\preceq[s',t']\iff s'\le s,\quad t'\ge t.
$$

### CE1 exact midpoint subset $\{M_0\}$, normalized to $e_{0,1}$

The full proof and numerical check for the normalized target

$$
T_C\cap\{M_0,\dots,M_5\}=\{M_0\}, \qquad T_C\text{ has positive-length boundary overlap only on }e_{0,1},
$$

is recorded in
[`213_CE1_M0_e01_maximal_intervals.md`](213_CE1_M0_e01_maximal_intervals.md).

For this subcase, the maximal feasible intervals are exactly

$$
\boxed{\displaystyle [s,t]=[s,\sqrt{s^2-s+1}-(1-s)^2],\quad 0\lt s\lt 1}
$$

The endpoints $s=0$ and $s=1$ are limiting degeneracies, not feasible positive-length CE1 intervals.

## CE2

Normalize the two overlaps to adjacent edges:

$$
T_C\cap e_{5,0}=[s_{50},t_{50}],
$$

$$
T_C\cap e_{0,1}=[s_{01},t_{01}].
$$

Maximality is product interval inclusion:

$$
([s_{50},t_{50}],[s_{01},t_{01}])\preceq ([s'_{50},t'_{50}],[s'_{01},t'_{01}])
$$

iff both intervals are contained in the primed intervals.

### CE2 exact midpoint subset $\{M_0\}$, normalized to $e_{5,0}$ and $e_{0,1}$

The full proof and numerical check for the normalized target

$$
T_C\cap\{M_0,\dots,M_5\}=\{M_0\}, \qquad T_C\text{ has positive-length boundary overlap only on }e_{5,0}\text{ and }e_{0,1},
$$

is recorded in
[`214_CE2_M0_e50_e01_maximal_interval_pairs.md`](214_CE2_M0_e50_e01_maximal_interval_pairs.md).

Set

$$
x=s_{50},\qquad u=t_{50},\qquad y=s_{01},\qquad v=t_{01},
$$

and

$$
S=x+y, \qquad D=\sqrt{x^2+xy+y^2}.
$$

For this subcase, the maximal feasible interval pairs are exactly all pairs

$$
([s_{50},t_{50}],[s_{01},t_{01}])=([x,u],[y,v])
$$

satisfying

$$
0<x<u<1, \qquad 0<y<v<1,
$$

$$
(u+v)(x+y)-xy=\sqrt{x^2+xy+y^2},
$$

$$
u(x+y)\ge x, \qquad v(x+y)\ge y,
$$

and

$$
u(x+y)<x+\frac y2, \qquad v(x+y)<y+\frac x2.
$$

Every feasible pair in this semialgebraic surface is already maximal under product inclusion. In particular, the two edge intervals cannot be optimized independently.

This file supports the CE1/CE2 exactly-one-midpoint proof write-up.
