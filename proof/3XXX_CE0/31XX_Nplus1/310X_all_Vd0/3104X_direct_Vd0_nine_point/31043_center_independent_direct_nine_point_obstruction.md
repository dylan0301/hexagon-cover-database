# Center-Independent Direct Nine-Point Obstruction

Status: Proven

This theorem is the simplified all-Vd0 closure.  It replaces the comparison
of six model $AB$-unions by direct exclusions from the six actual open vertex
roles.

## Theorem

The side-one regular hexagon $H$ has no cover by open unit equilateral
triangles

$$
T_C,T_0,\dots,T_5
$$

such that

1. $T_i$ is a Vd0 role at $V_i$ for every $i$;
2. $T_0,\dots,T_5$ cover $\partial H$; and
3. exactly one actual maximal boundary row is supercritical.

No center class is assumed for $T_C$.

## Proof

### 1. Strict exact-one handoffs

Apply the exact-one case of
[`1214_strict_boundary_handoff_selection.md`](../../../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md).
It gives points

$$
X_i=V_i+x_i(V_{i+1}-V_i),
\qquad 0<x_i<1,
$$

covered by both endpoint roles, and selected row demands

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

Exactly one selected row is supercritical, at the same index as the unique
supercritical actual row.  Rotate the indices so that this is row $4$.
Every other selected row is strictly nonsupercritical, and therefore

$$
x_3<x_2<x_1<x_0<x_5<x_4.
\tag{1}
$$

Set

$$
a=1-x_3,
\qquad b=x_4,
\qquad p=1-b,
\qquad q=1-a.
\tag{2}
$$

The strict supercritical inequality gives $a+b>1$.  The anchors $X_3,X_4$
belong to the open unit triangle $T_4$, and their squared distance is

$$
\lVert X_3-X_4\rVert^2=a^2+ab+b^2<1.
$$

Thus

$$
0<a,b<1,
\qquad a+b>1,
\qquad a^2+ab+b^2<1.
\tag{3}
$$

Moreover, (1) gives for every row

$$
a_i\ge p,
\qquad b_i\ge q.
\tag{4}
$$

### 2. Six directly forced radial points

Put

$$
c_*=c_{\max}(p,q),
\qquad
D_i=(1-c_*)V_i.
\tag{5}
$$

The direct radial-forcing theorem
[`31041_direct_radial_forcing.md`](31041_direct_radial_forcing.md), applied
to (1), proves that no vertex role contains any $D_i$.  The full cover hence
forces

$$
D_0,\dots,D_5\in T_C.
$$

By convexity, $T_C$ contains the centered closed disk

$$
\mathcal D_\eta
=
\left\{P:\lVert P\rVert\le\eta\right\},
\qquad
\eta=\frac{\sqrt3}{2}(1-c_*).
\tag{6}
$$

### 3. Three directly forced asymmetric points

Let

$$
Q_-(a,b),
\qquad Q_0(a,b),
\qquad Q_+(a,b)
$$

be the exact witnesses from `31033`.  The direct asymmetric-forcing theorem
[`31042_direct_asymmetric_witness_forcing.md`](31042_direct_asymmetric_witness_forcing.md)
uses the actual handoffs $X_2,X_5$, direct vertex distances, and only the
unique strict-row $AB$-frontier to prove

$$
Q_-,Q_0,Q_+\in T_C.
\tag{7}
$$

Combining (6)--(7), the center role contains the compact set

$$
K_{\mathrm{wit}}(a,b)
=
\mathcal D_\eta\mathbin\cup\{Q_-(a,b),Q_0(a,b),Q_+(a,b)\}.
\tag{8}
$$

Equivalently, the nine directly forced points are

$$
D_0,\dots,D_5,Q_-,Q_0,Q_+.
$$

The convex hull of these nine points contains the set in (8).

### 4. Terminal enclosure contradiction

For a compact set $K$, let $\Lambda(K)$ be the least side length of a closed
equilateral triangle containing $K$.  The terminal cap reduction and analytic
adjacent-overlap proof are in
[`31034_witness_enclosure_inequality.md`](../3103X_residual_core/31034_witness_enclosure_inequality.md),
and the two mixed overlaps are completed without interval arithmetic in
[`31037_rational_cmax_upper_envelope.md`](../3103X_residual_core/31037_rational_cmax_upper_envelope.md).
Together they prove throughout the strict domain (3) that

$$
\Lambda\left(K_{\mathrm{wit}}(a,b)\right)\ge1.
\tag{9}
$$

On the other hand, (8) puts this compact set inside the open unit
equilateral triangle $T_C$.  The compact set has positive distance from
each of the three sides.  Moving all three sides inward by a smaller amount
produces a closed equilateral triangle of side strictly less than $1$ that
still contains the set.  Therefore

$$
\Lambda\left(K_{\mathrm{wit}}(a,b)\right)<1,
$$

contradicting (9).  This proves the theorem. $\square$

## Simplification audit

The proof uses all-Vd0 precisely in `31041`, where it excludes a radial
witness from the two adjacent actual roles.  It uses no $AB$-union for any
nonsupercritical row.  In particular, the proof does not require the
comparison

$$
\mathcal C_{\mathrm{sym}}
\subseteq
\mathcal C_{\mathrm{asym}}
\subseteq
\mathcal U_6^\circ,
$$

the neighboring-ray maximum theorem `2008`, or the optional six-point
inequality $F_6\ge1$.  The unique supercritical frontier, the exact
fixed-line circle signs, the terminal reduction `31034`, and the exact
mixed-overlap completion `31037` remain essential.
