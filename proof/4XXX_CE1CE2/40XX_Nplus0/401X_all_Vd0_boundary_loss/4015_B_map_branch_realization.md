# Corrected $B$-Map Semantics and Branch-Realization Warning

Status: Definition

This file corrects the map semantics used by the `401X` branch inventory. The
former version treated a disconnected algebraic sheet as a second geometric
radial component. That is impossible for the true down-closed admissible set.

## Exact unclassified map

Use the exact admissible set $\mathcal A$ and finite support criterion from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md).
The exact unclassified demand map is

$$
B_c(a)=\max\left\{b:(a,b,c)\in\mathcal A\right\}.
$$

It is proved and audited in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md).

## Actual nonsupercritical map

Let $A(T),B(T),C(T)$ be the actual local reaches of a unit Vd0 triangle. The
map relevant to an $N_+=0$ row is the supremal envelope

$$
\mathsf B_c^0(a)=
\sup\left\{
B(T):
T\text{ is Vd0},
A(T)\ge a,
C(T)\ge c,
A(T)+B(T)\le1
\right\},
$$

when the set is nonempty. It satisfies the safe bounds

$$
\mathsf B_c^0(a)\le B_c(a),
$$

and

$$
\mathsf B_c^0(a)\le1-a.
$$

The shortcut

$$
\max\left\{b:(a,b,c)\in\mathcal A, a+b\le1\right\}
$$

restricts demands, not the actual realizing row. It is an upper relaxation,
not an exact row-class definition without an additional tightening theorem.

## The discarded Cell-2 sheet

In the ordered half $a\le b$, put

$$
s=a+b,
\qquad
d=\sqrt{4s^2-3}.
$$

The former raw inequality

$$
(s^2-1)c^2+bc-b^2\le0
$$

has roots

$$
c_- =\frac{2b}{1+d},
\qquad
c_+ =\frac{2b}{1-d}.
$$

As a quadratic inequality it accepts

$$
c\le c_-
\qquad\text{or}\qquad
c\ge c_+.
$$

But every true $c$-fiber of $\mathcal A$ is an interval starting at zero.
Therefore the high-$c$ component is not a second geometric branch. The
necessary component selector is

$$
c\le2b
$$

in this ordered half, or symmetrically

$$
c\le2\max(a,b).
$$

This selector removes the demonstrated fake sheet. It does not prove that the
remaining algebraic roots are attainable or form a complete maximum catalog.

In the old notation, the sheet called $T_+^{lo}$ was this fake high-$c$
component. It may not be called a realized branch of $B_c(a)$ or
$\mathsf B_c^0(a)$.

## Status of the old branch-pair inventory

The labels

$$
L,
\quad
\mathrm{Full},
\quad
T_-,
\quad
T_+^{hi},
\quad
T_+^{lo}
$$

in older `401X` and `407X` files are now historical algebraic labels. Their
individual inequalities may still be useful, but the old list is not a
proved complete geometric partition of the exact classified map.

Before either package is upgraded to `Proven`, it must establish one of the
following:

1. a complete active-support classification of $\mathsf B_c^0(a)$; or
2. a certified upper relaxation containing every true classified maximum,
   together with a proof that every cell of that relaxation is covered by the
   branch inequalities.

Numerical root selection or satisfaction of the raw Cell-2 polynomial is not
such a proof.
