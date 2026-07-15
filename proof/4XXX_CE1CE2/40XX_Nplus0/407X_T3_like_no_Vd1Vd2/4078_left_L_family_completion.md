# Completion of the Left-Low Family in $407X$

Status: Proven

This file closes the remaining hard-region branches with first coordinate

$$
B_5=B(A_5,C_5)=L.
$$

Together with `4074` and `4075`, it proves

$$
B_5=L\quad\Longrightarrow\quad B_5+B_1<1
$$

for every realized right branch in the support-isolated $407X$ domain.

The detailed polynomial, convexity, and center-transfer computations used
below are recorded in
[`407c_rigor_completion_details.md`](407c_rigor_completion_details.md),
Section 1.

## 1. Low branch separation

### Lemma 1.1

Let $0\le\eta\le1-\sqrt3/2$ and let $z=e(\eta)$.  If the Low candidate is realized for input $a=1-\beta$, then

$$
\boxed{\beta\ge z+\eta.}
$$

### Proof

The Low equation is

$$
z^2-(1-\eta)z+(1-\eta)^2\left(1-(1-\eta)^2\right)=0.
$$

Equivalently $P(\eta,z)=0$, where

$$
P(x,z)=x^4-4x^3+5x^2-(2+z)x+z-z^2.
$$

The Low cell condition contains

$$
(a+z)^4-(a+z)^2+az\le0.
$$

With $a=1-\beta$ and $h=\beta-z$, this is $P(h,z)\le0$. The domain
condition $a+z\le1$ gives $h\ge0$; see
[`407c_rigor_completion_details.md`](407c_rigor_completion_details.md),
Lemma 1.1. On $0\le x\le1-\sqrt3/2<1/7$,

$$
\frac{\partial P}{\partial x}=4x^3-12x^2+10x-(2+z)<0.
$$

Thus $P$ is strictly decreasing on the Low range.  If $h<\eta$, then $P(h,z)>P(\eta,z)=0$, contradiction.  Hence $h\ge\eta$, proving $\beta\ge z+\eta$.

## 2. Cases with $e(\gamma_5)<A_1$

### Theorem 2.1

If the hard region holds, the left branch is Low, and $A_5=1-\alpha$, then

$$
e(\gamma_5)<A_1.
$$

### Proof

The hard region gives $A_1\le\alpha$.  The case $A_1=q$ is impossible because $q=\alpha+(D-1)/D>\alpha$.  Hence $A_1=A_C$.  Put $A=A_C$.

The middle condition $s\le p_1$ gives

$$
\frac{X+Y+1-\rho}{\lambda}\le \frac{1}{D}-\alpha.
$$

Using $Y=\lambda-A$ and $\gamma_5\le X/(1-\lambda)$,

$$
(1-\lambda)\gamma_5\le \rho-1-\lambda+A+\frac{\lambda}{D}-\lambda\alpha.
$$

By Lemma 1.1 applied to $A_5=1-\alpha$,

$$
\alpha\ge e(\gamma_5)+\gamma_5.
$$

If $e(\gamma_5)\ge A$, then

$$
\gamma_5\le G:=(1-\lambda)A+\rho-1-\lambda+\frac{\lambda}{D}\le (1-\lambda)A+\rho-1.
$$

Here the hard inequality gives $0<A\le\alpha<1/2$, and
$A=\lambda-Y<\lambda$.  Put

$$
r_A=\sqrt{1-A+A^2},
\qquad
g=r_A(1-r_A),
$$

so $r_A>\sqrt3/2$ and

$$
0<g<\frac{\sqrt3}{2}\left(1-\frac{\sqrt3}{2}\right)<\frac{1}{8}.
$$

For $A\le x\le1$, define

$$
h_A(x)=(1-x)A+\sqrt{1-x+x^2}-1.
$$

Then

$$
h_A''(x)=\frac{3}{4(1-x+x^2)^{3/2}}>0.
$$

Thus $h_A$ is convex, so its maximum on $[A,1]$ is attained at an endpoint.
The endpoint values are

$$
h_A(A)=g,
\qquad
h_A(1)=0.
$$

Since $\lambda\in(A,1)$, the preceding bound on $\gamma_5$ now gives

$$
\gamma_5\le h_A(\lambda)\le g.
$$

The elementary bound $e(x)\le2x+5x^2$ on $[0,1/8]$, together with the
comparison in
[`407c_rigor_completion_details.md`](407c_rigor_completion_details.md),
Lemma 1.2, gives

$$
e(\gamma_5)\le2\gamma_5+5\gamma_5^2<A,
$$

contradiction.  Thus $e(\gamma_5)<A=A_1$.

### Theorem 2.2

If the hard region holds, the left branch is Low, $A_5=1-T$, and $A_1=A_C$, then

$$
e(\gamma_5)<A_1.
$$

### Proof

Put $A=A_C$.  Since $A_1=A_C$, one has $s\le p_1<t$.  Since $A_5=1-T$ is CE2 overlap, $\alpha\ge S$.  Hence

$$
s+S\le p_1+\alpha=\frac{1}{D}<1.
$$

Writing $W=X+Y+1-\rho$, this gives $W<\lambda(1-\lambda)$, so

$$
\gamma_5=\frac{X}{1-\lambda}
$$

and

$$
\gamma_5<G_1:=\frac{A+\rho-1-\lambda^2}{1-\lambda}.
$$

Lemma 1.1 applied to $A_5=1-T$ gives $T\ge e(\gamma_5)+\gamma_5$.  If $e(\gamma_5)\ge A$, then $\gamma_5\le T-A=X+Y$, hence

$$
\gamma_5\le G_2:=\frac{\lambda-A}{\lambda}.
$$

Thus $\gamma_5\le G=\min(G_1,G_2)$. The detailed comparison in
[`407c_rigor_completion_details.md`](407c_rigor_completion_details.md),
Lemma 1.3, gives $e(G)<A$. Therefore $e(\gamma_5)<A$, contradiction.
Hence $e(\gamma_5)<A_1$.

## 3. CE2 overlap with $A_1=q$

### Lemma 3.1: $p_1<s$

Assume $A_5=1-T$, $B_5=L$, and $A_1=q$ because $p_1<s$.  Then

$$
e(\gamma_5)<q.
$$

### Proof

Lemma 1.1 gives $T\ge e(\gamma_5)+\gamma_5$, so $e(\gamma_5)\le T-\gamma_5$.  Since $p_1<s$, one has $q=1-p_1>1-s$.  The hard region gives $q\le T$, so $s+T>1$.  The center identity

$$
T-\gamma_5-S=\frac{\lambda}{1-\lambda}(1-s-T)
$$

gives $T-\gamma_5<S$.  Hence $e(\gamma_5)<S$.  Since CE2 overlap gives $q>S$, we get $e(\gamma_5)<q$.

### Lemma 3.2: $p_1\ge t$ and right high sheet

Assume $A_5=1-T$, $B_5=L$, $A_1=q$ because $p_1\ge t$, and $B_1=T_+^{hi}$.  Then

$$
e(\gamma_5)<q.
$$

### Proof

Let $u=\gamma_5$, $z=e(u)$, and $y=Y/\lambda$.  Lemma 1.1 gives $T\ge z+u$.  Since $T=(1-\lambda)u+\lambda$,

$$
\lambda\ge \frac{z}{1-u}.
$$

The center-transfer lemma in
[`407c_rigor_completion_details.md`](407c_rigor_completion_details.md),
Lemma 1.4, applies to

$$
S=u+\frac{\lambda}{1+\rho}+\frac{\lambda}{1-\lambda}y.
$$

If $T_0$ hits the exit on $r_1$, then `4074` gives $e(\gamma_5)<S<q$.  In the miss case, $C_1=1-\gamma_1$ and $\gamma_1\le y$.  The right high-sheet filter gives

$$
\gamma_1\ge1-\sqrt3/2
\quad\text{or}\quad
q\le e(\gamma_1).
$$

Thus either $y\ge1-\sqrt3/2$, or
$S<q\le e(\gamma_1)\le e(y)$. In both alternatives,
[`407c_rigor_completion_details.md`](407c_rigor_completion_details.md),
Lemma 1.4, gives $e(\gamma_5)<S<q$.

## 4. Completion

The branch $(L,\mathrm{Full})$ is proved in `4074`. The genuine branches with
right label $L$ or $T_-$ are covered by `4075`. The only remaining exact
left-Low branch is right high sheet, and the preceding theorems cover all left
input cases. In those cases $B_5<A_1$, while $B_1\le1-A_1$, so

$$
B_5+B_1<1.
$$

Therefore

$$
\boxed{B_5=L\quad\Longrightarrow\quad B_5+B_1<1.}
$$
