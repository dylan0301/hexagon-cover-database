# Hexagon Covering Proof Corpus

**Animated companion:** [case-by-case GIF guide](interactive/animated_proof_guide/README.md)
with 40 visualizer animations and 48 case/subcase explanations.

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
`2610` for the three active finite-enclosure witness families. Detailed case files are
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

## Compressed proof route

The three active finite-witness families BC/D/F use at most 5/4/9 points.
Only F uses a disk in the minimal route. The seven-point complementary-gap
construction A is retained as an optional independent proof. N0 now uses the
center-aligned BC theorem, not A. Nonsupercritical path roles are never
split by V type.

`2008b` proves the required neighboring domination directly, without the
piecewise cubic capacity formula. `2612` owns the actual/bounded radial
frontier and exact boundary propagation identities. `2613` gives one
midpoint-supplier reduction for CE1/CE2; `2614` gives the two-vertex scalar
replacement with both charts and all strict margins. The two rescuer charts
supply only local inputs to D. `2532` separates the common open-cover budget
from the distinct length and area estimates. The CE1 return remains historical; the exact zero-gap certificate is unchanged.

## Reading-order and self-containment review

The follow-up audit in
`arrange/20260910_self_containment_editorial_report.md` records the definition-order
review, notation crosswalks, and repaired local proof inputs. The `(3,0)`
normalization remains intact. The paper's exact computational appendix is
supplied with its finite data and both replay programs in the source package.

## Human-readable manuscript revision

Both paper editions now begin with the boundary/interior tradeoff and include
a worked selected-gap witness, explicit original/candidate/replacement scopes,
and a staged explanation of the zero-gap enclosure. The reviewer report is
[`arrange/20260913_readability_review_report.md`](arrange/20260913_readability_review_report.md).
Run `python arrange/_support/verify_readability_preservation.py` to compare the
formal statements, complete proof environments, and proof/certificate corpus
with the pre-review baseline.

## Five-point BC and four-point D calipers

The active selected-gap obstruction uses **at most five points**, two different own-ray capacity pairs, and an explicit neighboring-supplier clipping. The D geometric theorem uses **four points and only a ratio bound**. Both terminal enclosure proofs use finite hull-edge calipers rather than the signed center normal form. The new numbered sources are [2615](proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2615_slack_sensitive_radial_envelope.md) and [2616](proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2616_bc_d_finite_calipers.md).

The [standalone BC/D caliper viewer](interactive/bc_d_finite_calipers.html) constructs the current point sets. Historical live six-point visualizer recordings are explicitly labeled in the animated guide; their provenance is not rewritten. Structural midpoint classification, the original supplier charts, replacement, and the zero-gap certificate remain separate.

### Reusable lemmas and shorter manuscripts

The [shortening report](arrange/20260923_reusable_lemmas_shortening_report.md)
records the 76-to-70-page canonical and 73-to-68-page inline revisions.
The five-point BC threshold is now capacity-free; total-endpoint forcing
supplies both clipped-path and uniform witnesses; BC and F share one deficit
estimate. Duplicate wrappers and calculations are removed without changing
raw (3,0) normalization, replacement charts, or exact zero-gap certificates.

### Quarter-range envelope and factored rescuer ratios

The [next revision report](arrange/20260923_quarter_envelope_revision_report.md)
records the further 70-to-67-page canonical and 68-to-65-page inline changes.
The exact five-point BC witnesses now use a polynomially proved quarter-range
comparison envelope with linear slack coefficient; no implicit-root derivatives
are needed in the active coupling proof. The T3-like and Vd1 ratio estimates
are factored directly, and a strict own-ray lemma shortens the preliminary F
bound. Witness counts remain 5/4/9, clipping is unchanged, and both replacement
charts and exact zero-gap data retain byte-preservation checks. The wider
historical envelope remains available separately in numbered source 2615a.

## Case F explicit-comparison revision

The active fixed-start Case F calculation is [3105b_explicit_comparison_enclosure.md](proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105b_explicit_comparison_enclosure.md).
The original nine witnesses and actual disk are unchanged. The tangent proof
uses explicit cubic/quadratic comparisons and exact coefficient budgets, with
remaining degree-27 boundary Taylor work. It no longer reads an SOS witness file
or a Bernstein transcript. The old exact programs remain historical CI checks.

Run the active calculation from the repository root:

```bash
python proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/verify_explicit_stage.py --output /tmp/F-explicit.json
```

The new [fixed-start viewer](interactive/f_explicit_comparison.html)
is a numerical illustration, not a proof. Older F Newton/cap-chain captures
are labeled historical. See `arrange/20260924_f_explicit_comparison_integration.md`
for the integration and validation record.
