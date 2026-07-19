# Center-Independent Direct Nine-Point Obstruction

Status: Proven

## Theorem

The side-one regular hexagon $H$ has no cover by open unit equilateral
triangles

$$
U_C,U_0,\dots,U_5
$$

such that

1. $U_i$ is a Vd0 role at $V_i$ for every $i$;
2. $U_0,\dots,U_5$ cover $\partial H$; and
3. exactly one actual maximal boundary row is supercritical.

No center class is assumed for $U_C$.

## Proof

### 1. Strict exact-one handoffs

Apply the exact-one case of
[`1214_strict_boundary_handoff_selection.md`](../../../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md).
It gives strict handoff points

$$
X_i=V_i+x_i(V_{i+1}-V_i),
\qquad 0<x_i<1,
$$

with

$$
X_i\in U_i\cap U_{i+1},
$$

and selected row demands

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

Exactly one selected row is supercritical, at the same index as the unique
supercritical actual row.  Rotate the indices so that this is row $4$.
Every other selected row is strictly nonsupercritical.  Since

$$
a_i+b_i>1
\quad\Longleftrightarrow\quad
x_i>x_{i-1},
$$

the five strict descents and the unique ascent give

$$
x_3<x_2<x_1<x_0<x_5<x_4.
\tag{1}
$$

Set

$$
a=1-x_3,
\qquad
b=x_4,
\qquad
p=1-b=1-x_4,
\qquad
q=1-a=x_3.
\tag{2}
$$

The unique ascent gives $a+b>1$.  The two handoffs $X_3,X_4$ belong to the
open unit triangle $U_4$, and in the local $120$-degree corner coordinates at
$V_4$ their squared distance is

$$
\left\lVert X_3-X_4\right\rVert^2
=a^2+ab+b^2.
$$

Two points of an open unit equilateral triangle have distance strictly less
than $1$.  Hence

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1.
\tag{3}
$$

Equation (1) also says that every $x_j$ lies in $[x_3,x_4]$.  Therefore every
selected row satisfies the common lower bounds

$$
a_i=1-x_{i-1}\ge1-x_4=p,
\qquad
b_i=x_i\ge x_3=q.
\tag{4}
$$

### 2. The nine directly forced points

Let

$$
c_*=c_{\max}(p,q),
\qquad
D_i=(1-c_*)V_i,
\qquad
\eta=\frac{\sqrt3}{2}(1-c_*).
\tag{5}
$$

The direct radial-forcing theorem
[`31051_direct_radial_forcing.md`](31051_direct_radial_forcing.md), applied to
(1)--(4), proves that none of the six vertex roles contains any $D_i$.
Every $D_i$ lies in $\mathrm{int}(H)$, so the assumed cover forces

$$
D_0,\dots,D_5\in U_C.
$$

The six points form a regular hexagon of circumradius $1-c_*$.  Convexity of
$U_C$ consequently gives

$$
\mathcal D_\eta
=
\left\{P:\left\lVert P\right\rVert\le\eta\right\}
\subset U_C.
\tag{6}
$$

At the unique strict row, let

$$
Q_-(a,b),
\qquad Q_0(a,b),
\qquad Q_+(a,b)
$$

be the exact frontier witnesses defined in
[`31053_direct_asymmetric_witness_forcing.md`](31053_direct_asymmetric_witness_forcing.md).
That theorem uses the actual handoffs $X_2,X_5$, the complete fixed-line signs
from [`31052_fixed_line_circle_signs.md`](31052_fixed_line_circle_signs.md),
and direct vertex distances to prove

$$
Q_-,Q_0,Q_+
\in
\mathrm{int}(H)\setminus\bigcup_{i=0}^5U_i.
$$

The full cover therefore forces

$$
Q_-,Q_0,Q_+\in U_C.
\tag{7}
$$

Combining (6)--(7), the compact witness set

$$
K_{\mathrm{wit}}(a,b)
=
\mathcal D_\eta
\mathbin\cup
\left\{Q_-(a,b),Q_0(a,b),Q_+(a,b)\right\}
$$

satisfies

$$
K_{\mathrm{wit}}(a,b)\subset U_C.
\tag{8}
$$

Equivalently, the nine directly forced points are

$$
D_0,\dots,D_5,Q_-,Q_0,Q_+,
$$

and their convex hull contains the compact set in (8).

### 3. Exact terminal contradiction

For a compact plane set $K$, let $\Lambda(K)$ be the least side length of a
closed equilateral triangle containing $K$.  The terminal enclosure theorem
[`31057_terminal_nine_point_enclosure.md`](31057_terminal_nine_point_enclosure.md)
applies throughout the strict domain (3) and gives

$$
\Lambda\left(K_{\mathrm{wit}}(a,b)\right)\ge1.
\tag{9}
$$

On the other hand, (8) places this compact set inside the open unit
equilateral triangle $U_C$.  A compact subset of an open triangle has positive
distance from each of its three side lines.  Move all three sides inward by a
smaller common distance.  The resulting closed equilateral triangle still
contains $K_{\mathrm{wit}}(a,b)$ and has side length strictly less than $1$.
Thus

$$
\Lambda\left(K_{\mathrm{wit}}(a,b)\right)<1,
$$

contradicting (9).  This proves the theorem. $\square$

## Dependency audit

The Vd0 hypothesis is used to exclude each radial witness from its two
adjacent actual roles.  Only the unique supercritical row uses an $AB$-union.
No nonsupercritical model union, neighboring-ray maximum, model residual core,
interval subdivision, branch-and-bound, or optional six-point inequality is
used.
