# CE1/CE2 Branch

Status: Reference

The common signed center form is
[`2109`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md).
The active branch is organized by reusable length rows and six finite-enclosure
terminals, not by repeated endpoint-propagation chains.

## 1. Common preprocessing

The length dispatcher
[`2531`](../2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md)
removes every state with

$$
N_++N_{\rm sp}\ge3
$$

and every nonzero-gap state with $N_+\ge2$. The surviving placement rows have
$N_+\in\{0,1\}$ and $N_++d+t\le2$.

## 2. Strategy 1 rows

| Row | Branch |
|---|---|
| P0 | $N_+=0$ with at least one Vd1/Vd2 role, CE1 or CE2 |
| P1 | CE1, $N_+=1$, at least one Vd1/Vd2 role |
| P2 | CE2, $N_+=1$, at least two Vd1/Vd2 roles |
| P3 | CE2 one-Vd2 neighboring-midpoint hybrid |
| S0 | $N_++N_{\rm sp}\ge3$ |
| S1 | $N_+\ge2$ |

The historical files `4040`, `4041`, `4110`, `4111`, `4123`, `4149`,
`414a`, and `4200` are compatibility wrappers around these rows.

## 3. Strategy 3 terminal map

The terminal-first interface is
[`2610`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md).

| Active package | Adapter responsibility | Terminal |
|---|---|---|
| [`4013_new`](40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md) | all-Vd0 common pair | A or B |
| [`4070_new`](40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md) | T3-like neighboring-capacity domination | A or B |
| [`4101_new`](41XX_Nplus1/410X_all_Vd0_new/4101_new_all_Vd0_finite_enclosure.md), [`4103`](41XX_Nplus1/410X_all_Vd0_new/4103_transverse_seven_point_enclosure.md) | actual transverse endpoints | C or B |
| [`4130_new`](41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) | T3-like supported endpoint | D or B |
| [`4140_new`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md) | exhaustive one-Vd placements | D, E, Strategy 1, or replacement routing |

## 4. Replacement policy

The corrected two-chart Vd1 replacement preserves the covered skeleton and
produces six nonsupercritical Vd0 roles. It recomputes the output gap rank:
zero routes to Strategy 1 row Z0, one to Terminal A, and two to Terminal B.
No input-gap-rank preservation is asserted.

The old composed boundary-transfer packages remain for provenance and link
compatibility but own no active case.
