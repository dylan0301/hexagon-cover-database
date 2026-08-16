# Strategy 2 optimization statement project

This directory is a deliberately limited Lean 4 project. It records and
typechecks only the real-variable Strategy 2 optimization problem statements.
It does **not** formalize the geometry-to-parameter bridge or prove the
optimization inequalities. Every theorem currently ends with `sorry`.

The project includes:

- S2-E1 and S2-E2 endpoint inequalities;
- S2-R1 and S2-R2 return-slack inequalities;
- the finite S2-T3 endpoint-cell problem;
- the two S2-SC adjacent-support problems;
- adjacent and nonadjacent S2-VD radial problems.

The environment is pinned to Lean 4.32.2 and Mathlib commit
`905b95818eb32af7874a58b427f50c1711a5e96c`. CI runs `lake build` so that
the definitions, domains, and theorem statements are reproducibly parsed and
elaborated despite the intentional `sorry` placeholders.

The geometric dictionary remains in
`arrange/paper_draft/04d_strategy2_parameter_bridges.tex`. The Vd1--
supercritical two-chart replacement is excluded because it is a geometric
reduction rather than a scalar optimization problem.


## Canonical notation interface

The Lean source follows the paper's public symbols through semantic ASCII
identifiers:

- `forwardCap c a` formalizes $\overline M_c(a)$;
- `propagate c a` formalizes $\Phi_c(a)$;
- `strictSupercriticalForwardSupremum c` formalizes $M_c^{\rm sup}$;
- `SignedCenterInput.alpha` and `.delta` formalize the signed C-triangle
  slacks $\alpha$ and $\delta$;
- `centerRadical`, `centerEta`, `centerP`, and `centerK` formalize
  $E$, $\eta$, $P$, and $k$;
- `rightSurplus` and `leftSurplus` formalize $\Delta_R$ and $\Delta_L$;
- `ForwardCapBranch` has the constructors `lin`, `const`, `qMinus`, and
  `qPlus`;
- `VdPosition` excludes invalid nonadjacent placements at the type level.

The theorem identifiers `problemS2...` remain stable verification keys.
