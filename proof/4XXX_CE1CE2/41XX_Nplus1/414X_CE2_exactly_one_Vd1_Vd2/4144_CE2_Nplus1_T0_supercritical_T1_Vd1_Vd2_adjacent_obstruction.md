# CE2, $N_+=1$, $T_0$ Supercritical and Adjacent $T_1$ Vd1/Vd2

Status: Proven

This file proves the adjacent placement in the `414X` branch.  The former
half-edge $1/3$ envelope is replaced by the global quarter radial envelope
[`201b`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md),
and the two Vd radial substitutions are replaced by the corner margins
[`201c`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md).

## 1. Setup and residual boundary lower bounds

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

Let $(A_0,B_0)$ be the boundary reaches of the supercritical V triangle.  Then

$$
\boxed{
A_0+B_0>1,
\qquad
A_0^2+A_0B_0+B_0^2\le1.
}
$$

Use the residual operator from
[`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
and put

$$
\boxed{
\rho_R=\mathcal R_{I_R}(B_0),
\qquad
\rho_L=\mathcal R_{I_L}(A_0).
}
$$

Thus $\rho_R$ is the incoming reach forced on $T_1$, while $\rho_L$ is the far-side
reach forced on $T_5$.  In a genuine reduced candidate $\rho_L>0$.  Boundary
handoffs through the four ordinary nonsupercritical V triangles give

$$
B_5\ge \rho_L
\Longrightarrow
B_4\ge \rho_L
\Longrightarrow
B_3\ge \rho_L
\Longrightarrow
B_2\ge \rho_L
\Longrightarrow
B_1\ge \rho_L.
$$

Hence

$$
A_1\ge \rho_R,
\qquad
B_1\ge \rho_L.
$$

The Vd1/Vd2 half-unit cap gives

$$
\boxed{\rho_R+\rho_L<\frac12.}
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

Since $\rho_L>0$, the residual formula has two possible positive values.

### Case 1: $\rho_L=1-(R+\alpha)=W-\alpha$

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
4\delta<W-\alpha=\rho_L.
$$

### Case 2: $\rho_L=1-A_0$

The other residual $\rho_R$ cannot equal $1-B_0$.  Otherwise

$$
\rho_R+\rho_L=2-A_0-B_0<\frac12
$$

would give $A_0+B_0>3/2$, whereas the endpoint-distance inequality gives

$$
A_0+B_0\le\frac2{\sqrt3}<\frac32.
$$

Also $B_0<1$, because $B_0=1$ would force $A_0=0$ in the endpoint-distance
inequality, contradicting strict supercriticality.  The signed center domain
gives

$$
W+\delta<1.
$$

Consequently the residual $\rho_R$ is positive.  The residual formula therefore
forces

$$
\boxed{
\rho_R=1-(W+\delta),
\qquad
B_0\ge\frac{k}{R}.
}
$$

Since $\rho_R+\rho_L<1/2$,

$$
W+\delta>\frac12+\rho_L.
$$

Put

$$
y=\frac{k}{R}.
$$

Because $A_0=1-\rho_L$ and $B_0\ge y$, the endpoint-distance inequality gives

$$
(1-\rho_L)^2+(1-\rho_L)y+y^2\le1.
$$

The diameter-transfer lemma `2018` gives

$$
\rho_L>\frac y2>\frac{\eta}{2R}.
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
\rho_L>\frac{\eta}{2R}>\frac16.
$$

Together with $\delta<1/24$, this gives

$$
4\delta<\frac16<\rho_L.
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
supported-arm margin `201c`, together with $B_1\ge \rho_L$, gives

$$
u_{1\to2}<1-\rho_L<1-\delta=q_2.
$$

Here $u_{1\to2}$ denotes the far endpoint of the supported $T_1$ trace on $r_2$. Thus $T_1$ cannot meet the center interval.

### The ordinary V triangle $T_2$

Coverage of $e_{1,2}$ gives

$$
A_2\ge1-B_1.
$$

Since $A_1+B_1<1/2$ and $A_1\ge \rho_R$,

$$
A_2>\frac12+\rho_R.
$$

Backward propagation gives $B_2\ge \rho_L$.  Put

$$
p=\frac12+\rho_R.
$$

The inequality $\rho_R+\rho_L<1/2$ gives

$$
0\le \rho_L\le p,
\qquad
p+\rho_L<1.
$$

Coordinatewise down-closedness of the exact admissible set and the quarter
envelope `201b` give

$$
C_2
\le
c_{\max}(p,\rho_L)
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
