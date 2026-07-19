# Direct Asymmetric-Witness Forcing

Status: Proven

This note defines the three asymmetric witnesses exactly and excludes them
from all six actual open vertex roles. Only the distinguished supercritical
row uses a row union; the other five exclusions use actual contained vertices
or actual handoff points.

## 1. Handoffs and local coordinates

Let $H$ be the side-$1$ regular hexagon centered at $O=0$, with cyclic
vertices $V_0,\dots,V_5$. Let $T_i$ be an open unit equilateral triangle
containing $V_i$. Choose strict handoffs

$$
X_i=V_i+x_i(V_{i+1}-V_i),
\qquad
X_i\in T_i\cap T_{i+1},
\tag{1}
$$

with

$$
x_3<x_2<x_1<x_0<x_5<x_4.
\tag{2}
$$

This is the exact-one chain derived in
[`31051_direct_radial_forcing.md`](31051_direct_radial_forcing.md). Put

$$
a=1-x_3,
\qquad
b=x_4.
\tag{3}
$$

The two row-$4$ anchors belong to $T_4$, so their mutual distance and (2)
give

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
\rho:=a^2+ab+b^2<1.
\tag{4}
$$

At $V_4$, use local coordinates

$$
P=V_4+u(V_5-V_4)+v(V_3-V_4),
\qquad
\mathsf q(u,v)=u^2+v^2-uv.
\tag{5}
$$

The first coordinate is outgoing and the second is incoming. In particular,

$$
X_4=(b,0),
\qquad
X_3=(0,a)
\tag{6}
$$

in these local coordinates.

## 2. Exact witness formulas

Put

$$
h=\frac{\sqrt3}{2},
\qquad
D=\sqrt{4\rho-3},
\tag{7}
$$

and define

$$
\alpha=\frac{h(b+2a-bD)}{2\rho},
\qquad
\beta=\frac{h(b-a+(a+b)D)}{2\rho},
\tag{8}
$$

$$
\gamma=\frac{h(-b+a+(a+b)D)}{2\rho},
\qquad
\delta=\frac{h(2b+a-aD)}{2\rho}.
\tag{9}
$$

The exact frontier lines for the row-$4$ source union
$\mathcal U_{AB}(b,a)$ are

$$
L_-(\lambda)=(b-\beta\lambda,\alpha\lambda),
\qquad
L_+(\mu)=(\delta\mu,a-\gamma\mu).
\tag{10}
$$

Their common parameter and junction are

$$
\lambda_*=\mu_*=\frac{8h\rho}{3(D+3)},
\tag{11}
$$

$$
J=
\left(
\frac{2b+a-aD}{D+3},
\frac{b+2a-bD}{D+3}
\right).
\tag{12}
$$

Define the two first-root parameters by the exact radicals

$$
\lambda_-
=
2(\alpha+b\beta)
-\frac23
\sqrt{9(\alpha+b\beta)^2-9b^2+9b-6},
\tag{13}
$$

$$
\mu_+
=
2(\delta+a\gamma)
-\frac23
\sqrt{9(\delta+a\gamma)^2-9a^2+9a-6}.
\tag{14}
$$

The fixed-line theorem
[`31052_fixed_line_circle_signs.md`](31052_fixed_line_circle_signs.md)
proves that both radicals are real and that

$$
\lambda_*<\lambda_-<h^{-1},
\qquad
\mu_*<\mu_+<h^{-1}.
\tag{15}
$$

The three local witnesses are

$$
Q_-^{\mathrm{loc}}
=
L_-(\lambda_-)
=
(b-\beta\lambda_-,\alpha\lambda_-),
\tag{16}
$$

$$
Q_0^{\mathrm{loc}}
=
J
=
\left(
\frac{2b+a-aD}{D+3},
\frac{b+2a-bD}{D+3}
\right),
\tag{17}
$$

$$
Q_+^{\mathrm{loc}}
=
L_+(\mu_+)
=
(\delta\mu_+,a-\gamma\mu_+).
\tag{18}
$$

For $\nu\in\{-,0,+\}$, convert the local point
$Q_\nu^{\mathrm{loc}}=(u_\nu,v_\nu)$ to the global point

$$
Q_\nu
=
V_4+u_\nu(V_5-V_4)+v_\nu(V_3-V_4).
\tag{19}
$$

By the exact strict-frontier theorem
[`20091_ab_union_curve_a_plus_b_gt_1.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md),
equations (15)--(18) put all three points on the non-axis frontier of
$\mathcal U_{AB}(b,a)$.

## 3. Interior membership

The coefficients in (8)--(9) are positive. The exact frontier identities are

$$
\alpha^2+\alpha\beta+\beta^2=h^2,
\qquad
\gamma^2+\gamma\delta+\delta^2=h^2.
\tag{20}
$$

Thus $\alpha<h$ and $\delta<h$. The coordinate bounds from the fixed-line
theorem give

$$
J_u<\frac12,
\qquad
J_v<\frac12.
\tag{21}
$$

Since $\lambda_->\lambda_*$ and $\mu_+>\mu_*$,

$$
(Q_-^{\mathrm{loc}})_u<J_u<\frac12,
\qquad
(Q_+^{\mathrm{loc}})_v<J_v<\frac12.
\tag{22}
$$

On the other coordinates, (15) and (20) give

$$
(Q_-^{\mathrm{loc}})_v
=
\alpha\lambda_-<\frac\alpha h<1,
\tag{23}
$$

$$
(Q_+^{\mathrm{loc}})_u
=
\delta\mu_+<\frac\delta h<1.
\tag{24}
$$

All local coordinates are positive because the three points lie on the
strict non-axis frontier. Therefore every $Q\in\{Q_-,Q_0,Q_+\}$ has

$$
0<u,v<1.
\tag{25}
$$

Every point of $\mathcal U_{AB}(b,a)$ lies in a closed unit equilateral
triangle containing $V_4$. Hence

$$
\mathsf q(u,v)\le1.
\tag{26}
$$

Since $uv>0$,

$$
(u-v)^2=\mathsf q(u,v)-uv<1.
\tag{27}
$$

In the $V_4$ coordinate chart, inequalities (25) and (27) are strict
hexagon inequalities. Consequently,

$$
Q_-,Q_0,Q_+\in\mathrm{int}(H).
\tag{28}
$$

## 4. Exclusion from the distinguished role

The closure $\overline{T_4}$ is one of the closed unit triangles represented
in $\mathcal U_{AB}(b,a)$ because it contains $V_4,X_3,X_4$. Suppose one of
the witnesses belonged to the open triangle $T_4$. Its local coordinates
are positive, so a sufficiently small plane ball about it would lie both in
$T_4$ and in the interior of the local corner cone. That ball would lie in
$\mathcal U_{AB}(b,a)$, making the witness an interior point of the union.
This contradicts its exact frontier membership. Thus

$$
Q_-,Q_0,Q_+\notin T_4.
\tag{29}
$$

## 5. Exclusion from $T_0,T_1,T_2$

In the $V_4$ chart, the three relevant vertices are

$$
V_0=(2,1),
\qquad
V_1=(2,2),
\qquad
V_2=(1,2).
\tag{30}
$$

For $P=(u,v)$,

$$
\lVert P-V_0\rVert^2-1
=
\mathsf q(u,v)+2-3u,
\tag{31}
$$

$$
\lVert P-V_2\rVert^2-1
=
\mathsf q(u,v)+2-3v.
\tag{32}
$$

Equations (21)--(22) show that (31) is positive for $Q_-,Q_0$, and that
(32) is positive for $Q_0,Q_+$.

For the remaining comparison with $V_0$, let

$$
E_+=(2-a,1-a).
$$

The definition of the first root gives

$$
\mathsf q(Q_+^{\mathrm{loc}}-E_+)=1,
\tag{33}
$$

and $V_0=E_++a(1,1)$. The coordinate-sum bound in the fixed-line theorem is

$$
(Q_+^{\mathrm{loc}})_u+(Q_+^{\mathrm{loc}})_v<3-2a.
\tag{34}
$$

Expanding (33) with the bilinear form associated with $\mathsf q$ gives

$$
\begin{aligned}
\lVert Q_+-V_0\rVert^2-1
&=a\left(3-a-(Q_+^{\mathrm{loc}})_u
-(Q_+^{\mathrm{loc}})_v\right)\\
&>a^2>0.
\end{aligned}
\tag{35}
$$

Reflection in the radial line through $V_4$ exchanges
$(u,v,a,b,Q_+,V_0)$ with $(v,u,b,a,Q_-,V_2)$. It therefore gives

$$
\lVert Q_--V_2\rVert^2-1>b^2>0.
\tag{36}
$$

Finally fix any of the three witnesses and write $u=1-\xi$, $v=1-\eta$.
Equation (25) gives $\xi,\eta>0$, and

$$
\begin{aligned}
\lVert P-V_1\rVert^2
&=\mathsf q(1+\xi,1+\eta)\\
&=1+\xi+\eta+\xi^2+\eta^2-\xi\eta>1.
\end{aligned}
\tag{37}
$$

Each $T_j$ contains $V_j$, and two points of an open unit equilateral
triangle have distance strictly below $1$. Equations (31)--(37) exclude all
three witnesses from $T_0,T_1,T_2$.

## 6. Exclusion using the actual adjacent handoffs

In the local chart,

$$
X_5
=
V_5+x_5(V_0-V_5)
=
(1+x_5,x_5).
\tag{38}
$$

By (2)--(3),

$$
1-a=x_3<x_5<b=x_4.
\tag{39}
$$

Thus $X_5=C_5(x_5)$ is one of the actual centers covered by the fixed-line
sign theorem. Its three signs give

$$
\lVert Q_+-X_5\rVert\ge1,
\qquad
\lVert Q_0-X_5\rVert>1,
\qquad
\lVert Q_--X_5\rVert>1.
\tag{40}
$$

Since $X_5\in T_5$, these inequalities exclude all three witnesses from
$T_5$.

For the other adjacent role, put $y=1-x_2$. Then

$$
X_2
=
V_2+x_2(V_3-V_2)
=
(y,1+y),
\tag{41}
$$

and (2)--(3) give

$$
1-b<y<a.
\tag{42}
$$

Thus $X_2=C_3(y)$. The reflected fixed-line signs give

$$
\lVert Q_--X_2\rVert\ge1,
\qquad
\lVert Q_0-X_2\rVert>1,
\qquad
\lVert Q_+-X_2\rVert>1.
\tag{43}
$$

Since $X_2\in T_3$, equation (43) excludes all three witnesses from $T_3$.

Combining (28)--(29), (31)--(37), and (40)--(43) proves

$$
\boxed{
Q_-,Q_0,Q_+
\in
\mathrm{int}(H)\setminus\bigcup_{i=0}^5T_i.
}
\tag{44}
$$

If an additional center role $T_C$ and the six vertex roles cover $H$, the
three interior witnesses in (44) must all belong to $T_C$. This is the
direct asymmetric-witness forcing theorem. $\square$
