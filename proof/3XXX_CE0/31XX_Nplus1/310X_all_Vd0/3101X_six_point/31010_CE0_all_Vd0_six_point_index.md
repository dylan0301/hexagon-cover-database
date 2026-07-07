# CE0 All-Vd0 Six-Point Strategy

Status: Strategy

This package records the six-point core construction and the associated
two-variable graph definitions for the CE0, $N_+=1$, all-Vd0 branch.

These files define the relaxed-P construction, prove the local relaxed-P
two-variable reduction, and define the visualization target.  They do not prove
that the branch is closed, and numerical or plotted behavior remains empirical
unless a rigorous certificate is recorded.

The construction was transcribed from `dylan0301/hexagon-cover-visual` branch
`gulgu`, with the two-line $AB$-superset variant checked against commit
`6dacaa72047d67a5d7c3e5fbc4bccb26c3e72732`.  The definitions below are written
self-contained in this package.

## Files

| File | Recorded status | Notes |
|---|---|---|
| [`31011_six_point_construction.md`](31011_six_point_construction.md) | Definition | Defines the relaxed-P two-line $AB$-superset construction, with $P_3^{\mathrm{rel}}$, $P_5^{\mathrm{rel}}$, $P_4$, the boundary collinearity note on $\rho=1$, and the diagonal points $D_0,D_1,D_2$. |
| [`31012_core_graph_two_variable_relaxation.md`](31012_core_graph_two_variable_relaxation.md) | Proven | Proves the strict fixed-line monotonicity certificate, relaxed-P containment reduction, diagonal monotonicity reduction, and two-variable dependence. |
| [`31013_core_surface_definition.md`](31013_core_surface_definition.md) | Definition | Defines the side-length surface $F_6(a,b)$ and selected-point surfaces. |
| [`31015_minimum_curve_limit_figures.md`](31015_minimum_curve_limit_figures.md) | Empirical | Records the toward-limit figure sequence and the observed stable support pattern involving $D_0,D_2,P_4,P_5$. |
| [`31016_fixed_angle_g_strategy.md`](31016_fixed_angle_g_strategy.md) | Strategy | Defines the fixed-angle function $G_E(a,b,\theta)$ and records the far-from-limit selected-subset angle split for the relaxed six-point route. |
| [`31017_ray_transition_curve_minimum_conjecture.md`](31017_ray_transition_curve_minimum_conjecture.md) | Lemma target | Defines the ideal minimum relation and records algebraic transition-curve targets, including constant-difference, ray, local-metric, quadratic, product, and sum slices. |
| [`31018_ray_transition_computation_memo.md`](31018_ray_transition_computation_memo.md) | Experiment | Records numerical tests for the algebraic slice families, including fixed-angle failures and optimized-slice success/failure evidence. |
| [`31019_constant_difference_slice_minimum_target.md`](31019_constant_difference_slice_minimum_target.md) | Lemma target | Records the primary constant-$d=q-p$ optimized slice theorem target, exact $T=0$ formula, support-tie reduction, and partial cusp analysis. |
| [`31020_slice_family_status_catalog.md`](31020_slice_family_status_catalog.md) | Experiment | Concise success/failure catalog for the tested algebraic slice families and the recommended proof direction. |
