# Archival release bundle

`tools/build_release_bundle.py` creates a deterministic ZIP containing:

- the consolidated compiled paper;
- the complete TeX manuscript/specification source and figure assets;
- current verification metadata;
- the complete proof-source tree, active proof-reference graph, and proof manifest;
- the 407X and Strategy 4 provenance manifests;
- exact Strategy 4 certificate code and sparse data;
- the pinned Lean Strategy 2 statement project;
- the write-enabled canonical paper workflow and the read-only permanent proof workflow;
- all verification and pinned-rebuild scripts, including the stable-semantic
  PDF comparator;
- the license and reproduction instructions.

The ZIP is uploaded by the permanent proof workflow. It is not tracked in Git
because it is deterministically regenerated from tracked inputs. The workflow
extracts it into a clean directory and reruns the proof-reference graph, source linter,
Strategy 2 semantic interface, algebra, PDF metadata, and manifest checks.
