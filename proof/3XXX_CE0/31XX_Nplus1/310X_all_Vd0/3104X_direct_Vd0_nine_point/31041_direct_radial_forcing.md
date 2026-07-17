# Direct Vd0 Radial Forcing

Status: Proven

This note replaces the symmetric model-core comparison by a direct statement
about the six actual open vertex roles.

## Setup

Let $H$ be the side-one regular hexagon centered at $O=0$, with cyclic
vertices $V_0,\dots,V_5$.  Suppose open unit equilateral triangles
$T_0,\dots,T_5$ contain their corresponding vertices.  Let

$$
X_i=V_i+x_i(V_{i+1}-V_i),
\qquad 0<x_i<1,
$$

be strict handoff points such that $X_i\in T_i\cap T_{i+1}$.  The selected
incoming and outgoing demands of row $i$ are

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

Assume

$$
x_3<x_2<x_1<x_0<x_5<x_4.
\tag{1}
$$

Put

$$
p=1-x_4,
\qquad q=x_3,
\qquad c_*=c_{\max}(p,q),
\tag{2}
$$

where $c_{\max}$ is the exact radial envelope from
[`2004_admissible_set.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md).

## Theorem

If every $T_i$ is Vd0, then the six points

$$
D_i=(1-c_*)V_i,
\qquad i=0,\dots,5,
\tag{3}
$$

lie in none of the six open vertex roles.  Consequently, if
$T_C,T_0,\dots,T_5$ cover $H$, then

$$
D_0,\dots,D_5\in T_C,
\tag{4}
$$

and

$$
\mathcal D_\eta
=
\left\{P:\lVert P\rVert\le\eta\right\}
\subset T_C,
\qquad
\eta=\frac{\sqrt3}{2}(1-c_*).
\tag{5}
$$

## Proof

### 1. Common demand domination

Equation (1) says every $x_j$ belongs to $[x_3,x_4]$.  Hence, for every
row, including row $4$,

$$
a_i=1-x_{i-1}\ge1-x_4=p,
\qquad
b_i=x_i\ge x_3=q.
\tag{6}
$$

Also

$$
p>0,
\qquad q>0,
\qquad p+q<1.
\tag{7}
$$

In particular,

$$
p^2+pq+q^2<(p+q)^2<1,
$$

so the radial envelope in (2) is defined.

We record explicitly that

$$
0<c_*<1.
\tag{8}
$$

At $c=0$, the exact minimum-side formula in `2004` gives

$$
L_{\min}(p,q,0)=\sqrt{p^2+pq+q^2}<1.
$$

Continuity therefore gives an admissible positive value of $c$, so $c_*>0$.
At $c=1$, put $s=p+q$.  Since $0<p,q<1$ and $s<1$, the four support-contact
values in `2004` are

$$
1+q,
\qquad
1+p,
\qquad
\frac1{\sqrt{p^2-p+1}},
\qquad
\frac1{\sqrt{q^2-q+1}}.
$$

Each is strictly greater than $1$.  Thus $(p,q,1)$ is not admissible and
$c_*<1$, proving (8).

### 2. Exclusion from the matching role

Fix $i$.  In the local corner coordinates at $V_i$, the two edge directions
meet at $120$ degrees and their sum points from $V_i$ to $O$.  Thus the
radial demand $c$ is the global point $(1-c)V_i$.

Suppose $D_i\in T_i$.  By (8), $D_i$ lies in the relative interior of the
radial arm $OV_i$.  Since $T_i$ is open, there is an $\varepsilon>0$ with
$c_*+\varepsilon<1$ such that

$$
(1-c_*-\varepsilon)V_i\in T_i.
\tag{9}
$$

The triangle $T_i$ also contains $V_i,X_{i-1},X_i$.  By convexity and (6),
its closure contains the incoming and outgoing demand points at distances
$p$ and $q$ from $V_i$.  Together with (9), the closure is a closed unit
equilateral triangle containing the local demand set

$$
K(p,q,c_*+\varepsilon).
$$

Therefore $(p,q,c_*+\varepsilon)$ is admissible.  This contradicts the
definition of $c_*$, and hence

$$
D_i\notin T_i.
\tag{10}
$$

### 3. Exclusion from adjacent roles

For $T_{i-1}$ and $T_{i+1}$, the arm $OV_i$ is an adjacent radial arm.  If
one of these open roles contained $D_i$, a small plane ball about $D_i$
would contain a positive-length interval of $OV_i$.  The role would then
have positive-length intersection with an adjacent radial arm, contrary to
the Vd0 definition in
[`1201_V_triangle_types.md`](../../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).
Thus

$$
D_i\notin T_{i-1}\cup T_{i+1}.
\tag{11}
$$

### 4. Exclusion from nonadjacent roles

Write $r=1-c_*>0$.  For the two vertices at cyclic distance two,

$$
\left\lVert rV_i-V_{i\pm2}\right\rVert^2
=1+r+r^2>1.
\tag{12}
$$

For the opposite vertex,

$$
\left\lVert rV_i-V_{i+3}\right\rVert=1+r>1.
\tag{13}
$$

A unit equilateral triangle has diameter $1$.  Equations (12)--(13) exclude
$D_i$ from the remaining three vertex roles.  Together with (10)--(11), this
proves that no open vertex role contains $D_i$.

If the seven roles cover $H$, then $D_i\in\mathrm{int}(H)$ and the only
remaining covering role is $T_C$.  This proves (4).

Finally, the six points in (3) form a regular hexagon of circumradius
$1-c_*$.  Their convex hull contains its centered in-disk of radius
$\sqrt3(1-c_*)/2$.  Since the open triangle $T_C$ is convex, (4) implies
(5). $\square$
