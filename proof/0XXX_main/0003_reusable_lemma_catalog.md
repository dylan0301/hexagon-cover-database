# Reusable Lemma and Terminal Catalog

Status: Reference

This catalog explains which source owns each reusable argument. It is
navigation, not a substitute for the Proven sources linked below.

## 1. Design rule

The active proof tree has four kinds of nodes.

1. **Structural interfaces** define the roles, invariants, and normal forms.
2. **Quantitative engines** prove a reusable inequality or forcing principle.
3. **Case adapters** verify that a normalized placement satisfies an engine's
   hypotheses.
4. **Terminals** turn the engine output into noncoverage.

A detailed case file should own only its placement-specific adapter. A common
budget, cyclic aggregation, or enclosure contradiction is stated and proved
once in the corresponding interface package.

## 2. Structural interfaces

| Interface | Exact output | Used by |
|---|---|---|
| [`1003`](../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md) | open/closed/scaled equivalence | final theorem |
| [`1101`](../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md) | CE0/CE1/CE2 exhaustiveness | all routing |
| [`1201`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) | exact-trace normalization and Vd0/Vd1/Vd2/T3-like exhaustiveness | all routing |
| [`1214`](../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) | strict handoffs, telescoping sum, supercritical-ascent preservation | Strategies 2 and 3, zero-gap Strategy 1 |
| [`2109`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md) | CE sign, two traces, six radial exits, unique midpoint, center boundary contribution | Strategies 1 and 3 |

The gap convention is part of the structural interface: on
$e_{i,i+1}$ the actual gap is

$$
X_i([B_i,1-A_{i+1}]),
$$

and equality gives a singleton gap because the incident roles are open.

## 3. Strategy 1: length engines

| Engine | Statement owned | Case adapters or wrappers |
|---|---|---|
| [`2500`](../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md) | complete boundary-cap table and boundary-complete base rows | zero-gap rows, Vd caps |
| [`2510`](../2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md) | center, positive-support, ordinary, and supercritical skeleton caps | high-count rows |
| [`2530`](../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md) | master perimeter deficit, CE2 slack bounds, $N_++N_{\rm sp}$ skeleton theorem | all CE1/CE2 substitutions |
| [`2531`](../2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md) | named dispatch rows Z0, Z1, P0--P3, S0, S1 | `4040`, `4041`, `4110`, `4111`, `4123`, `4149`, `414a`, `4200` |

The essential compression is that five perimeter files are substitutions into
one deficit inequality, while three skeleton files are count substitutions
into one $N_++N_{\rm sp}$ theorem.

## 4. Strategy 2: area engines

| Engine | Statement owned |
|---|---|
| [`3205`](../3XXX_CE0/32XX_Nplus_ge2/3205_unconditional_local_square_loss.md) | $G\ge\min(a,b)^2$, and $G\ge\max(a,b)^2$ for a supercritical selected pair |
| [`3175`](../3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3175_direct_T3_like_area_loss.md) | T3-like nonsupercriticality and $G_{\rm T3}\ge2m-4m^2$ |
| [`2400`](../2XXX_geometric_lemmas/24XX_area_loss/2400_zero_gap_area_loss_interface.md) | one cyclic loss aggregator closing both active zero-gap area rows |

After reflection, every selected coordinate is at least
$m=\min_i x_i$. With at least two ascents the second defect is a loss
strictly above $1/4$; with one ascent and a T3-like role it is the profile
$2m-4m^2$. The rest of the global proof is identical.

## 5. Strategy 3: local capacity engines

| Engine | Exact output |
|---|---|
| [`2004`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md) | exact down-closed admissible set and $c_{\max}(a,b)$ |
| [`2008`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md) | permitted neighboring capacities $C_+,C_-$ |
| [`2608`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md) | support gauge, type-aware radial forcing, common-pair domination, disk-plus-point and complementary-gap results |
| [`2609`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2609_simplified_finite_enclosure_lemmas.md) | finite calipers, CE2 short ray, one-third radial envelope, rescuer-tail budget |
| [`2610`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md) | six terminal families A--F and replacement routing |

## 6. Strategy 3 terminal families

| Terminal | Center-forced object | Adapters |
|---|---|---|
| A | common radial disk plus the actual one-edge gap | `4013_new`, `4070_new` |
| B | $D_2,D_4$ from the common CE2 pair | all applicable two-gap rows and replacement output |
| C | $K_{\rm tr}=\{O,M_0,X(\ell),X(r),P_2,P_3,P_4\}$ | `4102`, `4103` |
| D | O-side endpoint of a supported special role | `4130_new`, `4143` |
| E | a residual point or interval between all local V traces and the C exit | `4144`, `4146` |
| F | radial disk plus $Q_-,Q_0,Q_+$ | `3105X` exact nine-point package |

The corrected Vd1 replacement is not a terminal. It produces six
nonsupercritical Vd0 roles and recomputes the output gap rank: rank zero routes
to Strategy 1, rank one to A, and rank two to B.

## 7. What remains case-specific

The following calculations should not be merged into a generic theorem:

- the T3-like and Vd1 inequalities verifying Terminal D;
- the adjacent and nonadjacent Vd residual estimates verifying Terminal E;
- the scalar CE1 reverse-return inequalities inside Terminal C;
- the eight exact mixed-overlap polynomial signs and their Bernstein
  certificates inside Terminal F.

These are adapters or exact certificates, not duplicated global endings.
