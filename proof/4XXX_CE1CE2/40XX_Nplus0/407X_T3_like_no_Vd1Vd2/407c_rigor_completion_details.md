# Rigor Completion Details for the $407X$ Branch Package

Status: Proven

This file supplies detailed proofs for the analytic estimates used by

- [`4078_left_L_family_completion.md`](4078_left_L_family_completion.md),
- [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md).

It is intended as a local dependency for those files. The computational check
remains in `407X_computation/`, but the threshold implication formerly
supplied by that check is proved analytically in Lemma 4.1 below.

Throughout, use the notation of `4073`.  For high-sheet calculations put

$$
r=1-\lambda,\qquad u=\gamma_5,\qquad y=\frac{Y}{\lambda},\qquad
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

The Low branch is realized for input $a=1-\beta$ and output $z=e(\eta)$.  Its domain includes

$$
a+z\le1.
$$

Substituting $a=1-\beta$ gives

$$
1-\beta+z\le1,
$$

hence $z\le\beta$ and $h=\beta-z\ge0$.

### Lemma 1.2: the non-overlap Low comparison

For $0<A<1/2$, put

$$
r_A=\sqrt{1-A+A^2},
\qquad
g=r_A(1-r_A).
$$

Then

$$
2g+5g^2<A.
$$

#### Proof

Write $r_A=1-y$.  Then $0<y<1-\sqrt3/2<1/7$ and

$$
A=\frac{1-\sqrt{1-8y+4y^2}}{2}.
$$

The desired inequality is equivalent to

$$
\sqrt{1-8y+4y^2}<1-4y-6y^2+20y^3-10y^4.
$$

The right side is positive because

$$
1-4y-6y^2-10y^4
>1-\frac{4}{7}-\frac{6}{49}-\frac{10}{2401}>0.
$$

After squaring, the difference of the right square and the left square is
$4y^3Q(y)$, where

$$
Q(y)=25y^5-100y^4+130y^3-40y^2-36y+22.
$$

On $0<y<1/7$,

$$
Q(y)>22-36y-40y^2-100y^4.
$$

Thus

$$
Q(y)>22-\frac{36}{7}-\frac{40}{49}-\frac{100}{2401}=\frac{38414}{2401}>0.
$$

This proves the claim.

### Lemma 1.3: the CE2-overlap middle comparison

Let $0<A\le\lambda<1$ and

$$
\rho=\sqrt{1-\lambda+\lambda^2}.
$$

Define

$$
G_1=\frac{A+\rho-1-\lambda^2}{1-\lambda},\qquad
G_2=\frac{\lambda-A}{\lambda},\qquad G=\min(G_1,G_2).
$$

If $G\ge0$, then

$$
\boxed{e(G)<A.}
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

First prove $e(g)<A_0$.  Put $c=1-g$ and $b_0=A_0=\lambda c$.  The Low polynomial in $b$ is

$$
F_c(b)=b^2-cb+c^2(1-c^2).
$$

Using $\rho^2=1-\lambda+\lambda^2$, direct reduction gives

$$
F_c(b_0)=-(\rho-1)^2(\rho^2+1)(\rho^2-\rho+1)^2<0.
$$

Since $F_c(0)=c^2(1-c^2)>0$ and $e(g)$ is the smaller positive root of $F_c$, this implies

$$
e(g)<b_0=A_0.
$$

If $G=G_2$, then $A\ge A_0$, and $G_2=(\lambda-A)/\lambda\le g$.  Since $\ell$ is increasing on the Low range,

$$
e(G)\le e(g)<A_0\le A.
$$

If $G=G_1$, then $A\le A_0$.  On the interval where $G_1\ge0$, let

$$
F(A)=A-e(G_1(A)).
$$

The lower endpoint is $A_L=1+\lambda^2-\rho$, where $G_1=0$ and $F(A_L)=A_L>0$.  At the upper endpoint $A_0$,

$$
F(A_0)=A_0-e(g)>0.
$$

Moreover $0\le G_1\le g<1/8$, and $e$ is convex on $[0,1/8]$.  Since $G_1$ is affine in $A$, the function $A\mapsto e(G_1(A))$ is convex, so $F$ is concave.  A concave function lies above the chord joining its endpoint values.  Hence $F(A)>0$ throughout the interval, proving $e(G_1(A))<A$.

Thus $e(G)<A$ in all cases.

### Lemma 1.4: the center-transfer lemma used in `4078`

Let $0<u\le1-\sqrt3/2$ and $z=e(u)$.  Suppose $0<\lambda<1$ and

$$
\lambda\ge \frac{z}{1-u}.
$$

Set

$$
\rho=\sqrt{1-\lambda+\lambda^2},\qquad
S_\lambda(v)=u+\frac{\lambda}{1+\rho}+\frac{\lambda}{1-\lambda}v.
$$

If either $v\ge1-\sqrt3/2$, or $0\le v\le1-\sqrt3/2$ and

$$
S_\lambda(v)\le e(v),
$$

then

$$
\boxed{z<S_\lambda(v).}
$$

#### Proof

Put

$$
c=1-u,\qquad \beta=\frac{z}{c}.
$$

Since $z=e(u)$,

$$
\beta=\frac{1-\sqrt{4c^2-3}}{2}
$$

and

$$
c^2=1-\beta+\beta^2.
$$

The hypothesis is $\lambda\ge\beta$.  The functions

$$
\lambda\mapsto \frac{\lambda}{1+\sqrt{1-\lambda+\lambda^2}}
$$

and

$$
\lambda\mapsto \frac{\lambda}{1-\lambda}
$$

are increasing on $(0,1)$.  Hence

$$
S_\lambda(v)\ge S_\beta(v).
$$

At $\lambda=\beta$, the corresponding value of $\rho$ is $c$.  Thus

$$
S_\beta(v)=u+\frac{\beta}{1+c}+\frac{\beta}{1-\beta}v.
$$

If $S_\beta(0)\ge z$, then $S_\lambda(v)\ge z$.  Strictness is automatic in the two alternatives of the lemma: if $v>0$, then $S_\beta(v)>S_\beta(0)$, and if $v=0$ the alternative $S_\lambda(0)\le e(0)=0$ is impossible because $S_\lambda(0)>0$.

It remains to treat the case $S_\beta(0)<z$.  Let $v_0$ be defined by

$$
S_\beta(v_0)=z.
$$

Then

$$
v_0=\frac{(1-\beta)(\beta^2+c-1)}{1+c}>0.
$$

Also

$$
u-v_0=\frac{(1-\beta)(1+\beta-\beta^2-c)}{1+c}.
$$

The numerator is positive because

$$
(1+\beta-\beta^2)^2-c^2=\beta(\beta-1)(\beta^2-\beta-3)>0
$$

for $0<\beta\le1/2$.  Hence $0<v_0<u$.  Furthermore,

$$
v_0<(1-\beta)\beta^2\le \frac{1}{8}.
$$

On $[0,v_0]$ the Low function is convex, so

$$
H(v)=S_\beta(v)-e(v)
$$

is concave.  We have $H(0)>0$, and

$$
H(v_0)=z-e(v_0)>0
$$

because $v_0<u$ and $\ell$ is increasing.  Hence $H(v)>0$ for $0\le v\le v_0$.

If $v\ge1-\sqrt3/2$, then $v>v_0$, so

$$
S_\lambda(v)\ge S_\beta(v)>z.
$$

If instead $0\le v\le1-\sqrt3/2$ and $S_\lambda(v)\le e(v)$, suppose for contradiction that $S_\lambda(v)\le z$.  Then $S_\beta(v)\le z$, so $v\le v_0$.  But then

$$
S_\lambda(v)\ge S_\beta(v)>e(v),
$$

contradicting $S_\lambda(v)\le e(v)$.  Therefore $S_\lambda(v)>z$.

This proves the lemma.

## 2. Details for the left-high-sheet arguments in `407a`

### Lemma 2.1: realized left high-sheet Cell 2 condition

In the left high-sheet parameterization

$$
A_5=rc,\qquad B_5=\beta c,\qquad c=\frac{m}{r+\beta},\qquad m^2=\beta^2-\beta+1,
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
=m^2\left(m^2-1+\frac{r\beta}{(r+\beta)^2}\right).
$$

Since $m^2-1=\beta^2-\beta=-\beta(1-\beta)$ and $m^2>0$, the inequality $\Delta\ge0$ is equivalent to

$$
\frac{r\beta}{(r+\beta)^2}\ge \beta(1-\beta).
$$

Dividing by $\beta>0$ gives

$$
r\ge(1-\beta)(r+\beta)^2.
$$

### Lemma 2.2: high-left envelope

For the left high-sheet parameterization, define

$$
y_*=\frac{r}{1-r}\left(\frac{m}{r+\beta}-\frac{1}{2}-\frac{1-r}{1+\rho}\right),\qquad b=\frac{\beta m}{r+\beta}.
$$

If $S<1/2$, then $y<y_*$.  Moreover

$$
\boxed{y_*<\frac{1}{10}},\qquad
\boxed{3y_*\le1-b.}
$$

#### Proof

The inequality $S<1/2$ gives $y<y_*$ directly.

First prove $y_*<1/10$.  The function $m/(r+\beta)$ is decreasing in
$\beta$, so $y_*$ is maximized at

$$
\beta_0(r)=\max\left\{r,\frac{1}{2},\frac{1-r^2}{1+2r}\right\}.
$$

Let $r_0=(\sqrt3-1)/2$.

If $0<r\le r_0$, then $m/(r+\beta)\le1$ and

$$
\frac{1-r}{1+\rho}\ge \frac{1}{3}.
$$

For the latter inequality, $2-3r\ge\rho$ has positive sides, and its squared
difference is

$$
(2-3r)^2-\rho^2=(8r-3)(r-1)\ge0.
$$

Therefore

$$
y_*\le \frac{r}{1-r}\left(\frac{1}{2}-\frac{1}{3}\right)
<\frac{3}{5}\cdot\frac{1}{6}=\frac{1}{10}.
$$

If $r_0\le r\le1/2$, then

$$
\frac{m}{r+\beta}\le\frac{\sqrt3}{1+2r}.
$$

We also use

$$
\frac{1-r}{1+\rho}
\ge L(r):=2-\sqrt3+\frac{1/2-r}{2}.
$$

This is equivalent to $1-r-L\ge L\rho$.  Both sides of the latter
inequality are positive on $[r_0,1/2]$.  After squaring, the difference is

$$
-\frac{(r-1)(2r-1)}{16}
\left(
2r^2+(8\sqrt3-17)r+56-32\sqrt3
\right).
$$

The quadratic factor is negative on $[r_0,1/2]$: its derivative is
$4r+8\sqrt3-17<0$, and its value at $r_0$ is
$(157-91\sqrt3)/2<0$.  Hence the displayed squared difference is
nonnegative and the lower bound for $L$ follows.

Consequently

$$
y_*\le
G(r):=\frac{r}{1-r}
\left(
\frac{\sqrt3}{1+2r}-\frac{1}{2}-2+\sqrt3-\frac{1/2-r}{2}
\right).
$$

A simplification gives

$$
\frac{1}{10}-G(r)
=\frac{P(r)}{20(r-1)(2r+1)},
$$

where

$$
P(r)=20r^3+(40\sqrt3-96)r^2+(40\sqrt3-57)r-2.
$$

Here

$$
P'(r)=60r^2+(80\sqrt3-192)r+40\sqrt3-57.
$$

This quadratic is positive on the real line: its minimum is

$$
168\sqrt3-\frac{1453}{5}>0,
$$

where the last inequality follows by squaring the positive integers
$840\sqrt3>1453$.  Hence $P$ is increasing.  Since
$P(1/2)=30\sqrt3-52<0$, one has $P(r)<0$ throughout the interval.  The
denominator is also negative, and therefore $G(r)<1/10$.

Finally, if $1/2\le r<1$, then $m/(r+\beta)\le\rho/(2r)$, whence

$$
y_*
\le\frac{\rho+1-3r}{2(1+\rho)}.
$$

The assertion that the right side is less than $1/10$ is equivalent to

$$
15r-4\rho-4>0.
$$

Its derivative is $15-2(2r-1)/\rho>0$; here
$2r-1<\rho$ follows after squaring from $3r(1-r)>0$.  At $r=1/2$ its value is
$7/2-2\sqrt3>0$.  This finishes the proof of $y_*<1/10$.

Now prove $3y_*\le1-b$.  Let

$$
E_r(\beta)=1-b-3y_*.
$$

A direct differentiation gives

$$
\frac{\partial E_r}{\partial\beta}=\frac{N_r(\beta)}{2(\beta+r)^2(1-r)\sqrt{\beta^2-\beta+1}},
$$

where

$$
N_r(\beta)=2\beta^3r-2\beta^3+4\beta^2r^2-5\beta^2r+\beta^2-9\beta r^2+5r^2+4r.
$$

Also

$$
\frac{\partial N_r}{\partial\beta}=-6\beta^2(1-r)+2\beta(1-r)(1-4r)-9r^2<0
$$

on the allowed domain $\beta\ge1/2$.  Hence $E_r$ has no interior minimum and it suffices to check endpoints.

At $\beta=1$,

$$
E_r(1)=\frac{r(6r-\rho+5)}{2(1+r)(1+\rho)}>0.
$$

At the lower endpoint there are three cases.  If $0<r\le r_0$, then $\beta_0=(1-r^2)/(1+2r)$ and

$$
E_r(\beta_0)=
\frac{r(7+\rho-2r-8r\rho-14r^2-2r^2\rho)}{2(1-r)(1+2r)(1+\rho)}>0,
$$

because the numerator is at least $r(7-10r-16r^2)>0$ for $r<3/8$.

If $r_0\le r\le1/2$, then $\beta_0=1/2$, so $b\le1/2$ and $y_*<1/8$, hence

$$
E_r(\beta_0)>1-\frac{1}{2}-\frac{3}{8}>0.
$$

If $1/2\le r<1$, then $\beta_0=r$ and

$$
E_r(r)=\frac{10r-r^2-2\rho-2}{2(1+\rho)}>0,
$$

because $10r-r^2-2\rho-2\ge10r-r^2-4>0$ on $[1/2,1]$.

Thus $E_r(\beta)\ge0$ throughout, proving $3y_*\le1-b$.

### Lemma 2.3: the estimates $S>3y$ and $A_C>3y$

Under $B_5=T_+^{hi}$ in the hard region,

$$
\boxed{S>3y},\qquad \boxed{A_C>3y}.
$$

#### Proof

Since $y<y_*<1/10$, we have $3y<3/10$.

Write $S=u+\delta+ky$ with $k=(1-r)/r$.  If $k\ge3$, then $S>3y$.  If $k<3$, the function $S-3y$ decreases in $y$, and at the endpoint $y=y_*$ one has $S=1/2$.  Thus

$$
S-3y>\frac{1}{2}-3y_*>\frac{1}{2}-\frac{3}{10}>0.
$$

For $A_C$, first prove $1-r>3/8$.  If $r\le1/2$ this is immediate.  If $r>1/2$, the feasibility condition $y_*>0$ gives

$$
\frac{\rho}{2r}>\frac{1}{2}+\frac{1-r}{1+\rho}.
$$

This is equivalent to $3r<1+\rho$.  Since $r>1/2$, squaring $3r-1<\rho$ gives $8r^2-5r<0$, so $r<5/8$.  Hence $1-r>3/8$ in all cases.

Therefore

$$
A_C=(1-r)(1-y)>\frac{3}{8}\cdot\frac{9}{10}=\frac{27}{80}>\frac{3}{10}>3y.
$$

## 3. Details for the right $T_-$ estimates in `407a`

Let $C=1-y$, $q=tC$, and $B_1=b_1$.  In the right $T_-$ branch,

$$
q+b_1=\mu=\sqrt{t^2-t+1}.
$$

The branch condition $b_1\le q$ gives $b_1\le\mu/2$ and $\mu\le2t$.

### Lemma 3.1

In the branch $B_1=T_-$ with $A_1=q$,

$$
B_1\le\kappa:=\frac{\sqrt{13}-1}{6}.
$$

#### Proof

From $\mu\le2t$,

$$
t^2-t+1\le4t^2,
$$

so $3t^2+t-1\ge0$ and $t\ge\kappa$.  Since $y<1/10$ and $q<1/2$, one has $t=q/(1-y)<5/9$.  On $[\kappa,5/9]$,

$$
\frac{1}{2}\sqrt{t^2-t+1}\le\kappa.
$$

Therefore

$$
B_1\le \frac{\mu}{2}\le\kappa.
$$

### Lemma 3.2

In the branch $B_1=T_-$ with $A_1=q$,

$$
q\le\tau<\frac{93}{200},
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
C\le\frac{\mu(1-t)}{t}.
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
P\left(\frac{93}{200}\right)<0,
$$

so $\tau<93/200$.

## 4. Analytic left-high threshold

### Lemma 4.1

Let $0<r<1$ and

$$
\max\left\{r,\frac12\right\}\le\beta\le1.
$$

Put

$$
m=\sqrt{\beta^2-\beta+1},
\qquad
\rho=\sqrt{r^2-r+1},
\qquad
s=r+\beta,
$$

$$
S_0=1-\frac{m}{s}+\frac{1-r}{1+\rho},
\qquad
B_5=\frac{\beta m}{s}.
$$

If the realized high-sheet Cell 2 condition

$$
r\ge(1-\beta)(r+\beta)^2
$$

holds, then

$$
S_0<\frac{93}{200}
\quad\Longrightarrow\quad
B_5<\frac{5657}{10000}.
$$

#### Proof

First simplify the Cell 2 condition. The exact factorization

$$
r-(1-\beta)(r+\beta)^2
=
(s-1)(\beta^2+r\beta-r)
$$

has a nonnegative second factor, because

$$
\beta^2+r\beta-r
=\beta^2-r(1-\beta)
\ge\beta^2-\beta(1-\beta)
=\beta(2\beta-1)\ge0.
$$

If this factor vanishes, the displayed inequalities force
$r=\beta=1/2$, and hence $s=1$. Otherwise the Cell 2 condition forces
$s>1$. Thus in every case

$$
s\ge1.
$$

Conversely, $s\ge1$ makes both factors nonnegative, so on the stated domain
the Cell 2 condition is equivalent to $s\ge1$. In particular, the additional
left-high condition $\beta\ge(1-r^2)/(1+2r)$ is not needed for this lemma.

Since $r\le\beta$,

$$
\rho^2-m^2=(r-\beta)(s-1)\le0,
$$

so $\rho\le m$. Define

$$
\overline S(\beta)=1-m+\frac{\beta}{1+m}.
$$

Then

$$
S_0\ge1-\frac{m}{s}+\frac{1-r}{1+m}.
$$

The difference between the right side and $\overline S(\beta)$ is

$$
(s-1)\left(\frac{m}{s}-\frac{1}{1+m}\right).
$$

This is nonnegative. Indeed, $s\le2\beta$, and

$$
2\beta\le m(1+m).
$$

For the latter inequality, put $g=3\beta-\beta^2-1$. On
$[1/2,1]$ one has $g>0$, while

$$
m^2-g^2
=-\beta(\beta-1)(\beta^2-5\beta+5)\ge0.
$$

Hence $m\ge g$, and therefore

$$
m(1+m)\ge m^2+g=2\beta.
$$

We have proved

$$
S_0\ge\overline S(\beta).
$$

Now set

$$
B_0=\frac{5657}{10000},
\qquad
T=\frac{93}{200},
\qquad
\beta_*=\frac{161}{250}.
$$

Suppose $B_5\ge B_0$. Since $s\ge1$, this gives

$$
\beta m=sB_5\ge B_0.
$$

The function $\phi(\beta)=\beta m$ is strictly increasing, because

$$
\phi'(\beta)=\frac{4\beta^2-3\beta+2}{2m}>0.
$$

At $\beta_*$,

$$
B_0^2-\beta_*^2m(\beta_*)^2
=\frac{22782769}{62500000000}>0.
$$

Thus $\beta>\beta_*$. It remains to show
$\overline S(\beta)>T$ on $[\beta_*,1]$. Put

$$
F(\beta)=\frac{107}{200}-T m-(1-\beta)^2.
$$

Since

$$
m''=\frac{3}{4m^3},
$$

one has

$$
F''(\beta)=-\frac{3T}{4m^3}-2<0.
$$

Thus $F$ is concave. At the right endpoint,

$$
F(1)=\frac{7}{100}>0.
$$

At the left endpoint, put

$$
a_*:=\frac{107}{200}-(1-\beta_*)^2
=\frac{51033}{125000}>0.
$$

The exact comparison

$$
a_*^2-T^2m(\beta_*)^2
=\frac{1693881}{62500000000}>0
$$

gives $F(\beta_*)>0$. Concavity places $F$ above the positive chord
joining its endpoint values, so $F>0$ throughout $[\beta_*,1]$.
Finally, the identity

$$
\left(\overline S(\beta)-T\right)(1+m)=F(\beta)
$$

shows that $\overline S(\beta)>T$. We have proved

$$
B_5\ge B_0
\quad\Longrightarrow\quad
S_0\ge\overline S(\beta)>T.
$$

Taking the contrapositive gives the claimed strict implication. $\square$
