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

## 2. Residual demands at the Vd1/Vd2 V triangle

Let $(a_0,b_0)$ be the boundary reaches of the supercritical V triangle.  Then

$$
\boxed{
a_0+b_0>1,
\qquad
a_0^2+a_0b_0+b_0^2\le1.
}
$$

Let

$$
B=e_{I_R}(b_0),
\qquad
U=e_{I_L}(a_0)
$$

be the farthest already-covered extents from $V_0$ on the two active boundary
edges, in the notation of the interval calculus
[`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md).
Put

$$
\boxed{A=1-B,
\qquad
H=1-U.}
$$

Boundary propagation through the intervening nonsupercritical V triangles gives

$$
\boxed{a_\tau\ge A,
\qquad
b_\tau\ge H.}
$$

The Vd1/Vd2 half-unit cap therefore gives

$$
\boxed{A+H<\frac12.}
$$

## 3. Diameter transfer on the two active edges

Let

$$
\beta(q)=\frac{-q+\sqrt{4-3q^2}}2.
$$

We prove

$$
\boxed{B\le\beta(x),
\qquad
U\le\beta(y).}
$$

It is enough to prove the first inequality.  By the explicit interval
component formula, $B$ is either the supercritical endpoint $b_0$ or the far
center endpoint $W+\delta$.

If

$$
B=W+\delta,
$$

then the center triangle contains points with parameters $x$ and $B$ on the
two adjacent boundary edges.  Its diameter is one, so

$$
x^2+xB+B^2\le1,
$$

and hence $B\le\beta(x)$.

Now suppose $B=b_0$.  If $a_0<x$, then the component on the other edge ends at
$a_0$, so $U=a_0$.  The inequality $A+H<1/2$ would then imply

$$
a_0+b_0>\frac32,
$$

contrary to

$$
a_0+b_0\le\frac2{\sqrt3}<\frac32.
$$

Thus $a_0\ge x$.  The endpoint-distance inequality gives

$$
b_0\le\beta(a_0)\le\beta(x),
$$

because $\beta$ is decreasing.  Reflection proves $U\le\beta(y)$.

The complementary diameter-transfer inequality from `2018` is

$$
1-\beta(q)>\frac q2
\qquad(q>0).
$$

Consequently

$$
A=1-B>\frac x2>T,
\qquad
H=1-U>\frac y2>T.
$$

Therefore

$$
\boxed{T<\min\{A,H\}.}
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
d_\tau^C<\min\{A,H\},
\qquad
\tau\in\{2,3,4\}.
}
$$

The Vd corner margin
[`201c`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md),
applied to $a_\tau\ge A$ and $b_\tau\ge H$, gives

$$
\boxed{c_\tau<1-\min\{A,H\}.}
$$

The center interval on $r_\tau$ begins from the vertex side at

$$
q_\tau=1-d_\tau^C
>
1-\min\{A,H\}
>
c_\tau.
$$

Hence the own-radial trace of $T_\tau$ does not meet the center trace.
Diameter locality and the Vd0 hypotheses exclude every other positive
interval on $r_\tau$.  Thus the arm is uncovered, a contradiction.

All three nonadjacent placements are impossible.

$$
\Box
$$
