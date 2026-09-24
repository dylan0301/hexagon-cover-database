# Case F fixed-start explicit-comparison integration

## Revision and scope

Base: `e255ed51d54c3f005dc9c5764e8ee3736cd06946`.
Delivery branch: `chatgpt/f-explicit-comparison-20260923155000`.

This revision integrates the complete sequence of Case F simplifications,
not only the last four quadratic models. The exact nine forced points,
the actual forced disk, the strict AB frontier, the type-independent forcing,
and the general four-contact geometry retain their roles.

The paper's two editions share one current certificate body. Their source
comparison, immediate-proof order, and no-forward-dependency audits remain
active. The former baseline inventories are archived rather than silently
removed. The manuscript and proof-corpus baseline is intentionally advanced
only for this documented revision; the source manifest fingerprints the
unchanged historical certificate files.

## Mathematical changes

1. The moving adjacent-triangle signs use normalized two-coefficient identities
   and the fixed parameter `k=1/2`, not expanded junction polynomials. Root
   ordering is strengthened, and coordinate positivity is explicitly justified.
2. The inner comparison points use the fixed-start Newton formulas. They remain
   strictly between the junction and original frontier witnesses by convexity.
   They are not new individually forced witnesses.
3. One rational Newton deficit and a convexity/chord proof produce
   `e0=max(r,m-kappa U)<=1-c*` across both capacity branches. An undefined `q`
   in a preliminary radius-lemma typesetting draft is corrected to `omega`.
4. The active tangent proof uses a single ordered residual and a radical-free
   polynomial. A cubic endpoint comparison proves `B(m,U,b0)>4` uniformly;
   four quadratic models prove the mixed-derivative bounds. The curvature
   comparison uses the affine slope `(1+5m)/2` and a cubic lower model.
5. Exact Chebyshev reconstruction and rational coefficient budgets replace
   separately supplied SOS/Bernstein witnesses. The increment comparisons,
   norm-order proof, radius transfer, and boundary Taylor argument are included.
6. The actual disk remains in every exposed-hull and straight-line argument.
   The smaller radius is used only for initially proving the tangent residuals.

This remains a **computer-assisted proof**. Five explicit-model checks process
383 Chebyshev coefficients; curvature uses 113, and the two increment comparisons
use 208 nonconstant coefficients. Other exact identities and the degree-27
boundary Taylor work are additional. These are not total operation counts.
The result is not described as a computer-free proof or a formal verification
of the upstream geometric lemmas.

## Proof and publication ownership

The active numbered authority is `3105b_explicit_comparison_enclosure.md`.
`31052` supplies the shortened moving-circle proof, and `31057` assembles the
current terminal result. `31054`--`31056` and the two original exact programs
are preserved as explicitly historical alternatives for their old comparison
points. Their data are not relabeled as certificates for the fixed-start points.

The active program is `3105X_computation/verify_explicit_stage.py`, with the
colocated `mathematical_supplement.md`. It takes no coefficient-witness input.
The supplied latest verifier was rerun before integration, and CI adds a fresh
replay alongside both original exact programs. The source checker binds the
program hash and the unchanged historical files to the integration manifest.

## Interactive material

The new offline `interactive/f_explicit_comparison.html` shows the fixed-start
points, unchanged frontier witnesses, and actual disk. A Node diagnostic checks
2,401 valid configurations for implementation consistency; it is not evidence
of the universal theorem. Proof trees and the dependency graph refer to the new
active source. The older F cap-chain explorer and GIF captures are labeled
historical, not silently presented as the current point construction.

## Validation

The delivery workflow separately applies the source revision, regenerates the
proof-tree/dependency artifacts, replays all exact certificates, and rebuilds
both manuscripts using the repository's pinned TeX Live 2025 image. Only an
allowlisted, hash-checked artifact is eligible for publication. The publication
job does not execute the proof payload and cannot write to main. Workflow-file
finalization and temporary delivery cleanup use the connected GitHub actions.

The associated generated validation record identifies the checks actually run.
Publication is confirmed only after the remote branch and its final files are
read back. A queued CI run is not reported as passing.

### Local pre-publication results

The integrated active exact calculation passed, as did both unchanged historical
zero-gap programs, the numbered-source interfaces, the statement/proof-order
audit, the reviewed mathematical inventory, the offline proof-tree renderer,
and the new viewer's 2,401 numerical implementation diagnostics. The two local
manuscript builds have 69 and 67 pages respectively and no overfull boxes or
unresolved references. All pages passed the PDF render scan; the affected F
pages were also rendered for visual inspection. The final published PDFs are
rebuilt separately in the repository's pinned TeX environment.

Local trace-asset regeneration changed PNG bytes under the container's different
Matplotlib installation. Those unrelated image changes were discarded; the
pinned CI regeneration remains the authoritative check. A local failure of this
byte comparison is not reported as a passing pinned regeneration.
