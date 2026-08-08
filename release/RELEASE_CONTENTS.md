# Archival release bundle

`tools/build_release_bundle.py` creates a deterministic ZIP containing:

- the compiled paper;
- current verification metadata;
- the active dependency graph and complete proof manifest;
- the 407X and Strategy 4 provenance manifests;
- exact Strategy 4 certificate code and sparse data;
- the pinned Lean Strategy 2 statement project;
- the pinned permanent workflow and verification scripts, including the
  stable-semantic PDF comparator;
- the license and reproduction instructions.

The ZIP is uploaded by the permanent verification workflow. It is not tracked
in Git because it is deterministically regenerated from tracked inputs.
