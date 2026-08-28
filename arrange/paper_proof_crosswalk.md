# Paper-to-Proof Crosswalk

Paper root: `arrange/paper_draft/`  
Proof-package root: `proof/`

Status: Reference

This document maps the consolidated paper to the numbered proof corpus.  It is
navigation and maintenance metadata, not an additional proof.

## 1. Authority

The authority order is:

1. a numbered proof source whose status supports the asserted conclusion;
2. an exact electronic certificate incorporated by authenticated path and data;
3. the TeX paper faithfully reorganizing those sources;
4. this crosswalk, indexes, and other navigation files.

A `Reference`, `Reduction`, `Strategy`, `Empirical`, `Experiment`, `Lemma
target`, or `Failed` file does not become a proof because it is listed here.

## 2. Three-strategy publication architecture

| Printed section | Active TeX wrapper | Principal proof packages |
|---|---|---|
| 1. Introduction and proof outline | `01_introduction.tex` | `0000`, `1003`, `1101`, `1201`, `1214`, `2530` |
| 2. Structural reduction and common geometry | `02_structure_and_common_geometry.tex` | `1001`, `1003`, `1101`, `1201`--`1214`, `2100`, `2109`, `2530` |
| 3. Strategy 1: trace-length bounds | `03_trace_bounds.tex` | `2500`, `2510`, `2530` and routed length terminals |
| 4. Strategy 2: area loss | `05_area_loss_full.tex` | `3171`, `3174`, `3175`, `3201`, `3205`, `3208` |
| 5. Strategy 3: finite enclosure | `06_finite_enclosure_full.tex` | `2608`, the five `_new` nonzero-gap packages, `31050`--`31059`, and the retained exact local reach certificates |
| 6. Completion of the proof | `07_exhaustive_assembly.tex` | `0000` |
| Appendix A. Exact mixed overlaps | `06a_strategy4_exact_certificate.tex` | `31055`, `31056`, authenticated sparse data and verifiers |

The file names `04_strategy2_*` and the directory
`formalization/strategy2_optimization/` are retained for compatibility and
provenance.  They no longer name a global proof strategy in the paper.

## 3. Canonical terminology and notation

The paper and proof package use **V triangle** and **C triangle**.  The shared
public notation is

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

The authenticated `407X` files retain the compatibility aliases recorded in
`proof/09XX_appendices/0910_notation_dictionary.md`.

## 4. Sections 1 and 2: theorem, routing, and common geometry

The authoritative exhaustive assembly is
`proof/0XXX_main/0000_main_theorem.md`; `0001` is navigation only.

The structural sources include:

- distinct distinguished roles and open/closed equivalence: `1001`, `1003`;
- CE0/CE1/CE2 classification: `1101`;
- normalized Vd0/Vd1/Vd2/T3-like classification: `1201`;
- actual reaches and strict handoffs: `1202`, `1212`, `1214`;
- unique CE1/CE2 midpoint and signed center form: `2100`, `2109`;
- common high-count skeleton pruning: `2530`.

The outer split is $N_{\rm gap}=0$ versus $N_{\rm gap}\ge1$.  Zero-gap cases
use Strategies 1, 2, or the explicit nine-point member of Strategy 3.
Nonzero-gap cases use Strategy 1 or the residual-hull member of Strategy 3.

## 5. Section 3: Strategy 1, trace length

The printed section incorporates:

- `03_strategy1_length.tex`;
- `04b_common_CE1_CE2_budgets.tex`.

Reusable bounds are `2500`, `2510`, and `2530`.  Terminal branches include:

- every zero-gap $N_+=0$ branch;
- every zero-gap $N_+=1$ branch with a Vd1/Vd2 role;
- CE1/CE2, $N_+=0$, some Vd1/Vd2: `4040`, `4041`;
- CE1, $N_+=1$, one Vd1/Vd2: `4110`;
- all states with $N_++N_{\rm sp}\ge3$;
- the Vd2 neighboring-midpoint and extra-positive-support terminals inside
  the CE2 one-Vd assembly.

## 6. Section 4: Strategy 2, area loss

The printed section incorporates `05_strategy3_area.tex` under the new
Strategy 2 numbering.

- boundary-complete one-supercritical T3-like certificate: `3171`, `3174`,
  `3175`;
- boundary-complete $N_+\ge2$ square-loss certificate: `3201`, `3205`, `3208`;
- strict handoff selection: `1214`.

## 7. Section 5: Strategy 3, finite enclosure

### 7.1 Common residual-hull principle

The reusable theorem is
[`2608`](../proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md).
For fixed V roles, put

$$
R=H\setminus\bigcup_{i=0}^5U_i,
\qquad
K_R=\mathrm{vert}(\mathrm{conv}R).
$$

If the relevant C-triangle completion theorem excludes every unit C triangle
containing $R$, then $\Lambda(K_R)\ge1$.  Under a hypothetical cover,
$K_R\subset U_C$.

### 7.2 Active nonzero-gap packages

| Branch | Active finite-enclosure source | Exact certificate cited |
|---|---|---|
| CE1/CE2, $N_+=0$, all Vd0 | [`4013_new`](../proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md) | original `4013`, `2107`, `2108`, `2110` |
| CE1/CE2, $N_+=0$, one or two T3-like, no Vd1/Vd2 | [`4070_new`](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md) | complete authenticated `407X` package |
| CE1/CE2, $N_+=1$, all Vd0 | [`4101_new`](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4101_new_all_Vd0_finite_enclosure.md) | `4105`, `4106`, `4107`, and the paired two-gap certificate |
| CE1/CE2, $N_+=1$, exactly one T3-like | [`4130_new`](../proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) | `4131`, `4132`, `2018` |
| $N_+=1$, exactly one Vd1/Vd2 | [`4140_new`](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md) | CE1 length terminal and complete `414X` placement package |

The exact local reach calculus is printed inside Strategy 3 through the
legacy-named wrappers:

- `02a_universal_calculus.tex`;
- `04c_short_Vd_placements.tex`;
- `04_strategy2_verification.tex` and its detailed modules.

These calculations are certificates for the inequality
$\Lambda(K_R)\ge1$; they are not a fourth strategy.

### 7.3 Explicit zero-gap nine-point theorem

The explicit package is
`proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/`.
The printed files are `06_strategy4_ab_core.tex` and
`06_strategy4_completion.tex`.  The exact appendix is
`06a_strategy4_exact_certificate.tex`.

Key components are:

- exact-one handoff chain and radial forcing: `31050`--`31054`;
- rational radial envelopes and mixed-sign reduction: `31055`;
- global analytic positivity: `31056`;
- final witness enclosure and branch completion: `31057`--`31059`.

## 8. The CE2 one-Vd placement assembly

The exact placement partition remains in the original `414X` package, with
assembly `4148` and audit `414b`.  The active branch-level finite-enclosure
wrapper is `4140_new`.

The corrected replacement `4147` does not preserve input gap rank.  Its output
rank is recomputed.  Rank zero uses Strategy 1; positive rank uses
`4013_new`.

## 9. Final assembly

`07_exhaustive_assembly.tex` invokes the three strategy families.  The
numbered exhaustive proof is `0000_main_theorem.md`.

## 10. Verification and generated PDF

The workflow filenames and compatibility checks retain their historical
`strategy2` and `strategy4` identifiers.  They verify the exact local reach
specifications and the explicit nine-point certificate respectively.  The
write-enabled workflow rebuilds the PDF and verification summary on the
triggering branch; the read-only workflow checks the proof graph, manifest,
source lint, certificates, Lean statement project, semantic PDF rebuild, and
release bundle.
