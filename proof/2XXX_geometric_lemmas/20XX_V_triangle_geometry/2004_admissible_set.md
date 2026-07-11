# Exact Local Admissible Set

Status: Proven

This note gives a proof-safe definition and an exact finite support-function
test for the local admissible set. It replaces the former polynomial sheet
list, which did not select the connected geometric component of one of its
quadratic inequalities.

## Local demand coordinates

Put the vertex role at the origin. Let

$$
e_B=left(1,0\right),
\qquad
e_A=left(-\frac12,\frac{\sqrt3}{2}\right),
\qquad
e_R=e_A+e_B.
$$

The three vectors are unit vectors. The two boundary directions $e_A,e_B$
meet at $120$ degrees, and $e_R$ is the inward radial direction.

For $0\le a,b,c\le1$, set

$$
P(a,b,c)=
\left\{
0,
a e_A,
b e_B,
c e_R
\right\}.
$$

The numbers $(a,b,c)$ in this note are lower-bound demands. They are
admissible when one closed unit equilateral triangle contains all four points.
Thus

$$
\mathcal A=
\left\{
(a,b,c)\in[0,1]^3:
P(a,b,c)\text{ lies in a closed unit equilateral triangle}
\right\}.
$$

If a particular triangle has actual reaches $(A,B,C)$, then it realizes every
demand triple satisfying

$$
0\le a\le A,
\qquad
0\le b\le B,
\qquad
0\le c\le C.
$$

This distinction is essential when a proof also fixes the row class through
$A+B\le1$ or $A+B>1$.

## Exact support criterion

For a compact set $K\subset\mathbb R^2$, write

$$
h_K(n)=\max_{p\in K} n\mathbin{\cdot}p.
$$

For an angle $\phi$, let

$$
n_j(\phi)=
\left(
\cos\left(\phi+\frac{2\pi j}{3}\right),
\sin\left(\phi+\frac{2\pi j}{3}\right)
\right),
\qquad j=0,1,2.
$$

Define

$$
L_K(\phi)=
\frac{2}{\sqrt3}
\sum_{j=0}^2 h_K\left(n_j(\phi)\right).
$$

Then

$$
\boxed{
(a,b,c)\in\mathcal A
\quad\Longleftrightarrow\quad
\min_{0\le\phi<2\pi/3}L_{P(a,b,c)}(\phi)\le1.
}
$$

### Proof

Fix three outward unit normals $n_0,n_1,n_2$ separated by $120$ degrees. A
triangle with these normals has the form

$$
E=\left\{x:n_j\mathbin{\cdot}x\le t_j, j=0,1,2\right\}.
$$

Because

$$
n_0+n_1+n_2=0,
$$

translation changes the three $t_j$ but not their sum. For an equilateral
triangle of side length $L$, the centered support value is the inradius
$L/(2\sqrt3)$. Hence

$$
L=\frac{2}{\sqrt3}(t_0+t_1+t_2).
$$

For a fixed orientation, the smallest such triangle containing $K$ has

$$
t_j=h_K(n_j).
$$

Its side length is therefore $L_K(\phi)$. Minimizing over the orientation
proves the criterion.

## Finite exact evaluation

The angular minimum above is finite algebraic data, not a numerical oracle.
Let $K=P(a,b,c)$ and form the finite breakpoint set

$$
\Theta_K=
\left\{
\phi\mathbin{\bmod}\frac{2\pi}{3}:
n_j(\phi)\mathbin{\cdot}(p-q)=0
\text{ for some }j\text{ and distinct }p,q\in K
\right\}.
$$

Between consecutive breakpoints, each support value is attained at a fixed
point of $K$. Consequently

$$
S(\phi)=
\sum_{j=0}^2h_K\left(n_j(\phi)\right)
$$

has the form $A\cos\phi+B\sin\phi$ and satisfies

$$
S''(\phi)=-S(\phi)\le0.
$$

Thus $S$ is concave on every breakpoint cell, so its minimum on that cell is
at an endpoint. Therefore

$$
\min_{0\le\phi<2\pi/3}L_K(\phi)
=
\min_{\phi\in\Theta_K}L_K(\phi),
$$

with any one angle added in the degenerate case $\Theta_K=\varnothing$.
Every breakpoint is the direction perpendicular to a difference of two of
the four displayed points. This gives an independently checkable finite exact
test using only dot products, square roots, maxima, and comparisons.

## Structural consequences

The set $\mathcal A$ is compact. Indeed, the minimum support value is a
continuous function of $(a,b,c)$ on the compact cube.

It is symmetric:

$$
(a,b,c)\in\mathcal A
\quad\Longleftrightarrow\quad
(b,a,c)\in\mathcal A.
$$

Reflection in the radial line swaps $e_A$ and $e_B$ and proves this identity.

It is coordinatewise down-closed. If $(a,b,c)\in\mathcal A$ and

$$
0\le a'\le a,
\qquad
0\le b'\le b,
\qquad
0\le c'\le c,
$$

then convexity of the containing triangle and its containment of $0$ imply

$$
(a',b',c')\in\mathcal A.
$$

In particular, every fixed-coordinate fiber is an interval starting at zero.
There is no geometrically valid second high-$c$ component.

## Radial envelope

The lower-bound radial envelope is

$$
c_{\max}(a,b)=
\max\left\{c:(a,b,c)\in\mathcal A\right\}.
$$

Compactness gives attainment. Down-closedness shows that the former
definition with existential $a'\ge a$ and $b'\ge b$ gives exactly the same
quantity. The exact value is obtained by the finite support test above.

Any simpler polynomial expression for $c_{\max}$ must prove its breakpoint
selection and component inequalities before it is used as a geometric
formula.
