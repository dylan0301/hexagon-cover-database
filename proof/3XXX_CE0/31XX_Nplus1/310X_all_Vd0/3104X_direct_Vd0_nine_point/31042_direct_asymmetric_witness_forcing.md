# Direct Asymmetric-Witness Forcing

Status: Proven

This note extracts from the six-point and residual-core packages exactly the
three off-axis witnesses needed by the direct proof.  It excludes them from
the six actual open vertex roles.  No $AB$-union for a nonsupercritical row
is used.

## Setup and exact witnesses

Use strict handoffs

$$
X_i=V_i+x_i(V_{i+1}-V_i)
$$

such that

$$
X_i\in T_i\cap T_{i+1}.
$$

Equivalently, $V_i,X_{i-1},X_i\in T_i$ for every $i$.  Assume

$$
x_3<x_2<x_1<x_0<x_5<x_4.
\tag{1}
$$

Put

$$
a=1-x_3,
\qquad b=x_4.
\tag{2}
$$

The strict ascent at row $4$ gives $a+b>1$.  Moreover,
$X_3,X_4\in T_4$, so the distance between these two points of the open unit
triangle is strictly less than $1$.  In the local coordinates at $V_4$,
its square is $a^2+ab+b^2$.  Therefore

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1.
\tag{3}
$$

At $V_4$, write

$$
P=V_4+u(V_5-V_4)+v(V_3-V_4).
$$

Let

$$
Q_-(a,b),
\qquad Q_0(a,b),
\qquad Q_+(a,b)
\tag{4}
$$

be the exact points defined in Section 1 of
[`31033_asymmetric_witness_construction.md`](../3103X_residual_core/31033_asymmetric_witness_construction.md).
Thus $Q_0$ is the junction of the two strict frontier lines, while $Q_-$
and $Q_+$ are the first intersections with the relaxed left and right unit
circles.  The row-$4$ source union in these coordinates is

$$
\mathcal U_{AB}(b,a),
$$

with the outgoing demand first.

## Theorem

Let $T_0,\dots,T_5$ be the actual open unit vertex-role triangles above.
Then

$$
Q_-,Q_0,Q_+
\in
\mathrm{int}(H)\setminus\bigcup_{i=0}^5T_i.
\tag{5}
$$

Consequently, if $T_C,T_0,\dots,T_5$ cover $H$, all three points in (4)
belong to $T_C$.

## Proof

### 1. Interior membership

Section 2 of `31033` proves from the exact frontier formulas that every
witness has local coordinates

$$
0<u,v<1
$$

and satisfies the strict local hexagon inequalities.  Hence

$$
Q_-,Q_0,Q_+\in\mathrm{int}(H).
\tag{6}
$$

### 2. The distinguished role $T_4$

The strict frontier theorem
[`20091_ab_union_curve_a_plus_b_gt_1.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md)
and equations (5)--(6) of `31033` put all three witnesses on the exact
non-axis frontier of the cone-clipped row-$4$ union.  Their local coordinates
satisfy $u,v>0$.

The closed triangle $\overline{T_4}$ is one of the unit triangles represented
in that union because it contains $V_4,X_3,X_4$.  If a witness belonged to
the open triangle $T_4$, a sufficiently small plane ball about it would lie
both in $T_4$ and in the interior of the corner cone.  The witness would then
be an interior point of the union, contrary to its frontier membership.
Therefore

$$
Q_-,Q_0,Q_+\notin T_4.
\tag{7}
$$

This is the only row in the proof for which an $AB$-union is used.

### 3. The roles $T_0,T_1,T_2$

Equations (12)--(16) of `31033` are direct distance calculations from the
three vertices.  They give

$$
\left\lVert Q_\nu-V_j\right\rVert>1
\qquad
(\nu\in\{-,0,+\},\ j\in\{0,1,2\}).
\tag{8}
$$

Since $V_j\in T_j$ and two points of an open unit equilateral triangle have
distance strictly less than $1$, equation (8) excludes every witness from
$T_0,T_1,T_2$.

### 4. The moving adjacent role $T_5$

The actual handoff in $T_5$ is

$$
X_5=V_5+x_5(V_0-V_5).
$$

Equation (1) gives

$$
1-a=x_3<x_5<b=x_4.
\tag{9}
$$

In the notation of
[`31012_core_graph_two_variable_relaxation.md`](../3101X_six_point/31012_core_graph_two_variable_relaxation.md),
the corresponding moving circle has center

$$
E_5(t)=V_5+t(V_0-V_5),
\qquad t=x_5.
$$

The proved fixed-line certificate there gives all three required signs:

- first-root monotonicity puts $Q_+=P_5(1-a)$ at or before the actual first
  root, so $\lVert Q_+-X_5\rVert\ge1$;
- the junction-outside-circle calculation gives
  $\lVert Q_0-X_5\rVert>1$; and
- the no-opposite-line-intersection calculation gives
  $\lVert Q_--X_5\rVert>1$.

Thus

$$
Q_-,Q_0,Q_+\notin T_5.
\tag{10}
$$

### 5. The reflected adjacent role $T_3$

The actual handoff in $T_3$ is

$$
X_2=V_2+x_2(V_3-V_2).
$$

Putting $y=1-x_2$, equation (1) gives

$$
1-b<y<a.
$$

The reflected fixed-line certificate in `31012` gives

$$
\lVert Q_--X_2\rVert\ge1,
\qquad
\lVert Q_0-X_2\rVert>1,
\qquad
\lVert Q_+-X_2\rVert>1.
\tag{11}
$$

Since $X_2\in T_3$, equation (11) excludes all three witnesses from $T_3$.

Equations (6)--(11) prove (5).  Under a full cover of $H$, the only remaining
role that can contain these interior points is $T_C$. $\square$
