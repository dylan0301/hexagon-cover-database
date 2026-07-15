# One-Side Capped-Loss Theorem

Status: Proven

This note proves the analytic loss estimate shared by the one-gap CE1 and CE2
boundary arguments. It uses only the capped demand map from
[`2011`](../20XX_V_triangle_geometry/2011_capped_demand_map.md), not any
CE1-specific endpoint inequality. This is the reason the two formerly
separate branch matrices can be replaced by one theorem.

## 1. Statement and notation

Let

$$
0<R<1,
\qquad
S=\sqrt{1-R+R^2},
$$

and let $s,u,w$ be positive numbers satisfying

$$
s+u+w=1,
\qquad
0<u<R.
$$

Define

$$
\delta=\frac{R}{1+S},
\qquad
\eta=(1-R)\delta=1-S,
$$

$$
\gamma_5=u-\delta-\frac{R}{1-R}w.
$$

Assume $\gamma_5>0$, and put

$$
c_1=\frac{u}{R},
\qquad
c_5=1-\gamma_5
=\frac{1-u+\eta-Rs}{1-R}.
$$

Let

$$
B_5=\widehat B_{c_5}(s),
\qquad
B_1=\widehat B_{c_1}(u),
$$

where $\widehat B$ is the capped safe map of `2011`. Then

$$
\boxed{B_5+B_1<1.}
$$

The identity used in the formula for $c_5$ is

$$
(1-S)(1+S)=R(1-R).
$$

The assumptions also place both demands in the high-radial range of the
four-label theorem:

$$
\frac12<c_1<1,
\qquad
\frac12<c_5<1.
$$

Indeed, $\gamma_5>0$ implies $u>\delta$, and hence

$$
c_1=\frac uR>\frac{\delta}{R}=\frac1{1+S}>\frac12.
$$

Its upper bound is $u<R$. The inequality $c_5<1$ is $\gamma_5>0$.
Moreover,

$$
\gamma_5<u-\delta<R-\delta=\frac{RS}{1+S}<\frac12.
$$

For the last inequality, it is immediate when $R\le1/2$; when $R>1/2$,
it is equivalent to $S(2R-1)<1$, and both factors are strictly less than
one. Thus $c_5>1/2$. Finally,

$$
c_5=\frac{1-u+\eta-Rs}{1-R}.
$$

The positivity can also be seen directly from

$$
1-u+\eta-Rs
=(1-R)s+w+\eta>0.
$$

## 2. A right low-label bound

We prove that either right low label satisfies

$$
\boxed{B_1\le S-u.}
$$

### Right label $T_-$

Write $b=B_1$. The exact Cell-$T$ frontier is

$$
\left((u+b)^2-1\right)c_1^2+uc_1-u^2=0.
$$

Substituting $c_1=u/R$ gives

$$
(u+b)^2=1-R+R^2=S^2.
$$

All quantities are nonnegative, so

$$
\boxed{B_1=S-u.}
$$

### Right label $L$

Put

$$
b=kc_1,
\qquad
0\le k\le\frac12.
$$

The exact Cell-$L$ frontier gives

$$
c_1^2=1-k+k^2=:C.
$$

Set $x=R+k$. Then

$$
u+b=c_1x.
$$

The Cell-$L$ selector is

$$
q=(u+b)^4-(u+b)^2+ub\le0.
$$

Exact substitution factors it as

$$
q=c_1^2(x-1)G(x),
$$

where

$$
G(x)=Cx^3+Cx^2-k(1-k)x+k^2.
$$

For $x\ge k$, one has $G(x)>0$. This is immediate for $k=0$. For $k>0$,

$$
G'(x)=C(3x^2+2x)-k(1-k)
\ge k(1+2k-k^2+3k^3)>0,
$$

and $G(k)>0$. Hence $q\le0$ implies $x\le1$.

Put $h=1-x\ge0$. Direct subtraction gives

$$
S^2-(u+b)^2
=h\left(1+2k^2+k(1-k)h\right)\ge0.
$$

Thus $u+b\le S$, and again

$$
\boxed{B_1\le S-u.}
$$

## 3. Left $T_-$ against a right high label or Full

Suppose the left label is $T_-$. Put

$$
z=\frac{s}{c_5},
\qquad
p=1-z,
\qquad
h=\sqrt{1-p+p^2}.
$$

The component selector $c_5\le2s$ gives $z\ge1/2$. The upper bound $z\le1$
follows from the nonsupercritical cap: the frontier identity below gives
$s+B_5=\sqrt{1-z+z^2}>1$ if $z>1$. Thus

$$
\frac12\le z\le1,
\qquad
0\le p\le\frac12.
$$

The Cell-$T$ frontier gives

$$
s+B_5=h.
$$

Its selector polynomial factors as

$$
q=-(s-hz)(s-h(1-z)).
$$

Since $q\ge0$ and $B_5\le s$, one obtains

$$
s\le zh.
$$

The center identity is

$$
c_5(1-Rp)=1-u+\eta.
$$

Therefore $s\le zh$ implies

$$
u\ge U:=\eta+A+Rph,
\qquad
A:=1-h.
$$

We next prove

$$
G:=\eta+A-(1-R)ph>0.
$$

Put $q_0=ph$. If $q_0>R$, then $q_0\le p\le1/2$ forces
$R<p\le1/2$, and therefore

$$
p(1-p)>R(1-R).
$$

Also

$$
\eta=\frac{R(1-R)}{1+S},
\qquad
A=\frac{p(1-p)}{1+h}.
$$

Both denominators are less than $2$, so

$$
U>R(1-R)+R^2=R,
$$

contrary to $u<R$. Hence $q_0\le R$. Since $q_0\le p\le1/2$,

$$
\begin{aligned}
\eta+A
&>\frac{R(1-R)+p(1-p)}2\\
&\ge\frac{R(1-R)+q_0(1-q_0)}2\\
&\ge(1-R)q_0.
\end{aligned}
$$

The last difference is

$$
\frac{(R-q_0)(1-R+q_0)}2\ge0.
$$

Thus $G>0$.

The exact center formula also gives

$$
w=
\frac{(1-R)(1-u)p-\eta(1-p)}{1-Rp}.
$$

Using $u\ge U$, direct subtraction yields

$$
(1-Rp)(A-w)
\ge
(1-Rp)G>0.
$$

Consequently

$$
\boxed{w<A=1-h.}
$$

If the right label is $T_+^{hi}$, write

$$
H=u+B_1=\sqrt{1-\beta+\beta^2}\le1.
$$

For the right Full label, use $H=1$. In both cases,

$$
\begin{aligned}
B_5+B_1
&=h+H-(s+u)\\
&=1+w-(1-h)-(1-H)\\
&<1.
\end{aligned}
$$

This proves both formerly missing or incomplete cells

$$
(T_-,T_+^{hi})
\qquad\text{and}\qquad
(T_-,\mathrm{Full}).
$$

## 4. Left $L$ against a right high label or Full

On a left $L$ frontier, put

$$
x=\frac{B_5}{c_5},
\qquad
0\le x\le\frac12,
\qquad
h(x)=\sqrt{1-x+x^2}.
$$

Then

$$
c_5=h(x),
\qquad
B_5=xh(x).
$$

For fixed $R,u$, the center equation gives

$$
s(x)=
\frac{R-u+\eta+(1-R)(1-h(x))}{R}.
$$

It makes $s(x)$ strictly increasing, while
$(1-x)h(x)$ is strictly decreasing and $xh(x)$ is strictly increasing. The
Cell-$L$ selector $q\le0$ places the realized point on the side

$$
s(x)\le(1-x)h(x)
$$

of the shared $q=0$ transition. Explicitly, if $y=s/h(x)$, then

$$
\frac{q}{h(x)^2}=(y-(1-x))P_x(y),
$$

where

$$
\begin{aligned}
P_x(y)
={}&(1-x+x^2)y^3
 +(1+2x-2x^2+3x^3)y^2\\
&+(x+2x^2-x^3+3x^4)y
 +(x^2+x^3+x^5).
\end{aligned}
$$

All coefficients are nonnegative for $0\le x\le1/2$, and the relevant
nondegenerate value is positive. Hence $q\le0$ gives $y\le1-x$.

For completeness, the transition lies in $0<x<1/2$ for either right label
considered here. At the actual point, $\gamma_5>0$ and $w>0$ imply
$u>\delta$. Hence the extrapolated value at $x=0$ has positive $w(0)$ and

$$
s(0)<1=(1-x)h(x).
$$

At $x=1/2$, put

$$
e=1-\frac{\sqrt3}{2}>\frac18.
$$

Then

$$
s\left(\frac12\right)
=\frac{R-u+\eta+(1-R)e}{R}.
$$

It is enough to prove $s(1/2)\ge1/2$, since

$$
\frac12h\left(\frac12\right)=\frac{\sqrt3}{4}<\frac12.
$$

Equivalently, it is enough to prove

$$
u\le \frac R2+\eta+(1-R)e.
$$

For the right Full label, $c_1=u/R>u$. Full feasibility therefore forces
$u<1/2$ and

$$
\frac{u}{R}\le1-u,
\qquad
u\le\frac{R}{1+R}.
$$

We use the elementary bounds

$$
\eta\ge\frac{R(1-R)}2,
\qquad
S\le1-\frac R2+\frac{R^2}{2}.
$$

The exact right-label bounds are

$$
u\le\frac{R}{1+R}
\qquad(\mathrm{Full}),
$$

and

$$
u\le\min\{RS,\frac S2\}
\qquad(T_+^{hi}).
$$

For Full, subtracting $R/(1+R)$ from the sufficient lower threshold

$$
\frac R2+\frac{R(1-R)}2+(1-R)e
$$

gives

$$
\frac{(1-R)(R^2+2Re+2e)}{2(1+R)}>0.
$$

For $T_+^{hi}$, if $R\le1/2$, the remaining difference is

$$
\frac{2e(1-R)-R^3}{2}\ge0;
$$

this follows because $R^3/(1-R)$ is increasing and its value at $1/2$ is
$1/4<2e$. If $R\ge1/2$, the difference is

$$
\frac{(1-R)(3R+4e-2)}4\ge0.
$$

The two right-$T_+^{hi}$ bounds used here are exact. Writing

$$
\beta=\frac{B_1}{c_1},
\qquad
H=\sqrt{1-\beta+\beta^2},
$$

one has $\beta\ge\max\{R,1/2\}$ and

$$
u=\frac{RH}{R+\beta}.
$$

The last quotient decreases with $\beta$; after multiplication by the
positive factor $2H(R+\beta)^2/R$, the sign of its derivative is the sign
of

$$
R(2\beta-1)+\beta-2<0.
$$

This gives $u\le S/2$ when $R\ge1/2$. When $R\le1/2$, the exact selector

$$
R\ge(1-\beta)(R+\beta)^2
$$

factors as

$$
(R+\beta-1)(\beta^2+R\beta-R)\ge0.
$$

The second factor is positive for $\beta\ge1/2$ except at
$(R,\beta)=(1/2,1/2)$, where $\beta=1-R$ already. Thus
$\beta\ge1-R$. Monotonicity then gives $c_1\le S$ and $u\le RS$.

Thus there is a unique shared transition $x_0\in(0,1/2)$. At this point

$$
s=(1-x_0)h(x_0),
\qquad
B_5=x_0h(x_0),
$$

so the transition is the $q=0$ endpoint of the $T_-$ case in Section 3.
Because $xh(x)$ is increasing, every realized left-$L$ output is no larger
than its transition output. This comparison point can have $w\le0$ and need
not itself lie in the positive-$w$ side-model domain. That causes no gap: the
algebra in
Section 3 uses only $0<R<1$, $u<R$, the center identity, the cap and component
conditions, and $q\ge0$; it never uses $w>0$. Section 3 therefore proves

$$
B_5+B_1<1
$$

for $(L,T_+^{hi})$ and $(L,\mathrm{Full})$ as well.

## 5. Full on the left and a high label on the right

Left Full feasibility first forces $s<1/2$ and

$$
\gamma_5\ge s.
$$

Indeed, $c_5\le\max\{s,1-s\}$, while
$\gamma_5<u<1-s$ gives $c_5>s$, excluding the $s\ge1/2$ alternative.

Right Full or right $T_+^{hi}$ gives $u\le1/2$. But

$$
\gamma_5-s
=2u-1-\delta+\frac{1-2R}{1-R}w.
$$

If $R\ge1/2$, the right side is negative. If $R<1/2$, use $w<1-u$ to get

$$
\gamma_5-s
<\frac{u-R}{1-R}-\delta<0.
$$

Both cases contradict $\gamma_5\ge s$. Hence

$$
(\mathrm{Full},\mathrm{Full})
\quad\text{and}\quad
(\mathrm{Full},T_+^{hi})
$$

are impossible.

## 6. Left $T_+^{hi}$ and right Full

The left high label gives $s<1/2$. Right Full gives

$$
u\le\frac{R}{1+R}.
$$

Since $\gamma_5>0$,

$$
w<\frac{1-R}{R}(u-\delta).
$$

On the other hand, $s<1/2$ gives $w>1/2-u$. Combining these inequalities
would force

$$
u>\frac R2+\eta.
$$

This is impossible because

$$
\frac R2+\eta>\frac{R}{1+R}.
$$

After division by $R(1-R)>0$, the last inequality is equivalent to
$2(1+R)>1+S$. Thus $(T_+^{hi},\mathrm{Full})$ is impossible.

## 7. A low label on the right

Put

$$
X=S-u.
$$

Section 2 gives $B_1\le X$. Notice that $X>0$, because $S>R>u$.
If $s>X$, then $B_1<s$, whereas the cap gives $B_5\le1-s$; equality
in the cap can occur only for the Full label. Thus $B_5+B_1<1$.
It remains to consider $s\le X$.

Set

$$
c_X=c_5(X)=X+2\delta,
\qquad
f(c,z)=c^4-c^2+zc-z^2.
$$

We first prove

$$
c_X>\frac{\sqrt3}{2},
\qquad
f(c_X,X)>0.
$$

For fixed $R$, both $X$ and $c_X$ decrease with $u$. At the limiting
endpoint $u=R$, put $\kappa=\delta$. Then

$$
X_0=\frac{1-2\kappa}{1+\kappa},
\qquad
c_0=\frac{1+2\kappa^2}{1+\kappa}.
$$

The inequality $c_0>\sqrt3/2$ follows after squaring from

$$
16\kappa^4+13\kappa^2-6\kappa+1>0;
$$

the quadratic $13\kappa^2-6\kappa+1$ has negative discriminant. Direct
substitution gives

$$
f(c_0,X_0)
=
\frac{
\kappa^2(1-2\kappa)^2
\left(4\kappa^4+4\kappa^3+10\kappa^2+6\kappa+5\right)
}{(1+\kappa)^4}>0.
$$

Along the $u$-line,

$$
\frac{d}{du}f(c_X,X)=-4c_X^3+c_X+X<0,
$$

because $X<c_X$ and $c_X\ge c_0>\sqrt3/2$. Consequently the two claimed
inequalities hold for every $u<R$.

Define

$$
\ell(c)=\frac c2\left(1-\sqrt{4c^2-3}\right).
$$

The roots of

$$
H_c(z)=z^2-cz+c^2-c^4
$$

are $\ell(c)$ and $c-\ell(c)$. Since
$H_{c_X}(X)=-f(c_X,X)<0$,

$$
\ell(c_X)<X<c_X-\ell(c_X).
$$

In particular, $\ell(c_X)<c_X-X=2\delta$. Since $c_5$ decreases with
$s$, the assumptions $s\le X$ and $c_5(s)<1$ give

$$
c_X\le c_5(s)<1,
\qquad
2\delta=c_X-X<1-X.
$$

For $\sqrt3/2\le c\le1$, write

$$
c=h(z):=\sqrt{1-z+z^2},
\qquad
0\le z\le\frac12.
$$

Then $\ell(c)=zh(z)$. The actual $c_5(s)\in[c_X,1)$ corresponds to some
$0<z\le z_X<1/2$. Along the center line, its input is

$$
s(z)=s_0+\frac{1-R}{R}(1-h(z)),
\qquad
s_0=\frac{R-u+\eta}{R}>0.
$$

Both $s(z)$ and $zh(z)$ increase, while

$$
a_{tr}(z)=(1-z)h(z)
$$

decreases. At $z_X$, the root ordering above says

$$
s(z_X)=X<c_X-\ell(c_X)=a_{tr}(z_X).
$$

Hence $s(z)<a_{tr}(z)$ for $0\le z\le z_X$.

We also need the smaller coordinate in the Cell-$L$ equation to be
$b(z)=zh(z)$. Put

$$
\phi(z)=s(z)-zh(z),
\qquad
k=\frac{1-R}{R}.
$$

Both endpoint values are positive:

$$
\phi(0)=s_0>0,
\qquad
\phi(z_X)=X-\ell(c_X)>0.
$$

Moreover,

$$
\phi'(z)=\frac{(k+z)(1-2z)}{2h(z)}-h(z).
$$

If $k\le2$, then $(k+z)(1-2z)\le2h(z)^2$, so $\phi'\le0$.
If $k>2$, the equation $\phi'(z)=0$ is equivalent to

$$
k=K(z):=\frac{2-3z+4z^2}{1-2z},
$$

and

$$
K'(z)=\frac{1+8z-8z^2}{(1-2z)^2}>0.
$$

Thus $\phi$ first increases and then decreases, and its minimum is at an
endpoint. In either case $b(z)<s(z)$.

The exact selector factorization from the proof of the Cell-$L$ row in
Section 4 is

$$
\frac{q}{h(z)^2}
=
\left(\frac{s(z)}{h(z)}-(1-z)\right)
P_z\left(\frac{s(z)}{h(z)}\right),
$$

where $P_z$ has nonnegative coefficients and is positive at every
nondegenerate point. Thus $q<0$. Also

$$
s+b\le X+\ell(c_X)<1,
$$

so $s^2+sb+b^2<(s+b)^2<1$. All Cell-$L$ conditions therefore hold, and

$$
\frac{\partial F_L}{\partial b}=c-2b=c(1-2z)>0.
$$

Every immediate increase of $b$ is infeasible; the interval-fiber theorem
in [`2007`](../20XX_V_triangle_geometry/2007_max_b_map.md) rules out later
re-entry. The uncapped maximum is $zh(z)$, and the cap can only decrease it.
Consequently

$$
B_5\le zh(z)\le z_Xh(z_X)=\ell(c_X)<1-X.
$$

Together with $B_1\le X$, this proves $B_5+B_1<1$ whenever the right label
is $L$ or $T_-$.

## 8. Exclusion of the high/high pair

For $0\le z\le1/2$, let $c_L(z)$ be the unique root in
$[\sqrt3/2,1]$ of

$$
f(c,z)=c^4-c^2+zc-z^2=0.
$$

This root is strictly convex. Indeed, with

$$
D=4c^3-2c+z>0,
$$

implicit differentiation and $f(c,z)=0$ give

$$
c_L' =\frac{2z-c}{D},
\qquad
c_L''
=
\frac{2(c^2-cz+z^2)+16c^2z(c-z)}{D^3}>0.
$$

A realized left $T_+^{hi}$ point requires

$$
s<\frac12,
\qquad
c_5(s)\le c_L(s).
$$

Set

$$
s_0=\frac{R-u+\eta}{R}.
$$

Because $u<R$ and $\eta>0$, while $\gamma_5>0$, a left high label has

$$
0<s_0<s<\frac12,
\qquad
c_5(s_0)=1.
$$

The function $g(z)=c_5(z)-c_L(z)$ is concave, and
$g(s_0)=1-c_L(s_0)>0$.

For a right $T_+^{hi}$ label, Section 4 proved

$$
u\le\min\{RS,S/2\}.
$$

If $0<R\le1/2$, this gives

$$
c_5\left(\frac12\right)
\ge
\frac{2-(1+R)S-R/2}{1-R}
>\frac78.
$$

The strict inequality is $9+3R>8(1+R)S$. Both sides are positive, and the
difference of their squares is

$$
P(R)=17-10R+9R^2-64R^3-64R^4.
$$

On $[0,1/2]$, one has $P'(R)<0$ because $18R\le9$, and
$P(1/2)=9/4>0$. Hence $P(R)>0$.

If $1/2\le R<1$, the same bound gives

$$
c_5\left(\frac12\right)
\ge
\frac{4-3S-R}{2(1-R)}
>\frac78,
$$

where the last inequality follows from

$$
(3+R)^2-16S^2=(1-R)(15R-7)>0.
$$

Finally,

$$
f\left(\frac78,\frac12\right)=\frac{33}{4096}>0,
$$

and $f$ increases with $c$ on $[\sqrt3/2,1]$. Therefore

$$
c_L(1/2)<\frac78<c_5(1/2),
$$

so $g(1/2)>0$. Concavity makes $g$ positive throughout
$[s_0,1/2]$, contradicting $c_5(s)\le c_L(s)$. Thus high/high is
impossible.

## 9. Exhaustive assembly

The four exact safe labels are

$$
L,
\qquad
T_-,
\qquad
T_+^{hi},
\qquad
\mathrm{Full}.
$$

If both labels lie in $\{L,T_-\}$, then

$$
B_5+B_1\le s+u=1-w<1.
$$

Section 7 covers the remaining pairs with a low label on the right.
Sections 3--4 cover a low label on the left against a high label or Full.
Section 5 excludes Full against a high label or Full, Section 6 excludes a
high label against Full, and Section 8 excludes high/high. These are all
ordered pairs, so

$$
\boxed{B_5+B_1<1}
$$

under precisely the hypotheses in Section 1.

$$
\Box
$$
