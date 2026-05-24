# Hexagon Covering Database

The `documentation/` folder is a structured database of Markdown research notes about the problem of covering a regular hexagon by seven open unit equilateral triangles. It collects definitions, local lemmas, case strategies, computational experiments, and failed approaches.

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

The open/closed/scaled equivalence is recorded in [`documentation/100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`](documentation/100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md).

## Start Here

Recommended reading order:

1. [`documentation/100_foundations/100_problem_statement.md`](documentation/100_foundations/100_problem_statement.md)
2. [`documentation/100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`](documentation/100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md)
3. [`documentation/200_center_triangle/200_C_triangle_overview.md`](documentation/200_center_triangle/200_C_triangle_overview.md)
4. [`documentation/300_vertex_triangle/300_V_triangle_overview.md`](documentation/300_vertex_triangle/300_V_triangle_overview.md)
5. [`documentation/400_global_propagation/403_six_step_composition.md`](documentation/400_global_propagation/403_six_step_composition.md)
6. [`documentation/500_half_skeleton_lemmas/500_half_skeleton_lemma_index.md`](documentation/500_half_skeleton_lemmas/500_half_skeleton_lemma_index.md)
7. [`documentation/600_case_strategies/600_case_strategy_index.md`](documentation/600_case_strategies/600_case_strategy_index.md)
8. [`documentation/900_failed_ideas/900_failed_idea_index.md`](documentation/900_failed_ideas/900_failed_idea_index.md)

The navigation entry point is [`documentation/000_INDEX.md`](documentation/000_INDEX.md). The future-work hygiene note is [`documentation/001_README_FOR_FUTURE_WORK.md`](documentation/001_README_FOR_FUTURE_WORK.md).

## Repository Layout

- [`documentation/100_foundations/`](documentation/100_foundations): problem statement, geometry objects, target sets, open/closed equivalence, symmetry, and proof-status conventions.
- [`documentation/200_center_triangle/`](documentation/200_center_triangle): center-triangle classifications, inner gamma models, cone types, parameterizations, and midpoint attempts.
- [`documentation/300_vertex_triangle/`](documentation/300_vertex_triangle): vertex-triangle types, local coordinates, admissible sets, midpoint subsets, and boundary degeneracies.
- [`documentation/400_global_propagation/`](documentation/400_global_propagation): propagation maps, cyclic contradiction templates, and global inequality structure.
- [`documentation/500_half_skeleton_lemmas/`](documentation/500_half_skeleton_lemmas): local half-skeleton lemmas and missing proof obligations.
- [`documentation/600_case_strategies/`](documentation/600_case_strategies): active case strategies, including the CE0 + Vd1/Vd2 proof package.
- [`documentation/700_equations_and_inequalities/`](documentation/700_equations_and_inequalities): equation inventory, type equations, kite inequality, gamma constraints, and symbolic targets.
- [`documentation/800_computation/`](documentation/800_computation): computational experiment plans, sampling notes, finite-target searches, and certificate formats.
- [`documentation/900_failed_ideas/`](documentation/900_failed_ideas): postmortems for approaches that are known to be insufficient.
- [`documentation/950_implementation_notes/`](documentation/950_implementation_notes): notes for future implementation helpers and repository policy.
- [`documentation/appendices/`](documentation/appendices): glossary, notation dictionary, claim table, case tree, open questions, and reading order.

The complete documentation file list is in [`documentation/MANIFEST.txt`](documentation/MANIFEST.txt).

## Skeleton Counterexample Warning

The May 24, 2026 imported counterexample numerically verifies seven closed
equilateral triangles of side strictly less than $1$ covering the full skeleton
$S$. See
[`documentation/800_computation/811_skeleton_cover_counterexample.md`](documentation/800_computation/811_skeleton_cover_counterexample.md).

Consequently, noncoverage of $S$ is no longer a viable standalone route to the
main theorem. Conditional half-skeleton results keep their stated status unless
the counterexample is separately shown to satisfy their hypotheses.

## Current Proof Package

The most developed recorded case is:

$$
\mathrm{CE0}+\text{at least one Vd1 or Vd2}.
$$

It is recorded as a proven half-skeleton obstruction across:

- [`documentation/600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md`](documentation/600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md)
- [`documentation/600_case_strategies/602_CE0_Vd1_Vd2_rhombus_geometry.md`](documentation/600_case_strategies/602_CE0_Vd1_Vd2_rhombus_geometry.md)
- [`documentation/600_case_strategies/603_CE0_Vd1_Vd2_frontier_perturbation.md`](documentation/600_case_strategies/603_CE0_Vd1_Vd2_frontier_perturbation.md)
- [`documentation/600_case_strategies/604_CE0_Vd1_Vd2_F_chain_inequalities.md`](documentation/600_case_strategies/604_CE0_Vd1_Vd2_F_chain_inequalities.md)
- [`documentation/600_case_strategies/605_CE0_Vd1_Vd2_midpoint_hole_subcases.md`](documentation/600_case_strategies/605_CE0_Vd1_Vd2_midpoint_hole_subcases.md)
- [`documentation/600_case_strategies/606_CE0_Vd1_Vd2_assembly.md`](documentation/600_case_strategies/606_CE0_Vd1_Vd2_assembly.md)

Other major cases are still strategy- or target-lemma-dependent; see [`documentation/600_case_strategies/600_case_strategy_index.md`](documentation/600_case_strategies/600_case_strategy_index.md).

## Status Labels

Status labels are defined in [`documentation/100_foundations/106_proof_status_conventions.md`](documentation/100_foundations/106_proof_status_conventions.md).

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

- Keep research-note files Markdown-only unless the repository policy changes.
- Use `$...$` for inline LaTeX and `$$...$$` for display LaTeX.
- Do not cite a claim as proven unless its source file has a proven status label.
- Preserve failed approaches with enough detail to avoid repeating them.
- Use [`documentation/appendices/B_notation_dictionary.md`](documentation/appendices/B_notation_dictionary.md) when introducing or checking notation.
