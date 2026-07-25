# CE2, $N_+=1$, $T_0$ Supercritical and Non-Adjacent Vd1/Vd2

Status: Proven

This file proves the non-adjacent placements in the `414X` branch:

$$
T_C\text{ is CE2},
\qquad
T_0\text{ is the unique supercritical row},
$$

$$
T_\tau\text{ is the unique Vd1/Vd2 row},
\qquad
\tau\in\{2,3,4\}.
$$

Every other vertex row is Vd0 and nonsupercritical.

## 1. Signed CE2 data

Use the common center normal form
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md).
Put

$$
0<R<1,
\qquad
W=1-R,
$$

$$
E=\sqrt{1-RW},
\qquad
\eta=1-E,
\qquad
P=E(1-E),
$$

and let $\alpha,\delta>0$ be the two center slacks. Set

$$
T=\alpha+\delta,
\qquad
k=\eta+T.
$$

The two initial boundary endpoints are

$$
\boxed{
x=\frac{k}{W},
\qquad
y=\frac{k}{R}.
}
$$

The relevant center exits are

$$
\boxed{
d_2^C=\delta,
\qquad
d_4^C=\alpha,
}
$$

and

$$
\boxed{
d_3^C
=
\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\}.
}
$$

The CE2 total-slack lemma in
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
gives

$$
\boxed{
T<\frac12\min\{x,y\}.
}
$$

## 2. Boundary demands

Let $(a_0,b_0)$ be the boundary reaches of the supercritical row $T_0$. Then

$$
a_0+b_0>1,
$$

and

$$
\boxed{a_0^2+a_0b_0+b_0^2\le1.}
$$

Let $B$ and $U$ be the farthest extents already covered from $V_0$ on the two
CE2-active boundary edges. Equivalently, define

$$
A=1-B,
\qquad
H=1-U,
$$

where

$$
B=
\begin{cases}
b_0,&b_0<y,\\
\max\{b_0,W+\delta\},&b_0\ge y,
\end{cases}
$$

and

$$
U=
\begin{cases}
a_0,&a_0<x,\\
\max\{a_0,R+\alpha\},&a_0\ge x.
\end{cases}
$$

Boundary coverage and propagation through the ordinary nonsupercritical rows
force

$$
\boxed{a_\tau\ge A,
\qquad
b_\tau\ge H.}
$$

The Vd1/Vd2 boundary cap gives

$$
a_\tau+b_\tau<\frac12,
$$

so

$$
\boxed{A+H<\frac12.}
$$

## 3. Diameter transfer at the two active edges

Let $\beta$ be the diameter-transfer curve from
[`2018`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md):

$$
\beta(q)=\frac{-q+\sqrt{4-3q^2}}2.
$$

We prove

$$
\boxed{B\le\beta(x),
\qquad
U\le\beta(y).}
$$

It is enough to prove the first inequality; the second is its reflection.

If $B=W+\delta$, then the center triangle contains the boundary point with
parameter $x$ on $e_{5,0}$ and the boundary point with parameter $B$ on
$e_{0,1}$. Their squared distance is

$$
x^2+xB+B^2.
$$

The center triangle has diameter $1$, so this quantity is at most $1$, and
therefore $B\le\beta(x)$.

Now suppose $B=b_0$. If $a_0<x$, then $U=a_0$, and $A+H<1/2$ would imply

$$
a_0+b_0>\frac32,
$$

contrary to the endpoint-distance inequality, which gives

$$
a_0+b_0\le\frac2{\sqrt3}<\frac32.
$$

Hence $a_0\ge x$. The diameter bound gives

$$
b_0\le\beta(a_0).
$$

The function $\beta$ is strictly decreasing, since

$$
\beta'(q)
=
-\frac12-\frac{3q}{2\sqrt{4-3q^2}}<0.
$$

Thus

$$
B=b_0\le\beta(a_0)\le\beta(x).
$$

The reflected argument gives $U\le\beta(y)$.

The complementary form of the diameter-transfer lemma is

$$
1-\beta(q)>\frac q2
\qquad(q>0).
$$

Consequently

$$
A=1-B
\ge1-\beta(x)
>\frac x2,
$$

and

$$
H=1-U
\ge1-\beta(y)
>\frac y2.
$$

Together with the total-slack estimate,

$$
\boxed{T<\min\{A,H\}.}
$$

## 4. All three non-adjacent center exits are below the boundary minimum

For $r_2$ and $r_4$,

$$
d_2^C=\delta<T,
\qquad
d_4^C=\alpha<T.
$$

For $r_3$, the minimum is at most the $R,W$-weighted average:

$$
\begin{aligned}
d_3^C
&=
\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\}\\
&\le
R\frac{\alpha}{R}
+
W\frac{\delta}{W}\\
&=
\alpha+\delta\\
&=T.
\end{aligned}
$$

Hence

$$
\boxed{
d_\tau^C<\min\{A,H\},
\qquad
\tau=2,3,4.
}
$$

## 5. Radial contradiction

Orient the Vd1/Vd2 corner normal form
[`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md)
at $V_\tau$. For some $t>0$ and

$$
d=\sqrt{t^2+t+1},
$$

its own-radial reach is

$$
c_\tau
=
\frac{d-a_\tau-tb_\tau}{t+1}.
$$

Since $d<t+1$,

$$
\begin{aligned}
c_\tau
&<
1-
\frac{a_\tau+tb_\tau}{t+1}\\
&\le
1-\min\{a_\tau,b_\tau\}\\
&\le
1-\min\{A,H\}.
\end{aligned}
$$

The center-side exit gives the vertex-side entry point

$$
q_\tau=1-d_\tau^C.
$$

Since $d_\tau^C<\min\{A,H\}$,

$$
q_\tau
>
1-\min\{A,H\}
>
c_\tau.
$$

Thus the own-radial interval of $T_\tau$ does not meet the center interval on
$r_\tau$. Every other vertex role is Vd0 and has no positive-length support
on this arm. Hence $r_\tau$ is not covered, a contradiction.

All non-adjacent placements $\tau\in\{2,3,4\}$ are impossible.

$$
\Box
$$
