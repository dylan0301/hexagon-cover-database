# CE2, $N_+=1$, Exactly One Vd1/Vd2

Status: Strategy

This branch is not yet recorded as a complete theorem.  Several local
placements are now proved, but the package still needs a final assembly or an
additional obstruction for the remaining Vd1 adjacent-rescue placements where
the unique supercritical row is not $T_0$.

The Vd1/Vd2 corner-side normal form used by the local obstruction files is
proved in
[`4145_Vd1_Vd2_corner_side_normal_form.md`](4145_Vd1_Vd2_corner_side_normal_form.md).

A proved local cap for the Vd2 midpoint-rescue subcases is recorded in
[`4142_CE2_Nplus1_Vd2_midpoint_local_caps.md`](4142_CE2_Nplus1_Vd2_midpoint_local_caps.md).
It shows that Vd2 rows whose exact local midpoint subset is one of

$$
\{M_0,M_1\},\qquad \{M_0,M_5\},\qquad \{M_5,M_0,M_1\}
$$

have adjacent boundary contribution below the reduced 414X perimeter threshold
needed to survive the CE2, $N_+=1$ accounting.

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

These files close the placements in which the unique supercritical row is
adjacent to $T_0$ as above or is itself $T_0$.  They do not yet record a full
case assembly for every possible position of a Vd1 row that rescues a
supercritical row away from the CE2-active vertex.  Until that final assembly or
additional obstruction is supplied, this index remains `Status: Strategy`.

An empirical visual candidate for a cover of $S_{1/2}$ in this branch is
recorded in
[`4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md`](4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md).
