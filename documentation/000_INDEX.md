# Hexagon Covering Notes, 2026-05-08

Status: Navigation

These notes organize definitions, proof strategies, local lemmas, computations, and failed approaches for the problem of covering a regular hexagon by seven open unit equilateral triangles.

## Main theorem target

$$
\boxed{\text{The regular hexagon }H\text{ of side length }1\text{ cannot be covered by seven open unit equilateral triangles.}}
$$

The equivalent expanded closed-triangle formulation is:

$$
\boxed{\text{For every }L>1,\ H_L\text{ cannot be covered by seven closed unit equilateral triangles.}}
$$

The equivalence is proved in `100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`.

## Reading order

1. `100_foundations/100_problem_statement.md`
2. `100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`
3. `200_center_triangle/200_C_triangle_overview.md`
4. `300_vertex_triangle/300_V_triangle_overview.md`
5. `400_global_propagation/403_six_step_composition.md`
6. `500_half_skeleton_lemmas/500_half_skeleton_lemma_index.md`
7. `550_CE_Vd0_boundary_loss/550_index.md`
8. `600_case_strategies/600_case_strategy_index.md`
9. `900_failed_ideas/900_failed_idea_index.md`

## Most important current proof package

The case

$$
\mathrm{CE0}+\text{at least one Vd1 or Vd2}
$$

is recorded as proven for the half-skeleton target in:

- `600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md`
- `600_case_strategies/602_CE0_Vd1_Vd2_rhombus_geometry.md`
- `600_case_strategies/603_CE0_Vd1_Vd2_frontier_perturbation.md`
- `600_case_strategies/604_CE0_Vd1_Vd2_F_chain_inequalities.md`
- `600_case_strategies/605_CE0_Vd1_Vd2_midpoint_hole_subcases.md`
- `600_case_strategies/606_CE0_Vd1_Vd2_assembly.md`

## Active CE1/CE2 Vd0 boundary-loss package

The branch package for the CE1/CE2 all-Vd0 boundary-loss obstruction is recorded in:

- `550_CE_Vd0_boundary_loss/550_index.md`

It is not a finished proof of the full CE1/CE2 Vd0 case.  It contains a reduction, corrected admissible-map definitions, several proven branch lemmas, computational verification notes, and remaining lower-sheet $T_+$ obligations.

## Proof-status labels

See `100_foundations/106_proof_status_conventions.md`.
