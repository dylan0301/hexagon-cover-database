# Closed Branch Inventory for $407X$

Status: Reference

This file records the branch inventory after the completion files

- [`4078_left_L_family_completion.md`](4078_left_L_family_completion.md),
- [`4079_first_Full_and_lower_sheet_branches.md`](4079_first_Full_and_lower_sheet_branches.md),
- [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md),
- [`407b_final_assembly.md`](407b_final_assembly.md),
- [`407c_detailed_gap_closure.md`](407c_detailed_gap_closure.md), and
- [`407e_final_gap_fixes.md`](407e_final_gap_fixes.md).

The purpose of this file is to show that the formerly open hard-region branch obligations are now covered by local proof files.  The detailed auxiliary inequalities used in the compressed branch files are recorded in `407c` and `407e`.

## 1. Reduction target

The structural reductions are recorded in `4071` and `4072`:

$$
T_0\text{ is T3-like},
$$

$$
T_2,T_4,T_5\text{ are Vd0},
$$

$$
r_1\text{ has positive-length support only from }T_C,T_0,T_1,
$$

and

$$
r_5\text{ has positive-length support only from }T_C,T_5.
$$

The boundary-loss framework is recorded in `4073`. The branch is closed once

$$
B(A_5,C_5)+B(A_1,C_1)<1
$$

is proved, with the stricter neighboring-ray constrained right map used if $T_1$ contributes to $r_0$.

## 2. Branch coverage

### Easy region

The easy region

$$
A_1+A_5>1
$$

is covered by the boundary-loss package.

### Previously proved families

`4074` proves

$$
(L,\mathrm{Full}).
$$

`4075` proves

$$
(B_5,B_1)\in\{L,T_-,T_+^{lo}\}^2
$$

and the full first-coordinate $T_-$ family

$$
(T_-,*).
$$

### Left-Low completion

`4078`, with details in `407c`, completes

$$
(L,*),
$$

including the previously open

$$
(L,T_+^{hi}).
$$

### First-Full and lower-sheet completions

`4079`, with details in `407c` and `407e`, proves that

$$
(\mathrm{Full},*)
$$

is geometrically impossible in the hard region, and closes

$$
(T_+^{lo},\mathrm{Full}),
\qquad
(T_+^{lo},T_+^{hi}).
$$

The remaining right branches for first-coordinate $T_+^{lo}$ are already covered by `4075`.

### Left-high completion

`407a`, with details in `407c` and `407e`, proves

$$
(T_+^{hi},\mathrm{Full}),
\qquad
(T_+^{hi},L),
\qquad
(T_+^{hi},T_+^{hi}),
$$

$$
(T_+^{hi},T_-),
\qquad
(T_+^{hi},T_+^{lo}).
$$

Thus

$$
(T_+^{hi},*)
$$

is closed.

## 3. Certified computations

The left-high proof uses two local finite interval certificates:

$$
\texttt{407X\_computation/407b\_T\_hi\_Tminus\_qright\_threshold\_certificate.py},
$$

and

$$
\texttt{407X\_computation/407c\_T\_hi\_Tlo\_left\_threshold\_certificate.py}.
$$

Both use exact rational interval arithmetic and one-sided integer square-root bounds. The recorded runs have zero unresolved boxes and are summarized in `407X_computation/README.md`.

## 4. Final inventory

Every hard-region branch pair is now covered:

$$
(L,*),
\qquad
(T_-,*),
\qquad
(\mathrm{Full},*),
$$

$$
(T_+^{lo},*),
\qquad
(T_+^{hi},*).
$$

Therefore every hard-region branch satisfies the `4073` boundary-loss contradiction or is geometrically impossible. Hence the full $407X$ branch is closed by `407b_final_assembly.md`.
