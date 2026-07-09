# Rigorous Final Assembly for the $407X$ Branch

Status: Proven modulo recorded dependencies and local interval certificates

This file is the rigorous final assembly for the $407X$ branch.  It should be
read together with

- [`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md),
- [`4078_left_L_family_completion.md`](4078_left_L_family_completion.md),
- [`4079_first_Full_and_lower_sheet_branches.md`](4079_first_Full_and_lower_sheet_branches.md),
- [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md), and
- [`407c_rigor_completion_details.md`](407c_rigor_completion_details.md).

The file `407c` supplies the detailed analytic lemmas that are only summarized
inside the branch-completion files.

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
B(A_5,C_5)+B(A_1,C_1)<1
$$

is proved.  If the neighboring-ray constrained right map is needed because
$T_1$ contributes to $r_0$, then that map is no larger than $B(A_1,C_1)$, so the
same strict inequality is sufficient.

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

The possible first-coordinate branches are

$$
L,\qquad T_-,\qquad T_+^{lo},\qquad T_+^{hi},\qquad \mathrm{Full}.
$$

They are covered as follows.

### 2.1. First coordinate $L$

The branch

$$
(L,\mathrm{Full})
$$

is proved in `4074`.  The right branches

$$
L,\quad T_-,\quad T_+^{lo}
$$

are covered by `4075`.  The remaining right branch

$$
(L,T_+^{hi})
$$

is proved in `4078`.  The detailed Low-polynomial, middle-overlap comparison,
and center-transfer lemmas needed by `4078` are supplied in `407c`, Section 1.

Therefore

$$
B_5=L\quad\Longrightarrow\quad B_5+B_1<1.
$$

### 2.2. First coordinate $T_-$

The full first-coordinate $T_-$ family is proved in `4075`, with the final
one-variable calculus lemma recorded in `4077`.  Therefore

$$
B_5=T_-\quad\Longrightarrow\quad B_5+B_1<1.
$$

### 2.3. First coordinate $\mathrm{Full}$

Theorem 2.3 of `4079` proves that the hard region contains no first-coordinate
Full branch:

$$
B_5\ne \mathrm{Full}.
$$

The detailed midpoint-exit and CE2-overlap estimates used there are supplied in
`407c`, Section 2.

### 2.4. First coordinate $T_+^{lo}$

The right branches

$$
L,\quad T_-,\quad T_+^{lo}
$$

are already covered by the square-family result in `4075`.  The two remaining
right branches are handled in `4079`:

$$
(T_+^{lo},\mathrm{Full})\text{ is impossible},
$$

and

$$
(T_+^{lo},T_+^{hi})\text{ is impossible}.
$$

The detailed estimates

$$
y<{1\over4},\qquad S>\ell(y),\qquad
\left(y\ge1-{\sqrt3\over2}\Rightarrow S>{7\over16},\ A_C>{7\over16}\right)
$$

are proved in `407c`, Lemma 2.2.

Thus all first-coordinate lower-sheet branches are closed.

### 2.5. First coordinate $T_+^{hi}$

The file `407a` proves the following branches:

$$
(T_+^{hi},\mathrm{Full}),\qquad
(T_+^{hi},L),\qquad
(T_+^{hi},T_+^{hi}),\qquad
(T_+^{hi},T_-),\qquad
(T_+^{hi},T_+^{lo}).
$$

The detailed high-sheet Cell-2 condition

$$
r\ge(1-\beta)(r+\beta)^2,
$$

high-left envelope estimates, inequalities $S>3y$ and $A_C>3y$, and the right
$T_-$ estimates are proved in `407c`, Sections 3 and 4.  The two finite interval
certificates used in the $T_-$ and $T_+^{lo}$ right-branch cases are

$$
\texttt{407X\_computation/407b\_T\_hi\_Tminus\_qright\_threshold\_certificate.py},
$$

and

$$
\texttt{407X\_computation/407c\_T\_hi\_Tlo\_left\_threshold\_certificate.py}.
$$

Their hypotheses are checked in `407c`, Section 5.

Therefore

$$
B_5=T_+^{hi}\quad\Longrightarrow\quad B_5+B_1<1.
$$

## 3. Conclusion

Every hard-region realized branch pair either is impossible or satisfies

$$
B(A_5,C_5)+B(A_1,C_1)<1.
$$

By `4073`, this gives the perimeter contradiction.  Hence the branch

$$
T_C\text{ is CE1 or CE2},\qquad N_+=0,
$$

with no Vd1/Vd2 rows and at least one T3-like row is closed.
