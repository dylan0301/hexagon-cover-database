# Far-From-Tight Subpackage For The CE0 All-Vd0 Five-Point Route

Status: Strategy

This subpackage collects the far-from-tight part of the CE0, $N_+=1$, all-Vd0 five-point route. In the current strategy, far-from-tight means the algorithm-2 region away from the two vertex-limit corners.

## Files In This Subpackage

| File | Recorded status | Role |
|---|---|---|
| [`3100a1_far_from_tight_status.md`](3100a1_far_from_tight_status.md) | Reference | Current far-from-tight proof status, proved inputs, and remaining certificate obligations. |
| [`3100a2_algorithm2_setup_and_point_construction.md`](3100a2_algorithm2_setup_and_point_construction.md) | Strategy | Reduced variables, fixed $V_4$ points, and algorithm-2 diagonal points; key containment remains empirical. |
| [`3100a5_strict_branch_line_realization.md`](3100a5_strict_branch_line_realization.md) | Proven | Strict $\rho<1$ realization of $P_3,P_5$ on the two $309$ line pieces. |
| [`3100a6_algorithm2_two_variable_transition.md`](3100a6_algorithm2_two_variable_transition.md) | Strategy | Exact two-variable reduction and radial formulas; their transition use needs selector-aware rechecking. |
| [`3100a8_convex_order_from_line_branches.md`](3100a8_convex_order_from_line_branches.md) | Proven | Convex cyclic order $D_0,D_1,D_2,P_3,P_5$ once line realization holds. |
| [`3100a9_algorithm2_transition_strip_certificate.md`](3100a9_algorithm2_transition_strip_certificate.md) | Empirical / certificate outline | Transition-strip numerical constants and interpolation-certificate outline. |
| [`3100aX_computation/`](3100aX_computation/) | Experiment | Helper scripts for symbolic identity checks, interval arithmetic, numerical modeling, and certificate arithmetic. |

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
