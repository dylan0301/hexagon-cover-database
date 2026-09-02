# Status and Active Dependencies

Status: Reference

This file records the active three-strategy proof interfaces. It does not
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

## Active strategy interfaces

| Strategy | Interface | Status | Detailed sources retained beneath it |
|---|---|---|---|
| 1: trace length | [`2531`](../2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md) | Proven | `2500`, `2510`, `2530`, and the placement adapters |
| 2: area loss | [`2400`](../2XXX_geometric_lemmas/24XX_area_loss/2400_zero_gap_area_loss_interface.md) | Proven | `3174`, `3175`, `3205`, `3208` |
| 3: finite enclosure | [`2610`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md) | Proven | `2608`, `2609`, `4013_new`, `4070_new`, `4102_new`, `4103`, `4130_new`, `4140_new`--`4145_new`, `3105X` |

The reader-facing cross-strategy catalog is
[`0003`](0003_reusable_lemma_catalog.md) and has Reference status.

## Terminal ownership

| Terminal family | Authoritative interface | Principal detailed source |
|---|---|---|
| zero-gap length rows | `2531` | `2500` |
| CE1/CE2 perimeter substitutions | `2531` | `2500`, `2530` |
| high-count skeleton rows | `2531` | `2510`, `2530` |
| both zero-gap area rows | `2400` | `3174`, `3208` |
| common disk plus actual gap | `2610` Terminal A | `2608`, `4013_new`, `4070_new` |
| common CE2 two-gap short ray | `2610` Terminal B | `2609` |
| transverse one-gap return | `2610` Terminal C | `4102_new`, `4103` |
| supported rescuer tail | `2610` Terminal D | `2609`, `4130_new`, [`4143_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4143_new_Vd1_rescuer_finite_enclosure.md) |
| residual radial separation | `2610` Terminal E | [`4141_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4141_new_adjacent_Vd_finite_enclosure.md), [`4142_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4142_new_nonadjacent_Vd_finite_enclosure.md) |
| zero-gap asymmetric support | `2610` Terminal F | `31058` and the colocated exact certificate |

The complete CE2 one-Vd theorem is
[`4140_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md),
its two-chart replacement is
[`4144_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4144_new_two_chart_replacement_and_router.md),
and its placement audit is
[`4145_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4145_new_complete_placement_audit.md).

## Compatibility sources

The files `4040`, `4041`, `4110`, `4111`, `4123`, `4149`, `414a`, and
`4200` remain Proven sources at their historical paths, but their proofs now
invoke the named row of `2531` instead of repeating the same arithmetic.

The former active one-Vd paths `4143`, `4144`, `4146`, `4147`, `4148`, and
`414b` now have Reference status and point to the corresponding
`4141_new`--`4145_new` source. They contain no duplicate finite-enclosure
proof body. The unsuffixed 401X, 407X, and 410X packages retain the old
Strategy 2 arguments for historical comparison; the active replacement
finite-enclosure proofs are the `_new` sources.

No proof-assistant formalization is maintained. The exact zero-gap certificate
continues to use integer, rational, and $\mathbb Q(\sqrt3)$ arithmetic; no
floating-point scan is a proof dependency.
