# Zero-gap nine-point unification

Status: Implementation report; not a proof authority

Date: 2026-09-05
Audited base: `cc4aa455b1aa174accdfd891b0691ff9c26e721d`
Feature branch: `chatgpt/unify-zero-gap-20260905080358`

## Result and exact scope

The active zero-gap theorem now closes the entire row

\[
N_{\rm gap}=0,\qquad N_+=1,
\]

for arbitrary normalized V types, independently of the C-triangle class.
The actual criticality test remains `A_i+B_i>1`; selected lowercase reaches
remain explicitly bounded by the actual uppercase reaches. Singleton gaps
are still gaps. No claim is added for multiple supercritical roles or for
nonzero boundary gaps.

The nine geometric witnesses, the two-parameter domain, and every exact
mixed-overlap certificate are unchanged. This is a strengthening of the
forcing step and of the theorem's scope, not a new enclosure computation.

## Shared proof mechanism

Strict full-boundary handoffs with unique supercritical index 4 give

\[
x_3<x_2<x_1<x_0<x_5<x_4,\qquad
a=1-x_3,\quad b=x_4,\quad p=1-b,\quad q=1-a.
\]

Every selected pair dominates `(p,q)`. Convexity therefore permits
reselecting **all** boundary lower bounds as this common pair. Set
`c_*=c_max(p,q)`. The existing common-pair domination theorem gives

\[
C_+(p,q),C_-(p,q)\le1-\min(p,q)\le c_*.
\]

Each type-aware maximum contains the own-ray term `c_*`, and every actual
permitted neighboring term is at most `c_*`. Thus every maximum is exactly
`c_*`. The shared forcing lemma excludes the same six symmetric points
`(1-c_*)V_i` from all open V roles. Full coverage puts them in the open
C triangle, whose convexity gives the same centered disk.

The three asymmetric frontier points are excluded by the strict
supercritical frontier and distances from contained vertices and actual
handoffs. Those arguments never require Vd0 locality. The existing exact
terminal inequality and compact-open shrinking contradiction then apply
without any change of coordinates or certificate.

An additional paragraph in `2608` records the equivalent convexity
uniformization with varying selected pairs: if their maxima are
`Gamma_i<=c_*`, the symmetric point is the convex combination of
`(1-Gamma_i)V_i` and `O` with coefficient `(1-c_*)/(1-Gamma_i)`. The active
proof uses common-pair reselection because it directly proves V-role
exclusion as well as C-role containment.

## Numbered proof sources

| Source | Change |
|---|---|
| `2608` | Adds uniform common-pair radial forcing, preserving actual neighboring-support selection and the strict noncentral condition. |
| `31051` | Generalizes direct radial forcing; keeps the own-role and nonlocal explanations and replaces only the Vd0-specific adjacent-role step. |
| `31058` | States the type-independent zero-gap theorem and updates the dependency audit. |
| `31059` | Broadens the CE0 consequence to every normalized V type. |
| `31050` | Synchronizes package scope, dependencies, and historical attribution. |
| `2610` | Makes Terminal F type-independent and connects it to the common radial engine. |
| `0000`, `0001`, `0003` | Synchronizes final routing and source ownership. |
| `2400` | Identifies its one-ascent special-type argument as an independent alternative; retains its proof. |

Historical filenames and directories are retained to avoid breaking links.
The earlier all-Vd0 direct route remains in `3104X`. The Vd1/Vd2 length
proofs and T3-like area proofs have not been deleted or weakened.

## Paper and reader-facing changes

The three former zero-gap `N_+=1` refinements are merged into one arbitrary-
V-type row. The other zero-gap rows remain `N_+=0` (length) and `N_+>=2`
(area). Nonzero-gap hypotheses, CE1/CE2 distinctions, and replacement charts
are not changed.

The finite-enclosure body contains the new uniform forcing corollary and a
short proof explaining why adjacent crossings leave the six symmetric
coordinates unchanged. Appendix E retains the exact scalar bounds and
makes the `C_+,C_-` adjacent-role exclusion explicit. The public nine-point
statement, final assembly, case register, roadmap, and figure caption are
synchronized. The length and area chapters explain which arguments remain
short independent alternatives.

The dependency-graph generator and generated page have the same unified
row and the new shared-lemma dependency. Its routing identifiers are now
R0--R11 instead of R0--R13; these are navigation labels, not mathematical
notation. No sampled geometry or trace-envelope asset is changed.

## Source regression guard

`proof/check.py` now checks that the public zero-gap obstruction has both
required hypotheses and has not regained an all-Vd0 restriction, that the
new corollary has exactly one label owner, that Appendix E cites it, and
that the introduction has one zero-gap `N_+=1` routing row. These are
source-consistency checks, not a formal verification of the mathematics.

## Preserved exact material

The numbered sources `31052`--`31057`, certificate data modules, derivation
and positivity programs, and provenance file are byte-for-byte unchanged.
The expected core-polynomial transcript SHA-256 remains

```text
dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485
```

## Validation and publication protocol

Local source and interactive checks pass. The local canonical build produces
92 pages, with no undefined or multiply defined references and no overfull
boxes; all pages pass the repository render audit. The new corollary and
terminal theorem have also been visually inspected. The local derivation
replay exceeded the sandbox command limit, and local dependency versions do
not exactly match the pinned CI requirements; neither is represented as a
successful pinned verification.

Before publication, the branch-specific read-only validation job must install
the repository's pinned dependencies, replay both exact zero-gap programs,
regenerate and check the graph, check trace assets and interactive pages,
rebuild in pinned TeX Live 2025, and validate the complete changed-path and
byte-digest manifest. The resulting PDF and exact prospective tree are
exported for inspection. Publication uses a fresh guarded job, executes no
repository or artifact code, and accepts only that independently sealed tree.
The permanent CI workflow is unchanged; the final pull request checks the
exact delivered content. Temporary delivery files are removed before the
pull request is opened.

The companion delivery report and GitHub checks record the final remote
commit and actual pinned-validation results, rather than inferring success
from this source-level implementation report.
