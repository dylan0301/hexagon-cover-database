# Relaxed-P Two-Variable Reduction

Status: Proven

This file proves the relaxed-P reduction for the CE0, $N_+=1$, all-Vd0
six-point route.  The construction is defined in
[`31011_six_point_construction.md`](31011_six_point_construction.md).

The result proved here is local: after the unique supercritical row is rotated
to $V_4$, the relaxed points

$$
P_3^{\mathrm{rel}},\qquad P_5^{\mathrm{rel}}
$$

and the algorithm-2 diagonal points are controlled by the two variables

$$
a=a_4,\qquad b=b_4.
$$

This file does not prove the final inequality

$$
\Lambda(K_6^{\mathrm{rel}}(a,b))>1
$$

on the two-variable domain, and it does not by itself close the CE0,
$N_+=1$, all-Vd0 branch.

## Statement

Let

$$
(a_i,b_i)=(1-x_{i-1},x_i)
$$

be the boundary row data of a CE0, $N_+=1$, all-Vd0 configuration, with the
unique supercritical row equal to $V_4$.  Set

$$
a=a_4,\qquad b=b_4.
$$

Thus

$$
x_3=1-a,\qquad x_4=b.
$$

Assume first the strict branch

$$
a+b>1,\qquad \rho=a^2+ab+b^2<1.
$$

Let $P_5(t)$ be the selected point obtained from the fixed two-line boundary of
$R_4^{\mathrm{lin}}(a,b)$ and the radius-$1$ circle centered at

$$
E_5(t)=V_5+t(V_0-V_5).
$$

Then for

$$
1-a\le t_1\le t_2\le b
$$

one has

$$
P_5(t_1)\in[P_4,P_5(t_2)].
$$

The symmetric statement holds for $P_3$.  If $P_3(y)$ is selected using the
center with $V_4$-local coordinates

$$
(y,1+y),
$$

then for

$$
1-b\le y_1\le y_2\le a
$$

one has

$$
P_3(y_1)\in[P_4,P_3(y_2)].
$$

Consequently, for any original configuration with the same $(a,b)$, the
relaxed points satisfy

$$
P_5^{\mathrm{rel}}=P_5(1-a)\in[P_4,P_5^{\mathrm{act}}],
$$

and

$$
P_3^{\mathrm{rel}}=P_3(1-b)\in[P_4,P_3^{\mathrm{act}}].
$$

In particular,

$$
\mathrm{conv}\ K_6^{\mathrm{rel}}(a,b)
\subset
\mathrm{conv}\ K_6^{\mathrm{act}}
$$

for the strict branch, where $K_6^{\mathrm{act}}$ denotes the corresponding
actual six-point set with actual centers $E_2(x_2)$ and $E_5(x_5)$.

On the boundary $\rho=1$, the point $P_4$ is omitted as in
[`31011_six_point_construction.md`](31011_six_point_construction.md).  The
strict line junction degenerates to a point on the segment between the limiting
$P_3$ and $P_5$, so omitting it does not change the relevant convex hull.

## Chain inequalities

For every nonsupercritical row $i\ne4$,

$$
a_i+b_i\le1.
$$

Using

$$
a_i+b_i=(1-x_{i-1})+x_i,
$$

we get

$$
x_i\le x_{i-1}\qquad(i\ne4).
$$

Applying this to rows $5,0,1,2,3$ gives

$$
x_5\le x_4,
$$

$$
x_0\le x_5,
$$

$$
x_1\le x_0,
$$

$$
x_2\le x_1,
$$

and

$$
x_3\le x_2.
$$

Therefore

$$
x_3\le x_2\le x_1\le x_0\le x_5\le x_4.
$$

Since

$$
x_3=1-a,\qquad x_4=b,
$$

we have

$$
1-a\le x_2\le b,
$$

and

$$
1-a\le x_5\le b.
$$

For $P_3$, it is convenient to use

$$
y=1-x_2.
$$

Then

$$
1-b\le y\le a.
$$

Thus the relaxed centers $E_5(1-a)$ and $E_2(b)$ are the lower endpoints of the
actual feasible center intervals in the $P_5$ and $P_3$ parameterizations.

## Strict fixed-line coordinates

Put

$$
r=b,\qquad s=a,\qquad \rho=r^2+rs+s^2,
$$

and

$$
D=\sqrt{4\rho-3},\qquad h=\frac{\sqrt3}{2}.
$$

In the strict branch,

$$
r+s>1,\qquad \rho<1.
$$

Define

$$
\alpha=\frac{h(r+2s-rD)}{2\rho},\qquad
\beta=\frac{h(r-s+(r+s)D)}{2\rho},
$$

$$
\gamma=\frac{h(-r+s+(r+s)D)}{2\rho},\qquad
\delta=\frac{h(2r+s-sD)}{2\rho}.
$$

The two non-axis line sides of $R_4^{\mathrm{lin}}(a,b)$ are

$$
L_3(\lambda)=(r-\beta\lambda,\alpha\lambda)
$$

and

$$
L_5(\mu)=(\delta\mu,s-\gamma\mu).
$$

They meet at the common parameter

$$
\mu_* = \lambda_* = \frac{8h\rho}{3(D+3)}.
$$

The junction is

$$
J=L_3(\mu_*)=L_5(\mu_*).
$$

Equivalently,

$$
J=\left(\frac{2r+s-sD}{D+3},\frac{r+2s-rD}{D+3}\right).
$$

The right line endpoint inherited from the exact strict $AB$ curve is

$$
L_5\left(\frac1h\right).
$$

The selected $P_5(t)$ will be shown to lie strictly between $J$ and this
endpoint.

Let

$$
Q(u,v)=u^2+v^2-uv
$$

be the local metric.  For the moving $P_5$ center

$$
C_5(t)=(1+t,t),
$$

define

$$
F(P,t)=Q(P-C_5(t))-1.
$$

On the right and left line sides write

$$
F_5(\mu,t)=F(L_5(\mu),t),
$$

and

$$
F_3(\lambda,t)=F(L_3(\lambda),t).
$$

The goal is to prove that, for every

$$
1-s\le t\le r,
$$

the selected zero of $F(\cdot,t)$ lies on the right line side and its parameter
$\mu$ is increasing in $t$.

## Domain reparameterization

Set

$$
U=r+s-1,
$$

and

$$
z=s-r.
$$

Then

$$
r=\frac{1+U-z}{2},\qquad s=\frac{1+U+z}{2}.
$$

A direct calculation gives

$$
D^2=z^2+6U+3U^2.
$$

Since $\rho<1$, we have $D^2<1$.  Hence

$$
0<U<\frac16,
$$

and, with

$$
A=1-6U-3U^2,
$$

we have

$$
z^2<A.
$$

These inequalities will be used repeatedly.

## The junction is outside the moving circle

First note that

$$
J_u+J_v=\frac{(r+s)(3-D)}{3+D}=\frac{(1+U)(3-D)}{3+D}.
$$

We claim that

$$
J_u+J_v<1.
$$

This is equivalent to

$$
3U<D(2+U).
$$

Since

$$
D^2=z^2+6U+3U^2\ge3U(2+U),
$$

it is enough to show

$$
3U(2+U)^3>9U^2.
$$

Because $U>0$, this is equivalent to

$$
(2+U)^3>3U,
$$

which is immediate.  Therefore

$$
J_u+J_v<1.
$$

Now

$$
\frac{\partial}{\partial t}F(J,t)=1+2t-(J_u+J_v)>0
$$

for $t\ge0$.  Thus $F(J,t)$ is increasing in $t$.  It is enough to check the
left endpoint $t=1-s$.

After substituting $r=(1+U-z)/2$, $s=(1+U+z)/2$, and reducing with
$D^2=z^2+6U+3U^2$, one obtains

$$
(D+3)^2F(J,1-s)=3D(z^2+Uz+1-3U)+P_J,
$$

where

$$
P_J=z^4+5z^2+6Uz^2+3U^2z^2+9Uz+3U+15U^2.
$$

The factor multiplying $D$ is positive, because

$$
z^2+Uz+1-3U\ge1-3U-\frac{U^2}{4}>0.
$$

For $P_J$, the only term that may be negative is $9Uz$.  Since

$$
5z^2+9Uz+15U^2
$$

is a positive definite quadratic form, all remaining terms imply

$$
P_J>0.
$$

Thus

$$
F(J,1-s)>0.
$$

Since $F(J,t)$ is increasing,

$$
F(J,t)>0\qquad(1-s\le t\le r).
$$

So the moving circle never passes through the junction $J$.

## There is no left-line intersection

For fixed $t$, the function

$$
\lambda\mapsto F_3(\lambda,t)
$$

is a quadratic with positive leading coefficient.  At the junction,

$$
F_3(\mu_*,t)=F(J,t)>0.
$$

It is enough to prove

$$
\frac{\partial F_3}{\partial\lambda}(\mu_*,t)>0
$$

for the whole interval $1-s\le t\le r$.  This derivative is affine in $t$, so
it is enough to check $t=1-s$ and $t=r$.

After multiplying by the positive denominator, the numerator at $t=1-s$ is

$$
N_0=D(9+3z^2+6Uz-9U^2)+P_0,
$$

where

$$
P_0=18U^3+6U^2z^2+63U^2+18Uz^2+18Uz+54U+2z^4+9z^2+9.
$$

The coefficient of $D$ satisfies

$$
9+3z^2+6Uz-9U^2\ge9-6U-9U^2>0.
$$

Also

$$
P_0\ge9+54U-18U>0.
$$

Thus $N_0>0$.

At $t=r$, the corresponding numerator is

$$
N_1=D(9+3z^2+6U-3U^2)+P_1,
$$

where

$$
\begin{aligned}
P_1={}&9U^4-3U^3z+45U^3+9U^2z^2-6U^2z+72U^2\\
&-Uz^3+21Uz^2+9Uz+45U+2z^4+9z^2+9.
\end{aligned}
$$

The coefficient of $D$ is positive.  Using $|z|<1$ gives

$$
P_1\ge9+45U-9U-U-6U^2-3U^3>0.
$$

Hence $N_1>0$.  Therefore

$$
\frac{\partial F_3}{\partial\lambda}(\mu_*,t)>0
$$

for every $t\in[1-s,r]$.

Since $F_3(\lambda,t)$ is convex in $\lambda$, positive at $\lambda=\mu_*$,
and increasing there, it remains positive for all $\lambda\ge\mu_*$.  Thus the
moving $P_5$ circle has no intersection on the opposite line side.

## The right-line intersection exists before the endpoint

At the junction,

$$
F_5(\mu_*,t)=F(J,t)>0.
$$

We prove that

$$
F_5\left(\frac1h,t\right)<0
$$

for every $t\in[1-s,r]$.  For fixed $\mu=1/h$, the function of $t$ is convex,
because the coefficient of $t^2$ is $Q(1,1)=1$.  Therefore it is enough to prove
negativity at the two endpoints.

At $t=1-s$, after multiplying by the positive denominator, the numerator is

$$
A_0=P_2-4DU(1+U+z),
$$

where

$$
\begin{aligned}
P_2={}&3U^4+6U^3z+6U^3+4U^2z^2+12U^2z+12U^2\\
&+2Uz^3+6Uz^2+2Uz+6U+z^4+2z^2-3.
\end{aligned}
$$

Since

$$
1+U+z=2s>0,
$$

it is enough to show $P_2<0$.  For fixed $U$, the odd terms in $z$ are
maximized when $z=|z|$.  Put $x=|z|$.  The function

$$
P_2^+(U,x)=P_2(U,x)
$$

has

$$
\frac{\partial P_2^+}{\partial x}
=2(3U^3+4U^2x+6U^2+3Ux^2+6Ux+U+2x^3+2x)>0.
$$

Thus the maximum occurs at $x=\sqrt A$.  Substitution gives

$$
P_2^+(U,\sqrt A)=4U(U+\sqrt A-3)<0.
$$

Therefore

$$
F_5\left(\frac1h,1-s\right)<0.
$$

At $t=r$, after multiplying by the positive denominator, the numerator is

$$
A_1=P_3-8DUz,
$$

where

$$
P_3=3U^4+24U^3+10U^2z^2+54U^2+24Uz^2+24U+3z^4+6z^2-9.
$$

If $z\ge0$, then $A_1\le P_3$.  Since $P_3$ is increasing in $z^2$, its maximum
on $z^2<A$ occurs at $z^2=A$, where

$$
P_3=-8U(U+3)<0.
$$

If $z<0$, put $x=-z>0$.  Since $D<1$,

$$
A_1\le P_3+8Ux.
$$

The function $P_3(U,x^2)+8Ux$ is increasing in $x\ge0$, and its maximum occurs
at $x=\sqrt A$.  At that point,

$$
P_3(U,A)+8U\sqrt A=8U(\sqrt A-U-3)<0.
$$

Therefore $A_1<0$ for all $z$.  Hence

$$
F_5\left(\frac1h,r\right)<0.
$$

By convexity in $t$,

$$
F_5\left(\frac1h,t\right)<0\qquad(1-s\le t\le r).
$$

Thus, for every $t\in[1-s,r]$, the signs

$$
F_5(\mu_*,t)>0,\qquad F_5\left(\frac1h,t\right)<0
$$

force a zero

$$
\mu(t)\in\left(\mu_*,\frac1h\right).
$$

This zero lies on the non-axis right line side before the exact endpoint.  Thus
there is no missing-intersection case, no axis hit, and no point-on-edge
fallback in the strict branch.

## The first right root is the selected root

The restriction $F_5(\mu,t)$ is a quadratic in $\mu$ with positive leading
coefficient.  Since it is positive at $\mu_*$ and negative at $1/h$, the first
root lies in $(\mu_*,1/h)$ and the quadratic crosses from positive to negative
there.

If there is a second right-line root, it is farther from $V_4$.  Indeed, let

$$
w=(\delta,-\gamma).
$$

For two roots $\mu_1<\mu_2$ on the same line, the difference of squared
distances from $V_4$ satisfies

$$
Q(L_5(\mu_2))-Q(L_5(\mu_1))
=2(\mu_2-\mu_1)B_Q(C_5(t),w),
$$

where $B_Q$ is the symmetric bilinear form associated to $Q$.  Since

$$
B_Q((u,v),(x,y))=ux+vy-\frac12(uy+vx),
$$

we have

$$
B_Q(C_5(t),w)=\delta\left(1+\frac t2\right)+\gamma\left(\frac{1-t}{2}\right)>0.
$$

Thus the first right root is the closest right-root to $V_4$.  Since there is
no left-line root, this first right root is the selected point $P_5(t)$.

## Monotonicity of the selected right root

At a point $P=(u,v)$,

$$
F_t(P,t)=1+2t-(u+v).
$$

The selected root lies on the segment from $J$ to $L_5(1/h)$.  The coordinate
sum $u+v$ is affine on this segment.

We already proved $J_u+J_v<1$.  Since $s<1$,

$$
J_u+J_v<3-2s.
$$

Now set

$$
E=L_5\left(\frac1h\right),\qquad E_\Sigma=E_u+E_v.
$$

After substituting the $U,z$ variables, the sign of $3-2s-E_\Sigma$ is the sign
of

$$
D(6U+2z+6)+B(U,z),
$$

where

$$
\begin{aligned}
B(U,z)={}&-9U^3-9U^2z-9U^2-3Uz^2-18Uz+3U\\
&-3z^3+3z^2-3z+3.
\end{aligned}
$$

The coefficient $6U+2z+6$ is positive.  For $B$, compute

$$
B_z=-3(3z^2+2Uz+6U-2z+3U^2+1).
$$

The quadratic in parentheses has negative discriminant

$$
-32U^2-80U-8<0,
$$

so it is positive and $B_z<0$.  Hence $B$ is decreasing in $z$.  Its minimum on
$z^2<A$ occurs at $z=\sqrt A$, and

$$
B(U,\sqrt A)=6(1-3U-\sqrt A)>0,
$$

because

$$
(1-3U)^2-A=12U^2>0
$$

and $1-3U>0$.  Therefore

$$
E_\Sigma<3-2s.
$$

Since $u+v$ is affine on $[J,E]$, every selected root satisfies

$$
u+v<3-2s.
$$

For $t\ge1-s$,

$$
1+2t\ge3-2s.
$$

Thus, at the selected root,

$$
F_t>0.
$$

At the first right root,

$$
F_{5,\mu}<0,
$$

because the quadratic crosses from positive to negative there.  Differentiating

$$
F_5(\mu(t),t)=0
$$

gives

$$
F_{5,\mu}\mu'(t)+F_{5,t}=0.
$$

Therefore

$$
\mu'(t)=-\frac{F_{5,t}}{F_{5,\mu}}>0.
$$

Hence $P_5(t)=L_5(\mu(t))$ moves strictly away from $P_4=J$ as $t$ increases.
Consequently, if

$$
1-s\le t_1\le t_2\le r,
$$

then

$$
P_5(t_1)\in[P_4,P_5(t_2)].
$$

## The symmetric $P_3$ statement

The involution

$$
(u,v,r,s)\longleftrightarrow(v,u,s,r)
$$

sends the right line side to the left line side and sends the $P_5$ moving
center to the $P_3$ moving center.  Thus the previous proof gives the symmetric
statement:

if

$$
1-b\le y_1\le y_2\le a,
$$

then

$$
P_3(y_1)\in[P_4,P_3(y_2)].
$$

In particular, with $y=1-x_2$,

$$
P_3^{\mathrm{rel}}=P_3(1-b)\in[P_4,P_3(1-x_2)]=[P_4,P_3^{\mathrm{act}}].
$$

Similarly, with $t=x_5$,

$$
P_5^{\mathrm{rel}}=P_5(1-a)\in[P_4,P_5(x_5)]=[P_4,P_5^{\mathrm{act}}].
$$

This proves the strict fixed-line monotonicity certificate.

## Red-validity of the relaxed $P$ points for the moving adjacent rows

The same proof gives the adjacent-row red-validity needed by the relaxed
construction.  Fix the actual parameter $t=x_5$.  Since

$$
\mu(1-a)\le\mu(t),
$$

the relaxed point $P_5^{\mathrm{rel}}$ lies on the right line side before the
first zero for the actual circle centered at $E_5(t)$.  Hence

$$
Q(P_5^{\mathrm{rel}}-E_5(t))\ge1.
$$

Thus $P_5^{\mathrm{rel}}$ is not in the interior of any unit equilateral
triangle containing the actual boundary point $E_5(t)$.  It is also on the
boundary of the preserved row $R_4^{\mathrm{lin}}(a,b)$.  Therefore the relaxed
$P_5$ point is valid for the two rows whose constraints are involved in the
relaxation.

The same argument gives

$$
Q(P_3^{\mathrm{rel}}-E_2(x_2))\ge1,
$$

and $P_3^{\mathrm{rel}}$ lies on the boundary of $R_4^{\mathrm{lin}}(a,b)$.
Thus the relaxed $P_3$ point is valid for its adjacent moving row as well.

The remaining row exclusions are the standard all-Vd0 locality input of this
branch: the relaxed $P$ points lie on the preserved $V_4$ two-line boundary and
can interact only with the adjacent rows used above.  No additional
non-adjacent-row optimization is used in the relaxed-P reduction.

## Diagonal points and two-variable dependence

Set

$$
p=1-b,\qquad q=1-a.
$$

For rows $0,1,2$, the chain

$$
x_3\le x_2\le x_1\le x_0\le x_5\le x_4
$$

gives lower bounds by $(p,q)$.

For row $0$,

$$
a_0=1-x_5\ge1-b=p,
$$

and

$$
b_0=x_0\ge x_3=q.
$$

For row $1$,

$$
a_1=1-x_0\ge1-b=p,
$$

and

$$
b_1=x_1\ge x_3=q.
$$

For row $2$,

$$
a_2=1-x_1\ge1-b=p,
$$

and

$$
b_2=x_2\ge x_3=q.
$$

The admissible-set value $c(\alpha,\beta)$ is defined using lower-bound edge
constraints.  Therefore it is monotone nonincreasing in the pair
$(\alpha,\beta)$: if

$$
\alpha_0\le\alpha_1,\qquad \beta_0\le\beta_1,
$$

then

$$
c(\alpha_1,\beta_1)\le c(\alpha_0,\beta_0).
$$

Consequently the common value

$$
c_*=c(p,q)
$$

is at least as large as the maximum radial coordinate available to each of rows
$0,1,2$ under their actual lower-bound data.  Hence the diagonal points

$$
D_j=(1-c_*)V_j,\qquad j=0,1,2,
$$

are valid relaxed diagonal obstruction points for the actual configuration.

All relaxed points are now functions only of

$$
a=a_4,\qquad b=b_4.
$$

Indeed, $P_3^{\mathrm{rel}}$ uses the virtual center $E_2(b)$, $P_5^{\mathrm{rel}}$
uses the virtual center $E_5(1-a)$, $P_4$ uses only the strict row
$R_4(a,b)$, and the diagonal points use only

$$
(p,q)=(1-b,1-a).
$$

Thus, in the strict branch,

$$
K_6^{\mathrm{rel}}=K_6^{\mathrm{rel}}(a,b).
$$

On $\rho=1$, the selected set is

$$
K_5^{\partial,\mathrm{rel}}(a,b),
$$

which also depends only on $(a,b)$.

## Boundary $\rho=1$

When

$$
\rho=r^2+rs+s^2=1,
$$

one has $D=1$ and the strict line-line formula degenerates.  The limiting
non-axis boundary is the single segment between

$$
(0,s)
$$

and

$$
(r,0).
$$

The limiting line junction lies on this segment.  Therefore it lies in the
convex hull of the limiting $P_3$ and $P_5$ points.  Omitting $P_4$ on this
boundary does not change the convex hull and does not change the minimal
enclosing equilateral triangle side length.

This proves the relaxed-P two-variable reduction with $P_4$ omitted on
$\rho=1$.
