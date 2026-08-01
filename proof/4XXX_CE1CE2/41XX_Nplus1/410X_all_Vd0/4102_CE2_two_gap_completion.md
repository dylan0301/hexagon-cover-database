# CE2 Two-Gap Completion for $N_+=1$, All Vd0

Status: Proven

This note is the $N_+=1$ corollary of the common CE2 two-gap theorem
[`2110`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2110_common_CE2_two_gap_application.md).
The endpoint calculation and the three-V triangle boundary budget are no longer
repeated here.

## Corollary

Assume a hypothetical cover has

- a CE2 center role;
- six Vd0 vertex roles;
- $N_+=1$;
- a V-gap, possibly a singleton, in each of the two center traces.

Then the perimeter cannot be covered.

## Proof

Normalize the unique center midpoint to $M_0$.  The midpoint argument in
[`4101`](4101_CE1CE2_Nplus1_all_Vd0_strategy.md) makes $T_0$ the unique
supercritical V triangle and gives

$$
A_i+B_i\le1
\qquad(i=1,\ldots,5).
$$

Thus V triangles $T_1,\ldots,T_5$ are nonsupercritical Vd0 V triangles.  Both center traces
contain active gaps by hypothesis, so every assumption of `2110` is satisfied.
That theorem applies the exact paired endpoint loss `2108` and the common
boundary-path budget `2019`, yielding a contradiction.

Therefore the CE2 two-gap state is impossible.

$$
\Box
$$
