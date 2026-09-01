
# Interactive explanations

The files in this directory are explanatory interfaces, not proof
certificates.

- `readable_proof_dependency_graph.html`: clickable formal-statement graph,
  routing table, case cards, and embedded figures;
- `trace_exact_ab_envelope_explorer.html`: trace-exact \(AB\)-envelopes,
  actual gaps, and finite witnesses;
- `trace_exact_ab_presets.json`: deterministic visualization presets;
- `zero_gap_nine_point_demo.html`: zero-gap finite-enclosure mechanism.

```bash
python interactive/generate.py --dependency-graph
python interactive/generate.py --dependency-graph --check
python interactive/check.py
```

The generated companion JSON is intentionally ignored because the HTML already
contains the complete data payload and offers it as a download.
