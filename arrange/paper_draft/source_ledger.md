# Paper Source Ledger

This ledger records the sources assembled into the consolidated manuscript and
the numbered proof objects supporting them. It is a maintenance document, not
an additional proof.

## 1. Publication architecture

The printed proof is a single mathematical narrative rather than a short
reader summary followed by a second technical manuscript. Its active sections
are:

| File | Printed function |
|---|---|
| `01_introduction.tex` | theorem, canonical labeling, finite types, routing table |
| `02_structure_and_common_geometry.tex` | structural reduction, handoffs, midpoint facts, signed center geometry |
| `03_trace_bounds.tex` | Strategy 1: complete perimeter and skeleton trace argument |
| `05_area_loss_full.tex` | Strategy 2: complete local and cyclic area-loss proof |
| `06_finite_enclosure_full.tex` | Strategy 3: residual-hull principle, exact nonzero-gap reach certificates, and explicit nine-point enclosure |
| `07_exhaustive_assembly.tex` | final exhaustive application of the routing table |

The exact mixed support-arc certificate remains a printed appendix. Repository
formalization registries, parameter dictionaries, and provenance manifests are
retained as source and verification infrastructure but are not separately
typeset when their mathematical content has already been incorporated.

### Technical appendices

| File | Function |
|---|---|
| `04_strategy2_verification.tex` | legacy-named exact local-reach certificate assembled inside Strategy 3 |
| `06a_strategy4_exact_certificate.tex` | exact unequal-radius support-arc certificate printed as Appendix A |

The body-end label occurs immediately after the seven proof sections and
immediately before `\appendix`.

## 2. Assembly map

`02_structure_and_common_geometry.tex` demotes and incorporates
`02_structural_reductions.tex` and `04a_signed_center_calculus.tex`.

`03_trace_bounds.tex` incorporates `03_strategy1_length.tex` and
`04b_common_CE1_CE2_budgets.tex`.

`05_area_loss_full.tex` incorporates `05_strategy3_area.tex` under the new
Strategy 2 numbering.

`06_finite_enclosure_full.tex` incorporates the residual-hull principle,
`02a_universal_calculus.tex`, the signed-center local-reach interface,
`04c_short_Vd_placements.tex`, the consolidated exact reach-certificate
modules, and the explicit nine-point files `06_strategy4_ab_core.tex` and
`06_strategy4_completion.tex`.  The finite optimization specifications and
Lean statement-elaboration project remain compatibility interfaces for the
long scalar certificates.  The exact mixed-overlap proof follows as the sole
appendix.

## 3. Proof-source authority

The authority order is:

1. a numbered `proof/**/*.md` source whose status supports the claim;
2. the exact electronic objects formally incorporated by the paper;
3. the consolidated TeX proof faithfully reorganizing those sources;
4. navigation files, this ledger, and the paper-to-proof crosswalk.

The manuscript preserves all proof-critical distinctions: actual maximal
reaches versus selected lower bounds, the definition of `N_+` from actual
reaches, singleton boundary gaps, low-radial direct nonsupercritical transfer,
high-radial component selectors and equality assignments, center-free path
hypotheses, endpoint external components, the inclusive CE2 threshold
alternative, every T3-like branch, the Vd placement margins, the two-chart
replacement, and exact certificate denominator signs.

## 4. Legacy exact reach-certificate provenance

The complete support-isolated T3-like endpoint proof is authenticated by
`proof/407X_PROVENANCE.json`. CI recomputes the Git blob identities from the
exact bytes. The current objects are:

| Object | Git blob prefix |
|---|---|
| `4073_boundary_loss_framework.md` | `910c7a8a1330` |
| `4074_L_Full_branch.md` | `7c72dfaf7eb3` |
| `4075_Tminus_low_lower_branch_obligations.md` | `ebe2b65f8840` |
| `4078_left_L_family_completion.md` | `f1323325b069` |
| `4079_first_Full_branch.md` | `c66eea05277d` |
| `407a_left_Thigh_branch_completion.md` | `aa5cb1a6dc63` |
| `407c_rigor_completion_details.md` | `c80243f67124` |
| `407d_rigor_final_assembly.md` | `e22c85c95fdd` |

In the canonical branch crosswalk, first-`Const` followed by
right-`Const` or right-$Q_-$ is owned by `4075`; `4078` owns the remaining
first-`Const`, right-$Q_+$ family. The authenticated files retain their
legacy symbols; the repository notation dictionary gives their crosswalk to
the canonical symbols used in print.

## 5. Exact Strategy 4 certificate

The mixed-overlap appendix incorporates all sparse-data shards, the exact
derivation and positivity verifiers, and the canonical transcript digest

`dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485`.

The arithmetic model is exact over integers, rationals, and
`Q(sqrt(3))`; floating-point and interval arithmetic are not proof
dependencies.

## 6. Build status

On `main`, the paper-rebuild workflow replays the active proof-reference graph, legacy local-reach
specifications, the exact nine-point certificate, and Lean scalar-statement
elaboration; it then uses the pinned TeX Live 2025 image for two semantic
rebuilds, checks references, overfull boxes, and rendering, and commits a
changed canonical PDF and summary back to `main`. The read-only proof workflow
independently performs the same checks on user pushes and pull requests.
