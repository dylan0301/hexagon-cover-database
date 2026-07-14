# CE1/CE2 At Least Two T3-Like Diagonal Obstruction

Status: Proven

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

The full diagonal-trace caps are proved in
[`../../../2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md)
(Status: Proven).

T3-like rows are nonsupercritical by
[`../../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md`](../../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md)
(Status: Proven). Therefore, in the $N_+=1$ branch, the unique
supercritical vertex row is Vd0.

## Diagonal length accounting

Pass to the closures of the original open roles and put

$$
L_C=\mathcal H^1(T_C\cap D),
\qquad
L_i=\mathcal H^1(T_i\cap D).
$$

The original open center role contains $O$, so its closure retains
$O\in\mathrm{int}(T_C)$, as required by the center cap in `2520`.

Let $k$ be the number of T3-like rows. Since T3-like rows are
nonsupercritical and $N_+=1$, the unique supercritical row is Vd0. Therefore

$$
2\le k\le5,
$$

and the remaining $5-k$ rows are nonsupercritical Vd0. The proved strict caps
give

$$
L_C<\frac32,
$$

$$
L_i<\frac12
$$

for the unique supercritical Vd0 row and for every T3-like row, while each of
the remaining Vd0 rows contributes at most $1$. Hence

$$
\begin{aligned}
L_C+\sum_{i=0}^5L_i
&<\frac32+\frac12+\frac{k}{2}+(5-k)\\
&=7-\frac{k}{2}\\
&\le6.
\end{aligned}
$$

If the seven open roles covered $D$, passing to closures and using
subadditivity would instead give

$$
6=\mathcal H^1(D)
\le L_C+\sum_{i=0}^5L_i,
$$

a contradiction. Therefore the CE1/CE2, $N_+=1$, no-Vd1/Vd2,
at-least-two-T3-like branch cannot occur.
