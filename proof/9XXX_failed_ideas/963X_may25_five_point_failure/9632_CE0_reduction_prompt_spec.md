# May 25 Reduction Prompt Specification

Status: Reference

This file records the self-contained May 25 five-point reduction specification
from `dylan0301/hexagon-cover-visual/proof2/conj0525-reduction-prompt.md` in
the notation of this repository.

It is a specification of a conjectural finite-point obstruction, not a proof
that the obstruction holds.

Historical caveat: the source prompt mentions a conjectural full-skeleton
obstruction.  The standalone claim that seven unit triangles cannot cover the
full skeleton $S$ is refuted numerically in
`../908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md`.  This file records
only the May 25 reduced five-point target.

## 1. Geometry

Let $H$ be the regular hexagon of side length $1$, centered at

$$
O=(0,0).
$$

The vertices are

$$
V_i=\left(\cos\frac{i\pi}{3},\sin\frac{i\pi}{3}\right), \qquad i=0,\dots,5,
$$

with indices modulo $6$.  Let

$$
e_i=[V_i,V_{i+1}]
$$

be the boundary edge from $V_i$ to $V_{i+1}$.

The full skeleton is

$$
S=\partial H\cup [V_0,V_3]\cup [V_1,V_4]\cup [V_2,V_5].
$$

## 2. Boundary points and local coordinates

Choose one point on each boundary edge:

$$
X_i=V_i+t_i(V_{i+1}-V_i),\qquad 0\le t_i\le1.
$$

Set

$$
b_i=t_i,
$$

and

$$
a_i=1-t_{i-1}.
$$

Then

$$
a_i+b_i=1-t_{i-1}+t_i,
$$

so

$$
a_i+b_i=1\Longleftrightarrow t_i=t_{i-1}.
$$

At $V_i$, use local coordinates $(u,v)$ in the $120^\circ$ cone spanned by the
two boundary directions from $V_i$.  The coordinate $u$ points toward
$V_{i+1}$ and $v$ points toward $V_{i-1}$.  The metric is

$$
\|(u,v)\|^2=u^2+v^2-uv.
$$

In these coordinates,

$$
X_i=(b_i,0),\qquad X_{i-1}=(0,a_i).
$$

## 3. May 25 reduced slice

Assume the unique strict $AB$-union vertex is $V_4$:

$$
a_4+b_4>1.
$$

Use the May 21/22 equality reductions

$$
a_3+b_3=1,\qquad a_5+b_5=1.
$$

For the first three vertices assume only

$$
a_0+b_0\le1,\qquad a_1+b_1\le1,\qquad a_2+b_2\le1.
$$

There is no assumption that $a_1+b_1=1$.

In edge parameters, these conditions are

$$
t_3=t_2,\qquad t_5=t_4,
$$

and

$$
t_4>t_2,\qquad t_0\le t_5,\qquad t_1\le t_0,\qquad t_2\le t_1.
$$

## 4. $AB$-union regions

For each $i$, define $R_i$ to be the set of points $P\in H$ such that there
exists a closed unit equilateral triangle containing

$$
V_i,\qquad X_{i-1},\qquad X_i,\qquad P.
$$

Equivalently, in local coordinates at $V_i$, $R_i=R(a_i,b_i)$ is the set of all
$(u,v)$, $u,v\ge0$, that can be added to

$$
(0,0),\qquad (0,a_i),\qquad (b_i,0)
$$

inside one closed unit equilateral triangle.

Let

$$
U=H\setminus\bigcup_{i=0}^5 R_i.
$$

The candidate nondegenerate strict $AB$-union frontier formula, including the
two unit-circle arcs and two line segments, is recorded as a lemma target in
[../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md](../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md).
In the local predicate below, the two axis lengths are $\alpha$ and $\beta$.

The five-point construction uses all six sets $R_i$ when defining the three
diagonal points.

## 5. Local membership predicate

This predicate follows the May 25 axis convention: the outgoing boundary
length $b$ lies on the $u$-axis and the incoming boundary length $a$ lies on
the $v$-axis.  Set

$$
\alpha=b,\qquad \beta=a.
$$

Let

$$
A=(\alpha,0),\qquad B=(0,\beta),\qquad X=(u,v).
$$

If

$$
\alpha^2+\alpha\beta+\beta^2>1,
$$

then $R(a,b)=\varnothing$.  Otherwise $X\in R(a,b)$ if at least one of the
following conditions holds.

### Convex hull part

$$
\beta u+\alpha v\le\alpha\beta.
$$

### Fixed-side parts

$$
\max(\alpha+\beta,\alpha-u+v,u+\beta,v)\le1,
$$

or

$$
\max(\alpha+\beta,\beta-v+u,v+\alpha,u)\le1.
$$

### Moving side through $A$

Define

$$
D_A^2=(u-\alpha)^2+v^2-(u-\alpha)v,
$$

$$
P_A=\alpha(\alpha-u+v)+\beta v,\qquad Q_A=\alpha(\alpha-u),
$$

and

$$
S_A=\alpha(\alpha+\beta-u)+\beta(v-u).
$$

When $D_A>0$, set

$$
\ell_A= \max\left(D_A,\frac{P_A}{D_A}\right) - \min\left(0,\frac{Q_A}{D_A},\frac{S_A}{D_A}\right).
$$

The moving-side-through-$A$ condition is

$$
\ell_A\le1.
$$

### Moving side through $B$

Define

$$
D_B^2=u^2+(v-\beta)^2-u(v-\beta),
$$

$$
P_B=\beta(\beta-v+u)+\alpha u,\qquad Q_B=\beta(\beta-v),
$$

and

$$
S_B=\beta(\alpha+\beta-v)+\alpha(u-v).
$$

When $D_B>0$, set

$$
\ell_B= \max\left(D_B,\frac{P_B}{D_B}\right) - \min\left(0,\frac{Q_B}{D_B},\frac{S_B}{D_B}\right).
$$

The moving-side-through-$B$ condition is

$$
\ell_B\le1.
$$

## 6. The five points

Let $C_2$ be the radius-$1$ circle centered at $X_2$, and let $C_5$ be the
radius-$1$ circle centered at $X_5$.

Define $P_3$ to be the selected intersection point between the non-axis
boundary curve of $R_4$ and $C_2$.  Define $P_5$ analogously using $C_5$.

If there are multiple non-axis intersections, use the branch closest to $V_4$.
If one of these intersections does not exist, then the five-point
configuration is undefined for that parameter choice.

The other three points lie on the half-diagonals

$$
[O,V_0],\qquad [O,V_1],\qquad [O,V_2].
$$

If $O\notin U$, then the five-point configuration is undefined.  Otherwise,
for $j=0,1,2$, define

$$
\rho_j=\sup\{\rho\in[0,1]: \lambda V_j\in U \text{ for every }0\le \lambda<\rho\}.
$$

Then define

$$
D_j=\rho_j V_j.
$$

Thus $D_j$ is the point farthest from $O$ in the initial uncovered interval
along $[O,V_j]$.  It may lie on $\partial U$.

If the whole half-diagonal segment remains uncovered, then $D_j=V_j$.  If an
$R_i$ cuts $[O,V_j]$ before $V_j$, then $D_j$ is the first such boundary point.

The five obstruction points are

$$
P_3,\qquad P_5,\qquad D_0,\qquad D_1,\qquad D_2.
$$

## 7. Minimal enclosing equilateral triangle

For a finite set $K\subset\mathbb R^2$, define

$$
h_K(n)=\max_{x\in K} n\cdot x.
$$

For an angle $\theta$, define the three unit normal directions

$$
n_k(\theta)= \left( \cos\left(\theta+\frac{2\pi k}{3}\right), \sin\left(\theta+\frac{2\pi k}{3}\right) \right), \qquad k=0,1,2.
$$

The side length of the smallest equilateral triangle with these outward normal
directions that contains $K$ is

$$
L_K(\theta)=\frac{2}{\sqrt3}\sum_{k=0}^2 h_K(n_k(\theta)).
$$

The optimized enclosing side length is

$$
\Lambda(K)=\inf_{\theta\in[0,2\pi/3)}L_K(\theta).
$$

For the May 25 five-point set, write

$$
K_5=\{P_3,P_5,D_0,D_1,D_2\}
$$

and

$$
\Lambda_5=\Lambda(K_5).
$$

## 8. May 25 conjecture

For every parameter choice in the reduced slice of Section 3 for which all
five points are defined,

$$
\Lambda_5>1.
$$

Equivalently, no closed equilateral triangle of side length $1$ contains all
five points

$$
P_3,\qquad P_5,\qquad D_0,\qquad D_1,\qquad D_2.
$$

A proof of this conjecture would give the intended five-point obstruction
without assuming $a_1+b_1=1$, while still using the reductions

$$
a_3+b_3=1,\qquad a_5+b_5=1.
$$
