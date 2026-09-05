# Hexagon Covering Proof Corpus

This repository contains the proof that seven open unit equilateral triangles
do not cover a regular hexagon of side length one.

\[
\boxed{\text{The regular unit hexagon cannot be covered by seven open unit
 equilateral triangles.}}
\]

The authoritative mathematical material is maintained in four content
directories:

- [`proof/`](proof/): numbered proof sources, exact certificates, and status
  information;
- [`arrange/`](arrange/): the canonical manuscript and publication support;
- [`interactive/`](interactive/): self-contained visual explanations and
  dependency navigation;
- [`prompts/`](prompts/): research prompts and their dated archive.

No proof-assistant formalization is maintained at present. The former partial
Lean statement project was deleted because it did not prove the geometric
argument and is no longer part of the repository contract.

## Main entry points

- Main theorem and exhaustive assembly:
  [`proof/0XXX_main/0000_main_theorem.md`](proof/0XXX_main/0000_main_theorem.md)
- Proof-tree index:
  [`proof/0XXX_main/0001_proof_tree_index.md`](proof/0XXX_main/0001_proof_tree_index.md)
- Reusable lemma and terminal catalog:
  [`proof/0XXX_main/0003_reusable_lemma_catalog.md`](proof/0XXX_main/0003_reusable_lemma_catalog.md)
- Current status:
  [`proof/0XXX_main/0002_status_and_dependencies.md`](proof/0XXX_main/0002_status_and_dependencies.md)
- Canonical paper:
  [`arrange/paper_draft/main.pdf`](arrange/paper_draft/main.pdf)
- Interactive proof dependency graph:
  [`interactive/readable_proof_dependency_graph.html`](interactive/readable_proof_dependency_graph.html)
- Standalone trace-exact \(AB\)-envelope explorer:
  [`interactive/trace_exact_ab_envelope_explorer.html`](interactive/trace_exact_ab_envelope_explorer.html)
- Colocated trace-exact manuscript panels:
  [`arrange/paper_draft/figures/trace_exact_ab/`](arrange/paper_draft/figures/trace_exact_ab/)
- Zero-gap nine-point demonstration:
  [`interactive/zero_gap_nine_point_demo.html`](interactive/zero_gap_nine_point_demo.html)

## Proof architecture

Seven distinguished points canonically identify one C triangle and six V
triangles. The C triangle is classified as CE0, CE1, or CE2. Each V triangle
is classified as Vd0, Vd1, Vd2, or T3-like. Every hypothetical cover is routed
to one of three methods:

1. trace-length or skeleton-length contradiction;
2. normalized area-loss contradiction;
3. a direct finite equilateral-enclosure contradiction.

For a V triangle, uppercase \((A_i,B_i,C_i)\) denotes actual maximal reaches.
Lowercase \((a_i,b_i,c_i)\) denotes selected lower bounds. In particular,
\(N_+\) is defined from the uppercase actual reaches. Singleton boundary gaps
remain gaps because the covering triangles are open.

The active proof mechanisms are exposed through three reusable interfaces:
`2400` for the multiple-ascent area route and the retained T3-like alternative,
`2531` for the length-budget rows, and
`2610` for the six finite-enclosure terminal families. Detailed case files are
retained as placement adapters and compatibility paths.

The zero-gap $N_+=1$ row now uses one type-independent nine-point theorem:
the common $c_{\max},C_+,C_-$ engine handles all permitted adjacent supports
without changing the six radial or three asymmetric points.

The difficult zero-gap nine-point overlap calculation is an exact certificate
over integers, rationals, and \(\mathbb Q(\sqrt3)\). Floating-point scans are
not proof dependencies.

The fifteen trace-exact manuscript panels are generated from the same preset
registry as the standalone explorer.  The additional
`strategy4_core_case_example.png` is a SHA-256-pinned static illustration.
These images explain the geometry but are not proof authorities; theorem
status comes from the numbered `proof/` sources and the incorporated exact
certificate.

## Validation

```bash
python -m pip install -r arrange/_support/requirements.txt
python proof/check.py
python interactive/generate.py --trace-assets --check
python interactive/generate.py --dependency-graph --check
python interactive/check.py
python arrange/build.py --all
```

GitHub Actions runs the same source, exact-certificate, interactive, and paper
checks on every branch and pull request. Generated verification summaries,
release ZIP files, dependency manifests, and LaTeX intermediates are not
tracked.
