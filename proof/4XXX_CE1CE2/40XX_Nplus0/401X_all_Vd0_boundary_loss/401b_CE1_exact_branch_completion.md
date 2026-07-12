# Exact CE1 Completion of the All-Vd0 Boundary-Loss Matrix

Status: Proven

This note proves the CE1 part of the `401X` all-Vd0, nonsupercritical
boundary-loss obstruction. It uses the exact formulas in `2105` and the exact
four-label safe map in `4015`. No interval certificate or undeclared runtime
dependency is used.

The result does not include CE2. The final inequality in the exact CE1 domain
excludes a second boundary interval and is essential below; the coupled CE2
domain in `2106` does not satisfy that hypothesis.

## 1. Exact CE1 coordinates

Use the exact normalization from
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md).
Put

$$
R=\lambda,
\qquad
S=\sqrt{1-R+R^2},
\qquad
0<R<1,
$$

and write

$$
T_C\cap e_{0,1}=[s,t],
\qquad
u=1-t,
\qquad
w=t-s=1-u-s>0.
$$

Define

$$
\delta=\frac{R}{1+S},
\qquad
\eta=(1-R)\delta=1-S.
$$

The last identity follows from

$$
(1-S)(1+S)=R(1-R).
$$

The historical variables in `4014` are not a specialization: they are the
exact substitutions $R=\lambda$ and $r=1/R$. The two adjacent radial demands
are

$$
c_1=\frac{u}{R},
$$

and

$$
c_5=1-\gamma_5,
\qquad
\gamma_5=u-\delta-\frac{R}{1-R}w.
$$

Equivalently,

$$
c_5=\frac{1-u+\eta-Rs}{1-R}.
$$

The open-center inequalities give

$$
0<u<R,
\qquad
\gamma_5>0.
$$

Let

$$
B_5=\widehat B_{c_5}(s),
\qquad
B_1=\widehat B_{c_1}(u),
$$

where $\widehat B$ is the safe capped map proved in `4015`. It is enough, by
the boundary-loss reduction in `4014`, to prove

$$
B_5+B_1<1.
$$

## 2. A strict center inequality

Two inequalities in the exact CE1 domain are

$$
t+R(1-s)\le S
$$

and

$$
t\ge S-\frac{R^2}{1-R}s.
$$

Combining them gives

$$
S-\frac{R^2}{1-R}s
\le
S-R(1-s),
$$

and hence

$$
\boxed{s\ge1-R.}
$$

The first inequality also gives

$$
u=1-t\ge1+R-S-Rs.
$$

Therefore

$$
\begin{aligned}
s+u-S
&\ge1+R-2S+(1-R)s\\
&\ge1+R-2S+(1-R)^2\\
&=1+S^2-2S\\
&=(1-S)^2>0.
\end{aligned}
$$

Thus

$$
\boxed{s>S-u,}
$$

or equivalently

$$
\boxed{w<1-S.}
$$

This exact inequality replaces the former convexity and Bernstein argument
for the left-$T_+^{hi}$ frontier.

## 3. A right low-label bound

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

Together with Section 2, every right $L$ or $T_-$ output satisfies

$$
B_1<s.
$$

## 4. Left $T_-$ against a right high label or Full

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

## 5. Left $L$ against a right high label or Full

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

For the right Full label, $c_1=u/R>u$. Full feasibility therefore forces
$u<1/2$ and

$$
\frac{u}{R}\le1-u,
\qquad
u\le\frac{R}{1+R}.
$$

The elementary bounds

$$
\eta\ge\frac{R(1-R)}2,
\qquad
S\le1-\frac R2+\frac{R^2}{2}
$$

reduce this to the following exact right-label bounds:

$$
u\le\frac{R}{1+R}
\qquad(\mathrm{Full}),
$$

and

$$
u\le\min\left\{RS,\frac S2\right\}
\qquad(T_+^{hi}).
$$

For Full, subtracting $R/(1+R)$ from the resulting upper threshold gives

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

The last quotient decreases with $\beta$, which gives $u\le S/2$ when
$R\ge1/2$. When $R\le1/2$, the exact selector

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

so the transition is the $q=0$ endpoint of the $T_-$ case in Section 4.
Because $xh(x)$ is increasing, every realized left-$L$ output is no larger
than its transition output. This comparison point can have $w\le0$ and need
not itself lie in the exact CE1 domain. That causes no gap: the algebra in
Section 4 uses only $0<R<1$, $u<R$, the center identity, the cap and component
conditions, and $q\ge0$; it never uses $w>0$. Section 4 therefore proves

$$
B_5+B_1<1
$$

for $(L,T_+^{hi})$ and $(L,\mathrm{Full})$ as well.

## 6. Full on the left and a high label on the right

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

## 7. Left $T_+^{hi}$ and right Full

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

## 8. The pair $(T_+^{hi},T_+^{hi})$

For $0\le y\le1/2$, let $c_L(y)$ be the unique root in
$[\sqrt3/2,1]$ of

$$
f(c,y)=c^4-c^2+yc-y^2=0.
$$

The exact $L/T$ cell ordering says that a realized left $T_+^{hi}$ point
requires

$$
c_5(y)\le c_L(y).
$$

The function $c_L$ is strictly convex. If

$$
D=4c^3-2c+y,
$$

implicit differentiation gives

$$
c_L' =\frac{2y-c}{D}
$$

and, after using $f(c,y)=0$,

$$
c_L''
=
\frac{
2(c^2-cy+y^2)+16c^2y(c-y)
}{D^3}>0.
$$

Put

$$
X=S-u.
$$

Section 2 gives $s>X$. The left high label gives $s<1/2$. It remains to show
that the concave function

$$
g(y)=c_5(y)-c_L(y)
$$

is positive at both endpoints of $[X,1/2]$.

At $y=X$,

$$
c_5(X)=X+2\delta.
$$

Put $\kappa=\delta\in(0,1/2)$. As $u$ increases to $R$, both $X$ and
$c_5(X)$ decrease, and

$$
\frac{d}{du}f(c_5(X),X)=-4c_5(X)^3+c_5(X)+X<0.
$$

Indeed, $X<c_5(X)$ and
$c_5(X)\ge c_5(X)|_{u=R}>\sqrt3/2$, so the derivative is less than
$-4c_5(X)^3+2c_5(X)<0$.

At $u=R$,

$$
X=\frac{1-2\kappa}{1+\kappa},
\qquad
c_5(X)=\frac{1+2\kappa^2}{1+\kappa}>\frac{\sqrt3}{2}.
$$

The last inequality follows because

$$
16\kappa^4+13\kappa^2-6\kappa+1>0.
$$

Here $13\kappa^2-6\kappa+1$ has negative discriminant.

Direct substitution gives

$$
f(c_5(X),X)
=
\frac{
\kappa^2(1-2\kappa)^2
\left(4\kappa^4+4\kappa^3+10\kappa^2+6\kappa+5\right)
}{(1+\kappa)^4},
$$

which is positive. Since

$$
\frac{\partial f}{\partial c}=4c^3-2c+X>0
$$

for $c\ge\sqrt3/2$, this implies $c_5(X)>c_L(X)$. At the other endpoint, the left high label and
$s\ge1-R$ force $R>1/2$. The right high formula gives $u\le S/2$, so

$$
c_5\left(\frac12\right)
\ge
\frac{4-3S-R}{2(1-R)}
>\frac78.
$$

The last inequality follows from

$$
(3+R)^2-16S^2=(1-R)(15R-7)>0.
$$

On the other hand,

$$
f\left(\frac78,\frac12\right)=\frac{33}{4096}>0,
$$

and the same positive $c$-derivative gives $c_L(1/2)<7/8$. Hence
$g(1/2)>0$. Concavity now gives $g>0$ throughout
$[X,1/2]$, contradicting the left-$T_+^{hi}$ realization condition. Therefore
the pair $(T_+^{hi},T_+^{hi})$ is impossible.

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

If the right label lies in $\{L,T_-\}$, Section 3 gives $B_1<s$.
Left Full then has $B_5=1-s$, while left $T_+^{hi}$ has the strict cap
$B_5<1-s$; both combinations have sum less than $1$.

Sections 3--8 cover every remaining ordered pair. Therefore

$$
\boxed{B_5+B_1<1}
$$

throughout the exact CE1 domain whenever a positive center-only interval is
present. If no such interval is present, the exact open-perimeter lemma in
`4014`, Section 6 gives the contradiction directly. Thus the CE1 branch with
all six vertex roles Vd0 and $a_i+b_i\le1$ is proved.

$$
\Box
$$
