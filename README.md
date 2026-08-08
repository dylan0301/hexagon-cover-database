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

The manuscript and active proof packages use three certificate classes,
retained as four named strategies for geometric readability:

1. **additive deficits:** boundary or conditional-skeleton length, and
   normalized area loss;
2. **isotone transfer:** compositions of one decorated $g$-family;
3. **convex support:** the equilateral enclosure gauge applied to the forced
   nine-point witness set.

The canonical transfer notation is:

$$
g_c(x)
=
\max\left\{
y:(1-x,y,c)\in\mathcal A
\right\},
\qquad
\widehat g_c(x)=\min\{g_c(x),x\}.
$$

Here $x$ is incoming boundary defect. For any map $f$, put

$$
f^\vee(a)=1-f(1-a).
$$

Then $g_c^\vee$ is the raw next-incoming reach lower transfer and
$\widehat g_c^\vee$ is its nonsupercritical extensive version. Center
intervals use the subscripted variants $g_{c,J}^\vee$ and
$\widehat g_{c,J}^\vee$. The free strict-supercritical outgoing envelope is
the single scalar

$$
g_c^{\rm sc}
=
\sup_{\{x:g_c(x)>x\}}g_c(x).
$$

Affine selected-$T_+$ and threshold relaxations are written as decorated
versions of $\widehat g_c^\vee$, rather than introducing new function
alphabets.

At zero radial demand,

$$
g_0(x)>x\quad(0<x<1),
\qquad
\widehat g_0(x)=x.
$$

Thus the historical raw $g_0$ is supercritical, while the hatted
nonsupercritical map is the identity.

The exact contact-cell files may retain the aliases

$$
B_c(a)=g_c(1-a),
\qquad
F_c(a)=\widehat g_c(1-a),
\qquad
G_c(a)=\widehat g_c^\vee(a)
$$

when they shorten branchwise algebra.

The existing Strategy 1 routing remains separate in the paper even when its
length bounds can be viewed as coarse transfer envelopes.

The universal local layer is:

- [`2019`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md): interval residuals, generalized handoffs, and boundary-path budgets;
- [`201d`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md): the canonical $g$-family, hats, complement duals, free-supercritical envelope, and relaxed composition;
- [`201a`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201a_equilateral_enclosure_and_radical_calculus.md): one enclosure gauge, one equilateral radical, and the four-frontier atlas;
- [`201b`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md): the global quarter radial envelope;
- [`201c`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md): the two Vd corner radial margins;
- [`2110`](proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2110_common_CE2_two_gap_application.md): one common application of the CE2 paired-endpoint theorem.

For CE1/CE2 all-Vd0 branches, the active proof is organized by the actual V triangle
count $N_+\in\{0,1\}$ and the active-gap rank
$\mathrm{gr}\in\{0,1,2\}$. The two $\mathrm{gr}=2$ cells share the same
paired-endpoint theorem.

## Interactive Navigation

These standalone pages are `Reference` visual aids. They explain the geometry,
notation, and proof-certificate structure, but they are not themselves proof
certificates and do not establish or change proof status.

| Interactive page | Scope | Status |
|---|---|---|
| [`strategy2demo.html`](interactive/strategy2demo.html) | Combined Strategy 2 geometry and certificate-overlay explorer, covering the five proof families and their canonical $g$-transfer chains | Reference |
| [`strategy2notation.html`](interactive/strategy2notation.html) | Interactive Strategy 2 notation lab for roles, reaches, the decorated $g$-family, composition, center data, and branch routing | Reference |
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
corpus, but they are not complete terminal proofs unless every named
dependency has a proven source. Numerical optimization, plotting, or search
evidence remains empirical unless a rigorous certificate is recorded.


## 2026-08-02 replacement and skeleton-interface audit

The CE2 exactly-one-Vd1/Vd2 terminal was re-audited after correcting `4147` to use separate local charts at the two distinguished vertices. The replacement now proves full skeleton preservation. `4013` is stated at the skeleton-data strength used by that reduction, and `414b` records the exhaustive placement re-audit. The main theorem status remains `Proven` because the corrected branch and all verification checks pass.

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
