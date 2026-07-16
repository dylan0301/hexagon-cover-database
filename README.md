# Hexagon Covering Proof Corpus

The `proof/` folder is the self-contained research corpus for the problem of
covering a regular hexagon by seven open unit equilateral triangles. It
contains definitions, proof-tree branches, local lemmas, computations,
experiments, empirical notes, and failed approaches.

The main theorem is proved in
[`proof/0XXX_main/0000_main_theorem.md`](proof/0XXX_main/0000_main_theorem.md),
which assembles the exhaustive CE and $N_+$ branches from their numbered
terminal sources. The corpus also retains unfinished alternative strategies,
empirical notes, and failed approaches; their local status labels remain
authoritative and they are not dependencies of the proved assembly.

## Main Theorem

The proved theorem is:

$$
\boxed{\text{The regular hexagon }H\text{ of side length }1\text{ cannot be covered by seven open unit equilateral triangles.}}
$$

The equivalent expanded closed-triangle formulation is:

$$
\boxed{\text{For every }L>1,\ H_L\text{ cannot be covered by seven closed unit equilateral triangles.}}
$$

The open/closed/scaled equivalence is recorded in
[`proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md`](proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md).
The complete case assembly is recorded in
[`proof/0XXX_main/0000_main_theorem.md`](proof/0XXX_main/0000_main_theorem.md).

## Start Here

Recommended reading order for mathematical orientation:

1. [`proof/0XXX_main/0000_main_theorem.md`](proof/0XXX_main/0000_main_theorem.md)
2. [`proof/0XXX_main/0001_proof_tree_index.md`](proof/0XXX_main/0001_proof_tree_index.md)
3. [`proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md`](proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md)
4. [`proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md`](proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md)
5. [`proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md)
6. [`proof/1XXX_foundations/12XX_V_triangle/1212_vertex_rows_and_Nplus.md`](proof/1XXX_foundations/12XX_V_triangle/1212_vertex_rows_and_Nplus.md)
7. [`proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md`](proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
8. [`proof/3XXX_CE0/3000_CE0_index.md`](proof/3XXX_CE0/3000_CE0_index.md)
9. [`proof/4XXX_CE1CE2/4000_CE1CE2_index.md`](proof/4XXX_CE1CE2/4000_CE1CE2_index.md)
10. [`proof/0XXX_main/0002_status_and_dependencies.md`](proof/0XXX_main/0002_status_and_dependencies.md)

The corpus uses four-character folder range labels with literal `X` digits.
Definitions live in
`proof/1XXX_foundations/`, reusable geometric lemmas in
`proof/2XXX_geometric_lemmas/`, and the proof tree splits first into the CE0
branch and the combined CE1/CE2 branch.

## Proof Corpus Map

- [`proof/0XXX_main/`](proof/0XXX_main): main theorem, proof-tree index, and status table.
- [`proof/09XX_appendices/`](proof/09XX_appendices): glossary, notation, open questions, and archived sketches.
- [`proof/1XXX_foundations/`](proof/1XXX_foundations): definitions and conventions.
- [`proof/2XXX_geometric_lemmas/`](proof/2XXX_geometric_lemmas): reusable geometric lemmas and targets.
- [`proof/3XXX_CE0/`](proof/3XXX_CE0): CE0 proof-tree branch.
- [`proof/4XXX_CE1CE2/`](proof/4XXX_CE1CE2): combined CE1/CE2 proof-tree branch.
- [`proof/9XXX_failed_ideas/`](proof/9XXX_failed_ideas): failed routes, empirical warnings, and counterexamples.

The complete proof file list is in [`proof/MANIFEST.txt`](proof/MANIFEST.txt).

## Skeleton Counterexample Warning

The May 24, 2026 imported counterexample numerically verifies seven closed
equilateral triangles of side strictly less than $1$ covering the full skeleton
$S$. See
[`proof/9XXX_failed_ideas/908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md`](proof/9XXX_failed_ideas/908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md).

Consequently, noncoverage of $S$ is no longer a viable standalone route to the
main theorem. Conditional half-skeleton results keep their stated status unless
the counterexample is separately shown to satisfy their hypotheses.

## Status Labels

Status labels are defined in
[`proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md`](proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md).
For reading and citation, the main rule is: use a result as established only
when its source file says `Status: Proven`.

Files marked `Reduction`, `Practically proven`, `Lemma target`, `Strategy`,
`Empirical`, `Experiment`, `Failed`, or `Reference` are part of the working
corpus, but they are not complete terminal proofs unless every named
dependency has a proven source. Numerical optimization, plotting, or search
evidence remains empirical unless a rigorous certificate is recorded.
