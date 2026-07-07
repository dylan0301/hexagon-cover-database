# Convex Cyclic Order From The Two Line Branches

Status: Proven

This file proves the convex-order reduction used in the algorithm-2 route, conditional on the strict line-branch realization proved in [`3100a5_strict_branch_line_realization.md`](3100a5_strict_branch_line_realization.md).

## Statement

Let

$$
P_3=(u,v)\in\Gamma_A^{\mathrm{lin}},\qquad P_5=(s,t)\in\Gamma_B^{\mathrm{lin}}
$$

in the strict $V_4$ branch coordinates. Then

$$
s\ge u,\qquad v\ge t.
$$

Consequently, for any $r\ge0$, the five points

$$
D_0=rV_0,\qquad D_1=rV_1,\qquad D_2=rV_2,\qquad P_3,\qquad P_5
$$

have cyclic convex order

$$
D_0,D_1,D_2,P_3,P_5,
$$

away from the central degeneracy where adjacent determinants can vanish.

## Line-Branch Coordinate Order

Use the notation of the strict $AB$-union curve:

$$
A=(a,0),\qquad B=(0,b).
$$

The two line segments have parameterizations

$$
\Gamma_A^{\mathrm{lin}}:\quad (u,v)=(a,0)+\lambda(-\beta,\alpha),
$$

and

$$
\Gamma_B^{\mathrm{lin}}:\quad (s,t)=(0,b)+\mu(\delta,-\gamma).
$$

The coefficients satisfy

$$
\alpha,\beta,\gamma,\delta>0.
$$

The two line segments meet at a common parameter $\lambda_*$ satisfying

$$
0<\lambda_*<\frac1h,
$$

and

$$
a-\lambda_*\beta=\lambda_*\delta,\qquad \lambda_*\alpha=b-\lambda_*\gamma.
$$

Points on the two line segments satisfy

$$
\lambda_*\le\lambda\le\frac1h,\qquad \lambda_*\le\mu\le\frac1h.
$$

Therefore, for $P_3=(u,v)\in\Gamma_A^{\mathrm{lin}}$,

$$
u=a-\lambda\beta\le a-\lambda_*\beta,
$$

and

$$
v=\lambda\alpha\ge\lambda_*\alpha.
$$

For $P_5=(s,t)\in\Gamma_B^{\mathrm{lin}}$,

$$
s=\mu\delta\ge\lambda_*\delta,
$$

and

$$
t=b-\mu\gamma\le b-\lambda_*\gamma.
$$

Using the common junction identities,

$$
a-\lambda_*\beta=\lambda_*\delta,\qquad \lambda_*\alpha=b-\lambda_*\gamma,
$$

we get

$$
u\le s,\qquad v\ge t.
$$

## Coordinate Bounds

The strict line segments lie in the unit square:

$$
0\le u,v,s,t\le1.
$$

For example, $\alpha/h\le1$ follows from a direct comparison. In the nontrivial case, after squaring, the needed inequality reduces to

$$
a^2D^2-(a+2b-2\rho)^2=4(1-b)(a+b-1)\rho\ge0.
$$

The proof for $\delta/h\le1$ is symmetric:

$$
b^2D^2-(2a+b-2\rho)^2=4(1-a)(a+b-1)\rho\ge0.
$$

The lower endpoint inequalities are analogous. For instance,

$$
a-\frac{\beta}{h}\ge0
$$

is equivalent in the nontrivial case to

$$
(2a\rho-a+b)^2-(a+b)^2D^2=4(a-1)(a+1)\rho(\rho-1)\ge0.
$$

The inequality

$$
b-\frac{\gamma}{h}\ge0
$$

is symmetric.

## Convex-Order Determinants

Write

$$
D_0=rV_0,\qquad D_1=rV_1,\qquad D_2=rV_2.
$$

Up to the positive factor $\sqrt3/2$, the oriented-area determinants for the cyclic order

$$
D_0,D_1,D_2,P_3,P_5
$$

are

$$
r^2,
$$

$$
r(r-v+1),
$$

$$
(1-v)(s-u)+(1-u)(v-t)+r(s-u),
$$

$$
(1-v)(s-u)+(1-u)(v-t)+r(v-t),
$$

and

$$
r(r-s+1).
$$

By the coordinate bounds and the inequalities $s-u\ge0$ and $v-t\ge0$, all five expressions are nonnegative. They are positive away from the central degeneracy and the degenerate case $r=0$.

Therefore the algorithm-2 five points have the cyclic convex order

$$
D_0,D_1,D_2,P_3,P_5.
$$
