# CE0 One-Supercritical T3-Like Area Certificate

Status: Proven

This note closes the CE0 branch with exactly one supercritical actual row, at
least one T3-like row, and no Vd1/Vd2 row. It uses three proved inputs:

- strict handoff selection in
  [`../../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md`](../../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md);
- local square loss in
  [`../../32XX_Nplus_ge2/3205_unconditional_local_square_loss.md`](../../32XX_Nplus_ge2/3205_unconditional_local_square_loss.md);
- direct T3-like loss in
  [`3175_direct_T3_like_area_loss.md`](3175_direct_T3_like_area_loss.md).

The failed tangent-envelope conjecture `3172` and any midpoint condition on a
T3-like row are not used.

## Theorem

Let $T_C$ be CE0. Suppose the six vertex roles are Vd0 or T3-like, at least
one is T3-like, and their actual reaches satisfy

$$
\left\lvert
\left\lbrace i:A_i+B_i>1\right\rbrace
\right\rvert=1.
$$

Then the seven triangles cannot cover $H$.

## Proof

Because $T_C$ is CE0, the six vertex roles cover $\partial H$: otherwise an
open center triangle covering a missed boundary point would contain a
positive-length edge interval. Apply `1214`. It gives cuts

$$
X_i=V_i+x_i(V_{i+1}-V_i),
\qquad
(a_i,b_i)=(1-x_{i-1},x_i),
$$

with $0<x_i<1$. Each actual vertex triangle realizes its selected pair, and
the selected rows have the same unique supercritical index as the actual
rows.

Rotate indices so that the unique supercritical row is $0$. Then

$$
x_0>x_5,
\qquad
x_0\ge x_1\ge\cdots\ge x_5.
$$

Put

$$
M=x_0,
\qquad
m=x_5.
$$

Thus $0<m<M<1$. Reflecting the hexagon replaces the cut sequence by

$$
y_i=1-x_{-i-1}
$$

and swaps the two coordinates of every row. The local loss estimates and the
Vd0/T3-like types are symmetric under this operation. Hence, after reflection
if necessary, assume

$$
m\le1-M.
\tag{1}
$$

For every $i$,

$$
x_i\ge m,
\qquad
1-x_{i-1}\ge1-M\ge m,
$$

so

$$
a_i,b_i\ge m,
\qquad
0<m\le\frac12.
\tag{2}
$$

Let $G_i$ be the normalized area of the part of the actual role $T_i$ lying
outside $H$. The square-loss theorem gives

$$
G_i\ge\min(a_i,b_i)^2
$$

for every row, and gives $G_i\ge\max(a_i,b_i)^2$ for a supercritical row.
Row $0$ has pair $(1-m,M)$; by (1),

$$
G_0\ge(1-m)^2.
\tag{3}
$$

Choose a T3-like row $q$. A T3-like row is nonsupercritical, so $q\ne0$.
By (2) and the direct T3-like theorem,

$$
G_q\ge2m-4m^2.
\tag{4}
$$

Each of the remaining four rows satisfies $G_i\ge m^2$. Combining this with
(3)--(4) gives

$$
\sum_{i=0}^5G_i
\ge
(1-m)^2+(2m-4m^2)+4m^2
=1+m^2
>1.
\tag{5}
$$

The six vertex triangles therefore contribute normalized inside area

$$
\sum_{i=0}^5(1-G_i)<5.
$$

The center triangle contributes at most one more normalized unit-triangle
area, while $H$ has normalized area $6$. Thus the seven triangles have total
inside area strictly below the area of $H$ and cannot cover it. $\square$
