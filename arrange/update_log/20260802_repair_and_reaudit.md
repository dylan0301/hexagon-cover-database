# 2026-08-02 Final Repair, Consolidation, and Re-Audit

## Mathematical repairs

- `4147` uses separate `V_0`- and `V_1`-charts and proves all open-role,
  reach, Vd0, nonsupercritical, and skeleton-preservation claims.
- `4013` is stated and proved at full-skeleton strength; the original
  full-hexagon statement is its corollary.
- `2110` uses only skeleton data.
- `414b` gives the exhaustive CE2 exactly-one-Vd1/Vd2 placement audit.
- No new mathematical defect was found in the repaired chain.

## Source and provenance repairs

- Actual `N_+` definitions use uppercase actual reaches.
- Singleton-inclusive branches use “nonempty gap.”
- Active geometric prose uses “V triangle,” not “row.”
- `04_strategy2_verification.tex` contains the single CE2 one-Vd assembly.
- Current `407X` blobs are generated and checked from exact file bytes.
- Strategy 4 code and data blobs are independently authenticated.
- The active proof dependency graph is generated transitively from the
  main theorem and status table.
- The proof manifest is generated and checked in both directions.

## Reproducible verification

Permanent CI is read-only, pins GitHub Actions and Python dependencies,
replays both exact Strategy 4 verifiers, and rebuilds the paper twice in TeX
Live 2025 with a fixed `SOURCE_DATE_EPOCH`.  Because XeTeX/xdvipdfmx raw object
bytes are not stable across otherwise identical builds, CI compares page
geometry, text coordinates, links, outlines, and exact 144-DPI raster pixels.
It also renders every page, checks the media-box border, and uploads the
verified artifact.

BUILD_METADATA_PLACEHOLDER
