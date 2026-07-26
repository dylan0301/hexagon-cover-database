# Completion of the Left-High-Sheet Branches in $407X$

Status: Proven

This file closes every hard-region branch with first coordinate

$$
B_5=T_+^{hi}.
$$

The canonical expanded derivations for the common left-high Cell-$T$
condition, the high-left envelope estimates, the $S>3y$ and $A_C>3y$
estimates, the detailed right-$T_-$ bounds, and the analytic threshold lemma
are recorded in
[`407c_rigor_completion_details.md`](407c_rigor_completion_details.md). The
present file is the branch-level proof using those lemmas.

The local square root in the historical $\beta$ parameter is the universal
selected-$T_+$ curve proved in
[`2016_universal_Tplus_normal_form.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2016_universal_Tplus_normal_form.md).
The optional rational parameter from that lemma is recorded below, but the
compact symbols $\beta,m$ are retained in the branch proof because the center
radical $\rho$ is independent of this local normalization.

Throughout, use the notation of `4073`. Put

$$
r=1-\lambda,
\qquad
\nu=\gamma_5,
\qquad
y=\frac{Y}{\lambda},
\qquad
\rho=\sqrt{r^2-r+1}.
$$

## 1. Common left-high reductions

### Lemma 1.1

If $B_5=T_+^{hi}$, then $A_5=1-T$. Moreover,

$$
\gamma_5=\frac{X}{1-\lambda},
$$

$$
S=\nu+\frac{1-r}{1+\rho}+\frac{1-r}{r}y,
$$

and

$$
T=r\nu+1-r.
$$

There is a parameter

$$
\beta\in\left[\max\left(r,\frac12,\frac{1-r^2}{1+2r}\right),1\right]
$$

such that, with

$$
m=\sqrt{\beta^2-\beta+1},
$$

one has

$$
1-\nu=\frac{m}{r+\beta},
\qquad
B_5=\frac{\beta m}{r+\beta}.
$$

Equivalently, the universal rational parameter gives a unique

$$
z\in[2-\sqrt3,1/2]
$$

with

$$
\boxed{
\beta=\frac{z(2-z)}{1-z^2},
\qquad
m=\frac{1-z+z^2}{1-z^2}.
}
$$

The realized left-high branch also satisfies

$$
r\ge(1-\beta)(r+\beta)^2.
$$

### Proof

The case $A_5=1-\alpha$ is impossible for a left $T_+$ branch: the $T_0$
support bound gives $\alpha<1/2$, hence $A_5>1/2$, while every selected
$T_+$ branch requires input at most $1/2$. Thus $A_5=1-T$, and the displayed
center identities are the direct formulas from `4073`.

Set

$$
c=1-\nu.
$$

The left input is $a=rc$ and write $B_5=\beta c$. The high sheet gives
$\beta\ge1/2$, while $B_5\ge a$ gives $\beta\ge r$. The selected-$T_+$
normal form `2016`, written with normalized coordinate $x=1-\beta$, gives the
universal local radical

$$
m=\sqrt{1-x+x^2}=\sqrt{\beta^2-\beta+1}.
$$

The exact contact relation is

$$
a+B_5=c(r+\beta)=m,
$$

so

$$
c=\frac{m}{r+\beta}.
$$

The condition $c\le1$ gives

$$
\beta\ge\frac{1-r^2}{1+2r}.
$$

The rational formulas are exactly Section 5 of `2016`. Finally, the Cell-$T$
selector gives

$$
r\ge(1-\beta)(r+\beta)^2
$$

by Lemma 2.1 of `407c`.

### Lemma 1.2

Under $B_5=T_+^{hi}$, the hit case on $r_1$ is impossible. In the miss case,

$$
\gamma_1=y.
$$

### Proof

CE2 overlap gives $\alpha\ge S$, and the $T_0$ support bound gives
$\alpha<1/2$, hence $S<1/2$.

First prove $S>y$. If $r\le1/2$, then the displayed formula for $S$ gives the
claim directly. If $r>1/2$ and $S\le y$, then

$$
S\ge\frac{\nu+\delta}{1-k},
\qquad
\delta=\frac{1-r}{1+\rho},
\qquad
k=\frac{1-r}{r}.
$$

Since

$$
1-\nu=\frac{m}{r+\beta}\le\frac{\rho}{2r}<\frac1{2r},
$$

we have $\nu>(1-k)/2$, and hence $S>1/2$, a contradiction. Thus $S>y$.

If $T_0$ hit the $T_C$ exit, the `4074` hit-overlap lemma would give
$S\le\gamma_1\le y$, a contradiction. Hence the case is miss. Then

$$
\gamma_1=\min\left(y,\frac1r-S\right)=y,
$$

because $S<1/2$ and $S>y$.

### Lemma 1.3

Under $B_5=T_+^{hi}$ in the hard region,

$$
y<\frac1{10}.
$$

### Proof

The inequality $S<1/2$ gives $y<y_*$, and Lemma 2.2 of `407c` proves
$y_*<1/10$.

## 2. The branch $(T_+^{hi},\mathrm{Full})$

### Theorem 2.1

The hard region contains no branch

$$
(T_+^{hi},\mathrm{Full}).
$$

### Proof

By Lemma 1.2, the right side is in the miss case, so $C_1=1-y$ and
$\gamma_1=y$.

If $A_1=q$, then $q<1/2$ and the right Full condition gives $y\ge q$. But
$q>S$ in the CE2 overlap case, while $S>y$, a contradiction.

If $A_1=A_C$ and $A_C\ge1/2$, then Full gives $y\ge1-A_C$, which with
$A_C=(1-r)(1-y)$ forces $y\ge1$, a contradiction.

If $A_1=A_C\le1/2$, then

$$
y\ge A_C=(1-r)(1-y),
\qquad
y\ge\frac{1-r}{2-r}.
$$

We prove $S>1/2$. If $r\le1/2$, then

$$
\frac{1-r}{r}\ge1,
\qquad
y\ge\frac13,
\qquad
\frac{1-r}{1+\rho}\ge2-\sqrt3,
$$

and therefore

$$
S\ge2-\sqrt3+\frac13>\frac12.
$$

If $r\ge1/2$, then

$$
\nu\ge1-\frac{\rho}{2r},
\qquad
\frac{1-r}{1+\rho}=\frac{1-\rho}{r}.
$$

After substituting the lower bound for $y$, the assertion $S>1/2$ is
equivalent, after multiplication by $2r(2-r)>0$, to

$$
r^2-4r+6>3(2-r)\rho.
$$

Both sides are positive, and their squared difference is

$$
r(1-r)(8r^2-29r+24)>0.
$$

The last quadratic is decreasing on $[1/2,1]$ and has value $3$ at $1$.
Thus $S>1/2$ also in this range, contradicting the common bound $S<1/2$.

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

By Lemma 1.2, $\gamma_1=y$, so $B_1=e(y)$. Put

$$
b=B_5=\frac{\beta m}{r+\beta}.
$$

From $S<1/2$ we have $y<y_*$. Lemma 2.2 of `407c` gives

$$
y_*<\frac1{10},
\qquad
3y_*\le1-b.
$$

Since

$$
e(y)\le2y+5y^2<3y<3y_*,
$$

we obtain

$$
B_5+B_1=b+e(y)<b+3y_*\le1.
$$

## 4. The branch $(T_+^{hi},T_+^{hi})$

### Theorem 4.1

The hard region contains no branch

$$
(T_+^{hi},T_+^{hi}).
$$

### Proof

By Lemma 1.2, the right side is in the miss case, so $C_1=1-y$. By
Lemma 1.3,

$$
y<\frac1{10}<1-\frac{\sqrt3}{2}.
$$

For a valid right high-sheet branch with radial input $1-y$, the exact
selected-$T_+$ filter gives

$$
A_1\le e(y).
$$

Lemma 2.3 of `407c` gives

$$
S>3y,
\qquad
A_C>3y.
$$

If $A_1=q$, then $q>S>3y>e(y)$, a contradiction. If $A_1=A_C$, then
$A_C>3y>e(y)$, again a contradiction.

## 5. The branch $(T_+^{hi},T_-)$

### 5.1. The $A_1=A_C$ subcase

If $A_1=A_C$, then $A_1=(1-r)(1-y)$. With $C_1=1-y$, the right $T_-$
equation gives

$$
A_1+B_1=\rho.
$$

Thus

$$
B_1=\rho-(1-r)(1-y).
$$

Using $y<y_*$ and the left high-sheet parameterization,

$$
\begin{aligned}
B_5+B_1
&<\frac{\beta m}{r+\beta}+\rho-(1-r)+(1-r)y_*\\
&=m+2\rho-2+\frac r2.
\end{aligned}
$$

If $r\le8/15$, then $m\le1$ and $2\rho-2+r/2\le0$, so the desired strict
bound follows. Suppose $r>8/15$. The inequality $y_*>0$ gives

$$
\frac{m}{r+\beta}>\frac12+\frac{1-r}{1+\rho}.
$$

Since $\beta\ge r$ and $m/(r+\beta)$ decreases in $\beta$,

$$
\frac{\rho}{2r}>\frac12+\frac{1-r}{1+\rho}.
$$

This simplifies to $3r<1+\rho$. Since $3r-1>0$, squaring gives

$$
r<\frac58.
$$

On this range

$$
\frac{1-r}{1+\rho}\ge\frac15,
$$

because $4-5r\ge\rho$ has nonnegative sides and squared difference

$$
(4-5r)^2-\rho^2=3(8r-5)(r-1)\ge0.
$$

Therefore $m/(r+\beta)>7/10$. If $\beta\ge4/5$, then on
$4/5\le\beta\le1$,

$$
\frac{49}{100}\left(\beta+\frac8{15}\right)^2
-(\beta^2-\beta+1)\ge0.
$$

The left side is a concave quadratic in $\beta$, and its endpoint values are
$7/225$ and $3421/22500$. Hence

$$
m\le\frac7{10}\left(\beta+\frac8{15}\right)
<\frac7{10}(\beta+r),
$$

contradicting $m/(r+\beta)>7/10$. Thus $\beta<4/5$. Since $\beta\ge1/2$,

$$
m^2<\left(\frac45\right)^2-\frac45+1=\frac{21}{25}<\frac{225}{256},
$$

so $m<15/16$. Finally $2\rho+r/2$ is increasing, and at $r=5/8$ it is
$33/16$. Therefore

$$
2\rho-2+\frac r2<\frac1{16}.
$$

It follows that $m+2\rho-2+r/2<1$, and hence $B_5+B_1<1$.

### 5.2. The $A_1=q$ subcase

Let

$$
C=1-y,
\qquad
q=tC,
\qquad
B_1=b_1.
$$

Lemmas 3.1 and 3.2 of `407c` prove

$$
B_1\le\kappa:=\frac{\sqrt{13}-1}{6}
$$

and

$$
q\le\tau<\frac{93}{200},
$$

where $\tau\in(0,1/2)$ is the unique root of

$$
\tau^4-3\tau^3+3\tau^2-3\tau+1=0.
$$

Because $q>S$, we have $S<93/200$. Write

$$
S=S_0+\frac{1-r}{r}y,
\qquad
S_0=1-\frac{m}{r+\beta}+\frac{1-r}{1+\rho}.
$$

Thus $S_0<93/200$. Lemma 4.1 of `407c` proves

$$
S_0<\frac{93}{200}
\quad\Longrightarrow\quad
B_5<\frac{5657}{10000}.
$$

Also

$$
\frac{5657}{10000}<\frac{7-\sqrt{13}}6=1-\kappa.
$$

Therefore

$$
B_5+B_1<1.
$$

## 6. Conclusion for left-high branches

Combining Theorems 2.1, 3.1, 4.1 and the two parts of Section 5 gives

$$
\boxed{
B_5=T_+^{hi}
\quad\Longrightarrow\quad
B_5+B_1<1.
}
$$

This holds for every realized right branch in the hard support-isolated
`407X` domain.