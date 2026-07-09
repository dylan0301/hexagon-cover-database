# CE1/CE2, $N_+=0$, T3-Like With No Vd1/Vd2

Status: Proven

This folder proves the shared CE1/CE2 branch

$$
T_C\text{ is CE1 or CE2},\qquad N_+=0,
$$

with no Vd1/Vd2 vertex roles and at least one T3-like vertex role.

The midpoint normalization is

$$
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\}.
$$

## Proof path

The preferred final assembly is

[`407b_final_assembly.md`](407b_final_assembly.md).

It uses:

- [`4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md`](4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md), proving $T_0$ is T3-like.
- [`4072_support_isolation_after_T0_T3_like.md`](4072_support_isolation_after_T0_T3_like.md), proving support isolation after reflecting so that $T_0$ supports $r_1$.
- [`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md), reducing the case to $B(A_5,C_5)+B(A_1,C_1)<1$.
- [`4074_L_Full_branch.md`](4074_L_Full_branch.md), proving $(L,\mathrm{Full})$.
- [`4075_Tminus_low_lower_branch_obligations.md`](4075_Tminus_low_lower_branch_obligations.md), proving $\{L,T_-,T_+^{lo}\}^2$ and the full left-$T_-$ family.
- [`4077_Tminus_final_residual_calculus_lemma.md`](4077_Tminus_final_residual_calculus_lemma.md), supplying the one-variable calculus lemma used by `4075`.
- [`4078_left_L_family_completion.md`](4078_left_L_family_completion.md), completing the left-Low family.
- [`4079_first_Full_and_lower_sheet_branches.md`](4079_first_Full_and_lower_sheet_branches.md), excluding first-coordinate Full and closing the remaining first-coordinate lower-sheet branches.
- [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md), closing all first-coordinate high-sheet branches.
- [`407c_detailed_gap_closure.md`](407c_detailed_gap_closure.md), supplying expanded derivations for compressed inequalities and branch-realization links.
- [`407e_final_gap_fixes.md`](407e_final_gap_fixes.md), proving the final local estimates: the stronger $y_*<1/10$ high-left envelope, the $r<5/8$, $\beta<4/5$ high-$r$ estimate for the $(T_+^{hi},T_-)$, $A_1=A_C$ subcase, and the expanded lower-sheet three-range estimate.

The formerly open inventory is recorded in [`4076_remaining_branch_inventory.md`](4076_remaining_branch_inventory.md).

## Certified computations

The following finite interval certificates are part of the local proof package:

- [`407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py`](407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py), used in the $(T_+^{hi},T_-)$ branch.
- [`407X_computation/407c_T_hi_Tlo_left_threshold_certificate.py`](407X_computation/407c_T_hi_Tlo_left_threshold_certificate.py), used in the $(T_+^{hi},T_+^{lo})$ branch.
- [`407X_computation/README.md`](407X_computation/README.md), recording the expected outputs for the local certificates.

Both scripts use rational interval arithmetic with one-sided integer square-root bounds and report zero unresolved boxes in their recorded runs.

## Branch coverage summary

The following are proved or excluded in this folder:

$$
A_1+A_5>1,
$$

$$
(L,*),\qquad (T_-,*),\qquad (\mathrm{Full},*),
$$

$$
(T_+^{lo},\mathrm{Full}),\qquad (T_+^{lo},T_+^{hi}),
$$

and

$$
(T_+^{hi},*).
$$

Together these cover every realized hard-region branch pair in the support-isolated $407X$ domain. Therefore, by `4073`, the full $407X$ branch is closed.
