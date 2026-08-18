# Paper-to-Proof Crosswalk

Paper root: `arrange/paper_draft/`  
Proof-package root: `proof/`

This document maps the consolidated paper to the numbered proof corpus. It is
navigation and maintenance metadata, not an additional proof.

## 1. Authority

The authority order is:

1. a numbered proof source whose status supports the asserted conclusion;
2. an exact electronic certificate incorporated by authenticated path and data;
3. the TeX paper faithfully reorganizing those sources;
4. this crosswalk, indexes, and other navigation files.

A `Reference`, `Reduction`, `Strategy`, `Empirical`, `Experiment`, `Lemma
target`, or `Failed` file does not become a proof because it is listed here.

## Canonical terminology and notation

The paper uses the terms **V triangle** and **C triangle** throughout.  The
proof package retains the same established terminology.

The shared public notation is

$$
(A_i,B_i,C_i),\qquad (a_i,b_i,c_i),
$$

$$
M_c,\qquad \overline M_c,\qquad \Phi_c,
$$

and

$$
N_+,\qquad N_{\rm sp},\qquad N_{\rm gap}.
$$

The authenticated 407X package retains provenance-preserving compatibility
aliases listed in `proof/09XX_appendices/0910_notation_dictionary.md`.

The redundant navigation-only files `1100_C_triangle_overview.md` and
`1200_V_triangle_overview.md` were merged into the substantive classification
sources `1101` and `1201`, respectively.  No route index, active theorem
source, historical failed route, or provenance-bound file was deleted.

## 2. Top-level assembly

| Printed section | Active TeX wrapper | Principal proof packages |
|---|---|---|
| 1. Introduction and Proof Outline | `01_introduction.tex` | `0000`, `1003`, `1101`, `1201`, `1214`, `2530` |
| 2. Structural Reduction and Common Geometry | `02_structure_and_common_geometry.tex` | `1001`, `1003`, `1101`, `1201`--`1214`, `2100`, `2109`, `2530` |
| 3. Trace-Length Bounds | `03_trace_bounds.tex` | `2500`, `2510`, `2530` and the routed length terminals |
| 4. Boundary-Reach Propagation | `04_boundary_propagation.tex` | `2004`, `2007`, `2010`--`2019`, `2107`--`2110`, `4013`, `407X`, `410X`, `413X`, `414X` |
| 5. Area-Loss Estimate | `05_area_loss_full.tex` | `3171`, `3174`, `3175`, `3201`, `3205`, `3208` |
| 6. Nine-Point Enclosure Obstruction | `06_nine_point_full.tex` | `31050`--`31059` and `3105X_computation` |
| 7. Completion of the Proof | `07_exhaustive_assembly.tex` | `0000` |
| Appendix A. Exact Mixed Overlaps | `06a_strategy4_exact_certificate.tex` | `31055`, `31056`, authenticated sparse data and verifiers |

## 3. Section 1: theorem and routing

### Main theorem and scaled closed formulation

- Main theorem: `proof/0XXX_main/0000_main_theorem.md`.
- Open/closed/scaled equivalence:
  `proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md`.

### Canonical labeling and finite types

- Global objects and conventions: `1001`.
- CE0/CE1/CE2 classification: `1101`.
- Vd0/Vd1/Vd2/T3-like classification: `1201`.
- Maximal reaches and local coordinates: `1202`.
- Actual `N_+`: `1212`.
- Strict handoff selection preserving the actual criticality pattern: `1214`.

### Routing table

The authoritative exhaustive assembly is `0000`; `0001` is navigation only.
The direct $N_++N_{\rm sp}\ge3$ skeleton theorem is in
`2530` together with the trace packages `2500` and `2510`.

## 4. Section 2: structural and signed-center geometry

The printed section incorporates:

- `02_structural_reductions.tex`;
- `04a_signed_center_calculus.tex`.

The corresponding numbered sources include:

- distinct distinguished triangles and global geometry: `0000`, `1001`;
- C-triangle and V-triangle classifications: `1101`, `1201`;
- T3-like nonsupercriticality and normalization: `1213`, supporting material
  in `1201`;
- strict boundary handoffs: `1214`;
- unique center midpoint in CE1/CE2: `2100` and the signed normal form `2109`;
- exact center traces and exits: `2105`, `2106`, `2109`;
- $N_++N_{\rm sp}$ skeleton routing: `2530`, `0000`.

## 5. Section 3: trace-length proof

The printed section incorporates:

- `03_strategy1_length.tex`;
- `04b_common_CE1_CE2_budgets.tex`.

Reusable bounds:

- perimeter trace bounds: `2500`;
- full-skeleton trace bounds: `2510`;
- common CE1/CE2 budgets and $N_++N_{\rm sp}$ theorem: `2530`.

Terminal branches closed here include:

- CE0, `N_+=0`: `3010`;
- CE0, `N_+=1`, some Vd1/Vd2: `3141`;
- CE1/CE2, `N_+=0`, some Vd1/Vd2: `4040`, `4041`;
- CE1, `N_+=1`, exactly one Vd1/Vd2: `4110` and associated length sources;
- all CE1/CE2 states with $N_++N_{\rm sp}\ge3$, including the
  `N_+>=2` route: `2530`, terminal assembly in `0000`;
- the neighboring-midpoint Vd2 subcase used inside the CE2 hybrid branch:
  the Vd corner and budget sources cited by `4140`.

## 6. Section 4: boundary-reach propagation

The printed section incorporates:

- `02a_universal_calculus.tex`;
- `04c_short_Vd_placements.tex`;
- `04_strategy2_verification.tex` and its detailed mathematical modules.

### Local transfer calculus

- exact local admissible set: `2004`;
- exact outgoing envelope and interval fibers: `2007`;
- strict-supercritical envelope: `2010`;
- branchwise nonsupercritical output and high-radial branches: `2011`;
- selected affine and threshold relaxations: `2016`, `2017`;
- adjacent exceptional transfer: `2018`;
- center intervals and path budget: `2019`;
- enclosure radical and support calculus: `201a`;
- quarter radial envelope: `201b`;
- Vd corner radial margins: `201c`;
- raw and relaxed transfer chains: `201d`.

### Signed endpoint inequalities

- one-side endpoint inequality: `2107`;
- paired CE2 endpoint inequality: `2108`;
- signed center normal form: `2109`;
- common paired-gap application: `2110`.

### Routed terminal families

- `N_+=0`, all Vd0: `4013`;
- `N_+=0`, T3-like and no Vd1/Vd2: complete `407X` package;
- `N_+=1`, all Vd0 with a gap: `4105`, `4106`, `4107`, assembled in `4101`;
- `N_+=1`, exactly one T3-like: `413X`;
- CE2, `N_+=1`, exactly one Vd1/Vd2: `414X`, including the corrected
  two-chart replacement `4147` and exhaustive placement audit `414b`.

The finite optimization specifications and pinned Lean statement-elaboration
project are repository interfaces for the long scalar calculations. Their
duplicate explanatory prose is not printed. CI checks their complete semantic
specification; the admitted Lean theorem bodies are not described as a formal
proof of the geometric bridge or of the global theorem.

## 7. Section 5: area loss

The printed section incorporates `05_strategy3_area.tex`.

- direct T3-like area certificate: `3171`, with local components `3174`, `3175`;
- `N_+>=2` square-loss area branch: `3201`, with local and cyclic components
  `3205`, `3208`;
- strict handoff selection: `1214`.

The section contains the local wedge reduction, both orientation families,
minimum- and maximum-square loss, the T3-like loss, the cyclic ascent
structure, and the two CE0 terminal sums.

## 8. Section 6 and Appendix A: nine-point enclosure

The printed section incorporates:

- `06_strategy4_ab_core.tex`;
- `06_strategy4_completion.tex`.

The exact appendix is `06a_strategy4_exact_certificate.tex`.

Primary numbered package:

`proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/`.

Key components are:

- exact-one handoff chain and radial forcing: `31050`--`31054`;
- rational radial envelopes and reduction to mixed signs: `31055`;
- global analytic mixed positivity: `31056`;
- exact computation package and sparse data: `3105X_computation`;
- final witness enclosure and branch completion: `31057`--`31059`.

The certificate is a single proof object consisting of the mathematical
reduction, authenticated data, exact derivation verifier, exact Bernstein
verifier, and canonical transcript digest. A printed `PASS` line alone is not
a proof.

## 9. Final assembly

`07_exhaustive_assembly.tex` invokes one terminal result for each row of the
routing table. The authoritative branch exhaustiveness and conclusion are in
`0000_main_theorem.md`. The proof-tree index `0001` and this crosswalk are
navigation only.

## 10. Verification and generated PDF

`.github/workflows/paper-rebuild.yml` builds the consolidated source in the
pinned TeX Live image, checks the target page range and rendering, regenerates
the current verification summary, and commits the canonical PDF to `main`.

`.github/workflows/proof-ci.yml` then checks the numbered proof-reference graph
(whose untyped citation edges may be cyclic),
manifest, proof-source terminology, exact Strategy 2 specifications, pinned
Lean scalar-statement elaboration, exact Strategy 4 certificate, semantic PDF rebuild,
and deterministic release bundle.
