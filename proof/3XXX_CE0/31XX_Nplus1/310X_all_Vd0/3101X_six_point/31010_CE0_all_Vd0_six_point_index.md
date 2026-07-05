# CE0 All-Vd0 Six-Point Strategy

Status: Strategy

This package records the six-point core construction and the associated
two-variable graph definitions for the CE0, $N_+=1$, all-Vd0 branch.

These files define the construction and visualization target.  They do not
prove that the branch is closed, and numerical or plotted behavior remains
empirical unless a rigorous certificate is later recorded.

The construction was transcribed from `dylan0301/hexagon-cover-visual` branch
`gulgu`, with the two-line $AB$-superset variant checked against commit
`6dacaa72047d67a5d7c3e5fbc4bccb26c3e72732`.  The definitions below are
written self-contained in this package.

## Files

| File | Recorded status | Notes |
|---|---|---|
| [`31011_six_point_construction.md`](31011_six_point_construction.md) | Definition | Defines the two-line $AB$-superset variant and the points $P_3,P_4,P_5,D_0,D_1,D_2$, including the point-on-edge fallbacks for $P_3$ and $P_5$. |
| [`31012_core_graph_two_variable_relaxation.md`](31012_core_graph_two_variable_relaxation.md) | Lemma target | Targets the conditional two-line red-region containment and two-variable dependence of the six selected points. |
| [`31013_core_surface_definition.md`](31013_core_surface_definition.md) | Definition | Defines the side-length surface $F_6(a,b)$ and selected-point surfaces. |
| [`31014_minimum_curve_definition.md`](31014_minimum_curve_definition.md) | Definition | Defines the ideal minimum relation and the sampled pink curve drawn by the app. |
| [`31015_minimum_curve_limit_figures.md`](31015_minimum_curve_limit_figures.md) | Empirical | Records the toward-limit figure sequence and the observed stable support pattern involving $D_0,D_2,P_4,P_5$. |
