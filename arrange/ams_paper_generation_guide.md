# AMS-Style Self-Contained Paper Guide

This file specifies the active manuscript architecture. Numbered proof sources
remain authoritative for theorem status and hypotheses. The paper may
reorganize proved material, but it may not strengthen a claim, remove a
strictness condition, infer actual criticality from selected lower bounds, or
replace an exact certificate by numerical evidence.

## 1. Publication objective

The target is a self-contained paper in the repository's audited 84--104 page
range. Length is controlled by removing duplicate reader, registry, and
historical-calculation layers, not by deleting proof obligations.

## 2. Active printed architecture

The body has three strategies:

```text
01_introduction.tex
02_structure_and_common_geometry.tex
03_trace_bounds.tex
05_area_loss_full.tex
06_finite_enclosure_full.tex
07_exhaustive_assembly.tex
```

Their functions are:

1. theorem, classifications, and exhaustive routing;
2. structural reduction and signed center geometry;
3. Strategy 1: trace-length contradictions;
4. Strategy 2: area-loss contradictions;
5. Strategy 3: direct finite-point and finite-set enclosure contradictions;
6. final exhaustive assembly.

The sole printed appendix is
`06a_strategy4_exact_certificate.tex`, which contains the authenticated exact
mixed-overlap certificate for the zero-gap nine-point theorem.

The former files `04_boundary_propagation.tex` and
`04_strategy2_verification.tex` are not compiled. Historical files with
`strategy2` in their names may remain for provenance and the pinned Lean
statement interface, but they must not own a printed theorem or an active case.

## 3. Strategy 3 source incorporation

`06_finite_enclosure_full.tex` incorporates these proof-bearing sources:

```text
06_direct_local_calculus.tex
06a_neighbor_ray_calculus.tex
06b_ce1_direct_certificate.tex
06c_exceptional_direct_terminals.tex
06d_detailed_direct_certificates.tex
06e_direct_local_proof_details.tex
06f_casewise_witness_details.tex
06g_endpoint_selector_audit.tex
06_strategy4_ab_core.tex
06_strategy4_completion.tex
```

The first eight files contain the actual new nonzero-gap proofs: radial witness
forcing, complementary-gap enclosure, CE2 short-ray separation, the direct CE1
reverse path, T3-like and Vd1 O-side endpoints, Vd-specific radial separation,
and casewise endpoint audits. They may use the exact local admissible set and
single-triangle capacity functions, but they must not introduce or compose a
boundary-transfer map.

## 4. Content placement

Keep in the main proof:

- open/closed/scaled equivalence;
- center and vertex classifications;
- actual and selected reaches, gaps, and handoffs;
- midpoint forcing and signed center geometry;
- exact own-ray and permitted neighbor-ray capacities;
- explicit center-forced witness points;
- support-function enclosure calculations;
- direct CE1 and CE2 scalar estimates;
- T3-like and Vd placement arguments;
- the two-chart replacement;
- the zero-gap nine-point theorem;
- the exhaustive completion.

Keep in the exact appendix only the authenticated sparse polynomial data and
exact mixed-overlap positivity proof. Keep historical alternative proofs,
maintenance provenance, and formalization registries outside the printed
article.

## 5. Paper-wide notation

Use:

- C triangle and V triangle;
- actual reaches $(A_i,B_i,C_i)$;
- selected lower bounds $(a_i,b_i,c_i)$;
- $N_+$ defined only from $A_i+B_i>1$;
- boundary gaps, including singleton gaps;
- $N_{\rm gap}$ for the number of positive center traces containing a gap;
- CE0, CE1, CE2 and Vd0, Vd1, Vd2, T3-like;
- $c_{\max}(a,b)$ for the exact own-ray capacity;
- $C_+(a,b),C_-(a,b)$ for exact permitted neighboring-ray capacities;
- $D_i=(1-\Gamma_i)V_i$ for type-aware radial witnesses.

The printed proof may state a direct one-triangle output inequality, but it
must not package successive triangles into a composed map. Provenance-bound
legacy aliases may remain only in authenticated historical files.

## 6. Non-negotiable distinctions

Every revision must preserve:

1. actual versus selected criticality;
2. open traces and singleton gaps;
3. CE1 point contact versus CE2 positive companion trace;
4. actual V-type restrictions on neighboring radial support;
5. center-free hypotheses for direct path budgets;
6. connected-component selectors after squaring;
7. all branch-boundary equality assignments;
8. the inclusive CE2 threshold dichotomy;
9. the complete T3-like parameter domain;
10. adjacent and nonadjacent Vd-specific margins;
11. both charts and all strict margins in the Vd1 replacement;
12. the authenticated zero-gap exact arithmetic model.

## 7. Build and verification

The permanent workflows:

1. regenerate the active proof graph and manifest;
2. run source linting and historical compatibility checks;
3. elaborate the pinned Lean statement project;
4. replay the exact zero-gap Strategy 3 certificate;
5. build twice in pinned TeX Live 2025;
6. reject unresolved or duplicate references and overfull boxes;
7. compare stable PDF semantics and exact rendered pixels;
8. verify the 84--104 page range and rendering;
9. regenerate the canonical verification summary;
10. construct a deterministic release bundle.

For a local preview:

```bash
cd arrange/paper_draft
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Do not manually update the tracked PDF without regenerating the verification
summary and running the permanent checks.
