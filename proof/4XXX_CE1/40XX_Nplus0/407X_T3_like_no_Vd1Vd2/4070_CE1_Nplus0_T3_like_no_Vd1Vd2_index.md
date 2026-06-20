# CE1, $N_+=0$, T3-Like With No Vd1/Vd2

Status: Strategy

This folder records the CE1-only work for the branch

$$
T_C\text{ is CE1},\qquad N_+=0,
$$

with no Vd1/Vd2 vertex roles and at least one T3-like vertex role.

## Proved reduction

The current proved reduction is recorded in
[`4071_CE1_Nplus0_T3_like_forces_V0_T3_like.md`](4071_CE1_Nplus0_T3_like_forces_V0_T3_like.md):

$$
\mathrm{CE1}+N_+=0+\text{no Vd1/Vd2}+\text{at least one T3-like}
\quad\Longrightarrow\quad
T_0\text{ is T3-like},
$$

after normalizing the unique CE1/CE2 midpoint covered by $T_C$ to $M_0$.

## Remaining branch

After this reduction, the remaining CE1 branch may assume, after the reflection
fixing $V_0$ and $M_0$ if necessary, that

$$
T_0\text{ is T3-like and }M_1\in T_0.
$$

This folder does not yet prove the resulting post-reduction branch obstruction.
It only removes the alternatives in which the T3-like roles occur away from
$V_0$.

## CE2 reuse note

The proof in `4071` uses CE1 only through the normalized exactly-one-midpoint
input for $T_C$ and the local vertex-type support conventions. The analogous CE2
branch should reference this reduction only after recording the corresponding
CE2 normalization and active-interval reductions.
