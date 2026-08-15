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

## One transfer alphabet

The common notation is proved in
[`../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md).
The only transfer family is the raw defect map

$$
g_c(x)
=
\max\left\{
y:(1-x,y,c)\in\mathcal A
\right\}.
$$

For any map $f$,

$$
f^\vee(a)=1-f(1-a).
$$

A nonsupercritical role is handled branchwise.  For radial demand at most
$1/2$, use $B\le1-A$ directly.  For radial demand above $1/2$, use the raw
map $g_c$; midpoint forcing gives $g_c(x)\le x$, so $g_c^\vee$ is extensive.
Center intervals use the same split after applying the residual operator. The
single free strict-supercritical outgoing envelope is

$$
g_c^{\rm sc}
=
\sup_{\{x:g_c(x)>x\}}g_c(x).
$$

The exact appendix aliases are

$$
B_c(a)=g_c(1-a),
\qquad
F_c(a)=
\begin{cases}
1-a,&c\le1/2,\\
B_c(a),&c>1/2,
\end{cases}
\qquad
G_c(a)=1-F_c(a).
$$

For maps listed in geometric row order,

$$
[\Phi_1\mid\cdots\mid\Phi_r](x)
=
(\Phi_r\circ\cdots\circ\Phi_1)(x).
$$

No separate branch-signature symbol is used; the tables state the seed,
relaxed slots, and terminal inequality in separate columns.

## Strategy 2 chain table

| branch | exact chain skeleton | relaxations retained | terminal certificate | source |
|---|---|---|---|---|
| $N_+=0$, all Vd0, $\mathrm{gr}=0$ | six direct nonsupercritical inequalities | none | strict cyclic ascent | `4013` |
| $N_+=0$, all Vd0, $\mathrm{gr}=1$ | two exact high-radial endpoint outputs and three middle rows | middle $\mathrm I^3$ | $g_{c_1}(1-q)+g_{c_5}(1-s)<1$ | `4013`, `2107` |
| CE2, all Vd0, $\mathrm{gr}=2$, $N_+=0$ or $1$ | paired exact high-radial endpoint outputs and three middle rows | middle $\mathrm I^3$ | $g_{p/W}(1-p)+g_{q/R}(1-q)<1$ | `2110`, `2108` |
| $N_+=0$, T3-like, no Vd1/Vd2 | branchwise residual endpoint inputs and three middle rows | middle $\mathrm I^3$ | low-radial Full or high-radial four-label sum $<1$ | `407X` |
| CE1, $N_+=1$, all Vd0, one gap | $[g_{c_1}^\vee\mid\cdots\mid g_{c_5}^\vee](X)$ | two affine superscript relaxations and one threshold superscript | returned demand $>1-X$ | `4105`, `4106` |
| CE2, $N_+=1$, all Vd0, one gap | the same high-radial five-V-triangle chain | one threshold-decorated slot; all others $\mathrm I$ | returned demand $>1-H$ | `4105`, `4107` |
| one T3-like or adjacent Vd1 rescuer | free supercritical source and ordinary path | seed $1-g_c^{\rm sc}$, then $\mathrm I^3$ | $b_5<g_c^{\rm sc}\le h$ | `4132`, `4143`, `2018` |
| CE2 adjacent Vd1/Vd2 placement | exact residuals $A,H$ and backward ordinary chain | backward $\mathrm I^4$ | $g_{1-\delta}^\vee(1/2+A)>1-H$ | `4144` |
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
| [`41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md`](41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md) | Proven | Common $1-g_c^{\rm sc}$--identity--$g_c^{\rm sc}$ adjacent-rescuer chain. |
| [`41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md) | Proven | Residual, free-envelope, radial-envelope, and replacement chains, with Strategy 1 complements unchanged. |
| [`42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md`](42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md) | Proven | $N_+\ge2$ Strategy 1 skeleton route. |

The May 25 five-point route is not used; see
[`../9XXX_failed_ideas/963X_may25_five_point_failure/9630_may25_CE1_CE2_failure.md`](../9XXX_failed_ideas/963X_may25_five_point_failure/9630_may25_CE1_CE2_failure.md)
(Status: Failed).
