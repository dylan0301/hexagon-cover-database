# Current Status And Remaining Obligations For The All-Vd0 Five-Point Route

Status: Reference

This file summarizes the state of the CE0, $N_+=1$, all-Vd0 five-point route after the June 2026 proof-tree discussion. The package is split into a far-from-tight algorithm-2 subpackage and a close-to-tight algorithm-1 subpackage.

## Subpackages

| Package | Recorded status | Meaning |
|---|---|---|
| [`310X_far_from_tight/3100_far_from_tight_index.md`](310X_far_from_tight/3100_far_from_tight_index.md) | Strategy | Algorithm-2 away-from-limit route. |
| [`312X_close_to_tight/3120_close_to_tight_index.md`](312X_close_to_tight/3120_close_to_tight_index.md) | Strategy | Algorithm-1 near-limit finite-$x$ route. |

## Proved Components Recorded In This Package

| Component | File | Recorded status | Meaning |
|---|---|---|---|
| Strict line realization for $P_3,P_5$ | [`310X_far_from_tight/3105_strict_branch_line_realization.md`](310X_far_from_tight/3105_strict_branch_line_realization.md) | Proven | In the strict $\rho<1$ branch, the selected $C_2$ and $C_5$ intersections lie on $\Gamma_A^{\mathrm{lin}}$ and $\Gamma_B^{\mathrm{lin}}$. |
| Algorithm-2 two-variable model | [`310X_far_from_tight/3106_algorithm2_two_variable_transition.md`](310X_far_from_tight/3106_algorithm2_two_variable_transition.md) | Proven | Under the equality assumptions, algorithm 2 depends only on $(p,q)=(1-b_4,1-a_4)$. |
| Transition polynomial and diagonal-radius monotonicity | [`310X_far_from_tight/3106_algorithm2_two_variable_transition.md`](310X_far_from_tight/3106_algorithm2_two_variable_transition.md) | Proven | The branch transition is $T=(p+q)^4-(p+q)^2+pq$, and $r=1-c_*$ is nondecreasing. |
| Algorithm-1 tangent gap | [`312X_close_to_tight/3125_algorithm1_limit_tangent_gap.md`](312X_close_to_tight/3125_algorithm1_limit_tangent_gap.md) | Proven | The tangent coefficient satisfies $C_1\ge1/4$. |
| Convex cyclic order from line branches | [`310X_far_from_tight/3108_convex_order_from_line_branches.md`](310X_far_from_tight/3108_convex_order_from_line_branches.md) | Proven | Once line realization holds, the algorithm-2 five points have cyclic order $D_0,D_1,D_2,P_3,P_5$. |

## Strategy, Empirical, Practical, Or Certificate-Outline Components

| Component | File | Recorded status | Notes |
|---|---|---|---|
| Algorithm-2 setup and point construction | [`310X_far_from_tight/3102_algorithm2_setup_and_point_construction.md`](310X_far_from_tight/3102_algorithm2_setup_and_point_construction.md) | Strategy | Defines reduced variables, fixed $V_4$ points, and algorithm-2 diagonal points; exact relaxed-region containment remains open. |
| Far-from-tight transition strip | [`310X_far_from_tight/3101_far_from_tight_status.md`](310X_far_from_tight/3101_far_from_tight_status.md) and [`310X_far_from_tight/3109_algorithm2_transition_strip_certificate.md`](310X_far_from_tight/3109_algorithm2_transition_strip_certificate.md) | Empirical / certificate outline | Records interval constants and an interpolation scheme. Helper code is in [`310X_far_from_tight/310X_computation/`](310X_far_from_tight/310X_computation/), but full interval subdivision data is not recorded. |
| Close-to-tight diagonal remainders | [`312X_close_to_tight/3122_diagonal_remainder_progress.md`](312X_close_to_tight/3122_diagonal_remainder_progress.md) | Practically proven | Records working estimates $E_{01}\ge-2x^2$ and $E_2\ge-kx^2$; full Bernstein data not recorded. |
| Close-to-tight final $P_{\mathrm{res}}$ inequality | [`312X_close_to_tight/3123_pres_final_two_variable_target.md`](312X_close_to_tight/3123_pres_final_two_variable_target.md) | Lemma target | Final reduced two-variable target for the finite-$x$ algorithm-1 proof. |
| Symbolic identity and arithmetic helper scripts | [`310X_far_from_tight/310X_computation/`](310X_far_from_tight/310X_computation/) | Experiment | These scripts support checking identities and certificate arithmetic. They do not by themselves complete the transition-strip certificate. |

## Assembly Target

The intended proof must combine:

| Input | Current status |
|---|---|
| Fixed $V_4$ points from the strict $AB$-union frontier | Strict line-piece branch proved for $\rho<1$; boundary $\rho=1$ open. |
| Three algorithm-2 diagonal points | Two-variable construction proved under equality assumptions; containment in the relaxed obstruction region open. |
| Near-limit treatment | Algorithm-1 tangent gap proved; finite-$x$ bound open. |
| Away-region treatment | Transition strip has a certificate outline; region $p\ge0.15$ remains open. |
| Full branch reduction | Slack/equality reduction to $a_3+b_3=a_5+b_5=1$ remains open. |

## Transition-Strip Target

The transition strip is organized in the variables

$$
p=1-b_4,\qquad q=1-a_4,
$$

with

$$
0.1\le p\le0.15,\qquad p\le q.
$$

The branch transition is

$$
T(p,q)=(p+q)^4-(p+q)^2+pq.
$$

The certificate outline in
[`310X_far_from_tight/3109_algorithm2_transition_strip_certificate.md`](310X_far_from_tight/3109_algorithm2_transition_strip_certificate.md)
records the current numerical constants for:

| Edge or branch | Recorded status |
|---|---|
| Dangerous edge $P_3P_5$ | Empirical interval-certificate outline with lower value $1.0031590223\ldots$. |
| Non-dangerous edge $D_0D_1$ | Conditional interval certificate outline. |
| Non-dangerous edge $D_1D_2$ | Conditional interval certificate outline. |
| Non-dangerous edge $D_2P_3$ | Conditional interpolation certificate outline. |
| Non-dangerous edge $P_5D_0$ | Conditional interpolation certificate outline. |

Until verifier data is added, these remain empirical or certificate-outline
claims, not proven lemmas.

## Still Open

The all-Vd0 five-point route does not yet prove the CE0 all-Vd0 branch. The remaining obligations are:

| Obligation | Status |
|---|---|
| Justify the reductions $a_3+b_3=1$ and $a_5+b_5=1$ from the full all-Vd0 branch. | Open. |
| Treat the limiting boundary $\rho=1$ for the strict $AB$ curve. | Open. |
| Replace the far-from-tight transition-strip outline with reproducible verifier code or exact certificate data for all endpoint and curvature interval enclosures. | Open. |
| Complete the far-from-tight algorithm-2 region for $p\ge0.15$ and its reflection. | Open. |
| Prove the close-to-tight final two-variable target $P_{\mathrm{res}}\ge(2+k)x^2$, or replace it by another certified finite-$x$ argument. | Open. |
| Prove that the algorithm-2 diagonal points are valid obstruction points for the exact relaxed region required by the CE0 all-Vd0 branch. | Open. |
| Assemble the close-to-tight and far-from-tight arguments into a full branch obstruction. | Open. |

## Failed Or Discarded Routes

The following routes should not be reused without new hypotheses.

| Route | Reason |
|---|---|
| Global coordinate-wise unimodality of the algorithm-1 function in $a_1,b_1$. | Numerical counterexamples show support-regime switching creates non-unimodal slices. |
| Reducing algorithm 1 to vertices where two of $a_0+b_0,a_1+b_1,a_2+b_2$ equal $1$. | Numerical examples have smaller values on edge interiors. |
| Algorithm 2 near the vertex-limit corners. | The tangent coefficient is negative for approach directions $1/3<k<1$. |
| Global coordinate monotonicity of $P_3,P_5$. | For example, $P_3^y$ can decrease as $q$ increases. |
| Ordinary convex-hull inclusion under slack pushes. | Individual support functions can move the wrong way; only the three-direction width has the hoped-for cancellation. |
| Near-tight $x$-convexity of the finite-$x$ residual. | Stable second differences are negative in some smooth regions. |
| Componentwise finite-linear diagonal bounds $r_j\ge xd_j$. | Diagonal deficits occur and are compensated by the $P_3P_5$ side term. |
