# Proof Tree Index

Status: Reference

This file is navigation only. A branch is proved only by a numbered source
whose recorded status supports the claimed conclusion. The exhaustive proof is
[`0000_main_theorem.md`](0000_main_theorem.md).

## 1. Structural spine

Under a hypothetical cover, write the original open roles as

$$
U_C,U_0,\\ldots,U_5,
$$

and put $T_C=\overline{U_C}$ and $T_i=\overline{U_i}$. The center triangle is
exactly one of CE0, CE1, CE2, and every normalized vertex triangle is exactly
one of Vd0, Vd1, Vd2, T3-like. The conventions and classifications are in
[`1003`](../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md),
[`1101`](../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md), and
[`1201`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).

Let

$$
N_+=\left\lvert\left\{i:A_i+B_i>1\right\}\right\rvert,
$$

where $A_i,B_i$ are actual maximal boundary reaches. Let $d$ count Vd1/Vd2
roles, let $t$ count T3-like roles, and put $N_{\rm sp}=d+t$. A singleton
missed boundary point counts as a gap; $N_{\rm gap}$ counts the positive center
traces containing such gaps.

Strict handoffs preserving the actual supercritical pattern are supplied by
[`1214`](../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md).

## 2. Three global strategies

1. **Strategy 1: trace length.** Perimeter, diagonal, or full-skeleton
   contributions have strict total deficit. Principal sources are
   [`2500`](../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md),
   [`2510`](../2XXX_geometric_lemmas/25XX_length_bounds/2510_half_skeleton_length_bounds.md), and
   [`2530`](../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md).
2. **Strategy 2: area loss.** Local exterior losses and cyclic handoffs exceed
   the available normalized area. Principal zero-gap sources are `317X` and
   `320X`.
3. **Strategy 3: finite enclosure.** Explicit points missed by all six V roles
   are forced into the center role, while support functions or direct radial
   separation show that no open unit center triangle can contain them.

The exact one-triangle functions $c_{\max}$ and $C_\pm$ remain local geometry.
The historical composed-transfer files remain in the corpus only for
provenance and compatibility; they own no active case.

## 3. Reusable direct finite-enclosure lemmas

- [`2004`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md): exact own-ray admissible set and $c_{\max}$.
- [`2008`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md): exact permitted neighboring-ray capacities $C_+,C_-$.
- [`2109`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md): common signed CE1/CE2 trace and radial-exit formulas.
- [`2608`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md): support gauge, type-aware radial witnesses, complementary-gap enclosure, and CE2 short-ray theorem.
- [`31058`](../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md): direct zero-gap nine-point theorem.

## 4. Zero-gap routing

When $N_{\rm gap}=0$, the six V roles cover the perimeter and the center type
is irrelevant.

| $N_+$ | Vertex refinement | Active terminal | Strategy | Status |
|---:|---|---|---:|---|
| $0$ | any | strict perimeter overlap `2500` | 1 | Proven |
| $1$ | $d\ge1$ | V-only perimeter deficit `2500` | 1 | Proven |
| $1$ | $d=0$, $t\ge1$ | T3-like cyclic area certificate `3174` | 2 | Proven |
| $1$ | $(d,t)=(0,0)$ | direct nine-point theorem `31058` | 3 | Proven |
| at least $2$ | any | cyclic square-loss certificate `3208` | 2 | Proven |

## 5. Nonzero-gap routing

A nonzero gap forces CE1 or CE2. The skeleton theorem `2530` removes
$N_++N_{\rm sp}\ge3$, and midpoint rescue removes $N_+\ge2$. The remaining
cases are:

| $N_+$ | Vertex refinement | Center | Active terminal | Strategy | Status |
|---:|---|---|---|---:|---|
| $0$ | $(d,t)=(0,0)$ | CE1/CE2 | [`4013_new`](../4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md) | 3 | Proven |
| $0$ | $d\ge1$ | CE1/CE2 | `4040`, `4041` | 1 | Proven |
| $0$ | $(d,t)=(0,1)$ or $(0,2)$ | CE1/CE2 | [`4070_new`](../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md) | 3 | Proven |
| $1$ | $(d,t)=(0,0)$ | CE1/CE2 | [`4101_new`](../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4101_new_all_Vd0_finite_enclosure.md), [`4102_new`](../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4102_new_CE1_direct_radial_certificate.md) | 3 | Proven |
| $1$ | $(d,t)=(0,1)$ | CE1/CE2 | [`4130_new`](../4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) | 3 | Proven |
| $1$ | $(d,t)=(1,0)$ | CE1 | `4110` | 1 | Proven |
| $1$ | $(d,t)=(1,0)$ | CE2 | [`4140_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md) | 1 or 3 | Proven |

## 6. Direct nonzero-gap proof contents

- `4013_new`: one gap gives a common radial disk plus the complementary gap;
  two gaps give a CE2 short-ray point beyond the center exit.
- `4070_new`: actual T3-like neighboring support is bounded by $C_\pm$ and is
  dominated by the same common own-ray capacity; the preceding two terminals
  apply.
- `4101_new`: six anisotropic own-ray endpoints and the gap are center-forced;
  CE2 is closed by a direct threshold dichotomy and CE1 by the explicit
  reverse path in `4102_new`.
- `4130_new`: the O-side endpoint of the T3-like supported trace is
  center-forced and creates a direct four-triangle boundary-path deficit.
- `4140_new`: each placement ends in direct radial separation, a Vd1 O-side
  endpoint, a perimeter deficit, or the two-chart replacement followed by
  `4013_new`.

## 7. Detailed CE2 one-Vd placement audit

The exhaustive placement classification remains in the established `414X`
structural files, but its active terminals are restated and proved in
`4140_new`:

- supercritical $T_0$, adjacent Vd role: a point of $r_2$ lies after all V
  traces and before the center trace;
- supercritical $T_0$, nonadjacent Vd role: the Vd-specific radial point lies
  beyond the center exit;
- Vd1 at $T_0$: its O-side supported-trace endpoint yields the direct path
  deficit;
- Vd2 midpoint rescue: Strategy 1 perimeter deficit;
- neither special role at $0$: the corrected two-chart replacement routes to
  Strategy 1 or `4013_new` according to the recomputed gap count;
- an additional positive-support role: Strategy 1 skeleton deficit.

## 8. Historical and failed routes

The former boundary-propagation packages remain as historical alternative
proofs and formalization interfaces. The failed four-point, May 25 five-point,
area-only CE1/CE2, and unconditional skeleton routes remain in
`9XXX_failed_ideas` with their recorded statuses. None is an active dependency.
