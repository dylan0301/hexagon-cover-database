# 2026-08-16 paper consolidation

## Objective

Reduce the 134-page manuscript to an approximately ninety-page self-contained
paper without deleting any theorem, routed case, proof-critical hypothesis,
geometric construction, or exact certificate.

## Structural change

The previous manuscript separated a short reader account from fourteen
technical appendices. The same definitions, transfer interfaces, and branch
conclusions appeared in multiple layers. The revised assembly uses one proof
narrative:

1. introduction and routing;
2. structural reduction and signed center geometry;
3. complete trace-length proof;
4. complete boundary-reach propagation proof;
5. complete area-loss proof;
6. complete nine-point enclosure proof;
7. final assembly;
8. exact mixed-overlap certificate appendix.

Established TeX modules are incorporated under method-level wrappers and their
heading levels are demoted during input. This preserves theorem text, labels,
equations, and proofs while eliminating the duplicate reader/appendix account.

## Strategy 2

The printed paper no longer repeats the formalization-oriented sequence

`geometric bridge -> optimization registry -> universal theorem owner -> application`.

The exact source files and Lean statements remain in the repository and in CI.
The printed Section 4 states the geometric endpoint, return, T3-like, and Vd
conclusions once and follows them by the full detailed calculations. The 407X
provenance manifest remains linted but is not typeset.

## Strategy 4

The detailed nine-point construction is printed directly. A short completion
module supplies the cyclic support-arc lemma, exact mixed-overlap invocation,
witness enclosure, zero-gap obstruction, and routed applications. The exact
mixed-overlap certificate remains the sole appendix.

## Navigation and automation

Updated:

- `README.md`;
- `arrange/ams_paper_generation_guide.md`;
- `arrange/paper_proof_crosswalk.md`;
- `arrange/paper_draft/source_ledger.md`.

Added `.github/workflows/paper-rebuild.yml`. A source commit to `main` now
builds the manuscript in the pinned TeX Live image, checks references, boxes,
rendering, and the target page range, regenerates the current verification
summary, and commits the canonical PDF back to `main`. The existing read-only
proof workflow then performs the full proof, certificate, Lean, semantic PDF,
and release audit.

## Canonical build result

GitHub Actions run `31943335628` completed successfully and committed the
canonical artifact in commit `3c554d611b48f48cea4119580baa271c9e1464e4`.
The consolidated PDF has 97 pages, no undefined or multiply-defined references,
no overfull horizontal or vertical boxes, and passes the semantic rebuild and
rendered-border checks. Its canonical SHA-256 is
`2859cfc8814f50b54997e2997809bb592411dba0ac688405e9f2a86a6b53418a`.

## Proof invariants retained

- `N_+` is defined from actual maximal reaches.
- Lowercase reaches remain selected lower bounds.
- Singleton gaps remain uncovered gaps.
- Low-radial nonsupercritical transfer uses `B<=1-A` directly.
- High-radial component selectors and equality assignments are unchanged.
- Every center-free path hypothesis and endpoint external component is retained.
- The CE2 threshold alternative remains inclusive.
- Every T3-like branch and every Vd placement is retained.
- The two-chart Vd1 replacement is unchanged.
- The exact Strategy 4 arithmetic model and authenticated input are unchanged.
