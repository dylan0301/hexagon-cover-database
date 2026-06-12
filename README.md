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
[`proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md`](proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md).

## Start Here

Recommended reading order:

1. [`proof/0XXX_main/0000_main_theorem.md`](proof/0XXX_main/0000_main_theorem.md)
2. [`proof/0XXX_main/0001_proof_tree_index.md`](proof/0XXX_main/0001_proof_tree_index.md)
3. [`proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md`](proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md)
4. [`proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md`](proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md)
5. [`proof/1XXX_foundations/12XX_V_triangle/1212_vertex_rows_and_Nplus.md`](proof/1XXX_foundations/12XX_V_triangle/1212_vertex_rows_and_Nplus.md)
6. [`proof/3XXX_CE0/3000_CE0_index.md`](proof/3XXX_CE0/3000_CE0_index.md)
7. [`proof/4XXX_CE1/4000_CE1_index.md`](proof/4XXX_CE1/4000_CE1_index.md)
8. [`proof/5XXX_CE2/5000_CE2_index.md`](proof/5XXX_CE2/5000_CE2_index.md)
9. [`proof/0XXX_main/0002_status_and_dependencies.md`](proof/0XXX_main/0002_status_and_dependencies.md)

The corpus uses four-character folder range labels with literal `X` digits.
Definitions live in
`proof/1XXX_foundations/`, reusable geometric lemmas in
`proof/2XXX_geometric_lemmas/`, and the proof tree splits first into CE0,
CE1, and CE2 branches.

## Repository Layout

- [`proof/0XXX_main/`](proof/0XXX_main): main theorem, proof-tree index, status table, and manifest.
- [`proof/09XX_appendices/`](proof/09XX_appendices): glossary, notation, open questions, and archived sketches.
- [`proof/1XXX_foundations/`](proof/1XXX_foundations): definitions and conventions.
- [`proof/2XXX_geometric_lemmas/`](proof/2XXX_geometric_lemmas): reusable geometric lemmas and targets.
- [`proof/3XXX_CE0/`](proof/3XXX_CE0): CE0 proof-tree branch.
- [`proof/4XXX_CE1/`](proof/4XXX_CE1): CE1 proof-tree branch.
- [`proof/5XXX_CE2/`](proof/5XXX_CE2): CE2 proof-tree branch.
- [`proof/9XXX_failed_ideas/`](proof/9XXX_failed_ideas): failed routes, empirical warnings, and counterexamples.

The complete proof file list is in [`proof/0XXX_main/0004_manifest.txt`](proof/0XXX_main/0004_manifest.txt).

## Skeleton Counterexample Warning

The May 24, 2026 imported counterexample numerically verifies seven closed
equilateral triangles of side strictly less than $1$ covering the full skeleton
$S$. See
[`proof/9XXX_failed_ideas/908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md`](proof/9XXX_failed_ideas/908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md).

Consequently, noncoverage of $S$ is no longer a viable standalone route to the
main theorem. Conditional half-skeleton results keep their stated status unless
the counterexample is separately shown to satisfy their hypotheses.

## Current Proof Package

The most developed recorded case is:

$$
\mathrm{CE0}+\text{at least one Vd1 or Vd2}.
$$

It is recorded as a proven half-skeleton obstruction across:

- [`proof/3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3111_CE0_Vd1_Vd2_half_skeleton_theorem.md`](proof/3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3111_CE0_Vd1_Vd2_half_skeleton_theorem.md)
- [`proof/3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3112_CE0_Vd1_Vd2_rhombus_geometry.md`](proof/3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3112_CE0_Vd1_Vd2_rhombus_geometry.md)
- [`proof/3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3113_CE0_Vd1_Vd2_frontier_perturbation.md`](proof/3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3113_CE0_Vd1_Vd2_frontier_perturbation.md)
- [`proof/3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3114_CE0_Vd1_Vd2_F_chain_inequalities.md`](proof/3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3114_CE0_Vd1_Vd2_F_chain_inequalities.md)
- [`proof/3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3115_CE0_Vd1_Vd2_midpoint_hole_subcases.md`](proof/3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3115_CE0_Vd1_Vd2_midpoint_hole_subcases.md)
- [`proof/3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3116_CE0_Vd1_Vd2_assembly.md`](proof/3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3116_CE0_Vd1_Vd2_assembly.md)

Other major cases are still strategy- or target-lemma-dependent; see
[`proof/0XXX_main/0001_proof_tree_index.md`](proof/0XXX_main/0001_proof_tree_index.md).

## Status Labels

Status labels are defined in
[`proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md`](proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md).

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
- Write cardinalities in math as
  `\left\lvert \left\lbrace\, ... \,\right\rbrace \right\rvert`;
  do not use hash-based notation for cardinality.
- Use `\mathrm{...}` for named operators in math; do not use the
  operatorname macro.
- Put conditions for `\sup`, `\inf`, `\min`, and `\max` in subscripts, using
  `\substack{...}` when multiple lines are needed. Do not put alignment
  markers inside operator arguments.
- Write display-LaTeX blocks with `$$` on separate delimiter lines, and keep
  the equation content between them on one physical line. Multi-line equation
  content inside a `$$` block can fail to render.
- Do not cite a claim as proven unless its source file has a proven status label.
- Preserve failed approaches with enough detail to avoid repeating them.
- Use [`proof/09XX_appendices/0910_notation_dictionary.md`](proof/09XX_appendices/0910_notation_dictionary.md) when introducing or checking notation.
