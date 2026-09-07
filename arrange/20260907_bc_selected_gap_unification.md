# Unified B/C selected-gap proof

Status: Reference

This report describes the B/C-only refactor based on main commit
`c9e8269a7989cab1cb108af70801240113b3e51b`. Numbered Proven sources,
not this report, are the mathematical authorities. D is unchanged.

## Mathematical change

The active nonzero-gap path constructor is now

\[
K_{BC}=\{M_0,X_0(B_0),X_0(1-A_1),\widehat P_2,\widehat P_3,\widehat P_4\}.
\]

Its pure enclosure theorem explicitly assumes an actual selected gap
$J_0$, five nonsupercritical path roles, the four middle strict handoffs,
and $B_5\ge B_0/2$. It does not assume that the opposite incident edge
is gap-free. The origin lies in the convex hull of a boundary witness and
the two total endpoints on $r_2,r_4$; no seventh point or disk is added.

The new numbered source `2018b` proves the missing boundary input from
original perimeter coverage. Write $G=X_0(B_0)$ and $L=X_5(B_5)$.
Then $G\in T_0\cap U_C$ and $L\in U_0\cup U_C$. A common unit triangle
contains one point openly and the other in its closure, so

\[
B_0^2+B_0(1-B_5)+(1-B_5)^2<1,
\qquad B_5>1-M_0(B_0)>B_0/2.
\]

This is a fact about the original configuration. We do not require an
arbitrary candidate containing the six witnesses to cover the unselected
gap. The pure theorem keeps the scalar tail premise because dropping
both that premise and perimeter coverage would give a false statement.
The exact regression script includes the previously constructed example
showing that the omitted opposite gap matters.

For any candidate, the selected endpoints give $B_0>2Q$, $A_1>X$.
The tail premise gives $B_5>Q$, and the four middle handoffs propagate
$A_i>X$, $B_i>Q$ throughout $T_1,\ldots,T_5$. The former squeeze on
$A_0$ and the fifth handoff are not needed by BC.

CE2 uses the existing transverse threshold dichotomy. CE1 uses the
existing selected calculations in tail-input form, starting at $B_4\ge Q$.
The sequence is still: recover the own demands at $T_4,T_3$; apply only
the first selected step; exclude neighboring supply at $r_2$; recover
$C_2$; apply the full return. In particular, the late $\delta<1/10$ bound
remains conditional. The older five-handoff $A_0$ return remains a corollary.

## Paper and interface changes

The body table has three active constructors: BC, D, F (at most 6, 4, 9
points). Either actual gap can be selected and reflected to $J_0$; only
that gap's endpoints are in $K_{BC}$. Singleton endpoints may coincide.

The former four-point B theorem and its short-ray proof are retained in
Appendix D as an optional refinement, not as a dependency of N0. Optional
A is likewise retained. The center-aligned theorem, N0, main assembly,
source catalog, and generated graph all use BC without a gap-count split.
The CE1 reverse-path figure now starts from the shared-anchor tail input.

The local preview has 89 pages, versus 88 in the preceding compressed
paper: the new scalar premise and transfer proof are explicit, and the
optional four-point B refinement is retained. The existing 86--90-page
CI contract is unchanged. The goal here is one active point construction,
not deletion of the useful independent B proof or explanatory prose.

## D and other invariants preserved

D's geometric four-point theorem, fixed witnesses, adapter, two local
rescuer proofs, and manuscript proof blocks are byte-identical to the
baseline. The replacement source is also unchanged. The new regression
script checks these exact hashes and block boundaries. Total radial
endpoints remain defined by all actual permitted contributions; they do
not become candidate-dependent when a role is supercritical.

Original open roles and their closed classifications, actual maximal
reaches, singleton gaps, selected components, both replacement charts,
and the exact zero-gap certificate files are preserved.

## Validation and delivery requirements

`verify_bc_unification.py` contains 60 exact algebraic/interval checks and
additional source-hypothesis/D-preservation regressions; `proof/check.py`
invokes it. These tests do not substitute for the inherited geometric
proofs. The interactive checks require BC/D/F and verify that the N0
closure includes the shared-anchor lemma but excludes optional A and B.

Run the full source, generated-graph, trace-assets, interactive, exact
zero-gap, pinned manuscript build, semantic PDF comparison, and render
checks before delivery. A local unpinned graphics regeneration differed
from the tracked trace PNGs; those files were restored unchanged. The
pinned dependency install is unavailable on the sandbox's DNS-restricted
network, so the authoritative reproduction is the pinned GitHub Actions
run, not a relaxation of the asset checks.

Publication follows AGENTS.md: validate immutable files, create remote
blobs and a tree, create a child of the current feature head, and advance
the branch without force. Final verification must inspect the remote
head, changed paths/modes/digests, absence of transient workflows, PR, and
checks associated with that exact head. A green transport job alone is
not publication.
