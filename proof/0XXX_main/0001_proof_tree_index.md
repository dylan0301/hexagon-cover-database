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

## 5. Nonzero-gap fixed-witness map

The fixed-set proofs and the type-independent N0 theorem are in
[`2612`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md).
All reaches below are actual reaches. Normalize the center midpoint to $M_0$;
B has gaps on $e_{5,0},e_{0,1}$ and C has its single gap on $e_{0,1}$.

| Normalized row | Active construction | Terminal |
|---|---|---|
| $N_+=0$, one gap, arbitrary V types | six common radial points and farther gap endpoint | A: at most seven points and their explicit disk |
| $T_1,\ldots,T_5$ nonsupercritical, two gaps | two boundary anchors and total endpoints on $r_2,r_4$ | B: at most four fixed points |
| $T_1,\ldots,T_5$ nonsupercritical, one gap | $M_0$, both gap endpoints, total endpoints on $r_2,r_3,r_4$ | C: at most six fixed points |
| center-based T3-like or Vd1 role rescues a supercritical neighbor | origin, supported O-side endpoint, both left-gap endpoints | D: at most four fixed points, both gap ranks |
| Vd2 neighboring-midpoint placement | retained perimeter bound | `2531` row P3 |
| Vd1--supercritical pair away from $M_0$ | both replacement charts preserved | `4144_new`, then N0 |

When the supercritical role is $T_0$, every nonsupercritical V-type pattern
uses C for one gap and B for two gaps. The old adjacent/nonadjacent Vd
residual estimates remain alternatives, not active E families. The T3-like
and Vd1 local endpoint calculations remain in `4130_new` and `4143_new`.
The CE1 local first step and full conditional return remain in `4102_new`.

The complete one-Vd assembly and positional exhaustiveness are still owned
by `4140_new` and `4145_new`. Replacement preserves the skeleton with the
original C triangle fixed and produces six nonsupercritical roles. N0
handles its output gaps internally; no equality of input/output gap ranks
is asserted.

## 6. Compatibility policy

The established case filenames remain where necessary so old links, audits,
and historical notes continue to resolve. The short length terminals `4040`,
`4041`, `4110`, `4111`, `4123`, `4149`, `414a`, and `4200` are Proven
compatibility wrappers around `2531`. The displaced old one-Vd paths `4143`,
`4144`, `4146`, `4147`, `4148`, and `414b` are Reference-status pointers to
the active `_new` package and contain no duplicate proof bodies. The former
endpoint-propagation packages remain historical alternatives and own no active
routing row. Failed routes remain under `9XXX_failed_ideas`.
