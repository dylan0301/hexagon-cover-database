# Area Function and Monotonicity

Status: Strategy

This file records the local area function used by the CE0 six-point strategy.

## Local vertex data

At a vertex $V_i$, let $P_a$ and $P_b$ be the two adjacent boundary points at
distances $a$ and $b$ from $V_i$ along the incoming and outgoing boundary
edges.  Thus

$$
0\le a\le1,\qquad 0\le b\le1.
$$

Define

$$
f(a,b) = \max_T \frac{\mathrm{area}(T\cap H)}{\mathrm{area}(T)},
$$

where the maximum is over closed unit equilateral triangles $T$ such that

$$
V_i,\quad P_a,\quad P_b\in T.
$$

The denominator is fixed:

$$
\mathrm{area}(T)=\frac{\sqrt3}{4}.
$$

The quantity $1-f(a,b)$ is the normalized area forced outside $H$ by that
local vertex requirement.

## Symmetry

By reflection in the symmetry axis of $H$ through $V_i$, the two adjacent
boundary edges are interchanged.  Hence

$$
f(a,b)=f(b,a).
$$

This symmetry is used in the CE0 conditional certificate in
[`3208_CE0_conditional_area_certificate.md`](3208_CE0_conditional_area_certificate.md).

## Monotonicity

The intended monotonicity statement is:

$$
a_1\le a_2,\qquad b_1\le b_2 \quad\Longrightarrow\quad f(a_1,b_1)\ge f(a_2,b_2).
$$

Reason: requiring the unit triangle to contain farther boundary points gives a
smaller feasible search space.  A maximum over a smaller feasible set cannot
exceed the maximum over a larger feasible set.

This monotonicity is recorded as local context for $f(a,b)$.

## Structural conjecture for local maximizers

Let $T(a,b)$ denote a maximizing triangle for $f(a,b)$, when one is selected.
The working structural conjecture is:

1. If

   $$
   a+b\le1,
   $$

   then $T(a,b)$ can be chosen axis-aligned with the hexagon.  After reflecting
   if needed, if $a\le b$, one side of $T(a,b)$ lies on the same line as the
   hexagon edge containing the $b$-point.

2. If

   $$
   a+b>1,
   $$

   then $T(a,b)$ can be chosen with one of its vertices exactly at $P_a$ or
   $P_b$.

This structural conjecture is not proved in this repository.  Any use of
explicit formulas for $f(a,b)$ must either prove this structure or independently
certify the relevant upper bound for $f(a,b)$.

## Square-loss local bounds sufficient for CE0

The conditional CE0 certificate in
[`3208_CE0_conditional_area_certificate.md`](3208_CE0_conditional_area_certificate.md)
requires only the following two local upper bounds:

$$
a+b\le1 \quad\Longrightarrow\quad f(a,b)\le1-\min(a,b)^2,
$$

and

$$
a+b>1 \quad\Longrightarrow\quad f(a,b)\le1-\max(a,b)^2.
$$

Equivalently,

$$
a+b\le1 \quad\Longrightarrow\quad 1-f(a,b)\ge\min(a,b)^2,
$$

and

$$
a+b>1 \quad\Longrightarrow\quad 1-f(a,b)\ge\max(a,b)^2.
$$

These square-loss bounds are not proved in this file.  Once they are proved or
certified, the CE0 six-point final inequality follows from
[`3208_CE0_conditional_area_certificate.md`](3208_CE0_conditional_area_certificate.md)
directly.

The supercritical implication

$$
a+b>1 \quad\Longrightarrow\quad 1-f(a,b)\ge\max(a,b)^2
$$

is proved in
[`3204_supercritical_vertex_loss_lemma.md`](3204_supercritical_vertex_loss_lemma.md)
under the supercritical structural hypothesis stated above.  The structural
hypothesis itself and the subcritical implication remain open obligations.

## Area target using $f$

The package aims to prove a vertex-triangle area bound in configurations with
at least two supercritical rows:

$$
\left\lvert \left\lbrace\, i : a_i+b_i>1 \,\right\rbrace \right\rvert\ge2 \quad\Longrightarrow\quad \sum_{i=0}^5 f(a_i,b_i)<5.
$$

This target uses only the six vertex-triangle functions $f(a_i,b_i)$.  The
center triangle is handled afterward by the trivial bound that one unit
equilateral triangle contributes at most one normalized unit of area inside
$H$.
