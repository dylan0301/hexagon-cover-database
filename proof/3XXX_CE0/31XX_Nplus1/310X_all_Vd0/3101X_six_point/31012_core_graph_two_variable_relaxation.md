# Core Graph Two-Variable Relaxation

Status: Lemma target

This file records the conditional relaxation target that reduces the six-point
core graph to the two variables

$$
a=a_4,\qquad b=b_4.
$$

It assumes the equality input

$$
a_3+b_3=1,\qquad a_5+b_5=1,
$$

which is to be proved elsewhere.  This file does not prove those equalities or
close the CE0, $N_+=1$, all-Vd0 branch.

The point definitions used below are those of
[`31011_six_point_construction.md`](31011_six_point_construction.md).

## Lemma target

For each row $i$, let $R_i$ be the closed $AB$-union region determined by
$V_i,X_{i-1},X_i$, and let $R_i^{\mathrm{lin}}$ be the corresponding closed
two-line $AB$-superset from
[`31011_six_point_construction.md`](31011_six_point_construction.md).  Use the
boundary-included two-line red region

$$
U_{\mathrm{red}}^{\mathrm{lin}}
=H\setminus\bigcup_{i=0}^5 \mathrm{int}\left(R_i^{\mathrm{lin}}\right).
$$

The target is to prove that, under the equality input above, the six selected
points from [`31011_six_point_construction.md`](31011_six_point_construction.md)
are contained in this red region and are determined only by $(a,b)$:

$$
K_6(a,b)\subset U_{\mathrm{red}}^{\mathrm{lin}},
$$

and

$$
K_6=K_6(a,b).
$$

The use of $\mathrm{int}\left(R_i^{\mathrm{lin}}\right)$ is intentional:
boundary points of the six two-line regions are included in
$U_{\mathrm{red}}^{\mathrm{lin}}$.  Since the two-line regions are larger than
the exact $AB$-union regions, this is the stronger red-containment target.

## Target domain

The two-variable domain is

$$
\mathcal D=\left\{(a,b):0\le a\le1, 0\le b\le1, a+b>1, a^2+ab+b^2\le1\right\}.
$$

The condition $a+b>1$ says that the displayed row $V_4$ is the unique
supercritical row.  The condition $a^2+ab+b^2\le1$ is the nonemptiness
condition for the local edge pair at $V_4$.

## Boundary-point collapse

Use edge parameters $x_i$ with

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

The row $V_4$ data give

$$
a_4=1-x_3=a,\qquad b_4=x_4=b.
$$

Thus

$$
x_3=1-a,\qquad x_4=b.
$$

The equality $a_3+b_3=1$ gives

$$
(1-x_2)+x_3=1,
$$

hence

$$
x_2=x_3=1-a.
$$

The equality $a_5+b_5=1$ gives

$$
(1-x_4)+x_5=1,
$$

hence

$$
x_5=x_4=b.
$$

Therefore the retained boundary points are

$$
X_2=V_2+(1-a)(V_3-V_2),
$$

$$
X_3=V_3+(1-a)(V_4-V_3)=A(a),
$$

$$
X_4=V_4+b(V_5-V_4)=B(b),
$$

and

$$
X_5=V_5+b(V_0-V_5).
$$

These are the centers and adjacent edge points used for $P_3,P_4,P_5$ in
[`31011_six_point_construction.md`](31011_six_point_construction.md).

## Strict fixed-line monotonicity for $P_5$

This subsection records the conditional monotonicity proof needed for the
$a_5+b_5=1$ equality reduction on the strict fixed-line branch.

Fix $X_0,\dots,X_4$ and move only

$$
X_5(t)=V_5+t(V_0-V_5).
$$

Equivalently, in local coordinates at $V_4$,

$$
X_5(t)=(1+t,t).
$$

Since $R_4^{\mathrm{lin}}$ is fixed, the points $P_3,P_4,D_0,D_1,D_2$ are
fixed during this motion.  Assume that, for $t$ in the interval considered,
$P_5(t)$ is always selected on the same non-axis line side of the fixed
two-line boundary of $R_4^{\mathrm{lin}}$, with no line-side switch and no
point-on-edge fallback.  Parametrize this line side by

$$
P_5(t)=P_4+s(t)w,\qquad s(t)\ge0,
$$

where increasing $s$ means moving away from $P_4$.

Let

$$
F(s,t)=\left\lVert P_4+s w-X_5(t)\right\rVert^2-1.
$$

The selected intersection satisfies

$$
F(s(t),t)=0.
$$

On the selected near-side root of this fixed line,

$$
F_s(s(t),t)<0.
$$

Also, as $X_5(t)$ moves in the direction $V_0-V_5$, the selected root lies on
the $V_4$-facing side of the moving circle.  Equivalently,

$$
F_t(s(t),t)>0.
$$

Differentiating $F(s(t),t)=0$ gives

$$
F_s(s(t),t)s'(t)+F_t(s(t),t)=0.
$$

Therefore

$$
s'(t)=-\frac{F_t(s(t),t)}{F_s(s(t),t)}>0.
$$

Thus $P_5(t)$ moves monotonically away from $P_4$ along the fixed two-line
boundary side as $X_5(t)$ moves toward $V_0$.

Let

$$
S=\left\{P_3,P_4,D_0,D_1,D_2\right\}.
$$

If $t_1\le t_2$, then the monotonicity gives

$$
P_5(t_1)\in[P_4,P_5(t_2)].
$$

Since $P_4\in S$,

$$
P_5(t_1)\in \mathrm{conv}\left(S\cup\left\{P_5(t_2)\right\}\right).
$$

Consequently,

$$
\mathrm{conv}\left(S\cup\left\{P_5(t_1)\right\}\right)
\subset
\mathrm{conv}\left(S\cup\left\{P_5(t_2)\right\}\right).
$$

This proves containmentwise growth of the six-point convex hull on the strict
fixed-line branch.  Line-side switches, missing intersections, axis hits, and
point-on-edge fallback cases are separate boundary cases for the
equality-reduction proof.

## Remaining-row relaxation target

Set

$$
p=1-b,\qquad q=1-a.
$$

The remaining free pair may be represented by $(a_1,b_1)$ with constraints

$$
p\le a_1,\qquad q\le b_1,\qquad a_1+b_1\le1.
$$

Equivalently, the feasible set is the triangle with vertices

$$
(p,q),\qquad (p,b),\qquad (a,q).
$$

These three vertices correspond to the three equality patterns among the
nonsupercritical rows $V_0,V_1,V_2$.  The relaxation target is that, for the
algorithm-2 diagonal points, all three patterns may be represented by the
common lower-bound pair

$$
(p,q)=(1-b,1-a).
$$

Using the admissible-set coordinate $c(\alpha,\beta)$ from
[`../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md),
the common diagonal coordinate is

$$
c_*=c(p,q),
$$

and the diagonal points are

$$
D_j=(1-c_*)V_j,\qquad j=0,1,2.
$$

Thus, once the equality input and this relaxation target are established, the
six selected points

$$
P_3,P_4,P_5,D_0,D_1,D_2
$$

depend only on the two variables $(a,b)$.
