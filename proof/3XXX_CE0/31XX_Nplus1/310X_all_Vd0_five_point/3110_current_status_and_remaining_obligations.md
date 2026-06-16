# Current Status And Remaining Obligations For The Algorithm-2 Route

Status: Reference

This file summarizes the state of the CE0, $N_+=1$, all-Vd0 algorithm-2 route after the June 2026 proof-tree discussion.

## Proved Components Recorded In This Package

| Component | File | Recorded status | Meaning |
|---|---|---|---|
| Strict line realization for $P_3,P_5$ | [`3105_strict_branch_line_realization.md`](3105_strict_branch_line_realization.md) | Proven | In the strict $\rho<1$ branch, the selected $C_2$ and $C_5$ intersections lie on $\Gamma_A^{\mathrm{lin}}$ and $\Gamma_B^{\mathrm{lin}}$. |
| Algorithm-2 two-variable model | [`3106_algorithm2_two_variable_transition.md`](3106_algorithm2_two_variable_transition.md) | Proven | Under the equality assumptions, algorithm 2 depends only on $(p,q)=(1-b_4,1-a_4)$. |
| Transition polynomial and diagonal-radius monotonicity | [`3106_algorithm2_two_variable_transition.md`](3106_algorithm2_two_variable_transition.md) | Proven | The branch transition is $T=(p+q)^4-(p+q)^2+pq$, and $r=1-c_*$ is nondecreasing. |
| Algorithm-1 tangent gap | [`3107_algorithm1_limit_tangent_gap.md`](3107_algorithm1_limit_tangent_gap.md) | Proven | The tangent coefficient satisfies $C_1\ge1/4$. |
| Convex cyclic order from line branches | [`3108_convex_order_from_line_branches.md`](3108_convex_order_from_line_branches.md) | Proven | Once line realization holds, the algorithm-2 five points have cyclic order $D_0,D_1,D_2,P_3,P_5$. |

## Empirical Or Certificate-Outline Components

| Component | File | Recorded status | Notes |
|---|---|---|---|
| Algorithm-2 transition strip | [`3109_algorithm2_transition_strip_certificate.md`](3109_algorithm2_transition_strip_certificate.md) | Empirical / certificate outline | Records interval constants and an interpolation scheme. Helper code is in [`310X_computation/`](310X_computation/), but full interval subdivision data is not recorded. |
| Numerical away-region behavior | [`3109_algorithm2_transition_strip_certificate.md`](3109_algorithm2_transition_strip_certificate.md) and [`310X_computation/algo2_numeric_model.py`](310X_computation/algo2_numeric_model.py) | Empirical | The lowest recorded dangerous value is $1.0031590223\ldots$ at $p=0.1$ and $T=0$. |
| Symbolic identity and arithmetic helper scripts | [`310X_computation/`](310X_computation/) | Experiment | These scripts support checking identities and certificate arithmetic. They do not by themselves complete the transition-strip certificate. |

## Still Open

The algorithm-2 route does not yet prove the CE0 all-Vd0 branch. The remaining obligations are:

| Obligation | Status |
|---|---|
| Justify the reductions $a_3+b_3=1$ and $a_5+b_5=1$ from the full all-Vd0 branch. | Open. |
| Treat the limiting boundary $\rho=1$ for the strict $AB$ curve. | Open. |
| Replace the transition-strip certificate outline with reproducible verifier code or exact certificate data for all endpoint and curvature interval enclosures. | Open. |
| Complete the algorithm-2 away region for $p\ge0.15$ and its reflection. | Open. |
| Prove the near-limit finite-$x$ algorithm-1 remainder bound, or replace it by another certified near-limit argument. | Open. |
| Prove that the algorithm-2 diagonal points are valid obstruction points for the exact relaxed region required by the CE0 all-Vd0 branch. | Open. |
| Assemble the algorithm-1 near-limit and algorithm-2 away-region arguments into a full branch obstruction. | Open. |

## Failed Or Discarded Routes

The following routes should not be reused without new hypotheses.

| Route | Reason |
|---|---|
| Global coordinate-wise unimodality of the algorithm-1 function in $a_1,b_1$. | Numerical counterexamples show support-regime switching creates non-unimodal slices. |
| Reducing algorithm 1 to vertices where two of $a_0+b_0,a_1+b_1,a_2+b_2$ equal $1$. | Numerical examples have smaller values on edge interiors. |
| Algorithm 2 near the vertex-limit corners. | The tangent coefficient is negative for approach directions $1/3<k<1$. |
| Global coordinate monotonicity of $P_3,P_5$. | For example, $P_3^y$ can decrease as $q$ increases. |
| Ordinary convex-hull inclusion under slack pushes. | Individual support functions can move the wrong way; only the three-direction width has the hoped-for cancellation. |
