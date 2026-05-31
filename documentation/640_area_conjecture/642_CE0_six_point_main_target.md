# CE0 Six-Point Main Target

Status: Strategy

This file records the main area-conjecture target for CE0.

## CE0 perimeter data

Assume

$$
T_C\text{ is CE0}.
$$

Thus $T_C$ has no positive-length overlap with any boundary edge.  The boundary
handoff data is one cut point on each edge:

$$
X_i=V_i+x_i(V_{i+1}-V_i),
\qquad i=0,\dots,5,
$$

where

$$
0\le x_i\le1.
$$

These are the six perimeter cut points for the CE0 area target.

## Induced vertex rows

At vertex $V_i$, the incoming boundary length is the portion of $e_{i-1}$ from
$X_{i-1}$ to $V_i$, and the outgoing boundary length is the portion of $e_i$
from $V_i$ to $X_i$.  Therefore

$$
(a_i,b_i)=(1-x_{i-1},x_i),
\qquad i=0,\dots,5,
$$

with indices modulo $6$.

Equivalently,

$$
a_i+b_i=1-x_{i-1}+x_i.
$$

The cyclic sum satisfies

$$
\sum_{i=0}^5(a_i+b_i)=6.
$$

Thus any supercritical row with $a_i+b_i>1$ must be balanced by subcritical
rows elsewhere.

## CE0 area target

For the six vertex triangles, use the local area function $f(a,b)$ from
`641_area_function_and_monotonicity.md`.

The CE0 area-conjecture target is

$$
\#\{i:a_i+b_i>1\}\ge2
\quad\Longrightarrow\quad
\sum_{i=0}^5 f(a_i,b_i)<5.
$$

If this strict inequality is proved under the correct CE0 hypotheses, then the
six vertex triangles contribute less than five unit-triangle areas inside
$H$.  The center triangle contributes at most one unit-triangle area inside
$H$, so the seven triangles contribute less than the area of $H$ and cannot
cover $H$.

## Why this is separate from CE1/CE2

The CE0 model has six perimeter cut points because $T_C$ contributes no
positive-length boundary interval.

The CE1 and reduced-CE2 model has seven perimeter cut points because one edge
cut point is replaced by the two endpoints of an active $C$-only boundary
interval.  That extension is recorded separately in
`643_CE1_CE2_seven_point_extension.md`.

## Main proof obligations

The CE0 six-point target requires:

1. certified upper bounds for each $f(a_i,b_i)$, or a proved structural formula
   for $f(a,b)$;
2. a pointwise threshold-bound reduction for supercritical rows, using
   $f(a_i,b_i)\le f(a_i,1+\varepsilon-a_i)$ when
   $a_i+b_i\ge1+\varepsilon$;
3. a proof of the final strict inequality
   $\sum_{i=0}^5 f(a_i,b_i)<5$ on all relaxed CE0 regimes with at least two
   supercritical rows.
