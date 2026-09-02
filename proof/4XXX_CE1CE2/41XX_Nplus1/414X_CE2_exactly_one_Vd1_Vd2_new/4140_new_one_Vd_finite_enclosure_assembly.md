# CE2, \(N_+=1\), Exactly One Vd1/Vd2: Complete Finite-Enclosure Package

Status: Proven

This directory contains the active proof package for the nonzero-gap CE2 row
with exactly one supercritical V role and exactly one Vd1/Vd2 role.  It is not
an index-only directory.  The placement calculations, replacement
construction, exhaustiveness audit, and final assembly are all contained
here.

The shared one-triangle and C-triangle interfaces remain in `2XXX`:

- the Vd corner normal form and radial margins in
  [`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md)
  and
  [`201c`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md);
- the signed CE1/CE2 center form in
  [`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md);
- the common length rows in
  [`2531`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md);
- the simplified finite-enclosure lemmas in
  [`2609`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2609_simplified_finite_enclosure_lemmas.md).

## Package contents

| File | Active responsibility |
|---|---|
| [`4141_new`](4141_new_adjacent_Vd_finite_enclosure.md) | supercritical \(T_0\), adjacent Vd role |
| [`4142_new`](4142_new_nonadjacent_Vd_finite_enclosure.md) | supercritical \(T_0\), nonadjacent Vd role |
| [`4143_new`](4143_new_Vd1_rescuer_finite_enclosure.md) | Vd1 role at \(T_0\), neighboring-midpoint rescuer |
| [`4144_new`](4144_new_two_chart_replacement_and_router.md) | neither special role at \(T_0\): two-chart replacement and recomputed-gap routing |
| [`4145_new`](4145_new_complete_placement_audit.md) | exhaustive placement audit |
| this file | theorem statement and final assembly |

## Theorem

Let \(U_C,U_0,\ldots,U_5\) be the original open unit equilateral roles, with

\[
O\in U_C,\qquad V_i\in U_i,
\]

and put

\[
T_C=\overline{U_C},\qquad T_i=\overline{U_i}.
\]

Assume:

1. \(T_C\) is CE2;
2. \(N_+=1\), defined from the actual reaches \(A_i+B_i>1\);
3. exactly one V role is Vd1 or Vd2;
4. at least one actual V-gap is present;
5. the seven open roles cover the full hexagon skeleton.

Then no such configuration exists.

## Proof

By the exactly-one-midpoint theorem, rotate and reflect so that

\[
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\}.
\tag{1}
\]

Let \(T_\sigma\) be the unique supercritical role and \(T_\tau\) the unique
Vd1/Vd2 role.  They are distinct because every Vd1/Vd2 role is
nonsupercritical.

If another V role has positive adjacent support, then the supercritical role,
the Vd role, and that additional role give

\[
N_++N_{\rm sp}\ge3.
\]

The skeleton row S0 in `2531` gives a contradiction.  Hence every remaining
V role is nonsupercritical Vd0.

The exhaustive audit
[`4145_new`](4145_new_complete_placement_audit.md) leaves three positional
cases.

### Case 1: \(\sigma=0\)

If \(T_\tau\) is adjacent to \(T_0\), apply
[`4141_new`](4141_new_adjacent_Vd_finite_enclosure.md).  If it is
nonadjacent, apply
[`4142_new`](4142_new_nonadjacent_Vd_finite_enclosure.md).

### Case 2: \(\tau=0\)

Midpoint rescue forces \(\sigma\in\{1,5\}\).  If \(T_0\) is Vd2, the
neighboring-midpoint perimeter row P3 in `2531` applies.  If \(T_0\) is Vd1,
reflection reduces to the supported-endpoint proof
[`4143_new`](4143_new_Vd1_rescuer_finite_enclosure.md).

### Case 3: \(\sigma\ne0\) and \(\tau\ne0\)

Midpoint rescue forces \(T_\sigma,T_\tau\) to be adjacent and
\(M_\sigma\in T_\tau\).  The Vd2 alternative is again row P3 of `2531`.
For Vd1, the two-chart theorem
[`4144_new`](4144_new_two_chart_replacement_and_router.md) replaces the
special pair by two open nonsupercritical Vd0 roles while preserving the full
skeleton.  It then recomputes the output gap rank:

\[
N'_{\rm gap}=0
\longrightarrow
\text{Strategy 1 row Z0},
\]

\[
N'_{\rm gap}=1
\longrightarrow
\text{common disk plus actual gap},
\]

\[
N'_{\rm gap}=2
\longrightarrow
\text{CE2 short-ray obstruction}.
\]

No preservation of the input gap rank is assumed.

The positive-support alternative and Cases 1--3 are pairwise disjoint and
exhaustive.  Every alternative is impossible, proving the theorem.
\(\square\)
