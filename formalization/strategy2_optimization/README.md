# Strategy 2 scalar-calculation statement project

This directory is a deliberately limited Lean 4 project. It records and
typechecks only the real-variable statements for the long,
calculation-heavy parts of Strategy 2. It does **not** formalize the
geometry-to-parameter bridge, the equivalence between the displayed paper
cells and the collapsed piecewise APIs below, the global case routing, or any
covering argument. It also does not prove the scalar inequalities: every
theorem currently ends with an intentional `sorry`.

The project includes:

- S2-E1 and S2-E2 endpoint inequalities;
- S2-R1 and S2-R2 return-slack inequalities;
- the S2-T3 endpoint inequality through collapsed piecewise residual and
  hit/miss functions;
- the two S2-SC adjacent-support problems;
- adjacent and nonadjacent S2-VD radial inequalities.

The environment is pinned to Lean 4.32.2 and Mathlib commit
`905b95818eb32af7874a58b427f50c1711a5e96c`. CI runs `lake build` so that
the definitions, domains, and theorem statements are reproducibly parsed and
elaborated despite the intentional `sorry` placeholders. A successful build
is therefore a **statement-elaboration check**, not a proof certificate.

The geometric dictionary remains in
`arrange/paper_draft/04d_strategy2_parameter_bridges.tex`. The Vd1--
supercritical two-chart replacement is excluded because it is a geometric
reduction rather than a scalar optimization problem.

The repository specification synchronized to the Lean T3 shell is the
five-variable compact projection
`prob:s2-t3-compact-projection` in
`arrange/paper_draft/04_strategy2_optimization_t3.tex`. The preceding
nine-variable finite-cell union is separately locked as a paper-side
specification; this project does not assert an equivalence between the two.


## Canonical notation interface

The Lean source follows the paper's public symbols through semantic ASCII
identifiers:

- on the high-radial theorem domains used here, `forwardCap c a` formalizes
  $\overline M_c(a)$; it is only a branch-totalized helper outside those domains;
- on those same high-radial theorem domains, `propagate c a` formalizes
  $\Phi_c(a)$; it is likewise totalized outside them;
- `strictSupercriticalForwardSupremum c` formalizes $M_c^{\rm sup}$;
- `SignedCenterInput.alpha` and `.delta` formalize the signed C-triangle
  slacks $\alpha$ and $\delta$;
- `centerRadical`, `centerEta`, `centerP`, and `centerK` formalize
  $E$, $\eta$, $P$, and $k$;
- `rightSurplus` and `leftSurplus` formalize $\Delta_R$ and $\Delta_L$;
- `qMinus c a` and `qPlus c a` use the implementation order `(c,a)` but
  correspond to the public paper notation $Q_-(a,c)$ and $Q_+(a,c)$;
- `forwardCapBranch c a` classifies every input into the constructors `lin`,
  `const`, `qMinus`, and `qPlus`, and `forwardCap` evaluates that selected
  constructor;
- `VdPosition` enumerates the three nonadjacent indices `pos2`, `pos3`, and
  `pos4`, which are consumed by `vdNonCenterExit`.

The T3 residual and radial subcells are intentionally collapsed into total
piecewise functions because cells with the same output formula do not need
distinct scalar objectives. The Lean file does not contain an equivalence
proof between those functions and the paper's full finite-cell inventory.
Likewise, `VdPosition` records the three index values but not the paper's
separate minimum-order cells. Any statement that those enumerations are
complete remains a paper-side obligation.

The theorem identifiers `problemS2...` remain stable statement-verification
keys. They must not be cited as formal proofs while their bodies are `sorry`.
