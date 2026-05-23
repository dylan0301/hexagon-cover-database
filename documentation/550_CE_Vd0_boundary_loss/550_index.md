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
