# Completion of the Left-Low Family in $407X$

Status: Proven

This file closes the remaining hard-region branches with first coordinate

$$
B_5=B(A_5,C_5)=L
$$

in the boundary-loss framework of
[`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md).  Together with `4074` and `4075`, it proves

$$
B_5=L\quad\Longrightarrow\quad B_5+B_1<1
$$

for every realized right branch in the support-isolated $407X$ domain.

Throughout use the notation of `4073`.  Let

$$
z=\ell(\gamma_5)
$$

when the left branch is Low.

## 1. Low branch separation

### Lemma 1.1

Let $0\le\eta\le1-\sqrt3/2$ and let $z=\ell(\eta)$.  If the Low candidate is realized for input $a=1-\beta$, then

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

With $a=1-\beta$ and $h=\beta-z$, this is $P(h,z)\le0$.  On $0\le x\le1-\sqrt3/2<1/7$,

$$
{\partial P\over\partial x}=4x^3-12x^2+10x-(2+z)<0.
$$

Thus $P$ is strictly decreasing on the Low range.  If $h<\eta$, then $P(h,z)>P(\eta,z)=0$, contradiction.  Hence $h\ge\eta$, proving $\beta\ge z+\eta$.

## 2. Non-overlap left input

### Theorem 2.1

Assume the hard region $A_1+A_5\le1$, the left Low branch, and

$$
A_5=1-\alpha.
$$

Then

$$
\boxed{\ell(\gamma_5)<A_1.}
$$

### Proof

The hard region gives $A_1\le\alpha$.  The case $A_1=q$ is impossible because

$$
q=\alpha+{D-1\over D}>\alpha.
$$

Hence $A_1=A_C$.  Put $A=A_C$.  The middle condition $s\le p_1$ gives

$$
{X+Y+1-\rho\over\lambda}\le{1\over D}-\alpha.
$$

Using $Y=\lambda-A$ and $\gamma_5\le X/(1-\lambda)$,

$$
(1-\lambda)\gamma_5\le \rho-1-\lambda+A+{\lambda\over D}-\lambda\alpha.
$$

By Lemma 1.1 applied to $A_5=1-\alpha$,

$$
\alpha\ge \ell(\gamma_5)+\gamma_5.
$$

Assume for contradiction that $\ell(\gamma_5)\ge A$.  Then $\alpha\ge A+\gamma_5$, and therefore

$$
\gamma_5\le G:=(1-\lambda)A+\rho-1-\lambda+{\lambda\over D}.
$$

Since $D\ge1$,

$$
G\le (1-\lambda)A+\rho-1.
$$

Let $r_A=\sqrt{1-A+A^2}$.  Convexity of $x\mapsto\sqrt{1-x+x^2}-Ax$ on $[A,1]$ gives

$$
(1-\lambda)A+\rho-1\le r_A-r_A^2.
$$

Writing $g=r_A-r_A^2$, one checks directly that

$$
2g+5g^2<A.
$$

Indeed, with $y=1-r_A$, this reduces to

$$
4y^3(25y^5-100y^4+130y^3-40y^2-36y+22)>0,
$$

and the final polynomial is positive on $0<y<1-\sqrt3/2$.  Hence

$$
\ell(\gamma_5)\le2\gamma_5+5\gamma_5^2\le2G+5G^2<A,
$$

contradiction.  Thus $\ell(\gamma_5)<A=A_1$.

## 3. CE2 overlap with $A_1=A_C$

### Theorem 3.1

Assume the hard region, the left Low branch,

$$
A_5=1-T,
$$

and

$$
A_1=A_C.
$$

Then

$$
\boxed{\ell(\gamma_5)<A_1.}
$$

### Proof

Put $A=A_C$.  Since $A_1=A_C$, $s\le p_1<t$.  Since $A_5=1-T$ is CE2 overlap, $\alpha\ge S$.  Hence

$$
s+S\le p_1+\alpha={1\over D}<1.
$$

Let $W=X+Y+1-\rho$.  Then

$$
{W\over\lambda}+{W\over1-\lambda}<1,
$$

so $W<\lambda(1-\lambda)$ and the first arm of $\gamma_5$ is active:

$$
\gamma_5={X\over1-\lambda}.
$$

Also

$$
\gamma_5< G_1:={A+\rho-1-\lambda^2\over1-\lambda}.
$$

Lemma 1.1 applied to $A_5=1-T$ gives $T\ge\ell(\gamma_5)+\gamma_5$.  If $\ell(\gamma_5)\ge A$, then $\gamma_5\le T-A=X+Y$, and hence

$$
\gamma_5\le {Y\over\lambda}={\lambda-A\over\lambda}=:G_2.
$$

Thus $\gamma_5\le G=\min(G_1,G_2)$.  The comparison $\ell(G)<A$ follows by checking the crossover $G_1=G_2$, where $A=\lambda(2-\lambda+\lambda^2-\rho)$ and $G=\rho(1-\rho)$, and then using convexity of the Low function on $[0,1/8]$ on each side.  Hence $\ell(\gamma_5)<A$, contradiction.  Therefore $\ell(\gamma_5)<A_1$.

## 4. CE2 overlap with $A_1=q$

### Lemma 4.1: $p_1<s$

Assume $A_5=1-T$, $B_5=L$, and $A_1=q$ because $p_1<s$.  Then

$$
\ell(\gamma_5)<q.
$$

### Proof

Lemma 1.1 gives $T\ge\ell(\gamma_5)+\gamma_5$, so $\ell(\gamma_5)\le T-\gamma_5$.  Since $p_1<s$, one has $q=1-p_1>1-s$.  The hard region gives $q\le T$, so $s+T>1$.  The center identity

$$
T-\gamma_5-S={\lambda\over1-\lambda}(1-s-T)
$$

gives $T-\gamma_5<S$.  Hence $\ell(\gamma_5)<S$.  Finally CE2 overlap gives $q>S$, so $\ell(\gamma_5)<q$.

### Lemma 4.2: $p_1\ge t$ and right high sheet

Assume $A_5=1-T$, $B_5=L$, $A_1=q$ because $p_1\ge t$, and $B_1=T_+^{hi}$.  Then

$$
\ell(\gamma_5)<q.
$$

### Proof

Let $u=\gamma_5$, $z=\ell(u)$, and $y=Y/\lambda$.  Lemma 1.1 gives $T\ge z+u$.  Since $T=(1-\lambda)u+\lambda$, we get

$$
\lambda\ge {z\over1-u}.
$$

Write

$$
S=u+{\lambda\over1+\rho}+{\lambda\over1-\lambda}y.
$$

The following center-transfer lemma applies: if $\lambda\ge\ell(u)/(1-u)$ and either $y\ge1-\sqrt3/2$ or $S\le\ell(y)$, then $\ell(u)<S$.  It is proved by reducing to the minimal value $\lambda=\ell(u)/(1-u)$, defining the point $v_0$ where the affine function $S_0(v)$ equals $\ell(u)$, and using concavity of $S_0(v)-\ell(v)$ on $[0,v_0]$.

If $T_0$ hits the exit on $r_1$, then `4074` gives $\ell(\gamma_5)<S<q$.  In the miss case, $C_1=1-\gamma_1$ and $\gamma_1\le y$.  The right high-sheet filter gives

$$
\gamma_1\ge1-\sqrt3/2
\quad\text{or}\quad
q\le\ell(\gamma_1).
$$

Thus either $y\ge1-\sqrt3/2$, or $S<q\le\ell(\gamma_1)\le\ell(y)$.  The transfer lemma gives $\ell(\gamma_5)<S<q$.

## 5. Completion

The branch $(L,\mathrm{Full})$ is proved in `4074`.  The branches with right branch in $\{L,T_-,T_+^{lo}\}$ are covered by `4075`.  The only remaining left-Low branch is right high sheet, and the preceding theorems cover all left input cases.  In those cases $B_5<A_1$, while $B_1\le1-A_1$, so

$$
B_5+B_1<1.
$$

Therefore

$$
\boxed{B_5=L\quad\Longrightarrow\quad B_5+B_1<1.}
$$
