# Area Function and Monotonicity

Status: Reference

This file defines the local area function used by the CE0 area packages and
records its basic symmetry and monotonicity.  The square-loss inequalities are
proved unconditionally in
[`3205_unconditional_local_square_loss.md`](3205_unconditional_local_square_loss.md).

## Local vertex data

At a vertex $V_i$, let $P_a$ and $P_b$ be the two adjacent boundary points at
distances $a$ and $b$ from $V_i$ along the incoming and outgoing boundary
edges:

$$
0\le a\le1,
\qquad
0\le b\le1.
$$

Define

$$
f(a,b)
=
\max_T
\frac{\mathrm{area}(T\cap H)}{\mathrm{area}(T)},
$$

where the maximum is over closed unit equilateral triangles $T$ such that

$$
V_i,\qquad P_a,\qquad P_b\in T.
$$

The denominator is fixed:

$$
\mathrm{area}(T)=\frac{\sqrt3}{4}.
$$

The quantity

$$
G(a,b)=1-f(a,b)
$$

is the minimum normalized area forced outside $H$ by the two local boundary
requirements.

## Symmetry

Reflection in the symmetry axis of $H$ through $V_i$ swaps the two adjacent
boundary edges.  Hence

$$
\boxed{f(a,b)=f(b,a).}
$$

## Monotonicity

If

$$
a_1\le a_2,
\qquad
b_1\le b_2,
$$

then every triangle feasible for $(a_2,b_2)$ is also feasible for $(a_1,b_1)$.
Therefore

$$
\boxed{
f(a_1,b_1)\ge f(a_2,b_2).
}
$$

Equivalently, $G(a,b)$ is nondecreasing in each coordinate.

## Proven square-loss theorem

The unconditional theorem in
[`3205_unconditional_local_square_loss.md`](3205_unconditional_local_square_loss.md)
proves

$$
\boxed{
f(a,b)\le1-\min(a,b)^2
}
$$

for every feasible row, and

$$
\boxed{
a+b>1
\quad\Longrightarrow\quad
f(a,b)\le1-\max(a,b)^2.
}
$$

Equivalently,

$$
G(a,b)\ge\min(a,b)^2
$$

for every feasible row, and

$$
a+b>1
\quad\Longrightarrow\quad
G(a,b)\ge\max(a,b)^2.
$$

These statements require no classification of maximizing triangles.

## Historical structural conjecture

An earlier route conjectured that a maximizing triangle could always be chosen
axis-aligned when $a+b\le1$, and with a vertex at one of the required boundary
points when $a+b>1$.  That structural conjecture is not proved here.

It is no longer a dependency of the CE0 area proof.  The orientation argument
in `3205` establishes the needed area inequalities directly for every
admissible triangle.

## Use in the CE0 packages

For CE0 cut points

$$
X_i=V_i+x_i(V_{i+1}-V_i),
$$

the induced rows are

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

The package
[`3201_area_conjecture_index.md`](3201_area_conjecture_index.md)
uses the proven square-loss theorem together with
[`3208_CE0_conditional_area_certificate.md`](3208_CE0_conditional_area_certificate.md)
to close the case with at least two supercritical rows.
