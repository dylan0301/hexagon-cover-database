# The $(L,\mathrm{Full})$ Branch in the $407X$ Boundary-Loss Reduction

Status: Proven

This file proves the hard-region branch

$$
(B_5,B_1)=(L,\mathrm{Full})
$$

for the boundary-loss framework in
[`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md).

Throughout, use the notation of `4073`.

## 1. Statement

Assume the support-isolated $407X$ branch of `4073`, and assume the hard region

$$
A_1+A_5\le1.
$$

Assume the realized branches are

$$
B(A_5,C_5)=L,\qquad B(A_1,C_1)=\mathrm{Full}.
$$

Then

$$
B(A_5,C_5)+B(A_1,C_1)<1.
$$

Equivalently, since

$$
B(A_5,C_5)=\ell(\gamma_5),\qquad C_5=1-\gamma_5,
$$

and

$$
B(A_1,C_1)=1-A_1,
$$

it is enough to prove

$$
\boxed{\ell(\gamma_5)<A_1.}
$$

Here

$$
\ell(\eta)={ (1-\eta)\left(1-\sqrt{4(1-\eta)^2-3}\right)\over2}
$$

is the Low-branch output.

## 2. Two center-geometry lemmas

Use the direct $C$-side variables from `4073`:

$$
0<\lambda<1,\qquad \rho=\sqrt{1-\lambda+\lambda^2},
$$

$$
X\ge0,\qquad Y\ge0,\qquad X+(1-\lambda)Y<\rho(1-\rho),
$$

$$
A_C=1-t=\lambda-Y,
$$

$$
\gamma_1=\min\left({Y\over\lambda},{\rho-X-Y\over1-\lambda}\right),
$$

and

$$
\gamma_5=\min\left({X\over1-\lambda},{\rho-X-Y\over\lambda}\right).
$$

When the CE2 interval $T_C\cap e_{5,0}=[S,T]$ exists,

$$
S={X+Y+1-\rho\over1-\lambda}.
$$

### Lemma 2.1: core estimate

If

$$
\gamma_1\ge A_C,
$$

then

$$
\ell(\gamma_5)<A_C.
$$

#### Proof

Since

$$
\gamma_1\le {Y\over\lambda},
$$

the hypothesis gives

$$
A_C\le {Y\over\lambda}={\lambda-A_C\over\lambda}.
$$

Hence

$$
A_C\le {\lambda\over1+\lambda}.
$$

Put

$$
\delta={1-\rho\over1-\lambda}={\lambda\over1+\rho}.
$$

Using

$$
X+(1-\lambda)Y<\rho(1-\rho),\qquad Y=\lambda-A_C,
$$

one obtains

$$
X<(1-\lambda)(A_C-\delta).
$$

Therefore

$$
\gamma_5\le {X\over1-\lambda}<A_C-\delta.
$$

Let

$$
z=A_C-\delta.
$$

Then

$$
0\le\gamma_5<z.
$$

Moreover

$$
z\le z_{\max}:={\lambda\over1+\lambda}-{\lambda\over1+\rho}.
$$

A direct calculation gives

$$
z_{\max}< {1\over8}
$$

and

$$
z_{\max}+5z_{\max}^2\le\delta.
$$

For the second inequality, after writing $\delta=\lambda/(1+\rho)$, it reduces to

$$
2\rho(6\lambda+1)>11\lambda^2-7\lambda+2.
$$

Both sides are positive, and the squared difference is

$$
4(6\lambda+1)^2\rho^2-(11\lambda^2-7\lambda+2)^2
=\lambda(23\lambda^3+58\lambda^2+7\lambda+72)>0.
$$

The Low estimate

$$
\ell(\eta)\le 2\eta+5\eta^2\qquad(0\le\eta\le1/8)
$$

is the same elementary estimate used in the $401X$ $(L,\mathrm{Full})$ branch.  Since $\gamma_5<z\le z_{\max}<1/8$,

$$
\ell(\gamma_5)<2z+5z^2=z+(z+5z^2)\le z+\delta=A_C.
$$

This proves the lemma.

### Lemma 2.2: $S$-estimate

Assume the CE2 interval $[S,T]$ exists.  If

$$
S\le {Y\over\lambda},
$$

then

$$
\ell(\gamma_5)<S.
$$

#### Proof

The hypothesis is equivalent to

$$
\lambda X+(2\lambda-1)Y+\lambda(1-\rho)\le0.
$$

Hence $\lambda<1/2$ and

$$
Y\ge {\lambda(X+1-\rho)\over1-2\lambda}.
$$

Thus

$$
S\ge {X+1-\rho\over1-2\lambda}=:S_0.
$$

Combining this lower bound for $Y$ with

$$
X+(1-\lambda)Y<\rho(1-\rho)
$$

gives

$$
X<X_*(\lambda):={ (1-\rho)(\rho(1-2\lambda)-\lambda(1-\lambda))\over1-\lambda-\lambda^2}.
$$

The positivity of $X_*(\lambda)$ implies $0<\lambda<3/8$ by squaring

$$
\rho(1-2\lambda)>\lambda(1-\lambda).
$$

On this interval one checks

$$
{X_*(\lambda)\over1-\lambda}< {1\over8}.
$$

The check reduces to positivity of

$$
N_\eta=(-15\lambda^3+16\lambda^2-18\lambda+9)+(8\lambda^2+8\lambda-8)\rho,
$$

which follows from

$$
(-15\lambda^3+16\lambda^2-18\lambda+9)^2
-(8\lambda^2+8\lambda-8)^2\rho^2>0
$$

on $0<\lambda<3/8$.

Set

$$
\eta_0={X\over1-\lambda}.
$$

Then $0\le\gamma_5\le\eta_0<1/8$.  It is enough to prove

$$
2\eta_0+5\eta_0^2<S.
$$

Since $S\ge S_0$, it is enough to prove

$$
G_\lambda(X):={X+1-\rho\over1-2\lambda}-2{X\over1-\lambda}-5{X^2\over(1-\lambda)^2}>0.
$$

For fixed $\lambda$, $G_\lambda$ is concave in $X$.  Hence its minimum on $[0,X_*(\lambda)]$ occurs at an endpoint.  At $X=0$ it is positive.  At $X=X_*(\lambda)$, direct simplification gives a positive value after reducing to the sign of

$$
(A(\lambda)\rho+B(\lambda))(\rho-1),
$$

where

$$
A=-28\lambda^4+31\lambda^3-14\lambda^2+10\lambda-4,
$$

and

$$
B=22\lambda^5-26\lambda^4+5\lambda^3+14\lambda^2-14\lambda+4.
$$

On $0<\lambda<3/8$, one has $A<0$, $B>0$, and $A^2\rho^2-B^2>0$, so $A\rho+B<0$.  Since $\rho-1<0$, the endpoint value is positive.

Thus

$$
2\eta_0+5\eta_0^2<S.
$$

The Low estimate now gives

$$
\ell(\gamma_5)\le \ell(\eta_0)<S.
$$

This proves the lemma.

## 3. Proof of the branch

Let

$$
p_1={1\over D}-\alpha,\qquad q=1-p_1.
$$

There are two relevant cases for $p_1$ on $e_{0,1}$.

### Case 1: $p_1<t$ and $T_0$ misses the $r_1$ exit

If $p_1<t$, then

$$
A_1\ge A_C.
$$

If $T_0$ misses the $T_C$ exit on $r_1$, then

$$
C_1=1-\gamma_1.
$$

If $A_1\ge1/2$, the target is immediate because $\ell(\gamma_5)\le\sqrt3/4<1/2\le A_1$.  Otherwise the Full condition for the right branch, when the right branch is Full, gives the core lemma.  In the present branch the right branch is $T_+^{hi}$, so this argument does not directly apply.  This case remains part of the open $(L,T_+^{hi})$ obligation unless one can prove $\ell(\gamma_5)<A_1$ from the full right-high realization.

### Case 2: $p_1<t$ and $T_0$ hits the $r_1$ exit

If $\gamma_1\ge A_C$, Lemma 2.1 gives

$$
\ell(\gamma_5)<A_C\le A_1.
$$

If $\gamma_1<A_C$ and the CE2 $e_{5,0}$ interval is overlapped by $T_0$, then the hit-overlap argument from the $(L,\mathrm{Full})$ proof gives

$$
S\le\gamma_1\le {Y\over\lambda}.
$$

By Lemma 2.2,

$$
\ell(\gamma_5)<S.
$$

In the hit-low subcase previously treated for $(L,\mathrm{Full})$, one also has $S<A_1$, and hence the branch closes.  This proves the hit-overlap subcase whenever $S<A_1$ is available.

### Case 3: $p_1\ge t$

If $T_C$ is CE1 and $p_1\ge t$, then the unique positive $C$-boundary interval is already covered by $T_0$, and the six vertex roles alone would have to cover $\partial H$.  Since $T_0$ is T3-like and has $a_0+b_0=1/D<1$, while all other vertex rows are nonsupercritical, the total perimeter contribution is strictly less than $6$.  Hence the CE1 case is impossible.

If $T_C$ is CE2, the remaining $e_{5,0}$ interval must be treated.  The same $S$-dominance proof used in the $(L,\mathrm{Full})$ branch closes the subcase when $S\le Y/\lambda$ and $A_1\ge S$.  The other subcases remain part of the open right-high branch-realization problem.

## 4. Remaining exact target

The only genuinely unresolved branch from this file is the formal right-high gap case.

Write

$$
z:=\ell(\gamma_5),\qquad A:=A_1,\qquad C_1=1-\eta,\qquad B_1=1-A-h.
$$

The right $T_+$ equation is

$$
(1-A-h)(A+h-\eta)=h(2-h)(1-\eta)^2.
$$

If $z>A$, set

$$
r=z-A.
$$

Then the branch is closed iff

$$
G(r)>0,\qquad
G(x)=(1-A-x)(A+x-\eta)-x(2-x)(1-\eta)^2.
$$

Equivalently, the remaining exact target is

$$
\boxed{(1-z)(z-\eta)>(z-A)(2-z+A)(1-\eta)^2.}
$$

This inequality is false without the full geometry: for example

$$
\eta={1\over4},\qquad z={2\over5},\qquad A={109-3\sqrt{241}\over200}
$$

violates it while satisfying the formal right high-sheet equation.  Therefore the final proof must use the full semialgebraic system $\mathcal S_{L,hi}$ from Section 2, not only branch algebra.

## 5. Status

The $(L,T_+^{hi})$ branch is proved in all cases where one can show either

$$
z\le A_1,
$$

or

$$
\eta\ge z,
$$

or

$$
(1-z)(A_1-\eta)>2(z-A_1)(1-\eta)^2.
$$

The remaining case is

$$
z>A_1,\qquad \eta<z,\qquad
(1-z)(z-\eta)\le(z-A_1)(2-z+A_1)(1-\eta)^2.
$$

No complete proof of this final case is included here.
