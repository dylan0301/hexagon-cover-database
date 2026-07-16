# Asymmetric Residual-Core Witness Construction

Status: Proven

This note defines the three asymmetric witnesses exactly and proves their
uniform membership in the asymmetric model core from
[`31030_CE0_all_Vd0_residual_core_strategy.md`](31030_CE0_all_Vd0_residual_core_strategy.md).
The proof uses the strict frontier theorem
[`20091_ab_union_curve_a_plus_b_gt_1.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md)
and the fixed-line sign certificate
[`31012_core_graph_two_variable_relaxation.md`](../3101X_six_point/31012_core_graph_two_variable_relaxation.md).

## 1. Coordinate convention and exact formulas

At $V_4$, write

$$
P=V_4+u(V_5-V_4)+v(V_3-V_4),
$$

and put

$$
\mathsf q(u,v)=u^2+v^2-uv.
$$

The first coordinate is outgoing and the second is incoming. Thus the
$V_4$-placed source union is

$$
\mathcal U_{AB}(b,a),
$$

not $\mathcal U_{AB}(a,b)$. Assume

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1,
$$

and set

$$
\rho=a^2+ab+b^2,
\qquad
D=\sqrt{4\rho-3},
\qquad
h=\frac{\sqrt3}{2}.
$$

The strict domain gives $0<D<1$. Define

$$
\alpha=\frac{h(b+2a-bD)}{2\rho},
\qquad
\beta=\frac{h(b-a+(a+b)D)}{2\rho},
$$

$$
\gamma=\frac{h(-b+a+(a+b)D)}{2\rho},
\qquad
\delta=\frac{h(2b+a-aD)}{2\rho}.
$$

The two line pieces of the exact `20091` frontier are parameterized by

$$
L_3(\lambda)=(b-\beta\lambda,\alpha\lambda),
$$

and

$$
L_5(\mu)=(\delta\mu,a-\gamma\mu).
$$

They meet at

$$
\lambda_*=\mu_*
=\frac{8h\rho}{3(D+3)},
$$

at the point

$$
J=
\left(
\frac{2b+a-aD}{D+3},
\frac{b+2a-bD}{D+3}
\right).
\tag{1}
$$

The relaxed circle centers from `31011` are

$$
C_-=(1-b,2-b),
\qquad
C_+=(2-a,1-a).
\tag{2}
$$

Expanding their circle equations on the two lines gives

$$
\mathsf q\left(L_3(\lambda)-C_-\right)-1
=
\frac34\lambda^2
-3(\alpha+b\beta)\lambda
+3b^2-3b+2,
$$

and

$$
\mathsf q\left(L_5(\mu)-C_+\right)-1
=
\frac34\mu^2
-3(\delta+a\gamma)\mu
+3a^2-3a+2.
$$

Let $\lambda_-$ and $\mu_+$ be their first roots:

$$
\lambda_-
=
2(\alpha+b\beta)
-\frac23
\sqrt{
9(\alpha+b\beta)^2-9b^2+9b-6
},
\tag{3}
$$

$$
\mu_+
=
2(\delta+a\gamma)
-\frac23
\sqrt{
9(\delta+a\gamma)^2-9a^2+9a-6
}.
\tag{4}
$$

The exact sign proof in `31012` gives

$$
\lambda_*<\lambda_-<\frac1h,
\qquad
\mu_*<\mu_+<\frac1h.
\tag{5}
$$

Consequently the selected points lie on the actual line pieces proved in
`20091`, not merely on the boundary of the two-line superset. Define their
local coordinates by

$$
Q_-^{\mathrm{loc}}=L_3(\lambda_-),
\qquad
Q_0^{\mathrm{loc}}=J,
\qquad
Q_+^{\mathrm{loc}}=L_5(\mu_+),
\tag{6}
$$

and convert a local point $(u,v)$ to the global point

$$
V_4+u(V_5-V_4)+v(V_3-V_4).
$$

These global points are the witnesses $Q_-,Q_0,Q_+$.

## 2. Coordinate bounds and interior membership

Put

$$
U=a+b-1,
\qquad
z=a-b.
$$

Then

$$
D^2=z^2+6U+3U^2,
\qquad
\lvert z\rvert<1-U.
$$

It follows that

$$
D^2-(3U-z)^2=6U(1+z-U)>0,
$$

and

$$
D^2-(3U+z)^2=6U(1-z-U)>0.
$$

Using (1), these inequalities give

$$
J_u<\frac12,
\qquad
J_v<\frac12.
\tag{7}
$$

For example, $2J_u<1$ is equivalent to

$$
3U-z<D(1+2a).
$$

Indeed,

$$
D>\lvert3U-z\rvert\ge3U-z,
\qquad
1+2a>1,
$$

this inequality follows directly. The other inequality is its reflection.

Since $\beta,\gamma>0$, equations (5)--(7) imply

$$
(Q_-^{\mathrm{loc}})_u<J_u<\frac12,
\qquad
(Q_+^{\mathrm{loc}})_v<J_v<\frac12.
\tag{8}
$$

The identities proved in `20091`,

$$
\alpha^2+\alpha\beta+\beta^2=h^2,
\qquad
\gamma^2+\gamma\delta+\delta^2=h^2,
$$

together with positivity give $\alpha,\delta<h$. Hence (5) gives

$$
(Q_-^{\mathrm{loc}})_v<1,
\qquad
(Q_+^{\mathrm{loc}})_u<1.
\tag{9}
$$

All three points have positive local coordinates because they lie on the
strict non-axis frontier. Equations (7)--(9) therefore show that every
$Q\in\{Q_-,Q_0,Q_+\}$ has

$$
0<u,v<1.
\tag{10}
$$

Every exact frontier point lies in a unit triangle containing $V_4$, so
$\mathsf q(u,v)\le1$. Since $uv>0$,

$$
(u-v)^2=\mathsf q(u,v)-uv<1.
$$

Together with (10), these are the strict local hexagon inequalities from
`1201`. Thus

$$
Q_-,Q_0,Q_+\in\mathrm{int}(H).
\tag{11}
$$

## 3. The five comparison rows

Put

$$
p=1-b,
\qquad
q=1-a.
$$

In $V_4$-coordinates, the following are mandatory points of the indicated
comparison row unions:

| Row union | Mandatory point |
|---|---:|
| $R_0(p,q)$ | $V_0=(2,1)$ |
| $R_1(p,q)$ | $V_1=(2,2)$ |
| $R_2(p,q)$ | $V_2=(1,2)$ |
| $R_3(p,q)$ | $C_-=(p,1+p)$ |
| $R_5(p,q)$ | $C_+=(1+q,q)$ |

Every row union is contained in the closed unit disk about each of its
mandatory points. Distance at least $1$ from one such point therefore proves
exclusion from the plane interior of that row union.

For a point $P=(u,v)$,

$$
\lVert P-V_0\rVert^2-1
=\mathsf q(u,v)+2-3u,
\tag{12}
$$

and

$$
\lVert P-V_2\rVert^2-1
=\mathsf q(u,v)+2-3v.
\tag{13}
$$

By (7)--(8), equations (12)--(13) exclude $Q_-$ and $Q_0$ from $R_0$,
and exclude $Q_0$ and $Q_+$ from $R_2$.

For $Q_+$, its defining circle gives

$$
\mathsf q(Q_+^{\mathrm{loc}}-C_+)=1,
\qquad
V_0=C_++a(1,1).
$$

The exact sum bound proved in `31012` is

$$
(Q_+^{\mathrm{loc}})_u+(Q_+^{\mathrm{loc}})_v<3-2a.
$$

Using the bilinear form associated with $\mathsf q$ gives

$$
\lVert Q_+-V_0\rVert^2-1
=a\left(3-a-(Q_+^{\mathrm{loc}})_u-(Q_+^{\mathrm{loc}})_v\right)
>a^2>0.
\tag{14}
$$

Reflection gives

$$
\lVert Q_--V_2\rVert^2-1
>b^2>0.
\tag{15}
$$

Thus all three points avoid the interiors of $R_0(p,q)$ and $R_2(p,q)$.

For $V_1=(2,2)$, write $u=1-\xi$ and $v=1-\eta$. Equation (10) gives
$\xi,\eta>0$, and

$$
\begin{aligned}
\lVert P-V_1\rVert^2
&=\mathsf q(1+\xi,1+\eta)\\
&=1+\xi+\eta+\xi^2+\eta^2-\xi\eta>1.
\end{aligned}
\tag{16}
$$

Hence all three points lie outside $R_1(p,q)$.

Finally, the circle sign analysis proved in `31012` gives

$$
\mathsf q(Q_-^{\mathrm{loc}}-C_-)=1,
\qquad
\mathsf q(Q_0^{\mathrm{loc}}-C_-)>1,
\qquad
\mathsf q(Q_+^{\mathrm{loc}}-C_-)>1,
\tag{17}
$$

and

$$
\mathsf q(Q_+^{\mathrm{loc}}-C_+)=1,
\qquad
\mathsf q(Q_0^{\mathrm{loc}}-C_+)>1,
\qquad
\mathsf q(Q_-^{\mathrm{loc}}-C_+)>1.
\tag{18}
$$

The strict parts of (17)--(18) are exactly the junction-outside-circle and
opposite-line-exclusion calculations in `31012`, together with their
reflection. Therefore the three points avoid the interiors of $R_3(p,q)$
and $R_5(p,q)$.

## 4. The distinguished row and conclusion

By (5)--(6), all three witnesses lie on the exact non-axis frontier of
$R_4(a,b)$ proved in `20091`. Hence none lies in
$\mathrm{int}(R_4(a,b))$. Combining this with (11)--(18) proves

$$
\boxed{
Q_-,Q_0,Q_+
\in\mathcal C_{\mathrm{asym}}(a,b).
}
$$

No ordering assumption on $a$ and $b$ was used. Reflection in the radial
line $OV_4$ acts by

$$
(a,b,u,v)\longmapsto(b,a,v,u),
$$

and exchanges

$$
R_0(p,q)\longleftrightarrow R_2(q,p),
\qquad
R_3(p,q)\longleftrightarrow R_5(q,p),
\qquad
Q_-(a,b)\longleftrightarrow Q_+(b,a),
$$

while sending $R_1(p,q)$ to $R_1(q,p)$, $R_4(a,b)$ to $R_4(b,a)$, and
$Q_0(a,b)$ to $Q_0(b,a)$. Thus these labels are fixed as parameter-dependent
families, although their individual geometric objects need not be fixed when
$a\ne b$. This also audits the formulas on both halves of the parameter
domain. $\square$
