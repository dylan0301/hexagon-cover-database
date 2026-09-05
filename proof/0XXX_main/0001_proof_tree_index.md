# Proof Tree Index

Status: Reference

This file is navigation only. A mathematical claim is established by a
numbered source whose recorded status supports it. The exhaustive proof is
[`0000_main_theorem.md`](0000_main_theorem.md), and the reusable-source catalog
is [`0003_reusable_lemma_catalog.md`](0003_reusable_lemma_catalog.md).

## 1. Structural spine

Under a hypothetical cover, use the original open roles

$$
U_C,U_0,\ldots,U_5
$$

and their closures $T_C,T_i$. The center classification is CE0/CE1/CE2, and
the normalized V classification is Vd0/Vd1/Vd2/T3-like. The structural
sources are:

- [`1003`](../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md): open, shrunken closed, and scaled formulations;
- [`1101`](../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md): exhaustive C-triangle classification;
- [`1201`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md): exact-trace normalization and exhaustive V-triangle classification;
- [`1214`](../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md): strict handoffs and supercritical-ascent preservation;
- [`2109`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md): one signed CE1/CE2 data interface.

The global routing invariants are

$$
N_+=|\{i:A_i+B_i>1\}|,
\qquad
N_{\rm sp}=d+t,
\qquad
N_{\rm gap}.
$$

Here $d$ counts Vd1/Vd2 roles, $t$ counts T3-like roles, and singleton missed
boundary points remain gaps.

## 2. Dependency ownership

The active proof is organized by reusable engines, adapters, and terminals.

| Layer | Owner | Responsibility |
|---|---|---|
| local V geometry | [`2004`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md), [`2008`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md) | exact own-ray and permitted neighboring-ray capacities |
| zero-gap area | [`2400`](../2XXX_geometric_lemmas/24XX_area_loss/2400_zero_gap_area_loss_interface.md) | both cyclic area rows |
| trace length | [`2530`](../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md), [`2531`](../2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md) | generic budgets and all active substitutions |
| finite enclosure | [`2608`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md), [`2609`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2609_simplified_finite_enclosure_lemmas.md), [`2610`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md) | forcing engine, universal inequalities, terminal dispatch |
| zero-gap exact certificate | [`31058`](../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md) | asymmetric nine-point terminal |

The detailed `*_new` case packages contain the finite-enclosure proofs that
replace the former Strategy 2 routes. Their unsuffixed siblings are historical
packages or compatibility locations, not the active proof authorities.

## 3. Zero-gap routing

When $N_{\rm gap}=0$, the six V roles cover $\partial H$ and the center type
is irrelevant.

| $N_+$ | Refinement | Engine or terminal | Strategy |
|---:|---|---|---:|
| $0$ | any | `2531` row Z0 | 1 |
| $1$ | any normalized V types | `2610` Terminal F / `31058` | 3 |
| at least $2$ | any | `2400` multiple-ascent profile | 2 |

The former Vd1/Vd2 length row and T3-like area row are retained as
independent alternative proofs, not separate active zero-gap routes.

## 4. Nonzero-gap preprocessing

A gap forces CE1 or CE2. The signed center has exactly one radial midpoint.
The length interface removes

$$
N_++N_{\rm sp}\ge3.
$$

Midpoint rescue gives $N_{\rm sp}\ge1$ whenever $N_+\ge2$, so every
nonzero-gap state with $N_+\ge2$ is removed before placement analysis. The
survivors satisfy

$$
N_+\in\{0,1\},
\qquad
N_++d+t\le2.
$$

## 5. Nonzero-gap terminal map

| Normalized row | Active adapter | Terminal |
|---|---|---|
| $N_+=0$, all Vd0, one gap | [`4013_new`](../4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md) | A: common disk plus actual gap |
| $N_+=0$, one or two T3-like, one gap | [`4070_new`](../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md) | A, after neighboring-capacity domination |
| any applicable Vd0/T3-like two-gap row | `4013_new`, `4070_new`, `4101_new`, or `4130_new` | B: CE2 short ray |
| $N_+=1$, all Vd0, one gap | [`4102_new`](../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4102_new_CE1_direct_radial_certificate.md), [`4103`](../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4103_transverse_seven_point_enclosure.md) | C: transverse seven-point return |
| $N_+=1$, one T3-like, one gap | [`4130_new`](../4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) | D: supported rescuer tail |
| CE2 one-Vd adjacent placement | [`4141_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4141_new_adjacent_Vd_finite_enclosure.md) | E: residual radial separation |
| CE2 one-Vd nonadjacent placement | [`4142_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4142_new_nonadjacent_Vd_finite_enclosure.md) | E: residual radial separation |
| CE2 Vd1 neighboring-midpoint placement | [`4143_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4143_new_Vd1_rescuer_finite_enclosure.md) | D |
| CE2 Vd2 neighboring-midpoint placement | `4149` compatibility wrapper | Strategy 1 row P3 |
| corrected Vd1 replacement | [`4144_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4144_new_two_chart_replacement_and_router.md) | router: output gap rank $0\to$ length, $1\to$ A, $2\to$ B |

The complete one-Vd assembly is
[`4140_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md),
and its exhaustive placement audit is
[`4145_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4145_new_complete_placement_audit.md).
The complete terminal statements and their source ownership are in `2610`.

## 6. Compatibility policy

The established case filenames remain where necessary so old links, audits,
and historical notes continue to resolve. The short length terminals `4040`,
`4041`, `4110`, `4111`, `4123`, `4149`, `414a`, and `4200` are Proven
compatibility wrappers around `2531`. The displaced old one-Vd paths `4143`,
`4144`, `4146`, `4147`, `4148`, and `414b` are Reference-status pointers to
the active `_new` package and contain no duplicate proof bodies. The former
endpoint-propagation packages remain historical alternatives and own no active
routing row. Failed routes remain under `9XXX_failed_ideas`.
