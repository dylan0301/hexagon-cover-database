# Exact-Formula Reassembly for the $407X$ Branch

Status: Proven

This file reassembles the $407X$ branch using the corrected exact formulas. It
should be
read together with

- [`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md),
- [`4078_left_L_family_completion.md`](4078_left_L_family_completion.md),
- [`4079_first_Full_and_lower_sheet_branches.md`](4079_first_Full_and_lower_sheet_branches.md),
- [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md), and
- [`407c_rigor_completion_details.md`](407c_rigor_completion_details.md).

The exact capped-map theorem in `4015` resolves the former classified-map
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

The fake label $T_+^{lo}$ is absent. The direct diagonal-cap proof in `4072`
also makes that file independent of the general `2520` package, and `4073`
uses $\widehat B$ for the possibly T3-like row $T_1$.

The cited branch files have been canonicalized for strict GitHub math. All
active lemma citations use explicit filenames, so the two historical detail
files that share the `407c` prefix are unambiguous in this proof.

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
`407c_rigor_completion_details.md`, Section 2.

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
$T_-$ estimates are proved in `407c_rigor_completion_details.md` and
`407e_final_gap_fixes.md`. The finite interval certificate used in the
$T_-$ right-branch case is

$$
\texttt{407X\_computation/407b\_T\_hi\_Tminus\_qright\_threshold\_certificate.py}.
$$

Its hypotheses are checked in `407c_rigor_completion_details.md`, Section 5.
The second historical certificate concerns the deleted fake lower sheet and
is no longer part of the exact proof matrix.

Therefore

$$
B_5=T_+^{hi}\quad\Longrightarrow\quad B_5+B_1<1.
$$

## 3. Conclusion

The four-label partition in `4015` and the four row cases above exhaust every
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
