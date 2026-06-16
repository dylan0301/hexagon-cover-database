# CE0 All-Vd0 Five-Point Route

Status: Strategy

This folder records the live all-Vd0, one-supercritical CE0 route suggested by `prompts/20260610prooftreeSketch.txt`.

The branch assumptions are:

$$
T_C\text{ is CE0},\qquad N_+=1,
$$

and all six vertex roles are Vd0.

The live route is a finite-point strategy with two complementary parts:

- far from the vertex-limit corners, use algorithm 2;
- close to the vertex-limit corners, use algorithm 1 and a finite-$x$ remainder estimate.

Numerical evidence is not proof. Claims remain strategy, lemma target, empirical, or certificate outline until a proof file records a proven status.

## Subpackages

| Package | Recorded status | Role |
|---|---|---|
| [`310X_far_from_tight/3100_far_from_tight_index.md`](310X_far_from_tight/3100_far_from_tight_index.md) | Strategy | Algorithm-2 away-from-limit region, including strict line realization, transition polynomial, convex order, and transition-strip certificate outline. |
| [`312X_close_to_tight/3120_close_to_tight_index.md`](312X_close_to_tight/3120_close_to_tight_index.md) | Strategy | Algorithm-1 near-limit finite-$x$ route, including tangent gap, diagonal remainder progress, and the final $P_{\mathrm{res}}$ target. |

## Shared And Legacy Files

| File | Recorded status | Notes |
|---|---|---|
| [`3102_algorithm2_setup_and_point_construction.md`](3102_algorithm2_setup_and_point_construction.md) | Empirical strategy | Reduced variables, fixed $V_4$ points, and algorithm-2 diagonal points. |
| [`3103_algorithm2_obligations_and_status.md`](3103_algorithm2_obligations_and_status.md) | Reference | Assembly target, proof obligations, and status table. |
| [`3104_may21_four_point_warning.md`](3104_may21_four_point_warning.md) | Failed | Warning for the failed May 21 four-point route. |
| [`3105_strict_branch_line_realization.md`](3105_strict_branch_line_realization.md) | Proven local lemma | Strict $\rho<1$ realization of the selected $P_3,P_5$ intersections on the two $309$ line pieces. |
| [`3106_algorithm2_two_variable_transition.md`](3106_algorithm2_two_variable_transition.md) | Proven local lemma | Algorithm-2 two-variable reduction, transition polynomial, radius monotonicity, and limit failure. |
| [`3107_algorithm1_limit_tangent_gap.md`](3107_algorithm1_limit_tangent_gap.md) | Proven analytic inequality | Near-limit algorithm-1 tangent coefficient satisfies $C_1\ge1/4$. |
| [`3108_convex_order_from_line_branches.md`](3108_convex_order_from_line_branches.md) | Proven local lemma | Line branches imply $s\ge u$, $v\ge t$, and convex cyclic order for the algorithm-2 five points. |
| [`3109_algorithm2_transition_strip_certificate.md`](3109_algorithm2_transition_strip_certificate.md) | Empirical / certificate outline | Transition-strip numerical constants and interpolation-certificate outline; verifier data not recorded. |
| [`3110_current_status_and_remaining_obligations.md`](3110_current_status_and_remaining_obligations.md) | Reference | Current status ledger and remaining obligations. |
| [`310X_computation/`](310X_computation/) | Implementation note | Helper scripts for symbolic identity checks, interval arithmetic, numerical modeling, and certificate arithmetic. |

## Archived Related Route

| File | Recorded status | Notes |
|---|---|---|
| [`../../../9XXX_failed_ideas/963X_may25_five_point_failure/9631_CE0_may25_supremum_endpoint_archive.md`](../../../9XXX_failed_ideas/963X_may25_five_point_failure/9631_CE0_may25_supremum_endpoint_archive.md) | Failed / superseded | Archived May 25 supremum-endpoint route; not a live all-Vd0 dependency. |
