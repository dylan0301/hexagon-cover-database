# CE1/CE2 one-Vd assembly through the common midpoint supplier

Status: Proven

Assume a nonzero-gap skeleton cover, $N_+=1$, and exactly one Vd1/Vd2
role. An additional positive-support role is excluded by
[`2531`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md),
row S0. Otherwise apply the placement theorem
[`2613`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2613_midpoint_supplier_reduction.md).
Let $k$ be the C midpoint index.

If the unique supercritical index is $k$, use the center-aligned B/C theorem
in [`2612`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md).
Otherwise its unique midpoint supplier is the Vd role. A Vd2 supplier is
excluded by row P3 of `2531`, which uses only the common center half-cap.
A center-based Vd1 supplier is excluded by
[`4143_new`](4143_new_Vd1_rescuer_finite_enclosure.md). An away Vd1 supplier
has a center-free shared edge by `2613` and satisfies
[`4144_new`](4144_new_two_chart_replacement_and_router.md); its replacement
contradicts N0. These alternatives are disjoint and exhaustive in both
CE1 and CE2. No V-type split on a nonsupercritical path, duplicated
midpoint rescue proof, or output gap-rank assumption is required. $\square$
