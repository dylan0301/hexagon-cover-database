# Exact-Formula Reassembly for the $407X$ Branch

Status: Proven

This file reassembles the $407X$ branch using the corrected exact formulas. It
should be
read together with

- [`4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md`](4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md),
- [`4072_support_isolation_after_T0_T3_like.md`](4072_support_isolation_after_T0_T3_like.md),
- [`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md),
- [`4074_L_Full_branch.md`](4074_L_Full_branch.md),
- [`4075_Tminus_low_lower_branch_obligations.md`](4075_Tminus_low_lower_branch_obligations.md),
- [`4078_left_L_family_completion.md`](4078_left_L_family_completion.md),
- [`4079_first_Full_branch.md`](4079_first_Full_branch.md),
- [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md), and
- [`407c_rigor_completion_details.md`](407c_rigor_completion_details.md).

The exact capped-map theorem in
[`2011`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md)
resolves the former classified-map
blocker. It proves that the safe map $\widehat B$ has exactly four genuine
labels:

$$
\mathrm{Full},
\qquad
L,
\qquad
T_-,
\qquad
T_+^{hi}.
$$

The fake label $T_+^{lo}$ is absent.  The support count in `4072` now cites
the general diagonal-trace theorem `2520`, and `4073` uses $\widehat B$ for
the possibly T3-like row $T_1$.

## 1. Reduction target

The files `4071` and `4072` reduce the present branch to the support-isolated
configuration in which, after reflection if necessary,

$$
T_0\text{ is T3-like},\qquad T_2,T_4,T_5\text{ are Vd0},
$$

$$
r_1\text{ has positive-length support only from }T_C,T_0,T_1,
$$

and

$$
r_5\text{ has positive-length support only from }T_C,T_5.
$$

The file `4073` proves the boundary-loss reduction: the branch is closed once

$$
\widehat B_{C_5}(A_5)+\widehat B_{C_1}(A_1)<1
$$

is proved. An additional neighboring-ray requirement on $T_1$ only shrinks
the realizing set, so the same strict inequality is sufficient.

## 2. Hard-region branch inventory

The easy region

$$
A_1+A_5>1
$$

is already included in the boundary-loss package.

It remains to cover the hard region

$$
A_1+A_5\le1.
$$

The possible first-coordinate branches are exactly

$$
L,
\qquad
T_-,
\qquad
T_+^{hi},
\qquad
\mathrm{Full}.
$$

They are covered as follows.

### 2.1. First coordinate $L$

The branch

$$
(L,\mathrm{Full})
$$

is proved in `4074`. The right branches

$$
L,
\quad
T_-
$$

are covered by `4075`.  The remaining right branch

$$
(L,T_+^{hi})
$$

is proved in `4078`. The detailed Low-polynomial, middle-overlap comparison,
and center-transfer lemmas needed by `4078` are supplied in
[`407c_rigor_completion_details.md`](407c_rigor_completion_details.md),
Section 1.

Therefore

$$
B_5=L\quad\Longrightarrow\quad B_5+B_1<1.
$$

### 2.2. First coordinate $T_-$

The full first-coordinate $T_-$ family, including its final one-variable
calculus lemma, is proved in `4075`.  Therefore

$$
B_5=T_-\quad\Longrightarrow\quad B_5+B_1<1.
$$

### 2.3. First coordinate $\mathrm{Full}$

Theorem 1.3 of `4079` proves that the hard region contains no first-coordinate
Full branch:

$$
B_5\ne \mathrm{Full}.
$$

### 2.4. First coordinate $T_+^{hi}$

The file `407a` proves the following branches:

$$
(T_+^{hi},\mathrm{Full}),\qquad
(T_+^{hi},L),
\qquad
(T_+^{hi},T_+^{hi}),
\qquad
(T_+^{hi},T_-).
$$

The detailed high-sheet Cell-$T$ condition

$$
r\ge(1-\beta)(r+\beta)^2,
$$

high-left envelope estimates, inequalities $S>3y$ and $A_C>3y$, and the right
$T_-$ estimates are proved in `407c_rigor_completion_details.md` and `407a`.
The $T_-$ right-branch threshold is proved analytically in
`407c_rigor_completion_details.md`, Lemma 4.1. Its hypotheses are the
realized high-sheet Cell-$T$ condition checked in `407c`, Lemma 2.1, and the
common left-high parameterization checked in `407a`, Lemma 1.1.

Therefore

$$
B_5=T_+^{hi}\quad\Longrightarrow\quad B_5+B_1<1.
$$

## 3. Conclusion

The four-label partition in `2011` and the four row cases above exhaust every
safe upper-map maximizer. Every genuine branch pair either is impossible or
satisfies

$$
\widehat B_{C_5}(A_5)+\widehat B_{C_1}(A_1)<1.
$$

Therefore `4073` gives the perimeter contradiction. The branch

$$
T_C\text{ is CE1 or CE2},\qquad N_+=0,
$$

with no Vd1/Vd2 rows and at least one T3-like row is proved.
