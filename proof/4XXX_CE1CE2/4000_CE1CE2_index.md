# CE1/CE2 Branch

Status: Reference

This branch records CE1 and CE2 together. Their common center geometry is the
signed normal form
[`../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md`](../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):
one normalized trace has surplus $\Delta_R>0$, while the sign of the companion
surplus $\Delta_L$ distinguishes CE1 from CE2. All six center exits, one-gap
actual-V-triangle propagation, perimeter budgets, and skeleton budgets are shared.

Every terminal branch below is proven. Their exhaustive assembly is
[`../0XXX_main/0000_main_theorem.md`](../0XXX_main/0000_main_theorem.md).
The original vertex-role types Vd0, Vd1, Vd2, and T3-like are exhaustive by
[`../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).

## One forward envelope, one cap, and one propagation map

The common notation is proved in
[`../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md).
For selected lower bounds,

$$
M_c(a)=\max\{b:(a,b,c)\in\mathcal A\},
$$

$$
\overline M_c(a)=
\begin{cases}
1-a,&c\le1/2,\\
M_c(a),&c>1/2,
\end{cases}
\qquad
\Phi_c(a)=1-\overline M_c(a).
$$

A C-triangle interval is incorporated by applying the residual operator
$\mathcal R_J$ to $M_c(a)$ or $\overline M_c(a)$.  The strict-supercritical
source bound is $M_c^{\rm sup}$.  The authenticated 407X package retains its
older exact-cell aliases, listed in `0910`, solely to preserve blob
provenance.

For maps listed in geometric V-triangle order,

$$
[\Psi_1\mid\cdots\mid\Psi_r](x)
=(\Psi_r\circ\cdots\circ\Psi_1)(x).
$$

No separate branch-signature symbol is used; the tables state the seed,
relaxed slots, and terminal inequality in separate columns.

## Strategy 2 chain table

| branch | exact chain skeleton | relaxations retained | terminal certificate | source |
|---|---|---|---|---|
| $N_+=0$, all Vd0, $N_{\rm gap}=0$ | six direct nonsupercritical inequalities | none | strict cyclic ascent | `4013` |
| $N_+=0$, all Vd0, $N_{\rm gap}=1$ | two exact high-radial endpoint outputs and three middle rows | middle $\mathrm I^3$ | $M_{c_1}(q)+M_{c_5}(s)<1$ | `4013`, `2107` |
| CE2, all Vd0, $N_{\rm gap}=2$, $N_+=0$ or $1$ | paired exact high-radial endpoint outputs and three middle rows | middle $\mathrm I^3$ | $M_{p/W}(p)+M_{q/R}(q)<1$ | `2110`, `2108` |
| $N_+=0$, T3-like, no Vd1/Vd2 | branchwise residual endpoint inputs and three middle rows | middle $\mathrm I^3$ | low-radial Lin or high-radial four-label sum $<1$ | `407X` |
| CE1, $N_+=1$, all Vd0, one gap | $[\Phi_{c_1}\mid\cdots\mid \Phi_{c_5}](X)$ | two affine superscript relaxations and one threshold superscript | returned demand $>1-X$ | `4105`, `4106` |
| CE2, $N_+=1$, all Vd0, one gap | the same high-radial five-V-triangle chain | one threshold-decorated slot; all others $\mathrm I$ | returned demand $>1-H$ | `4105`, `4107` |
| one T3-like or adjacent Vd1 rescuer | free supercritical source and ordinary path | seed $1-M_c^{\rm sup}$, then $\mathrm I^3$ | $B_1<M_c^{\rm sup}\le h$ | `4132`, `4143`, `2018` |
| CE2 adjacent Vd1/Vd2 placement | exact residuals $A,H$ and backward ordinary chain | backward $\mathrm I^4$ | $\Phi_{1-\delta}(1/2+A)>1-H$ | `4144` |
| CE2 nonadjacent Vd1/Vd2 placement | exact residuals and intervening ordinary V triangles | identity propagation | Vd-specific terminal radial separation | `4146` |
| CE2 Vd1--supercritical replacement | exceptional adjacent pair | replace by two nonsupercritical Vd0 rows | invoke the skeleton-level `4013` obstruction | `4147` |

The hard `407X` endpoints remain exact; no unsupported universal replacement
of their four-label audit is asserted. The `4146` terminal estimate remains
Vd-type-specific rather than a universal raw-transfer bound.

The existing Strategy 1 routes are unchanged. In particular, `4040`, `4041`,
`4110`, `4111`, `4123`, `4149`, `414a`, and `4200` retain their perimeter or
skeleton proofs and their current routing labels.

## Terminal branch index

| File | Recorded status | Branch |
|---|---|---|
| [`40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`](40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md) | Proven | CE1/CE2, $N_+=0$, all Vd0; strict identity cycle and exact-endpoint chains. |
| [`40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE1, $N_+=0$, at least one Vd1/Vd2; Strategy 1. |
| [`40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE2, $N_+=0$, at least one Vd1/Vd2; Strategy 1. |
| [`40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md`](40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md) | Proven | Residual exact-endpoint chain with an irreducible four-label audit. |
| [`41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md) | Proven | One exact five-V-triangle chain with CE1 and CE2 relaxations. |
| [`41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md`](41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE1 Vd1/Vd2 Strategy 1 branch. |
| [`41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md`](41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE2 at-least-two-Vd Strategy 1 branch. |
| [`41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md`](41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md) | Proven | At-least-two-T3-like Strategy 1 branch. |
| [`41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md`](41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md) | Proven | Common $1-M_c^{\rm sup}$--identity--$M_c^{\rm sup}$ adjacent-rescuer chain. |
| [`41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md) | Proven | Residual, free-envelope, radial-envelope, and replacement chains, with Strategy 1 complements unchanged. |
| [`42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md`](42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md) | Proven | $N_+\ge2$ Strategy 1 skeleton route. |

The May 25 five-point route is not used; see
[`../9XXX_failed_ideas/963X_may25_five_point_failure/9630_may25_CE1_CE2_failure.md`](../9XXX_failed_ideas/963X_may25_five_point_failure/9630_may25_CE1_CE2_failure.md)
(Status: Failed).
