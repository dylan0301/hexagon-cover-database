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

## General Files

| File | Recorded status | Notes |
|---|---|---|
| [`3104_may21_four_point_warning.md`](3104_may21_four_point_warning.md) | Failed | Warning for the failed May 21 four-point route. |
| [`3110_current_status_and_remaining_obligations.md`](3110_current_status_and_remaining_obligations.md) | Reference | Current status ledger and remaining obligations. |

Route-specific notes and computation helpers are classified inside the
far-from-tight and close-to-tight subpackages above.

## Archived Related Route

| File | Recorded status | Notes |
|---|---|---|
| [`../../../9XXX_failed_ideas/963X_may25_five_point_failure/9631_CE0_may25_supremum_endpoint_archive.md`](../../../9XXX_failed_ideas/963X_may25_five_point_failure/9631_CE0_may25_supremum_endpoint_archive.md) | Failed | Archived May 25 supremum-endpoint route; superseded and not a live all-Vd0 dependency. |
