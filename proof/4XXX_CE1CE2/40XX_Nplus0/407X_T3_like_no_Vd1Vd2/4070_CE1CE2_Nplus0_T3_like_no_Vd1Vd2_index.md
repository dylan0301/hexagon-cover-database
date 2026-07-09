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

## Files

1. [`4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md`](4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md)

   Status: Proven.

   Proves the first reduction:

   $$
   \mathrm{CE1/CE2}+N_+=0+
   \text{no Vd1/Vd2}+\text{at least one T3-like}
   \quad\Longrightarrow\quad
   T_0\text{ is T3-like}.
   $$

2. [`4072_support_isolation_after_T0_T3_like.md`](4072_support_isolation_after_T0_T3_like.md)

   Status: Proven modulo recorded diagonal-cap dependencies.

   After reflecting if necessary so that $T_0$ has positive-length support on $r_1$, proves

   $$
   T_2,T_4,T_5\text{ are Vd0},
   $$

   and therefore

   $$
   r_1\text{ has positive-length support only from }T_C,T_0,T_1,
   $$

   while

   $$
   r_5\text{ has positive-length support only from }T_C,T_5.
   $$

3. [`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md)

   Status: Proven reduction.

   Defines the boundary inputs $A_1,A_5$, radial inputs $C_1,C_5$, and proves that

   $$
   B(A_5,C_5)+B(A_1,C_1)<1
   $$

   implies the perimeter contradiction. It also records the stricter neighboring-ray constrained map for the case where $T_1$ contributes to $r_0$.

4. [`4074_L_Full_branch.md`](4074_L_Full_branch.md)

   Status: Proven.

   Proves the hard-region branch

   $$
   (B_5,B_1)=(L,\mathrm{Full}).
   $$

5. [`4075_Tminus_low_lower_branch_obligations.md`](4075_Tminus_low_lower_branch_obligations.md)

   Status: Proven.

   Proves

   $$
   (B_5,B_1)\in\{L,T_-,T_+^{lo}\}^2
   \quad\Longrightarrow\quad B_5+B_1<1,
   $$

   and proves the full left-$T_-$ family.

6. [`4077_Tminus_final_residual_calculus_lemma.md`](4077_Tminus_final_residual_calculus_lemma.md)

   Status: Proven.

   Supplies the one-variable calculus lemma used in the final left-$T_-$ residual proof in `4075`.

7. [`4078_left_L_family_completion.md`](4078_left_L_family_completion.md)

   Status: Proven.

   Completes the left-Low family, including the formerly open

   $$
   (L,T_+^{hi})
   $$

   branch.

8. [`4079_first_Full_and_lower_sheet_branches.md`](4079_first_Full_and_lower_sheet_branches.md)

   Status: Proven.

   Excludes first-coordinate Full branches and closes the remaining first-coordinate lower-sheet branches

   $$
   (T_+^{lo},\mathrm{Full}),\qquad (T_+^{lo},T_+^{hi}).
   $$

9. [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md)

   Status: Proven with two recorded finite interval certificates.

   Closes all first-coordinate high-sheet branches

   $$
   (T_+^{hi},\mathrm{Full}),\quad
   (T_+^{hi},L),\quad
   (T_+^{hi},T_+^{hi}),\quad
   (T_+^{hi},T_-),\quad
   (T_+^{hi},T_+^{lo}).
   $$

10. [`407b_final_assembly.md`](407b_final_assembly.md)

    Status: Proven modulo recorded dependencies and local interval certificates.

    Assembles the branch coverage and concludes the $407X$ branch.

11. [`407c_detailed_gap_closure.md`](407c_detailed_gap_closure.md)

    Status: Proven.

    Supplies the expanded derivations for the compressed inequalities and branch-realization links used in `4078`, `4079`, and `407a`.

12. [`4076_remaining_branch_inventory.md`](4076_remaining_branch_inventory.md)

    Status: Closed inventory.

    Records the formerly open inventory and its completed coverage.

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
(L,*),
$$

$$
(T_-,*),
$$

$$
(\mathrm{Full},*),
$$

$$
(T_+^{lo},\mathrm{Full}),\qquad (T_+^{lo},T_+^{hi}),
$$

and

$$
(T_+^{hi},*).
$$

Together these cover every realized hard-region branch pair in the support-isolated $407X$ domain. Therefore, by `4073`, the full $407X$ branch is closed.
