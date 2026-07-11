# Relaxed-P Six-Point Core Construction

Status: Definition

This file defines the relaxed six-point obstruction set used in the CE0,
$N_+=1$, all-Vd0 core graph.  The construction keeps the strict row
$R_4(a,b)$ fixed and replaces the two moving circle centers for $P_3$ and
$P_5$ by the relaxed endpoint centers determined by the two variables

$$
a=a_4,\qquad b=b_4.
$$

The reduction proof and strict fixed-line monotonicity certificate are recorded
in [`31012_core_graph_two_variable_relaxation.md`](31012_core_graph_two_variable_relaxation.md).
This file records definitions only; it does not prove that the final two-variable
surface gives an obstruction for every point of the domain.

## Hexagon coordinates

Let $H$ be the side-$1$ regular hexagon with center $O=0$ and vertices
$V_0,\dots,V_5$ in cyclic order.  Indices are modulo $6$.  For an edge
parameter $x_i\in[0,1]$, write

$$
X_i=V_i+x_i(V_{i+1}-V_i).
$$

The row convention is

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

Thus $X_i$ is the outgoing $b_i$ point for the row at $V_i$ and the incoming
$a_{i+1}$ point for the row at $V_{i+1}$.

At $V_4$, use the outgoing and incoming unit edge directions

$$
e_+=V_5-V_4,\qquad e_-=V_3-V_4.
$$

A point near $V_4$ has local coordinates $(u,v)$ when

$$
P=V_4+u e_+ + v e_-.
$$

The local metric is

$$
Q(u,v)=u^2+v^2-uv.
$$

The strict row data are

$$
a=a_4,\qquad b=b_4.
$$

The incoming and outgoing edge points of the preserved $V_4$ row are

$$
A(a)=V_4+a(V_3-V_4)=V_3+(1-a)(V_4-V_3),
$$

and

$$
B(b)=V_4+b(V_5-V_4).
$$

The graph domain is

$$
\mathcal D=\left\{(a,b):0\le a\le1,\ 0\le b\le1,\ a+b>1,\ a^2+ab+b^2\le1\right\}.
$$

Set

$$
r=b,\qquad s=a,\qquad \rho=r^2+rs+s^2.
$$

## The preserved row and the strict two-line model

The set $R(a,b)$ is the $V_4$-placed copy of the local $AB$-union set
$\mathcal U_{AB}(b,a)$ recorded in
[`../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md).
In that source note, the first cone direction is $e_+$ and the second cone
direction is $e_-$.  Thus the marked points are $(b,0)$ and $(0,a)$ in the
local coordinates of this file.

For the strict nondegenerate branch

$$
r+s>1,\qquad \rho<1,
$$

let

$$
h=\frac{\sqrt3}{2},\qquad D=\sqrt{4\rho-3}.
$$

Define

$$
\alpha=\frac{h(r+2s-rD)}{2\rho},\qquad
\beta=\frac{h(r-s+(r+s)D)}{2\rho},
$$

$$
\gamma=\frac{h(-r+s+(r+s)D)}{2\rho},\qquad
\delta=\frac{h(2r+s-sD)}{2\rho},
$$

and

$$
\Omega=\alpha\delta-\gamma\beta.
$$

The two non-axis line sides of the strict two-line model lie on

$$
\alpha(u-r)+\beta v=0,
$$

and

$$
\gamma u+\delta(v-s)=0.
$$

Their junction is

$$
u_J=\frac{\delta(r\alpha-s\beta)}{\Omega},\qquad
v_J=\frac{\alpha(s\delta-r\gamma)}{\Omega}.
$$

Let

$$
J(a,b)=V_4+u_J e_+ + v_J e_-.
$$

The strict two-line superset $R^{\mathrm{lin}}(a,b)$ is the closed polygonal
local region with vertices

$$
(0,0),\qquad
\left(0,\frac{\alpha r}{\beta}\right),\qquad
(u_J,v_J),\qquad
\left(\frac{\delta s}{\gamma},0\right).
$$

It is used only in the strict nondegenerate branch $\rho<1$.  On the boundary
$\rho=1$, the line-line junction is interpreted as its limiting point, which is
collinear with the limiting $P_3^{\mathrm{rel}}$ and $P_5^{\mathrm{rel}}$.

Let $\partial_{\mathrm{na}}R^{\mathrm{lin}}(a,b)$ denote the non-axis part of
the boundary, namely the part with local coordinates $u>0$ and $v>0$.  In the
strict branch this is the union of the two line sides meeting at $J(a,b)$.

## Relaxed circle centers

In relaxed-P mode the preserved region is still $R_4(a,b)$ or its strict
two-line superset $R^{\mathrm{lin}}(a,b)$, but the two circle centers are virtual
endpoint centers.

For $P_3^{\mathrm{rel}}$, use

$$
X_2^{\mathrm{rel}}(b)=V_2+b(V_3-V_2).
$$

In $V_4$-local coordinates this is

$$
X_2^{\mathrm{rel}}(b)=(1-b,2-b).
$$

For $P_5^{\mathrm{rel}}$, use

$$
X_5^{\mathrm{rel}}(a)=V_5+(1-a)(V_0-V_5).
$$

In $V_4$-local coordinates this is

$$
X_5^{\mathrm{rel}}(a)=(2-a,1-a).
$$

Define the relaxed radius-$1$ circles

$$
C_2^{\mathrm{rel}}(b)=\left\{P:\left\lVert P-X_2^{\mathrm{rel}}(b)\right\rVert=1\right\},
$$

and

$$
C_5^{\mathrm{rel}}(a)=\left\{P:\left\lVert P-X_5^{\mathrm{rel}}(a)\right\rVert=1\right\}.
$$

These are the circles obtained by pretending that the nonsupercritical chain
has been pushed to the endpoint equalities on the opposite side of the preserved
$V_4$ row.

## The relaxed $P$ points

If

$$
\partial_{\mathrm{na}}R^{\mathrm{lin}}(a,b)\cap C_2^{\mathrm{rel}}(b)
$$

is nonempty in the strict branch $\rho<1$, define $P_3^{\mathrm{rel}}(a,b)$ to
be the point in this intersection closest to $V_4$ in the metric $Q$.  If this
selected non-axis intersection is absent but $a^2+ab+b^2\le1$, use the
point-on-edge fallback

$$
P_3^{\mathrm{rel}}(a,b)=A(a).
$$

If

$$
\partial_{\mathrm{na}}R^{\mathrm{lin}}(a,b)\cap C_5^{\mathrm{rel}}(a)
$$

is nonempty in the strict branch $\rho<1$, define $P_5^{\mathrm{rel}}(a,b)$ to
be the point in this intersection closest to $V_4$ in the metric $Q$.  If this
selected non-axis intersection is absent but $a^2+ab+b^2\le1$, use the
point-on-edge fallback

$$
P_5^{\mathrm{rel}}(a,b)=B(b).
$$

In the strict branch, the monotonicity certificate in
[`31012_core_graph_two_variable_relaxation.md`](31012_core_graph_two_variable_relaxation.md)
proves that the relaxed non-axis intersections exist and the fallbacks are not
used.

## The point $P_4$

For $\rho<1$, define

$$
P_4(a,b)=J(a,b).
$$

For $\rho=1$, define $P_4(a,b)$ as the limiting line-line junction.  The
limiting non-axis boundary is a single line segment, and
$P_3^{\mathrm{rel}},P_4,P_5^{\mathrm{rel}}$ are collinear on this segment.
Thus $P_4$ is redundant for the convex hull relevant to the minimal enclosing
equilateral triangle, but the notation $K_6^{\mathrm{rel}}(a,b)$ is still used.

## The three diagonal points

Set

$$
p=1-b,\qquad q=1-a.
$$

Let

$$
c_*=c_{\max}(p,q),
$$

where $c_{\max}(\alpha,\beta)$ is the admissible-set radial envelope from
[`../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md).
In that note, its arguments are lower-bound edge demands.

For $j=0,1,2$, define

$$
D_j(a,b)=(1-c_*)V_j.
$$

These are the algorithm-2 diagonal points used in the relaxed two-variable core
set.

## Relaxed selected set

The relaxed six-point set is

$$
K_6^{\mathrm{rel}}(a,b)=
\left\{P_3^{\mathrm{rel}}(a,b),P_4(a,b),P_5^{\mathrm{rel}}(a,b),D_0(a,b),D_1(a,b),D_2(a,b)\right\}.
$$

On the boundary $\rho=1$, the collinear point $P_4$ does not change
$\mathrm{conv}\ K_6^{\mathrm{rel}}(a,b)$ or $\Lambda(K_6^{\mathrm{rel}}(a,b))$.
The selected set is determined only by the two variables $(a,b)$.
