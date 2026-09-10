# Self-containment and editorial repair

Date: 10 September 2026

Branch: `chatgpt/paper-shortening-20260909141118` (PR #46).

Reviewed manuscript baseline: `56be06718a674bda1779ee6ed30d8571217f06cd`.

## Result and scope

The full manuscript has **69 pages**, including the proof appendices, and the
proof-free reading version has **37 pages**. These compare with 66/36 at the
shortening baseline and 89/50 before shortening. Fonts, margins, and page
sizes are unchanged. Necessary definitions and local justifications were
restored instead of forcing the paper to retain the 66-page count.

The raw `(3,0)->(2,0)` exact-trace normalization is retained. Its statement
and full calculation remain byte-identical under the existing regression
check. Both replacement templates are also byte-preserved. Optional A/B,
the old seven-point specialization, alternative one-Vd radial separations,
and the fifth-handoff corollary were not restored to the canonical paper.

BC still proves N0; replacement still invokes N0. Zero-gap configurations
still use F or cyclic area loss. Long proofs may follow their fully defined
statements in the appendices; notation is introduced before its use.

## 1. Definitions and reading order

The introduction defines the segment, convex-hull, interior, relative-interior,
length, positive-part, cross-product, trace, skeleton, and disk notation. The
least equilateral enclosure side `Lambda` is defined before the compact-margin
lemma. That lemma also states and proves the converse needed by candidate
obstructions: `Lambda(K)<1` gives containment in an open unit triangle.

Center-free edges, positive support, nonsupercriticality, midpoint suppliers,
and the names BC/D/F and N0 are introduced before the routing summary.
Actual reaches remain defined after exact-trace normalization.

The scalar diameter envelope `M_0(x)` and strict-supercritical envelope
`M_c^sup` are defined before their BC and D applications. The midpoint
`M_0` is distinguished from the scalar function `M_0(x)`. The finite-witness
table follows the constructions, so its symbols `Y`, `epsilon`, the frontier
points, and `K_F` are no longer forward definitions.

Appendix A puts the common corner chart and both orientation families before
the normalization and T3-like calculations. The support-cell and disk-caliper
statements are together. Appendix B introduces the Vd corner form before
using it in the skeleton caps. Appendix D defines outgoing capacities and
selected roots before the chord calculation and CE1 return; their fixed-point
application follows. Positional references such as a stale "preceding lemma"
are replaced by explicit references.

Figures are included in this reading-order review. The CE1 diagram follows
its second return bound; the four-contact diagram follows the tangent
residuals. The body zero-gap figure uses the already defined radial points
and disk rather than appendix-only notation.

## 2. Local versus global zero-gap notation

Appendix E uses `O_loc` for the corner origin and separately names its local
cone and feasible union. The hexagon center remains `O`. The conversion map

\[
\Psi_4(u,v)=V_4+u(V_5-V_4)+v(V_3-V_4)
\]

is defined before use. Its relationship with the local union explicitly
records the incoming/outgoing parameter exchange `(b,a)`. Actual handoffs
are written `X_i(xi_i)` rather than reusing the function `X_i` as an undefined
point.

The rescaled quadratics used for Newton's step are defined before their
quotients and derivatives. Newton vectors `A,B,C` are explicitly global
images under `Psi_4`; subsequent norms and cross products use those global
vectors. Their local anchor names have a delimited scope. The outgoing
functions in Appendix D are `mathcal Q_+` and `mathcal Q_-`, distinct from
the zero-gap frontier points `Q_+` and `Q_-`.

## 3. T3-like correction: the original supported interval

This correction is mathematical, not merely terminological. In the original
Type-II chart, let `0<t<1`, `z=sqrt(1-t+t^2)`, `alpha_T>0`, and `a=A_0`.
Direct substitution gives the actual interval on the forward radial segment:

\[
 c=\frac{1+\alpha_T+a-z}{1-t},\qquad
 u=a+t,\qquad \varepsilon=1-u.
\]

Setting `alpha_T=0` gives only a lower bound on the actual near endpoint.
The proof no longer identifies an endpoint of a translated closed majorant
with the endpoint of the original open covering role.

Put `x=a/(1-t)` and `theta=t/(1+z)`. Then

\[
 a+\varepsilon=1-t<1,\qquad
 \frac a{a+\varepsilon}=x,\qquad
 c=x+\theta+\frac{\alpha_T}{1-t}>x+\theta.
\]

The midpoint bounds give

\[
 \frac{1-4\theta+\theta^2}{2(1-2\theta)}<x<\frac12-\theta,
 \qquad 0<\theta<\frac12.
\]

The full feasible range is retained. For `theta<=1/5`, evaluate
`Q_theta(x)=2x^2+(theta-1)x+theta` at the lower endpoint, to the right of
its vertex. For `theta>=1/5`, use its positive unrestricted minimum.
Consequently

\[
 x^2+(c-2)x+c
 =Q_\theta(x)+\frac{\alpha_T}{1-t}(x+1)>0.
\]

The common ratio test supplies D's required inequality. Actual skeleton
coverage gives `C_1>=c`, and the O-side supported endpoint is the total
local frontier, hence is forced into the original open C triangle. The
fixed four-point D witness is unchanged.

The T3-like own-midpoint exclusion needed by the supplier lemma is now
proved explicitly. Positive forward support gives
`beta<(z-z^2)/t<(1-t)/2`, so the midpoint violates the Type-II side
inequality. The identity

\[
 t(1-t)-2(z-z^2)=(1-z)^2>0
\]

justifies the strict comparison. Neither translation nor altered actual
reaches are needed for this exclusion.

## 4. Other local proof justifications

### Strict-supercritical envelope

The envelope is derived from the selected admissible cell using

\[
 F_S(1-M,M,c)=M(c-M)(1-2c+cM-M^2),\qquad
 \partial_mF_S(m,M,c)=2c(M^2+cm)>0.
\]

The proof handles `c=0` separately and excludes `c=1/2` through the
self-midpoint result. The continuous endpoint convention is not an assertion
of an attainable strict-supercritical triangle.

### Vd1 orientation and size

A Vd1 role supplying the prescribed forward midpoint has `t>=1`: for `t<1`
the opposite adjacent trace would also have positive length. This fact is
proved before restricting to that chart range. The supported-tail adapter
also explicitly proves `a+epsilon<1`, and justifies the signs in its scalar
inequality before and after squaring.

### CE1 selected chords

The selected boundary function is distinguished from a subsequent actual
handoff: the latter satisfies an inequality, not an unjustified equality.
The proof derives monotonicity and concavity and proves the chord estimates
on both radial ranges needed by CE1. The first-step lemma still requires
only the radial demand at T4. BC recovers the third demand before invoking
the complete return. Selected-state estimates are not promoted to statements
on the bare signed CE1 domain.

## 5. Reference types, layout, and certificate exposition

Aliased counters retain one numbering sequence while giving automatic
references their correct names: lemma, proposition, corollary, definition,
and remark. The geometry figure is closer to its definitions; the V-type
gallery follows the reach/gap/support definitions. This removes an avoidable
sparse introductory page without shrinking the text or figures.

Appendix F defines the Bernstein basis and its nonnegative partition-of-unity
property before using the coefficient certificate. It explains exact sign
comparisons over `Q(sqrt3)` and identifies the electronic appendix at an
immutable repository revision. The PDF contains the mathematical reduction
and checking rules; the sparse data and programs are included in the source
package, not printed in full in the PDF. This electronic dependency is now
explicit rather than hidden behind repository provenance wording.

## 6. Source synchronization and regression protection

The numbered sources `1201`, `2014`, and `4130_new` are synchronized with the
T3 own-midpoint, Vd1 orientation/size, and actual T3 interval/ratio arguments.
The historical optional proof archive is otherwise retained.

`verify_editorial_order.py`, invoked by `proof/check.py`, checks **30 targeted
reading-order/reference contracts** and **26 exact algebraic identities and
sign reductions**. Its T3 test includes `t=7/10`, outside the previously
restricted translated range. This is not a universal natural-language
first-use parser or proof-assistant formalization.

All **60 existing BC symbolic checks** remain. Two intended pins are updated:
the D body sketch, which no longer uses signed parameters prematurely, and
the repaired numbered T3 source. The normalization blocks, replacement
construction, geometric D statement, and electronic certificate remain
protected. No exact zero-gap data shard or verifier is changed.

## 7. Validation and publication protocol

Local proof/interface checks, the 30/26 editorial regressions, generated graph
checks, and interactive checks pass. The local 69-page and 37-page LaTeX builds
pass undefined-reference, duplicate-label, and overfull-box checks, as well
as the all-page PDF render audit.

The publication workflow uses the repository's pinned dependencies and
TeX Live 2025 image. It replays both exact zero-gap verifiers, checks trace
assets, rebuilds both PDFs, and verifies the delivery manifest before a
non-forced branch push. Ordinary PR CI then checks the final cleaned commit,
including a fresh canonical rebuild and comparison with the tracked PDF.
Final commit identifiers and completed CI results are recorded in PR #46
and the delivery verification file, rather than predicted in this report.

These checks validate the refactoring contracts and replay the certificate;
they are not formal verification of every geometric argument.
