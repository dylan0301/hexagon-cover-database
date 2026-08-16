# Hexagon Covering Proof Corpus

The `proof/` folder is the self-contained research corpus for the problem of
covering a regular hexagon by seven open unit equilateral triangles. It
contains definitions, proof-tree branches, local lemmas, computations,
experiments, empirical notes, and failed approaches.

The main theorem is proved in
[`proof/0XXX_main/0000_main_theorem.md`](proof/0XXX_main/0000_main_theorem.md),
which assembles the exhaustive CE and $N_+$ branches from their numbered
final sources. The corpus also retains unfinished alternative strategies,
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
6. [`proof/1XXX_foundations/12XX_V_triangle/1212_vertex_V_triangles_and_Nplus.md`](proof/1XXX_foundations/12XX_V_triangle/1212_vertex_V_triangles_and_Nplus.md)
7. [`proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md`](proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
8. [`proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
9. [`proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md)
10. [`proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201a_equilateral_enclosure_and_radical_calculus.md`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201a_equilateral_enclosure_and_radical_calculus.md)
11. [`proof/2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md`](proof/2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
12. [`proof/3XXX_CE0/3000_CE0_index.md`](proof/3XXX_CE0/3000_CE0_index.md)
13. [`proof/4XXX_CE1CE2/4000_CE1CE2_index.md`](proof/4XXX_CE1CE2/4000_CE1CE2_index.md)
14. [`proof/0XXX_main/0002_status_and_dependencies.md`](proof/0XXX_main/0002_status_and_dependencies.md)

The corpus uses four-character folder range labels with literal `X` digits.
Definitions live in `proof/1XXX_foundations/`, reusable geometric lemmas in
`proof/2XXX_geometric_lemmas/`, and the proof tree splits first into the CE0
branch and the combined CE1/CE2 branch.

## Unified Proof Architecture

The manuscript uses four geometric methods:

1. trace-length bounds on the perimeter or the full skeleton;
2. propagation of boundary-reach lower bounds;
3. normalized area-loss estimates;
4. an equilateral-enclosure obstruction for nine points forced into the
   center triangle.

For a vertex triangle, let $A,B,C$ be its maximal backward, forward, and
radial reaches. The local admissible set $\mathcal A$ determines

$$
M_c(a)=\max\{b:(a,b,c)\in\mathcal A\},
$$

the maximum possible forward reach when the backward and radial reaches are
at least $a$ and $c$. For a nonsupercritical triangle, define

$$
\overline M_c(a)=\min\{M_c(a),1-a\},
\qquad
\Phi_c(a)=1-\overline M_c(a).
$$

The midpoint theorem gives the exact branch split

$$
\overline M_c(a)=
\begin{cases}
1-a,&0\le c\le1/2,\\
M_c(a),&1/2<c\le1.
\end{cases}
$$

Hence a center-free edge propagates the next backward-reach lower bound
$A_{\mathrm{next}}\ge\Phi_c(a)$. If a center interval occurs on the edge, its
covered component is included before taking the uncovered suffix. The
strict-supercritical forward envelope is denoted $M_c^{\rm sup}$.

The exact calculation files retain the technical aliases

$$
g_c(x)=M_c(1-x),
\qquad
g_c^\vee(a)=1-M_c(a),
$$

and

$$
B_c(a)=M_c(a),
\qquad
F_c(a)=\overline M_c(a),
\qquad
G_c(a)=1-F_c(a).
$$

At zero radial lower bound, $g_0(x)>x$ for $0<x<1$. Therefore the low-radial
nonsupercritical step uses $B\le1-A$ directly rather than the raw technical
alias. The high-radial algebraic calculation has four formula branches: the
linear branch, the selected $Q_+$ branch, the constant branch, and the
selected $Q_-$ branch.

The reusable local sources are:

- [`2019`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md): center-assisted suffixes and the center-free boundary-path bound;
- [`201d`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md): technical $g$ aliases and relaxed composition;
- [`201a`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201a_equilateral_enclosure_and_radical_calculus.md): the enclosure gauge and universal equilateral radical;
- [`201b`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md): the global quarter radial envelope;
- [`201c`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md): the Vd corner radial inequalities;
- [`2110`](proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2110_common_CE2_two_gap_application.md): the common CE2 paired-endpoint application.

For the all-Vd0 CE1/CE2 cases, $N_+$ counts supercritical vertex triangles and
$N_{\rm gap}$ counts positive center traces containing a boundary gap. The two
$N_{\rm gap}=2$ cases use the same paired-endpoint inequality.

## Interactive Navigation

These standalone pages are `Reference` visual aids. They explain the geometry,
notation, and proof-certificate structure, but they are not themselves proof
certificates and do not establish or change proof status.

| Interactive page | Scope | Status |
|---|---|---|
| [`strategy2demo.html`](interactive/strategy2demo.html) | Combined Strategy 2 geometry and certificate-overlay explorer, covering the five proof families and their canonical $g$-transfer chains | Reference |
| [`strategy2notation.html`](interactive/strategy2notation.html) | Interactive Strategy 2 notation lab for the canonical triangle labeling, reaches, propagation functions, signed-center data, and case routing | Reference |
| [`strategy4demo.html`](interactive/strategy4demo.html) | Strategy 4 mechanism explorer for the direct nine-point obstruction | Reference |

### Preview in GitHub Codespaces

From the repository root, run:

```bash
python3 -m http.server 8000
```

In the Codespaces editor, open the **Ports** tab, find port `8000`, and select
**Open in Browser**. If the port does not appear automatically, use
**Forward a Port** and enter `8000`. From the directory page, open
`interactive/` and select a page. Locally, the direct paths are:

- `http://localhost:8000/interactive/strategy2demo.html`
- `http://localhost:8000/interactive/strategy2notation.html`
- `http://localhost:8000/interactive/strategy4demo.html`

Keep the terminal command running while using the explorer. Press `Ctrl+C` in
that terminal to stop the server. The forwarded port is private by default.

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
corpus, but they are not complete proofs unless every named
dependency has a proven source. Numerical optimization, plotting, or search
evidence remains empirical unless a rigorous certificate is recorded.


## 2026-08-02 replacement verification

The CE2 exactly-one-Vd1/Vd2 case was rechecked after `4147` was corrected to use separate local charts at the two distinguished vertices. The replacement preserves the full skeleton. `4013` has the corresponding skeleton-data strength, and `414b` contains the exhaustive positional case split. The main theorem status remains `Proven` because the corrected branch and all verification checks pass.

## Current reproducible verification

The permanent workflow
[`.github/workflows/proof-ci.yml`](.github/workflows/proof-ci.yml) verifies the
active proof graph, exact certificate replays, universal Strategy 2
real-variable theorems, pinned semantic-equivalence paper rebuild, visual
page-boundary scan, and the pinned Lean statement project. The current
verification metadata is generated in
[`arrange/CURRENT_VERIFICATION_SUMMARY.txt`](arrange/CURRENT_VERIFICATION_SUMMARY.txt).

The Strategy 2 formalization milestone is intentionally limited: Lean checks
that the exact optimization domains and theorem statements elaborate under a
pinned Lean/Mathlib environment, while the ten theorem proofs still contain
`sorry`. The complete paper proofs of the universal optimization statements
are in
[`arrange/paper_draft/04f_strategy2_pure_theorems.tex`](arrange/paper_draft/04f_strategy2_pure_theorems.tex).

For local and archival reproduction, see [`REPRODUCE.md`](REPRODUCE.md). The
workflow also publishes a deterministic bundle containing the paper,
provenance records, exact certificate code/data, and Lean statement project.
