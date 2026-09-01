# Historical Strategy 2 Radial-Propagation Package

Status: Historical snapshot; not an active proof owner

## Audit result

The cleanup did **not** delete the numbered radial-propagation mathematics.
The reusable map and routing lemmas remain in the `20XX_V_triangle_geometry`
block, including `2011`, `2016`, `2017`, `2019`, and `201d`.  The historical
case packages also remain at their numbered locations, notably the old
`401X`, `407X`, `410X`, `413X`, and `414X` directories.

What the cleanup removed was the assembled Strategy 2 manuscript and scalar
verification layer formerly stored in `arrange/paper_draft`, together with its
navigation registry, provenance wrapper, verification scripts, and two
interactive explanatory pages.  Those removed materials are restored here as
an archive.

## Snapshot provenance

- Source repository: `dylan0301/hexagon-cover-database`
- Source commit: `399fdd69f21d7ad1bcf12e4cbd726857395e60d0`
- Source tree: `23a6b9cf60e7975f10191a2181f3d0c892b08985`
- Restoration date: 2026-09-01
- Restoration rule: existing source blobs are reused byte-for-byte; no
  mathematical wording is edited in the archived copies.

The complete blob crosswalk is recorded in `snapshot_manifest.json`.

## Contents

### `paper_sources/`

The historical chapter entry point is
`paper_sources/04_boundary_propagation.tex`.  The directory also contains the
complete `04_strategy2_*`, `04d_*`, `04e_*`, and `04f_*` source family that was
removed from the active manuscript directory.

These files are intentionally not imported by either current `main.tex` and
are not a standalone publication target.  Shared prerequisites such as the
universal calculus, signed-center calculus, common budgets, and short-Vd
placement material remain in the live manuscript sources.

### `registry/`

The old scalar-calculation crosswalk is retained byte-for-byte as
`2111_strategy2_pure_optimization_registry.md.txt`.  The archival `.txt`
suffix prevents the current proof-link checker from treating its historical
relative links as live dependencies.

### `provenance/`

`407X_PROVENANCE.json` records the authenticated file hashes produced by the
old Strategy 2 split finalizer.

### `auxiliary_tools/`

The exact symbolic checker, statement-synchronization checker, and split
provenance finalizer are retained for forensic reproducibility.  They preserve
their historical path assumptions and are not run by current CI.

### `interactive/`

The retired Strategy 2 notation laboratory and geometry/certificate explorer
are retained as explanatory artifacts.  They are not linked from the active
interactive index.

## Live numbered sources

The surviving numbered proof owners remain in place and should be consulted
before this archive:

- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md`
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2016_universal_Tplus_normal_form.md`
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2017_threshold_routing.md`
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md`
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md`
- `proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/`
- `proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/`
- `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/`
- `proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/`
- `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/`

No Lean or other proof-assistant project is revived by this archive.
