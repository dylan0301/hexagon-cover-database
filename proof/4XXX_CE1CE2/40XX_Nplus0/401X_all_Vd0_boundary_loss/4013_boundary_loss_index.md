# CE1/CE2 Vd0 Boundary-Loss Package

Status: Strategy

This folder records the proposed proof package for the CE1/CE2, all-Vd0
boundary-loss obstruction. Its former `Proven` status was not supported: the
branch inventory used the fake Cell-2 sheet corrected in `2007` and `4015`,
and its CE2 reduction cited a supercritical hypothesis inside an $N_+=0$
branch.

The target local statement is:

$$
\mathrm{CE1/CE2}+\text{all six }V_i\text{ are Vd0}+\text{all }a_i+b_i\le 1 \quad\Longrightarrow\quad \text{boundary-loss contradiction.}
$$

For CE2, the replacement theorem in `2104` removes a two-gap system only up to
possible V-type and $N_+$ exits. Those exits remain an assembly obligation.

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
B_5=\mathsf B^0_{1-\gamma_5}(s),
\qquad
B_1=\mathsf B^0_{1-\gamma_1}(u),
$$

where

$$
\mathsf B^0_c(a)
=
\sup_{\substack{
A(T)\ge a\\
C(T)\ge c\\
A(T)+B(T)\le1\\
T\text{ is Vd0}
}}B(T).
$$

Let

$$
F=B_5+B_1.
$$

The reduction in
[`4014_setup_and_reduction.md`](4014_setup_and_reduction.md)
(Status: Strategy) shows conditionally that $F<1$ gives the boundary
contradiction: the portion left for $V_2,V_3,V_4$ has length $4-F>3$, while

$$
(a_2+b_2)+(a_3+b_3)+(a_4+b_4)\le3.
$$

Therefore the branch analysis target is

$$
F<1.
$$

The corrected semantics and the reason the old labels are not yet a complete
geometric partition are recorded in
[`4015_B_map_branch_realization.md`](4015_B_map_branch_realization.md)
(Status: Definition).

## Files

| File | Recorded status | Notes |
|---|---|---|
| [`4014_setup_and_reduction.md`](4014_setup_and_reduction.md) | Strategy | Target, notation, C-triangle parameterization, and proven reduction to $F<1$. |
| [`4015_B_map_branch_realization.md`](4015_B_map_branch_realization.md) | Definition | Corrected demand/actual semantics and withdrawal of the fake high-$c$ sheet. |
| [`4016_proven_branch_lemmas.md`](4016_proven_branch_lemmas.md) | Strategy | Historical algebraic inequalities pending actual-coordinate classified-map inclusion audit. |
| [`4017_remaining_Tplus_obligations.md`](4017_remaining_Tplus_obligations.md) | Reference | Historical record of the discarded lower-sheet obligations and failed approaches; cross-read with [`4019_lower_sheet_completion_proofs.md`](4019_lower_sheet_completion_proofs.md) as algebraic history only. |
| [`4018_computational_verification.md`](4018_computational_verification.md) | Empirical | Numerical checks, interval-certificate status, and code references. |
| [`4019_lower_sheet_completion_proofs.md`](4019_lower_sheet_completion_proofs.md) | Strategy | Historical calculations on the now-discarded lower sheet. |
| [`401aX_boundary_loss_experiments/401a0_README.md`](401aX_boundary_loss_experiments/401a0_README.md) | Experiment | Experiment helpers for the package. |

## Historical branch calculations

The following algebraic cells have recorded calculations in this package:

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

These calculations do not currently prove completeness for the exact
actual-coordinate map $\mathsf B^0$. The package remains Strategy until the
true-branch inclusion and CE2 replacement exits are certified.
