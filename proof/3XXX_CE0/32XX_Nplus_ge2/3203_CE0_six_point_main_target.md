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
X_i=V_i+x_i(V_{i+1}-V_i), \qquad i=0,\dots,5,
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
(a_i,b_i)=(1-x_{i-1},x_i), \qquad i=0,\dots,5,
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
\left\lvert \left\lbrace\, i : a_i+b_i>1 \,\right\rbrace \right\rvert\ge2 \quad\Longrightarrow\quad \sum_{i=0}^5 f(a_i,b_i)<5.
$$

If this strict inequality is proved under the correct CE0 hypotheses, then the
six vertex triangles contribute less than five unit-triangle areas inside
$H$.  The center triangle contributes at most one unit-triangle area inside
$H$, so the seven triangles contribute less than the area of $H$ and cannot
cover $H$.

## Conditional certificate now available

The final CE0 inequality above is proved in
`647_CE0_conditional_area_certificate.md` under the following local square-loss
hypothesis:

$$
a+b\le1 \quad\Longrightarrow\quad f(a,b)\le1-\min(a,b)^2,
$$

and

$$
a+b>1 \quad\Longrightarrow\quad f(a,b)\le1-\max(a,b)^2.
$$

Under this hypothesis, the stronger estimate holds:

$$
\left\lvert \left\lbrace\, i : a_i+b_i>1 \,\right\rbrace \right\rvert\ge2 \quad\Longrightarrow\quad \sum_{i=0}^5 f(a_i,b_i)<\frac{99}{20}<5.
$$

This conditional certificate replaces the need for the threshold relaxation in
the CE0 six-point subcase once the displayed local square-loss bounds are
proved or otherwise certified.  It does not prove those local bounds.

## Why this is separate from CE1/CE2

The CE0 model has six perimeter cut points because $T_C$ contributes no
positive-length boundary interval.

The CE1 and reduced-CE2 model has seven perimeter cut points because one edge
cut point is replaced by the two endpoints of an active $C$-only boundary
interval.  That extension is recorded separately in
`643_CE1_CE2_seven_point_extension.md`.

## Main proof obligations

After `647_CE0_conditional_area_certificate.md`, the CE0 six-point target
requires only the local input needed by that certificate:

1. prove or certify the square-loss local upper bounds for $f(a,b)$ stated
   above; or
2. prove a structural formula for $f(a,b)$ that implies those square-loss
   bounds.

The older pointwise threshold-bound route in `644_threshold_relaxation.md`
remains recorded as a strategy, but it is no longer needed for the conditional
CE0 certificate if the square-loss local bounds are supplied.
