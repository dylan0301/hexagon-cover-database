# CE2 Exact Formulas as a Signed-Normal-Form Adapter

Status: Proven

This note records the CE2 specialization of the common signed center normal
form in
[`2109`](2109_signed_CE1_CE2_center_normal_form.md).  The former interval-pair
coupling and all six radial exits follow from one three-parameter model.

## 1. Signed variables and exact domain

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
P=E(1-E).
$$

Let $\alpha,\delta$ be the two nontrivial center slacks and put

$$
k=\eta+\alpha+\delta.
$$

Define

$$
\Delta_R=P-\alpha-W\delta,
\qquad
\Delta_L=P-R\alpha-\delta.
$$

The closed normalized exact-$M_0$ CE2 domain is

$$
\boxed{
\begin{gathered}
0<R<1,
\qquad
\alpha\ge0,
\qquad
\delta\ge0,\\
\Delta_R>0,
\qquad
\Delta_L>0.
\end{gathered}
}
$$

For the closure of an original open center role, the center slacks are strict:

$$
\boxed{\alpha>0,
\qquad
\delta>0.}
$$

The two positive center traces, both parameterized from $V_0$, are

$$
\boxed{
T_C\cap e_{5,0}=[x,u],
\qquad
x=\frac{k}{W},
\qquad
u=R+\alpha,
}
$$

and

$$
\boxed{
T_C\cap e_{0,1}=[y,v],
\qquad
y=\frac{k}{R},
\qquad
v=W+\delta.
}
$$

Here $\nu$ is the far endpoint denoted by $u$ in the legacy notation. Thus,
when using the historical symbols below, set $u=\nu$.

Their lengths are

$$
\nu-x=\frac{\Delta_L}{W}>0,
$$

and

$$
v-y=\frac{\Delta_R}{R}>0.
$$

The midpoint inequalities formerly listed separately follow from the signed
domain and the midpoint tests in
[`2100`](2100_CE1_CE2_exactly_one_midpoint_lemma.md).  In particular,

$$
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\}.
$$

Conversely, `2109` proves that every normalized exact-$M_0$ CE2 center role
yields exactly these signed inequalities.  Hence the domain is exact.

## 2. Legacy interval-pair coupling

Return to the historical endpoint names

$$
T_C\cap e_{5,0}=[x,u],
\qquad
T_C\cap e_{0,1}=[y,v],
$$

where

$$
x=\frac{k}{W},
\qquad
u=u=R+\alpha,
$$

$$
y=\frac{k}{R},
\qquad
v=W+\delta.
$$

Put

$$
S=x+y,
\qquad
D=\sqrt{x^2+xy+y^2}.
$$

Then

$$
S=\frac{k}{RW},
\qquad
D=\frac{Ek}{RW}.
$$

The classical coupling equation follows immediately:

$$
\begin{aligned}
(u+v)S-xy
&=
(1+\alpha+\delta)\frac{k}{RW}
-
\frac{k^2}{RW}\\
&=
\frac{Ek}{RW}\\
&=D.
\end{aligned}
$$

Thus

$$
\boxed{(u+v)S-xy=D,}
$$

or equivalently

$$
\boxed{u+v=\frac{D+xy}{x+y}.}
$$

The two intervals are therefore coupled automatically; the coupling is not an
additional equation beyond the signed normal form.

The old center-containment quantities also reduce to the signed slacks:

$$
vS-y=\delta S,
$$

and

$$
uS-x=\alpha S.
$$

Consequently

$$
uS\ge x,
\qquad
vS\ge y
$$

are exactly $\alpha,\delta\ge0$, with strict inequalities for closures of
original open center roles.  Likewise

$$
uS<x+\frac y2,
\qquad
vS<y+\frac x2
$$

are the exact neighboring-midpoint exclusions and follow from
$\alpha<W/2$ and $\delta<R/2$.

## 3. Half-plane model

In the affine coordinates of `2109`, the common side slacks are

$$
\begin{aligned}
F_0&=R+\alpha-a+Wb,\\
F_1&=Rb+Wa-k,\\
F_2&=W+\delta-b+Ra.
\end{aligned}
$$

This is equivalent to the legacy physical-coordinate support model in which
the side through the initial endpoints has outward normal

$$
n_2=\frac1{2D}\left(\sqrt3S,y-x\right),
$$

and the other two normals are its rotations by $\pm2\pi/3$.  The support
constants are

$$
\alpha_2=\frac{\sqrt3(S-xy)}{2D},
$$

$$
\alpha_0=\frac{\sqrt3(vS-y)}{2D},
\qquad
\alpha_1=\frac{\sqrt3(uS-x)}{2D}.
$$

Their sum is $\sqrt3/2$ precisely because the coupling identity above holds.
No separate support calculation is needed.

## 4. Radial exits and demands

The common exit theorem `2109` gives

$$
\boxed{
\begin{aligned}
d_0^C&=E-\alpha-\delta,\\
d_1^C&=\frac{\delta}{R},\\
d_2^C&=\delta,\\
d_3^C&=\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\},\\
d_4^C&=\alpha,\\
d_5^C&=\frac{\alpha}{W}.
\end{aligned}
}
$$

Substitution of the legacy endpoints gives the former formulas exactly:

$$
\boxed{
\begin{aligned}
d_0^C&=1-\frac{xy}{S},\\
d_1^C&=\frac{vS-y}{x},\\
d_2^C&=\frac{vS-y}{S},\\
d_3^C&=\min\left\{\frac{vS-y}{y},\frac{uS-x}{x}\right\},\\
d_4^C&=\frac{uS-x}{S},\\
d_5^C&=\frac{uS-x}{y}.
\end{aligned}
}
$$

The complementary vertex-role demands are

$$
\boxed{c_i=1-d_i^C.}
$$

For closures of original open center roles,

$$
d_0^C>\frac12,
\qquad
d_i^C<\frac12\quad(i\ne0),
$$

and hence

$$
c_0<\frac12,
\qquad
c_i>\frac12\quad(i\ne0).
$$

If an actual vertex role reaches distance $\widehat c_i$ from $V_i$, radial
coverage gives $\widehat c_i\ge c_i$.  Replacing the actual reach by this lower
demand is a valid relaxation by coordinatewise down-closedness.

## 5. Two-gap warning

The common formulas do not make the two-gap state into two independent
one-gap chains.  Both gaps share the same supercritical row $T_0$ and the same
center triangle.  The exact paired endpoint loss is the rank-two theorem
[`2108`](2108_CE2_two_endpoint_capped_loss.md), while the one-gap interface is
[`4105`](../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4105_CE1_CE2_one_gap_five_row_interface.md).
