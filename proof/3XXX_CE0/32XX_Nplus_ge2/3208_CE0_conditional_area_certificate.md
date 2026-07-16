# CE0 Six-Row Area Certificate

Status: Proven

This note closes the CE0 branch with at least two supercritical actual rows.
It uses the strict handoff theorem
[`../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md`](../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
and the local square-loss theorem
[`3205_unconditional_local_square_loss.md`](3205_unconditional_local_square_loss.md).

## Local input

Let $f(a,b)$ be the maximal normalized inside area of a feasible vertex role
with boundary demands $(a,b)$, as defined in
[`3202_area_function_and_monotonicity.md`](3202_area_function_and_monotonicity.md),
and put $g=1-f$. The proved square-loss bounds are

$$
g(a,b)\ge\min(a,b)^2,
$$

and, when $a+b>1$,

$$
g(a,b)\ge\max(a,b)^2.
\tag{1}
$$

## Six-row lemma

Let $x_0,\dots,x_5\in(0,1)$, with cyclic indices, and set

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

Assume every pair is feasible and at least two rows are supercritical. Then

$$
\boxed{
\sum_{i=0}^5 f(a_i,b_i)<\frac{99}{20}<5.
}
\tag{2}
$$

### Proof

Write

$$
G_i=g(1-x_{i-1},x_i),
\qquad
m=\min_i x_i,
\qquad
M=\max_i x_i.
$$

Here row $i$ is supercritical exactly when $x_i>x_{i-1}$.

The reflection

$$
y_i=1-x_{-i-1}
$$

swaps the two coordinates of each row, preserves feasibility, the number of
supercritical rows, and the sum of the six $f$-values. Hence assume, after
reflection if necessary, that

$$
m\le1-M.
\tag{3}
$$

Every row coordinate is then at least $m$:

$$
x_i\ge m,
\qquad
1-x_{i-1}\ge1-M\ge m.
$$

Thus (1) gives $G_i\ge m^2$ for all $i$.

The cyclic sequence has a strict ascent out of a minimum plateau. Choose $p$
with $x_{p-1}=m<x_p$. Row $p$ is supercritical, so

$$
G_p\ge\max(1-m,x_p)^2\ge(1-m)^2.
\tag{4}
$$

Choose a second strict ascent $q\ne p$. Since

$$
(1-x_{q-1})+x_q>1,
$$

one of its two coordinates is strictly larger than $1/2$, and hence

$$
G_q>\frac14.
\tag{5}
$$

The remaining four rows contribute at least $4m^2$. Therefore

$$
\begin{aligned}
\sum_{i=0}^5G_i
&>4m^2+(1-m)^2+\frac14
\\
&=5\left(m-\frac15\right)^2+\frac{21}{20}
\ge\frac{21}{20}.
\end{aligned}
$$

Since $\sum_i f(a_i,b_i)=6-\sum_iG_i$, equation (2) follows. $\square$

## CE0 contradiction

Let $T_C$ be CE0 and suppose

$$
\left\lvert
\left\lbrace i:A_i+B_i>1\right\rbrace
\right\rvert\ge2
$$

for the actual vertex reaches. CE0 forces the six vertex roles to cover
$\partial H$; otherwise the open center role would cover a positive-length
edge interval. The at-least-two part of `1214` therefore supplies strict cuts
whose selected rows have at least two supercritical indices. Each actual
vertex triangle realizes its selected pair, so the six-row lemma bounds their
total normalized inside area by less than $99/20$.

The center triangle contributes at most one additional unit-triangle area.
Thus all seven triangles contribute less than

$$
\frac{99}{20}+1
=\frac{119}{20}
<6,
$$

whereas the normalized area of $H$ is $6$. Hence they cannot cover $H$.
