# CE2, $N_+=1$, Exactly One Vd1/Vd2 Assembly

Status: Proven

This file assembles the local obstructions in the 414X package and closes the
CE2, $N_+=1$, exactly-one-Vd1/Vd2 branch under the standard reduced hypotheses:
all vertex rows other than the unique Vd1/Vd2 row are Vd0, and there is exactly
one supercritical row.

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

and exactly one vertex row is Vd1 or Vd2.  Under the reduced 414X hypotheses,
these seven role triangles cannot cover the required target.  Hence the 414X
branch is impossible.

## Dependencies

We use the following proved local files.

1. [`4142_CE2_Nplus1_Vd2_midpoint_local_caps.md`](4142_CE2_Nplus1_Vd2_midpoint_local_caps.md): Vd2 rows covering adjacent midpoint subsets have boundary contribution below the required 414X perimeter threshold.
2. [`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md): the normalized pair $T_0$ Vd1, $M_1\in T_0$, $T_1$ supercritical is impossible, with reflection.
3. [`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md): the adjacent placement $T_0$ supercritical, $T_1$ Vd1/Vd2 is impossible, with reflection.
4. [`4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md`](4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md): the non-adjacent placements $T_0$ supercritical, $T_\tau$ Vd1/Vd2 for $\tau\in\{2,3,4\}$ are impossible.
5. [`4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`](4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md): if a Vd1 row adjacent to a supercritical row rescues that row's midpoint, the pair can be replaced by two nonsupercritical Vd0 rows, reducing to the all-Vd0 CE2 boundary-loss obstruction.

The Vd1/Vd2 corner-side normal form needed by the local files is proved in
[`4145_Vd1_Vd2_corner_side_normal_form.md`](4145_Vd1_Vd2_corner_side_normal_form.md).

## Midpoint forcing

Let $T_\sigma$ be the unique supercritical row and $T_\tau$ the unique Vd1/Vd2
row.

A supercritical Vd0 row does not cover its own midpoint in the reduced
skeleton/midpoint accounting.  Since $T_C$ covers exactly $M_0$, if
$\sigma\ne0$, the midpoint $M_\sigma$ must be covered by the unique Vd1/Vd2 row.
An ordinary Vd0 row has no positive-length adjacent-ray support, so it cannot
rescue a neighboring midpoint.  Therefore, when $\sigma\ne0$, the Vd1/Vd2 row
must be adjacent to $T_\sigma$ and must contain $M_\sigma$.

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
adjacent-midpoint case is eliminated by `4142`.

If $T_0$ is Vd1 and covers the neighboring midpoint $M_\sigma$, then the pair
is the normalized obstruction of `4143`, after reflection if $\sigma=5$.

Thus no candidate exists with $\tau=0$.

### Case 3: $\sigma\ne0$ and $\tau\ne0$

If $T_\tau$ is not adjacent to $T_\sigma$, then $M_\sigma$ is uncovered by the
midpoint forcing observation.  Hence $T_\tau$ must be adjacent to $T_\sigma$ and
must cover $M_\sigma$.

If $T_\tau$ is Vd2, then it is a Vd2 row covering a neighboring midpoint.  This
is eliminated by the Vd2 midpoint cap obstruction in `4142`.

If $T_\tau$ is Vd1, then the adjacent Vd1--supercritical rescue pair is
eliminated by the axis-replacement argument of `4147`.

Thus no candidate exists in this case.

## Conclusion

Every possible placement of the unique supercritical row and the unique
Vd1/Vd2 row falls into one of the three cases above, and every case is
impossible.  Therefore the CE2, $N_+=1$, exactly-one-Vd1/Vd2 branch is closed.

$$
\Box
$$
