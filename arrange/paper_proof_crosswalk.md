# Paper-to-Proof Crosswalk

Paper root: `arrange/paper_draft/`  
Proof-package root: `proof/`

Status: Reference

This document maps the consolidated paper to the numbered proof corpus. It is
navigation metadata, not an additional proof.

## 1. Authority

A claim is established only by a numbered proof source with a supporting
status or by an exact authenticated certificate. Indexes, this crosswalk, and
historical compatibility files do not upgrade a proof status.

## 2. Three-strategy publication architecture

| Printed section | Active TeX source | Principal proof packages |
|---|---|---|
| 1. Introduction and routing | `01_introduction.tex` | `0000`, `1003`, `1101`, `1201`, `1214`, `2530` |
| 2. Common geometry | `02_structure_and_common_geometry.tex` | `1001`, `1003`, `1101`, `1201`--`1214`, `2004`, `2008`, `2100`, `2109` |
| 3. Strategy 1: trace length | `03_trace_bounds.tex` | `2500`, `2510`, `2530` and routed length terminals |
| 4. Strategy 2: area loss | `05_area_loss_full.tex` | `3171`, `3174`, `3175`, `3201`, `3205`, `3208` |
| 5. Strategy 3: finite enclosure | `06_finite_enclosure_full.tex` and its `06*` direct-calculation inputs | `2608`, the five `_new` packages, `31050`--`31059` |
| 6. Exhaustive completion | `07_exhaustive_assembly.tex` | `0000` |
| Appendix A | `06a_strategy4_exact_certificate.tex` | `31055`, `31056`, sparse data, and exact verifiers |

The paper does not compile `04_boundary_propagation.tex` or
`04_strategy2_verification.tex`. Files retaining `strategy2` in their names
are historical scalar-compatibility interfaces, not a fourth strategy.

## 3. Common direct finite-enclosure geometry

The reusable source is
[`2608`](../proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md).
It proves:

1. the support-function formula for the minimum enclosing equilateral triangle;
2. the exact disk-plus-point formula;
3. the type-aware radial witness
   $$D_i=(1-\Gamma_i)V_i,$$
   where only own and actually permitted neighboring capacities enter
   $\Gamma_i$;
4. common-pair domination of neighboring support by the own-ray capacity;
5. the complementary-gap enclosure theorem;
6. the CE2 two-gap short-ray theorem.

These are forward geometric implications. They do not define a residual hull
and then cite an old case exclusion.

At an actual gap $X_i([\ell,r])$, the endpoint identities are\n$\ell=B_i$ and $r=1-A_{i+1}$.  The local incident roles are represented by\nthe trace-exact AB envelopes proved in [`2009e`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/2009e_trace_exact_ab_envelopes.md).  These are source-conditioned subunions of the ordinary AB-set, so the existing $c_{\max},C_+,C_-$ capacities remain safe, while the edge sections stop at the actual gap endpoints.  The interactive explorer and paper atlas are generated from this same model.

## 4. Active nonzero-gap proofs

| Branch | Direct proof source | Mathematical terminal |
|---|---|---|
| CE1/CE2, $N_+=0$, all Vd0 | [`4013_new`](../proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md) | common radial disk plus complementary gap; CE2 short ray for two gaps |
| CE1/CE2, $N_+=0$, one or two T3-like roles | [`4070_new`](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md) | exact neighboring-ray capacity is dominated by the common own-ray capacity, then the same gap or short-ray terminal |
| CE1/CE2, $N_+=1$, all Vd0 | [`4101_new`](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4101_new_all_Vd0_finite_enclosure.md), [`4102_new`](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4102_new_CE1_direct_radial_certificate.md) | six actual radial endpoints plus gap endpoints; direct CE1 reverse path or direct CE2 threshold dichotomy |
| CE1/CE2, $N_+=1$, exactly one T3-like role | [`4130_new`](../proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) | O-side endpoint of the supported T3 trace plus a direct four-triangle path budget |
| CE2, $N_+=1$, exactly one Vd1/Vd2 role | [`4140_new`](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md) | direct radial separation, Vd1 O-side endpoint, perimeter deficit, or two-chart replacement followed by the new all-Vd0 theorem |

The former `4013`, `407X`, `4105`--`4107`, `413X`, and propagation-owned
parts of `414X` remain in the corpus as historical proofs. They are not active
case terminals and are not used to justify the new files.

## 5. Printed direct calculations

The direct mathematical calculations are printed in:

- `06_direct_local_calculus.tex`;
- `06a_neighbor_ray_calculus.tex`;
- `06b_ce1_direct_certificate.tex`;
- `06c_exceptional_direct_terminals.tex`;
- `06d_detailed_direct_certificates.tex`;
- `06e_direct_local_proof_details.tex`;
- `06f_casewise_witness_details.tex`;
- `06g_endpoint_selector_audit.tex`.

In particular, the CE1 proof follows the actual boundary reaches through
$T_5,T_4,T_3,T_2,T_1$ and proves explicit lower bounds $L_1,L_2$ and the final
capacity violation. It does not introduce or compose a propagation map.

## 6. Zero-gap Strategy 3 theorem

The center-independent nine-point package remains
`proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/`.
It directly forces six radial points and three strict-supercritical
$AB$-frontier points and proves their enclosure number is at least one. The
mixed-overlap certificate remains Appendix A.

## 7. Strategy 1 and Strategy 2 terminals

Strategy 1 retains all perimeter, diagonal, and skeleton-length closures,
including the Vd2 midpoint and extra-positive-support branches. Strategy 2
retains the zero-gap cyclic area arguments. Neither is affected by the new
direct nonzero-gap proofs.

## 8. Verification

The active dependency graph and proof manifest include the new proof sources.
The old scalar files and Lean project are retained only for compatibility.
The permanent workflows check the direct three-strategy paper, replay the exact
nine-point certificate, build the pinned Lean project, and perform a two-build
semantic PDF audit.
