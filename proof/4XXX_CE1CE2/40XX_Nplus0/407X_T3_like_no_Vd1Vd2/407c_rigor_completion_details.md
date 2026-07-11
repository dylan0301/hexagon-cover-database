# Rigor Completion Details for the $407X$ Branch Package

Status: Proven

This file supplies detailed proofs for the analytic estimates and certificate
hypotheses used by

- [`4078_left_L_family_completion.md`](4078_left_L_family_completion.md),
- [`4079_first_Full_and_lower_sheet_branches.md`](4079_first_Full_and_lower_sheet_branches.md), and
- [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md).

It is intended as a local dependency for those files.  The computational
certificates remain in `407X_computation/`.

Throughout, use the notation of `4073`.  For high-sheet and lower-sheet
calculations put

$$
r=1-\lambda,\qquad u=\gamma_5,\qquad y={Y\over\lambda},\qquad
\rho=\sqrt{r^2-r+1}.
$$

## 1. Details for the Low branch arguments in `4078`

### Lemma 1.1: nonnegativity in the Low separation lemma

In the Low branch separation lemma of `4078`, the quantity

$$
h=\beta-z
$$

satisfies $h\ge0$.

#### Proof

The Low branch is realized for input $a=1-\beta$ and output $z=\ell(\eta)$.  Its domain includes

$$
a+z\le1.
$$

Substituting $a=1-\beta$ gives

$$
1-\beta+z\le1,
$$

hence $z\le\beta$ and $h=\beta-z\ge0$.

### Lemma 1.2: the polynomial used in the non-overlap Low comparison

For

$$
0<y<1-{\sqrt3\over2},
$$

the polynomial

$$
Q(y)=25y^5-100y^4+130y^3-40y^2-36y+22
$$

is positive.

#### Proof

Since $1-\sqrt3/2<1/7$, it is enough to prove positivity for $0<y<1/7$.  On this interval,

$$
Q(y)>22-36y-40y^2-100y^4.
$$

Thus

$$
Q(y)>22-{36\over7}-{40\over49}-{100\over2401}={38414\over2401}>0.
$$

This proves the claim.

### Lemma 1.3: the CE2-overlap middle comparison

Let $0<A\le\lambda<1$ and

$$
\rho=\sqrt{1-\lambda+\lambda^2}.
$$

Define

$$
G_1={A+\rho-1-\lambda^2\over1-\lambda},\qquad
G_2={\lambda-A\over\lambda},\qquad G=\min(G_1,G_2).
$$

If $G\ge0$, then

$$
\boxed{\ell(G)<A.}
$$

#### Proof

The equality $G_1=G_2$ is equivalent to

$$
A=A_0:=\lambda(2-\lambda+\lambda^2-\rho).
$$

At this value,

$$
G_1=G_2=g:=\rho(1-\rho),
$$

and

$$
A_0=\lambda(1-g).
$$

First prove $\ell(g)<A_0$.  Put $c=1-g$ and $b_0=A_0=\lambda c$.  The Low polynomial in $b$ is

$$
F_c(b)=b^2-cb+c^2(1-c^2).
$$

Using $\rho^2=1-\lambda+\lambda^2$, direct reduction gives

$$
F_c(b_0)=-(\rho-1)^2(\rho^2+1)(\rho^2-\rho+1)^2<0.
$$

Since $F_c(0)=c^2(1-c^2)>0$ and $\ell(g)$ is the smaller positive root of $F_c$, this implies

$$
\ell(g)<b_0=A_0.
$$

If $G=G_2$, then $A\ge A_0$, and $G_2=(\lambda-A)/\lambda\le g$.  Since $\ell$ is increasing on the Low range,

$$
\ell(G)\le\ell(g)<A_0\le A.
$$

If $G=G_1$, then $A\le A_0$.  On the interval where $G_1\ge0$, let

$$
F(A)=A-\ell(G_1(A)).
$$

The lower endpoint is $A_L=1+\lambda^2-\rho$, where $G_1=0$ and $F(A_L)=A_L>0$.  At the upper endpoint $A_0$,

$$
F(A_0)=A_0-\ell(g)>0.
$$

Moreover $0\le G_1\le g<1/8$, and $\ell$ is convex on $[0,1/8]$.  Since $G_1$ is affine in $A$, the function $A\mapsto\ell(G_1(A))$ is convex, so $F$ is concave.  A concave function lies above the chord joining its endpoint values.  Hence $F(A)>0$ throughout the interval, proving $\ell(G_1(A))<A$.

Thus $\ell(G)<A$ in all cases.

### Lemma 1.4: the center-transfer lemma used in `4078`

Let $0<u\le1-\sqrt3/2$ and $z=\ell(u)$.  Suppose $0<\lambda<1$ and

$$
\lambda\ge {z\over1-u}.
$$

Set

$$
\rho=\sqrt{1-\lambda+\lambda^2},\qquad
S_\lambda(v)=u+{\lambda\over1+\rho}+{\lambda\over1-\lambda}v.
$$

If either $v\ge1-\sqrt3/2$, or $0\le v\le1-\sqrt3/2$ and

$$
S_\lambda(v)\le\ell(v),
$$

then

$$
\boxed{z<S_\lambda(v).}
$$

#### Proof

Put

$$
c=1-u,\qquad \beta={z\over c}.
$$

Since $z=\ell(u)$,

$$
\beta={1-\sqrt{4c^2-3}\over2}
$$

and

$$
c^2=1-\beta+\beta^2.
$$

The hypothesis is $\lambda\ge\beta$.  The functions

$$
\lambda\mapsto {\lambda\over1+\sqrt{1-\lambda+\lambda^2}}
$$

and

$$
\lambda\mapsto {\lambda\over1-\lambda}
$$

are increasing on $(0,1)$.  Hence

$$
S_\lambda(v)\ge S_\beta(v).
$$

At $\lambda=\beta$, the corresponding value of $\rho$ is $c$.  Thus

$$
S_\beta(v)=u+{\beta\over1+c}+{\beta\over1-\beta}v.
$$

If $S_\beta(0)\ge z$, then $S_\lambda(v)\ge z$.  Strictness is automatic in the two alternatives of the lemma: if $v>0$, then $S_\beta(v)>S_\beta(0)$, and if $v=0$ the alternative $S_\lambda(0)\le\ell(0)=0$ is impossible because $S_\lambda(0)>0$.

It remains to treat the case $S_\beta(0)<z$.  Let $v_0$ be defined by

$$
S_\beta(v_0)=z.
$$

Then

$$
v_0={ (1-\beta)(\beta^2+c-1)\over1+c}>0.
$$

Also

$$
u-v_0={ (1-\beta)(1+\beta-\beta^2-c)\over1+c}.
$$

The numerator is positive because

$$
(1+\beta-\beta^2)^2-c^2=\beta(\beta-1)(\beta^2-\beta-3)>0
$$

for $0<\beta\le1/2$.  Hence $0<v_0<u$.  Furthermore,

$$
v_0<(1-\beta)\beta^2\le {1\over8}.
$$

On $[0,v_0]$ the Low function is convex, so

$$
H(v)=S_\beta(v)-\ell(v)
$$

is concave.  We have $H(0)>0$, and

$$
H(v_0)=z-\ell(v_0)>0
$$

because $v_0<u$ and $\ell$ is increasing.  Hence $H(v)>0$ for $0\le v\le v_0$.

If $v\ge1-\sqrt3/2$, then $v>v_0$, so

$$
S_\lambda(v)\ge S_\beta(v)>z.
$$

If instead $0\le v\le1-\sqrt3/2$ and $S_\lambda(v)\le\ell(v)$, suppose for contradiction that $S_\lambda(v)\le z$.  Then $S_\beta(v)\le z$, so $v\le v_0$.  But then

$$
S_\lambda(v)\ge S_\beta(v)>\ell(v),
$$

contradicting $S_\lambda(v)\le\ell(v)$.  Therefore $S_\lambda(v)>z$.

This proves the lemma.

## 2. Details for the left-lower-sheet arguments in `4079`

### Lemma 2.1: midpoint exit bound

In the normalized $407X$ configuration,

$$
\gamma_5<{1\over2}.
$$

#### Proof

The center triangle $T_C$ contains exactly $M_0$ among the radial midpoints.  Since $T_C\cap r_5$ is the closed interval from the center to the exit parameter $\gamma_5$, the condition $M_5\notin T_C$ gives $\gamma_5<1/2$.

### Lemma 2.2: left lower-sheet estimates

Assume $B_5=T_+^{lo}$ in the hard CE2 overlap region.  Let

$$
y={Y\over\lambda},\qquad r=1-\lambda,\qquad \rho=\sqrt{r^2-r+1}.
$$

Then

$$
y<{1\over4}.
$$

Moreover, if $0\le y<1-\sqrt3/2$, then

$$
S>\ell(y),
$$

and if $y\ge1-\sqrt3/2$, then

$$
S>{7\over16},\qquad A_C>{7\over16}.
$$

#### Proof

The lower sheet gives $A_5=1-T$ and $\lambda\ge1/2$.  Thus $0<r\le1/2$.  Write

$$
S=u+\delta+ky,\qquad \delta={1-r\over1+\rho},\qquad k={1-r\over r}.
$$

Since $k\ge1$ and $\delta\ge2-\sqrt3$, the hard-region inequality $S<1/2$ implies

$$
y<{1\over2}-(2-\sqrt3)=\sqrt3-{3\over2}<{1\over4}.
$$

For the lower-sheet parameterization, set $c=1-u$ and $B_5=c\beta$ with

$$
r\le\beta\le{1\over2},\qquad c={\sqrt{\beta^2-\beta+1}\over r+\beta}.
$$

The existence of such a point implies $r\ge r_0=(\sqrt3-1)/2$.

We next prove

$$
u+\delta+k\left(1-{\sqrt3\over2}\right)>{7\over16}.
$$

If $r\le7/16$, then $\delta>9/32$ and $k\ge9/7$, hence

$$
u+\delta+k\left(1-{\sqrt3\over2}\right)>{9\over32}+{9\over7}\left(1-{\sqrt3\over2}\right)>{7\over16}.
$$

If $7/16\le r\le9/20$, then $\delta>22/75$ and $k\ge11/9$, while $1-\sqrt3/2>1/8$, giving

$$
u+\delta+k\left(1-{\sqrt3\over2}\right)>{22\over75}+{11\over72}>{7\over16}.
$$

If $9/20\le r\le1/2$, then

$$
1-u\le{\rho\over2r}\le{\sqrt{301}\over18},
$$

so

$$
u+\delta+k\left(1-{\sqrt3\over2}\right)
\ge
4-{3\sqrt3\over2}-{\sqrt{301}\over18}>{7\over16}.
$$

The last inequality follows, for example, from $\sqrt{301}<347/20$ and $\sqrt3<97/56$.

Now suppose $0\le y<1-\sqrt3/2$.  Define

$$
D(x)=u+\delta+kx-\ell(x).
$$

The function $\ell$ is convex on $[0,1-\sqrt3/2]$, hence $D$ is concave.  We have $D(0)>0$.  At $x=1-\sqrt3/2$ the preceding estimate gives

$$
D(x)>{7\over16}-{\sqrt3\over4}>0.
$$

If the interval is truncated earlier by $S=1/2$, then at that endpoint $D=1/2-\ell(x)>0$.  Therefore by concavity $D(y)>0$, i.e. $S>\ell(y)$.

It remains to prove $A_C>7/16$ when $y\ge1-\sqrt3/2$.  From $S<1/2$,

$$
y<{1/2-u-\delta\over k}.
$$

Therefore

$$
A_C=(1-r)(1-y)>1-{3r\over2}+ru+r\delta.
$$

If $r\le7/16$, then $1-3r/2\ge11/32$ and $r\delta\ge9(\sqrt3-1)/64$, so $A_C>7/16$.

If $r\ge7/16$, then $u\ge1-\rho/(2r)$ and $\delta\ge(1-r)/2$, hence

$$
A_C>1-{r\over2}+{r(1-r)\over2}-{\rho\over2}.
$$

On $[7/16,1/2]$, this is at least

$$
{3\over4}+{63\over512}- {\sqrt{193}\over32}>{7\over16},
$$

because $223>16\sqrt{193}$.  This proves the lemma.

## 3. Details for the left-high-sheet arguments in `407a`

### Lemma 3.1: realized left high-sheet Cell 2 condition

In the left high-sheet parameterization

$$
A_5=rc,\qquad B_5=\beta c,\qquad c={m\over r+\beta},\qquad m^2=\beta^2-\beta+1,
$$

every realized $T_+^{hi}$ branch satisfies

$$
\boxed{r\ge(1-\beta)(r+\beta)^2.}
$$

#### Proof

The realized $T_+$ branch lies in Cell 2, so

$$
\Delta=(A_5+B_5)^4-(A_5+B_5)^2+A_5B_5\ge0.
$$

Now $A_5+B_5=m$ and $A_5B_5=r\beta c^2$.  Thus

$$
\Delta=m^4-m^2+r\beta c^2
=m^2\left(m^2-1+{r\beta\over(r+\beta)^2}\right).
$$

Since $m^2-1=\beta^2-\beta=-\beta(1-\beta)$ and $m^2>0$, the inequality $\Delta\ge0$ is equivalent to

$$
{r\beta\over(r+\beta)^2}\ge \beta(1-\beta).
$$

Dividing by $\beta>0$ gives

$$
r\ge(1-\beta)(r+\beta)^2.
$$

### Lemma 3.2: high-left envelope

For the left high-sheet parameterization, define

$$
y_*={r\over1-r}\left({m\over r+\beta}-{1\over2}-{1-r\over1+\rho}\right),\qquad b={\beta m\over r+\beta}.
$$

If $S<1/2$, then $y<y_*$.  Moreover

$$
\boxed{y_*<{1\over8}},\qquad
\boxed{3y_*\le1-b.}
$$

#### Proof

The inequality $S<1/2$ gives $y<y_*$ directly.

First prove $y_*<1/8$.  The function $m/(r+\beta)$ is decreasing in $\beta$, so $y_*$ is maximized at

$$
\beta_0(r)=\max\left(r,{1\over2},{1-r^2\over1+2r}\right).
$$

Let $r_0=(\sqrt3-1)/2$.

If $0<r\le r_0$, then $m/(r+\beta)\le1$ and $(1-r)/(1+\rho)>(1-r)/2$, hence

$$
y_*<{r^2\over2(1-r)}\le {r_0^2\over2(1-r_0)}<{1\over8}.
$$

If $r_0\le r\le1/2$, then

$$
{m\over r+\beta}\le{\sqrt3\over1+2r},\qquad {1-r\over1+\rho}>{1-r\over2}.
$$

It remains to check

$$
{r\over1-r}\left({\sqrt3\over1+2r}-1+{r\over2}\right)<{1\over8}.
$$

This is equivalent to

$$
8r^3-10r^2+(8\sqrt3-9)r-1<0.
$$

The derivative is positive on the interval, and at $r=1/2$ the value is $4\sqrt3-7<0$.

If $1/2\le r<1$, then $m/(r+\beta)\le\rho/(2r)$.  Hence

$$
y_*\le {\rho+1-3r\over2(\rho+1)}<{1\over8},
$$

because the latter inequality is equivalent to $\rho+1<4r$, which follows from $\rho<1$ and $r\ge1/2$.

Now prove $3y_*\le1-b$.  Let

$$
E_r(\beta)=1-b-3y_*.
$$

A direct differentiation gives

$$
{\partial E_r\over\partial\beta}={N_r(\beta)\over2(\beta+r)^2(1-r)\sqrt{\beta^2-\beta+1}},
$$

where

$$
N_r(\beta)=2\beta^3r-2\beta^3+4\beta^2r^2-5\beta^2r+\beta^2-9\beta r^2+5r^2+4r.
$$

Also

$$
{\partial N_r\over\partial\beta}=-6\beta^2(1-r)+2\beta(1-r)(1-4r)-9r^2<0
$$

on the allowed domain $\beta\ge1/2$.  Hence $E_r$ has no interior minimum and it suffices to check endpoints.

At $\beta=1$,

$$
E_r(1)={r(6r-\rho+5)\over2(1+r)(1+\rho)}>0.
$$

At the lower endpoint there are three cases.  If $0<r\le r_0$, then $\beta_0=(1-r^2)/(1+2r)$ and

$$
E_r(\beta_0)=
{r(7+\rho-2r-8r\rho-14r^2-2r^2\rho)\over2(1-r)(1+2r)(1+\rho)}>0,
$$

because the numerator is at least $r(7-10r-16r^2)>0$ for $r<3/8$.

If $r_0\le r\le1/2$, then $\beta_0=1/2$, so $b\le1/2$ and $y_*<1/8$, hence

$$
E_r(\beta_0)>1-{1\over2}-{3\over8}>0.
$$

If $1/2\le r<1$, then $\beta_0=r$ and

$$
E_r(r)={10r-r^2-2\rho-2\over2(1+\rho)}>0,
$$

because $10r-r^2-2\rho-2\ge10r-r^2-4>0$ on $[1/2,1]$.

Thus $E_r(\beta)\ge0$ throughout, proving $3y_*\le1-b$.

### Lemma 3.3: the estimates $S>3y$ and $A_C>3y$

Under $B_5=T_+^{hi}$ in the hard region,

$$
\boxed{S>3y},\qquad \boxed{A_C>3y}.
$$

#### Proof

Since $y<y_*<1/10$, we have $3y<3/10$.

Write $S=u+\delta+ky$ with $k=(1-r)/r$.  If $k\ge3$, then $S>3y$.  If $k<3$, the function $S-3y$ decreases in $y$, and at the endpoint $y=y_*$ one has $S=1/2$.  Thus

$$
S-3y>{1\over2}-3y_*>{1\over2}-{3\over10}>0.
$$

For $A_C$, first prove $1-r>3/8$.  If $r\le1/2$ this is immediate.  If $r>1/2$, the feasibility condition $y_*>0$ gives

$$
{\rho\over2r}>{1\over2}+{1-r\over1+\rho}.
$$

This is equivalent to $3r<1+\rho$.  Since $r>1/2$, squaring $3r-1<\rho$ gives $8r^2-5r<0$, so $r<5/8$.  Hence $1-r>3/8$ in all cases.

Therefore

$$
A_C=(1-r)(1-y)>{3\over8}\cdot{9\over10}={27\over80}>{3\over10}>3y.
$$

## 4. Details for the right $T_-$ estimates in `407a`

Let $C=1-y$, $q=tC$, and $B_1=b_1$.  In the right $T_-$ branch,

$$
q+b_1=\mu=\sqrt{t^2-t+1}.
$$

The branch condition $b_1\le q$ gives $b_1\le\mu/2$ and $\mu\le2t$.

### Lemma 4.1

In the branch $B_1=T_-$ with $A_1=q$,

$$
B_1\le\kappa:={\sqrt{13}-1\over6}.
$$

#### Proof

From $\mu\le2t$,

$$
t^2-t+1\le4t^2,
$$

so $3t^2+t-1\ge0$ and $t\ge\kappa$.  Since $y<1/10$ and $q<1/2$, one has $t=q/(1-y)<5/9$.  On $[\kappa,5/9]$,

$$
{1\over2}\sqrt{t^2-t+1}\le\kappa.
$$

Therefore

$$
B_1\le {\mu\over2}\le\kappa.
$$

### Lemma 4.2

In the branch $B_1=T_-$ with $A_1=q$,

$$
q\le\tau<{93\over200},
$$

where $\tau$ is the unique root in $(0,1/2)$ of

$$
x^4-3x^3+3x^2-3x+1=0.
$$

#### Proof

The realized $T_-$ Cell 2 condition is

$$
(q+b_1)^4-(q+b_1)^2+qb_1\ge0.
$$

Using $q+b_1=\mu$ and $q=tC$, this becomes

$$
-tC^2+\mu C-(1-t)\mu^2\ge0.
$$

Since $C>9/10$, this inequality first forces $t<1/2$: if $t\ge1/2$, the upper root is $C=\mu<9/10$, contradiction.

For $t<1/2$, the larger root is $\mu(1-t)/t$, so

$$
C\le{\mu(1-t)\over t}.
$$

Thus

$$
q=tC\le\mu(1-t),
$$

and also $q=tC\le t$.  Therefore

$$
q\le\min\{t,\mu(1-t)\}.
$$

The first function is increasing and the second is decreasing on $(0,1/2)$.  The maximum of the minimum occurs when

$$
t=\mu(1-t),
$$

which is equivalent to

$$
t^4-3t^3+3t^2-3t+1=0.
$$

This polynomial is strictly decreasing on $(0,1/2)$, so it has a unique root $\tau$ there.  Direct evaluation gives

$$
P\left({93\over200}\right)<0,
$$

so $\tau<93/200$.

## 5. Certificate applicability

The certificate `407b_T_hi_Tminus_qright_threshold_certificate.py` assumes the left high-sheet necessary conditions

$$
\beta\ge r,\qquad
\beta\ge {1-r^2\over1+2r},\qquad
r\ge(1-\beta)(r+\beta)^2.
$$

These are proved above in Lemma 3.1 and the common left-high parameterization.  Hence it applies to every realized left high-sheet branch.

The certificate `407c_T_hi_Tlo_left_threshold_certificate.py` assumes the same left high-sheet conditions and the right lower-sheet necessary condition

$$
3p^2+p-1\ge0.
$$

The latter follows from $B_1\ge A_1$ as shown in `407a`, Lemma 6.1.  Therefore this certificate also applies to every realized branch in its stated case.
