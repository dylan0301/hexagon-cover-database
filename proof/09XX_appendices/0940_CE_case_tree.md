# CE Case Tree

Status: Strategy

This file records the current branch organization. It is not a proof of the
main theorem; each cited file keeps its own proof status.

## Spine

Under a hypothetical seven-triangle cover, choose role triangles

$$
T_C,T_0,\dots,T_5.
$$

Classify $T_C$ as CE0, CE1, or CE2. Inside each CE branch, define the
perimeter rows $(a_i,b_i)$ and split by

$$
N_+=\#\{i:a_i+b_i>1\}.
$$

The main navigation files are:

- [`../0XXX_main/0001_proof_tree_index.md`](../0XXX_main/0001_proof_tree_index.md).
- [`../3XXX_CE0/3000_CE0_index.md`](../3XXX_CE0/3000_CE0_index.md).
- [`../4XXX_CE1/4000_CE1_index.md`](../4XXX_CE1/4000_CE1_index.md).
- [`../5XXX_CE2/5000_CE2_index.md`](../5XXX_CE2/5000_CE2_index.md).

The open/closed equivalence is proved in
[`../1XXX_foundations/1003_open_unit_vs_shrunken_closed_equivalence.md`](../1XXX_foundations/1003_open_unit_vs_shrunken_closed_equivalence.md).

The May 24, 2026 skeleton-cover counterexample prevents using full-skeleton
noncoverage as a standalone route; see
[`../9XXX_failed_ideas/908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md`](../9XXX_failed_ideas/908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md).

## CE0

### CE0, $N_+=0$

- Route: perimeter-length obstruction.
- Status source: [`../3XXX_CE0/30XX_Nplus0/3010_CE0_perimeter_length_obstruction.md`](../3XXX_CE0/30XX_Nplus0/3010_CE0_perimeter_length_obstruction.md).
- Recorded status: Lemma target.

### CE0, $N_+=1$, all Vd0

- Route: May 25 five-point route and algorithm-2 finite-point route.
- Status sources:
  - [`../3XXX_CE0/31XX_Nplus1/310X_all_Vd0_five_point/3101_CE0_all_Vd0_five_point_index.md`](../3XXX_CE0/31XX_Nplus1/310X_all_Vd0_five_point/3101_CE0_all_Vd0_five_point_index.md).
  - [`../3XXX_CE0/31XX_Nplus1/310X_all_Vd0_five_point/312X_may25_five_point/3120_may25_five_point_index.md`](../3XXX_CE0/31XX_Nplus1/310X_all_Vd0_five_point/312X_may25_five_point/3120_may25_five_point_index.md).
- Recorded status: Strategy / lemma target / empirical, depending on the cited subfile.
- Warning: the May 21 four-point route failed for this branch; see [`../3XXX_CE0/31XX_Nplus1/310X_all_Vd0_five_point/3130_may21_four_point_warning.md`](../3XXX_CE0/31XX_Nplus1/310X_all_Vd0_five_point/3130_may21_four_point_warning.md) and [`../9XXX_failed_ideas/962X_may21_four_point_failure/9620_may21_patternA_index.md`](../9XXX_failed_ideas/962X_may21_four_point_failure/9620_may21_patternA_index.md).

### CE0, $N_+=1$, at least one Vd1/Vd2

- Route: half-skeleton obstruction.
- Status source: [`../3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3110_CE0_Vd1_Vd2_obstruction_index.md`](../3XXX_CE0/31XX_Nplus1/311X_Vd1_Vd2_obstruction/3110_CE0_Vd1_Vd2_obstruction_index.md).
- Recorded status: Proven.

### CE0, $N_+=1$, T3-like and no Vd1/Vd2

- Route: conditional T3-like area certificate.
- Status sources:
  - [`../3XXX_CE0/31XX_Nplus1/312X_T3_like_no_Vd1Vd2/3120_CE0_one_T3_like_area_certificate_index.md`](../3XXX_CE0/31XX_Nplus1/312X_T3_like_no_Vd1Vd2/3120_CE0_one_T3_like_area_certificate_index.md).
  - [`../3XXX_CE0/31XX_Nplus1/312X_T3_like_no_Vd1Vd2/3124_CE0_one_supercritical_T3_certificate.md`](../3XXX_CE0/31XX_Nplus1/312X_T3_like_no_Vd1Vd2/3124_CE0_one_supercritical_T3_certificate.md).
- Recorded status: Proven analytic inequality, conditional.

### CE0, $N_+\ge2$

- Route: conditional area certificate.
- Status sources:
  - [`../3XXX_CE0/32XX_Nplus_ge2/3200_CE0_area_certificate.md`](../3XXX_CE0/32XX_Nplus_ge2/3200_CE0_area_certificate.md).
  - [`../3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md`](../3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md).
- Recorded status: Proven analytic inequality, conditional on local square-loss bounds.

## CE1

### CE1, $N_+=0$, all Vd0

- Route: boundary-loss package under recorded assumptions.
- Status source: [`../4XXX_CE1/40XX_Nplus0/400X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`](../4XXX_CE1/40XX_Nplus0/400X_all_Vd0_boundary_loss/4013_boundary_loss_index.md).
- Recorded status: Proven local lemma under recorded assumptions.

### CE1, $N_+=1$, all Vd0

- Route: open branch.
- Status source: [`../4XXX_CE1/41XX_Nplus1/410X_all_Vd0/4101_CE1_Nplus1_all_Vd0_TODO.md`](../4XXX_CE1/41XX_Nplus1/410X_all_Vd0/4101_CE1_Nplus1_all_Vd0_TODO.md).
- Warning: the May 25 five-point route is not used for this branch because of the reported CE1/CE2 failure in [`../9XXX_failed_ideas/963X_may25_five_point_failure/9630_may25_CE1_CE2_failure.md`](../9XXX_failed_ideas/963X_may25_five_point_failure/9630_may25_CE1_CE2_failure.md).

### CE1, $N_+=1$, Vd1/Vd2 or T3-like branches

- Shared Vd1/Vd2 route: [`../4XXX_CE1/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_CE2_Vd1_Vd2_length_branches.md`](../4XXX_CE1/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_CE2_Vd1_Vd2_length_branches.md).
- At least two T3-like route: [`../4XXX_CE1/41XX_Nplus1/412X_at_least_two_T3_like/4120_CE1_CE2_T3_like_midpoint_branches.md`](../4XXX_CE1/41XX_Nplus1/412X_at_least_two_T3_like/4120_CE1_CE2_T3_like_midpoint_branches.md).
- Exactly one T3-like open branch: [`../4XXX_CE1/41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1_exactly_one_T3_like_TODO.md`](../4XXX_CE1/41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1_exactly_one_T3_like_TODO.md).

### CE1, $N_+\ge2$

- Route: shared CE1/CE2 skeleton-length and set-cover routes.
- Status sources:
  - [`../4XXX_CE1/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md`](../4XXX_CE1/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md).
  - [`../4XXX_CE1/42XX_Nplus_ge2/4202_CE1_CE2_two_supercritical_set_cover_strategy.md`](../4XXX_CE1/42XX_Nplus_ge2/4202_CE1_CE2_two_supercritical_set_cover_strategy.md).

## CE2

CE2 files cite CE1 shared routes only where the hypotheses are the same.

### CE2, $N_+=0$

- All Vd0 open branch: [`../5XXX_CE2/50XX_Nplus0/500X_all_Vd0_open/5011_CE2_Nplus0_all_Vd0_TODO.md`](../5XXX_CE2/50XX_Nplus0/500X_all_Vd0_open/5011_CE2_Nplus0_all_Vd0_TODO.md).
- Vd1/Vd2 route target: [`../5XXX_CE2/50XX_Nplus0/501X_Vd1_Vd2_obstruction/5012_CE2_Nplus0_Vd1_Vd2_TODO.md`](../5XXX_CE2/50XX_Nplus0/501X_Vd1_Vd2_obstruction/5012_CE2_Nplus0_Vd1_Vd2_TODO.md).
- T3-like open branch: [`../5XXX_CE2/50XX_Nplus0/502X_T3_like_no_Vd1Vd2/5013_CE2_Nplus0_T3_like_TODO.md`](../5XXX_CE2/50XX_Nplus0/502X_T3_like_no_Vd1Vd2/5013_CE2_Nplus0_T3_like_TODO.md).

### CE2, $N_+=1$

- All Vd0 open branch: [`../5XXX_CE2/51XX_Nplus1/510X_all_Vd0/5101_CE2_Nplus1_all_Vd0_TODO.md`](../5XXX_CE2/51XX_Nplus1/510X_all_Vd0/5101_CE2_Nplus1_all_Vd0_TODO.md).
- At least two Vd1/Vd2: [`../5XXX_CE2/51XX_Nplus1/511X_at_least_two_Vd1_Vd2/5110_CE2_Nplus1_at_least_two_Vd1_Vd2_TODO.md`](../5XXX_CE2/51XX_Nplus1/511X_at_least_two_Vd1_Vd2/5110_CE2_Nplus1_at_least_two_Vd1_Vd2_TODO.md).
- Exactly one Vd1/Vd2: [`../5XXX_CE2/51XX_Nplus1/512X_exactly_one_Vd1_Vd2/5120_CE2_Nplus1_exactly_one_Vd1_Vd2_TODO.md`](../5XXX_CE2/51XX_Nplus1/512X_exactly_one_Vd1_Vd2/5120_CE2_Nplus1_exactly_one_Vd1_Vd2_TODO.md).
- At least two T3-like rows: [`../5XXX_CE2/51XX_Nplus1/513X_at_least_two_T3_like/5130_CE2_Nplus1_at_least_two_T3_like_TODO.md`](../5XXX_CE2/51XX_Nplus1/513X_at_least_two_T3_like/5130_CE2_Nplus1_at_least_two_T3_like_TODO.md).
- Exactly one T3-like row: [`../5XXX_CE2/51XX_Nplus1/514X_exactly_one_T3_like/5140_CE2_Nplus1_exactly_one_T3_like_TODO.md`](../5XXX_CE2/51XX_Nplus1/514X_exactly_one_T3_like/5140_CE2_Nplus1_exactly_one_T3_like_TODO.md).
- Warning: the May 25 five-point route is not used for all-Vd0 CE2 because of the reported CE1/CE2 failure in [`../9XXX_failed_ideas/963X_may25_five_point_failure/9630_may25_CE1_CE2_failure.md`](../9XXX_failed_ideas/963X_may25_five_point_failure/9630_may25_CE1_CE2_failure.md).

### CE2, $N_+\ge2$

- Route: shared CE1/CE2 route.
- Status source: [`../5XXX_CE2/52XX_Nplus_ge2/5200_CE2_Nplus_ge2_shared_route.md`](../5XXX_CE2/52XX_Nplus_ge2/5200_CE2_Nplus_ge2_shared_route.md).
