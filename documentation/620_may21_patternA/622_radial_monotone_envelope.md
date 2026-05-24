# Radial Monotone Envelope and Elimination of $p$

Status: Proven analytic inequality

This file proves that the Pattern A radial sum

$$
R_{q,r}(p)=\rho(r,p)+\rho(p,q)
$$

has an explicit lower envelope.  This removes the middle parameter $p$ from the hard inequality.

## 1. Setup

Work in the lower outside-quarter region

$$
q<\frac14,\qquad q<r,\qquad q\le p\le r,
$$

with

$$
r^2+r(1-q)+(1-q)^2\le1.
$$

For $0\le B\le A<2/5$, define

$$
\rho(A,B)=1-c^{\max}(1-A,B)
$$

and

$$
\Phi(A,B)=(1-A+B)^4-(1-A+B)^2+B(1-A).
$$

Let $\sigma(A)$ be the unique switch satisfying

$$
\Phi(A,\sigma(A))=0.
$$

For $B<\sigma(A)$, $\rho(A,B)=\rho_1(B)$, where $\rho_1(B)=1-c_1(B)$ and $c_1(B)$ is the largest root of

$$
c^4-c^2+Bc-B^2=0.
$$

For $B>\sigma(A)$,

$$
\rho(A,B)=\rho_2(A,B)=1-\frac{2(1-A)}{1+\sqrt{4(1-A+B)^2-3}}.
$$

## 2. Unique switch

For fixed $A\in(0,2/5)$, the function $B\mapsto\Phi(A,B)$ is strictly increasing on $0\le B\le A$.

With $s=1-A+B$,

$$
\frac{\partial\Phi}{\partial B}=4s^3-2s+(1-A).
$$

Since $1-A>3/5$ and $s\ge1-A$, this derivative is positive.  Also

$$
\Phi(A,0)=(1-A)^4-(1-A)^2<0,
$$

and

$$
\Phi(A,A)=A(1-A)>0.
$$

Thus a unique switch $\sigma(A)\in(0,A)$ exists.

## 3. Switch parametrization

At the switch, set

$$
s=1-A+\sigma(A),\qquad g=\sqrt{4s^2-3}.
$$

The switch equation is equivalent to

$$
1-A=\frac{s(1+g)}2,
\qquad
\sigma(A)=\frac{s(1-g)}2.
$$

At the switch,

$$
\rho(A,\sigma(A))=A-\sigma(A).
$$

Moreover,

$$
\sigma'(A)=\frac{2g^2-g+3}{2g^2+g+3},
$$

so $0<\sigma'(A)<1$.

## 4. Branch order in $p$

If $q\ge\sigma(r)$, then $p\ge q\ge\sigma(r)$ and, by monotonicity of $\sigma$, also $q\ge\sigma(p)$.  Hence both radial terms are Cell $2$:

$$
R_{q,r}(p)=\rho_2(r,p)+\rho_2(p,q).
$$

If $q<\sigma(r)$, let

$$
\beta(q)=\sigma^{-1}(q).
$$

Then the interval $q\le p\le r$ decomposes as

$$
[q,\sigma(r)]\cup[\sigma(r),\beta(q)]\cup[\beta(q),r],
$$

with branch types

$$
(1,2),\qquad (2,2),\qquad (2,1).
$$

The branch type $(1,1)$ cannot occur.  Indeed, the switch-iterate inequality

$$
\sigma(\sigma(A))<\frac A2
$$

holds in the lower region, while nonemptiness gives

$$
q\ge q_{\min}(r)=\frac{r+2-\sqrt{4-3r^2}}2>\frac r2.
$$

Thus $p\le\sigma(r)$ and $q\le\sigma(p)$ are incompatible.

## 5. Derivative lemmas

Let $h(A,B)=\rho_2(A,B)$.  Then

$$
h_B(A,B)=\frac{8(1-A)(1-A+B)}{\sqrt{4(1-A+B)^2-3}(1+\sqrt{4(1-A+B)^2-3})^2}>0.
$$

On the lower region,

$$
\rho_1'(B)>0,
\qquad
\rho_1'(B)\le1-2B,
$$

and

$$
h_A(A,B)\le -(1-2A).
$$

Also

$$
p\mapsto \rho_2(r,p)+\rho_2(p,q)
$$

is concave on each Cell $2/2$ interval.  These inequalities follow by differentiating the explicit formula for $\rho_2$ and the implicit equation for $\rho_1$; each reduces to a one-variable polynomial inequality after the standard Cell $1$ or switch parametrization.

## 6. First envelope theorem

If $q\ge\sigma(r)$, then

$$
\min_{q\le p\le r}R_{q,r}(p)=R_{q,r}(q)=\rho_2(r,q)+q.
$$

Proof.  The whole interval is Cell $2/2$.  The function is concave, so its minimum occurs at an endpoint.  At $p=q$,

$$
R_{q,r}(q)=\rho_2(r,q)+q,
$$

because $\rho(q,q)=q$.  At $p=r$,

$$
R_{q,r}(r)=r+\rho_2(r,q).
$$

Since $r>q$, $p=q$ gives the smaller endpoint.

If $q<\sigma(r)$, the minimum is initially reduced to

$$
\min\{R_{q,r}(\sigma(r)),R_{q,r}(\beta(q))\}.
$$

The next theorem removes the second candidate.

## 7. Strong comparison theorem

Assume $q<\sigma(r)$ and set $\beta=\beta(q)=\sigma^{-1}(q)$.  Then

$$
R_{q,r}(\beta)\ge R_{q,r}(\sigma(r)).
$$

Proof.  Since $q=\sigma(\beta)$, define

$$
D_r(\beta)=R_{q,r}(\beta)-R_{q,r}(\sigma(r)).
$$

At $\beta=\sigma(r)$, $D_r(\beta)=0$.  It suffices to prove $D_r'(\beta)>0$ for $\beta\in[\sigma(r),r]$.

Using $\rho(A,\sigma(A))=A-\sigma(A)$,

$$
D_r(\beta)=h(r,\beta)+\beta-\sigma(\beta)-r+\sigma(r)-h(\sigma(r),\sigma(\beta)).
$$

Thus

$$
D_r'(\beta)=h_B(r,\beta)+1-\sigma'(\beta)-h_B(\sigma(r),\sigma(\beta))\sigma'(\beta).
$$

Write

$$
h_B(A,B)=(1-A)f(1-A+B),
$$

where

$$
f(x)=\frac{8x}{\sqrt{4x^2-3}(1+\sqrt{4x^2-3})^2}.
$$

The function $f$ is decreasing on $(\sqrt3/2,1]$.  Since $\sigma'\le1$,

$$
1-r+\beta\le1-\sigma(r)+\sigma(\beta).
$$

Therefore

$$
\frac{h_B(r,\beta)}{h_B(\sigma(r),\sigma(\beta))}
\ge
\frac{1-r}{1-\sigma(r)}.
$$

It remains to prove

$$
\frac{1-r}{1-\sigma(r)}\ge\sigma'(r).
$$

Using the switch parametrization, this becomes

$$
6(g^2+1)\sqrt{g^2+3}-8g^2+4g-12\ge0.
$$

On the lower region, $g\ge1/3$.  Squaring after checking signs gives

$$
4(g+1)(9g^5-9g^4+38g^3-22g^2+33g-9)\ge0.
$$

The quintic factor is positive for $g\ge1/3$ because its value at $1/3$ is $8/9$ and its derivative is positive on $[1/3,\infty)$.  Hence $D_r'(\beta)>0$.

## 8. Final envelope

Therefore

$$
\min_{q\le p\le r}\{\rho(r,p)+\rho(p,q)\}
=
\begin{cases}
\rho_2(r,q)+q, & q\ge\sigma(r),\\
r-\sigma(r)+\rho_2(\sigma(r),q), & q<\sigma(r).
\end{cases}
$$

Thus Pattern A is reduced to

$$
\rho_2(r,q)+q\ge\tau(q,r)
\qquad(q\ge\sigma(r)),
$$

and

$$
r-\sigma(r)+\rho_2(\sigma(r),q)\ge\tau(q,r)
\qquad(q<\sigma(r)).
$$
