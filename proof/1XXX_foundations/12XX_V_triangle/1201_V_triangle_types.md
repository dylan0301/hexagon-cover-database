# V-Triangle Types

Status: Definition

For a $V_i$-triangle, define

$$
o=\left\lvert \left\lbrace \text{vertices of }T_i\text{ outside }H \right\rbrace \right\rvert,
$$

and

$$
n=\left\lvert \left\lbrace \text{adjacent rays }r_{i-1},r_{i+1}\text{ having positive-length intersection with }T_i \right\rbrace \right\rvert.
$$

Every original vertex role has

$$
1\le o\le3.
$$

Indeed, if all three vertices of $T_i$ belonged to the convex hexagon $H$,
then the whole triangle would belong to $H$. This is impossible because the
extreme point $V_i$ of $H$ lies in the interior of the original vertex role.

The zero-adjacent-support class is

$$
\boxed{
\mathrm{Vd0}: n=0,
}
$$

or equivalently

$$
\mathrm{Vd0}:
(o,n)=(1,0),(2,0),\text{ or }(3,0).
$$

The positive-support names are:

$$
\mathrm{Vd1}: (o,n)=(1,1),
$$

$$
\mathrm{Vd2}: (o,n)=(1,2),
$$

$$
\mathrm{T3\text{-}like}: (o,n)=(2,1).
$$

Thus a T3-like $V_i$-triangle has positive-length intersection with exactly one
of the adjacent half-diagonals $r_{i-1}$ and $r_{i+1}$. Among the six
half-diagonals, it can have positive-length intersection only with

$$
r_i
$$

and exactly one of

$$
r_{i-1},\qquad r_{i+1}.
$$

Equivalently, after rotating indices to $i=0$, it can meet only $OV_0$ and
exactly one of $OV_1$ and $OV_5$ in positive length.

For a $\mathrm{T3\text{-}like} V_i$-triangle, we use the normalization
that the triangle may be translated, preserving side length and orientation,
so that $V_i$ lies on a side of $T_i$.  Relative to the local target under
consideration, the translated triangle contains the previously covered target
region and covers a strict superset of that region.  Thus T3-like arguments
may assume $V_i$ lies on a side of $T_i$.

The case $(o,n)=(2,2)$ is unattainable.

The positive-support list is not asserted to classify every pair with
$n\ge1$. Proofs that need only the complementary split use

$$
n=0
\qquad\text{or}\qquad
n\ge1
$$

directly. In particular, the definition of Vd0 does not depend on the number
of outside vertices.
