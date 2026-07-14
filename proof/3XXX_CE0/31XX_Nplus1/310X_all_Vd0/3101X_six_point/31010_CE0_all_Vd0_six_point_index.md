# CE0 All-Vd0 Six-Point Strategy

Status: Strategy

This package records the six-point core construction and the associated
two-variable optimization target for the CE0, $N_+=1$, all-Vd0 branch.

It is a strategy package: the recorded reduction is local, and the branch is
closed only if the remaining optimized enclosing-triangle inequality is proved.
Numerical or plotted behavior remains empirical unless a rigorous certificate
is recorded.

## Flow

| Step | File | Recorded status | Role |
|---:|---|---|---|
| 1 | [`31011_six_point_construction.md`](31011_six_point_construction.md) | Definition | Defines the relaxed six-point set $K_6^{\mathrm{rel}}(a,b)$. |
| 2 | [`31012_core_graph_two_variable_relaxation.md`](31012_core_graph_two_variable_relaxation.md) | Proven | Using the proved strict-union theorem `20091` and its proved limiting degeneration, reduces the branch to a two-variable optimization over $(a,b)$. |
| 3 | [`31013_core_surface_definition.md`](31013_core_surface_definition.md) | Definition | Defines the enclosing-triangle side-length surface $F_6(a,b)$. |
| 4 | [`31015_minimum_curve_limit_figures.md`](31015_minimum_curve_limit_figures.md) | Empirical | Records minimum-curve figures and the observed near-limit support pattern. |
| 5 | [`31016_fixed_angle_g_strategy.md`](31016_fixed_angle_g_strategy.md) | Strategy | Defines the fixed-angle function $G_E(a,b,\theta)$. |
| 6 | [`31017_ray_transition_curve_minimum_conjecture.md`](31017_ray_transition_curve_minimum_conjecture.md) | Lemma target | Defines minimum relations, slice partitions, and transition targets. |

## Supporting Notes

| File | Recorded status | Role |
|---|---|---|
| [`31018_ray_transition_computation_memo.md`](31018_ray_transition_computation_memo.md) | Experiment | Numerical tests for the slice families. |
| [`31019_constant_difference_slice_minimum_target.md`](31019_constant_difference_slice_minimum_target.md) | Lemma target | Primary constant-$d=q-p$ optimized-slice target. |
| [`3101a_slice_family_status_catalog.md`](3101a_slice_family_status_catalog.md) | Experiment | Success/failure catalog and recommended proof direction. |
