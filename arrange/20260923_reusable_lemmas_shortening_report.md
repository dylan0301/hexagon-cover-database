# Reusable lemmas and manuscript shortening: exact change report

## Revision and scope

Repository: `dylan0301/hexagon-cover-database`
Delivery branch: `chatgpt/reusable-lemmas-shortening-20260922232121`
Reviewed baseline: `a4f44a8b52c5097e07b82d2e4dec7efb83dd80e4`
Date: 23 September 2026

This revision implements the preceding shortening review. It edits both the
canonical paper and its inline-proof edition, synchronizes the authoritative
numbered proofs, updates affected interactive explanations and the dependency
graph, and adds regression checks. It does not change `main`, alter the main
theorem, or claim a new minimal witness count. The BC/D/F counts remain 5/4/9.

The publication commit, pull request, remote byte verification, and final CI
state are recorded in the exported delivery copy of this report. This repository
copy documents the mathematical/source change independently of its own commit ID.

## 1. Measured reduction

| Measure | Before | After | Change |
|---|---:|---:|---:|
| Canonical PDF pages | 76 | 70 | −6 (7.89%) |
| Inline-proof PDF pages | 73 | 68 | −5 (6.85%) |
| Canonical formal statement entries | 96 | 88 | −8 |
| Inline formal statement entries | 82 | 78 | −4 |
| Remaining canonical-to-inline statement merges | 14 | 10 | Four pairs merged in the canonical paper itself |
| Canonical extracted text characters | 152,313 | 144,847 | −7,466 |
| Inline extracted text characters | 141,182 | 135,132 | −6,050 |

The page counts come from clean builds, not a target or estimate. Font sizes,
page dimensions, margins, the main TeX preambles, and certificate data are not
changed. The reduction comes from mathematical reuse, deleted duplicate prose
and calculations, and removal of the classification example galleries from the
compiled paper. Image assets remain available to the interactive companions.
Text-character counts include extracted equations and are not word counts.

## 2. Capacity-free five-point BC threshold

### Before

The geometric five-point lemma included the auxiliary parameter `z` and the two
capacity-defined radii in its hypotheses. Geometry, capacity calculus, and the
covering application were presented as one package, although the proof already
showed that four hull-edge calipers always exceed one.

### After

The lemma in `fixed_witness/D_bc_finite_calipers.tex` is now purely geometric:

\[
0<x\le y<1,\qquad 0<r\le\min(y,1-y),\qquad 0<t\le x/2,
\]
\[
G_w=(1-w)V_0+wV_1,\quad k=y-r,\quad
F=\{M_0,G_x,G_y,rV_2,tV_4\}.
\]
Then
\[
\boxed{\Lambda(F)>1\iff
r+t+\max\{1/2,1-x(1-k)\}>\sqrt{1-k+k^2}.}
\]

The labels `lem:bc-five-point` and `lem:five-point-threshold` identify the same
lemma. The easy calipers are bounded below using selected point projections; only
the decisive caliper requires a nontrivial exact support maximum. The full five-caliper formulas
remain in authoritative source `2616_bc_d_finite_calipers.md`, so the reduced
paper display does not discard the underlying calculation.

The separate capacity instance sets
\[
r=f(1-y,z),\qquad t=f(1-z,x/2),\qquad f=1-c_{\max},
\]
and invokes the existing coupled inequality
\[
2(r+t)>(1-y+r)(2x-y+r).
\]
It gives `r+t > (1-k)(x-k/2)`, so the decisive numerator exceeds
`1-k/2+k²/2`. The remaining squared difference is `k²(1-k)²/4`.

This is an equivalence at side length one. It is **not** the assertion that this
caliper always attains the global minimum enclosure side. The coincident-gap
case `x=y` is retained explicitly by discarding the zero hull edge, not by an
invalid appeal to limiting strictness.

The finite-caliper discussion now also states the reusable support lower-bound
principle: selected point projections bound support maxima below. A complete
candidate orientation list is still required; a numerical angle scan is not a
replacement for that list.

## 3. One radial-forcing lemma, two useful consequences

### Total endpoint

The actual frontier remains
\[
\gamma_i=\max\{C_i,u_{i-1\to i},u_{i+1\to i}\},\qquad d_i=1-\gamma_i.
\]
The shortened lemma proves that every `s V_i`, `0≤s≤d_i`, is missed by every
open V triangle. Skeleton coverage therefore puts the entire closed segment
`[O,d_i V_i]` in the C triangle. Its proof is given once: maximal endpoints
exclude local open roles; diameter excludes nonlocal roles; the center is
excluded even from the closed V roles.

The arbitrary-candidate own-demand recovery clause is no longer part of the
active manuscript. It remains a separately proved compatibility result in the
numbered corpus, clearly marked as unnecessary for the current BC proof.
This does not remove the distinct original-cover condition `C_1≥c` used by D.

### Clipped-path corollary

Selected nonsupercritical lower pairs give the safe radius
\[
s_i=\min\{f(a_i,b_i),a_{i-1},b_{i-1},a_{i+1},b_{i+1}\}.
\]
On an actual gap-free nonsupercritical path, monotonicity reduces it to
\[
\boxed{s_i=\min\{f(A_i,B_i),A_{i-1},B_{i+1}\}.}
\]
This replaces the long public type-aware `Γ_i`/`D_i` capacity-maximum setup.
The distinction between the actual radius `d_i` and a certified smaller radius
`s_i` is stated explicitly. Neighboring suppliers are not ignored.

### Uniform consequence

Using one selected pair `(p,q)` at every vertex makes the clipped minimum
`f(p,q)`, because `f(p,q)≤min(p,q)`. The six forced radial points and the disk
of radius `h f(p,q)` in their convex hull follow immediately. The same argument
therefore serves the nonuniform BC path and the uniform F construction.
The uniform conclusion requires only skeleton coverage; convexity supplies the
disk. No claim that every point of that disk is individually V-excluded is made.

### BC clipping is unchanged

The active BC witnesses are still
\[
\{M_0,G_x,G_y,rV_2,\widehat tV_4\},\qquad
\widehat t=\min(t,A_3).
\]
The covering proof now cites the clipped-path corollary instead of repeating
neighbor-by-neighbor bookkeeping. If `A_3≥t`, it uses the capacity instance of
the new threshold lemma. Otherwise
\[
\|G_y-A_3V_4\|^2\ge1+(1-y)(2-y)>1.
\]
This diameter exit and the two **different** capacity pairs are retained.

## 4. Shared BC/F deficit bound and shorter envelope proof

The existing bound
\[
\frac{m(1-m)}2\le f(a,b)\le m,\qquad m=\min(a,b),\quad a+b\le1,
\]
is now reused explicitly in the F supporting-line calculation. Applied to its
complementary pair `(m,M)`, it gives
\[
2c_*-1\le1-m+m^2.
\]
The former separate quartic substitution and monotonicity calculation proving
that same inequality has been deleted from both manuscript editions. The
subsequent `X_0,Y_0,Φ` argument, its selector, the other radial sheet, exposed
contacts, and exact mixed-overlap certificates remain.

The slack-sensitive envelope proof now uses an explicit chord principle. If
`0<β≤m`, `F(0)=m`, `F≥β`, and `F` is concave on `[0,β]`, then
\[
F(\delta)\ge\max\{\beta,m-(m-\beta)\delta/\beta\}.
\]
The capacity application uses `β=m/2−2m²/5` and
`F(δ)=f(1−m−δ,m)`. It retains the coefficient range `m≤3/8`; no global
concavity claim or extension beyond that range is introduced.

**Domain clarification.** The former concavity statement assumed that the
larger coordinate was at least `1/2`, while its derivative proof only needs the
coordinates ordered. At `m=3/8`, the endpoint larger coordinate is `79/160`,
which is below `1/2`. The statement is now correctly given on the full ordered
nonsupercritical domain. On the chord interval,
`1−2m−β(m)≥19/160>0`, and the selected triangular branch applies. Exact
regression checks include these endpoint values.

The second proof of `β(m)≤ℓ(m)` using `H(m)` and a derivative estimate has
been deleted. The first positive-coefficient quartic-substitution certificate
is retained. Historical auxiliary algebra tests may still check the old
identity; they are not printed as a second proof in the paper.

## 5. Deletions and consolidations

| Former item | Action and reason |
|---|---|
| Four body/appendix pairs for common-pair domination, total endpoints, BC, and D | One statement and full proof per pair in the canonical paper; former labels remain aliases. |
| `D_fixed_witness_extensions.tex` | Deleted after its three full proofs were moved into their active results. No mathematical proof is lost with the file. |
| `lem:fixed-origin-in-hull` in the manuscript | Removed from the active BC route; retained in source 2612 for compatibility with older witness sets. |
| `prop:new-one-t3-terminal` and `prop:new-one-vd-assembly` | Replaced by one direct final assembly using midpoint placement, the original local adapters, D, replacement, and Vd2 length. |
| Old finite-witness summary table | Removed from both editions; its BC row still displayed the obsolete six-point recipe. |
| Generic `M_c(a)` definition | Removed after the active-reference check. The used `M_0(x)` and `M_c^{sup}` remain. |
| Unused CE2 total-slack lemma | Removed from both editions; center midpoint, boundary, and skeleton estimates remain. |
| Expanded `Q(s,δ)` polynomial | Replaced by its exact definition `Q=16P(3/2−s)` after the specified substitution; factored derivative and boundary value remain. |
| Center/vertex classification example galleries | Removed from the compiled editions; diagrams used by the proof and underlying gallery assets remain. |
| Stale six-point and separate-candidate descriptions | Corrected in structure, reading guides, and inline final routing. |

The compact variational definitions of the neighboring capacities are retained
because the common-pair lemma uses them. The removed object is the lengthy
aggregate type-aware maximum, not the validity of neighboring-ray control.
Other appendix interfaces are retained where they separate a structural
statement from a substantial calculation. This revision does not indiscriminately
delete every theorem wrapper or every explanatory figure.

## 6. Dependencies and preservation

The proof still has the acyclic order
\[
\mathrm{BC}\Longrightarrow\mathrm{N0}\Longrightarrow
\text{replacement contradiction}.
\]
Replacement is not used to prove N0. Both replacement charts, their positive
margins, and their skeleton-only scope remain. Raw `(3,0)` open/closed trace
normalization remains with its original preserved calculation. The original
T3-like and Vd1 supplier proofs retain their byte-hash checks. The full D
four-caliper proof is byte-identical to its former appendix proof, now located
under its theorem.

Actual uppercase reaches, selected lowercase demands, singleton gaps,
CE1/CE2 geometry, connected-component selectors, and open/closed endpoint
strictness are retained. The exact zero-gap certificate data, provenance,
transcript digest, derivation program, and positivity program are unchanged.

## 7. Interactive and verification changes

The dependency graph now uses the surviving primary statements. Its BC
geometric node depends on finite calipers, **not** on the capacity inequality;
the BC covering-application node explicitly carries that additional capacity
input. Uniform forcing depends on the clipped-radius corollary. Removed
assembly and origin-normalization nodes are no longer active dependencies.
The graph is regenerated, and its source links point to the delivery branch.
The standalone BC/D viewer explains the capacity-free threshold and identifies
its sliders as the capacity instance; its numerical calculations are unchanged.

The linked proof-tree snapshot remains a valid explanation of the specialized
BC/D arguments. Its immutable source links, existing rendered viewer, and
historical six-point animation provenance are not relabeled as new proofs.

`verify_reusable_lemmas.py` adds six exact identities plus ordered-domain and
source-interface checks. Existing audits are retargeted to moved/merged results,
not disabled. The graph checker rejects an accidental capacity dependency in
the pure geometric lemma and rejects missing capacity input in the covering
application. The old readability baseline is archived as
`arrange/_support/baselines/pre_reusable_lemmas_baseline.json`; the reviewed new
inventory is recorded separately. An inventory fingerprint is a regression
contract, not proof-assistant verification of the mathematics.

The canonical CI page guard changes from 73–78 to 68–72 to match the genuinely
shorter edition. Undefined-reference, overfull-box, exact-certificate, source
correspondence, PDF semantic comparison, and page-render checks remain enabled.
No font or margin change is used to meet the guard.

## 8. Validation and reproducibility

Local clean builds passed for both editions, with no undefined or multiply
defined references and no overfull boxes. Every page was rendered and scanned
for media-box clipping. The inline audit found 78 immediate proofs, accounted
for every statement/equation target, and matched 76 retained canonical proof
bodies. The full source check, both exact zero-gap programs, interactive source
check, proof-tree source/HTML check, and animated-guide asset check passed.

The local container cannot reach package registries. Its existing SymPy and
PyMuPDF match the pinned versions, but its plotting-library versions differ.
Consequently local regeneration of untouched trace PNGs did not byte-match the
pinned artifacts. Those incidental PNG changes were reverted. The publication
workflow repeats the checks with the repository's pinned Python/Node packages
and TeX Live 2025 image, rather than committing locally regenerated unrelated
trace images or claiming that the failed local byte-comparison passed.

Required checks include:

```bash
python proof/check.py
python arrange/_support/verify_inline_proofs.py
python arrange/_support/verify_readability_preservation.py
python interactive/generate.py --dependency-graph --check
python interactive/generate.py --trace-assets --check
python interactive/check.py
python interactive/proof_trees/check.py --html
python interactive/proof_trees/build.py --check
python interactive/animated_proof_guide/check.py --require-live
python arrange/build.py --all
python arrange/_support/verify_pdf_render.py arrange/_build/canonical.pdf
python arrange/_support/verify_pdf_render.py arrange/_build/inline_proofs.pdf
python arrange/_support/verify_inline_proofs.py --pdf arrange/_build/inline_proofs.pdf
git diff --check
```

The two certificate commands are run in the existing `3105X_computation`
directory. Publication uses an allowlisted, hash-checked branch-scoped delivery;
temporary transport files are removed from the final tree. Final remote checks
and publication identifiers belong in the delivery record below.

## 9. File-level inventory

The principal source changes are listed below. Paths are relative to the repository.

| Status | File |
|---|---|
| M | `.github/workflows/ci.yml` |
| M | `README.md` |
| M | `arrange/README.md` |
| A | `arrange/_support/baselines/pre_reusable_lemmas_baseline.json` |
| M | `arrange/_support/readability_baseline.json` |
| M | `arrange/_support/verify_readability_preservation.py` |
| M | `arrange/paper_draft/02_structure_and_common_geometry.tex` |
| M | `arrange/paper_draft/06_finite_enclosure_full.tex` |
| M | `arrange/paper_draft/07_exhaustive_assembly.tex` |
| M | `arrange/paper_draft/A_structural_shared_local_signed_center_optimization.tex` |
| M | `arrange/paper_draft/B_trace_length_optimization.tex` |
| M | `arrange/paper_draft/D_nonzero_gap_finite_enclosure_optimization.tex` |
| M | `arrange/paper_draft/E_zero_gap_nine_point_optimization.tex` |
| M | `arrange/paper_draft/fixed_witness/06_fixed_witness_body.tex` |
| M | `arrange/paper_draft/fixed_witness/D_bc_capacity_envelope.tex` |
| M | `arrange/paper_draft/fixed_witness/D_bc_finite_calipers.tex` |
| D | `arrange/paper_draft/fixed_witness/D_fixed_witness_extensions.tex` |
| M | `arrange/paper_draft/inline_proofs/02_common_geometry.tex` |
| M | `arrange/paper_draft/inline_proofs/03_trace_bounds.tex` |
| M | `arrange/paper_draft/inline_proofs/05_nonzero_gap.tex` |
| M | `arrange/paper_draft/inline_proofs/06_zero_gap.tex` |
| M | `arrange/paper_draft/inline_proofs/07_main_theorem.tex` |
| M | `arrange/paper_draft/inline_proofs/README.md` |
| M | `arrange/paper_draft/inline_proofs/main.pdf` |
| M | `arrange/paper_draft/inline_proofs/source_map.json` |
| M | `arrange/paper_draft/main.pdf` |
| M | `arrange/paper_draft/reading_guide/fixed_witness_logic.tex` |
| M | `arrange/paper_draft/reading_guide/geometric_overview.tex` |
| M | `arrange/paper_draft/reading_guide/selected_gap_walkthrough.tex` |
| M | `interactive/_support/generate_dependency_graph.py` |
| M | `interactive/bc_d_finite_calipers.html` |
| M | `interactive/check.py` |
| M | `interactive/readable_proof_dependency_graph.html` |
| M | `proof/0XXX_main/0003_reusable_lemma_catalog.md` |
| M | `proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md` |
| M | `proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2615_slack_sensitive_radial_envelope.md` |
| M | `proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2616_bc_d_finite_calipers.md` |
| M | `proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/26XX_index.md` |
| M | `proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/verify_bc_unification.py` |
| M | `proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/verify_editorial_order.py` |
| M | `proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/verify_paper_shortening.py` |
| A | `proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/verify_reusable_lemmas.py` |
| M | `proof/check.py` |

`A` means added, `M` modified, and `D` deleted. The report itself is an additional new file.

## 10. Delivery record

See the exported delivery copy for the final commit, PR, byte verification, and CI status.
