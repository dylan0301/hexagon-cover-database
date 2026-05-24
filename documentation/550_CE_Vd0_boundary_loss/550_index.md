# CE1/CE2 Vd0 Boundary-Loss Package

Status: Strategy with proven local lemmas and remaining proof obligations

This folder records the current proof package for the CE1/CE2, all-Vd0 boundary-loss obstruction discussed in the working notes.

The intended global obstruction is:

$$
\mathrm{CE1/CE2}+\text{all six }V_i\text{ are Vd0}+\text{all }a_i+b_i\le 1
\quad\Longrightarrow\quad
\text{the target boundary cannot be covered.}
$$

Equivalently, in any successful CE1/CE2 Vd0 covering of the target boundary, at least one vertex triangle must satisfy

$$
a_i+b_i>1.
$$

This package is not yet a finished proof of the full CE1/CE2 Vd0 case.  It contains a rigorous reduction, a corrected admissible-map formulation, several proven branch lemmas, numerical tests, and a precise list of remaining obligations.

## Working strategy

The strategy is a boundary-loss argument.  Work under the contradiction assumptions

$$
\mathrm{CE1/CE2}+\text{all six }V_i\text{ are Vd0}+\text{all }a_i+b_i\le1.
$$

After normalization, the active $C$-boundary interval is

$$
T_C\cap e_{0,1}=[s,t],
\qquad
u=1-t,
\qquad
w=t-s>0.
$$

For CE2, this uses the CE2 one-interval reduction assumed in `551_setup_and_reduction.md`; this folder does not prove that reduction.

The adjacent $V_5$- and $V_1$-triangles can help cover boundary near the active interval.  For a fixed input boundary coordinate $a$ and radial requirement $c$, the corrected maximal Vd0 contribution is

$$
B(a,c)=\max\{b:(a,b,c)\in\mathcal A,\ a+b\le1\}.
$$

The two adjacent maximal contributions are

$$
B_5=B(s,1-\gamma_5),
\qquad
B_1=B(u,1-\gamma_1),
$$

and the boundary-loss objective is

$$
F=B_5+B_1.
$$

If $F<1$, then the boundary left for $V_2,V_3,V_4$ has length at least

$$
(1-B_1)+1+1+(1-B_5)=4-F>3.
$$

But the contradiction assumption gives

$$
(a_2+b_2)+(a_3+b_3)+(a_4+b_4)\le3.
$$

Thus $F<1$ contradicts boundary coverage.  As a simple counting example, a hypothetical certified bound $F\le0.95$ would leave at least $3.05$ units of boundary for only three Vd0 triangles whose total allowed contribution is at most $3$.

The main technical point is that a branch pair must describe realized maxima, not formal algebraic roots.  For example,

$$
(L,\mathrm{Full})
$$

means $B_5$ is actually realized on the Low branch and $B_1=1-u$ satisfies the exact Full branch conditions.  It is not enough for the Low or Full equations to have roots; the candidate must satisfy all cell inequalities and be maximal among admissible candidates.  This correction removes fake branches such as $(\mathrm{Full},\mathrm{Full})$ and prevents treating $D_1$ as an independent maximal branch.

The proved branch lemmas use a few recurring proof styles.  In branches such as $(L,\mathrm{Full})$ and $(T_-,\mathrm{Full})$, the goal is to show the non-Full side is smaller than the available gap.  For instance, if $B_1=1-u$, then proving $B_5<u$ gives

$$
F=B_5+(1-u)<1.
$$

The branch $(\mathrm{Full},L)$ is split into a tight horn near $r=1$, handled analytically, and a far region handled by a finite interval certificate.  The branch $(L,T_+)$ is similar: large $r$ is handled analytically, while $1<r<10$ is certified by the corrected interval verifier using the exact $T_+$ loss equation.  Left $T_+^{hi}$ branches use a frontier comparison: convexity and endpoint checks force inequalities such as $s\ge S-u$, which then prove or eliminate several high-sheet cases.

The remaining difficulty is not numerical tightness but proof of a uniform analytic gap for lower-sheet left $T_+$ branches.  The still-open cases are

$$
(T_+^{lo},T_-),
\qquad
(T_+^{lo},T_+^{hi}),
\qquad
(T_+^{lo},T_+^{lo}).
$$

The current evidence suggests these branches stay below $F=1$, but that evidence is empirical until the coupled lower-sheet estimates in `554_remaining_Tplus_obligations.md` are proved.

## Files

- `551_setup_and_reduction.md`: target, notation, C-triangle parameterization, and reduction to the boundary-loss inequality $F<1$.
- `552_B_map_branch_realization.md`: corrected definition of $B(a,c)$ as a maximal admissible value, branch-realization conditions, and why algebraic roots alone create fake branches.
- `553_proven_branch_lemmas.md`: proven branch lemmas currently available, including the main high branches and the convexity/endpoint arguments for $T_+^{hi}$.
- `554_remaining_Tplus_obligations.md`: remaining coupled $T_+$ cases and exact unsolved inequalities.
- `555_computational_verification.md`: numerical checks, interval-certificate status, and code references.

## Code

Related scripts are in:

- `experiments/ce_vd0_boundary_loss/`

The scripts are exploratory or certificate-style helpers.  Numerical outputs stay empirical unless the corresponding script and certificate conditions are explicitly stated in a documentation file.

## Current status

Proved or eliminated in this package:

- $(L,\mathrm{Full})$.
- $(T_-,\mathrm{Full})$.
- $(\mathrm{Full},L)$, using a local analytic horn proof plus a finite interval certificate for the far region.
- $(\mathrm{Full},T_-)$.
- $(\mathrm{Full},\mathrm{Full})$ is impossible.
- $D_1$ is not an independent maximal branch.
- $(L,T_+)$.
- $(T_+,\mathrm{Full})$ is impossible.
- $(T_+^{hi},L)$ and $(T_+^{lo},L)$.
- $(T_+^{hi},T_-)$.
- $(T_+^{hi},T_+^{hi})$ is impossible.

Still not certified:

- $(T_+^{lo},T_-)$.
- $(T_+^{lo},T_+^{hi})$.
- $(T_+^{lo},T_+^{lo})$.

The remaining coupled-loss target is

$$
d_1+d_5>w
$$

for the lower-sheet $T_+T_+$ cases, together with the corresponding one-low-sheet cases.
