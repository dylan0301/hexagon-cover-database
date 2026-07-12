# CE2 Zero-Support Classification Bridge

Status: Proven

This note closes the classification step between the positive-support split
in `414a` and the reduced assembly in `4148`.

## Statement

For an original $V_i$-role, zero positive support on the two adjacent radial
arms is exactly the Vd0 condition:

$$
\boxed{
n=0
\quad\Longleftrightarrow\quad
T_i\text{ is Vd0}.
}
$$

Equivalently, the possible outside-vertex data in this class are

$$
(o,n)=(1,0),(2,0),(3,0).
$$

Thus no geometric replacement or simultaneous normalization is needed. After
`414a` excludes every candidate with an additional positive-support row, all
remaining rows other than the unique Vd1/Vd2 row are already Vd0.

## Why $o\ge1$

Suppose all three vertices of a vertex-role triangle belonged to the convex
hexagon $H$. Convexity would give

$$
T_i\subset H.
$$

But the extreme point $V_i$ of $H$ lies in the interior of the original open
role $T_i$. An interior neighborhood of $V_i$ contains points outside every
supporting half-plane of $H$ at $V_i$, a contradiction. Hence every vertex
role has $o\ge1$, and of course $o\le3$.

Together with the corrected definition in
[`../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md),
this proves the statement.

## The omitted $(3,0)$ case is real

Work in physical coordinates relative to $V_0$, with the interior tangent
wedge of $H$ pointing to the left. Put

$$
r=\frac1{\sqrt3},
\qquad
h=\frac1{100\sqrt3},
$$

and take the triangle with vertices

$$
A=(h+r,0),
$$

$$
B=\left(h-\frac r2,\frac12\right),
$$

and

$$
C=\left(h-\frac r2,-\frac12\right).
$$

The three side lengths are one. Its center is $(h,0)$ and its inradius is
$1/(2\sqrt3)$, so the origin lies strictly in its interior.

The point $A$ lies outside the tangent wedge because its first coordinate is
positive. For $B$ and $C$,

$$
h-\frac r2=-\frac{49}{100\sqrt3},
$$

while

$$
\left\lvert y\right\rvert=\frac12>
-\sqrt3 x=\frac{49}{100}.
$$

Thus all three vertices lie outside $H$. The whole triangle lies in

$$
x\ge-\frac{49}{100\sqrt3}>-\frac12,
$$

whereas the two adjacent radial arms from $V_1$ and $V_5$ toward $O$ have
$x\le-1/2$ in these coordinates. Therefore the triangle has no positive
adjacent-ray support and has type $(o,n)=(3,0)$.

Its two adjacent boundary reaches are

$$
a=b=\frac{49}{50\sqrt3},
$$

so this omitted type can even be supercritical:

$$
a+b=\frac{49}{25\sqrt3}>1.
$$

## Compatibility with 401X

The `401X` safe-map proof uses Vd0 only through zero adjacent support, the
actual row-sum condition, local boundary and own-radial reaches, and the
unclassified admissible-map upper bound. None of those arguments uses
$o\le2$. Therefore the corrected definition does not change any formula or
inequality in `401X`; it makes the intended zero-support class exhaustive.

$$
\Box
$$
