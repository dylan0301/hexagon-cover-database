# Far-From-Tight Subpackage For The CE0 All-Vd0 Five-Point Route

Status: Strategy

This subpackage collects the far-from-tight part of the CE0, $N_+=1$, all-Vd0 five-point route. In the current strategy, far-from-tight means the algorithm-2 region away from the two vertex-limit corners.

The parent package remains the source for shared definitions and core local lemmas. In particular:

| File | Recorded status | Role |
|---|---|---|
| [`../3105_strict_branch_line_realization.md`](../3105_strict_branch_line_realization.md) | Proven | Strict $\rho<1$ realization of $P_3,P_5$ on the two $309$ line pieces. |
| [`../3106_algorithm2_two_variable_transition.md`](../3106_algorithm2_two_variable_transition.md) | Proven | Algorithm-2 two-variable model, transition polynomial, and diagonal-radius monotonicity. |
| [`../3108_convex_order_from_line_branches.md`](../3108_convex_order_from_line_branches.md) | Proven | Convex cyclic order $D_0,D_1,D_2,P_3,P_5$ once line realization holds. |
| [`../3109_algorithm2_transition_strip_certificate.md`](../3109_algorithm2_transition_strip_certificate.md) | Empirical / certificate outline | Transition-strip numerical constants and interpolation-certificate outline. |

## Files In This Subpackage

| File | Recorded status | Notes |
|---|---|---|
| [`3101_far_from_tight_status.md`](3101_far_from_tight_status.md) | Reference | Current far-from-tight proof status, proved inputs, and remaining certificate obligations. |

## Current Boundary Of The Proof

The transition strip

$$
0.1\le p\le0.15
$$

has a recorded certificate outline but not a repository-grade certificate. The farther region

$$
p\ge0.15
$$

still needs a finite interval, Taylor, or algebraic certificate.
