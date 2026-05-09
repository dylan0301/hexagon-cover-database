# Hexagon Covering Database

This repository is a structured database of Markdown research notes about the problem of covering a regular hexagon by seven open unit equilateral triangles. It collects definitions, local lemmas, case strategies, computational experiments, and failed approaches.

These notes are not a single finished proof of the main theorem. Each file carries its own status label, and only files marked as proven should be cited as established results.

## Main Target

The central theorem target is:

$$
\boxed{\text{The regular hexagon }H\text{ of side length }1\text{ cannot be covered by seven open unit equilateral triangles.}}
$$

The main equivalent closed-triangle formulation is:

$$
\boxed{\text{For every }L>1,\ H_L\text{ cannot be covered by seven closed unit equilateral triangles.}}
$$

The open/closed/scaled equivalence is recorded in [`100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`](100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md).

## Start Here

Recommended reading order:

1. [`100_foundations/100_problem_statement.md`](100_foundations/100_problem_statement.md)
2. [`100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`](100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md)
3. [`200_center_triangle/200_C_triangle_overview.md`](200_center_triangle/200_C_triangle_overview.md)
4. [`300_vertex_triangle/300_V_triangle_overview.md`](300_vertex_triangle/300_V_triangle_overview.md)
5. [`400_global_propagation/403_six_step_composition.md`](400_global_propagation/403_six_step_composition.md)
6. [`500_half_skeleton_lemmas/500_half_skeleton_lemma_index.md`](500_half_skeleton_lemmas/500_half_skeleton_lemma_index.md)
7. [`600_case_strategies/600_case_strategy_index.md`](600_case_strategies/600_case_strategy_index.md)
8. [`900_failed_ideas/900_failed_idea_index.md`](900_failed_ideas/900_failed_idea_index.md)

The navigation entry point is [`000_INDEX.md`](000_INDEX.md). The future-work hygiene note is [`001_README_FOR_FUTURE_WORK.md`](001_README_FOR_FUTURE_WORK.md).

## Repository Layout

- [`100_foundations/`](100_foundations): problem statement, geometry objects, target sets, open/closed equivalence, symmetry, and proof-status conventions.
- [`200_center_triangle/`](200_center_triangle): center-triangle classifications, inner gamma models, cone types, parameterizations, and midpoint attempts.
- [`300_vertex_triangle/`](300_vertex_triangle): vertex-triangle types, local coordinates, admissible sets, midpoint subsets, and boundary degeneracies.
- [`400_global_propagation/`](400_global_propagation): propagation maps, cyclic contradiction templates, and global inequality structure.
- [`500_half_skeleton_lemmas/`](500_half_skeleton_lemmas): local half-skeleton lemmas and missing proof obligations.
- [`600_case_strategies/`](600_case_strategies): active case strategies, including the CE0 + Vd1/Vd2 proof package.
- [`700_equations_and_inequalities/`](700_equations_and_inequalities): equation inventory, type equations, kite inequality, gamma constraints, and symbolic targets.
- [`800_computation/`](800_computation): computational experiment plans, sampling notes, finite-target searches, and certificate formats.
- [`900_failed_ideas/`](900_failed_ideas): postmortems for approaches that are known to be insufficient.
- [`950_implementation_notes/`](950_implementation_notes): notes for future implementation helpers and repository policy.
- [`appendices/`](appendices): glossary, notation dictionary, claim table, case tree, open questions, and reading order.

The complete file list is in [`MANIFEST.txt`](MANIFEST.txt).

## Current Proof Package

The most developed recorded case is:

$$
\mathrm{CE0}+\text{at least one Vd1 or Vd2}.
$$

It is recorded as a proven half-skeleton obstruction across:

- [`600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md`](600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md)
- [`600_case_strategies/602_CE0_Vd1_Vd2_rhombus_geometry.md`](600_case_strategies/602_CE0_Vd1_Vd2_rhombus_geometry.md)
- [`600_case_strategies/603_CE0_Vd1_Vd2_frontier_perturbation.md`](600_case_strategies/603_CE0_Vd1_Vd2_frontier_perturbation.md)
- [`600_case_strategies/604_CE0_Vd1_Vd2_F_chain_inequalities.md`](600_case_strategies/604_CE0_Vd1_Vd2_F_chain_inequalities.md)
- [`600_case_strategies/605_CE0_Vd1_Vd2_midpoint_hole_subcases.md`](600_case_strategies/605_CE0_Vd1_Vd2_midpoint_hole_subcases.md)
- [`600_case_strategies/606_CE0_Vd1_Vd2_assembly.md`](600_case_strategies/606_CE0_Vd1_Vd2_assembly.md)

Other major cases are still strategy- or target-lemma-dependent; see [`600_case_strategies/600_case_strategy_index.md`](600_case_strategies/600_case_strategy_index.md).

## Status Labels

Status labels are defined in [`100_foundations/106_proof_status_conventions.md`](100_foundations/106_proof_status_conventions.md).

Important labels:

- `Definition`: exact convention or mathematical definition.
- `Proven`: complete proof in the file or explicitly referenced files.
- `Proven local lemma`: complete local proof used as a component.
- `Proven analytic inequality`: complete inequality proof.
- `Lemma target`: useful statement whose proof is not complete here.
- `Strategy`: active proof direction.
- `Empirical`: supported by computation or plotting only.
- `Failed`: known insufficient or abandoned approach.
- `Implementation note`: source-code or UI-facing note.
- `Reference`: dictionary, inventory, or index.

Numerical optimization claims remain `Empirical` until a certificate is supplied.

## Working Conventions

- Keep files Markdown-only unless the repository policy changes.
- Use `$...$` for inline LaTeX and `$$...$$` for display LaTeX.
- Do not cite a claim as proven unless its source file has a proven status label.
- Preserve failed approaches with enough detail to avoid repeating them.
- Use [`appendices/B_notation_dictionary.md`](appendices/B_notation_dictionary.md) when introducing or checking notation.
