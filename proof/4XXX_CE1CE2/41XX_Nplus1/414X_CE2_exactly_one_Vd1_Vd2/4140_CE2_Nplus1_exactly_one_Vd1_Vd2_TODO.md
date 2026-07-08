# CE2, $N_+=1$, Exactly One Vd1/Vd2

Status: Strategy

The intended route is a discrete $S_{1/2}$ or diagonal set-cover fallback. No
full certificate for this branch is recorded here.

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
T_0\text{ Vd1},\qquad M_1\in T_0,\qquad T_1\text{ supercritical}
$$

is obstructed in
[`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md),
with the reflected $M_5/T_5$ case included by symmetry.

The adjacent remaining placement

$$
T_0\text{ supercritical},\qquad T_1\text{ Vd1/Vd2}
$$

is obstructed in
[`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md),
with the reflected $T_5$ placement included by symmetry.

These are local placement obstructions only; they do not by themselves close
non-adjacent Vd1 placements, the remaining $\sigma=0$ placements away from the
adjacent normalization, or the full 414X branch.

An empirical visual candidate for a cover of $S_{1/2}$ in this branch is
recorded in
[`4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md`](4141_CE2_Nplus1_one_Vd1_S_half_cover_candidate.md).
