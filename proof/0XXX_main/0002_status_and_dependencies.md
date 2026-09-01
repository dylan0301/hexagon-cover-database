
# Status and Active Dependencies

Status: Reference

This file records the active three-method proof interfaces. It does not
upgrade the status of any listed source.

## Foundations and shared geometry

| Item | Source | Status |
|---|---|---|
| Open/closed/scaled equivalence | [`1003`](../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md) | Proven |
| Center classification | [`1101`](../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md) | Proven |
| Vertex classification | [`1201`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) | Proven |
| Strict handoff selection | [`1214`](../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) | Proven |
| Exact own-ray admissible set | [`2004`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md) | Proven |
| Exact neighboring-ray capacity | [`2008`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md) | Proven |
| Signed CE1/CE2 normal form | [`2109`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md) | Proven |
| Common trace and skeleton budgets | [`2500`](../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md), [`2530`](../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md) | Proven |
| Radial-witness and gap-enclosure lemmas | [`2608`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md) | Proven |

## Active branch terminals

| Branch | Source | Status |
|---|---|---|
| Zero-gap all-Vd0 exact-one | [`31058`](../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md) | Proven |
| Nonzero-gap, \(N_+=0\), all Vd0 | [`4013_new`](../4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md) | Proven |
| Nonzero-gap, \(N_+=0\), one or two T3-like roles | [`4070_new`](../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md) | Proven |
| Nonzero-gap, \(N_+=1\), all Vd0 | [`4101_new`](../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4101_new_all_Vd0_finite_enclosure.md), [`4102_new`](../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4102_new_CE1_direct_radial_certificate.md) | Proven |
| Nonzero-gap, \(N_+=1\), exactly one T3-like role | [`4130_new`](../4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) | Proven |
| CE2 nonzero-gap, \(N_+=1\), exactly one Vd1/Vd2 role | [`4140_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md) | Proven |

The trace-length method retains the terminals `4040`, `4041`, `4110`,
`4111`, `4123`, `4149`, `414a`, and `4200`. The area-loss method retains the
zero-gap certificates `317X` and `320X`.

## Exact certificate

The zero-gap nine-point mixed overlaps are established by the exact
`3105X_computation` package. Its source, sparse data, derivation check,
positivity check, and provenance record are colocated with the theorem.

No proof-assistant formalization is currently maintained. The complete
mathematical arguments are the numbered proof sources and the two manuscript
presentations.
