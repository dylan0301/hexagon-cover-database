# Paper Source Ledger

This ledger records the files assembled into the consolidated manuscript and
the numbered proof objects supporting them. It is maintenance metadata, not an
additional proof.

## 1. Printed three-strategy architecture

| File | Printed function |
|---|---|
| `01_introduction.tex` | theorem, classifications, and exhaustive routing |
| `02_structure_and_common_geometry.tex` | open/closed conventions, handoffs, midpoint forcing, and signed CE1/CE2 geometry |
| `03_trace_bounds.tex` | Strategy 1: perimeter, diagonal, and skeleton trace bounds |
| `05_area_loss_full.tex` | Strategy 2: local and cyclic area loss |
| `06_finite_enclosure_full.tex` | Strategy 3: explicit center-forced points and direct equilateral-enclosure contradictions |
| `07_exhaustive_assembly.tex` | final application of the three-strategy routing table |
| `06a_strategy4_exact_certificate.tex` | Appendix A: exact mixed-overlap certificate for the zero-gap nine-point theorem |

The former boundary-propagation files `04_boundary_propagation.tex` and
`04_strategy2_verification.tex` are not inputs to `main.tex`. They remain in
the source tree only as historical provenance and as compatibility sources for
the separately pinned scalar-statement project.

## 2. Active Strategy 3 source map

The finite-enclosure section is assembled from the following direct sources.

| File | Function |
|---|---|
| `06_direct_local_calculus.tex` | support gauge, exact local admissibility, own-ray capacity, and selected direct chord estimates |
| `06a_neighbor_ray_calculus.tex` | exact neighboring-ray capacity and type-aware radial exclusion |
| `06b_ce1_direct_certificate.tex` | direct CE1 one-gap reverse boundary path and scalar contradiction, with no composed transfer map |
| `06c_exceptional_direct_terminals.tex` | T3-like and Vd1 supported-trace endpoints and direct path budgets |
| `06d_detailed_direct_certificates.tex` | complementary-gap, CE2 one-gap, CE2 short-ray, and Vd separation calculations |
| `06e_direct_local_proof_details.tex` | direct finite-caliper branches, strict-supercritical envelope, quarter envelope, and Vd margins |
| `06f_casewise_witness_details.tex` | casewise witness sets, singleton-gap handling, and replacement routing |
| `06g_endpoint_selector_audit.tex` | endpoint selectors, continuity, compactness, and the finite support audit |
| `06_strategy4_ab_core.tex`, `06_strategy4_completion.tex` | explicit zero-gap nine-point construction and terminal enclosure theorem |

The corresponding proof-package authorities are:

- `2608_residual_hull_finite_enclosure_principle.md`, whose retained filename
  now contains the proved radial-witness, complementary-gap, and CE2 short-ray
  lemmas;
- `4013_new_all_Vd0_finite_enclosure.md`;
- `4070_new_T3_like_finite_enclosure.md`;
- `4101_new_all_Vd0_finite_enclosure.md` and
  `4102_new_CE1_direct_radial_certificate.md`;
- `4130_new_T3_like_finite_enclosure.md`;
- `4140_new_one_Vd_finite_enclosure_assembly.md`;
- the established `3105X` direct nine-point package.

## 3. Proof-source authority

The authority order is:

1. a numbered `proof/**/*.md` source whose status supports the claim;
2. exact electronic certificates incorporated by authenticated path and data;
3. the consolidated TeX proof faithfully reorganizing those sources;
4. navigation files, this ledger, and the paper-to-proof crosswalk.

The manuscript preserves actual maximal reaches versus selected lower bounds,
the definition of $N_+$ from actual reaches, singleton boundary gaps, the
CE1/CE2 signed-domain inequalities, type-aware adjacent radial support, open
endpoint exclusions, and the two-chart Vd1 replacement.

## 4. Historical scalar compatibility sources

The files whose names begin with `04_strategy2_` and the Lean project in
`formalization/strategy2_optimization/` are not active paper sources and own no
case in the three-strategy proof. They are retained unchanged to preserve the
old statement interface and historical reproducibility. The active CE1 proof
is the direct reverse-path calculation printed in
`06b_ce1_direct_certificate.tex` and recorded in `4102_new`.

## 5. Authenticated 407X provenance

The former four-label T3-like proof is retained as an alternative historical
proof and authenticated by `proof/407X_PROVENANCE.json`; it is not cited as
the proof of `4070_new`. CI still recomputes the exact Git blob identities:

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
first-`Const`, right-$Q_+$ family.

## 6. Exact zero-gap Strategy 3 certificate

The mixed-overlap appendix incorporates all sparse-data shards, the exact
derivation and positivity verifiers, and the canonical transcript digest

`dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485`.

The arithmetic model is exact over integers, rationals, and
`Q(sqrt(3))`; floating-point and interval arithmetic are not proof
dependencies.

## 7. Build status

The permanent workflows regenerate the active dependency graph and manifest,
run source linting and the historical compatibility checks, replay the exact
zero-gap enclosure certificate, elaborate the pinned Lean statement project,
build the manuscript twice in TeX Live 2025, compare stable PDF semantics and
rendered pixels, and construct the deterministic release bundle.
