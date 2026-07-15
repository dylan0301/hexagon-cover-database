# Low and $T_-$ Branch Obligations in $407X$

Status: Proven

This file proves the hard-region obligations involving $L$ and $T_-$, and
the full left-$T_-$ family, in the $407X$ boundary-loss framework of
[`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md).

Throughout, let

$$
B_5:=B(A_5,C_5),\qquad B_1:=B(A_1,C_1),
$$

and assume the hard region

$$
A_1+A_5\le1.
$$

## 1. Basic branch bounds

### Lemma 1.1: Low outputs are small

If a realized branch is $L$, then

$$
B_L< \frac{1}{2}.
$$

### Proof

The Low branch output is

$$
B_L=e(\eta)=\frac{(1-\eta)(1-\sqrt{4(1-\eta)^2-3})}{2}.
$$

Its maximum on the Low range occurs at $1-\eta=\sqrt3/2$ and is

$$
\frac{\sqrt3}{4}< \frac{1}{2}.
$$

### Lemma 1.2: $T_-$ outputs are input-bounded

If a realized branch is $T_-$, then

$$
B_{T_-}(a,c)\le \min(a,1-a).
$$

### Proof

The $T_-$ branch domain includes

$$
0\le b\le a,\qquad a+b\le1.
$$

Hence

$$
b\le a,\qquad b\le1-a.
$$

## 2. The family $\{L,T_-\}^2$

### Theorem 2.1

If

$$
(B_5,B_1)\in\{L,T_-\}^2,
$$

then

$$
B_5+B_1<1.
$$

### Proof

If at least one branch is $L$, then one output is strictly less than $1/2$
by Lemma 1.1 and the other is at most $1/2$ by Lemmas 1.1 and 1.2.  Hence
the sum is strictly less than $1$.

It remains to treat

$$
(B_5,B_1)=(T_-,T_-).
$$

By Lemma 1.2,

$$
B_5\le \min(A_5,1-A_5),\qquad B_1\le \min(A_1,1-A_1).
$$

Under $A_1+A_5\le1$,

$$
\min(A_5,1-A_5)+\min(A_1,1-A_1)\le1,
$$

with equality only if

$$
A_1=A_5=\frac{1}{2}.
$$

Therefore equality $B_5+B_1=1$ would force

$$
A_1=A_5=B_1=B_5=\frac{1}{2}.
$$

For the $T_-$ equation

$$
((a+b)^2-1)c^2+ac-a^2=0,
$$

substituting $a=b=1/2$ gives

$$
\frac{1}{2}c-\frac{1}{4}=0,
$$

so $c=1/2$.  Applying this to the $T_5$ side gives

$$
C_5=\frac{1}{2}.
$$

But $C_5=1-\gamma_5$, and $T_C$ covers exactly $M_0$ among the radial midpoints.  Since $M_5$ lies at coordinate $1/2$ on $r_5$ and $T_C\cap r_5=[0,\gamma_5]$ is closed, $M_5\notin T_C$ implies

$$
\gamma_5<\frac{1}{2},\qquad C_5>\frac{1}{2},
$$

contradiction.  Therefore equality is impossible, and the sum is strictly less than $1$.

## 3. Left-$T_-$: non-overlap branch

Assume

$$
B_5=T_-,\qquad A_5=1-\alpha.
$$

The hard region gives $A_1\le\alpha$.  Since the two outer cases for $A_1$
have $A_1=q>\alpha$, necessarily

$$
A_1=A_C=1-t,
\qquad
A_C\le\alpha,
$$

and $s\le p_1<t$.  We split the proof according to whether the formal far
endpoint $T=X+\lambda$ lies beyond or before the $T_0$ reach $\alpha$.

### 3.1. The separated case $\alpha<T$

In this case $\alpha<S$.  For CE2 this follows directly from the three-case
formula for $A_5$ in `4073`: the middle case $S\le\alpha<T$ would give
$A_5=1-T$.  For CE1, the same side model has formal trace
$[S,T]\cap[0,1]$ and no positive $e_{5,0}$ interval.  Since
$T>\alpha>0$, this forces $S\ge\min(T,1)>\alpha$.  Here and below

$$
S=\frac{\lambda s}{1-\lambda}.
$$

### Lemma 3.1

In this branch,

$$
B_5<A_1.
$$

### Proof

Let

$$
\delta=\alpha-A_C\ge0.
$$

The exact $T_-$ root-order test and its monotonicity are proved in
[`2011`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md).
Since $A_5=1-\alpha$, $A_1=A_C$, and $C_5=1-\gamma_5$, its expression here is

$$
\Psi^-_{1-\alpha,1-\gamma_5}(A_C)
=(1-\alpha)(\alpha-\gamma_5)-\delta(2-\delta)(1-\gamma_5)^2.
$$

By the $T_-$ root-order test, it is enough to prove this is positive.

The T3-like geometry gives $s\le p_1<t$, hence

$$
s<1-\alpha.
$$

Using

$$
X=\lambda s+A_C+\rho-1-\lambda
$$

and

$$
\gamma_5\le \frac{X}{1-\lambda},
$$

we obtain

$$
\gamma_5<\alpha-\kappa-\frac{\delta}{1-\lambda},\qquad \kappa=\frac{1-\rho}{1-\lambda}.
$$

Put

$$
u=\frac{\delta}{1-\lambda}.
$$

The inequalities $\alpha<S$ and $s<1-\alpha$ give $\alpha<\lambda$.
Moreover, $X>0$ and

$$
X+Y+1-\rho=\lambda s<\lambda(1-\alpha)
$$

give

$$
\frac{\delta}{1-\lambda}<\alpha-\kappa<\lambda-\kappa.
$$

Thus $0\le u<\lambda-\kappa$.  The desired stronger inequality

$$
\gamma_5<\alpha-\frac{\delta(2-\delta)}{1-\alpha}
$$

follows from

$$
\kappa+u>\frac{(1-\lambda)u(2-(1-\lambda)u)}{1-\alpha}.
$$

Since $\alpha<\lambda$ in this non-overlap branch, it is enough to prove

$$
\kappa-u+(1-\lambda)u^2>0
$$

for $0\le u<\lambda-\kappa$.

Use

$$
\lambda=\frac{\kappa(2-\kappa)}{1-\kappa^2},\qquad 0<\kappa<\frac{1}{2}.
$$

Then

$$
1-\lambda=\frac{1-2\kappa}{1-\kappa^2},\qquad \lambda-\kappa=\frac{\kappa(1-\kappa+\kappa^2)}{1-\kappa^2}.
$$

The quadratic

$$
Q(u)=\kappa-u+(1-\lambda)u^2
$$

is decreasing on $[0,\lambda-\kappa]$, and

$$
Q(\lambda-\kappa)=
\frac{\kappa^2(1-2\kappa)(2\kappa^4-2\kappa^3+\kappa^2-2\kappa+2)}{(1-\kappa)^3(1+\kappa)^3}>0.
$$

Thus $Q(u)>0$.  Hence the stronger inequality holds, so

$$
\Psi^-_{1-\alpha,1-\gamma_5}(A_C)>0.
$$

Therefore $B_5<A_1$.

### 3.2. The containment case $\alpha\ge T$

### Lemma 3.2

If $\alpha\ge T$, then

$$
B_5<A_1.
$$

### Proof

Put

$$
g=\gamma_5,
\qquad
c=1-g,
\qquad
z=\frac{\alpha-g}{1-g},
$$

and let

$$
m(x)=\sqrt{1-x+x^2}.
$$

A selected $T_-$ label has $1-\alpha<c$, hence $g<\alpha$.  Since
$\alpha<1/2$,

$$
0<z<\frac12,
\qquad
1-\alpha=c(1-z).
$$

The exact $T_-$ formula therefore becomes

$$
B_5=m(z)-c(1-z).
$$

We first record the selector consequence

$$
\boxed{c\le m(z).}
$$

Indeed, at the $T_-$ point one has

$$
a=c(1-z),
\qquad
b=m(z)-a,
\qquad
a+b=m(z).
$$

The exact Cell-$T$ condition $q\ge0$ from `2011` becomes

$$
-(1-z)c^2+m(z)c-zm(z)^2\ge0.
$$

As a quadratic in $c$, the boundary equation has roots

$$
\frac{zm(z)}{1-z}
\qquad\text{and}\qquad
m(z).
$$

Because $z<1/2$, the selector inequality places $c$ between these roots,
and in particular $c\le m(z)$.

Hardness already gave $A_1=A_C$ and $s\le p_1<t$.  Since

$$
p_1=\frac1D-\alpha<1-\alpha,
$$

one has $s<1-\alpha$.  Thus

$$
X+Y+1-\rho=\lambda s<\lambda(1-\alpha).
$$

Containment gives $\lambda<\alpha<1/2$.  Hence the second candidate in
the formula for $\gamma_5$ satisfies

$$
\frac{\rho-X-Y}{\lambda}
>\frac{1-\lambda(1-\alpha)}{\lambda}
>1.
$$

The last inequality is equivalent to $\lambda(2-\alpha)<1$, which follows
from $\lambda<\alpha<1/2$ and $\alpha(2-\alpha)<1$.

On the other hand $T=X+\lambda\le\alpha<1/2$ makes
$X/(1-\lambda)<1$.  Therefore the active radial exit is

$$
g=\frac{X}{1-\lambda},
\qquad
X=(1-\lambda)(1-c).
$$

Write $A=A_C=\lambda-Y$.  The preceding strict inequality gives

$$
A>A_0:=\lambda\alpha+(1-\lambda)g+1-\rho
=2-c-\rho+\lambda cz.
$$

Since $Y>0$, also $A<\lambda$, so

$$
2-\rho-\lambda<c(1-\lambda z)
\le m(z)(1-\lambda z).
$$

Furthermore, $\alpha\ge T=X+\lambda$ is, after substituting for $X$,

$$
g+cz\ge g+\lambda c,
$$

and hence

$$
z\ge\lambda.
$$

We claim that the strict inequality above forces

$$
\boxed{\lambda>z m(z).}
$$

Suppose instead that $\lambda\le z m(z)$.  For fixed $\lambda$, define

$$
E(x)=2-\rho-\lambda-m(x)(1-\lambda x).
$$

On $0<x<1/2$,

$$
E'(x)=
\frac{(1-2x)(1-\lambda x)}{2m(x)}+\lambda m(x)>0,
$$

and

$$
\frac{d}{dx}\bigl(xm(x)\bigr)
=\frac{2-3x+4x^2}{2m(x)}>0.
$$

There is therefore a unique $z_0\le z$ such that

$$
\lambda=z_0m(z_0).
$$

Put $m_0=m(z_0)$.  Since $m_0<1$, one has $\lambda<z_0$; since
$m$ is decreasing on $(0,1/2)$,

$$
m_0<m(\lambda)=\rho.
$$

At this point,

$$
\begin{aligned}
E(z_0)
&=2-\rho-m_0-\lambda+\lambda^2\\
&=(1-m_0)-\rho(1-\rho)>0.
\end{aligned}
$$

Monotonicity gives $E(z)>0$, contradicting

$$
2-\rho-\lambda<m(z)(1-\lambda z).
$$

This proves $\lambda>zm(z)$.  Now use $c\le m(z)$,
$z\ge\lambda$, and hence $m(z)\le m(\lambda)=\rho$ to obtain

$$
\begin{aligned}
A_0-B_5
&=2-\rho-m(z)-(1-\lambda)cz\\
&\ge2-\rho-m(z)-(1-\lambda)m(z)z\\
&>2-\rho-m(z)-\lambda(1-\lambda)\\
&\ge2-2\rho-\lambda(1-\lambda)\\
&=\frac{\lambda(1-\lambda)(1-\rho)}{1+\rho}>0.
\end{aligned}
$$

Consequently

$$
B_5<A_0<A=A_C=A_1.
$$

This closes the containment case and completes the proof for
$A_5=1-\alpha$.

## 4. Left-$T_-$: overlap middle branch

Assume

$$
B_5=T_-,\qquad A_5=1-T,\qquad s\le p_1<t.
$$

Then $A_1=A_C$.

### Lemma 4.1

In this branch,

$$
B_5<A_1.
$$

### Proof

In the overlap branch, the active $r_5$ exit is $X/(1-\lambda)$, so

$$
C_5=\frac{A_5}{1-\lambda}.
$$

Substituting into the $T_-$ equation gives

$$
A_5+B_5=\rho.
$$

Since $A_5=1-T$, we get

$$
B_5=T+\rho-1.
$$

Using $T=X+\lambda$ and $X=\lambda s+A_C+\rho-1-\lambda$ gives

$$
B_5=\lambda s+A_C+2\rho-2.
$$

Thus $B_5<A_C$ is equivalent to

$$
\lambda s<2(1-\rho).
$$

Because $A_5=1-T$ is the overlap branch, $\alpha\ge S$.  Because $s\le p_1$, we have

$$
\alpha+p_1\ge S+s.
$$

But

$$
\alpha+p_1=\frac{1}{D}<1.
$$

Therefore

$$
S+s<1.
$$

Since

$$
S=\frac{\lambda s}{1-\lambda},
$$

this gives

$$
\frac{s}{1-\lambda}<1,\qquad s<1-\lambda.
$$

Hence

$$
\lambda s<\lambda(1-\lambda)=1-\rho^2=(1-\rho)(1+\rho)<2(1-\rho).
$$

Therefore $B_5<A_C=A_1$.

## 5. Left-$T_-$: overlap $S$-dominance

Assume

$$
B_5=T_-,\qquad A_5=1-T,\qquad A_1\ge S,\qquad S\le \frac{Y}{\lambda}.
$$

### Lemma 5.1

In this branch,

$$
B_5<A_1.
$$

### Proof

As in Lemma 4.1, in the overlap branch

$$
A_5=1-T=1-X-\lambda,\qquad C_5=\frac{A_5}{1-\lambda}.
$$

Let $a=A_5$.  Use the exact $T_-$ root-order test and monotonicity from
[`2011`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md).
At the comparison point $S$ its expression is

$$
\Psi^-_{a,C_5}(S)= \frac{a^2}{(1-\lambda)^2}H(S),
$$

where

$$
H(S)=S^2+2aS+X^2+2\lambda X-2X-\lambda.
$$

The function $H$ is increasing in $S$. From $S\le Y/\lambda$ one obtains

$$
S\ge \frac{X+1-\rho}{1-2\lambda}
$$

and $0<\lambda<1/2$. We now check the substitution explicitly. Put

$$
x=\lambda,
\qquad
S_0=\frac{X+1-\rho}{1-2x}.
$$

Multiplication by the positive denominator $(1-2x)^2$ gives

$$
\begin{aligned}
(1-2x)^2H(S_0)
={}&p(x)+q(x)\rho\\
&+4x\left(2-3x+2x^2-\rho\right)X
+4x^2X^2,
\end{aligned}
$$

where

$$
p(x)=4-8x+9x^2-4x^3,
\qquad
q(x)=-4+6x-4x^2.
$$

On $0<x<1/2$, one has $p>0$ and $q<0$. Indeed, both $p$ and
$4-6x+4x^2$ are positive there. Moreover,

$$
p(x)^2-q(x)^2\rho^2
=x^2\left(4-12x+13x^2-8x^3\right)>0.
$$

The cubic in parentheses is decreasing on $[0,1/2]$ and has value $1/4$ at
$1/2$. Hence $p>|q|\rho$ and the constant term is positive. Also

$$
2-3x+2x^2>1>\rho,
$$

so the coefficient of $X$ is positive, and the coefficient of $X^2$ is
positive. Therefore $H(S_0)>0$.

Thus

$$
\Psi^-_{A_5,C_5}(S)>0.
$$

Since $\Psi^-_{A_5,C_5}(x)$ is increasing in $x$ and $A_1\ge S$,

$$
\Psi^-_{A_5,C_5}(A_1)>0.
$$

The $T_-$ root-order test gives $B_5<A_1$.

## 6. Final overlap residual with right $T_+^{hi}$

We first record the only calculus estimate needed in this section.

### Lemma 6.1

Let

$$
0<\kappa<\frac{1}{2},
\qquad
\lambda=\frac{\kappa(2-\kappa)}{1-\kappa^2},
$$

and put

$$
y_*=\frac{\kappa(1-2\kappa)}{(1-\kappa)(2-\kappa)}.
$$

Then, for $0\le y<y_*$,

$$
e(y)<\kappa+\frac{\lambda}{1-\lambda}y.
$$

### Proof

First, $y_*<1/8$, because this inequality is equivalent to

$$
2-11\kappa+17\kappa^2>0,
$$

whose discriminant is $121-136<0$.  Define

$$
L(y)=\kappa+\frac{\lambda}{1-\lambda}y
=\kappa+\frac{\kappa(2-\kappa)}{1-2\kappa}y.
$$

On $[0,1/8]$,

$$
e''(y)=
\frac{2(y-1)(8(y-1)^2-9)}{(4(y-1)^2-3)^{3/2}}>0.
$$

Thus $L-e$ is concave on $[0,y_*]$, so it is enough to check its two
endpoints.  At $0$ one has $L(0)-e(0)=\kappa>0$.  At the other endpoint,

$$
L(y_*)=\frac{\kappa}{1-\kappa}=:b_0.
$$

Put $c_*=1-y_*$.  The value $e(y_*)$ is the smaller positive root of

$$
P(b)=b^2-c_*b+c_*^2(1-c_*^2).
$$

Direct substitution gives

$$
P(b_0)=
-\frac{\kappa^2(1-2\kappa)^2Q(\kappa)}{(2-\kappa)^4(1-\kappa)^4},
$$

where

$$
Q(\kappa)=17\kappa^4-62\kappa^3+94\kappa^2-68\kappa+20.
$$

Here $Q>0$ on $(0,1/2)$.  Indeed,

$$
Q''(\kappa)=204\kappa^2-372\kappa+188>0
$$

because its discriminant is negative.  Hence $Q'$ is increasing; since
$Q'(1/2)<0$, it is negative on $(0,1/2)$.  Therefore $Q$ is decreasing and

$$
Q(\kappa)>Q(1/2)=\frac{45}{16}>0.
$$

It follows that $P(b_0)<0$, whereas $P(0)>0$.  Thus $b_0$ lies strictly to
the right of the smaller root, so $e(y_*)<L(y_*)$.  Concavity now gives
$e(y)<L(y)$ throughout $[0,y_*]$.

The only left-$T_-$ case not covered by Sections 3--5 is

$$
A_5=1-T,\qquad A_1=q,\qquad B_1=T_+^{hi},
$$

where $T_0$ misses the $r_1$ exit.

If $B_5\le q$, then $B_5+B_1<1$ immediately.  Assume $B_5>q$.

Since $B_5=T+\rho-1$, $B_5>q$ implies

$$
T+\rho-1>q>S.
$$

Hence

$$
T-S>1-\rho.
$$

Set

$$
y=\frac{Y}{\lambda},\qquad \kappa=\frac{1-\rho}{1-\lambda}.
$$

The inequality $T-S>1-\rho$ implies

$$
y<y_*(\kappa):=\frac{\kappa(1-2\kappa)}{(1-\kappa)(2-\kappa)}.
$$

Also

$$
S>\kappa+\frac{\lambda}{1-\lambda}y.
$$

For $0<\kappa<1/2$ and $0\le y<y_*(\kappa)$, Lemma 6.1 gives

$$
e(y)<\kappa+\frac{\lambda}{1-\lambda}y
$$

holds.  Hence

$$
e(y)<S<q.
$$

Since $\gamma\le y$ and $e$ is increasing,

$$
e(\gamma)<q.
$$

Moreover $y<1/8$, so

$$
\gamma<1-\frac{\sqrt3}{2}.
$$

But a realized right $T_+^{hi}$ branch satisfies the right-high filter

$$
\gamma\ge1-\frac{\sqrt3}{2}\quad\text{or}\quad q\le e(\gamma).
$$

This contradiction rules out the residual.  Therefore the entire left-$T_-$ family is proved.

## 7. Conclusion

After this file and `4074`, the following genuine cases are proved:

$$
A_1+A_5>1,
$$

$$
(L,\mathrm{Full}),
$$

$$
\{L,T_-\}^2,
$$

and all branches with first coordinate $T_-$.

In particular, every genuine branch with first coordinate $T_-$ satisfies

$$
\boxed{B_5+B_1<1.}
$$

The remaining $L$, Full, and $T_+^{hi}$ first-coordinate families are treated
in `4074`, `4078`, `4079`, and `407a`.
