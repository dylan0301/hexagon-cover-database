# Strategy 2 optimization problem shell

This folder is not a full formalization of the hexagon-cover proof.

`Strategy2OptimizationProblems.lean` records only the real-variable Strategy 2
optimization problems:

- S2-E1 and S2-E2 endpoint inequalities;
- S2-R1 and S2-R2 returned-demand inequalities;
- S2-T3 finite endpoint-cell inequality;
- S2-SC rescuer inequalities;
- S2-VD adjacent and nonadjacent radial inequalities.

Every theorem ends with `sorry`.  The geometry-to-parameter bridge remains in
the paper appendix `04d_strategy2_parameter_bridges.tex`.  The two-chart Vd1
replacement is deliberately excluded because it is a geometric reduction, not
a scalar optimization problem.

No Lean build is asserted by this revision.
