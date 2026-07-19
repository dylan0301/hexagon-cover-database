# Fixed-Line Circle Signs

Status: Proven

This note gives the complete fixed-line calculation used for the two moving
adjacent vertex roles. All formulas and sign reductions needed later are
recorded here.

## 1. Strict domain and exact frontier lines

Assume

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
\rho=a^2+ab+b^2<1.
\tag{1}
$$

Put

$$
h=\frac{\sqrt3}{2},
\qquad
D=\sqrt{4\rho-3}.
\tag{2}
$$

The identity

$$
4\rho-3(a+b)^2=(a-b)^2
$$

shows that $3/4<\rho<1$, so $0<D<1$. Define

$$
\alpha=\frac{h(b+2a-bD)}{2\rho},
\qquad
\beta=\frac{h(b-a+(a+b)D)}{2\rho},
\tag{3}
$$

$$
\gamma=\frac{h(-b+a+(a+b)D)}{2\rho},
\qquad
\delta=\frac{h(2b+a-aD)}{2\rho}.
\tag{4}
$$

All four coefficients are positive. In the local metric

$$
\mathsf q(u,v)=u^2+v^2-uv,
\tag{5}
$$

the two line pieces of the strict supercritical frontier from
[`20091_ab_union_curve_a_plus_b_gt_1.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md)
are

$$
L_-(\lambda)=(b-\beta\lambda,\alpha\lambda),
\qquad
L_+(\mu)=(\delta\mu,a-\gamma\mu).
\tag{6}
$$

They meet at

$$
\lambda_*=\mu_*=\frac{8h\rho}{3(D+3)}
\tag{7}
$$

in the junction

$$
J=
\left(
\frac{2b+a-aD}{D+3},
\frac{b+2a-bD}{D+3}
\right).
\tag{8}
$$

Each line piece runs from this junction to its outer parameter $h^{-1}$.
The frontier identities

$$
\alpha^2+\alpha\beta+\beta^2=h^2,
\qquad
\gamma^2+\gamma\delta+\delta^2=h^2
\tag{9}
$$

will be used below.

The moving adjacent handoff centers are

$$
C_5(t)=(1+t,t),
\qquad
1-a\le t\le b,
\tag{10}
$$

and, after reflection,

$$
C_3(y)=(y,1+y),
\qquad
1-b\le y\le a.
\tag{11}
$$

For the first family define

$$
F(P,t)=\mathsf q(P-C_5(t))-1.
\tag{12}
$$

At $t_0=1-a$, the center is $E_+=(2-a,1-a)$. At the reflected endpoint
$y_0=1-b$, the center is $E_-=(1-b,2-b)$. Restriction of the two endpoint
circle equations to their corresponding lines gives

$$
g_-(\lambda)
=
\frac34\lambda^2
-3(\alpha+b\beta)\lambda
+3b^2-3b+2,
\tag{13}
$$

$$
g_+(\mu)
=
\frac34\mu^2
-3(\delta+a\gamma)\mu
+3a^2-3a+2.
\tag{14}
$$

Let $\lambda_-$ and $\mu_+$ denote their smaller roots. Explicitly,

$$
\lambda_-
=
2(\alpha+b\beta)
-\frac23
\sqrt{9(\alpha+b\beta)^2-9b^2+9b-6},
\tag{15}
$$

$$
\mu_+
=
2(\delta+a\gamma)
-\frac23
\sqrt{9(\delta+a\gamma)^2-9a^2+9a-6}.
\tag{16}
$$

The proof below also proves that these roots are real and lie on the stated
frontier line pieces.

## 2. Fixed-line sign theorem

Throughout the domain (1),

$$
\lambda_*<\lambda_-<h^{-1},
\qquad
\mu_*<\mu_+<h^{-1}.
\tag{17}
$$

At the junction, the endpoint-circle quadratics also satisfy

$$
g_-'(\lambda_*)<0,
\qquad
g_+'(\mu_*)<0.
\tag{17a}
$$

Moreover,

$$
J_u<\frac12,
\qquad
J_v<\frac12,
\tag{18}
$$

and

$$
\left(L_+(\mu_+)\right)_u
+\left(L_+(\mu_+)\right)_v
<3-2a,
\tag{19}
$$

with the reflected bound

$$
\left(L_-(\lambda_-)\right)_u
+\left(L_-(\lambda_-)\right)_v
<3-2b.
\tag{20}
$$

For every $t\in[1-a,b]$,

$$
F(L_+(\mu_+),t)\ge0,
\qquad
F(J,t)>0,
\qquad
F(L_-(\lambda_-),t)>0.
\tag{21}
$$

If

$$
G(P,y)=\mathsf q(P-C_3(y))-1,
$$

then, for every $y\in[1-b,a]$,

$$
G(L_-(\lambda_-),y)\ge0,
\qquad
G(J,y)>0,
\qquad
G(L_+(\mu_+),y)>0.
\tag{22}
$$

## 3. Domain reparameterization

Put

$$
U=a+b-1,
\qquad
z=a-b.
\tag{23}
$$

Then

$$
a=\frac{1+U+z}{2},
\qquad
b=\frac{1+U-z}{2},
\tag{24}
$$

and direct calculation gives

$$
D^2=z^2+6U+3U^2.
\tag{25}
$$

Since $D^2<1$, one has

$$
0<U<\frac16,
\qquad
z^2<\Omega:=1-6U-3U^2.
\tag{26}
$$

The inequalities $a,b<1$ also give

$$
\lvert z\rvert<1-U.
\tag{27}
$$

## 4. The junction is outside every moving circle

From (8),

$$
J_u+J_v
=
\frac{(1+U)(3-D)}{3+D}.
\tag{28}
$$

We claim that this sum is less than $1$. This is equivalent to

$$
3U<D(2+U).
$$

Equation (25) gives $D^2\ge3U(2+U)$, while

$$
(2+U)^3>3U.
$$

Multiplying these inequalities shows
$D^2(2+U)^2>9U^2$, proving the claim. Thus

$$
J_u+J_v<1.
\tag{29}
$$

At the left endpoint $t_0=1-a$, exact substitution in (12), followed by
reduction with (25), gives

$$
(D+3)^2F(J,t_0)
=
3D(z^2+Uz+1-3U)+P_J,
\tag{30}
$$

where

$$
P_J
=
z^4+5z^2+6Uz^2+3U^2z^2+9Uz+3U+15U^2.
\tag{31}
$$

The coefficient of $D$ is positive because

$$
z^2+Uz+1-3U
\ge
1-3U-\frac{U^2}{4}>0.
\tag{32}
$$

Also $P_J>0$: the only potentially negative term is absorbed into the
positive-definite quadratic

$$
5z^2+9Uz+15U^2,
$$

and every remaining term in (31) is positive. Hence $F(J,t_0)>0$.

For any fixed $P=(u,v)$,

$$
\frac{\partial F}{\partial t}(P,t)=1+2t-u-v.
\tag{33}
$$

Equations (29) and (33) show that $F(J,t)$ is strictly increasing for
$t\ge0$. Therefore

$$
F(J,t)>0
\qquad
(1-a\le t\le b).
\tag{34}
$$

## 5. No intersection on the opposite line

For fixed $t$, the function

$$
\lambda\longmapsto F(L_-(\lambda),t)
$$

is a convex quadratic. At the junction its value is positive by (34). Its
derivative at $\lambda=\lambda_*$ is affine in $t$, so it is enough to check
the endpoints $t=1-a$ and $t=b$.

After multiplication by a positive factor, the numerator of the junction
derivative at $t=1-a$ is

$$
N_0
=
D(9+3z^2+6Uz-9U^2)+P_0,
\tag{35}
$$

where

$$
\begin{aligned}
P_0={}&18U^3+6U^2z^2+63U^2+18Uz^2+18Uz+54U\\
&+2z^4+9z^2+9.
\end{aligned}
\tag{36}
$$

The coefficient of $D$ is at least

$$
9-6U-9U^2>0,
$$

and, using $\lvert z\rvert<1$,

$$
P_0\ge9+54U-18U>0.
$$

Thus $N_0>0$.

At $t=b$, the corresponding numerator is

$$
N_1
=
D(9+3z^2+6U-3U^2)+P_1,
\tag{37}
$$

where

$$
\begin{aligned}
P_1={}&9U^4-3U^3z+45U^3+9U^2z^2-6U^2z+72U^2\\
&-Uz^3+21Uz^2+9Uz+45U+2z^4+9z^2+9.
\end{aligned}
\tag{38}
$$

The coefficient of $D$ is positive. Again using $\lvert z\rvert<1$,

$$
P_1
\ge
9+45U-9U-U-6U^2-3U^3>0.
\tag{39}
$$

Hence $N_1>0$. The junction derivative is therefore positive throughout
$[1-a,b]$. Convexity now implies

$$
F(L_-(\lambda),t)>0
\qquad
(\lambda\ge\lambda_*,\ 1-a\le t\le b).
\tag{40}
$$

This proves the strict opposite-line sign needed in (21).

## 6. The first root lies on the correct line piece

At $t=t_0$, equation (34) gives

$$
F(L_+(\mu_*),t_0)>0.
\tag{41}
$$

At the outer endpoint $\mu=h^{-1}$, clearing a positive denominator gives
the numerator

$$
A_0=P_2-4DU(1+U+z),
\tag{42}
$$

where

$$
\begin{aligned}
P_2={}&3U^4+6U^3z+6U^3+4U^2z^2+12U^2z+12U^2\\
&+2Uz^3+6Uz^2+2Uz+6U+z^4+2z^2-3.
\end{aligned}
\tag{43}
$$

Since $1+U+z=2a>0$, it is enough to prove $P_2<0$. For fixed $U$, replace
every odd power of $z$ by the corresponding power of $x=\lvert z\rvert$;
this can only increase $P_2$. Call the resulting polynomial
$P_2^+(U,x)$. Its derivative is

$$
\frac{\partial P_2^+}{\partial x}
=
2(3U^3+4U^2x+6U^2+3Ux^2+6Ux+U+2x^3+2x)>0.
\tag{44}
$$

Thus its supremum under $z^2<\Omega$ occurs at $x=\sqrt\Omega$. Direct
substitution gives

$$
P_2^+(U,\sqrt\Omega)
=
4U(U+\sqrt\Omega-3)<0.
\tag{45}
$$

Therefore $A_0<0$, and

$$
F(L_+(h^{-1}),t_0)<0.
\tag{46}
$$

The restriction to $L_+$ is a quadratic with positive leading coefficient
$h^2=3/4$. Its positive value at $\mu_*$ and negative value at $h^{-1}$
show that its smaller root lies strictly between these parameters. The
quadratic formula identifies that root with (16), so

$$
\mu_*<\mu_+<h^{-1}.
\tag{47}
$$

The same two endpoint values show that $g_+'(\mu_*)<0$. Indeed, if this
derivative were nonnegative, strict convexity would make $g_+$ increasing
to the right of $\mu_*$, contradicting its negative value at $h^{-1}$.

The involution

$$
(u,v,a,b)\longleftrightarrow(v,u,b,a)
\tag{48}
$$

preserves $\mathsf q$, exchanges $L_+$ with $L_-$, and exchanges $E_+$
with $E_-$. Applying (47) after this reflection gives

$$
\lambda_*<\lambda_-<h^{-1}.
\tag{49}
$$

The same reflection gives $g_-'(\lambda_*)<0$. This proves (17a).

This proves the root order (17), including the reality of both radicals in
(15)--(16).

## 7. Coordinate bounds

Equation (25) gives

$$
D^2-(3U-z)^2=6U(1+z-U)>0,
\tag{50}
$$

$$
D^2-(3U+z)^2=6U(1-z-U)>0.
\tag{51}
$$

The right sides are positive by $a,b<1$. From (8), the inequality
$J_u<1/2$ is equivalent to

$$
3U-z<D(1+2a),
$$

which follows from $D>\lvert3U-z\rvert$ and $1+2a>1$. Reflection gives
$J_v<1/2$. This proves (18).

It remains to control the coordinate sum on $L_+$. Put

$$
E=L_+(h^{-1}),
\qquad
E_\Sigma=E_u+E_v.
$$

After substitution of (24), the sign of $3-2a-E_\Sigma$ is the sign of

$$
D(6U+2z+6)+B(U,z),
\tag{52}
$$

where

$$
\begin{aligned}
B(U,z)={}&-9U^3-9U^2z-9U^2-3Uz^2-18Uz+3U\\
&-3z^3+3z^2-3z+3.
\end{aligned}
\tag{53}
$$

The coefficient of $D$ in (52) is positive. Moreover,

$$
B_z
=
-3(3z^2+2Uz+6U-2z+3U^2+1).
\tag{54}
$$

The quadratic in parentheses has discriminant

$$
-32U^2-80U-8<0,
$$

and positive leading coefficient. Thus $B_z<0$. Since
$z^2<\Omega$, one has

$$
B(U,z)>B(U,\sqrt\Omega)
=
6(1-3U-\sqrt\Omega)>0.
\tag{55}
$$

The final inequality follows from

$$
(1-3U)^2-\Omega=12U^2>0
$$

and $1-3U>0$. Equations (52)--(55) prove

$$
E_u+E_v<3-2a.
\tag{56}
$$

By (29), $J_u+J_v<1<3-2a$. The coordinate sum is affine on the segment
from $J$ to $E$, and (47) places $L_+(\mu_+)$ strictly on that segment.
This proves (19). Reflection proves (20).

## 8. Moving signs and reflection

By definition of $\mu_+$,

$$
F(L_+(\mu_+),1-a)=0.
$$

At this point, (19) and (33) give

$$
\frac{\partial F}{\partial t}(L_+(\mu_+),t)>0
\qquad(t\ge1-a).
$$

Therefore

$$
F(L_+(\mu_+),t)\ge0
\qquad(1-a\le t\le b).
\tag{57}
$$

Equation (34) supplies the strict junction sign, and (40), together with
$\lambda_->\lambda_*$, supplies the strict sign at $L_-(\lambda_-)$. This
proves all of (21).

Under the involution (48), the family $C_5(t)$ on $[1-a,b]$ becomes the
family $C_3(y)$ on $[1-b,a]$. It also exchanges the two first-root points
while fixing the junction as the parameter-dependent line intersection.
Reflecting (21) therefore gives every sign in (22). This completes the
fixed-line circle proof. $\square$
