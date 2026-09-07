# One midpoint supplier for all nonzero-gap placements

Status: Proven

Use the original open roles and their closures, actual maximal reaches,
and singleton-inclusive actual gaps. This source owns the placement reduction,
not any local capacity or enclosure estimate.

## The reduced count

Suppose the seven original open roles cover the skeleton and a nonzero gap
exists. The C triangle is CE1 or CE2 and contains exactly one midpoint $M_k$
openly, by [`2109`](../21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md).
The skeleton budget in [`2531`](../25XX_length_bounds/2531_length_budget_corollaries.md)
excludes $N_++N_{\rm sp}\ge3$. N0 in
[`2612`](2612_fixed_witness_unification.md), Theorem 7.1, excludes $N_+=0$.
If $N_+\ge2$, choose a supercritical role away from $k$. Its midpoint is
missed by itself and the C triangle, so an adjacent positive-support role
must rescue it. The support class is disjoint from the supercritical class,
forcing $N_++N_{\rm sp}\ge3$. Therefore every survivor has

$$\boxed{N_+=1,\qquad N_{\rm sp}\le1.}$$

## The midpoint-supplier lemma

Write $\sigma$ for the unique supercritical index. If $\sigma=k$, the
center-aligned B/C theorem in `2612`, Theorem 7.0, already gives a contradiction.
Otherwise there is exactly one positive-support role $T_\tau$, and

$$\tau\in\{\sigma-1,\sigma+1\},\qquad M_\sigma\in U_\tau.$$

**Proof.** Both the C triangle and the supercritical role miss $M_\sigma$.
Diameter excludes nonlocal roles, and openness makes any adjacent supplier
have positive trace on $r_\sigma$. The support-count bound makes it unique.
If $T_\tau$ is T3-like and $\tau\ne k$, its own midpoint is missed by the
C triangle and by itself. Every other role has no positive adjacent support,
so no role supplies that midpoint. Hence a T3-like supplier necessarily has
$\tau=k$. $\square$

The midpoint facts used here are the classified geometric obstructions in
[`1201`](../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).
A positive-support role is nonsupercritical; the unique supercritical role
is Vd0. All remaining roles in this reduced placement are nonsupercritical
Vd0, so the stated endpoint exclusions do not assume absent support silently.

## The only remaining local inputs

| Placement | Required local input |
|---|---|
| $\sigma=k$ | Center-aligned B/C theorem, arbitrary path types |
| $\sigma\ne k$, T3-like supplier | $\tau=k$ and the common D ratio interface |
| $\sigma\ne k$, Vd1 supplier at $k$ | The same D ratio interface |
| $\sigma,\tau\ne k$, Vd1 supplier | Two-vertex replacement, followed by N0 |
| Vd2 supplier | Common CE1/CE2 neighboring-midpoint perimeter cap |

For the away supplier, the shared edge $e_{\tau,\sigma}$ is not incident
with $k$. Both possible positive C traces are incident with $k$, so that
shared edge is center-free. This proves the replacement input in both CE1
and CE2. The two center classes are not identified: B and the CE2 part of C
use the CE2 domain, while the CE1 part of C retains its selected-branch return.
