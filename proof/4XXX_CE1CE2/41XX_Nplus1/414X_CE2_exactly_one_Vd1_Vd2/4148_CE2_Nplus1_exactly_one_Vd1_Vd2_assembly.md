# CE2, $N_+=1$, Exactly One Vd1/Vd2 Assembly

Status: Proven

This file assembles the local obstructions after the proved zero-support
classification in `414c`: all vertex rows other than the unique Vd1/Vd2 row
are Vd0, and there is exactly one supercritical row.

The exact-formula blockers in `4144`, `4145`, and `4147` are repaired. This
file proves that the entire no-additional-positive-support subbranch reduces
to the now-proved `4013` boundary-loss package. The complementary mixed
Vd1/Vd2--T3-like branch is proved separately in `414a`.

## Statement

Assume

$$
T_C\text{ is CE2},
\qquad
T_C\cap\{M_0,\dots,M_5\}=\{M_0\},
$$

$$
N_+=1,
$$

and exactly one vertex row is Vd1 or Vd2. Under the complementary
no-additional-positive-support hypothesis, every candidate is contradicted
directly or by reduction to proved `4013`. The proved classification bridge
`414c` identifies every other zero-support row as Vd0. This statement is the
complementary reduction to the mixed-branch obstruction in `414a`.

## Dependencies

The reduction uses the following local files.

1. [`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md): a Vd2 row covering a neighboring midpoint is impossible by the Vd2 local caps from [`4142`](4142_CE2_Nplus1_Vd2_midpoint_local_caps.md) and boundary length.
2. [`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md): the normalized pair $T_0$ Vd1, $M_1\in T_0$, $T_1$ supercritical is impossible, with reflection.
3. [`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md): the adjacent placement $T_0$ supercritical, $T_1$ Vd1/Vd2 is impossible, with reflection; its radial-envelope proof includes the exact Cell-$T$ selector.
4. [`4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md`](4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md): the non-adjacent placements $T_0$ supercritical, $T_\tau$ Vd1/Vd2 for $\tau\in\{2,3,4\}$ are impossible.
5. [`4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`](4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md): if a Vd1 row adjacent to a supercritical row rescues that row's midpoint, the pair can be replaced by two open nonsupercritical Vd0 rows preserving the boundary and radial cover. The radial bridge used there is proved in [`414b`](414b_CE2_Vd1_axis_replacement_radial_bridge_target.md).

The Vd1/Vd2 corner-side normal form and adjacent-ray bound needed by the local
files are proved in
[`4145_Vd1_Vd2_corner_side_normal_form.md`](4145_Vd1_Vd2_corner_side_normal_form.md).

## Midpoint forcing

Let $T_\sigma$ be the unique supercritical row and $T_\tau$ the unique Vd1/Vd2
row.

A supercritical Vd0 row covers none of its local midpoints.  Since $T_C$ covers
exactly $M_0$, if $\sigma\ne0$, the midpoint $M_\sigma$ must be covered by the
unique Vd1/Vd2 row.  An ordinary Vd0 row has no positive-length adjacent-ray
support and cannot rescue a neighboring midpoint.  Therefore, when
$\sigma\ne0$, the Vd1/Vd2 row must be adjacent to $T_\sigma$ and must contain
$M_\sigma$.

If $\sigma=0$, then the missing midpoint $M_0$ of the supercritical row is
already supplied by $T_C$; no adjacent midpoint rescue is forced by $M_0$.

## Case split

### Case 1: $\sigma=0$

Here $T_0$ is the unique supercritical row.

If $\tau=1$ or $\tau=5$, then the Vd1/Vd2 row is adjacent to $T_0$.  This is
exactly the adjacent obstruction proved in `4144`, after reflection if needed.

If $\tau\in\{2,3,4\}$, then the Vd1/Vd2 row is non-adjacent to $T_0$.  This is
exactly the non-adjacent obstruction proved in `4146`.

Thus no candidate exists with $\sigma=0$.

### Case 2: $\tau=0$

Here $T_0$ is the unique Vd1/Vd2 row, and the unique supercritical row is not
$T_0$.

By midpoint forcing, the supercritical row must be adjacent to $T_0$, so

$$
\sigma\in\{1,5\}.
$$

If $T_0$ is Vd2 and covers the neighboring midpoint $M_\sigma$, then the Vd2
neighbor-midpoint rescue is eliminated by `4149`.

If $T_0$ is Vd1 and covers the neighboring midpoint $M_\sigma$, then the pair
is the normalized obstruction of `4143`, after reflection if $\sigma=5$.

Thus no candidate exists with $\tau=0$.

### Case 3: $\sigma\ne0$ and $\tau\ne0$

If $T_\tau$ is not adjacent to $T_\sigma$, then $M_\sigma$ is uncovered by the
midpoint forcing observation.  Hence $T_\tau$ must be adjacent to $T_\sigma$ and
must cover $M_\sigma$.

If $T_\tau$ is Vd2, then it is a Vd2 row covering a neighboring midpoint.  This
is eliminated by the Vd2 neighbor-midpoint obstruction in `4149`.

If $T_\tau$ is Vd1, then the adjacent Vd1--supercritical rescue pair is
contradicted by the axis-replacement argument of `4147` and proved `4013`.

Thus the Vd2 alternative is impossible, and the Vd1 alternative is impossible
by reduction to proved `4013`.

## Conclusion

Every placement of the unique supercritical row and the unique Vd1/Vd2 row
within the all-other-rows-Vd0 hypothesis falls into one of the three cases
above. Each case is contradicted directly or reduced by `4147` to proved
`4013`.
Together with the stronger positive-support obstruction in `414a` and the
proved zero-support classification in `414c`, the full 414X package is
proved.

$$
\Box
$$
