# Shared-gap-anchor boundary transfer

Status: Proven

This is the boundary input that unifies the former B and C witnesses. It
uses the original perimeter cover, not coverage by an arbitrary candidate
enclosing triangle. All reaches below are actual maximal reaches of the
closures of the original open roles.

## Lemma

Suppose $U_C,U_0,\ldots,U_5$ cover $\partial H$, with $O\in U_C$,
$V_i\in U_i$, and $T_i=\overline{U_i}$. Suppose $J_0$ is an actual gap.
There is no condition on the gap status of $e_{5,0}$. Then

$$
B_5>1-M_0(B_0)>B_0/2,
\qquad M_0(z)=\frac{-z+\sqrt{4-3z^2}}2.
$$

Here $M_0(z)$ is the scalar diameter envelope of
[`2018`](2018_diameter_transfer_and_adjacent_rescuer.md), not the midpoint
$M_0=V_0/2$.

## Proof

Put $G=X_0(B_0)$ and $L=X_5(B_5)$. The actual gap endpoint is missed by
all open V roles, so $G\in U_C$; it also belongs to $T_0$ by maximality
of the following-edge reach. The point $L$ is outside $U_5$ by openness
and maximality. Boundary locality excludes every nonincident V role, so
original perimeter coverage gives $L\in U_0\cup U_C$.

Thus one unit triangle has $L$ in its interior and $G$ in its closure.
Their distance is strictly below one: at equality, moving the interior
point slightly away from the other point would violate diameter one.
The parameters measured from $V_0$ along its two incident edges are
$B_0$ and $1-B_5$. The angle is $120$ degrees, whence

$$
B_0^2+B_0(1-B_5)+(1-B_5)^2<1.
$$

The diameter envelope gives $1-B_5<M_0(B_0)<1-B_0/2$, as required.
The last inequality is strict because $B_0>0$. This proves the lemma
without separating a gap-free left edge, a second positive-length gap,
or a singleton second gap. $\square$

The endpoint ownership and locality used here are the elementary open-trace
facts in [`1214`](../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md).
The point $L$ need not occur in the final finite witness. It supplies a
scalar inequality for the original V configuration before any candidate
is introduced. Forgetting original perimeter coverage without retaining
$B_5\ge B_0/2$ is not a valid generalization.

For the old pure one-gap hypothesis, the same scalar bound follows even
without assuming a C role: $B_5+A_0>1$ and the diameter bound
$A_0\le M_0(B_0)$ give $B_5>1-M_0(B_0)>B_0/2$.
