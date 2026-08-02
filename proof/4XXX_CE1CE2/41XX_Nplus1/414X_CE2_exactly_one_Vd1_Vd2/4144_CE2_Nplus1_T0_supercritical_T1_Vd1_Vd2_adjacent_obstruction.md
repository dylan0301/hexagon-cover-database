# CE2, $N_+=1$, $T_0$ Supercritical and Adjacent $T_1$ Vd1/Vd2

Status: Proven

This file proves the adjacent placement in the `414X` branch.  The former
half-edge $1/3$ envelope is replaced by the global quarter radial envelope
[`201b`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md),
and the two Vd radial substitutions are replaced by the corner margins
[`201c`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md).

## 1. Setup and residual boundary demands

Assume

$$
T_C\text{ is CE2},
\qquad
T_0\text{ is the unique supercritical V triangle},
\qquad
T_1\text{ is the unique Vd1/Vd2 V triangle},
$$

and $T_2,T_3,T_4,T_5$ are nonsupercritical Vd0 V triangles.  Use the signed center
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
k=\eta+\alpha+\delta.
$$

The two center intervals, in coordinates from $V_0$, are

$$
I_L=\left[\frac{k}{W},R+\alpha\right]
\subset e_{5,0},
$$

and

$$
I_R=\left[\frac{k}{R},W+\delta\right]
\subset e_{0,1}.
$$

The center exit on $r_2$ is

$$
\boxed{d_2^C=\delta.}
$$

Let $(a_0,b_0)$ be the boundary reaches of the supercritical V triangle.  Then

$$
\boxed{
a_0+b_0>1,
\qquad
a_0^2+a_0b_0+b_0^2\le1.
}
$$

Use the residual operator from
[`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
and put

$$
\boxed{
A=\mathcal R_{I_R}(b_0),
\qquad
H=\mathcal R_{I_L}(a_0).
}
$$

Thus $A$ is the incoming reach forced on $T_1$, while $H$ is the far-side
reach forced on $T_5$.  In a genuine reduced candidate $H>0$.  Boundary
handoffs through the four ordinary nonsupercritical V triangles give

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

Hence

$$
a_1\ge A,
\qquad
b_1\ge H.
$$

The Vd1/Vd2 half-unit cap gives

$$
\boxed{A+H<\frac12.}
$$

## 2. A quarter-margin for the center exit

The common perimeter budget
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
gives

$$
\boxed{
T:=\alpha+\delta<\frac1{24},
\qquad
T<\frac{\min\{R,W\}}6.
}
$$

We prove

$$
\boxed{\delta<\frac H4.}
$$

Since $H>0$, the residual formula has two possible positive values.

### Case 1: $H=1-(R+\alpha)=W-\alpha$

Then

$$
4\delta+\alpha
\le
4(\alpha+\delta)
<
\frac{2W}{3}
<W,
$$

so

$$
4\delta<W-\alpha=H.
$$

### Case 2: $H=1-a_0$

The other residual $A$ cannot equal $1-b_0$.  Otherwise

$$
A+H=2-a_0-b_0<\frac12
$$

would give $a_0+b_0>3/2$, whereas the endpoint-distance inequality gives

$$
a_0+b_0\le\frac2{\sqrt3}<\frac32.
$$

Also $b_0<1$, because $b_0=1$ would force $a_0=0$ in the endpoint-distance
inequality, contradicting strict supercriticality.  The signed center domain
gives

$$
W+\delta<1.
$$

Consequently the residual $A$ is positive.  The residual formula therefore
forces

$$
\boxed{
A=1-(W+\delta),
\qquad
b_0\ge\frac{k}{R}.
}
$$

Since $A+H<1/2$,

$$
W+\delta>\frac12+H.
$$

Put

$$
y=\frac{k}{R}.
$$

Because $a_0=1-H$ and $b_0\ge y$, the endpoint-distance inequality gives

$$
(1-H)^2+(1-H)y+y^2\le1.
$$

The diameter-transfer lemma `2018` gives

$$
H>\frac y2>\frac{\eta}{2R}.
$$

Therefore

$$
\delta
>
R-\frac12+\frac{\eta}{2R}
=:J(R).
$$

Using

$$
\frac{\eta}{R}=\frac{W}{1+E},
$$

we have

$$
J(R)=R-\frac12+\frac{W}{2(1+E)}.
$$

Exact differentiation gives

$$
4E(1+E)^2J'(R)
=
2E(1+E)(1+2E)-W(2R-1)>0.
$$

For $R\le1/2$ the last term is nonnegative after subtraction.  For
$R\ge1/2$,

$$
W(2R-1)\le\frac18,
$$

whereas the first term is already larger than $1/8$.  Hence $J$ is strictly
increasing.  Since

$$
E\left(\frac38\right)=\frac78,
\qquad
J\left(\frac38\right)=\frac1{24},
$$

the inequalities $\delta>J(R)$ and $\delta<1/24$ force

$$
R<\frac38.
$$

Now

$$
(2-3R)^2-E^2=(3-8R)(1-R)>0,
$$

so $E<2-3R$ and

$$
\frac{\eta}{R}
=
\frac{W}{1+E}
>
\frac13.
$$

Thus

$$
H>\frac{\eta}{2R}>\frac16.
$$

Together with $\delta<1/24$, this gives

$$
4\delta<\frac16<H.
$$

Both cases prove the quarter-margin.

## 3. Neither possible radial bridge reaches the center

The center interval on $r_2$ ends at distance $\delta$ from $O$, so its
vertex-side entry point is

$$
q_2=1-\delta.
$$

### The Vd1/Vd2 V triangle

If $T_1$ has no positive-length trace on $r_2$, there is nothing to prove.
Otherwise orient the corner normal form toward that supported arm.  The
supported-arm margin `201c`, together with $b_1\ge H$, gives

$$
u_2<1-H<1-\delta=q_2.
$$

Here $u_{1\to2}$ denotes the far endpoint of the supported $T_1$ trace on $r_2$. Thus $T_1$ cannot meet the center interval.

### The ordinary V triangle $T_2$

Coverage of $e_{1,2}$ gives

$$
a_2\ge1-b_1.
$$

Since $a_1+b_1<1/2$ and $a_1\ge A$,

$$
a_2>\frac12+A.
$$

Backward propagation gives $b_2\ge H$.  Put

$$
p=\frac12+A.
$$

The inequality $A+H<1/2$ gives

$$
0\le H\le p,
\qquad
p+H<1.
$$

Coordinatewise down-closedness of the exact admissible set and the quarter
envelope `201b` give

$$
c_2
\le
c_{\max}(p,H)
\le
1-\frac H4
<
1-\delta
=q_2.
$$

Thus $T_2$ also cannot meet the center interval.  Diameter locality and the
Vd0 hypotheses exclude any other positive interval on $r_2$, so that arm is
uncovered.

The reflected adjacent placement with $T_5$ Vd1/Vd2 is identical.  Therefore
every adjacent placement is impossible.

$$
\Box
$$
