# Open Unit Triangles Versus Shrunken Closed Triangles

Status: Proven

## Statement

The following are equivalent:

1. $H$ is covered by seven open equilateral triangles of side length $1$.
2. There exists $\epsilon>0$ such that $H$ is covered by seven closed equilateral triangles of side length $1-\epsilon$.
3. There exists $L>1$ such that the expanded hexagon $H_L$ is covered by seven closed unit equilateral triangles.

## Open unit cover implies shrunken closed cover

Assume

$$
H\subset \bigcup_{j=1}^7 U_j,
$$

where each $U_j$ is the interior of an equilateral triangle of side length $1$.

For each $j$, define the margin function

$$
m_j(p)=\operatorname{dist}(p,\mathbb R^2\setminus U_j).
$$

Then $m_j(p)>0$ iff $p\in U_j$. Define

$$
m(p)=\max_{1\le j\le 7}m_j(p).
$$

Since the $U_j$ cover $H$,

$$
m(p)>0\qquad (p\in H).
$$

The function $m$ is continuous and $H$ is compact. Therefore

$$
\eta=\min_{p\in H}m(p)>0.
$$

Choose

$$
0<\rho<\min\left(\eta,\frac{\sqrt3}{6}\right).
$$

For each open side-$1$ equilateral triangle $U_j$, move its three sides inward by distance $\rho$. The resulting closed inner parallel triangle $K_j$ is equilateral. Since the inradius of a side-$1$ equilateral triangle is $\sqrt3/6$, the side length of $K_j$ is

$$
1-2\sqrt3\rho.
$$

Set

$$
\epsilon=2\sqrt3\rho.
$$

For every $p\in H$, there exists $j$ such that $m_j(p)\ge \eta>\rho$, hence $p\in K_j$. Thus

$$
H\subset \bigcup_{j=1}^7 K_j,
$$

where each $K_j$ is a closed equilateral triangle of side $1-\epsilon$.

This is the signed-distance form of the Lebesgue number lemma.

## Shrunken closed cover implies open unit cover

Suppose

$$
H\subset \bigcup_{j=1}^7 K_j,
$$

where each $K_j$ is a closed equilateral triangle of side $1-\epsilon$, with $\epsilon>0$.

Enlarge each $K_j$, about its incenter, to an open equilateral triangle $U_j$ of side length $1$. Then

$$
K_j\subset U_j
$$

for every $j$, so

$$
H\subset \bigcup_{j=1}^7 U_j.
$$

## Scaling form

A cover of $H$ by closed triangles of side $1-\epsilon$ is equivalent, after scaling by

$$
\frac{1}{1-\epsilon},
$$

to a cover of

$$
H_L, \qquad L=\frac1{1-\epsilon}>1,
$$

by closed unit triangles.

Conversely, if $H_L$ is covered by closed unit triangles for some $L>1$, scaling down by $1/L$ gives a cover of $H$ by closed triangles of side

$$
\frac1L=1-\epsilon, \qquad \epsilon=1-\frac1L.
$$

## Use in these notes

The final theorem is stated for open unit triangles covering the side-$1$ hexagon. Local contradiction arguments often work in the scaled model

$$
L=1+\epsilon
$$

with closed unit triangles.
