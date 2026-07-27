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

The common transfer notation is proved in
[`../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md).
For maps listed in row order,

$$
[\Phi_1\mid\cdots\mid\Phi_r](x)
=
(\Phi_r\circ\cdots\circ\Phi_1)(x).
$$

For a whole branch we write

$$
\mathscr C[\text{seed};\,\Phi_1\mid\cdots\mid\Phi_r;\,\text{terminal}],
$$

which records the seed data, the lower transfers retained in geometric order,
and the final capacity or separation certificate.

The raw map $g_c=1-B_c$ applies to every row.  The capped map
$G_c=\max\{g_c,\mathrm I\}$, the identity $\mathrm I$, the free envelope
$\mathsf S_c=A_{\rm sc}(c)$, selected-$T_+$ chords, thresholds, and
branch-specific radial envelopes are lower transfers in this one framework.

## Strategy 2 chain table

The table records the exact chain skeleton and the relaxations actually used.
An ``endpoint $F$'' entry means that the corresponding endpoint outgoing map
is retained exactly, while the intervening ordinary rows are replaced by
identity slots.

| branch | exact chain skeleton | relaxed chain or terminal comparison | source |
|---|---|---|---|
| $N_+=0$, all Vd0, $\mathrm{gr}=0$ | cyclic six-row capped chain | $\mathscr C[a_0;\mathrm I^6;a_0>a_0]$ | `4013` |
| $N_+=0$, all Vd0, $\mathrm{gr}=1$ | two exact endpoint $F$-maps with three middle rows | $\mathscr C[(q,s);\mathrm I^3;F_{c_1}(q)+F_{c_5}(s)<1]$ | `4013`, `2107` |
| CE2, all Vd0, $\mathrm{gr}=2$, $N_+=0$ or $1$ | two exact endpoint $F$-maps with three middle rows | $\mathscr C[(p,q);\mathrm I^3;F_{p/W}(p)+F_{q/R}(q)<1]$ | `2110`, `2108` |
| $N_+=0$, T3-like, no Vd1/Vd2 | residual inputs, two endpoint maps, three middle rows | $\mathscr C[(A_1,A_5);\mathrm I^3;F_{C_1}(A_1)+F_{C_5}(A_5)<1]$; the endpoints retain the exact four-label audit | `407X` |
| CE1, $N_+=1$, all Vd0, one gap | $[G_{c_1}\mid\cdots\mid G_{c_5}](X)$ | after exact duality, $\mathscr C[H;\mathsf L_{\alpha,1-4\alpha}\mid\mathsf L_{m,1-5m}\mid\Theta_\delta;>1-X]$ on the hard selected branch | `4105`, `4106` |
| CE2, $N_+=1$, all Vd0, one gap | $[G_{c_1}\mid\cdots\mid G_{c_5}](X)$ | either $\mathscr C[X;\mathrm I\mid\mathrm I\mid\mathrm I\mid\Theta_\alpha\mid\mathrm I;>1-H]$ or $\mathscr C[X;\mathrm I\mid\Theta_\delta\mid\mathrm I\mid\mathrm I\mid\mathrm I;>1-H]$ | `4105`, `4107` |
| $N_+=1$, one T3-like rescuer | free-supercritical source followed by the ordinary boundary path | $\mathscr C[A_{\rm sc}(c);\mathrm I^3;b_5<B_{\rm sc}(c)\le h]$ | `4132`, `2018` |
| $N_+=1$, one Vd1 adjacent rescuer | the same source and ordinary chain | $\mathscr C[A_{\rm sc}(c);\mathrm I^3;b_5<B_{\rm sc}(c)\le h]$ | `4143`, `2018` |
| CE2 adjacent Vd1/Vd2 placement | exact residuals $A,H$ and ordinary backward propagation | backward $\mathrm I^4$ plus the terminal inequality $G_{1-\delta}(1/2+A)>1-H$ | `4144` |
| CE2 nonadjacent Vd1/Vd2 placement | exact residuals followed by propagation to the exceptional row | identity slots through the intervening rows, followed by the Vd terminal inequality $c_\tau<1-\min\{A,H\}<1-d_\tau^C$ | `4146` |
| CE2 Vd1--supercritical replacement | exceptional adjacent pair | replace by two nonsupercritical Vd0 rows, then use the relevant `4013` chain | `4147` |

The hard `407X` endpoints remain exact; no unsupported universal replacement
of their four-label audit is asserted.  The `4146` terminal envelope is
Vd-type-specific rather than a universal $G_c$ bound.

The existing Strategy 1 routes are not changed.  In particular, `4040`,
`4041`, `4110`, `4111`, `4123`, `4149`, `414a`, and `4200` retain their
current perimeter or skeleton proofs and their current routing labels, even
though those additive estimates may be viewed abstractly as very coarse
envelopes.

## Terminal branch index

| File | Recorded status | Branch |
|---|---|---|
| [`40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`](40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md) | Proven | CE1/CE2, $N_+=0$, all Vd0; one signed no-gap/one-gap/two-gap proof, with the two-gap state possible only for CE2. |
| [`40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE1, $N_+=0$, at least one Vd1/Vd2; direct corollary of the common perimeter deficit. |
| [`40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE2, $N_+=0$, at least one Vd1/Vd2; direct corollary of the common perimeter deficit. |
| [`40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md`](40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md) | Proven | CE1/CE2, $N_+=0$, at least one T3-like and no Vd1/Vd2; residual endpoint chain with an irreducible exact four-label audit. |
| [`41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md) | Proven | CE1/CE2, $N_+=1$, all Vd0; one signed gap split and one common five-row interface, with separate CE1 and CE2 relaxations of the same exact chain. |
| [`41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md`](41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE1, $N_+=1$, at least one Vd1/Vd2; common perimeter budget. |
| [`41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md`](41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE2, $N_+=1$, at least two Vd1/Vd2; common perimeter budget. |
| [`41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md`](41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md) | Proven | CE1/CE2, $N_+=1$, at least two T3-like rows; three-short-role skeleton theorem. |
| [`41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md`](41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md) | Proven | CE1/CE2, $N_+=1$, exactly one T3-like; common $A_{\rm sc}$--identity--$B_{\rm sc}$ adjacent-rescuer chain. |
| [`41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md) | Proven | Surviving CE2, $N_+=1$, exactly one Vd1/Vd2; residual, free-envelope, radial-envelope, and replacement chains, with Strategy 1 complements unchanged. |
| [`42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md`](42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md) | Proven | CE1/CE2, $N_+\ge2$; two supercritical rows force a third short rescuer, so the common skeleton theorem applies. |

The May 25 five-point route is not used; see
[`../9XXX_failed_ideas/963X_may25_five_point_failure/9630_CE1_CE2_failure.md`](../9XXX_failed_ideas/963X_may25_five_point_failure/9630_CE1_CE2_failure.md)
(Status: Failed).
