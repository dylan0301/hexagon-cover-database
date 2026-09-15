# Enclosure key lemmas: editorial and mathematical report

Base: `1d603a69ad97b6a9c32cb0dc4aa6e6747632f3a1` (main, 14 September 2026).
Branch: `chatgpt/enclosure-key-lemmas-20260914140239`.

## Assessment

The finite-candidate minimum-equilateral-enclosure theorem is the central
general tool of this strategy. It belongs in the main text, together
with the support-function gauge and the support-cell argument that
explains why the continuous orientation search is finite. However,
witness forcing and case-specific structural reductions are not merely
auxiliary algebra. The three logically distinct obligations are:
construct one fixed set from the original configuration; prove that
every hypothetical C triangle contains it; and exclude every unit
enclosure of that same set.

## Implemented relocation

The complete four-result block, with all four proofs, was moved from
Appendix A into the beginning of the canonical finite-enclosure chapter:

1. Equilateral enclosure gauge (`prop:new-enclosure-gauge`, also
   `prop:universal-enclosure-gauge`).
2. Support-cell rotation (`lem:support-cell-rotation`).
3. Finite caliper certificate (`thm:cert-caliper`).
4. Disk--finite-set calipers (`prop:new-disk-finite-caliper`).

All mathematical statements, proofs, and established labels are retained.
The appendix now points to the main-text tools before applying them to
the exact local admissible set. It retains only short gauge formulas
as a local reminder and for the existing source-interface check. No
validation script or preservation baseline is relaxed. The alternative
inline-proofs edition already has no appendices and is left
mathematically unchanged.

An explicit disk-plus-one-point example and its elementary derivation
were added in prose from the proved source `2608`, Section 2. This
specialization was not an active named theorem of the current canonical
manuscript, so it is not described as a relocated existing theorem.
BC and D remain the current six-point and four-point constructions;
no discarded seven-point specialization or disk-based nonzero-gap
argument has been restored.

## Important qualifications

The finite list consists of orientations (normal triples); the tight
support triangle is then determined. It is not a list of all optimal
triangles. On each fixed-support angular cell, a positive sinusoidal
part has negative second derivative, excluding an interior minimum;
an all-disk cell is constant. This is the reason finitely many
support changes suffice.

The disk-only value is valid only when an orientation actually realizes
three disk supports. It cannot be inserted as an unconditional lower
candidate. The new explanatory paragraph makes this qualification
explicit without changing the preserved proposition. Including one
reference normal along with all tie normals is a complete finite test.

Checking each disk-plus-one-point set separately is insufficient for
several points. For example, each of the two points at distance 2r on
opposite sides of a diameter has individual enclosure side 2sqrt(3)r,
while their union has diameter 4r > 2sqrt(3)r.

## Other key structure already in the chapter

Fixed radial forcing and demand recovery, common-pair domination, and
uniform common-pair forcing are the main construction interfaces. They
account for actual adjacent V traces, openness, and strict endpoint
demand recovery. They must remain visible in the main text.

BC's selected-gap enclosure and shared-gap-anchor transfer preserve
the quantifier order: original V data are fixed before a new candidate
is chosen. D's four-point rescuer theorem is a reusable geometric
obstruction, not merely an algebraic bound. F additionally needs the
Newton inner inclusion and four-contact hull geometry. The new main-text
explanation distinguishes that reduction from the finite-candidate
theorem and preserves the exact tangent certificate's role.

The polynomial selectors for the local admissible set, detailed CE1/CE2
return calculations, first-root coordinates, supporting-line residuals,
and exact tangent-certificate algebra remain in the appendices.
Moving general tools forward is not a claim that these calculations
are optional, routine, or automatically implied by the caliper theorem.

## Validation policy

The existing formal-statement/proof preservation inventories and numbered
proof-corpus fingerprint are not reset. The delivery runs the repository
proof, inline-order, preservation, exact-certificate, dependency-graph,
trace, interactive, PDF-render, and pinned-publication checks. Updated
generated dependencies and the canonical PDF are included only after
validation. Read-only validation and branch-limited publication are
separate jobs; publication checks an allowlist and byte hashes and
removes this temporary workflow. Final remote CI status must be read
from GitHub rather than inferred from this report.

## Completed validation

All validation steps preceding packaging passed: the pinned builds of both editions; PDF render checks; identical inline-edition text and 144-dpi pixels; all 186 canonical statements and 184 proof groups preserved; the 446-file numbered proof/support fingerprint; exact-certificate checks; and dependency/trace regeneration and static checks. The dependency graph is staged before its freshness check, and packaging compares against HEAD so this staged generated file cannot be omitted. No check script or mathematical baseline was weakened. Remote publication is still separately gated by the hashed manifest and branch-head check.

## Final notation review

The appendix reminder now explicitly defines W_K as the three-direction support sum before using it. This is a notation clarification outside the preserved formal statements and proofs. The main-text four-result relocation is unchanged. Both editions and the final checks are rerun after this clarification.

All final validation steps passed after the notation clarification. The canonical PDF has 76 pages. No formal statement, proof, numbered proof/support file, checker, or preservation baseline was changed.
