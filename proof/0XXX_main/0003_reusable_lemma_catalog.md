# Reusable Lemma and Terminal Catalog

Status: Reference

This catalog explains which source owns each reusable argument.  It is
navigation, not a substitute for the Proven sources linked below.

## 1. Design rule

The active proof tree has four kinds of nodes.

1. **Structural interfaces** define the roles, invariants, and normal forms.
2. **Quantitative engines** prove a reusable inequality or forcing principle.
3. **Case adapters** verify that a normalized placement satisfies an engine's
   hypotheses.
4. **Terminals** turn the engine output into noncoverage.

A detailed case file should own only its placement-specific calculation.  A
common budget, cyclic aggregation, or enclosure contradiction is stated and
proved once in the corresponding interface package.

## 2. Structural interfaces

| Interface | Exact output | Used by |
|---|---|---|
| [`1003`](../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md) | open/closed/scaled equivalence | final theorem |
| [`1101`](../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md) | CE0/CE1/CE2 exhaustiveness | all routing |
| [`1201`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) | exact-trace normalization and Vd0/Vd1/Vd2/T3-like exhaustiveness | all routing |
| [`1214`](../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) | strict handoffs, telescoping sum, supercritical-ascent preservation | Strategies 2 and 3, zero-gap Strategy 1 |
| [`2109`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md) | CE sign, two traces, six radial exits, unique midpoint, center boundary contribution | Strategies 1 and 3 |

The actual gap on \(e_{i,i+1}\) is

\[
X_i([B_i,1-A_{i+1}]).
\]

Equality gives a singleton gap because the two incident roles are open.

## 3. Strategy 1: length engines

| Engine | Statement owned | Case adapters or wrappers |
|---|---|---|
| [`2500`](../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md) | complete boundary-cap table and boundary-complete base rows | zero-gap rows, Vd caps |
| [`2510`](../2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md) | center, positive-support, ordinary, and supercritical skeleton caps | high-count rows |
| [`2530`](../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md) | master perimeter deficit, CE2 slack bounds, \(N_++N_{\rm sp}\) skeleton theorem | all CE1/CE2 substitutions |
| [`2531`](../2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md) | named dispatch rows Z0, Z1, P0--P3, S0, S1 | `4040`, `4041`, `4110`, `4111`, `4123`, `4149`, `414a`, `4200` |

Five perimeter files are substitutions into one deficit inequality; three
skeleton files are count substitutions into one
\(N_++N_{\rm sp}\) theorem.

## 4. Strategy 2: area engines

| Engine | Statement owned |
|---|---|
| [`3205`](../3XXX_CE0/32XX_Nplus_ge2/3205_unconditional_local_square_loss.md) | \(G\ge\min(a,b)^2\), and \(G\ge\max(a,b)^2\) for a supercritical selected pair |
| [`3175`](../3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3175_direct_T3_like_area_loss.md) | T3-like nonsupercriticality and \(G_{\rm T3}\ge2m-4m^2\) |
| [`2400`](../2XXX_geometric_lemmas/24XX_area_loss/2400_zero_gap_area_loss_interface.md) | one cyclic loss aggregator closing both active zero-gap area rows |

After reflection, every selected coordinate is at least
\(m=\min_i x_i\).  With at least two ascents the second defect is a loss
strictly above \(1/4\); with one ascent and a T3-like role it is
\(2m-4m^2\).  The remaining global calculation is the same.

## 5. Fixed finite-witness interfaces

The active finite-enclosure interface is [2610](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md).
The fixed-endpoint forcing, arbitrary-candidate proofs and N0 theorem are
owned by [2612](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md).
The exact own and adjacent capacities remain in `2004`, `2008`, and `2608`.

| Family | Fixed set | Count | Disk |
|---|---|---:|---|
| A | six common radial points and farther actual gap endpoint | at most 7 | radius $h(1-c_A)$ |
| B | two boundary endpoints, total endpoints on $r_2,r_4$ | at most 4 | none |
| C | $M_0$, both gap endpoints, total endpoints on $r_2,r_3,r_4$ | at most 6 | none |
| D | $O$, supported endpoint, two actual left-gap endpoints | at most 4 | none |
| F | six common radial points and the three exact asymmetric points | at most 9 | radius $h(1-c_F)$ |

B/C depend on a five-role nonsupercritical path, not its V-type pattern.
Both formerly separate E placements with supercritical $T_0$ use C for one
gap and B for two gaps. Their residual estimates remain alternative sources.
The T3-like and Vd1 chart calculations verify D's endpoint/ratio interface;
both gap ranks have one four-point ending. The bare CE1 signed domain is
not a substitute for the selected-branch assumptions in `4102`.

The two-chart Vd1 replacement is not a sixth enclosure recipe. It preserves
the skeleton with the original C triangle fixed and produces $N_+'=0$,
contradicting the type-independent N0 theorem. Its two charts and strict
margins remain unchanged; its output gap rank need not equal the input rank.

## 6. Source ownership and retained calculations

`4013_new` and `4070_new` invoke the same nonsupercritical A/B route.
`4103` points to the six-point C theorem while retaining its original
all-Vd0 seven-point proof as an alternative. `4102` owns the conditional
local first step and full CE1 return. `4130_new` and `4143_new` own only
their distinct rescuer chart calculations before the common D theorem.
`4140_new` and `4145_new` assemble the placements without splitting the
active E families. `4141_new` and `4142_new` retain their residual estimates.
`4144_new` owns both replacement charts and ends through N0.

The exact zero-gap sources `3105X` and their authenticated certificate are
unchanged. `2611` is a four-contact caliper theorem for disk plus three-point
geometry; it is not the four-point rescuer theorem D. Length filters and the
zero-gap multiple-ascent area theorem remain explicitly different methods.
