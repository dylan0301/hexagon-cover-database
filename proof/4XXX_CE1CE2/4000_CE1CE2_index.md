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

No separate branch-signature symbol is used. The detailed crosswalk identified
below states the seed, relaxed slots, and terminal inequality separately.

## Nonzero-gap Method 2 and hybrid routing

The gap-first tree removes $N_{\rm gap}=0$ before this routing. At zero gap,
the common boundary-complete consequences `2500`, `3174`, and `3208` give
Methods 1 or 3 according to $N_+$ and the V-type counts, while the
$N_+=1$ all-Vd0 cell uses the center-independent Method 4 result `31058`.
Consequently every Method 2 invocation here has
$N_{\rm gap}\in\{1,2\}$.

The detailed combinatorial case-to-chain crosswalk is retained in the
`Method 2 combinatorial chains` section of
`proof/0XXX_main/0001_proof_tree_index.md`.
Its exact branch owners are `4013` for the all-Vd0 endpoint chains, `4070`
for the T3-like endpoint package, `4101` for the exactly-one-supercritical
all-Vd0 chains, and `4130` for the exactly-one-T3-like adjacent-rescuer
chain. The CE2 one-Vd1/Vd2 hybrid is indexed in
[`4140`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md),
assembled in
[`4148`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md),
and independently audited in
[`414b`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/414b_complete_placement_reaudit.md).

The hard `407X` endpoints remain exact; no unsupported universal replacement
of their four-label audit is asserted. The `4146` terminal estimate remains
Vd-type-specific rather than a universal raw-transfer bound. In the `4147`
replacement branch, the output rank $N'_{\rm gap}$ is recomputed: rank $0$
uses Method 1 `2500`, while ranks $1$ and $2$ use the nonzero-gap Method 2
part of `4013`. No preservation of the original gap rank is asserted.

The nonzero-gap Method 1 routes are unchanged. In particular, `4040`,
`4041`, `4110`, `4111`, `4123`, `4149`, `414a`, and `4200` retain their
perimeter or skeleton proofs and their current routing labels. The outer
zero-gap routing changes ownership, not any of those inequalities.

## Detailed `414X` placement pointer

The original zero-gap state is first closed by Method 1, so the placement
audit has the standing hypothesis $N_{\rm gap}\in\{1,2\}$. The detailed
entry reduction and six placement rows are retained in the
`Detailed 414X placement audit` section of
`proof/0XXX_main/0001_proof_tree_index.md`. The local package entry is `4140`,
the proved assembly is `4148`, and the hypothesis-by-hypothesis exhaustive
audit is `414b`. The `4147` output is routed only after recomputing
$N'_{\rm gap}$; neither the assembly nor the audit claims gap preservation.

## Terminal branch index

| File | Recorded status | Branch |
|---|---|---|
| [`40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`](40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md) | Proven | CE1/CE2, $N_+=0$, all Vd0; Method 1 strict zero-gap cycle and Method 2 nonzero-gap endpoint chains. |
| [`40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE1, $N_+=0$, at least one Vd1/Vd2; Method 1. |
| [`40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE2, $N_+=0$, at least one Vd1/Vd2; Method 1. |
| [`40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md`](40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md) | Proven | Nonzero-gap residual exact-endpoint chain with an irreducible four-label audit. |
| [`41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md) | Proven | Method 4 at zero gap and Method 2 exact chains at nonzero gap. |
| [`41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md`](41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE1 Vd1/Vd2 Method 1 branch. |
| [`41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md`](41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE2 at-least-two-Vd Method 1 branch. |
| [`41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md`](41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md) | Proven | At-least-two-T3-like Method 1 branch. |
| [`41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md`](41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md) | Proven | Nonzero-gap $1-M_c^{\rm sup}$--identity--$M_c^{\rm sup}$ adjacent-rescuer chain. |
| [`41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md`](41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md) | Proven | Nonzero-gap entry reduction `414a` and six placements, including the post-replacement Method 1/2 gap router. |
| [`42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md`](42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md) | Proven | $N_+\ge2$ Method 1 skeleton route. |

The May 25 five-point route is not used; see
[`../9XXX_failed_ideas/963X_may25_five_point_failure/9630_may25_CE1_CE2_failure.md`](../9XXX_failed_ideas/963X_may25_five_point_failure/9630_may25_CE1_CE2_failure.md)
(Status: Failed).
