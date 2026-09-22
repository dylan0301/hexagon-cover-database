
# Interactive explanations

The files in this directory are explanatory interfaces, not proof
certificates.

- **[Self-contained linked proof trees](proof_trees/README.md):** 28 Markdown
  pages separating the main argument from long calculations. Every argument
  page defines its local terminology, including neighboring suppliers, support,
  gaps, reaches, and candidate triangles. Start with
  [the newcomer introduction](proof_trees/START.md) or open any tree directly.
  The midpoint proofs remain expanded. The folder includes a reproducible
  offline HTML viewer generator and link/definition checks.

- **[Animated proof guide](animated_proof_guide/README.md):** 40 live-visualizer GIFs,
  48 case/subcase explanations, snapshots, and reproducible capture scripts.
  Download the folder and open `animated_proof_guide/index.html` locally; GitHub
  displays the HTML source rather than deploying it.

- `readable_proof_dependency_graph.html`: clickable canonical formal-statement graph
  (the legacy filename is retained for stable links),
  routing table, case cards, and embedded figures;
- `trace_exact_ab_envelope_explorer.html`: trace-exact \(AB\)-envelopes,
  actual gaps, and finite witnesses;
- `trace_exact_ab_presets.json`: deterministic visualization presets;
- `../arrange/paper_draft/figures/trace_exact_ab/`: fifteen PNG panels
  generated from those same presets and colocated with the manuscript;
- `zero_gap_nine_point_demo.html`: zero-gap finite-enclosure mechanism.

```bash
python interactive/generate.py --dependency-graph
python interactive/generate.py --dependency-graph --check
python interactive/generate.py --trace-assets
python interactive/generate.py --trace-assets --check
python interactive/check.py
python interactive/proof_trees/check.py
```

The `--trace-assets` flag regenerates the standalone trace-exact explorer,
its preset JSON, and exactly fifteen matching PNG panels under the manuscript
figure directory.  It does not generate either deleted atlas wrapper or the
separate `strategy4_core_case_example.png` illustration; the latter is a
static, SHA-256-pinned publication asset.

The dependency graph's generated companion JSON is intentionally ignored
because its HTML already contains the complete data payload and offers it as a
download. The trace-explorer preset JSON remains a tracked standalone artifact.
The explorer and every generated or static image are explanatory only and
have no proof-authority status.

## Current BC/D calipers

[BC/D finite-caliper viewer](bc_d_finite_calipers.html): standalone five-point BC and four-point D constructions, staged witnesses, and hull-edge support triangles. [Proof trees](proof_trees/index.html) and the dependency graph use the new 2615--2616 route. Archived live six-point recordings remain explicitly labeled in the animated guide.
