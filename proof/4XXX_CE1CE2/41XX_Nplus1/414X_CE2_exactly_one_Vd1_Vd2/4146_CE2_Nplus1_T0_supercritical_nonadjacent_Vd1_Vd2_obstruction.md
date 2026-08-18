# CE2, $N_+=1$, $T_0$ Supercritical and Non-Adjacent Vd1/Vd2

Status: Proven

This file proves all nonadjacent placements in one argument.  The residual
boundary demands are encoded by the interval operator `2019`, and the final
radial estimate is the universal Vd corner margin `201c`.

## 1. Setup

Assume

$$
T_C\text{ is CE2},
\qquad
T_0\text{ is the unique supercritical V triangle},
$$

and

$$
T_\tau\text{ is the unique Vd1/Vd2 V triangle},
\qquad
\tau\in\{2,3,4\}.
$$

Every other vertex V triangle is Vd0 and nonsupercritical.  Use the signed center
variables from
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):

$$
0<R<1,
\qquad
W=1-R,
\qquad
E=\sqrt{1-RW},
\qquad
\eta=1-E,
$$

$$
T=\alpha+\delta,
\qquad
k=\eta+T.
$$

The center intervals are

$$
I_L=\left[x,R+\alpha\right],
\qquad
x=\frac{k}{W},
$$

and

$$
I_R=\left[y,W+\delta\right],
\qquad
y=\frac{k}{R}.
$$

The relevant center exits are

$$
\boxed{
d_2^C=\delta,
\qquad
d_4^C=\alpha,
\qquad
d_3^C=\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\}.
}
$$

The common endpoint-slack lemma in
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
gives

$$
\boxed{T<\frac12\min\{x,y\}.}
$$

## 2. Residual lower bounds at the Vd1/Vd2 V triangle

Let $(A_0,B_0)$ be the boundary reaches of the supercritical V triangle.  Then

$$
\boxed{
A_0+B_0>1,
\qquad
A_0^2+A_0B_0+B_0^2\le1.
}
$$

Let

$$
B=e_{I_R}(B_0),
\qquad
U=e_{I_L}(A_0)
$$

be the farthest already-covered extents from $V_0$ on the two active boundary
edges, in the notation of the interval calculus
[`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md).
Put

$$
\boxed{\rho_R=1-B,
\qquad
\rho_L=1-U.}
$$

Boundary propagation through the intervening nonsupercritical V triangles gives

$$
\boxed{A_\tau\ge \rho_R,
\qquad
B_\tau\ge \rho_L.}
$$

The Vd1/Vd2 half-unit cap therefore gives

$$
\boxed{\rho_R+\rho_L<\frac12.}
$$

## 3. Diameter transfer on the two active edges

Let

$$
M_0(q)=\frac{-q+\sqrt{4-3q^2}}2.
$$

We prove

$$
\boxed{B\le M_0(x),
\qquad
U\le M_0(y).}
$$

It is enough to prove the first inequality.  By the explicit interval
component formula, $B$ is either the supercritical endpoint $B_0$ or the far
center endpoint $W+\delta$.

If

$$
B=W+\delta,
$$

then the C triangle contains points with parameters $x$ and $B$ on the
two adjacent boundary edges.  Its diameter is one, so

$$
x^2+xB+B^2\le1,
$$

and hence $B\le M_0(x)$.

Now suppose $B=B_0$.  If $A_0<x$, then the component on the other edge ends at
$A_0$, so $U=A_0$.  The inequality $\rho_R+\rho_L<1/2$ would then imply

$$
A_0+B_0>\frac32,
$$

contrary to

$$
A_0+B_0\le\frac2{\sqrt3}<\frac32.
$$

Thus $A_0\ge x$.  The endpoint-distance inequality gives

$$
B_0\le M_0(A_0)\le M_0(x),
$$

because $M_0$ is decreasing.  Reflection proves $U\le M_0(y)$.

The complementary diameter-transfer inequality from `2018` is

$$
1-M_0(q)>\frac q2
\qquad(q>0).
$$

Consequently

$$
\rho_R=1-B>\frac x2>T,
\qquad
\rho_L=1-U>\frac y2>T.
$$

Therefore

$$
\boxed{T<\min\{\rho_R,\rho_L\}.}
$$

## 4. Radial separation

For $r_2$ and $r_4$,

$$
d_2^C=\delta<T,
\qquad
d_4^C=\alpha<T.
$$

For $r_3$,

$$
\begin{aligned}
d_3^C
&=
\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\}\\
&\le
R\frac{\alpha}{R}+W\frac{\delta}{W}\\
&=
T.
\end{aligned}
$$

Thus

$$
\boxed{
d_\tau^C<\min\{\rho_R,\rho_L\},
\qquad
\tau\in\{2,3,4\}.
}
$$

The Vd corner margin
[`201c`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md),
applied to $A_\tau\ge \rho_R$ and $B_\tau\ge \rho_L$, gives

$$
\boxed{C_\tau<1-\min\{\rho_R,\rho_L\}.}
$$

The center interval on $r_\tau$ begins from the vertex side at

$$
q_\tau=1-d_\tau^C
>
1-\min\{\rho_R,\rho_L\}
>
C_\tau.
$$

Hence the own-radial trace of $T_\tau$ does not meet the center trace.
Diameter locality and the Vd0 hypotheses exclude every other positive
interval on $r_\tau$.  Thus the arm is uncovered, a contradiction.

All three nonadjacent placements are impossible.

$$
\Box
$$
