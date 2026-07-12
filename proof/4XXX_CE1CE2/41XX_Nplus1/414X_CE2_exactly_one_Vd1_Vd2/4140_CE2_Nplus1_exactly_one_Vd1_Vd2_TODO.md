# CE2, $N_+=1$, Exactly One Vd1/Vd2

Status: Reduction

This branch has a proved reduction assembly in
[`4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md).

The exact-formula reaudit repairs the Cell-$T$ selector calculation in `4144`,
the Vd1/Vd2 normal-form degeneracy in `4145`, and the explicit Vd0
replacements in `4147`. The complementary assembly first uses the Vd0
normalization target `414c`, then reduces to the radial bridge target `414b`
and the named `4013` boundary-loss dependency.

Mixed configurations with exactly one Vd1/Vd2 row and one or more T3-like
rows are now eliminated by the skeleton-length contradiction in
[`414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md`](414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md).
Thus the terminal dependencies of this package are `414c`, `414b`, and
`4013`. The
`Reduction` status certifies this routing; it does not by itself certify either
terminal dependency.

The Vd1/Vd2 corner-side normal form and adjacent-ray bound used by the local
obstruction files are proved in
[`4145_Vd1_Vd2_corner_side_normal_form.md`](4145_Vd1_Vd2_corner_side_normal_form.md).

A proved local cap for Vd2 midpoint-rescue subcases is recorded in
[`4142_CE2_Nplus1_Vd2_midpoint_local_caps.md`](4142_CE2_Nplus1_Vd2_midpoint_local_caps.md).
Its global use in the reduced no-T3-like subbranch is recorded in
[`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md).

The normalized adjacent-rescue Vd1 case

$$
T_0\text{ Vd1},\qquad M_1\in T_0,
\qquad T_1\text{ supercritical}
$$

is obstructed in
[`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md),
with the reflected $M_5/T_5$ case included by symmetry.

The adjacent placement

$$
T_0\text{ supercritical},\qquad T_1\text{ Vd1/Vd2}
$$

is obstructed in
[`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md),
with the reflected $T_5$ placement included by symmetry.

The non-adjacent placements

$$
T_0\text{ supercritical},\qquad T_\tau\text{ Vd1/Vd2},
\qquad \tau\in\{2,3,4\}
$$

are obstructed in
[`4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md`](4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md).

The remaining adjacent-rescue placement where the unique supercritical row is
not $T_0$ has a proved local axis replacement in
[`4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`](4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md),
but its final contradiction still uses the CE1/CE2 all-Vd0 boundary-loss
package.

The case split tying these local files together is recorded in `4148`.

The complete package split is therefore:

- every subbranch with an additional positive-support row, including the
  mixed Vd1/Vd2--T3-like subbranch, is `Proven` in `414a`;
- the complementary no-additional-positive-support subbranch is reduced by
  `4148` and `4147` to
  `414c`, `414b`, and `4013`.

An empirical visual candidate for a cover of $S_{1/2}$ in this branch is
recorded in
[`4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md`](4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md).
It is retained only as empirical history; it is not used in the proof.
