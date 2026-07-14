# Minimal Enclosing Equilateral Triangle for a Convex Quadrilateral

Status: Proven

Source context: this lemma records the May 22 quadrilateral-triangle prompt from `hexagon-cover-visual/prompts/20260522quadTriangle.txt` in repository notation.

## 1. Statement

Let $Q$ be a convex quadrilateral in the plane. Let $f(Q)$ be a smallest-side-length equilateral triangle containing $Q$.

Then at least one of the following contact patterns occurs.

1. One vertex of $Q$ is a vertex of $f(Q)$, and two of the other vertices of $Q$ lie on edges of $f(Q)$.
2. All four vertices of $Q$ lie on edges of $f(Q)$.
3. Two vertices of $Q$ are two vertices of $f(Q)$.

Here a vertex lying at a vertex of $f(Q)$ is considered to lie on both adjacent edges.

## 2. Support-function formulation

For compact $K\subset\mathbb R^2$, define

$$
h_K(n)=\sup_{x\in K} n\cdot x.
$$

Let $n_0,n_1,n_2$ be outward unit normals separated by $120^\circ$. The smallest equilateral triangle with these outward normal directions and containing $K$ has side length

$$
L_K(n_0,n_1,n_2)=\frac{2}{\sqrt3}\left(h_K(n_0)+h_K(n_1)+h_K(n_2)\right).
$$

Indeed, for an equilateral triangle with these outward normals, incenter $z$,
inradius $r$, and supporting constants $c_i$, one has

$$
c_i=z\cdot n_i+r.
$$

Since $n_0+n_1+n_2=0$, it follows that $c_0+c_1+c_2=3r$. Its side length
is $2\sqrt3 r$, which is $2/\sqrt3$ times this sum. For fixed normals, the
smallest containing choice is $c_i=h_K(n_i)$ for every $i$.

Thus minimizing the side length over all orientations is equivalent to minimizing

$$
g(\theta)=h_Q(n_0(\theta))+h_Q(n_1(\theta))+h_Q(n_2(\theta)),
$$

where

$$
n_i(\theta)=R_\theta n_i(0).
$$

## 3. Proof

Let $T=f(Q)$ be a smallest enclosing equilateral triangle. Let its outward normals be $n_0,n_1,n_2$, and let its support values be

$$
h_i=h_Q(n_i).
$$

Take the minimizing orientation to be $\theta=0$.

Write the three supporting half-planes of $T$ as

$$
n_i\cdot x\le c_i.
$$

Containment gives $c_i\ge h_i$. If one of these inequalities were strict,
replacing every $c_i$ by $h_i$ would give an enclosing equilateral triangle
of the same orientation and side length

$$
\frac{2}{\sqrt3}(h_0+h_1+h_2)
<
\frac{2}{\sqrt3}(c_0+c_1+c_2),
$$

contrary to minimality. Thus $c_i=h_i$ for every $i$. In particular, every
edge of $T$ is a supporting line of $Q$ and contains at least one vertex of
$Q$.

We first record the rotation fact that will be used in both cases below.
Suppose that, for each $i$, the support in direction $n_i$ is attained at a
unique vertex $q_i$ of $Q$; the vertices $q_i$ need not be distinct. For every
other vertex $p$ of $Q$,

$$
(q_i-p)\cdot n_i>0.
$$

There are only finitely many such strict inequalities, so they persist for
all sufficiently small $|\theta|$. Hence, on a neighborhood of $0$,

$$
h_Q(R_\theta n_i)=q_i\cdot R_\theta n_i
$$

for all $i$. If $J$ denotes rotation by $90^\circ$, then

$$
\begin{aligned}
g(\theta)
&=\sum_{i=0}^2 q_i\cdot R_\theta n_i\\
&=\cos\theta g(0)+\sin\theta g_\perp,
\end{aligned}
$$

where

$$
g_\perp=\sum_{i=0}^2 q_i\cdot J n_i.
$$

Moreover, $g(0)>0$, because it is $\sqrt3/2$ times the positive side length
of $T$. If $g_\perp>0$, a sufficiently small negative $\theta$ makes
$g(\theta)<g(0)$; if $g_\perp<0$, a sufficiently small positive $\theta$
does so; and if $g_\perp=0$, then every sufficiently small nonzero $\theta$
satisfies

$$
g(\theta)=\cos\theta g(0)<g(0).
$$

Each alternative contradicts the minimality of $T$. We have therefore proved:

$$
\boxed{\text{At a minimizing orientation, the three supports cannot all be unique.}}
$$

Now suppose that some vertex $q$ of $Q$ is a vertex of $T$. Label the two
edges through $q$ as edges $0$ and $1$. The third edge contains a vertex
$p\ne q$ of $Q$. If two distinct vertices of $Q\setminus\{q\}$ lie on edges
of $T$, then pattern 1 holds. We may therefore assume that $p$ is the only
vertex of $Q\setminus\{q\}$ on the boundary of $T$. If $p$ were also on edge
$0$ or edge $1$, then, being already on the third edge, it would be a second
vertex of $T$; this is pattern 3. Otherwise $q$ is the unique support vertex
on edges $0$ and $1$, while $p$ is the unique support vertex on edge $2$.
This contradicts the boxed rotation fact. Consequently pattern 1 or pattern 3
must hold whenever a vertex of $Q$ is a vertex of $T$.

It remains to consider the case where no vertex of $Q$ is a vertex of $T$.
Then a vertex of $Q$ on the boundary of $T$ lies on exactly one edge of $T$.
If all four vertices of $Q$ lie on edges of $T$, then pattern 2 holds.
Otherwise, the three edges still require three distinct contact vertices, so
exactly three vertices $q_0,q_1,q_2$ of $Q$ are boundary contacts, one on each
edge, and the fourth vertex lies strictly inside $T$. Thus $q_i$ is the unique
support vertex in direction $n_i$ for every $i$, again contradicting the
boxed rotation fact.

The listed three patterns are therefore exhaustive.

## 4. Use in the May 21/22 package

In the May 21/22 four-point package, this lemma justifies reducing the smallest enclosing equilateral triangle for

$$
Q=\mathrm{conv}\{P_3,P_5,G_0,G_2\}
$$

to finitely many support contact patterns. Pattern A is the case where $P_3$ and $P_5$ share one supporting side, with $G_2$ and $G_0$ supporting the other two sides.
