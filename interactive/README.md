
# Interactive explanations

The files in this directory are explanatory interfaces, not proof
certificates.

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
