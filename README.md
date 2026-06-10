# Hexagon Covering Proof Corpus

The `proof/` folder is the self-contained Markdown research corpus for the
problem of covering a regular hexagon by seven open unit equilateral triangles.
It contains definitions, proof-tree branches, local lemmas, computations,
experiments, empirical notes, and failed approaches.

These notes are not a single finished proof of the main theorem. Each file
carries its own status label, and only files marked as proven should be cited
as established results.

## Main Target

The central theorem target is:

$$
\boxed{\text{The regular hexagon }H\text{ of side length }1\text{ cannot be covered by seven open unit equilateral triangles.}}
$$

The equivalent expanded closed-triangle formulation is:

$$
\boxed{\text{For every }L>1,\ H_L\text{ cannot be covered by seven closed unit equilateral triangles.}}
$$

The open/closed/scaled equivalence is recorded in
[`proof/100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`](proof/100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md).

## Start Here

Recommended reading order:

1. [`proof/000_main_theorem.md`](proof/000_main_theorem.md)
2. [`proof/001_proof_tree_index.md`](proof/001_proof_tree_index.md)
3. [`proof/010_setup/010_open_closed_equivalence.md`](proof/010_setup/010_open_closed_equivalence.md)
4. [`proof/100_Nplus0/100_index.md`](proof/100_Nplus0/100_index.md)
5. [`proof/200_Nplus1/200_index.md`](proof/200_Nplus1/200_index.md)
6. [`proof/300_Nplus_ge2/300_index.md`](proof/300_Nplus_ge2/300_index.md)
7. [`proof/002_status_and_dependencies.md`](proof/002_status_and_dependencies.md)

The legacy object-centered notes are still inside `proof/` as local source
packages, for example `proof/100_foundations/`, `proof/300_vertex_triangle/`,
and `proof/600_case_strategies/`. They are retained to preserve the file-level
proof statuses and detailed arguments while the proof-tree files provide the
paper-style navigation layer.

## Repository Layout

- [`proof/010_setup/`](proof/010_setup): setup bridge files for the proof tree.
- [`proof/100_Nplus0/`](proof/100_Nplus0): no-supercritical-row branch.
- [`proof/200_Nplus1/`](proof/200_Nplus1): exactly-one-supercritical-row branch.
- [`proof/300_Nplus_ge2/`](proof/300_Nplus_ge2): at-least-two-supercritical-row branch.
- [`proof/400_local_lemmas/`](proof/400_local_lemmas): local lemma targets used by the proof tree.
- [`proof/500_finite_point_algorithms/`](proof/500_finite_point_algorithms): finite-point algorithm routes.
- [`proof/900_failed_and_empirical/`](proof/900_failed_and_empirical): failed and empirical route index.

The complete proof file list is in [`proof/MANIFEST.txt`](proof/MANIFEST.txt).

## Skeleton Counterexample Warning

The May 24, 2026 imported counterexample numerically verifies seven closed
equilateral triangles of side strictly less than $1$ covering the full skeleton
$S$. See
[`proof/800_computation/811_skeleton_cover_counterexample.md`](proof/800_computation/811_skeleton_cover_counterexample.md).

Consequently, noncoverage of $S$ is no longer a viable standalone route to the
main theorem. Conditional half-skeleton results keep their stated status unless
the counterexample is separately shown to satisfy their hypotheses.

## Current Proof Package

The most developed recorded case is:

$$
\mathrm{CE0}+\text{at least one Vd1 or Vd2}.
$$

It is recorded as a proven half-skeleton obstruction across:

- [`proof/600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md`](proof/600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md)
- [`proof/600_case_strategies/602_CE0_Vd1_Vd2_rhombus_geometry.md`](proof/600_case_strategies/602_CE0_Vd1_Vd2_rhombus_geometry.md)
- [`proof/600_case_strategies/603_CE0_Vd1_Vd2_frontier_perturbation.md`](proof/600_case_strategies/603_CE0_Vd1_Vd2_frontier_perturbation.md)
- [`proof/600_case_strategies/604_CE0_Vd1_Vd2_F_chain_inequalities.md`](proof/600_case_strategies/604_CE0_Vd1_Vd2_F_chain_inequalities.md)
- [`proof/600_case_strategies/605_CE0_Vd1_Vd2_midpoint_hole_subcases.md`](proof/600_case_strategies/605_CE0_Vd1_Vd2_midpoint_hole_subcases.md)
- [`proof/600_case_strategies/606_CE0_Vd1_Vd2_assembly.md`](proof/600_case_strategies/606_CE0_Vd1_Vd2_assembly.md)

Other major cases are still strategy- or target-lemma-dependent; see
[`proof/001_proof_tree_index.md`](proof/001_proof_tree_index.md).

## Status Labels

Status labels are defined in
[`proof/100_foundations/106_proof_status_conventions.md`](proof/100_foundations/106_proof_status_conventions.md).

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
- Write display-LaTeX blocks with `$$` on separate delimiter lines, and keep
  the equation content between them on one physical line. Multi-line equation
  content inside a `$$` block can fail to render.
- Do not cite a claim as proven unless its source file has a proven status label.
- Preserve failed approaches with enough detail to avoid repeating them.
- Use [`proof/appendices/B_notation_dictionary.md`](proof/appendices/B_notation_dictionary.md) when introducing or checking notation.
