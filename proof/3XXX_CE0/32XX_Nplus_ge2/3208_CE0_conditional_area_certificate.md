# Boundary-Complete Six-V-Triangle Area Certificate

Status: Proven

This note proves a center-independent boundary-complete obstruction with at
least two supercritical actual V triangles. The CE0 and zero-gap branches are
immediate corollaries. It uses the strict handoff theorem
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

## Six-V triangle lemma

Let $x_0,\dots,x_5\in(0,1)$, with cyclic indices, and set

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

Assume every pair is feasible and at least two V triangles are supercritical. Then

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

Here V triangle $i$ is supercritical exactly when $x_i>x_{i-1}$.

The reflection

$$
y_i=1-x_{-i-1}
$$

swaps the two coordinates of each V triangle, preserves feasibility, the number of
supercritical V triangles, and the sum of the six $f$-values. Hence assume, after
reflection if necessary, that

$$
m\le1-M.
\tag{3}
$$

Every V triangle coordinate is then at least $m$:

$$
x_i\ge m,
\qquad
1-x_{i-1}\ge1-M\ge m.
$$

Thus (1) gives $G_i\ge m^2$ for all $i$.

The cyclic sequence has a strict ascent out of a minimum plateau. Choose $p$
with $x_{p-1}=m<x_p$. V triangle $p$ is supercritical, so

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

The remaining four V triangles contribute at least $4m^2$. Therefore

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

## Boundary-complete contradiction

Let $U_C,U_0,\ldots,U_5$ be the original open roles, and put
$T_C=\overline{U_C}$ and $T_i=\overline{U_i}$. Suppose
$U_0,\ldots,U_5$ cover $\partial H$ and

$$
\left\lvert
\left\lbrace i:A_i+B_i>1\right\rbrace
\right\rvert\ge2
$$

for the actual V-triangle reaches. The at-least-two part of `1214` supplies
strict cuts whose selected V triangles have at least two supercritical
indices. Each actual V triangle realizes its selected pair, so the six-V
triangle lemma bounds their total normalized inside area by less than $99/20$.

The C triangle contributes at most one additional unit-triangle area.
Thus all seven triangles contribute less than

$$
\frac{99}{20}+1
=\frac{119}{20}
<6,
$$

whereas the normalized area of $H$ is $6$. Hence they cannot cover $H$.

## CE0 and zero-gap corollaries

If $T_C$ is CE0, the six V roles are boundary-complete: otherwise the open C
role covering a missed boundary point would contain a positive-length edge
interval. The boundary-complete contradiction therefore closes the original
CE0 branch.

More generally, the boundary-complete equivalence in
[`2500`](../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md#boundary-complete-zero-gap-consequences)
identifies $N_{\rm gap}=0$ with the boundary hypothesis above. Thus the same
area obstruction closes every center class with $N_{\rm gap}=0$ and
$N_+\ge2$.
