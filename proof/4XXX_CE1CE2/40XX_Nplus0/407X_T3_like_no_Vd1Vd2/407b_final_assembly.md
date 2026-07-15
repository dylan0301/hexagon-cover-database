# Final Assembly of the $407X$ Branch

Status: Reference

This file records the historical assembly of the branch

$$
T_C\text{ is CE1 or CE2},\qquad N_+=0,
$$

with no Vd1/Vd2 rows and at least one T3-like row.

Dependency warning: this is the superseded assembly. Its old branch list used
a fake Cell-$T$ sheet and did not prove completeness for the exact safe map.
The corrected four-label partition is now proved in `2011`, and the canonical
exact-formula reassembly is `407d`.

The detailed auxiliary inequalities used in the compressed branch files are recorded in
[`407c_detailed_gap_closure.md`](407c_detailed_gap_closure.md) and the final remaining gap fixes are recorded in
[`407e_final_gap_fixes.md`](407e_final_gap_fixes.md).  Thus this assembly uses the branch files together with the expanded gap-closure lemmas and the two local finite interval certificates.

## 1. Structural reductions

The file `4071` proves that, after the normalization

$$
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\},
$$

one has

$$
T_0\text{ is T3-like}.
$$

The file `4072` proves the support isolation, after reflecting so that $T_0$ supports $r_1$:

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

The file `4073` proves the boundary-loss reduction: it is enough to prove

$$
B(A_5,C_5)+B(A_1,C_1)<1.
$$

The same conclusion holds with the stricter neighboring-ray constrained right map in the case where $T_1$ contributes to $r_0$, because the constrained map is no larger than $B(A_1,C_1)$.

## 2. Branch coverage

The easy region

$$
A_1+A_5>1
$$

is already included in the boundary-loss package.

The hard-region branches are covered as follows.

### Previously recorded files

The branch

$$
(L,\mathrm{Full})
$$

is proved in `4074`.

The branches

$$
(B_5,B_1)\in\{L,T_-,T_+^{lo}\}^2
$$

and all branches with first coordinate $T_-$ are proved in `4075`.

### New completion files

The file `4078_left_L_family_completion.md`, with details supplied in `407c_detailed_gap_closure.md`, proves the remaining left-Low branches, including

$$
(L,T_+^{hi}).
$$

The file `4079_first_Full_and_lower_sheet_branches.md`, with details supplied in `407c_detailed_gap_closure.md` and `407e_final_gap_fixes.md`, proves

$$
(\mathrm{Full},*)\text{ is impossible},
$$

and proves or excludes the remaining first-coordinate lower-sheet branches

$$
(T_+^{lo},\mathrm{Full}),
\qquad
(T_+^{lo},T_+^{hi}).
$$

The file `407a_left_Thigh_branch_completion.md`, with details supplied in `407c_detailed_gap_closure.md` and `407e_final_gap_fixes.md`, proves all first-coordinate high-sheet branches:

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

The two finite interval certificates used there are recorded in

$$
\texttt{407X\_computation/407b\_T\_hi\_Tminus\_qright\_threshold\_certificate.py}
$$

and

$$
\texttt{407X\_computation/407c\_T\_hi\_Tlo\_left\_threshold\_certificate.py}.
$$

The recorded runs are summarized in `407X_computation/README.md`. Both certificates use exact rational interval arithmetic with one-sided square-root bounds and record zero unresolved boxes.

## 3. Conclusion

Every hard-region realized branch pair satisfies

$$
B(A_5,C_5)+B(A_1,C_1)<1,
$$

or is geometrically impossible in the $407X$ domain.  Therefore, by `4073`, the support-isolated $407X$ branch gives a perimeter contradiction.

The missing partition proof in this historical version is now supplied by
`2011`. The exact four-label conclusion and current package status are recorded
in `407d`; this superseded file does not independently determine that status.

The branch under discussion is

$$
T_C\text{ is CE1 or CE2},\qquad N_+=0,
$$

with no Vd1/Vd2 rows and at least one T3-like row.
