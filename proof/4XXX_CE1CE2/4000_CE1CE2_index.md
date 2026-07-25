# CE1/CE2 Branch

Status: Reference

This branch records CE1 and CE2 together. Their common center geometry is the
signed normal form
[`../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):
one normalized trace has surplus $\Delta_R>0$, while the sign of the companion
surplus $\Delta_L$ distinguishes CE1 from CE2. All six center exits, one-gap
actual-row propagation, perimeter budgets, and skeleton budgets are shared.
CE2-only rows remain only when a positive companion trace or a surviving
boundary budget is genuinely required.

Every terminal branch below is proven. Their exhaustive assembly is
[`../0XXX_main/0000_main_theorem.md`](../0XXX_main/0000_main_theorem.md).
The original vertex-role types Vd0, Vd1, Vd2, and T3-like are exhaustive by
[`../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).

| File | Recorded status | Branch |
|---|---|---|
| [`40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`](40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md) | Proven | CE1/CE2, $N_+=0$, all Vd0; one signed no-gap/one-gap/two-gap proof, with the two-gap state possible only for CE2. |
| [`40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE1, $N_+=0$, at least one Vd1/Vd2; direct corollary of the common perimeter deficit. |
| [`40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE2, $N_+=0$, at least one Vd1/Vd2; direct corollary of the common perimeter deficit. |
| [`40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md`](40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md) | Proven | CE1/CE2, $N_+=0$, at least one T3-like and no Vd1/Vd2; shared center side model and universal selected-$T_+$ curve. |
| [`41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md) | Proven | CE1/CE2, $N_+=1$, all Vd0; one signed gap split and one common five-row interface, with separate CE1 and CE2 scalar clauses only where necessary. |
| [`41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md`](41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE1, $N_+=1$, at least one Vd1/Vd2; common perimeter budget. |
| [`41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md`](41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE2, $N_+=1$, at least two Vd1/Vd2; common perimeter budget. |
| [`41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md`](41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md) | Proven | CE1/CE2, $N_+=1$, at least two T3-like rows; three-short-role skeleton theorem. |
| [`41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md`](41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md) | Proven | CE1/CE2, $N_+=1$, exactly one T3-like; common adjacent-rescuer center-hiding theorem. |
| [`41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md) | Proven | Surviving CE2, $N_+=1$, exactly one Vd1/Vd2; short common-slack adjacent and nonadjacent proofs, plus replacement to proved `4013`. |
| [`42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md`](42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md) | Proven | CE1/CE2, $N_+\ge2$; two supercritical rows force a third short rescuer, so the common skeleton theorem applies. |

The May 25 five-point route is not used; see
[`../9XXX_failed_ideas/963X_may25_five_point_failure/9630_may25_CE1_CE2_failure.md`](../9XXX_failed_ideas/963X_may25_five_point_failure/9630_may25_CE1_CE2_failure.md)
(Status: Failed).
