# CE1/CE2, $N_+=0$, T3-Like With No Vd1/Vd2

Status: Proven

This package proves the branch

$$
T_C\text{ is CE1 or CE2},
\qquad
N_+=0,
$$

with no Vd1/Vd2 vertex role and at least one T3-like vertex role.  The
midpoint normalization is

$$
T_C\cap\left\{M_0,\ldots,M_5\right\}=\left\{M_0\right\}.
$$

The proof has three stages.  First, `4071` uses the shared T3-like tradeoff
`2013` to force $T_0$ to be T3-like.  Second, `4072` and `4073` isolate the
two relevant radial arms and reduce the branch to one strict capped-loss
inequality.  Third, `4074`, `4075`, `4078`, `4079`, and `407a` prove the four
genuine capped-map rows, with detailed estimates in `407c` and the exact
assembly in `407d`.

## Proof path

| File | Status | Role |
|---|---|---|
| [`4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md`](4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md) | Proven | Simultaneously normalizes the T3-like traces and forces $T_0$ to be T3-like by midpoint matching and the crossed-pair obstruction. |
| [`4072_support_isolation_after_T0_T3_like.md`](4072_support_isolation_after_T0_T3_like.md) | Proven | Uses the general diagonal-length caps to show that at most two roles are T3-like and isolates the two active radial arms. |
| [`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md) | Reduction | Derives the center and T3-like demands and reduces the branch to $\widehat B_{C_5}(A_5)+\widehat B_{C_1}(A_1)<1$. |
| [`4074_L_Full_branch.md`](4074_L_Full_branch.md) | Proven | Proves the $(L,\mathrm{Full})$ branch. |
| [`4075_Tminus_low_lower_branch_obligations.md`](4075_Tminus_low_lower_branch_obligations.md) | Proven | Proves the $(L,L)$ and $(L,T_-)$ branches and the entire left-$T_-$ family. |
| [`4078_left_L_family_completion.md`](4078_left_L_family_completion.md) | Proven | Proves the remaining $(L,T_+^{hi})$ branch. |
| [`4079_first_Full_branch.md`](4079_first_Full_branch.md) | Proven | Proves that the first-coordinate $\mathrm{Full}$ branch cannot occur in the hard region. |
| [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md) | Proven | Proves all four first-coordinate $T_+^{hi}$ branches. |
| [`407c_rigor_completion_details.md`](407c_rigor_completion_details.md) | Proven | Supplies the detailed Low, high-sheet, center-transfer, and analytic threshold estimates used above. |
| [`407d_rigor_final_assembly.md`](407d_rigor_final_assembly.md) | Proven | Checks the exact four-label inventory and assembles the perimeter contradiction. |
| [`407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py`](407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py) | Experiment | Optional exact rational check of the analytic threshold in `407c`; not a proof dependency. |
| [`407X_computation/README.md`](407X_computation/README.md) | Reference | Records the optional check, method, and expected output. |

The shared inputs are the exact four-label capped-demand theorem
[`2011`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md),
the T3-like side tradeoff and crossed-pair theorem
[`2013`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2013_T3_like_side_tradeoff.md),
and the diagonal-length theorem
[`2520`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md).

## Exhaustive analytic inventory

The safe map has exactly the four labels

$$
L,
\qquad
T_-,
\qquad
T_+^{hi},
\qquad
\mathrm{Full}.
$$

The hard region is $A_1+A_5\le1$.  The retained proofs cover every possible
first label:

| First label | Complete source |
|---|---|
| $L$ | `4074`, `4075`, and `4078` |
| $T_-$ | `4075` |
| $T_+^{hi}$ | `407a`, with details in `407c` |
| $\mathrm{Full}$ | Excluded by `4079` |

Thus every genuine label pair either is unrealizable or has total capped
output strictly below $1$.  The reduction in `4073` then gives the required
perimeter contradiction.

The $(T_+^{hi},T_-)$ threshold is now proved analytically in `407c`, Lemma
4.1. The interval script in `407X_computation/` is retained only as a
redundant exact check and is not a dependency of the proof. No deleted
historical or fake-sheet certificate is part of the proof.
