# CE2, $N_+=1$, Exactly One Vd1/Vd2 Assembly

Status: Proven

This file assembles the local obstructions in the complementary branch with
no additional positive-support row. The exhaustive classification in
[`../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md)
then says that every row other than the unique Vd1/Vd2 row is Vd0. The mixed
positive-support branch is proved separately in `414a`.

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
directly or by reduction to proved `4013`. This is complementary to the
mixed-branch obstruction in `414a`.

## Dependencies

The reduction uses the following local files.

1. [`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md): a Vd2 row covering a neighboring midpoint is impossible by the generic Vd2 cap and boundary length.
2. [`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md): the normalized pair $T_0$ Vd1, $M_1\in T_0$, $T_1$ supercritical is impossible, with reflection.
3. [`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md): the adjacent placement $T_0$ supercritical, $T_1$ Vd1/Vd2 is impossible, with reflection; its radial-envelope proof includes the exact Cell-$T$ selector.
4. [`4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md`](4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md): the non-adjacent placements $T_0$ supercritical, $T_\tau$ Vd1/Vd2 for $\tau\in\{2,3,4\}$ are impossible.
5. [`4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`](4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md): if a Vd1 row adjacent to a supercritical row rescues that row's midpoint, the pair can be replaced by two open nonsupercritical Vd0 rows preserving the boundary and radial cover.
6. [`414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md`](414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md): any additional positive-adjacent-support row gives a strict skeleton-length contradiction.
7. [`../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md): the proved all-Vd0 boundary-loss obstruction used after the replacement in `4147`.

The shared Vd1/Vd2 corner normal form is proved in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md).

## Midpoint forcing

Let $T_\sigma$ be the unique supercritical row and $T_\tau$ the unique Vd1/Vd2
row.

These rows are distinct: positive adjacent support implies
$a_\tau+b_\tau<1/2$, whereas $T_\sigma$ has
$a_\sigma+b_\sigma>1$.

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
Together with the positive-support obstruction in `414a` and the exhaustive
classification in `1201`, the full 414X package is proved.

$$
\Box
$$
