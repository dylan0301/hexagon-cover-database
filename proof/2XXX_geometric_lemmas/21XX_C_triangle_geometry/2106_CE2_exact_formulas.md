# CE2 Exact Center, Interval-Coupling, Radial-Exit, and Demand Formulas

Status: Proven

This note records the exact formulas for the normalized CE2 center triangle
with unique midpoint $M_0$. The general centroid-and-angle model and generic
edge clipping formulas are recorded in
[`2105_CE1_exact_formulas.md`](2105_CE1_exact_formulas.md).

## Interval variables and exact domain

Parameterize both adjacent edges from $V_0$:

$$
e_{5,0}(a)=V_0+a(V_5-V_0),
\qquad
e_{0,1}(b)=V_0+b(V_1-V_0).
$$

Write

$$
T_C\cap e_{5,0}=[x,u],
\qquad
T_C\cap e_{0,1}=[y,v].
$$

Set

$$
S=x+y,
\qquad
D=\sqrt{x^2+xy+y^2}.
$$

By the exact interval-pair certificate in
[`2103_CE2_M0_e50_e01_maximal_interval_pairs.md`](2103_CE2_M0_e50_e01_maximal_interval_pairs.md),
the maximal closed exact-$M_0$ CE2 domain is

$$
0<x<u<1,
\qquad
0<y<v<1,
$$

$$
(u+v)S-xy=D,
$$

$$
uS\ge x,
\qquad
vS\ge y,
$$

and

$$
uS<x+\frac y2,
\qquad
vS<y+\frac x2.
$$

For the closure of an open center role, the two center inequalities are
strict:

$$
uS>x,
\qquad
vS>y.
$$

The interval on $e_{5,0}$ in the counterclockwise parameter from $V_5$ to
$V_0$ is

$$
[1-u,1-x].
$$

The two intervals are coupled by

$$
\boxed{
u+v=\frac{D+xy}{x+y}.
}
$$

They cannot be varied independently.

## Half-plane data

In standard physical coordinates, the side through the two initial endpoints
has outward normal

$$
n_2=\frac1{2D}\left(\sqrt3S,y-x\right).
$$

Set

$$
n_0=R_{2\pi/3}n_2,
\qquad
n_1=R_{-2\pi/3}n_2.
$$

The support constants are

$$
\alpha_2=\frac{\sqrt3(S-xy)}{2D},
$$

$$
\alpha_0=\frac{\sqrt3(vS-y)}{2D},
$$

$$
\alpha_1=\frac{\sqrt3(uS-x)}{2D}.
$$

Thus

$$
T_C=
\left\{
X:n_j\mathbin{\cdot}X\le\alpha_j, j=0,1,2
\right\}.
$$

The identity

$$
\alpha_0+\alpha_1+\alpha_2=\frac{\sqrt3}{2}
$$

is equivalent to the coupling equation and proves that the side length is
one.

## Exact radial exits

The ray $r_0$ exits through side $2$, so

$$
d_0
=
\frac{\alpha_2}{n_2\mathbin{\cdot}V_0}
=
\frac{S-xy}{S}
=
1-\frac{xy}{S}.
$$

The rays $r_1,r_2$ exit through side $0$:

$$
d_1=\frac{vS-y}{x},
\qquad
d_2=\frac{vS-y}{S}.
$$

The rays $r_4,r_5$ exit through side $1$:

$$
d_4=\frac{uS-x}{S},
\qquad
d_5=\frac{uS-x}{y}.
$$

On $r_3$, sides $0$ and $1$ both give upper bounds:

$$
d_3=
\min\left\{
\frac{vS-y}{y},
\frac{uS-x}{x}
\right\}.
$$

Therefore

$$
\boxed{
\begin{aligned}
d_0&=1-\frac{xy}{S},\\
d_1&=\frac{vS-y}{x},\\
d_2&=\frac{vS-y}{S},\\
d_3&=\min\left\{
\frac{vS-y}{y},
\frac{uS-x}{x}
\right\},\\
d_4&=\frac{uS-x}{S},\\
d_5&=\frac{uS-x}{y}.
\end{aligned}
}
$$

## Complementary radial demands

Set

$$
c_i=1-d_i.
$$

Then

$$
\boxed{
\begin{aligned}
c_0&=\frac{xy}{x+y},\\
c_1&=1-\frac{vS-y}{x},\\
c_2&=1-\frac{vS-y}{S},\\
c_3&=1-\min\left\{
\frac{vS-y}{y},
\frac{uS-x}{x}
\right\},\\
c_4&=1-\frac{uS-x}{S},\\
c_5&=1-\frac{uS-x}{y}.
\end{aligned}
}
$$

The exact midpoint conditions imply

$$
d_0\ge\frac12,
\qquad
d_i<\frac12\quad(i\ne0),
$$

and hence

$$
c_0\le\frac12,
\qquad
c_i>\frac12\quad(i\ne0).
$$

As in `2105`, the inequality $\widehat c_i\ge c_i$ for an actual vertex-role
reach is a relaxation in the correct direction by convexity and
coordinatewise down-closedness.

## Two-gap propagation warning

If both CE2 intervals contain V-gaps, the correct necessary propagation does
not consist of one six-row chain across either interval. It splits into two
one-row conditions through $T_0$ and two complementary five-row conditions.
The exact inequalities and the common-$T_0$ realization condition are
recorded in the `410X` strategy note.
