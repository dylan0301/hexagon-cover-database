# CE0 All-Vd0 Residual-Core Closure

Status: Proven

This note closes the CE0, $N_+=1$, all-Vd0 branch as a direct corollary of
the center-independent theorem
[`31035_center_independent_all_boundary_obstruction.md`](31035_center_independent_all_boundary_obstruction.md).

## Corollary

There is no cover of $H$ by seven open unit equilateral triangles for which

- the center role $T_C$ is CE0;
- all six vertex roles $T_0,\dots,T_5$ are Vd0; and
- exactly one actual maximal boundary row is supercritical.

## Proof

Assume such a cover exists. We first show that the six vertex roles cover
$\partial H$.

If some $P\in\partial H$ belonged to none of them, the cover would force
$P\in T_C$. Since $T_C$ is open, it would contain a plane ball about $P$.
On an edge interior this ball contains a positive-length boundary interval;
at a vertex it contains such an interval on each incident edge. In either
case $T_C$ meets a boundary edge of $H$ in positive length, contradicting
the definition of CE0 in
[`1101_CE_classification.md`](../../../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md).
Hence

$$
\partial H\subseteq\bigcup_{i=0}^5T_i.
$$

The six vertex roles are Vd0 by assumption, and $N_+=1$ says that exactly
one of their actual rows is supercritical; see
[`1212_vertex_rows_and_Nplus.md`](../../../../1XXX_foundations/12XX_V_triangle/1212_vertex_rows_and_Nplus.md).
All hypotheses of `31035` now hold, so that theorem gives a contradiction.
Therefore this branch is impossible.

The CE0 assumption is used only to obtain full vertex-role boundary
coverage. After that point, the argument is center-class independent.

## Proven dependencies

- `31035` reduces the cover to the residual-core witness.
- [`31032`](31032_symmetric_witness_construction.md) and
  [`31033`](31033_asymmetric_witness_construction.md) construct that witness.
- [`31034`](31034_witness_enclosure_inequality.md) gives the terminal cap
  reduction and analytic adjacent overlaps.
- [`31037`](31037_rational_cmax_upper_envelope.md) proves both remaining mixed
  overlaps by exact rational algebra and integer Bernstein coefficients, with
  no interval arithmetic.

The original research blueprint remains, for provenance only, in
[`31031_original_residual_core_draft.md`](31031_original_residual_core_draft.md).
