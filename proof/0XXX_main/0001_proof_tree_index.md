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
| zero-gap exact certificate | [`31058`](../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md) | the asymmetric nine-point terminal |

The detailed case packages now serve as adapters: they establish that a
normalized placement satisfies one of the common terminal interfaces. They do
not own a second copy of the terminal argument.

## 3. Zero-gap routing

When $N_{\rm gap}=0$, the six V roles cover $\partial H$ and the center type
is irrelevant.

| $N_+$ | Refinement | Engine or terminal | Strategy |
|---:|---|---|---:|
| $0$ | any | `2531` row Z0 | 1 |
| $1$ | $d\ge1$ | `2531` row Z1 | 1 |
| $1$ | $d=0$, $t\ge1$ | `2400` one-ascent exceptional profile | 2 |
| $1$ | $(d,t)=(0,0)$ | `2610` Terminal F / `31058` | 3 |
| at least $2$ | any | `2400` multiple-ascent profile | 2 |

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

| Normalized row | Adapter | Terminal |
|---|---|---|
| $N_+=0$, all Vd0, one gap | `4013_new` | A: common disk plus actual gap |
| $N_+=0$, one or two T3-like, one gap | `4070_new` | A, after neighboring-capacity domination |
| any applicable Vd0/T3-like two-gap row | `4013_new`, `4070_new`, `4101_new`, or `4130_new` | B: CE2 short ray |
| $N_+=1$, all Vd0, one gap | `4102`, `4103` | C: transverse seven-point return |
| $N_+=1$, one T3-like, one gap | `4130_new` | D: supported rescuer tail |
| CE2 one-Vd adjacent/nonadjacent placements | `4144`, `4146` | E: residual radial separation |
| CE2 Vd1 neighboring-midpoint placement | `4143` | D |
| CE2 Vd2 neighboring-midpoint placement | `4149` compatibility wrapper | Strategy 1 row P3 |
| corrected Vd1 replacement | `4147` | router: output gap rank $0\to$ length, $1\to$ A, $2\to$ B |

The complete terminal statements and their source ownership are in `2610`.

## 6. Compatibility policy

The established case filenames remain in place so old links, audits, and
historical notes continue to resolve. The short length terminals `4040`,
`4041`, `4110`, `4111`, `4123`, `4149`, `414a`, and `4200` are compatibility
wrappers around `2531`. The old endpoint-propagation packages remain historical
alternatives and own no active routing row. Failed routes remain under
`9XXX_failed_ideas`.
