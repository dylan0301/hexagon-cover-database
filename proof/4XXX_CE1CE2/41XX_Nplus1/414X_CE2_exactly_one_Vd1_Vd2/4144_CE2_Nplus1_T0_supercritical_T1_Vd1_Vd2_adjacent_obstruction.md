# CE2, $N_+=1$, $T_0$ Supercritical and Adjacent $T_1$ Vd1/Vd2

Status: Proven

This file proves the adjacent placement in the `414X` branch:

$$
T_C\text{ is CE2},
\qquad
T_0\text{ is the unique supercritical row},
\qquad
T_1\text{ is the unique Vd1/Vd2 row}.
$$

The reflected placement with $T_5$ Vd1/Vd2 follows by the explicit reflection
in the signed center normal form.

## 1. Signed center variables

Use
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
k=\eta+\alpha+\delta.
$$

The two CE2 traces are

$$
T_C\cap e_{5,0}
=
\left[\frac{k}{W},R+\alpha\right],
$$

and

$$
T_C\cap e_{0,1}
=
\left[\frac{k}{R},W+\delta\right].
$$

For later notation put

$$
x=\frac{k}{W},
\qquad
u=R+\alpha,
$$

$$
y=\frac{k}{R},
\qquad
v=W+\delta.
$$

The center exit on $r_2$ is

$$
\boxed{d_2^C=\delta.}
$$

## 2. Boundary demands at the adjacent Vd1/Vd2 row

Let $(a_0,b_0)$ be the boundary reaches of the supercritical row $T_0$. Then

$$
a_0+b_0>1,
$$

and the distance between its two boundary endpoints gives

$$
\boxed{a_0^2+a_0b_0+b_0^2\le1.}
$$

Coverage on $e_{0,1}$ forces $T_1$ to have incoming reach at least

$$
A=
\begin{cases}
1-b_0,&b_0<y,\\
\max\left\{0,1-\max\{b_0,v\}\right\},&b_0\ge y.
\end{cases}
$$

Coverage on $e_{5,0}$ forces the endpoint row $T_5$ to have reach at least

$$
H=
\begin{cases}
1-a_0,&a_0<x,\\
\max\left\{0,1-\max\{a_0,u\}\right\},&a_0\ge x.
\end{cases}
$$

In a genuine candidate $H>0$. The four ordinary rows $T_2,T_3,T_4,T_5$ are
nonsupercritical Vd0 rows. Boundary handoffs propagate the $T_5$ bound
backward:

$$
b_5\ge H
\Longrightarrow
b_4\ge H
\Longrightarrow
b_3\ge H
\Longrightarrow
b_2\ge H
\Longrightarrow
b_1\ge H.
$$

Thus

$$
\boxed{a_1\ge A,
\qquad
b_1\ge H.}
$$

The Vd1/Vd2 corner normal form
[`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md)
gives the strict boundary cap

$$
a_1+b_1<\frac12.
$$

Consequently

$$
\boxed{A+H<\frac12.}
$$

## 3. The small center-slack domain

The common boundary-budget theorem
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
applies to exactly one supercritical Vd0 row, exactly one Vd1/Vd2 row, and
four nonsupercritical Vd0 rows. It gives

$$
\boxed{
\alpha+\delta<\frac1{24},
}
$$

and the orientation-sensitive estimate

$$
\boxed{
\alpha+\delta<\frac{\min\{R,W\}}6.
}
$$

These two inequalities replace the separate outer-ratio calculations.

## 4. The center exit is below $H/3$

We prove

$$
\boxed{d_2^C=\delta<\frac H3.}
$$

There are two possible positive sources of the boundary tail $H$.

### Case 1: $H=1-u=W-\alpha$

The orientation-sensitive bound gives

$$
3\delta+\alpha
\le
3(\alpha+\delta)
<
\frac W2
<
W.
$$

Therefore

$$
3\delta<W-\alpha=H,
$$

as required.

### Case 2: $H=1-a_0$

First, the demand $A$ cannot equal $1-b_0$. Otherwise

$$
A+H=2-a_0-b_0<\frac12
$$

would imply

$$
a_0+b_0>\frac32.
$$

But the endpoint-distance inequality gives

$$
a_0+b_0\le\frac2{\sqrt3}<\frac32,
$$

which is impossible. Hence

$$
A=1-v,
$$

and therefore

$$
v>\frac12+H.
$$

For the demand to be determined by $v$, row $T_0$ reaches the initial center
endpoint $y$, so $b_0\ge y$. Since $a_0=1-H$, the endpoint-distance
inequality gives

$$
(1-H)^2+(1-H)y+y^2\le1.
$$

Since $A+H<1/2$, one has $H<1/2$. The diameter-transfer lemma
[`2018`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md)
therefore gives

$$
H\ge\lambda_\circ(y)>\frac y2.
$$

Also

$$
y=\frac{\eta+\alpha+\delta}{R}>\frac\eta R.
$$

Suppose first that $R\ge3/8$. Since $v=W+\delta>1/2+H$,

$$
\delta
>
R-\frac12+\frac{\eta}{2R}
=:J(R).
$$

We claim

$$
J(R)\ge\frac1{24}
\qquad(R\ge3/8).
$$

For $3/8\le R\le13/24$, one has

$$
RW\ge\frac{15}{64},
\qquad
E\le\frac78.
$$

Using

$$
\frac\eta R=\frac{W}{1+E},
$$

we obtain

$$
J(R)
\ge
R-\frac12+\frac{4W}{15}
=
\frac{11R}{15}-\frac7{30}
\ge
\frac1{24}.
$$

For $R\ge13/24$, the simpler estimate

$$
J(R)>R-\frac12\ge\frac1{24}
$$

applies. Thus $R\ge3/8$ would give $\delta>1/24$, contrary to Section 3.
Hence

$$
R<\frac38.
$$

Now

$$
(2-3R)^2-E^2
=(3-8R)(1-R)>0,
$$

so

$$
E<2-3R.
$$

Therefore

$$
\frac\eta R
=
\frac{W}{1+E}
>
\frac{W}{3W}
=
\frac13.
$$

It follows that

$$
y>\frac13,
\qquad
H>\frac y2>\frac16.
$$

Combining this with $\delta<1/24$ gives

$$
\delta
<
\frac1{24}
<
\frac1{18}
<
\frac H3.
$$

This proves the outer-ratio target in both cases.

## 5. Excluding coverage of $r_2$

The center covers $r_2$ from $O$ to distance $\delta$. Thus the vertex-side
entry point is

$$
q_2=1-\delta.
$$

There are only two possible ways to connect the vertex-side cover to this
center interval.

### The Vd1/Vd2 row cannot bridge

Orient the normal form `2014` so that $r_2$ is the supported adjacent arm.
For some $t>0$ and

$$
d=\sqrt{t^2+t+1},
$$

its upper endpoint on $r_2$ is

$$
u_2=\frac{d-a_1-tb_1-1}{t}.
$$

If $T_1$ bridged to the center interval, then $u_2\ge q_2$, so

$$
a_1+tb_1
\le
d-1-t+t\delta.
$$

Since $d<t+1$,

$$
a_1+tb_1<t\delta.
$$

But $a_1\ge0$ and $b_1\ge H$, so $tH<t\delta$, contradicting
$\delta<H/3$.

### The ordinary row $T_2$ cannot reach the center interval

If $T_2$ reached the center interval, its own-radial reach $c_2$ would satisfy

$$
c_2\ge q_2.
$$

On $e_{1,2}$,

$$
a_2\ge1-b_1.
$$

Since $a_1+b_1<1/2$ and $a_1\ge A$,

$$
a_2>\frac12+A.
$$

Backward boundary propagation gives

$$
b_2\ge H.
$$

Put

$$
p=\frac12+A.
$$

Then $p\ge1/2$, $H\le p$, and $p+H<1$. Coordinatewise down-closedness of the
exact admissible set therefore gives

$$
c_2
\le
c_{\max}(p,H).
$$

The half-edge radial envelope in
[`2012`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md)
gives

$$
c_2
\le
1-\frac H3.
$$

But $\delta<H/3$, so

$$
1-\frac H3
<
1-\delta
=q_2.
$$

Thus $c_2<q_2$, a contradiction.

Neither possible bridge covers $r_2$. Hence the adjacent
$T_0$-supercritical, $T_1$-Vd1/Vd2 placement is impossible.

$$
\Box
$$
