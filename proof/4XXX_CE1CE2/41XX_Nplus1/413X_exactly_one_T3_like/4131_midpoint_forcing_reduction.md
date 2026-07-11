# CE1/CE2, $N_+=1$, Exactly One T3-Like: Midpoint Reduction

Status: Proven

This file records the midpoint-counting reduction used by the shared
CE1/CE2 exactly-one-T3-like branch. The final boundary obstruction is recorded
in
[`4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md`](4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md).

## Statement

Assume a seven-role cover of the full skeleton is in the branch

$$
T_C,\ T_0,\dots,T_5,
$$

where $T_C$ is CE1 or CE2 and $O\in\mathrm{int}(T_C)$. Normalize by the
CE1/CE2 exactly-one-midpoint lemma so that

$$
T_C\cap\{M_0,\dots,M_5\}=\{M_0\}.
$$

Assume further that, among the six vertex rows,

$$
N_+=\left\lvert \left\lbrace i : a_i+b_i>1 \right\rbrace \right\rvert=1,
$$

there is exactly one T3-like row, and no row is Vd1 or Vd2. Equivalently, the
remaining four non-supercritical, non-T3-like rows are Vd0 rows.

Use the following local midpoint dependencies.

1. Since this is a full-skeleton cover and $T_C$ covers only $M_0$, every
   midpoint $M_1,\dots,M_5$ must be covered by vertex roles.
2. A T3-like row $T_i$ does not contain $M_i$.
3. A supercritical row contains none of its three local midpoints.
4. A Vd0 row has no positive-length adjacent-ray intersection and therefore
   cannot cover an adjacent midpoint.
5. In the present midpoint-forcing branch, each Vd0 row covers its own
   midpoint.

Then, after possibly reflecting across the axis through $O$ and $V_0$,

$$
\boxed{T_0\text{ is the unique T3-like row, }M_1\in T_0,\text{ and }T_1
\text{ is the unique supercritical row}.}
$$

Consequently,

$$
T_2,T_3,T_4,T_5
$$

are Vd0 rows satisfying

$$
a_i+b_i\le1,\qquad i=2,3,4,5.
$$

## Proof

Let $\tau$ be the index of the unique T3-like row. By the T3-like midpoint
exclusion,

$$
M_\tau\notin T_\tau.
$$

Suppose first that $\tau\ne0$. Then $M_\tau$ is not covered by $T_C$, because
$T_C$ covers only $M_0$ among the six midpoints. It is not covered by
$T_\tau$, as just noted. It is not covered by the unique supercritical row,
because supercritical rows contain no local midpoints. Finally, no Vd0 row can
cover $M_\tau$ unless it is the row based at $V_\tau$, because a Vd0 row
cannot cover an adjacent midpoint; but the row based at $V_\tau$ is the
T3-like row, not a Vd0 row. Hence $M_\tau$ would be uncovered, contradicting
coverage of the six radial midpoints. Therefore

$$
\tau=0.
$$

Thus $T_0$ is the unique T3-like row.

Let $\sigma$ be the index of the unique supercritical row. Since $T_0$ is
T3-like and T3-like rows are nonsupercritical, $\sigma\ne0$.

If $\sigma\notin\{1,5\}$, then the midpoint $M_\sigma$ is not covered by
$T_C$, because $\sigma\ne0$. It is not covered by $T_\sigma$, because
$T_\sigma$ is supercritical. It is not covered by $T_0$, because $M_\sigma$ is
not local to $T_0$. As before, no Vd0 row can rescue an adjacent midpoint, and
every non-supercritical non-T3-like row in this branch is Vd0. Thus
$M_\sigma$ would be uncovered, contradicting coverage of the six radial
midpoints. Therefore

$$
\sigma\in\{1,5\}.
$$

If $\sigma=1$, then $M_1$ cannot be covered by $T_C$, $T_1$, or any Vd0 row.
Hence full-skeleton coverage forces

$$
M_1\in T_0.
$$

If $\sigma=5$, the reflected argument gives $M_5\in T_0$. The reflection fixing
$O,V_0,M_0$ swaps $M_1$ with $M_5$ and preserves the branch hypotheses.
Therefore we may assume

$$
M_1\in T_0,\qquad \sigma=1.
$$

That is,

$$
T_0\text{ is T3-like with }M_1\in T_0,
\qquad
T_1\text{ is supercritical}.
$$

The four remaining rows are neither supercritical nor T3-like, and by the
branch assumption no row is Vd1 or Vd2. Hence they are Vd0 rows. Since they
are not supercritical,

$$
a_i+b_i\le1,\qquad i=2,3,4,5.
$$

This proves the reduction.
