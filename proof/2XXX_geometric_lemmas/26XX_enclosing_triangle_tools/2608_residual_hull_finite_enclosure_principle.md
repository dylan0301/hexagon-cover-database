# Residual-Hull Finite-Enclosure Principle

Status: Proven

## 1. Setup

Let

$$
H
$$

be the closed side-one regular hexagon, and let

$$
U_0,\ldots,U_5
$$

be open equilateral triangles.  Put

$$
R
=
H\setminus\bigcup_{i=0}^5U_i.
$$

Every $U_i$ is an open polygon, so $R$ is a compact polygonal set.  Its
convex hull is a compact polygon.  Let

$$
K_R
=
\mathrm{vert}(\mathrm{conv}R)
$$

be the finite set of vertices of this convex hull.  Then

$$
R\subseteq\mathrm{conv}K_R.
$$

For a compact plane set $K$, let $\Lambda(K)$ be the least side length of a
closed equilateral triangle containing $K$, as in
[`2600`](2600_minimum_enclosing_triangle_tools.md).

## 2. Finite residual witness

### Theorem 2.1

Assume that a specified class of open unit C triangles is known not to complete
$U_0,\ldots,U_5$ to a cover of $H$.  Assume also that every open unit
triangle containing $R$ and $O$ belongs to that excluded C-triangle class.
Then

$$
\boxed{\Lambda(K_R)\ge1.}
$$

Moreover, under any hypothetical cover by an open C triangle $U_C$ and the
six fixed V roles,

$$
K_R\subset U_C.
$$

### Proof

If the seven roles cover $H$, then by definition

$$
R\subset U_C,
$$

and therefore $K_R\subset U_C$.

Suppose instead that

$$
\Lambda(K_R)<1.
$$

Choose a closed equilateral triangle $T$ of side $s<1$ containing $K_R$.
Since $T$ is convex,

$$
R\subseteq\mathrm{conv}K_R\subseteq T.
$$

Enlarge $T$ homothetically about its center to an open equilateral triangle
$U_C'$ of side one.  The strict inequality $s<1$ gives

$$
T\subset U_C'.
$$

Thus

$$
R\subset U_C',
$$

so

$$
U_C',U_0,\ldots,U_5
$$

cover $H$.  This contradicts the assumed exclusion theorem for the specified
C-triangle class.  Hence $\Lambda(K_R)\ge1$.  $\square$

## 3. Center-class consequence in the hexagon proof

For a V role $U_i$ containing $V_i$, one has

$$
O\notin U_i,
$$

because $\lVert O-V_i\rVert=1$ while two points of one open unit equilateral
triangle have distance strictly below one.  Consequently

$$
O\in R.
$$

If the V roles leave a boundary gap, then $R$ contains a point of
$\partial H$.  Any open unit triangle containing this point contains a
relative boundary interval around it.  Therefore an open unit triangle
containing $R$ and $O$ is CE1 or CE2.  Singleton V gaps are included because
openness turns their containing C-triangle contact into a positive relative
boundary interval.

Hence every proved CE1/CE2 nonzero-gap exclusion immediately yields a finite
center-forced witness theorem through Theorem 2.1.  The local reach and
endpoint calculations remain exact certificates for the inequality
$\Lambda(K_R)\ge1$; they no longer need to own a separate global strategy.
