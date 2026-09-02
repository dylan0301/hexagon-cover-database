# Complete Audit of the Active CE2 One-Vd Finite-Enclosure Package

Status: Proven

This file proves that the placement partition used by
[`4140_new`](4140_new_one_Vd_finite_enclosure_assembly.md) is exhaustive and
that every placement is sent to a proof contained in this active package or
to an explicitly named Strategy 1 terminal.

## Standing branch

Assume:

- \(T_C\) is CE2 and contains exactly the midpoint \(M_0\);
- \(N_+=1\);
- at least one actual V-gap is present;
- exactly one V role is Vd1 or Vd2;
- the seven original open roles cover the full skeleton.

Let \(T_\sigma\) be the unique supercritical V role and \(T_\tau\) the unique
Vd1/Vd2 role.  They are distinct because every Vd1/Vd2 role has boundary sum
strictly below \(1/2\).

If an additional V role has positive support on an adjacent radial arm, then
the Vd role, that additional role, and the supercritical role give

\[
N_++N_{\rm sp}\ge3.
\]

The skeleton row S0 of
[`2531`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md)
closes the state.  Hence it remains to assume that every other role is
nonsupercritical Vd0.

## Case 1: \(\sigma=0\)

The unique supercritical role is based at the center-covered midpoint.

- If \(\tau\in\{1,5\}\), reflection gives the adjacent placement proved in
  [`4141_new`](4141_new_adjacent_Vd_finite_enclosure.md).
- If \(\tau\in\{2,3,4\}\), the placement is proved in
  [`4142_new`](4142_new_nonadjacent_Vd_finite_enclosure.md).

These are all possible indices.

## Case 2: \(\tau=0\)

The unique Vd role is based at the center-covered midpoint.  The midpoint
\(M_\sigma\) is missed by \(T_\sigma\) and by the C triangle.  A Vd0 role
cannot rescue an adjacent midpoint, so \(T_0\) must rescue \(M_\sigma\).
Diameter locality forces

\[
\sigma\in\{1,5\}.
\]

After reflection:

- if \(T_0\) is Vd2, the Vd2 neighboring-midpoint perimeter row P3 in
  `2531` gives the contradiction;
- if \(T_0\) is Vd1, the supported-endpoint proof is
  [`4143_new`](4143_new_Vd1_rescuer_finite_enclosure.md).

## Case 3: \(\sigma\ne0\) and \(\tau\ne0\)

Again \(M_\sigma\) is missed by the center and by the supercritical role.
Every role other than \(T_\tau\) that could be local to this midpoint is Vd0.
Therefore

\[
M_\sigma\in T_\tau,
\]

and diameter locality makes \(T_\tau\) adjacent to \(T_\sigma\).

- If \(T_\tau\) is Vd2, row P3 of `2531` applies.
- If \(T_\tau\) is Vd1, the shared edge is center-free on the reduced
  placement and the two-chart replacement
  [`4144_new`](4144_new_two_chart_replacement_and_router.md) applies.  It
  recomputes the output gap rank and routes to Z0, the common disk-plus-gap
  proof, or the CE2 short-ray proof.

## Conclusion

The positive-support alternative and Cases 1--3 are pairwise disjoint and
exhaust every relative position of \(T_0,T_\sigma,T_\tau\).  Their endings
are:

| Placement | Active ending |
|---|---|
| \(\sigma=0\), adjacent Vd | `4141_new` |
| \(\sigma=0\), nonadjacent Vd | `4142_new` |
| \(\tau=0\), Vd1 rescue | `4143_new` |
| \(\tau=0\), Vd2 rescue | `2531`, row P3 |
| neither special role at \(0\), Vd1 | `4144_new` |
| neither special role at \(0\), Vd2 | `2531`, row P3 |
| additional positive-support role | `2531`, row S0 |

Thus every nonzero-gap CE2 state with \(N_+=1\) and exactly one Vd1/Vd2 role
is impossible. \(\square\)
