# Paper shortening: implementation report

Date: 9 September 2026
Repository: `dylan0301/hexagon-cover-database`
Base: `908f81032cbf582b3be22f18a61f51746ef0196c`
Branch: `chatgpt/paper-shortening-20260909141118`

## 1. Result and scope

The canonical paper is shortened from **89 to 66 pages**, a reduction of
23 pages (25.8%). The proof-free rendering is shortened from **50 to 36
pages**, a reduction of 14 pages (28.0%). The document class, font sizes,
page dimensions, and margins are not reduced.

The active TeX input closure decreases from 29 to 23 sources. Its theorem,
lemma, proposition, and corollary environments decrease from 130 to 95.
These counts include the appendices but not the separate numbered proof
archive. Removing wrappers does not mean removing 35 independent proof steps.

All three requested editing passes were implemented **except** the proposed
change to the raw `(3,0)` classification. The raw `(3,0)` to `(2,0)` exact-trace
normalization, its original statement, and its full calculation are retained.
The new regression test verifies those statement/proof blocks byte for byte
against the audited source.

The changes concern the canonical manuscript, publication documentation,
its generated dependency graph, and the regression checks that refer to its
presentation. No numbered mathematical proof source or exact certificate
program/data file is deleted or rewritten. Historical alternatives remain
available in the proof archive, but they are not compiled into this paper.

## 2. Removed inactive arguments

### Optional A: complementary-gap disk

Removed its one-gap common-pair adapters, witness construction, complementary-
gap theorem, disk-plus-one-point formula, specialized calculation, and figure
inputs from Appendix D. The general disk--finite-set calipers remain because
F uses them. N0 continues to depend on BC, not on A.

### Optional B: four-point two-gap refinement

Removed `fixed_witness/optional_B.tex`, its two-gap candidate adapters, the
fixed four-point two-gap proof, and its CE2 short-ray calculation. The active
CE2 transverse thresholds inside the BC proof remain intact.

### Older seven-point specialization

Removed the `K_tr` construction with own endpoints, the endpoint-upper-squeeze
lemma, and its specialized CE2 calculation. BC still uses the six-point fixed
set with **total** radial endpoints, not own endpoints.

### Alternative one-Vd separation calculations

Removed the old residual-tail definitions and adjacent/nonadjacent separation
proofs. Removed their exclusive small-slack and one-third radial-envelope
helpers. The active Vd2 adjacent-midpoint **perimeter** cap remains. The active
Vd1 supported-tail adapter following the old subsection was retained.

### Retained fifth-handoff corollary

Removed the optional five-handoff return. The active tail-input CE1 obstruction
and all selected-component calculations remain. Its first return step now has
an independent statement, as described below.

## 3. Repeated definitions and proof summaries

The distinct-role proof is given once. The gap lemma is the common owner of
open trace endpoints, the exact gap interval, singleton gaps, boundary locality,
and C-triangle forcing. The separate generic open-trace-endpoint lemma was
removed: its unrestricted statement confused a genuine exit with an endpoint
of a truncated segment. The stronger, application-correct total-endpoint proof
remains.

The repeated structural-routing proposition, old perimeter case registers,
repeated zero-gap branch proposition, and final nonzero-gap wrapper were
removed. The routing table and the short final proof remain. The skeleton-count
sum is now proved directly in the body, rather than repeated in an appendix
lemma. The boundary-trace statement lists the bounds used by the active route.

The local area theorem is stated pointwise for a containing triangle, avoiding
an unused feasible-family/infimum layer. The short cyclic square-completion
proof is in the body. Its two-ascent strictness and strict handoff selection
are unchanged.

BC has one six-point enclosure statement with its forcing conclusion, and one
appendix proof with separate CE1 and CE2 parts. Several short theorem-sized
wrappers around that proof were removed. The D construction has one common
passage from the local endpoint/ratio bounds to the four-point enclosure.
The T3-like and Vd1 chart calculations still verify their distinct local inputs.

Zero-gap coordinates are derived once in Appendix E. The body gives the
geometric construction and its witness set instead of repeating all radicals
and frontier coefficients. The selected first roots, their existence/order
proofs, and the exclusions against moving handoff points remain. The smaller
rational comparison radius is introduced in the certificate appendix only.
The repeated Newton-inclusion subsection was merged into the original Newton
lemma.

Unused generic quartic-clause enumeration was removed from the finite caliper
theorem. The finite geometric caliper criterion itself remains. Historical
wording such as “old,” “former,” and “unchanged” was reduced where it described
a revision history rather than a mathematical hypothesis.

## 4. Structural proof consolidations

### 4.1 Self-midpoint obstruction from the admissible set

For the supercritical cell, with `m=min(a,b)` and `M=max(a,b)`, use

\[
F_S(m,M,c)=(m^2-1)c^2+(2mM^2+M)c+M^4-M^2.
\]

The two identities are

\[
4F_S(1-M,M,1/2)=M^2(2M-1)^2,
\qquad
\partial_m(4F_S(m,M,1/2))=2m+4M^2.
\]

Since `a+b>1` means `m>1-M`, they give `F_S(m,M,1/2)>0`, contradicting
admissibility. This replaces the separate four-edge caliper calculation.
Both identities are checked by exact symbolic expansion. The positive-margin
refinement is retained.

### 4.2 First CE1 return step

`lem:ce1-first-return-step` assumes the signed CE1 domain, the nonsupercritical
boundary path, the tail floor at T4, and **only** the own-radial demand at T4.
It concludes that the reflected T4 state is selected Q+ and

\[
B_3>L_1=(2-4\alpha)Q-(1-4\alpha)\alpha.
\]

BC then uses the retained identity

\[
R(L_1-\delta)
=(1-2\alpha)\eta+(W-2\alpha)(\alpha+\delta)+4R\alpha^2>0
\]

to exclude both neighboring contributions on r2 and recover `C2>1-delta`.
Only then is the full CE1 return invoked. This replaces references to an
unnumbered part of another proof without assuming a radial demand in order
to prove it. The conditional selected-state estimates, including the eventual
`delta<1/10` bound, are not promoted to claims on the bare signed domain.

### 4.3 Shared corner and support calculations

A single corner-chart lemma gives the wedge reduction, the metric
`x^2+y^2-xy`, and the normalized area Jacobian. The two orientation families
are defined once in Appendix A and reused for area loss. Closed containment
is allowed in the shared chart; strict interior slacks for the original open
roles remain explicitly separate.

The support-cell rotation lemma is colocated with the enclosure gauge and
finite caliper criterion. It supplies both polygon and disk applications.
The exposed-four-contact argument for F remains separate: generic calipers
alone do not justify discarding the other candidate contacts.

A single compact-cover-margin lemma now supplies both the scaling equivalence
and the compact-open enclosure contradiction.

## 5. Preserved mathematical contracts

The following remain explicit:

- Original open roles `U_C,U_i` and closed roles `T_C,T_i`; actual uppercase
  reaches and selected lowercase lower bounds.
- Raw `(3,0)` exact-trace normalization before reach definitions.
- Singleton gaps and strict overlap inequalities.
- BC's original-configuration tail premise `B5>=B0/2`, supplied by the
  shared-gap-anchor transfer before choosing any candidate.
- Fixed witness coordinates, including total radial endpoints and the
  origin-in-hull identity.
- Separate CE1 and CE2 candidate sign domains and geometric root selectors.
- Both Vd1 replacement charts, all strict margins, and skeleton-only coverage.
- N0 depending on BC; replacement invoking N0, not conversely.
- Both distinct rescuer chart inputs and the common four-point theorem.
- All moving-handoff exclusions, Newton inner points, four exposed contacts,
  paired radius transfer, exact certificate data, and both exact verifiers.

The compact disk in F is contained in the hull of the forced radial points;
its interior is not asserted to be pointwise missed by all V triangles.
Replacement is not claimed to preserve the whole hexagon or the input gap rank.

## 6. Page locations in the shortened rendering

| Part | Old start | New start |
|---|---:|---:|
| Common geometry | 6 | 5 |
| Trace-length mechanism | 10 | 9 |
| Area loss | 13 | 11 |
| Finite enclosure | 15 | 13 |
| Completion | 26 | 21 |
| Appendix A | 28 | 22 |
| Appendix B | 38 | 32 |
| Appendix C | 45 | 35 |
| Appendix D | 47 | 36 |
| Appendix E | 72 | 50 |
| Appendix F | 85 | 62 |

These are section starting pages; adjacent parts can share a page. The largest
reduction is the removal of inactive material from Appendix D. The exact
certificate remains five pages from its starting page through the end.

## 7. Validation and publication checks

The local source audit, interactive audit, full build, proof-free build, and
66-page render scan pass. All 66 canonical pages were rendered and visually
reviewed in contact sheets; the witness table, new CE1 step, and self-midpoint
corollary were also inspected at higher resolution. The builds reject undefined
references, multiply defined labels, and overfull boxes.

Both exact zero-gap programs pass and reproduce the preserved transcript digest:

```
dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485
```

The existing four-contact, fixed-witness, compression, and BC exact checks remain.
`verify_paper_shortening.py` adds the two self-midpoint identities, byte-preserved
normalization and replacement checks, and CE1 dependency-order regressions.
The D preservation checks now hash its unchanged theorem/proof blocks rather
than the surrounding duplicated prose; the numbered D sources stay pinned.

The dependency graph is regenerated from the shortened manuscript. Its audit
requires the new shared lemmas and first return step, rejects retired alternatives,
and retains its missing-node and directed-cycle checks. The CI page-count guard
is updated from 86--90 to 64--68; no validation command is removed.

Local Python uses the exact pinned SymPy and PyMuPDF but different plotting/
Markdown versions; the offline environment cannot install the full pinned set.
The publication workflow therefore uses the repository's pinned Python packages
and pinned TeX Live 2025 image for generated assets and release PDFs. It must run
all required checks before publishing, and verify the delivery manifest's paths,
modes, and exact byte hashes. Final CI state is reported with the pull request.

These tests validate the refactor and replay the certificate; they are not a
claim of proof-assistant verification of every geometric argument.
