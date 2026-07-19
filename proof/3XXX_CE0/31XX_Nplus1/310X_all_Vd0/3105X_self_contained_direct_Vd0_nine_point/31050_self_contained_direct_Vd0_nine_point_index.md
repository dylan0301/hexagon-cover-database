# Self-Contained Direct Vd0 Nine-Point Package

Status: Reference

This package is the canonical direct proof of the CE0, $N_+=1$, all-Vd0
branch.  It first proves a center-class-independent obstruction for six open
Vd0 vertex roles that cover the full boundary and have exactly one
supercritical actual row.  Six radial witnesses and three asymmetric
witnesses are forced directly into the center role, and an exact finite cap
certificate proves that no open unit equilateral triangle can contain them.

The proof notes below are self-contained relative to the earlier `310X`
packages.  They cite only one another and the proved foundational and
geometric results listed below.  Historical source attribution to earlier
`310X` notes and computation files is confined to the provenance section of
this index.

## Package contents

| File | Recorded status | Role |
|---|---|---|
| [`31051_direct_radial_forcing.md`](31051_direct_radial_forcing.md) | Proven | Forces the six common radial witnesses out of every actual vertex role. |
| [`31052_fixed_line_circle_signs.md`](31052_fixed_line_circle_signs.md) | Proven | Proves the exact first-root, moving-circle, coordinate, and reflected sign inequalities. |
| [`31053_direct_asymmetric_witness_forcing.md`](31053_direct_asymmetric_witness_forcing.md) | Proven | Defines the three asymmetric witnesses and excludes them from all six actual vertex roles. |
| [`31054_four_cap_enclosure_reduction.md`](31054_four_cap_enclosure_reduction.md) | Proven | Reduces enclosure to a cyclic cap chain and proves the two adjacent overlaps analytically. |
| [`31055_rational_radial_envelopes_and_mixed_reduction.md`](31055_rational_radial_envelopes_and_mixed_reduction.md) | Proven | Replaces the exact radial value by rational envelopes and reduces the mixed overlaps to eight integer-polynomial signs. |
| [`31056_global_analytic_mixed_positivity.md`](31056_global_analytic_mixed_positivity.md) | Proven | Proves the eight signs on three fixed charts by twenty global Bernstein identities. |
| [`31057_terminal_nine_point_enclosure.md`](31057_terminal_nine_point_enclosure.md) | Proven | Assembles the exact terminal inequality $\Lambda(K_{\mathrm{wit}})\ge1$. |
| [`31058_center_independent_direct_nine_point_obstruction.md`](31058_center_independent_direct_nine_point_obstruction.md) | Proven | Gives the reusable center-class-independent all-boundary contradiction. |
| [`31059_CE0_Nplus1_all_Vd0_completion.md`](31059_CE0_Nplus1_all_Vd0_completion.md) | Proven | Closes the CE0, $N_+=1$, all-Vd0 branch. |

The package-local directory [`3105X_computation/`](3105X_computation/)
contains the exact symbolic derivation audit, the nonadaptive global
Bernstein verifier, and its canonical integer-polynomial transcript.  These
are supporting certificate artifacts rather than separate proof-status notes.

## Proved external dependencies

| Source | Recorded status | Use in this package |
|---|---|---|
| [`1101_CE_classification.md`](../../../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md) | Proven | CE0 boundary-edge locality in the terminal branch wrapper. |
| [`1201_V_triangle_types.md`](../../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) | Proven | Vd0 adjacent-radial locality. |
| [`1214_strict_boundary_handoff_selection.md`](../../../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) | Proven | Strict exact-one handoffs and preservation of the unique supercritical row. |
| [`2004_admissible_set.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md) | Proven | Exact radial envelope $c_{\max}$. |
| [`20091_ab_union_curve_a_plus_b_gt_1.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md) | Proven | Exact four-piece frontier of the unique strict supercritical row. |

## Provenance from earlier `310X` work

The following table records where the ingredients were first proved or used.
It is attribution only: none of these files is a dependency of the proof notes
in this package.

| Earlier source | Recorded status | Ingredient rewritten locally |
|---|---|---|
| [`31012_core_graph_two_variable_relaxation.md`](../3101X_six_point/31012_core_graph_two_variable_relaxation.md) | Proven | Fixed-line circle signs, first-root selection, monotonicity, and reflection. |
| [`31033_asymmetric_witness_construction.md`](../3103X_residual_core/31033_asymmetric_witness_construction.md) | Proven | Exact asymmetric formulas, interior bounds, and vertex-distance identities. |
| [`31034_witness_enclosure_inequality.md`](../3103X_residual_core/31034_witness_enclosure_inequality.md) | Proven | Newton inner witnesses, cap reduction, ray order, and analytic adjacent overlaps. |
| [`31037_rational_cmax_upper_envelope.md`](../3103X_residual_core/31037_rational_cmax_upper_envelope.md) | Proven | Rational radial envelopes and exact mixed-residual elimination. |
| [`31038_global_analytic_core_positivity.md`](../3103X_residual_core/31038_global_analytic_core_positivity.md) | Proven | Three analytic charts and twenty global Bernstein identities. |
| [`31041_direct_radial_forcing.md`](../3104X_direct_Vd0_nine_point/31041_direct_radial_forcing.md) | Proven | Direct six-radial-point forcing architecture. |
| [`31042_direct_asymmetric_witness_forcing.md`](../3104X_direct_Vd0_nine_point/31042_direct_asymmetric_witness_forcing.md) | Proven | Direct exclusion of the three asymmetric points from the actual roles. |
| [`31043_center_independent_direct_nine_point_obstruction.md`](../3104X_direct_Vd0_nine_point/31043_center_independent_direct_nine_point_obstruction.md) | Proven | Center-independent nine-point assembly. |
| [`31044_CE0_Nplus1_all_Vd0_direct_completion.md`](../3104X_direct_Vd0_nine_point/31044_CE0_Nplus1_all_Vd0_direct_completion.md) | Proven | CE0 boundary-coverage wrapper. |

The package-local derivation checker was rewritten from the exact symbolic
derivation in
[`verify_rational_mixed_overlap.py`](../3103X_residual_core/3103X_computation/verify_rational_mixed_overlap.py).
The canonical transcript and nonadaptive verifier originate in
[`verify_global_core_positivity.py`](../3103X_residual_core/3103X_computation/verify_global_core_positivity.py),
[`mixed_overlap_core_polynomials.py`](../3103X_residual_core/3103X_computation/mixed_overlap_core_polynomials.py),
and its six numbered data modules.  The canonical polynomial digest is

```text
dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485
```

The older model residual-core proof remains independently Proven.  The new
canonical route does not use nonsupercritical $AB$-unions, their model-core
comparison, the neighboring-ray maximum theorem, the optional six-point
inequality, interval subdivision, or branch-and-bound.
