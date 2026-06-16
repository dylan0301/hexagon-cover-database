# Close-To-Tight Subpackage For The CE0 All-Vd0 Five-Point Route

Status: Strategy

This subpackage records the close-to-tight part of the CE0, $N_+=1$, all-Vd0 route. Close-to-tight means a neighborhood of the two vertex-limit corners where algorithm 2 fails and algorithm 1 is used instead.

The parent package records the tangent inequality

$$
C_1\ge\frac14
$$

in [`../3107_algorithm1_limit_tangent_gap.md`](../3107_algorithm1_limit_tangent_gap.md). That file does not prove a finite-$x$ remainder estimate.

## Files In This Subpackage

| File | Recorded status | Notes |
|---|---|---|
| [`3121_algorithm1_finite_x_setup.md`](3121_algorithm1_finite_x_setup.md) | Lemma target | Near-tight scaling, dominant-branch residual, and finite-$x$ target. |
| [`3122_diagonal_remainder_progress.md`](3122_diagonal_remainder_progress.md) | Practically proven | Working diagonal remainder bounds $E_{01}\ge-2x^2$ and $E_2\ge-kx^2$; full Bernstein data not recorded. |
| [`3123_pres_final_two_variable_target.md`](3123_pres_final_two_variable_target.md) | Lemma target | Final reduced two-variable inequality for $P_{\mathrm{res}}$. |
| [`3124_failed_near_tight_shortcuts.md`](3124_failed_near_tight_shortcuts.md) | Failed | Convexity and componentwise diagonal shortcuts that should not be reused. |

## Current Close-To-Tight Goal

The current goal is to prove the finite-$x$ inequality

$$
f_{\mathrm{algo1}}(x,k,s,\tau)\ge 1+xC_1(k,s,\tau)
$$

on the valid near-limit domain. The recorded reductions lower this to the final two-variable target in [`3123_pres_final_two_variable_target.md`](3123_pres_final_two_variable_target.md), but that target is still open.
