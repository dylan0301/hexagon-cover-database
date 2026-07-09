# Completion of the Left-High-Sheet Branches in $407X$

Status: Proven

This file closes every hard-region branch with first coordinate

$$
B_5=T_+^{hi}.
$$

It uses two finite rational interval certificates in

- [`407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py`](407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py),
- [`407X_computation/407c_T_hi_Tlo_left_threshold_certificate.py`](407X_computation/407c_T_hi_Tlo_left_threshold_certificate.py).

The expanded derivations for the common left-high Cell-2 condition, the high-left envelope estimates, the $S>3y$ and $A_C>3y$ estimates, and the detailed right-$T_-$ bounds are recorded in [`407c_detailed_gap_closure.md`](407c_detailed_gap_closure.md).  The present file is the branch-level proof using those lemmas.

Throughout, use the notation of `4073`.  Put

$$
r=1-\lambda,
\qquad
u=\gamma_5,
\qquad
y={Y\over\lambda},
\qquad
\rho=\sqrt{r^2-r+1}.
$$

## 1. Common left-high reductions

### Lemma 1.1

If $B_5=T_+^{hi}$, then $A_5=1-T$.  Moreover,

$$
\gamma_5={X\over1-\lambda},
$$

$$
S=u+{1-r\over1+\rho}+{1-r\over r}y,
$$

and

$$
T=ru+1-r.
$$

There is a parameter

$$
\beta\in\left[\max\left(r,{1\over2},{1-r^2\over1+2r}\right),1\right]
$$

such that

$$
m=\sqrt{\beta^2-\beta+1},
$$

$$
1-u={m\over r+\beta},
$$

and

$$
B_5={\beta m\over r+\beta}.
$$

The realized left-high branch also satisfies

$$
r\ge(1-\beta)(r+\beta)^2.
$$

### Proof

The case $A_5=1-\alpha$ is impossible for a left $T_+$ branch because the $T_0$ support bound gives $\alpha<1/2$, hence $A_5>1/2$, while every $T_+$ branch requires $a\le1/2$.

Thus $A_5=1-T$.  The center identities are the direct formulas from `4073`.  Setting $c=1-u$, the left input is $a=rc$ and $C_5=c$.  With $\beta=B_5/c$, the high sheet gives $\beta\ge1/2$, and $B_5\ge a$ gives $\beta\ge r$.  The $T_+$ equation gives

$$
\beta^2-\beta+1=(a+B_5)^2=c^2(r+\beta)^2,
$$

so $c=m/(r+\beta)$.  The condition $c\le1$ gives $\beta\ge(1-r^2)/(1+2r)$.  The Cell-2 condition gives $r\ge(1-\beta)(r+\beta)^2$ as proved in `407c`, Lemma 3.1.

### Lemma 1.2

Under $B_5=T_+^{hi}$, the hit case on $r_1$ is impossible.  In the miss case,

$$
\gamma_1=y.
$$

### Proof

CE2 overlap gives $\alpha\ge S$, and the $T_0$ support bound gives $\alpha<1/2$, hence $S<1/2$.

First prove $S>y$.  If $r\le1/2$, then

$$
S=u+{1-r\over1+\rho}+{1-r\over r}y>y.
$$

If $r>1/2$ and $S\le y$, then

$$
S\ge {u+\delta\over1-k},
\qquad
\delta={1-r\over1+\rho},
\quad
k={1-r\over r}.
$$

Since

$$
1-u={m\over r+\beta}\le {\rho\over2r}< {1\over2r},
$$

we have $u>(1-k)/2$, and hence $S>1/2$, contradiction.  Thus $S>y$.

If $T_0$ hit the $T_C$ exit, the `4074` hit-overlap lemma would give $S\le\gamma_1\le y$, contradiction.  Hence the case is miss.  Then

$$
\gamma_1=\min\left(y,{1\over r}-S\right)=y,
$$

because $S<1/2$ and $S>y$.

### Lemma 1.3

Under $B_5=T_+^{hi}$ in the hard region,

$$
y<{1\over10}.
$$

### Proof

This is Lemma 3.2 of `407c` in the stronger form $y_*<1/10$, applied to the inequality $y<y_*$ coming from $S<1/2$.

## 2. The branch $(T_+^{hi},\mathrm{Full})$

### Theorem 2.1

The hard region contains no branch

$$
(T_+^{hi},\mathrm{Full}).
$$

### Proof

By Lemma 1.2, the right side is in the miss case, so $C_1=1-y$ and $\gamma_1=y$.

If $A_1=q$, then $q<1/2$ and the right Full condition gives $y\ge q$.  But $q>S$ in the CE2 overlap case, while $S>y$, contradiction.

If $A_1=A_C$ and $A_C\ge1/2$, then Full gives $y\ge1-A_C$, which with $A_C=(1-r)(1-y)$ forces $y\ge1$, contradiction.

If $A_1=A_C\le1/2$, then Full gives $y\ge A_C=(1-r)(1-y)$, hence $y\ge(1-r)/(2-r)$.  A direct estimate using the left high-sheet lower bound gives $S>1/2$, contradicting $S<1/2$.  Thus the branch is impossible.

## 3. The branch $(T_+^{hi},L)$

### Theorem 3.1

If

$$
(B_5,B_1)=(T_+^{hi},L),
$$

then

$$
B_5+B_1<1.
$$

### Proof

By Lemma 1.2, $\gamma_1=y$.  Thus $B_1=\ell(y)$.

Let

$$
b=B_5={\beta m\over r+\beta}.
$$

From $S<1/2$ we have $y<y_*$.  Lemma 3.2 of `407c` gives

$$
y_*<{1\over8},
\qquad
3y_*\le1-b.
$$

Since

$$
\ell(y)\le2y+5y^2<3y<3y_*,
$$

we get

$$
B_5+B_1=b+\ell(y)<b+3y_*\le1.
$$

## 4. The branch $(T_+^{hi},T_+^{hi})$

### Theorem 4.1

The hard region contains no branch

$$
(T_+^{hi},T_+^{hi}).
$$

### Proof

By Lemma 1.2, the right side is in the miss case, so $C_1=1-y$.  By Lemma 1.3, $y<1/10<1-\sqrt3/2$.

For a valid right high-sheet branch with radial input $1-y$ in this range, the high-sheet input filter gives

$$
A_1\le\ell(y).
$$

Lemma 3.3 of `407c` gives

$$
S>3y,
\qquad
A_C>3y.
$$

If $A_1=q$, then $q>S>3y>\ell(y)$, contradiction.  If $A_1=A_C$, then $A_C>3y>\ell(y)$, contradiction.  Hence the double high-sheet branch is impossible.

## 5. The branch $(T_+^{hi},T_-)$

### 5.1. The $A_1=A_C$ subcase

If $A_1=A_C$, then $A_1=(1-r)(1-y)$.  With $C_1=1-y$, the right $T_-$ equation gives

$$
A_1+B_1=\rho.
$$

Thus

$$
B_1=\rho-(1-r)(1-y).
$$

Using $y<y_*$ and the left high-sheet parameterization,

$$
B_5+B_1
<
{\beta m\over r+\beta}+\rho-(1-r)+(1-r)y_*
=
m+2\rho-2+{r\over2}.
$$

If $r\le8/15$, then $m\le1$ and $2\rho-2+r/2\le0$.  If $r>8/15$, Lemma 3.4 of `407c` supplies the estimates $r<5/8$ and $\beta<4/5$, hence $m<15/16$; also $2\rho-2+r/2<1/16$.  Therefore $B_5+B_1<1$.

### 5.2. The $A_1=q$ subcase

Let

$$
C=1-y,
\qquad
q=tC,
\qquad
B_1=b_1.
$$

Lemma 3.4 of `407c` proves

$$
B_1\le\kappa:={\sqrt{13}-1\over6}
$$

and

$$
q\le\tau<{93\over200},
$$

where $\tau\in(0,1/2)$ is the unique root of

$$
\tau^4-3\tau^3+3\tau^2-3\tau+1=0.
$$

Because $q>S$, we have $S<93/200$.  Write

$$
S=S_0+{1-r\over r}y,
\qquad
S_0=1-{m\over r+\beta}+{1-r\over1+\rho}.
$$

Thus $S_0<93/200$.  The finite certificate
[`407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py`](407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py) proves

$$
S_0<{93\over200}
\quad\Longrightarrow\quad
B_5<{5657\over10000}.
$$

Also

$$
{5657\over10000}< {7-\sqrt{13}\over6}=1-\kappa.
$$

Therefore

$$
B_5+B_1<1.
$$

## 6. The branch $(T_+^{hi},T_+^{lo})$

### Lemma 6.1

For the right lower sheet in the miss case, put

$$
C=1-y,
\qquad
p={B_1\over C}.
$$

Then

$$
0<p\le {1\over2},
$$

$$
B_1=Cp,
$$

and with

$$
\mu=\sqrt{p^2-p+1},
$$

one has

$$
A_1=\mu-Cp.
$$

Moreover the branch condition $B_1\ge A_1$ implies

$$
3p^2+p-1\ge0.
$$

### Proof

The lower sheet gives $0<p\le1/2$.  The equation $p^2-p+1=(A_1+B_1)^2$ gives $A_1=\mu-Cp$.  The condition $B_1\ge A_1$ gives $2Cp\ge\mu$.  Since $C\le1$, this implies $2p\ge\mu$, hence $3p^2+p-1\ge0$.

### Lemma 6.2: certified lower-sheet threshold

Under the realized left high-sheet conditions and the parameter condition

$$
3p^2+p-1\ge0,
$$

if

$$
S_0<\sqrt{p^2-p+1}-p,
$$

then

$$
B_5<1-p.
$$

### Proof

This is exactly the finite rational interval certificate in

[`407X_computation/407c_T_hi_Tlo_left_threshold_certificate.py`](407X_computation/407c_T_hi_Tlo_left_threshold_certificate.py).

The verifier proves the implication over

$$
0\le r\le1,
\qquad
{1\over2}\le\beta\le1,
\qquad
0\le p\le {1\over2}.
$$

It uses the left high-sheet necessary conditions

$$
\beta\ge r,
\qquad
\beta\ge {1-r^2\over1+2r},
\qquad
r\ge(1-\beta)(r+\beta)^2,
$$

and the lower-sheet condition $3p^2+p-1\ge0$.  It certifies every rational box by one of: domain beta exclusion, domain Cell-2 exclusion, $p$-domain exclusion, direct $B_5<1-p$ upper bound, or threshold exclusion $S_0\ge\sqrt{p^2-p+1}-p$.  The recorded run has $1459$ terminal boxes and no unresolved boxes.

### Theorem 6.3

If

$$
(B_5,B_1)=(T_+^{hi},T_+^{lo}),
$$

then

$$
B_5+B_1<1.
$$

### Proof

By Lemma 6.1, write $B_1=Cp$ and $A_1=\mu-Cp$.

If $A_1=A_C$, then $\mu-Cp=(1-r)C$.  The branch condition $B_1\ge A_1$ gives $p\ge1-r$.  Since $p\le1/2$, $r\ge1/2$.  The high-left half-bound gives $B_5<1/2$, while $B_1\le p\le1/2$, so $B_5+B_1<1$.

If $A_1=q$, then $q>S$.  Since $q=\mu-(1-y)p=\mu-p+py$ and $S=S_0+((1-r)/r)y$, we have

$$
S_0<\mu-p+\left(p-{1-r\over r}\right)y.
$$

If $(1-r)/r<p$, then $r>1/(1+p)\ge2/3$, so $B_5<1/2$ and $B_1\le1/2$.

If $(1-r)/r\ge p$, then $S_0<\mu-p$.  Lemma 6.2 gives $B_5<1-p$.  Since $B_1=Cp\le p$, we get $B_5+B_1<1$.

## 7. Conclusion for left-high branches

Combining Theorems 2.1, 3.1, 4.1, the two parts of Section 5, and Theorem 6.3 gives

$$
\boxed{B_5=T_+^{hi}\quad\Longrightarrow\quad B_5+B_1<1}
$$

for every realized right branch in the hard support-isolated $407X$ domain.
