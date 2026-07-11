# Low, $T_-$, and Lower-Sheet Branch Obligations in $407X$

Status: Proven

This file proves the hard-region branch obligations involving

$$
\mathcal R=\{L,T_-,T_+^{lo}\}
$$

and the full left-$T_-$ family in the $407X$ boundary-loss framework of
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
B_L< {1\over2}.
$$

### Proof

The Low branch output is

$$
B_L=\ell(\eta)={ (1-\eta)(1-\sqrt{4(1-\eta)^2-3})\over2}.
$$

Its maximum on the Low range occurs at $1-\eta=\sqrt3/2$ and is

$$
{\sqrt3\over4}< {1\over2}.
$$

### Lemma 1.2: lower-sheet outputs are small

If a realized branch is $T_+^{lo}$, then

$$
B_{T_+^{lo}}< {1\over2}.
$$

### Proof

For a $T_+$ branch, write

$$
\mu=a+b,\qquad \beta={b\over c}.
$$

The $T_+$ equation is

$$
\beta^2-\beta+1-\mu^2=0.
$$

On the lower sheet,

$$
\beta=\beta_-(\mu)={1-\sqrt{4\mu^2-3}\over2}\le {1\over2}.
$$

Thus

$$
b=c\beta\le {c\over2}.
$$

The $T_+$ candidate has $c<1$, so $b<1/2$.

### Lemma 1.3: $T_-$ outputs are input-bounded

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

## 2. The family $\mathcal R^2$

### Theorem 2.1

If

$$
(B_5,B_1)\in\mathcal R\times\mathcal R,\qquad \mathcal R=\{L,T_-,T_+^{lo}\},
$$

then

$$
B_5+B_1<1.
$$

### Proof

If at least one of the two branches is $L$ or $T_+^{lo}$, then one output is strictly less than $1/2$ by Lemmas 1.1 and 1.2, and the other output is at most $1/2$ by Lemmas 1.1--1.3.  Hence the sum is strictly less than $1$.

It remains to treat

$$
(B_5,B_1)=(T_-,T_-).
$$

By Lemma 1.3,

$$
B_5\le \min(A_5,1-A_5),\qquad B_1\le \min(A_1,1-A_1).
$$

Under $A_1+A_5\le1$,

$$
\min(A_5,1-A_5)+\min(A_1,1-A_1)\le1,
$$

with equality only if

$$
A_1=A_5={1\over2}.
$$

Therefore equality $B_5+B_1=1$ would force

$$
A_1=A_5=B_1=B_5={1\over2}.
$$

For the $T_-$ equation

$$
((a+b)^2-1)c^2+ac-a^2=0,
$$

substituting $a=b=1/2$ gives

$$
{1\over2}c-{1\over4}=0,
$$

so $c=1/2$.  Applying this to the $T_5$ side gives

$$
C_5={1\over2}.
$$

But $C_5=1-\gamma_5$, and $T_C$ covers exactly $M_0$ among the radial midpoints.  Since $M_5$ lies at coordinate $1/2$ on $r_5$ and $T_C\cap r_5=[0,\gamma_5]$ is closed, $M_5\notin T_C$ implies

$$
\gamma_5<{1\over2},\qquad C_5>{1\over2},
$$

contradiction.  Therefore equality is impossible, and the sum is strictly less than $1$.

## 3. Left-$T_-$: non-overlap branch

Assume

$$
B_5=T_-,\qquad A_5=1-\alpha.
$$

In the hard region, one necessarily has

$$
A_1=A_C=1-t,\qquad A_C\le\alpha<S.
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

Since $A_5=1-\alpha$, $A_1=A_C$, and $C_5=1-\gamma_5$, the $T_-$ root-order expression is

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
\gamma_5\le {X\over1-\lambda},
$$

we obtain

$$
\gamma_5<\alpha-\kappa-{\delta\over1-\lambda},\qquad \kappa={1-\rho\over1-\lambda}.
$$

Put

$$
u={\delta\over1-\lambda}.
$$

The non-overlap constraints give $0\le u<\lambda-\kappa$.  The desired stronger inequality

$$
\gamma_5<\alpha-{\delta(2-\delta)\over1-\alpha}
$$

follows from

$$
\kappa+u>{(1-\lambda)u(2-(1-\lambda)u)\over1-\alpha}.
$$

Since $\alpha<\lambda$ in this non-overlap branch, it is enough to prove

$$
\kappa-u+(1-\lambda)u^2>0
$$

for $0\le u<\lambda-\kappa$.

Use

$$
\lambda={\kappa(2-\kappa)\over1-\kappa^2},\qquad 0<\kappa<{1\over2}.
$$

Then

$$
1-\lambda={1-2\kappa\over1-\kappa^2},\qquad \lambda-\kappa={\kappa(1-\kappa+\kappa^2)\over1-\kappa^2}.
$$

The quadratic

$$
Q(u)=\kappa-u+(1-\lambda)u^2
$$

is decreasing on $[0,\lambda-\kappa]$, and

$$
Q(\lambda-\kappa)=
{\kappa^2(1-2\kappa)(2\kappa^4-2\kappa^3+\kappa^2-2\kappa+2)
\over(1-\kappa)^3(1+\kappa)^3}>0.
$$

Thus $Q(u)>0$.  Hence the stronger inequality holds, so

$$
\Psi^-_{1-\alpha,1-\gamma_5}(A_C)>0.
$$

Therefore $B_5<A_1$.

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
C_5={A_5\over1-\lambda}.
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
\alpha+p_1={1\over D}<1.
$$

Therefore

$$
S+s<1.
$$

Since

$$
S={\lambda s\over1-\lambda},
$$

this gives

$$
{s\over1-\lambda}<1,\qquad s<1-\lambda.
$$

Hence

$$
\lambda s<\lambda(1-\lambda)=1-\rho^2=(1-\rho)(1+\rho)<2(1-\rho).
$$

Therefore $B_5<A_C=A_1$.

## 5. Left-$T_-$: overlap $S$-dominance

Assume

$$
B_5=T_-,\qquad A_5=1-T,\qquad A_1\ge S,\qquad S\le {Y\over\lambda}.
$$

### Lemma 5.1

In this branch,

$$
B_5<A_1.
$$

### Proof

As in Lemma 4.1, in the overlap branch

$$
A_5=1-T=1-X-\lambda,\qquad C_5={A_5\over1-\lambda}.
$$

Let $a=A_5$.  For the $T_-$ root-order expression at $S$,

$$
\Psi^-_{a,C_5}(S)= {a^2\over(1-\lambda)^2}H(S),
$$

where

$$
H(S)=S^2+2aS+X^2+2\lambda X-2X-\lambda.
$$

The function $H$ is increasing in $S$. From $S\le Y/\lambda$ one obtains

$$
S\ge {X+1-\rho\over1-2\lambda}
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
y={Y\over\lambda},\qquad \kappa={1-\rho\over1-\lambda}.
$$

The inequality $T-S>1-\rho$ implies

$$
y<y_*(\kappa):={\kappa(1-2\kappa)\over(1-\kappa)(2-\kappa)}.
$$

Also

$$
S>\kappa+{\lambda\over1-\lambda}y.
$$

For $0<\kappa<1/2$ and $0\le y<y_*(\kappa)$, the calculus lemma

$$
\ell(y)<\kappa+{\lambda\over1-\lambda}y
$$

holds.  Hence

$$
\ell(y)<S<q.
$$

Since $\gamma\le y$ and $\ell$ is increasing,

$$
\ell(\gamma)<q.
$$

Moreover $y<1/8$, so

$$
\gamma<1-{\sqrt3\over2}.
$$

But a realized right $T_+^{hi}$ branch satisfies the right-high filter

$$
\gamma\ge1-{\sqrt3\over2}\quad\text{or}\quad q\le\ell(\gamma).
$$

This contradiction rules out the residual.  Therefore the entire left-$T_-$ family is proved.

## 7. Exact-formula inventory note

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

The exact audit in `4015` deletes $T_+^{lo}$ completely. The remaining genuine
branch obligations at this stage of the historical file order are:

$$
(L,T_+^{hi}),
$$

possible first-coordinate Full branches,

$$
(\mathrm{Full},*),
$$

possible first-coordinate high branches,

$$
(T_+^{hi},*),
$$

There are no lower-sheet obligations.
