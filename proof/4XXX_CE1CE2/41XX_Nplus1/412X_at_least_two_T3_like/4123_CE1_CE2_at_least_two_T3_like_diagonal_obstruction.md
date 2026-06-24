# CE1/CE2 At Least Two T3-Like Diagonal Obstruction

Status: Practically proven

This file records the shared CE1/CE2 diagonal-length obstruction for the
branch:

$$
T_C\text{ is CE1 or CE2},
$$

$$
N_+=\left\lvert \left\lbrace i : a_i+b_i>1 \right\rbrace \right\rvert=1,
$$

no $V_i$-triangle is Vd1 or Vd2, and at least two $V_i$-triangles are T3-like.

## Inputs

The diagonal target is

$$
D=\bigcup_{i=0}^5 r_i,
$$

with

$$
\mathcal H^1(D)=6.
$$

The reduced diagonal-length caps are recorded in
[`../../../2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md)
(Status: Practically proven).

T3-like rows are nonsupercritical by
[`../../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md`](../../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md)
(Status: Practically proven). Therefore, in the $N_+=1$ branch, the unique
supercritical vertex row is Vd0.

## Diagonal length accounting

The worst possible reduced diagonal-length accounting has:

- one CE1/CE2 center role;
- one supercritical Vd0 row;
- two T3-like rows;
- three nonsupercritical Vd0 rows.

Using the caps from the diagonal-length package gives

$$
\frac32+\frac12+2\cdot\frac12+3\cdot1=6.
$$

In the reduced open-cover accounting, the endpoint and active-interval
degeneracies make the inequality strict. Thus the seven role triangles cannot
cover $D$, whose length is $6$.

Therefore the CE1/CE2, $N_+=1$, no-Vd1/Vd2, at-least-two-T3-like branch cannot
occur, subject to the practically proven diagonal caps cited above.
