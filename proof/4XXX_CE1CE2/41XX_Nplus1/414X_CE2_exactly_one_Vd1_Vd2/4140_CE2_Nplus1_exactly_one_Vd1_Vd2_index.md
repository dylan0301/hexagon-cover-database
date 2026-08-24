# CE2, $N_+=1$, Exactly One Vd1/Vd2

Status: Proven

The complete placement assembly is `4148`; the independent post-repair audit
is `414b`.

In the gap-first assembly this package has the standing hypothesis

$$
N_{\rm gap}\in\{1,2\}.
$$

The original zero-gap state is removed before the placement audit: the six
open V roles cover $\partial H$, and the common $N_+=1$ Vd1/Vd2
boundary-complete consequence
[`2500`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md#boundary-complete-zero-gap-consequences)
closes it by Method 1.

## Four-part route digest

The detailed placement table is retained in the `Detailed 414X placement
audit` section of `proof/0XXX_main/0001_proof_tree_index.md`.
The proved assembly is
[`4148`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md), and the complete
hypothesis-by-hypothesis audit is
[`414b`](414b_complete_placement_reaudit.md). Within the standing nonzero-gap
branch, `414a` removes the additional-positive-support alternative. On its
complement, $\sigma=0$ routes to `4144` or `4146`, $\tau=0$ routes to `4143`
or `4149`, and $\sigma\ne0$, $\tau\ne0$ routes to `4147` or `4149`, according
to adjacency and the Vd1/Vd2 type recorded in the detailed audit.

The former single-chart formula in `4147` has been removed. The replacement
at the first distinguished vertex is constructed in its own local chart, and
the replacement at the adjacent distinguished vertex is constructed in the
adjacent vertex's chart. `4013` is now stated at the skeleton-data strength
actually used by the argument.  The replacement does not assert preservation
of $N_{\rm gap}$: its output rank $N'_{\rm gap}$ is recomputed before choosing
the Method 1 or Method 2 terminal.

## Files

| File | Status | Role |
|---|---|---|
| `4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md` | Empirical | historical visualization only |
| [`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md) | Proven | Vd1 adjacent rescuer |
| [`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md) | Proven | adjacent residual/radial obstruction |
| [`4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md`](4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md) | Proven | nonadjacent radial obstruction |
| [`4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`](4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md) | Proven | corrected two-chart skeleton-preserving replacement |
| [`4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md) | Proven | assembly |
| [`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md) | Proven | Vd2 perimeter terminal |
| [`414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md`](414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md) | Proven | positive-support complement |
| [`414b_complete_placement_reaudit.md`](414b_complete_placement_reaudit.md) | Proven | exhaustive post-repair audit |
