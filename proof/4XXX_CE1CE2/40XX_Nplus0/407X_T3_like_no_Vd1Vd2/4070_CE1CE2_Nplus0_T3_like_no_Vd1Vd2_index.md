# CE1/CE2, $N_+=0$, T3-Like With No Vd1/Vd2

Status: Partial progress

This folder records progress for the shared CE1/CE2 branch

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
   \mathrm{CE1/CE2}+N_+=0+\text{no Vd1/Vd2}+\text{at least one T3-like}
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

   This file does not assume $M_1\in T_0$ or $M_5\in T_0$.

3. [`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md)

   Status: Proven reduction.

   Defines the direct $C$-triangle variables, T3-like $T_0$ variables, boundary inputs $A_1,A_5$, radial inputs $C_1,C_5$, and proves that

   $$
   B(A_5,C_5)+B(A_1,C_1)<1
   $$

   implies the perimeter contradiction.  It also records the stricter neighboring-ray constrained map for the case where $T_1$ contributes to $r_0$.

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

   and proves the full left-$T_-$ family, including non-overlap, middle-overlap, $S$-dominance, and the final right-high residual.

6. [`4075a_Tminus_final_residual_calculus_lemma.md`](4075a_Tminus_final_residual_calculus_lemma.md)

   Status: Proven.

   Supplies the one-variable calculus lemma used in the final left-$T_-$ residual proof in `4075`.

7. [`4076_remaining_branch_inventory.md`](4076_remaining_branch_inventory.md)

   Status: Open inventory.

   Records remaining possible branch obligations, especially the main open branch

   $$
   (B_5,B_1)=(L,T_+^{hi}),
   $$

   and gives the exact semialgebraic target for that branch.

## Current proved boundary-loss coverage

The following are proved in this folder:

$$
A_1+A_5>1,
$$

$$
(L,\mathrm{Full}),
$$

$$
\{L,T_-,T_+^{lo}\}^2,
$$

and all branches with first coordinate $T_-$.

## Remaining work

The main remaining branch is

$$
(L,T_+^{hi}).
$$

Possible branch-realization or exclusion work also remains for

$$
(\mathrm{Full},*),\qquad (T_+^{hi},*),\qquad
(T_+^{lo},\mathrm{Full}),\qquad (T_+^{lo},T_+^{hi}),
$$

unless future branch-realization arguments prove that these branches are not geometrically realizable in the $407X$ domain.

The folder therefore gives significant progress toward the post-`4071` obstruction but does not yet close the full $407X$ branch.
