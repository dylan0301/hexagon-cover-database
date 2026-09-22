# BC/D finite-caliper integration

## Mathematical changes

The active BC terminal now uses at most five fixed points. With $x=B_0$,
$y=1-A_1$, and $z=B_3$, its two nonuniform capacity deficits are
$r=1-c_{\max}(1-y,z)$ and $t=1-c_{\max}(1-z,x/2)$.
The actual forced set uses $\widehat t=\min(t,A_3)$, not an unverified
cross-pair domination assumption. Clipping yields a diameter contradiction;
otherwise five hull-edge calipers close through the coupled capacity inequality.
Source 2615 gives the reusable slack-sensitive envelope and complete analytic
concavity reduction; 2616 gives the calipers and original-cover forcing.

D retains four points but strengthens the geometric lemma to require only
$a\ge0$, $\varepsilon>0$, $\beta\ge0$, and
$\beta\le\varepsilon/(a+\varepsilon)$. Diameter handles $a=0$ or
$a+\varepsilon\ge1$; the remaining quadrilateral has four explicit calipers.
Original supplier size estimates remain where they are used for gap forcing.

## Scope and preserved mathematics

Only the BC/D terminal enclosure arguments cease to depend on the signed
center normal form. Structural midpoint/edge classification, the two local
supplier charts, replacement, and the exact zero-gap certificate remain.
The old CE1 return is retained as a historical independent calculation,
not as an active terminal prerequisite. The old six-point BC compatibility
set still obstructs enclosure by convex-hull inclusion.

Both paper editions share the new full capacity and caliper calculations.
The inline edition still has immediate proofs and no forward proof dependencies.
The deliberately changed D fingerprints and reviewed source baseline are
updated explicitly; the old baseline is archived. No exact geometric test
is replaced by a blanket success or a floating-point sample.

## Interactive materials

The dependency graph, Markdown proof trees and generated offline tree viewer
use the new route. A standalone BC/D viewer stages the current five/four-point
sets and displays every hull-edge caliper. Its numerical readouts are explanatory,
not mathematical certificates. Historical live six-point visualizer recordings
remain authenticated and clearly labeled; their pixels, snapshots and original
capture provenance are not rewritten as though they were new five-point captures.

## Validation contract

Run `python proof/check.py`, both paper-edition source audits, graph and trace
regeneration checks, interactive checks, proof-tree checks, the historical live
capture audit, browser QA, and both pinned TeX builds. The exact local scripts
check identities and rational signs; analytic domain coverage is supplied by
2615--2616. This is not proof-assistant formalization. Generated PDFs and source
links are published only after read-only validation succeeds.

## Completed integration validation

Both publication editions were rebuilt in the pinned TeX Live 2025 image in run 35738552404. Their exact PDFs and every manuscript input were verified against that reviewed snapshot before installation. The canonical PDF has 76 pages; the inline-proof PDF has 73 pages. The compiled source inventory has 96 canonical statements and 82 immediate inline proofs, with 14 statement consolidations and 80 retained canonical proof bodies cross-checked.

Read-only proof checks, 18 exact envelope identities/sign checks, 21 inherited identities and 9 rational sign-certificate leaves passed. The caliper regression suite passed 15 exact identities, 48 rational BC support cases and 9 rational D support cases; the analytic proof, not these samples, supplies universal coverage. Both exact zero-gap derivation and global-positivity replays passed.

Generated graph/trace checks, all interactive-page audits, proof-tree regeneration and the historical live-capture audit passed. Local Chromium review exercised 16 browser cases, including construction steps, every caliper button, singleton gaps, D diameter endpoints, offline navigation and 390-pixel layouts, with no JavaScript errors. Coincident witness labels are combined without changing the mathematical data. Relevant new BC/D and capacity-proof PDF pages were visually reviewed; all pages passed the PDF render/media-box audit.

The D proof-tree page no longer incorrectly lists the BC envelope as its prerequisite. The publication README inventory and active dependency map were reconciled. Historical six-point GIFs remain explicitly labeled and byte-unchanged. Temporary delivery code and payloads are removed from the final tree. Immutable navigation is pinned to the source-integration commit. The final remote SHA and CI status are reported in the pull request rather than assumed by this report.
