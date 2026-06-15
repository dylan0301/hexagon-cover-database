# Minimal Enclosing Equilateral Triangle for a Convex Quadrilateral

Status: Proven local lemma

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

Each edge of $T$ must contain at least one vertex of $Q$. If some edge contained no point of $Q$, then its support value could be decreased slightly while keeping the other two support values fixed, producing a strictly smaller enclosing equilateral triangle. This contradicts minimality.

Suppose first that some vertex $q$ of $Q$ is a vertex of $T$. Then $q$ lies on two adjacent edges of $T$. Since the third edge must also contain a vertex of $Q$, either two vertices of $Q$ are two vertices of $T$, giving pattern 3, or the remaining edge contacts provide two other vertices of $Q$ on edges of $T$, giving pattern 1.

It remains to consider the case where no vertex of $Q$ is a vertex of $T$. Then each contact point is on the relative interior of an edge of $T$.

If all four vertices of $Q$ lie on edges of $T$, then pattern 2 holds. So assume, for contradiction, that not all four vertices of $Q$ lie on edges of $T$. Since each edge has a contact vertex and there are three edges, this means that exactly three vertices $q_0,q_1,q_2$ of $Q$ are edge contacts, one for each edge, and the fourth vertex lies strictly inside $T$.

Because each support is realized by a unique vertex, there exists $\varepsilon>0$ such that for $|\theta|<\varepsilon$,

$$
h_Q(R_\theta n_i)=q_i\cdot R_\theta n_i
$$

for each $i=0,1,2$. Indeed, for every other vertex $p\ne q_i$,

$$
(q_i-p)\cdot n_i>0,
$$

and this strict inequality persists under sufficiently small rotation.

For $|\theta|<\varepsilon$, write $J$ for rotation by $90^\circ$. Then

$$
R_\theta n_i=\cos\theta\,n_i+\sin\theta\,J n_i,
$$

so

$$
g(\theta)=\sum_{i=0}^2 q_i\cdot R_\theta n_i =\cos\theta\,g(0)+\sin\theta\,g_\perp,
$$

where

$$
g_\perp=\sum_{i=0}^2 q_i\cdot J n_i.
$$

If $g_\perp>0$, then for small negative $\theta$,

$$
g(\theta)<g(0).
$$

If $g_\perp<0$, then for small positive $\theta$,

$$
g(\theta)<g(0).
$$

If $g_\perp=0$, then for any sufficiently small nonzero $\theta$,

$$
g(\theta)=\cos\theta\,g(0)<g(0).
$$

In all cases a sufficiently small rotation of the normals gives a smaller enclosing equilateral triangle, contradicting minimality.

Therefore the assumed three-unique-contact configuration is impossible. The only remaining possibilities are exactly patterns 1, 2, and 3.

## 4. Use in the May 21/22 package

In the May 21/22 four-point package, this lemma justifies reducing the smallest enclosing equilateral triangle for

$$
Q=\mathrm{conv}\{P_3,P_5,G_0,G_2\}
$$

to finitely many support contact patterns. Pattern A is the case where $P_3$ and $P_5$ share one supporting side, with $G_2$ and $G_0$ supporting the other two sides.
