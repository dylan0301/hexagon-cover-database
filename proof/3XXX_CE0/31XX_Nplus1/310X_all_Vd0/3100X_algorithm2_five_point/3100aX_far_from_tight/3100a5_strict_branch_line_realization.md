# Strict Branch Line Realization For The Two Fixed Points

Status: Proven

This file proves an exact intersection statement for the candidate strict
four-piece chain used by the algorithm-2 route.  The source chain is only a
lemma target: its identification with the actual $AB$-union frontier is not
proved.  Thus the algebraic result below is proven, while its geometric use as
a frontier-realization theorem is conditional on
[`../../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md`](../../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md).
It applies only in the strict branch

$$
a+b>1,\qquad \rho=a^2+ab+b^2<1.
$$

The limiting case $\rho=1$ is not covered here because the candidate strict
four-piece formula degenerates there.

## Statement

Let

$$
A=(a,0),\qquad B=(0,b),\qquad h=\frac{\sqrt3}{2},\qquad D=\sqrt{4\rho-3}.
$$

Assume

$$
a+b>1,\qquad \rho=a^2+ab+b^2<1.
$$

Let $\Gamma_{AB}$ be the candidate strict non-axis chain from the $AB$-union
target file, with pieces

$$
\Gamma_{AB}=\Gamma_A^{\mathrm{circ}}\cup\Gamma_A^{\mathrm{lin}}\cup\Gamma_B^{\mathrm{lin}}\cup\Gamma_B^{\mathrm{circ}}.
$$

Let

$$
C_2=(b,1+b),\qquad C_5=(1+a,a),
$$

and use the cone metric

$$
Q(u,v)=u^2+v^2-uv.
$$

Then the radius-$1$ circle centered at $C_2$ meets $\Gamma_{AB}$ exactly once, and that intersection lies on $\Gamma_A^{\mathrm{lin}}$. By symmetry, the radius-$1$ circle centered at $C_5$ meets $\Gamma_{AB}$ exactly once, and that intersection lies on $\Gamma_B^{\mathrm{lin}}$.

## Coefficients And Line Parameters

The strict curve file defines

$$
\alpha=\frac{h(a+2b-aD)}{2\rho},\qquad \beta=\frac{h(a-b+(a+b)D)}{2\rho},
$$

$$
\gamma=\frac{h(-a+b+(a+b)D)}{2\rho},\qquad \delta=\frac{h(2a+b-bD)}{2\rho},
$$

and

$$
\Omega=\alpha\delta-\gamma\beta=\frac{3(1-D)(D+3)}{16\rho}>0.
$$

Since $0<D<1$, the inequalities $\alpha>0$ and $\delta>0$ are immediate. For $\beta$ and $\gamma$, it is enough to note

$$
(a+b)^2D^2-(a-b)^2=4(a+b-1)(a+b+1)\rho>0.
$$

Thus

$$
\alpha,\beta,\gamma,\delta>0.
$$

Parametrize the two line pieces by

$$
\Gamma_A^{\mathrm{lin}}:\quad (u,v)=(a,0)+\lambda(-\beta,\alpha),
$$

and

$$
\Gamma_B^{\mathrm{lin}}:\quad (u,v)=(0,b)+\mu(\delta,-\gamma).
$$

The two line pieces meet at the common parameter

$$
\lambda_*=\mu_*=\frac{8h\rho}{3(D+3)}.
$$

Using $4\rho=D^2+3$ and $h^2=3/4$, one obtains

$$
0<\lambda_*<\frac1h.
$$

Furthermore,

$$
a-\lambda_*\beta=\lambda_*\delta,\qquad \lambda_*\alpha=b-\lambda_*\gamma.
$$

Thus the common junction is

$$
J_2=(a-\lambda_*\beta,\lambda_*\alpha)=(\lambda_*\delta,b-\lambda_*\gamma).
$$

The relevant line-segment parameter intervals are

$$
\Gamma_A^{\mathrm{lin}}:\quad \lambda_*\le\lambda\le\frac1h,
$$

and

$$
\Gamma_B^{\mathrm{lin}}:\quad \lambda_*\le\mu\le\frac1h.
$$

## Sign Function For The $C_2$ Circle

Define

$$
F(u,v)=Q((u,v)-C_2)-1.
$$

The goal is to locate the zero set of $F$ on $\Gamma_{AB}$.

Use the reparameterization

$$
x=1-b,\qquad y=a+b-1.
$$

Thus

$$
a=x+y,\qquad b=1-x,
$$

and the strict condition $\rho<1$ is

$$
g:=y^2+(1+x)y-x(1-x)<0.
$$

## Signs At The Three Junctions Adjacent To $\Gamma_A^{\mathrm{lin}}$

Let

$$
J_0=\left(0,\frac{-a+\sqrt{4-3a^2}}2\right),
$$

and

$$
J_1=\left(a-\frac{\beta}{h},\frac{\alpha}{h}\right).
$$

A direct substitution gives

$$
F(J_0)<0,\qquad F(J_1)<0,\qquad F(J_2)>0.
$$

For $J_2$, the exact expression is

$$
F(J_2)=\frac{2}{(D+3)^2}(P_2+DQ_2),
$$

where

$$
Q_2=3(2x^2+xy-2x+1)>0,
$$

and

$$
P_2=(2x-1)^2(2x^2-2x+3)+y(12x^3+x+4)+2y^2(7x^2-x+6)+6y^3(x+1)+2y^4>0.
$$

Hence $F(J_2)>0$.

For $J_1$, the exact form is

$$
F(J_1)=\frac{1}{2\rho}(P_1+DQ_1),
$$

where

$$
Q_1=y(1-2x-y).
$$

The polynomial part is

$$
P_1=6x(x-1)(x^2-x+1)+3y(2x+1)(2x^2-2x+1)+y^2(14x^2-2x+5)+2y^3(4x+1)+2y^4.
$$

One has $P_1<0$ on $g<0$. If $Q_1\le0$, then $F(J_1)<0$ follows immediately. If $Q_1>0$, the identity

$$
P_1^2-D^2Q_1^2=4\rho\left(gH+xy(x-2)(x-1)\right)
$$

with

$$
H=9x(x-1)(x^2-x+1)+2y(9x^3-9x^2+4x+1)+3y^2(5x^2-2x+1)+6xy^3+y^4
$$

gives $P_1^2>D^2Q_1^2$ in the branch. Since $P_1<0$ and $Q_1>0$, this implies $P_1+DQ_1<0$.

For $J_0$, write

$$
z=\frac{-a+\sqrt{4-3a^2}}2.
$$

Then $z^2+az+a^2=1$. Substituting $J_0=(0,z)$ and squaring the equivalent positive-sided inequality gives the factor

$$
I=g(2xy+3x+y^2+2y+3)-x(x-2)(x-1)(2y+3)<0.
$$

Hence $F(J_0)<0$.

## No Zero On $\Gamma_A^{\mathrm{circ}}$

On $\Gamma_A^{\mathrm{circ}}$, one has

$$
Q((u,v)-A)=1.
$$

Therefore $F$ restricted to the $A$-arc is the difference of two squared distances to fixed centers, hence an affine function of $(u,v)$ along the cone plane. With the arc written as the concave graph

$$
v=\frac{u-a+\sqrt{4-3(u-a)^2}}2,
$$

the coefficient of $v$ in that affine function is negative. Therefore $F$ restricted to $\Gamma_A^{\mathrm{circ}}$ is convex as a function of $u$.

Since

$$
F(J_0)<0,\qquad F(J_1)<0,
$$

there is no zero on $\Gamma_A^{\mathrm{circ}}$.

## Unique Zero On $\Gamma_A^{\mathrm{lin}}$

On $\Gamma_A^{\mathrm{lin}}$, the endpoints satisfy

$$
F(J_1)<0,\qquad F(J_2)>0.
$$

The restriction of $F$ to a line is a quadratic. A quadratic has at most two real zeros, and opposite signs at the two endpoints force an odd number of zeros in the open segment. Therefore there is exactly one zero on $\Gamma_A^{\mathrm{lin}}$.

## No Zero On $\Gamma_B^{\mathrm{lin}}$

On $\Gamma_B^{\mathrm{lin}}$, start at the common junction $J_2$. We have $F(J_2)>0$. The derivative of $F$ with respect to the parameter $\mu$ at $\mu=\lambda_*$ satisfies

$$
\frac{2\rho(D+3)}{\sqrt3}F'(\lambda_*)=P_D+DQ_D,
$$

where

$$
Q_D=3(x^2+xy-x+1)>0,
$$

and

$$
P_D=(x^2-x+1)(8x^2-8x+5)+y(14x^3+3x+8)+18y^2(x^2+1)+10y^3(x+1)+4y^4>0.
$$

Thus $F'(\lambda_*)>0$. Since the restriction of $F$ to the line has positive quadratic coefficient, its derivative is increasing. Hence $F$ is increasing on $\Gamma_B^{\mathrm{lin}}$, and $F>0$ on that segment.

## No Zero On $\Gamma_B^{\mathrm{circ}}$

On $\Gamma_B^{\mathrm{circ}}$, one has

$$
Q((u,v)-B)=1.
$$

Thus $F$ is again a difference of two squared distances to fixed centers. The $B$-arc is the convex graph

$$
v=b+\frac{u-\sqrt{4-3u^2}}2,
$$

and the coefficient of $v$ in the affine difference is negative. Hence $F$ is concave on the $B$-arc.

At the endpoint shared with $\Gamma_B^{\mathrm{lin}}$, $F>0$. At the axis endpoint

$$
J_4=\left(\frac{-b+\sqrt{4-3b^2}}2,0\right),
$$

one obtains

$$
F(J_4)>0.
$$

Indeed, if $w=(-b+\sqrt{4-3b^2})/2$, then

$$
F(J_4)=(1-2b)w+b+1.
$$

For $b\le1/2$ this is immediate. For $b>1/2$, after squaring the equivalent positive-sided inequality, the difference is

$$
4b(b-1)(4b^2-5)>0
$$

in the strict branch. Therefore $F(J_4)>0$.

Since a concave function lies above the minimum of its endpoint values, $F>0$ on $\Gamma_B^{\mathrm{circ}}$.

## Conclusion

The $C_2$ circle has no zero on $\Gamma_A^{\mathrm{circ}}$, exactly one zero on
$\Gamma_A^{\mathrm{lin}}$, and no zero on
$\Gamma_B^{\mathrm{lin}}\cup\Gamma_B^{\mathrm{circ}}$. Hence its selected
non-axis intersection with the candidate chain lies on
$\Gamma_A^{\mathrm{lin}}$.

The involution

$$
(u,v,a,b)\longleftrightarrow(v,u,b,a)
$$

sends $C_2=(b,1+b)$ to $C_5=(1+a,a)$ and sends
$\Gamma_A^{\mathrm{lin}}$ to $\Gamma_B^{\mathrm{lin}}$. Hence the $C_5$ circle
has its unique non-axis candidate-chain intersection on
$\Gamma_B^{\mathrm{lin}}$.

Thus, for the candidate chain in the strict nondegenerate branch,

$$
P_3\in\Gamma_A^{\mathrm{lin}},\qquad P_5\in\Gamma_B^{\mathrm{lin}}.
$$

## Remaining Boundary

The limiting case $\rho=1$ is not included. It should follow by a limiting degeneration argument, but that argument is not recorded here.
