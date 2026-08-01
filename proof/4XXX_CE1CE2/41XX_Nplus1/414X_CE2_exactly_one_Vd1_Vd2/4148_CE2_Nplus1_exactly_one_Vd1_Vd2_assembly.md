# CE2, $N_+=1$, Exactly One Vd1/Vd2 Assembly

Status: Proven

This file assembles the local obstructions in the complementary branch with
no additional positive-support V triangle. The exhaustive classification in
[`1201`](../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md)
then says that every V triangle other than the unique Vd1/Vd2 V triangle is Vd0. The mixed
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

and exactly one vertex V triangle is Vd1 or Vd2. Under the complementary
no-additional-positive-support hypothesis, every candidate is contradicted
directly or by reduction to proved `4013`. Together with `414a`, this proves
the full branch.

## Dependencies

1. [`4149`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md): a Vd2 V triangle
   covering a neighboring midpoint is impossible by the exact Vd2 cap and
   boundary length.
2. [`4143`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md): the
   normalized Vd1 neighboring-midpoint rescuer is impossible by the common
   center-hiding and strict-supercritical envelope argument.
3. [`4144`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md):
   the adjacent placement with $T_0$ supercritical is impossible by exact
   center residuals, the center quarter margin, the Vd supported-arm margin,
   and the global quarter radial envelope `201b`.
4. [`4146`](4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md):
   the nonadjacent placements are impossible by a Vd-specific own-radial
   separation.
5. [`4147`](4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md): an
   adjacent Vd1--supercritical rescue pair away from $T_0$ is replaced by two
   open nonsupercritical Vd0 V triangles preserving all required boundary and radial
   data.
6. [`414a`](414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md): an
   additional positive-adjacent-support V triangle gives the three-short-role
   skeleton contradiction.
7. [`4013`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md):
   the all-Vd0 boundary-loss obstruction used after `4147`.

The shared Vd corner normal form is [`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md).
The residual/path mechanism is the corrected [`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md).

## Midpoint forcing

Let $T_\sigma$ be the unique supercritical V triangle and $T_\tau$ the unique
Vd1/Vd2 V triangle. They are distinct: a Vd1/Vd2 V triangle has boundary sum below $1/2$,
whereas $T_\sigma$ has boundary sum above one.

A supercritical Vd0 V triangle misses its own local midpoint. Since the center covers
exactly $M_0$, if $\sigma\ne0$, the point $M_\sigma$ must be covered by a
neighboring vertex role. Every other ordinary V triangle is Vd0 and has no positive
adjacent-arm support. Therefore the unique Vd1/Vd2 V triangle must be adjacent to
$T_\sigma$ and must contain $M_\sigma$.

If $\sigma=0$, the center already covers the midpoint missed by the
supercritical V triangle, so no adjacent rescue follows from $M_0$.

## Exhaustive case split

### Case 1: $\sigma=0$

Here $T_0$ is the unique supercritical V triangle.

- If $\tau=1$ or $\tau=5$, the Vd1/Vd2 V triangle is adjacent. This is `4144`, after
  reflection when necessary.
- If $\tau\in\{2,3,4\}$, this is the nonadjacent obstruction `4146`.

Thus no candidate has $\sigma=0$.

### Case 2: $\tau=0$

Here $T_0$ is the unique Vd1/Vd2 V triangle and $\sigma\ne0$. Midpoint forcing gives
$\sigma\in\{1,5\}$.

- If $T_0$ is Vd2, `4149` applies.
- If $T_0$ is Vd1, the pair is `4143`, after reflection when $\sigma=5$.

Thus no candidate has $\tau=0$.

### Case 3: $\sigma\ne0$ and $\tau\ne0$

Midpoint forcing makes $T_\tau$ adjacent to $T_\sigma$ and forces
$M_\sigma\in T_\tau$.

- If $T_\tau$ is Vd2, `4149` applies.
- If $T_\tau$ is Vd1, the pair lies away from $T_0$. The two positive center
  boundary traces are on $e_{5,0}$ and $e_{0,1}$, whereas the shared edge of
  two adjacent V triangles neither of which is $T_0$ is center-free. Thus all
  hypotheses of `4147` hold. Replace the pair by two open nonsupercritical Vd0
  V triangles and invoke proved `4013`.

Both alternatives are impossible.

## Conclusion

Every placement of the unique supercritical V triangle and the unique Vd1/Vd2 V triangle in
the no-additional-support branch belongs to one of the three cases above.
Together with `414a` and the exhaustive vertex classification, this proves the
full exactly-one-Vd1/Vd2 branch.

$$
\Box
$$
