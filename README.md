# Hexagon Covering Proof Corpus

This repository contains the proved corpus for covering a regular hexagon by
seven open unit equilateral triangles, the self-contained AMS manuscript, exact
computer-assisted certificates, interactive geometric aids, and pinned
verification infrastructure.

## Main theorem

The proved theorem is

$$
\boxed{\text{The regular hexagon }H\text{ of side length }1\text{ cannot be covered by seven open unit equilateral triangles.}}
$$

Equivalently,

$$
\boxed{\text{For every }L>1,\ H_L\text{ cannot be covered by seven closed unit equilateral triangles.}}
$$

The exhaustive proof assembly is
[`proof/0XXX_main/0000_main_theorem.md`](proof/0XXX_main/0000_main_theorem.md).
The open/closed/scaled equivalence is
[`1003`](proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md).

## Paper

The current self-contained manuscript is
[`arrange/paper_draft/main.pdf`](arrange/paper_draft/main.pdf). Its source is
organized as one proof rather than a short summary followed by a second
technical manuscript:

1. introduction, classifications, and routing;
2. structural reduction and signed center geometry;
3. trace-length bounds;
4. boundary-reach propagation;
5. area loss;
6. nine-point enclosure;
7. exhaustive completion;
8. one exact mixed-overlap certificate appendix.

For a shorter first reading, the derived
[`statements-only edition`](arrange/paper_draft/statements_only/main.pdf)
retains the explanatory prose, definitions, formal statements, and figures
while omitting proof bodies and calculation-only material. Its complete
generated source is in
[`arrange/paper_draft/statements_only/`](arrange/paper_draft/statements_only/).
The canonical manuscript remains authoritative for every proof and exact
certificate.

The target is approximately ninety pages. Mathematical content formerly
repeated across reader, bridge, optimization-registry, and verification layers
is stated once in the printed paper. The source-only registries and pinned Lean
scalar-statement elaboration project remain active verification interfaces.

Paper navigation and provenance:

- [`arrange/ams_paper_generation_guide.md`](arrange/ams_paper_generation_guide.md): active authoring and build specification;
- [`arrange/paper_proof_crosswalk.md`](arrange/paper_proof_crosswalk.md): section-to-proof-package map;
- [`arrange/paper_draft/source_ledger.md`](arrange/paper_draft/source_ledger.md): TeX and exact-certificate source ledger;
- [`arrange/CURRENT_VERIFICATION_SUMMARY.txt`](arrange/CURRENT_VERIFICATION_SUMMARY.txt): current page count, PDF digest, and pinned verification metadata.

A source change on `main` triggers the write-enabled paper workflow, which
regenerates the statements-only source, builds and audits both editions, and
commits both PDFs, the generated reading-edition source, and the canonical
verification summary back to `main`. Before committing, that workflow replays
the active proof-reference graph, exact certificates, Lean scalar-statement
elaboration, and two-build semantic PDF audits. The ordinary read-only proof
workflow independently checks that the generated source is current and that
both editions rebuild reproducibly on user pushes and pull requests.

## Start here

Recommended mathematical reading order:

1. [`0000_main_theorem.md`](proof/0XXX_main/0000_main_theorem.md)
2. [`0001_proof_tree_index.md`](proof/0XXX_main/0001_proof_tree_index.md)
3. [`1003_open_unit_vs_shrunken_closed_equivalence.md`](proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md)
4. [`1101_CE_classification.md`](proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md)
5. [`1201_V_triangle_types.md`](proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md)
6. [`1214_strict_boundary_handoff_selection.md`](proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
7. [`2019_interval_component_and_path_budget.md`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
8. [`201d_raw_and_relaxed_g_chains.md`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md)
9. [`201a_equilateral_enclosure_and_radical_calculus.md`](proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201a_equilateral_enclosure_and_radical_calculus.md)
10. [`2530_common_CE1_CE2_budget_lemmas.md`](proof/2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
11. [`3000_CE0_index.md`](proof/3XXX_CE0/3000_CE0_index.md)
12. [`4000_CE1CE2_index.md`](proof/4XXX_CE1CE2/4000_CE1CE2_index.md)
13. [`0002_status_and_dependencies.md`](proof/0XXX_main/0002_status_and_dependencies.md)

## Unified proof architecture

Seven distinguished points force one C triangle and six V triangles.
The C triangle is exactly one of CE0, CE1, CE2. Every V triangle is
exactly one of Vd0, Vd1, Vd2, T3-like. For a V triangle let
`(A_i,B_i,C_i)` be its actual maximal backward, forward, and radial reaches,
and put

$$
N_+=\left|\{i:A_i+B_i>1\}\right|.
$$

Lowercase `(a_i,b_i,c_i)` always denotes selected lower bounds and never the
actual maxima defining `N_+`. Singleton boundary gaps remain gaps because the
covering triangles are open.

For a CE1/CE2 role closure $T_C=\overline{U_C}$ one has
$O\in U_C\subset\operatorname{int}(T_C)$, and $T_C$ contains exactly one
radial midpoint.  The precise hypothesis and proof are recorded in
[`2100`](proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md).

The proof uses four mechanisms:

1. trace-length bounds on the perimeter or full skeleton;
2. propagation of boundary-reach lower bounds through the exact local
   admissible set;
3. normalized area-loss estimates;
4. an equilateral-enclosure obstruction for nine points forced into the center
   C triangle.

For a nonsupercritical V triangle, low radial lower bounds use
`B<=1-A` directly. High radial lower bounds use the raw admissible-set transfer;
the demanded midpoint then makes the output automatically nonsupercritical.
The raw zero-radial map is not used as an identity transfer.

## Proof corpus map

- [`proof/0XXX_main/`](proof/0XXX_main): main theorem, proof-tree index, and dependency status.
- [`proof/09XX_appendices/`](proof/09XX_appendices): glossary, notation, and archived navigation.
- [`proof/1XXX_foundations/`](proof/1XXX_foundations): definitions, conventions, and classifications.
- [`proof/2XXX_geometric_lemmas/`](proof/2XXX_geometric_lemmas): reusable geometric and analytic lemmas.
- [`proof/3XXX_CE0/`](proof/3XXX_CE0): CE0 proof-tree branch.
- [`proof/4XXX_CE1CE2/`](proof/4XXX_CE1CE2): combined CE1/CE2 proof-tree branch.
- [`proof/9XXX_failed_ideas/`](proof/9XXX_failed_ideas): failed routes, counterexamples, and empirical warnings.

The complete file list is [`proof/MANIFEST.txt`](proof/MANIFEST.txt).

## Exact certificates and Lean statement elaboration

The Strategy 4 mixed support-arc intersections use exact integer, rational,
and `Q(sqrt(3))` arithmetic. The authenticated sparse data, derivation
verifier, positivity verifier, and transcript digest form one certificate.
Floating-point and interval arithmetic are not proof dependencies.

The Strategy 2 Lean project in
[`formalization/strategy2_optimization/`](formalization/strategy2_optimization/)
elaborates the scalar statements needed for the long calculation layer. Its
ten theorem bodies are intentional `sorry` admissions. This project is a
statement check, not a proof or formalization of the geometric argument; the
complete proofs remain in the TeX and numbered proof sources.

## Interactive navigation

The following pages are visual references, not proof certificates:

| Page | Scope |
|---|---|
| [`interactive/strategy2demo.html`](interactive/strategy2demo.html) | propagation geometry and case overlays |
| [`interactive/strategy2notation.html`](interactive/strategy2notation.html) | reaches, transfer maps, center data, and routing notation |
| [`interactive/strategy4demo.html`](interactive/strategy4demo.html) | nine-point obstruction mechanism |

To preview locally from the repository root:

```bash
python3 -m http.server 8000
```

Then open the relevant page under `http://localhost:8000/interactive/`.

## Skeleton counterexample warning

The May 24, 2026 imported counterexample numerically verifies seven closed
equilateral triangles of side strictly below one covering the full skeleton
`S`. See
[`9081_skeleton_cover_counterexample.md`](proof/9XXX_failed_ideas/908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md).

Therefore noncoverage of the full skeleton is not a valid unconditional route
to the theorem. Every active skeleton argument is conditional on its stated
classification and trace hypotheses.

## Status and verification

Use a mathematical result as established only when its numbered source has a
status supporting the claim, normally `Status: Proven`, or when it is an exact
definition. Navigation, empirical, experimental, target, strategy, and failed
files do not prove a claim.

The permanent workflows are:

- [`.github/workflows/paper-rebuild.yml`](.github/workflows/paper-rebuild.yml): regenerate, build, and commit the canonical and statements-only paper artifacts;
- [`.github/workflows/proof-ci.yml`](.github/workflows/proof-ci.yml): read-only proof, certificate, Lean, both-paper, and release verification.

For local and archival reproduction, see [`REPRODUCE.md`](REPRODUCE.md).
