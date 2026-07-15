# First-Coordinate Full Branch in $407X$

Status: Proven

This file excludes every hard-region branch whose first coordinate is
$\mathrm{Full}$ in the $407X$ boundary-loss reduction.

Throughout, use the notation and standing hypotheses of
[`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md), and the support isolation of
[`4072_support_isolation_after_T0_T3_like.md`](4072_support_isolation_after_T0_T3_like.md).

The hard region is

$$
A_1+A_5\le1.
$$

## 1. First-coordinate Full is impossible

### Lemma 1.1

In the hard region, if $A_5=1-\alpha$, then

$$
B(A_5,C_5)\ne\mathrm{Full}.
$$

### Proof

The hard region gives $A_1\le\alpha$.  The case $A_1=q$ is impossible because $q>\alpha$.  Hence $A_1=A_C$, so $s\le p_1<t$.

The Full condition for $A_5=1-\alpha$ and $C_5=1-\gamma_5$ is

$$
1-\gamma_5\le\max(1-\alpha,\alpha).
$$

By the common support bound in `4073`, $\alpha<1/2$, so $\gamma_5\ge\alpha$.  Since $\gamma_5=X/(1-\lambda)$,

$$
X\ge(1-\lambda)\alpha.
$$

Also $A_C\le\alpha$ gives $Y\ge\lambda-\alpha$.  Therefore

$$
s=\frac{X+Y+1-\rho}{\lambda}
\ge
1-\alpha+\frac{1-\rho}{\lambda}>1-\alpha.
$$

But $p_1=1/D-\alpha<1-\alpha$.  Hence $s>p_1$, contradicting $s\le p_1$.

### Lemma 1.2

In the CE2 overlap case $A_5=1-T$, one has

$$
B(A_5,C_5)\ne\mathrm{Full}.
$$

### Proof

CE2 overlap gives $\alpha\ge S$.  By the common support bound in `4073`,

$$
S<\frac{1}{2}.
$$

Assume the left branch is Full.  Put $u=\gamma_5=X/(1-\lambda)$ and $T=X+\lambda$.

If $T\le1/2$, Full gives $u\ge T$.  Then $X/(1-\lambda)\ge X+\lambda$, so $X\ge1-\lambda$, and hence

$$
S\ge \frac{1-\lambda+1-\rho}{1-\lambda}>1,
$$

contradiction.

If $T\ge1/2$, Full gives $u\ge1-T$.  Then

$$
\frac{X}{1-\lambda}\ge1-X-\lambda,
$$

so

$$
X\ge\frac{(1-\lambda)^2}{2-\lambda}.
$$

Writing $a=1-\lambda$, this implies

$$
S\ge \frac{a^2/(1+a)+1-\sqrt{1-a+a^2}}{a}.
$$

This lower bound is $>1/2$ because

$$
\left(1-\frac{a}{2}+\frac{a^2}{1+a}\right)^2-(1-a+a^2)
=\frac{a^2(1-a)(3a+5)}{4(1+a)^2}>0.
$$

Again this contradicts $S<1/2$.

### Theorem 1.3

The hard region contains no first-coordinate Full branch:

$$
\boxed{B_5\ne\mathrm{Full}.}
$$

### Proof

The left input is either $A_5=1-\alpha$ or $A_5=1-T$.  Lemmas 1.1 and 1.2 exclude Full in both cases.
