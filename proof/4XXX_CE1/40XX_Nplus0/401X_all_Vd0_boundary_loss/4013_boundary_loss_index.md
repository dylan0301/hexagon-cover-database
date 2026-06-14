# CE1/CE2 Vd0 Boundary-Loss Package

Status: Proven local lemma

This folder records the proof package for the CE1/CE2, all-Vd0 boundary-loss obstruction.

The proved local statement is:

$$
\mathrm{CE1/CE2}+\text{all six }V_i\text{ are Vd0}+\text{all }a_i+b_i\le 1 \quad\Longrightarrow\quad \text{boundary-loss contradiction.}
$$

For CE2 this still uses the CE2 one-interval lemma under the V4 supercritical
hypothesis.

Equivalently, under the CE1/CE2 reductions recorded here, any successful all-Vd0 covering must have at least one vertex triangle with

$$
a_i+b_i>1.
$$

## Boundary-loss reduction

Work under the contradiction assumptions

$$
\mathrm{CE1/CE2}+\text{all six }V_i\text{ are Vd0}+\text{all }a_i+b_i\le1.
$$

After normalization, the active $C$-boundary interval is

$$
T_C\cap e_{0,1}=[s,t], \qquad u=1-t, \qquad w=t-s>0.
$$

The adjacent maximal Vd0 contributions are

$$
B_5=B(s,1-\gamma_5), \qquad B_1=B(u,1-\gamma_1),
$$

where

$$
B(a,c)=\max\{b:(a,b,c)\in\mathcal A,\ a+b\le1\}.
$$

Let

$$
F=B_5+B_1.
$$

The reduction in
[`4014_setup_and_reduction.md`](4014_setup_and_reduction.md)
(Status: Strategy with proven reduction) shows that $F<1$ gives the boundary contradiction: the portion left for $V_2,V_3,V_4$ has length $4-F>3$, while

$$
(a_2+b_2)+(a_3+b_3)+(a_4+b_4)\le3.
$$

Therefore the branch analysis target is

$$
F<1.
$$

Branch labels use the corrected maximal meaning from
[`4015_B_map_branch_realization.md`](4015_B_map_branch_realization.md)
(Status: Definition with proven local branch-realization lemmas): a branch label means the value of $B(a,c)$ is actually realized as the maximal admissible $b$, not merely that a formal algebraic root exists.

## Files

| File | Recorded status | Notes |
|---|---|---|
| [`4012_remaining_reductions_to_all_Vd0.md`](4012_remaining_reductions_to_all_Vd0.md) | Strategy | Remaining reductions to all Vd0. |
| [`4014_setup_and_reduction.md`](4014_setup_and_reduction.md) | Strategy with proven reduction | Target, notation, C-triangle parameterization, and reduction to $F<1$. |
| [`4015_B_map_branch_realization.md`](4015_B_map_branch_realization.md) | Definition with proven local branch-realization lemmas | Corrected definition of $B(a,c)$ and branch-realization conditions. |
| [`4016_proven_branch_lemmas.md`](4016_proven_branch_lemmas.md) | Proven local lemmas, with remaining branches recorded elsewhere | Previously proved branch lemmas. |
| [`4017_remaining_Tplus_obligations.md`](4017_remaining_Tplus_obligations.md) | Reference / superseded | Historical record of the lower-sheet obligations and failed approaches; superseded by [`4019_lower_sheet_completion_proofs.md`](4019_lower_sheet_completion_proofs.md) for proof status. |
| [`4018_computational_verification.md`](4018_computational_verification.md) | Empirical / certificate support, with lower-sheet observations superseded by proof | Numerical checks, interval-certificate status, and code references. |
| [`4019_lower_sheet_completion_proofs.md`](4019_lower_sheet_completion_proofs.md) | Proven local lemma | Analytic proofs of the formerly remaining lower-sheet branches $(T_+^{lo},T_-)$, $(T_+^{lo},T_+^{hi})$, and $(T_+^{lo},T_+^{lo})$. |
| [`../409X_boundary_loss_experiments/4090_README.md`](../409X_boundary_loss_experiments/4090_README.md) | Computational helpers | Experiment helpers for the package. |

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
- $(T_+^{lo},T_-)$.
- $(T_+^{lo},T_+^{hi})$.
- $(T_+^{lo},T_+^{lo})$.

No realized branch pair remains open for the boundary-loss inequality $F<1$ under the assumptions of
[`4014_setup_and_reduction.md`](4014_setup_and_reduction.md)
(Status: Strategy with proven reduction).
