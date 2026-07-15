# CE1/CE2, $N_+=0$, T3-Like/No Vd1-Vd2: $T_0$ Forcing

Status: Proven

## Statement

Work with the original open cover and its role closures.  Normalize by the
CE1/CE2 exactly-one-midpoint lemma and dihedral symmetry so that

$$
T_C\cap\left\{M_0,\ldots,M_5\right\}=\left\{M_0\right\}.
$$

The original center role contains $O$, so its closure satisfies the interior
hypothesis in
[`2100`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md).

Assume

$$
N_+=0,
$$

no vertex role is Vd1 or Vd2, and at least one vertex role is T3-like.  Then

$$
\boxed{T_0\text{ is T3-like}.}
$$

## Normalize all T3-like traces once

For every original T3-like role, apply the translation-normalization theorem
in
[`1201`](../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md)
once, before defining any side or radial reach.  Denote the resulting closed
trace by $\widehat T_i$.  It has the same selected adjacent-support direction,
is still T3-like, and satisfies

$$
T_i\cap H\subseteq\widehat T_i\cap H.
$$

Thus the translated traces retain every midpoint covered by an original open
role and can only enlarge the covered part of the skeleton.  In particular,
it is enough to prove impossibility after these simultaneous trace
enlargements.  The side inequalities used below are now applied only to the
already normalized traces; no triangle is translated in the middle of an
argument.

We use the T3-like side tradeoff and crossed-pair obstruction proved in
[`2013`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2013_T3_like_side_tradeoff.md).

## Midpoint matching

Assume for contradiction that $T_0$ is not T3-like.  By the exhaustiveness
theorem in `1201`, every vertex role is then either Vd0 or T3-like.

The midpoints $M_1,\ldots,M_5$ are not in $T_C$ and must be covered by the
original open vertex roles.  The only vertex roles local to $M_j$ are

$$
T_{j-1},
\qquad
T_j,
\qquad
T_{j+1}.
$$

The own role $T_j$ cannot cover $M_j$ when it is T3-like, by
[`2006`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2006_T3_like_midpoint_lemma.md).
A Vd0 role cannot cover an adjacent midpoint: containment by the original
open triangle would give a positive-length interval on that adjacent ray.
Consequently each $M_j$ is covered by an adjacent T3-like role, in that
role's unique selected support direction.

Let $I$ be a maximal consecutive block of T3-like indices in
$\left\{1,\ldots,5\right\}$.  Every midpoint whose index lies in $I$ must be
covered by a T3-like role whose index also lies in $I$.  There are equally
many roles and midpoint requirements in the block, and each T3-like role can
cover at most one adjacent midpoint.  The covering incidences therefore give
a bijection between the role labels and midpoint labels in $I$, with edges
only between consecutive indices.

Let $m$ be the left endpoint of $I$.  The case $m=5$ is impossible because
neither $T_4$ nor $T_0$ is T3-like.  Thus $m<5$.  Since $T_{m-1}$ is outside
the block, the matching forces

$$
M_m\in T_{m+1}.
$$

The role $T_m$ must be matched inside $I$ and cannot be matched to its own
midpoint, so

$$
M_{m+1}\in T_m.
$$

Continuing from left to right shows that the block is paired as

$$
(T_m,T_{m+1}),
\quad
(T_{m+2},T_{m+3}),
\quad\ldots.
$$

In particular, the first pair is a crossed adjacent pair, and if $T_{m+2}$
exists then its selected support points toward $M_{m+3}$, not toward
$M_{m+1}$.

It remains to check the support hypothesis of `2013` for this first pair.
Since $T_C$ contains $O$ but not $M_m$ or $M_{m+1}$, convexity prevents it
from meeting either outer half-arm

$$
[V_m,M_m],
\qquad
[V_{m+1},M_{m+1}].
$$

Indeed, a point beyond the midpoint together with $O$ would contain the
midpoint on its joining segment.  A nonlocal vertex role has no
positive-length trace on either arm, because every noncentral point there is
at distance greater than $1$ from its vertex.  The remaining possible local
helper on the first arm is $T_{m-1}$, which is Vd0.  The remaining possible
helper on the second arm is $T_{m+2}$; it is absent, Vd0, or has its unique
selected support toward $M_{m+3}$ by the pairing just proved.  Hence neither
helper has positive-length support on the relevant arm.

The normalized traces $\widehat T_m$ and $\widehat T_{m+1}$ therefore satisfy
the crossed-pair obstruction in `2013`.  They cannot cover both outer
half-arms, contradicting the original skeleton cover, whose trace they
dominate.

Thus $T_0$ must be T3-like.
