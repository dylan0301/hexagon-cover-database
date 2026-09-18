# Construction-focused guide: validation record

## Scope

40 GIFs, 48 explanatory entries, 818 captured states. Fifteen clips are new or
revised; 25 original clips retain their previous captured bytes. Revised clips
are 960 by 900 pixels with 28–36 states and deliberate pauses.

Proof base: `3b927c996d7641b20887dc56c1fa741cac674256`.
Visualizer source: `1cd468b26aed30d5ddcf1ffa501805bf9720482c`.
The canonical proof and both manuscript editions are unchanged.

## Additional checks

- Actual BC total endpoints are independently recomputed from six original
  triangles. On r2 the neighbor, not the own triangle, determines the endpoint.
- BC/D capacity clips retain all six source-feasibility checks and full
  construction conditions while hiding off-diagonal witnesses and enclosure fits.
- BC capacity endpoints move at least 0.216 hexagon-side units; the D examples
  move 0.199247 and 0.171916. Fixed inputs and NEW INPUT phases are separate.
- Actual D supplier traces are measured in the original triangles. The entry,
  exit, epsilon=1-u, and P_T coordinates are independently replayed.
- Replacement begins with a genuine Vd1 source, tilted 15 degrees from hex axes.
  Both p2=0.33 and p2=0.67 outputs are independently classified as no-support
  nonsupercritical triangles, with boundary sums 0.98. Original supplier traces
  on the affected skeleton pieces are preserved. Vd2 remains a separate case.
- Area Conj uses six native high-quality optimizer rows with all handoffs moved
  by 0.58. Max Area changes a by 0.49 and b by 0.44. Native readouts are checked
  against the pinned optimizer, and candidate polygon areas are replayed by an
  independent Python clipping routine. Selected critical rows are not actual N+.
- The two area JSON files are explicitly labeled control recipes, not
  importable Controller snapshots. Other snapshots retain their native formats.
- Every revised scene must change a measurable part of its geometry panel; a
  changing caption alone cannot satisfy the visible-motion check.

`check.py --require-live` rejects development captures and verifies the deployed
JavaScript/source-build match, including retained capture provenance. Existing
proof, exact-certificate, dependency, trace, and interactive checks are retained.
Final remote CI also rebuilds and compares both manuscript PDFs.

These checks audit explanatory assets and numerical examples, not new proofs.
The area search gives lower estimates of true maximum area; its loss estimates
are upper estimates of minimum loss and cannot certify the theorem.

## Completed capture checks

Read-only live capture and all source/browser checks above passed in workflow run `35115923752`. Native readout text clipping is additionally checked before every area screenshot. Final remote publication and pinned manuscript rebuilds are checked separately on the final branch head.
