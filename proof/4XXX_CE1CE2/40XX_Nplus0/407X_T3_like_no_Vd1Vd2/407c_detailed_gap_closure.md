# Detailed Gap-Closure Lemmas for the $407X$ Completion

Status: Proven

This file supplies the details that are used, sometimes in compressed form, in

- [`4078_left_L_family_completion.md`](4078_left_L_family_completion.md),
- [`4079_first_Full_and_lower_sheet_branches.md`](4079_first_Full_and_lower_sheet_branches.md), and
- [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md).

The purpose is to make the final assembly in
[`407b_final_assembly.md`](407b_final_assembly.md) independent of any omitted
"direct checks" in those files.

Throughout use the variables of
[`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md).  In the
CE2 overlap formulas set

$$
r=1-\lambda,\qquad u=\gamma_5,\qquad y={Y\over\lambda},\qquad
\rho=\sqrt{r^2-r+1}.
$$

The Low function is

$$
\ell(\eta)=
{(1-\eta)(1-\sqrt{4(1-\eta)^2-3})\over2},\qquad
0\le\eta\le\eta_0:=1-{\sqrt3\over2}.
$$

## 1. Details for the left-Low completion

### Lemma 1.1: Low separation

Let $0\le\eta\le\eta_0$, let $z=\ell(\eta)$, and suppose the Low candidate is realized for input $a=1-\beta$.  Then

$$
\boxed{\beta\ge z+\eta.}
$$

#### Proof

The Low equation is

$$
z^2-(1-\eta)z+(1-\eta)^2(1-(1-\eta)^2)=0.
$$

Equivalently,

$$
P(\eta,z)=0,
$$

where

$$
P(x,z)=x^4-4x^3+5x^2-(2+z)x+z-z^2.
$$

The Low realization domain contains

$$
a+z\le1,\qquad (a+z)^4-(a+z)^2+az\le0.
$$

With $a=1-\beta$ and $h=\beta-z$, the first inequality gives $h\ge0$, while the second becomes

$$
P(h,z)\le0.
$$

On $0\le x\le\eta_0<1/7$,

$$
{\partial P\over\partial x}=4x^3-12x^2+10x-(2+z)<0,
$$

because $4x^3+10x<4/343+10/7<2$ and the remaining terms are non-positive. Thus $P(\cdot,z)$ is strictly decreasing on $[0,\eta_0]$. If $h<\eta$, then $P(h,z)>P(\eta,z)=0$, contradicting $P(h,z)\le0$. Therefore $h\ge\eta$, i.e. $\beta\ge z+\eta$.

### Lemma 1.2: the non-overlap comparison

Let $0<A<1/2$ and set

$$
r_A=\sqrt{1-A+A^2},\qquad g=r_A(1-r_A).
$$

Then

$$
\boxed{2g+5g^2<A.}
$$

#### Proof

Write $r_A=1-y$.  Since $0<A<1/2$, one has

$$
0<y<1-{\sqrt3\over2}< {1\over7},
$$

and

$$
A={1-\sqrt{1-8y+4y^2}\over2}.
$$

The desired inequality is

$$
2(1-y)y+5(1-y)^2y^2<{1-\sqrt{1-8y+4y^2}\over2}.
$$

Equivalently,

$$
\sqrt{1-8y+4y^2}<1-4y-6y^2+20y^3-10y^4.
$$

The right side is positive for $0<y<1/7$, since

$$
1-4y-6y^2-10y^4>1-{4\over7}-{6\over49}-{10\over2401}>0.
$$

Squaring is therefore legitimate.  A direct expansion gives

$$
(1-4y-6y^2+20y^3-10y^4)^2-(1-8y+4y^2)
=4y^3Q(y),
$$

where

$$
Q(y)=25y^5-100y^4+130y^3-40y^2-36y+22.
$$

For $0<y<1/7$,

$$
Q(y)>22-{36\over7}-{40\over49}-{100\over2401}>0.
$$

Hence the squared difference is positive, proving the lemma.

### Lemma 1.3: the CE2 middle-overlap comparison

Let $0<A\le\lambda<1$, put

$$
\rho=\sqrt{1-\lambda+\lambda^2},
$$

and define

$$
G_1={A+\rho-1-\lambda^2\over1-\lambda},\qquad
G_2={\lambda-A\over\lambda},\qquad
G=\min(G_1,G_2).
$$

If $G\ge0$, then

$$
\boxed{\ell(G)<A.}
$$

#### Proof

The two functions cross when

$$
G_1=G_2.
$$

Solving gives

$$
A=A_0:=\lambda(2-\lambda+\lambda^2-\rho).
$$

At this value

$$
G_1=G_2=g:=\rho(1-\rho),\qquad A_0=\lambda(1-g).
$$

Let $c=1-g$ and $b_0=A_0=\lambda c$.  The Low polynomial at radial loss $g$ is

$$
P_c(b)=b^2-cb+c^2(1-c^2).
$$

A direct simplification using $\rho^2=1-\lambda+\lambda^2$ gives

$$
P_c(b_0)=-(\rho-1)^2(\rho^2+1)(\rho^2-\rho+1)^2<0.
$$

Since $P_c(0)=c^2(1-c^2)>0$, the point $b_0$ lies to the right of the smaller Low root, so

$$
\ell(g)<A_0.
$$

If $G=G_2$, then $A\ge A_0$ and $G_2\le g$, hence

$$
\ell(G)\le\ell(g)<A_0\le A.
$$

If $G=G_1$, then $A\le A_0$.  On the interval where $0\le G_1\le g$, the function

$$
F(A)=A-\ell(G_1(A))
$$

is concave because $G_1$ is affine and $\ell$ is convex on $[0,1/8]$.  Here $g\le(\sqrt3/2)(1-\sqrt3/2)<1/8$.  At the endpoint $G_1=0$, one has $F(A)=A>0$; at $A=A_0$, one has $F(A_0)=A_0-\ell(g)>0$.  Concavity gives $F>0$ throughout.  Therefore $\ell(G)<A$ in all cases.

### Lemma 1.4: center-transfer for the left-Low/right-high residual

Let $0<u\le\eta_0$, let $z=\ell(u)$, and suppose

$$
\lambda\ge {z\over1-u}.
$$

Set

$$
S_\lambda(v)=u+{\lambda\over1+\sqrt{1-\lambda+\lambda^2}}+{\lambda\over1-\lambda}v.
$$

If either $v\ge\eta_0$, or $0\le v\le\eta_0$ and

$$
S_\lambda(v)\le\ell(v),
$$

then

$$
\boxed{z<S_\lambda(v).}
$$

#### Proof

Put $c=1-u$ and

$$
\beta={z\over c}={1-\sqrt{4c^2-3}\over2}.
$$

Then $c^2=1-\beta+\beta^2$ and the hypothesis is $\lambda\ge\beta$.  Both

$$
\delta(\lambda)={\lambda\over1+\sqrt{1-\lambda+\lambda^2}},\qquad
k(\lambda)={\lambda\over1-\lambda}
$$

are increasing in $\lambda$.  Hence $S_\lambda(v)\ge S_\beta(v)$ for every $v$.

At $\lambda=\beta$ one has $\sqrt{1-\beta+eta^2}=c$, so

$$
S_\beta(v)=u+{\beta\over1+c}+{\beta\over1-\beta}v.
$$

If $S_\beta(0)\ge z$, then $S_\lambda(v)\ge z$ for all $v\ge0$.  Equality could occur only at $v=0$ and $S_\lambda(0)=z$, but the alternative $S_\lambda(0)\le\ell(0)=0$ is impossible since $S_\lambda(0)>0$.  Thus the desired strict inequality holds in all relevant cases.

Assume now $S_\beta(0)<z$.  Let $v_0$ be defined by

$$
S_\beta(v_0)=z.
$$

Using $z=\beta c$ and $c^2=1-\beta+\beta^2$, one obtains

$$
v_0={ (1-\beta)(\beta^2+c-1)\over1+c}.
$$

The assumption $S_\beta(0)<z$ gives $v_0>0$.  Moreover

$$
u-v_0={ (1-\beta)(1+\beta-\beta^2-c)\over1+c}>0.
$$

Indeed, $c<1+\beta-\beta^2$ follows after squaring, since

$$
(1+\beta-\beta^2)^2-c^2
=\beta(\beta-1)(\beta^2-\beta-3)>0
$$

for $0<\beta\le1/2$.  Also

$$
v_0<(1-\beta)\beta^2\le {1\over8}.
$$

Define

$$
H(v)=S_\beta(v)-\ell(v).
$$

On $[0,v_0]$, $\ell$ is convex, hence $H$ is concave.  Also

$$
H(0)=S_\beta(0)>0,\qquad H(v_0)=z-\ell(v_0)>0
$$

because $v_0<u$ and $\ell$ is increasing.  Therefore $H(v)>0$ on $[0,v_0]$.

If $S_\lambda(v)\le z$, then $S_\beta(v)\le z$, so $v\le v_0$ and hence

$$
S_\lambda(v)\ge S_\beta(v)>\ell(v).
$$

This contradicts the second alternative.  If $v\ge\eta_0$, then $v>u>v_0$, so

$$
S_\lambda(v)\ge S_\beta(v)>S_\beta(v_0)=z.
$$

This proves the lemma.

## 2. Details for the left-lower-sheet file

### Lemma 2.1: midpoint exit bound

In the normalized $407X$ branch,

$$
\boxed{\gamma_5<{1\over2}.}
$$

#### Proof

The $C$-triangle contains exactly $M_0$ among the six radial midpoints.  Thus $M_5\notin T_C$.  The radial intersection $T_C\cap r_5$ is closed and has endpoint $\gamma_5$ in the center-to-$V_5$ coordinate.  Since $M_5$ is the point of coordinate $1/2$ on $r_5$, one must have $\gamma_5<1/2$.

### Lemma 2.2: left lower-sheet estimates

Assume $B_5=T_+^{lo}$ in the hard CE2 overlap region.  Put $r=1-\lambda$, $u=\gamma_5$, $y=Y/\lambda$, and $\rho=\sqrt{r^2-r+1}$.  Then

1. $0<r\le1/2$ and $r\ge r_0:=(\sqrt3-1)/2$;
2. $y<1/4$;
3. if $0\le y<\eta_0$, then $S>\ell(y)$;
4. if $y\ge\eta_0$, then $S>7/16$ and $A_C>7/16$.

#### Proof

The lower sheet has $A_5=1-T=(1-\lambda)(1-u)=r(1-u)$ and $C_5=1-u$.  Since $B_5\ge A_5$ and $B_5\le C_5/2$, one obtains $r\le1/2$.  By Lemma 2.1, $1-u>0$.

Write $B_5=(1-u)\beta$ with $r\le\beta\le1/2$.  The $T_+$ equation gives

$$
1-u={\sqrt{\beta^2-eta+1}\over r+\beta}.
$$

Since $1-u\le1$, there must exist $\beta\le1/2$ with $r+\beta\ge\sqrt{\beta^2-eta+1}$.  The weakest condition occurs at $\beta=1/2$, giving

$$
r+{1\over2}\ge {\sqrt3\over2},
$$

so $r\ge r_0$.

Now

$$
S=u+{1-r\over1+\rho}+{1-r\over r}y.
$$

Here $(1-r)/(1+ho)\ge2-\sqrt3$ and $(1-r)/r\ge1$.  Since CE2 overlap gives $S<1/2$, we get

$$
y<{1\over2}-(2-\sqrt3)=\sqrt3-{3\over2}<{1\over4}.
$$

For $0\le x\le\eta_0$, define

$$
D(x)=u+{1-r\over1+\rho}+{1-r\over r}x-\ell(x).
$$

The Low function is convex on $[0,\eta_0]$, so $D$ is concave.  One has $D(0)>0$.  At $x=\eta_0$, a three-range check in $r\in[r_0,1/2]$ gives

$$
u+{1-r\over1+ho}+{1-r\over r}\eta_0>{7\over16}>{\sqrt3\over4}=\ell(\eta_0).
$$

If the endpoint of the feasible interval is instead determined by $S=1/2$, then $D=1/2-\ell(x)>0$.  Thus $D>0$ throughout the feasible range, proving $S>\ell(y)$ for $y<\eta_0$.

For $y\ge\eta_0$, the same three-range check yields

$$
S\ge u+{1-r\over1+ho}+{1-r\over r}\eta_0>{7\over16}.
$$

Finally, $S<1/2$ gives

$$
y<{1/2-u-(1-r)/(1+ho)\over(1-r)/r}.
$$

Using $A_C=(1-r)(1-y)$ and the lower bound for $u$ coming from

$$
1-u\le {\sqrt{r^2-r+1}\over2r},
$$

one obtains

$$
A_C>{7\over16}.
$$

Explicitly, for $r\le7/16$ this follows from

$$
A_C>1-{3r\over2}+r{1-r\over1+ho}
\ge {11\over32}+{9(\sqrt3-1)\over64}>{7\over16},
$$

and for $7/16\le r\le1/2$ it follows from

$$
A_C>1-{r\over2}+r{1-r\over1+ho}-{\rho\over2}
>{447-16\sqrt{193}\over512}>{7\over16}.
$$

This proves all claims.

## 3. Details for the left-high-sheet file

### Lemma 3.1: the left-high Cell-2 condition

Under the realized left branch $B_5=T_+^{hi}$, with the notation of `407a`, one has

$$
\boxed{r\ge(1-\beta)(r+\beta)^2.}
$$

#### Proof

The left input is $a=rc$, the output is $b=\beta c$, and

$$
a+b=c(r+\beta)=m,\qquad m^2=\beta^2-\beta+1.
$$

The realized $T_+$ branch is in Cell 2, so

$$
\Delta=(a+b)^4-(a+b)^2+ab\ge0.
$$

Substituting gives

$$
\Delta=m^4-m^2+r\beta c^2.
$$

Since $c^2=m^2/(r+\beta)^2$ and $m^2-1=-\beta(1-\beta)$,

$$
\Delta=m^2\left(-\beta(1-\beta)+{r\beta\over(r+\beta)^2}\right).
$$

Because $m^2\beta>0$, the condition $\Delta\ge0$ is equivalent to

$$
r\ge(1-\beta)(r+\beta)^2.
$$

### Lemma 3.2: high-left envelope

Let

$$
y_*={r\over1-r}\left({m\over r+\beta}-{1\over2}-{1-r\over1+\rho}\right),
\qquad
b={\beta m\over r+\beta}.
$$

Under the left-high hypotheses,

$$
\boxed{y_*<{1\over8}},
\qquad
\boxed{3y_*\le1-b.}
$$

#### Proof

The proof of $y_*<1/8$ is the standard three-range estimate.  Since $m/(r+\beta)$ is decreasing in $\beta$, it suffices to use the lower endpoint

$$
\beta_0(r)=\max\left(r,{1\over2},{1-r^2\over1+2r}\right).
$$

If $0<r\le(\sqrt3-1)/2$, then $m/(r+\beta)\le1$ and $(1-r)/(1+\rho)>(1-r)/2$, giving

$$
y_*<{r^2\over2(1-r)}<{1\over8}.
$$

If $(\sqrt3-1)/2\le r\le1/2$, then

$$
{m\over r+\beta}\le {\sqrt3\over1+2r},\qquad
{1-r\over1+ho}\ge2-\sqrt3+{1/2-r\over2}.
$$

The inequality $y_*<1/8$ reduces to

$$
8r^3-10r^2+(8\sqrt3-9)r-1<0.
$$

Its derivative is positive on the interval and the value at $1/2$ is $4\sqrt3-7<0$.

If $1/2\le r<1$, then $m/(r+\beta)\le\rho/(2r)$, and the resulting bound is

$$
y_*\le {\rho+1-3r\over2(1+ho)}<{1\over8},
$$

because $\rho+1<4r$ for $r\ge1/2$.

Now define

$$
E_r(\beta)=1-b-3y_*.
$$

A direct differentiation gives

$$
{\partial E_r\over\partial\beta}= {N_r(\beta)
\over 2(\beta+r)^2(1-r)\sqrt{\beta^2-\beta+1}},
$$

where

$$
N_r(\beta)=2\beta^3r-2\beta^3+4\beta^2r^2-5\beta^2r+eta^2-9\beta r^2+5r^2+4r.
$$

Moreover

$$
{\partial N_r\over\partial\beta}
=-6\beta^2(1-r)+2\beta(1-r)(1-4r)-9r^2<0
$$

on the allowed interval $\beta\ge1/2$.  Hence $E_r$ has no interior minimum.

At $\beta=1$,

$$
E_r(1)={r(6r-ho+5)\over2(1+r)(1+ho)}>0.
$$

At the lower endpoint there are three cases.  If $0<r\le(\sqrt3-1)/2$, then $\beta_0=(1-r^2)/(1+2r)$ and

$$
E_r(\beta_0)=
{r(7+ho-2r-8r\rho-14r^2-2r^2\rho)
\over2(1-r)(1+2r)(1+ho)}>0,
$$

because the numerator is at least $r(7-10r-16r^2)>0$.  If $(\sqrt3-1)/2\le r\le1/2$, then $\beta_0=1/2$, so $b\le1/2$ and $y_*<1/8$, giving $E_r>1/8$.  If $1/2\le r<1$, then $\beta_0=r$ and

$$
E_r(r)={10r-r^2-2\rho-2\over2(1+ho)}>0,
$$

because $10r-r^2-2\rho-2\ge10r-r^2-4>0$ on $[1/2,1]$.  Thus $3y_*\le1-b$.

### Lemma 3.3: $S>3y$ and $A_C>3y$

Under the left-high hypotheses in the hard region,

$$
\boxed{S>3y},\qquad \boxed{A_C>3y}.
$$

#### Proof

Since $y<y_*<1/10$, one has $3y<3/10$.  Write

$$
S=u+{1-r\over1+ho}+{1-r\over r}y.
$$

If $(1-r)/r\ge3$, then $S>3y$.  Otherwise $S-3y$ is decreasing in $y$, and at $y=y_*$ one has $S=1/2$; hence

$$
S-3y>{1\over2}-3y_*>{1\over2}-{3\over10}>0.
$$

For $A_C$, first show $1-r>3/8$.  If $r\le1/2$ this is clear.  If $r>1/2$, feasibility $y_*>0$ gives

$$
{\rho\over2r}>{1\over2}+{1-r\over1+ho},
$$

which simplifies to $3r<1+ho$.  Squaring gives $r<5/8$.  Therefore $1-r>3/8$.  Since $A_C=(1-r)(1-y)$ and $y<1/10$,

$$
A_C>{3\over8}{9\over10}={27\over80}>{3\over10}>3y.
$$

### Lemma 3.4: detailed $T_-$ bounds for the $q$ case

In the branch $B_1=T_-$ and $A_1=q$, set $C=1-y$, $q=tC$, and $B_1=b_1$.  Then

$$
B_1\le\kappa:={\sqrt{13}-1\over6},
$$

and

$$
q\le\tau<{93\over200},
$$

where $\tau\in(0,1/2)$ is the unique root of

$$
x^4-3x^3+3x^2-3x+1=0.
$$

#### Proof

The $T_-$ equation gives

$$
q+b_1=\mu=\sqrt{t^2-t+1}.
$$

Since $b_1\le q$, we have $b_1\le\mu/2$ and $\mu\le2q\le2t$.  Thus $3t^2+t-1\ge0$, so $t\ge\kappa$.  Also $y<1/10$ and $q<1/2$ give $t<5/9$.  On $[\kappa,5/9]$, the quantity $\mu/2$ is at most $\kappa$, proving $B_1\le\kappa$.

For the $q$ bound, the realized Cell-2 condition gives

$$
(q+b_1)^4-(q+b_1)^2+qb_1\ge0.
$$

Substituting $q+b_1=\mu$ and $q=tC$ yields

$$
-tC^2+\mu C-(1-t)\mu^2\ge0.
$$

The case $t\ge1/2$ would force $C\le\mu<9/10$, contradicting $C>9/10$.  Hence $t<1/2$.  For $t<1/2$, the last quadratic gives

$$
C\le {\mu(1-t)\over t}.
$$

Therefore

$$
q=tC\le\min(t,\mu(1-t)).
$$

The maximum of the right side occurs when $t=\mu(1-t)$, which gives

$$
t^4-3t^3+3t^2-3t+1=0.
$$

The unique root in $(0,1/2)$ is $\tau$, and direct evaluation gives $\tau<93/200$.

## 4. Certificate linkage

The certificate `407b_T_hi_Tminus_qright_threshold_certificate.py` uses Lemma 3.1 as one of its domain conditions and proves

$$
S_0<{93\over200}\quad\Longrightarrow\quad B_5<{5657\over10000}< {7-\sqrt{13}\over6}.
$$

The certificate `407c_T_hi_Tlo_left_threshold_certificate.py` uses Lemma 3.1 and the lower-sheet condition $3p^2+p-1\ge0$ and proves

$$
S_0<\sqrt{p^2-p+1}-p\quad\Longrightarrow\quad B_5<1-p.
$$

Both scripts use rational interval arithmetic with one-sided integer square-root bounds and have recorded runs with zero unresolved boxes.
