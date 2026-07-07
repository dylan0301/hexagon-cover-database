# Alternate May 21/22 Strategy Specification

Status: Strategy

This file records the rigorous alternate strategy prompt from `jcpaik/hexagon-cover-visual/proof2/conj0521-alternate-strategies-prompt.md` in repository notation.  It is a strategy specification, not a completed proof.

The two strategies are:

1. a midpoint-window admissible-set attack;
2. a five-point obstruction avoiding the assumption $a_1+b_1=1$.

Important warning: band-window repairs of the four-point obstruction are false.  See `630_band_window_counterexamples.md` for exact counterexamples inside $[0.4,0.6]$, outside $[0.4,0.6]$, and outside $[1/3,2/3]$.

Additional warning: full-skeleton noncoverage is false as a standalone target. See `../908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md`.

## 1. Common setup

Let $H$ be the regular hexagon of side length $1$, centered at

$$
O=(0,0),
$$

with vertices

$$
V_i=\left(\cos\frac{i\pi}{3},\sin\frac{i\pi}{3}\right),\qquad i=0,\dots,5.
$$

Let

$$
e_i=[V_i,V_{i+1}].
$$

The full skeleton is

$$
S=\partial H\cup[V_0,V_3]\cup[V_1,V_4]\cup[V_2,V_5].
$$

Choose boundary points

$$
X_i=V_i+t_i(V_{i+1}-V_i),\qquad 0\le t_i\le1.
$$

Set

$$
b_i=t_i, \qquad a_i=1-t_{i-1}.
$$

Thus

$$
a_i+b_i=1-t_{i-1}+t_i,
$$

and

$$
a_i+b_i=1\Longleftrightarrow t_i=t_{i-1}.
$$

At vertex $V_i$, use local coordinates $(u,v)$ in the $120^\circ$ cone, with local metric

$$
\|(u,v)\|^2=u^2+v^2-uv.
$$

The adjacent boundary points have local coordinates

$$
X_i=(b_i,0),\qquad X_{i-1}=(0,a_i).
$$

## 2. Local admissible set

The admissible set

$$
\mathcal A\subset[0,1]^3
$$

is the set of triples $(a,b,c)$ for which a closed unit equilateral triangle containing $V_i$ can cover boundary lengths $a,b$ along the two adjacent edges and radial length $c$ along $[V_i,O]$.

For $a\le b$, it is the union of the following cells.

### Cell 1

$$
a+b\le1, \qquad a^2+ab+b^2\le1,
$$

$$
(a+b)^4-(a+b)^2+ab\le0,
$$

$$
c^4-c^2+ac-a^2\le0.
$$

### Cell 2

$$
a+b\le1, \qquad a^2+ab+b^2\le1,
$$

$$
(a+b)^4-(a+b)^2+ab\ge0,
$$

$$
((a+b)^2-1)c^2+bc-b^2\le0.
$$

### Cell 3

$$
a+b\ge1, \qquad a^2+ab+b^2\le1,
$$

$$
(a^2-1)c^2+(2ab^2+b)c+(b^4-b^2)\le0,
$$

$$
c\le\frac12.
$$

For $a>b$, define membership by symmetry.

For each $i$, define

$$
c_i^{\max}=\max\{c\in[0,1]:(a_i,b_i,c)\in\mathcal A\},
$$

and

$$
G_i=(1-c_i^{\max})V_i.
$$

## 3. AB-union region for the strict triangle

For local values $a,b$, $R(a,b)$ is the set of all local points $(u,v)$, $u,v\ge0$, that can be added to

$$
(0,0),\quad(0,a),\quad(b,0)
$$

inside one closed unit equilateral triangle.

Strategic caveat: this AB-union construction has intended proof-strategy meaning only for a triangle with $a+b>1$.  In the May 21/22 setting, this is the unique strict triangle at $V_4$.

The exact nondegenerate strict $AB$-union frontier formula is recorded in
[../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md](../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md).

Let

$$
R_4=R(a_4,b_4).
$$

Let $C_2$ be the radius-$1$ circle centered at $X_2$, and $C_5$ the radius-$1$ circle centered at $X_5$.  Define $P_3$ and $P_5$ as the selected intersections of the non-axis curved boundary of $R_4$ with $C_2$ and $C_5$, respectively.  The numerical app uses the branch closest to $V_4$.

## 4. Strategy A: midpoint-window admissible-set attack

The proposed local-admissible-set claim is:

If

$$
t_i\in[0.4,0.6]\qquad\text{for all }i,
$$

then the local admissible-set constraints at the six $V_i$-triangles are incompatible with covering the full skeleton portions left for the central triangle.

Under this assumption,

$$
a_i=1-t_{i-1}\in[0.4,0.6], \qquad b_i=t_i\in[0.4,0.6].
$$

A proof would use only

$$
(a_i,b_i,c_i)\in\mathcal A, \qquad i=0,\dots,5,
$$

and the need to cover the radial skeleton portions not handled by the central triangle.

### Important distinction

This Strategy A local-admissible-set claim is different from the four-point obstruction.

The four-point statement

$$
\Lambda(P_3,P_5,G_0,G_2)\ge1
$$

is already false inside the midpoint window $[0.4,0.6]$.  A certified example is

$$
q=\frac{499}{1000},\qquad p=r=\frac12,
$$

for which all six $t_i$ lie in $[0.4,0.6]$ but the four points fit inside an equilateral triangle of side

$$
\frac{8}{5\sqrt3}<1.
$$

Also, requiring at least one $t_i$ outside $[0.4,0.6]$ or outside $[1/3,2/3]$ does not rescue the four-point statement.  See `630_band_window_counterexamples.md`.

Known partial result from exploration: the smaller local-admissible window

$$
t_i\in\left[\frac9{20},\frac{11}{20}\right]
$$

is obstructed by local admissibility alone.  In that smaller window every local admissible $c_i$ satisfies

$$
c_i<\frac{31}{50},
$$

so the residual radial points lie beyond radius $19/50$, and six such residual radial points cannot be contained in one unit equilateral triangle.  This does not prove the full $[0.4,0.6]$ local-admissible claim.

Unresolved for Strategy A:

- prove or disprove the full $[0.4,0.6]$ local-admissible-set midpoint-window claim;
- find a cyclic inequality using the admissible slices of $\mathcal A$;
- determine the largest symmetric window $[\lambda,1-\lambda]$ for which the local admissible-set obstruction is true.

Not unresolved: the four-point band-window repairs are false; see `630_band_window_counterexamples.md`.

## 5. Strategy B: five-point obstruction without $a_1+b_1=1$

This strategy avoids assuming

$$
a_1+b_1=1.
$$

Keep the unique strict triangle at $V_4$:

$$
a_4+b_4>1.
$$

Keep

$$
a_3+b_3=1, \qquad a_5+b_5=1,
$$

and allow

$$
a_0+b_0\le1, \qquad a_1+b_1\le1, \qquad a_2+b_2\le1.
$$

In edge parameters,

$$
t_3=t_2, \qquad t_5=t_4,
$$

with

$$
t_4>t_3, \qquad t_0\le t_5, \qquad t_1\le t_0, \qquad t_2\le t_1.
$$

Use five obstruction points

$$
P_3,\quad P_5,\quad G_0,\quad G_1,\quad G_2.
$$

The target is

$$
\Lambda_5(P_3,P_5,G_0,G_1,G_2)\ge1,
$$

where $\Lambda_5$ is the smallest enclosing equilateral side length for these five points.

A necessary nonemptiness condition for the strict $R_4$ region is

$$
r^2+r(1-q)+(1-q)^2\le1
$$

in the four-parameter specialization

$$
t_2=t_3=q, \qquad t_4=t_5=r.
$$

Known partial result from exploration: near the suspected tight regime $q,t_1,t_0,r\to0$, the five-point obstruction approaches equality from above.  If

$$
r=\varepsilon, \qquad q=s\varepsilon, \qquad t_1=t\varepsilon, \qquad t_0=u\varepsilon,
$$

with

$$
\frac12\le s\le t\le u\le1,
$$

then

$$
\Lambda_5\ge1+\frac{\varepsilon}{6}+O(\varepsilon^2).
$$

This is not a global proof of Strategy B.

Unresolved for Strategy B:

- prove the correct global $P_3,P_5$ branch selection;
- reduce the five-point support-function problem to manageable finite cases;
- prove the non-endpoint inequalities or give a counterexample.

## 6. Support-function tool

For compact $K\subset\mathbb R^2$, define

$$
h_K(n)=\sup_{x\in K}n\cdot x.
$$

If an enclosing equilateral triangle has outward unit normals

$$
n_k(\theta)=\left(\cos\left(\theta+\frac{2\pi k}{3}\right),\sin\left(\theta+\frac{2\pi k}{3}\right)\right),\qquad k=0,1,2,
$$

then its side length is

$$
L_K(\theta)=\frac{2}{\sqrt3}\sum_{k=0}^2 h_K(n_k(\theta)).
$$

Thus

$$
\Lambda_K=\inf_{\theta\in[0,2\pi/3)} L_K(\theta).
$$

This formulation should be used for the five-point problem if direct contact-pattern analysis is too complicated.
