# First-Full and Left-Lower-Sheet Branches in $407X$

Status: Proven

This file closes the hard-region branch families

$$
(\mathrm{Full},*)
$$

and

$$
(T_+^{lo},\mathrm{Full}),\qquad (T_+^{lo},T_+^{hi})
$$

in the $407X$ boundary-loss reduction.

Throughout, use the notation and standing hypotheses of
[`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md), and the support isolation of
[`4072_support_isolation_after_T0_T3_like.md`](4072_support_isolation_after_T0_T3_like.md).

The hard region is

$$
A_1+A_5\le1.
$$

## 1. A $T_0$ support bound

### Lemma 1.1

In the support-isolated $407X$ branch,

$$
\boxed{\alpha<{1\over2}.}
$$

### Proof

Positive $r_1$ support for $T_0$ gives

$$
{Dq\over R}<q+{1-R\over D}.
$$

Multiplying by $DR>0$ gives

$$
D^2q<DRq+R(1-R),
$$

hence

$$
q(D^2-DR)<R(1-R).
$$

Using $R^2-DR+D^2=1$, this is

$$
q(1-R^2)<R(1-R).
$$

The equation $R^2-DR+D^2=1$ and $D>1$ imply $0<R<1$.  Therefore

$$
q(1+R)<R,
$$

so

$$
q<{R\over1+R}<{1\over2}.
$$

Since $q=\alpha+(D-1)/D>\alpha$, one obtains $\alpha<1/2$.

## 2. First Full is impossible

### Lemma 2.1

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

By Lemma 1.1, $\alpha<1/2$, so $\gamma_5\ge\alpha$.  Since $\gamma_5=X/(1-\lambda)$,

$$
X\ge(1-\lambda)\alpha.
$$

Also $A_C\le\alpha$ gives $Y\ge\lambda-\alpha$.  Therefore

$$
s={X+Y+1-\rho\over\lambda}
\ge
1-\alpha+{1-\rho\over\lambda}>1-\alpha.
$$

But $p_1=1/D-\alpha<1-\alpha$.  Hence $s>p_1$, contradicting $s\le p_1$.

### Lemma 2.2

In the CE2 overlap case $A_5=1-T$, one has

$$
B(A_5,C_5)\ne\mathrm{Full}.
$$

### Proof

CE2 overlap gives $\alpha\ge S$.  By Lemma 1.1,

$$
S<{1\over2}.
$$

Assume the left branch is Full.  Put $u=\gamma_5=X/(1-\lambda)$ and $T=X+\lambda$.

If $T\le1/2$, Full gives $u\ge T$.  Then $X/(1-\lambda)\ge X+\lambda$, so $X\ge1-\lambda$, and hence

$$
S\ge {1-\lambda+1-\rho\over1-\lambda}>1,
$$

contradiction.

If $T\ge1/2$, Full gives $u\ge1-T$.  Then

$$
{X\over1-\lambda}\ge1-X-\lambda,
$$

so

$$
X\ge{(1-\lambda)^2\over2-\lambda}.
$$

Writing $a=1-\lambda$, this implies

$$
S\ge {a^2/(1+a)+1-\sqrt{1-a+a^2}\over a}.
$$

This lower bound is $>1/2$ because

$$
\left(1-{a\over2}+{a^2\over1+a}\right)^2-(1-a+a^2)
={a^2(1-a)(3a+5)\over4(1+a)^2}>0.
$$

Again this contradicts $S<1/2$.

### Theorem 2.3

The hard region contains no first-coordinate Full branch:

$$
\boxed{B_5\ne\mathrm{Full}.}
$$

### Proof

The left input is either $A_5=1-\alpha$ or $A_5=1-T$.  Lemmas 2.1 and 2.2 exclude Full in both cases.

## 3. Left lower sheet reductions

### Lemma 3.1

If $B_5=T_+^{lo}$, then $A_5=1-T$ and

$$
\boxed{\lambda\ge {1\over2}.}
$$

### Proof

The case $A_5=1-\alpha$ is impossible because Lemma 1.1 gives $A_5>1/2$, while any $T_+$ branch requires $a\le1/2$.  Thus $A_5=1-T$.

Set $u=\gamma_5$.  Since $T=(1-\lambda)u+\lambda$,

$$
A_5=1-T=(1-\lambda)(1-u).
$$

On the lower sheet,

$$
B_5\ge A_5,
\qquad
B_5\le {1-u\over2}.
$$

Therefore

$$
(1-\lambda)(1-u)\le {1-u\over2}.
$$

Since $u<1/2$, this gives $\lambda\ge1/2$.

### Lemma 3.2

Under $B_5=T_+^{lo}$, the hit case on $r_1$ is impossible.

### Proof

Let $y=Y/\lambda$.  Since $\lambda\ge1/2$,

$$
S=\gamma_5+{\lambda\over1+\rho}+{\lambda\over1-\lambda}y>y.
$$

If $T_0$ hit the $T_C$ exit, the CE2 overlap estimate in `4074` would give

$$
S\le\gamma_1\le y,
$$

contradiction.

### Theorem 3.3: $(T_+^{lo},\mathrm{Full})$ is impossible

Assume $B_5=T_+^{lo}$ and $B_1=\mathrm{Full}$ in the hard region.  By Lemma 3.2, the right side is in the miss case, so $C_1=1-\gamma_1$ and $\gamma_1\le y$.  Also $S>y$.

If $A_1=q$, then $q<1/2$ and the right Full condition gives $\gamma_1\ge q$.  But CE2 overlap gives $q>S$, so $y\ge q>S$, contradicting $S>y$.

If $A_1=A_C$ and $A_C\ge1/2$, Full gives $\gamma_1\ge1-A_C$, hence $y\ge1-A_C$.  Since $A_C=\lambda(1-y)$, this forces $y\ge1$, impossible.

If $A_1=A_C\le1/2$, Full gives $\gamma_1\ge A_C$, hence

$$
y\ge A_C=\lambda(1-y),
$$

so $y\ge\lambda/(1+\lambda)$.  Since $\lambda\ge1/2$,

$$
S\ge {\lambda\over1+\rho}+{\lambda\over1-\lambda}{\lambda\over1+\lambda}>{1\over4}+{1\over3}>{1\over2},
$$

contradicting $S<1/2$.  Thus the branch is impossible.

### Theorem 3.4: $(T_+^{lo},T_+^{hi})$ is impossible

Assume $B_5=T_+^{lo}$ and $B_1=T_+^{hi}$.  Lemma 3.2 again puts the right side in the miss case, so $C_1=1-y$.

The left lower-sheet estimates give

$$
y<{1\over4},
\qquad
S>{7\over16},
\qquad
A_C>{7\over16}.
$$

For the right high sheet with $y<1/4$, the high-sheet input bound gives

$$
A_1\le {7\over16}.
$$

Indeed, writing $p=B_1/(1-y)$, if $p\le5/8$, then $A_1\le\mu/2\le7/16$; if $p\ge5/8$, then $A_1\le\mu-3p/4\le7/16$.

If $A_1=q$, then $q>S>7/16$, contradiction.  If $A_1=A_C$, then $A_C>7/16$, contradiction.  Hence $(T_+^{lo},T_+^{hi})$ is impossible.
