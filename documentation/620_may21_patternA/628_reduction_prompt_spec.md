# May 21/22 Reduction Prompt Specification

Status: Reference

This file records the rigorous self-contained reduction specification from `jcpaik/hexagon-cover-visual/proof2/conj0521-reduction-prompt.md` in the notation of this repository.

It is a specification of the target and proof obligations, not a proof that the target holds.

Case context: In the current case tree, this specification is best read as a conditional fragment of the open $\mathrm{CE0}+\text{all Vd0}$ direction, after a prior reduction to the May 21/22 constrained slice with exactly one strict local vertex triangle, normalized at $V_4$.  It does not prove the full $\mathrm{CE0}+\text{all Vd0}$ case and does not establish the prior global monotonicity or equality reductions; it records the four-point Pattern A target and its proof obligations under those assumptions.

## 1. Geometry

Let $H$ be the regular hexagon of side length $1$, centered at

$$
O=(0,0).
$$

The vertices are

$$
V_i=\left(\cos\frac{i\pi}{3},\sin\frac{i\pi}{3}\right),\qquad i=0,\dots,5,
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

Historical context: the original global target was to prove that seven open equilateral triangles of side length $1$ cannot cover $S$. The May 24, 2026 counterexample in `../800_computation/811_skeleton_cover_counterexample.md` refutes this as a standalone target. This file only records the May 21/22 focused reduction target.

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

At $V_i$, use local coordinates $(u,v)$ in the $120^\circ$ cone spanned by the two boundary directions from $V_i$.  The coordinate $u$ points toward $V_{i+1}$ and $v$ points toward $V_{i-1}$.  The metric is

$$
\|(u,v)\|^2=u^2+v^2-uv.
$$

In these coordinates,

$$
X_i=(b_i,0),\qquad X_{i-1}=(0,a_i).
$$

## 3. AB-union region and strategic caveat

For each $i$, let $R_i$ be the set of points $P\in H$ such that there exists a closed unit equilateral triangle containing

$$
V_i,\quad X_{i-1},\quad X_i,\quad P.
$$

Equivalently, in local coordinates at $V_i$, $R_i=R(a_i,b_i)$ is the set of all $(u,v)$, $u,v\ge0$, that can be added to

$$
(0,0),\quad(0,a_i),\quad(b_i,0)
$$

inside one closed unit equilateral triangle.

The uncovered AB-union region is

$$
U=H\setminus\bigcup_{i=0}^5 R_i.
$$

Strategic caveat: although $R(a,b)$ is formally defined for all local values, the AB-union construction has intended proof-strategy meaning only for a triangle with $a+b>1$.  In the May 21/22 reduction, this is the unique strict triangle at $V_4$.  The other vertices enter through equality or $\le1$ constraints and through radial max-$c$ points.  They should not be treated as independent AB-union proof objects unless that use is separately justified.

For the nondegenerate strict frontier formula, with its two unit-circle arcs
and two line segments, see
[`../300_vertex_triangle/309_ab_union_curve_a_plus_b_gt_1.md`](../300_vertex_triangle/309_ab_union_curve_a_plus_b_gt_1.md).
In the local predicate below, the two axis lengths are $\alpha$ and $\beta$.

## 4. Exact local predicate for $R(a,b)$

Set

$$
\alpha=b,
\qquad
\beta=a.
$$

Let

$$
A=(\alpha,0),\qquad B=(0,\beta),\qquad X=(u,v).
$$

If

$$
\alpha^2+\alpha\beta+\beta^2>1,
$$

then $R(a,b)=\varnothing$.

Otherwise, $X\in R(a,b)$ if at least one of the following holds.

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
P_A=\alpha(\alpha-u+v)+\beta v,
\qquad
Q_A=\alpha(\alpha-u),
$$

and

$$
S_A=\alpha(\alpha+\beta-u)+\beta(v-u).
$$

For $D_A>0$, set

$$
\ell_A=\max\left(D_A,\frac{P_A}{D_A}\right)-\min\left(0,\frac{Q_A}{D_A},\frac{S_A}{D_A}\right).
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
P_B=\beta(\beta-v+u)+\alpha u,
\qquad
Q_B=\beta(\beta-v),
$$

and

$$
S_B=\beta(\alpha+\beta-v)+\alpha(u-v).
$$

For $D_B>0$, set

$$
\ell_B=\max\left(D_B,\frac{P_B}{D_B}\right)-\min\left(0,\frac{Q_B}{D_B},\frac{S_B}{D_B}\right).
$$

The moving-side-through-$B$ condition is

$$
\ell_B\le1.
$$

## 5. Local admissible set for radial max-$c$ points

Let

$$
\mathcal A\subset[0,1]^3
$$

be the local admissible set.  A triple $(a,b,c)\in\mathcal A$ means that a closed unit equilateral triangle containing $V_i$ can cover boundary lengths $a,b$ along the two adjacent edges and radial length $c$ along $[V_i,O]$.

For $a\le b$, the set is the union of three cells.

### Cell 1

$$
a\le b,
\qquad
a+b\le1,
\qquad
a^2+ab+b^2\le1,
$$

$$
(a+b)^4-(a+b)^2+ab\le0,
$$

$$
c^4-c^2+ac-a^2\le0.
$$

### Cell 2

$$
a\le b,
\qquad
a+b\le1,
\qquad
a^2+ab+b^2\le1,
$$

$$
(a+b)^4-(a+b)^2+ab\ge0,
$$

$$
((a+b)^2-1)c^2+bc-b^2\le0.
$$

### Cell 3

$$
a\le b,
\qquad
a+b\ge1,
\qquad
a^2+ab+b^2\le1,
$$

$$
(a^2-1)c^2+(2ab^2+b)c+(b^4-b^2)\le0,
$$

$$
c\le\frac12.
$$

For $a>b$, membership is defined by symmetry.

For each $i$, define

$$
c_i^{\max}=\max\{c\in[0,1]:(a_i,b_i,c)\in\mathcal A\},
$$

and

$$
G_i=(1-c_i^{\max})V_i.
$$

## 6. May 21/22 constrained slice

Assume exactly one $V$-triangle has $a_i+b_i>1$.  By rotation, take this index to be $4$.  The constrained slice is

$$
a_4+b_4>1,
$$

$$
a_1+b_1=a_3+b_3=a_5+b_5=1,
$$

and

$$
a_0+b_0\le1,
\qquad
a_2+b_2\le1.
$$

Equivalently, after writing

$$
p=t_0=t_1,
\qquad
q=t_2=t_3,
\qquad
r=t_4=t_5,
$$

one has

$$
q<r,
\qquad
q\le p\le r.
$$

The intended monotonicity claim leading to this constrained slice is not assumed as proven in this repository package.

## 7. Four-point construction

Let

$$
R_4=R(a_4,b_4)=R(1-q,r).
$$

Let $C_2$ be the radius-$1$ circle centered at $X_2$, and let $C_5$ be the radius-$1$ circle centered at $X_5$. These are full circles, not clipped by a hexagon diagonal.

Define $P_3$ as the relevant intersection between the non-axis curved boundary of $R_4$ and $C_2$.  Define $P_5$ analogously using $C_5$.  If there are multiple algebraic intersections, the app branch is the one closest to $V_4$; a proof must justify that branch or state it as a branch condition.

Define

$$
G_0=(1-c_0^{\max})V_0,
\qquad
G_2=(1-c_2^{\max})V_2.
$$

The four-point target is

$$
\Lambda(P_3,P_5,G_0,G_2)\ge1,
$$

where $\Lambda$ is the side length of the smallest equilateral triangle containing the four points.

## 8. Accepted quadrilateral lemma dependency

The prompt allows the minimal enclosing equilateral triangle lemma for convex quadrilaterals as an accepted theorem.  The repository proof is recorded in

`../500_half_skeleton_lemmas/507_minimal_enclosing_equilateral_quadrilateral_lemma.md`.

It permits reducing the four-point target to finitely many contact patterns.  The current package studies Pattern A.
