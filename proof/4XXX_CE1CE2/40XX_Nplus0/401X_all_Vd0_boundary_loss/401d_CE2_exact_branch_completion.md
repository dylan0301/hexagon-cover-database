# Exact CE2 One-Gap Completion of the All-Vd0 Boundary-Loss Matrix

Status: Proven

This note proves the one-gap part of the CE2, all-Vd0, nonsupercritical
boundary-loss obstruction. Precisely, assume that:

- the center role is CE2 and contains exactly $M_0$;
- all six vertex roles are Vd0;
- $N_+=0$, so $a_i+b_i\le1$ for every vertex row; and
- exactly one of the two CE2 center intervals contains a V-gap.

Then the seven roles cannot cover the hexagon perimeter.

This theorem does not claim the full CE2 package. The no-gap case is proved
in [`4014_setup_and_reduction.md`](4014_setup_and_reduction.md), Section 6.
The two-gap case is outside this theorem and is proved separately in
[`401e_CE2_two_gap_completion.md`](401e_CE2_two_gap_completion.md).

## 1. Boundary reduction

Use the exact CE2 normalization from
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md):

$$
T_C\cap e_{5,0}=[x,U],
\qquad
T_C\cap e_{0,1}=[y,v],
$$

where both edges are parameterized from $V_0$. Assume that the interval on
$e_{0,1}$ contains the unique V-gap and the interval on $e_{5,0}$ contains
no V-gap. Write the actual adjacent reaches of $T_0$ as $a_0,b_0$, the
$e_{5,0}$ reach from $V_5$ as $b_5$, and the $e_{0,1}$ reach from $V_1$ as
$a_1$. Full boundary coverage and the active gap give

$$
y\le b_0<1-a_1\le v.
$$

The absence of a gap on $e_{5,0}$ gives

$$
a_0+b_5\ge1.
$$

Since $N_+=0$,

$$
a_0+b_0\le1.
$$

Consequently

$$
b_5\ge1-a_0\ge b_0\ge y,
\qquad
a_1\ge1-v.
$$

By Vd0 boundary and radial locality, only the endpoint roles can contribute
positive boundary length on the adjacent edges, and each such row must meet
its own complementary radial demand. Let $c_i=1-d_i$ be the exact demands
from `2106`, and let $\widehat B$ be the capped safe map proved in
[`2011_capped_demand_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md).
The outgoing boundary
reaches of $T_5$ and $T_1$ are therefore at most

$$
B_5:=\widehat B_{c_5}(y),
\qquad
B_1:=\widehat B_{c_1}(1-v).
$$

For $T_5$, reflect the local picture as in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md)
so that its $e_{5,0}$
reach is the input coordinate and its $e_{4,5}$ reach is the outgoing
coordinate. The map is symmetric under this reflection.

If $B_5+B_1<1$, the part of the perimeter left to $T_2,T_3,T_4$ has length

$$
(1-B_1)+1+1+(1-B_5)=4-(B_5+B_1)>3,
$$

contradicting their three row caps. Thus it remains to prove the displayed
strict inequality.

## 2. Virtual side-model coordinates

Put

$$
S_0=x+y,
\qquad
D=\sqrt{x^2+xy+y^2},
$$

and define

$$
R=\frac{x}{S_0},
\qquad
s=y,
\qquad
u=1-v,
\qquad
\rho=\sqrt{1-R+R^2}=\frac{D}{S_0},
$$

$$
\eta=1-\rho,
\qquad
\delta=\frac{R}{1+\rho},
\qquad
w=v-y=1-u-s.
$$

The exact radial formula for $c_1$ gives

$$
c_1
=1-\frac{vS_0-y}{x}
=\frac{S_0(1-v)}x
=\frac uR.
$$

The coupling equation

$$
(U+v)S_0-xy=D
$$

gives

$$
\begin{aligned}
c_5
&=1-\frac{US_0-x}{y}
=\frac{S_0(1-U)}y\\
&=\frac{S_0v+S_0-D-xy}{y}
=\frac{1-u+\eta-Rs}{1-R}.
\end{aligned}
$$

Set

$$
\gamma_5=1-c_5.
$$

Then

$$
\gamma_5
=u-\delta-\frac{R}{1-R}w.
$$

The strict center inequalities in `2106` give

$$
0<R<1,
\qquad
0<u<R,
\qquad
w>0,
\qquad
\gamma_5>0.
$$

Thus the one-gap CE2 objective is exactly the same algebraic side-model
objective used in [`401b_CE1_exact_branch_completion.md`](401b_CE1_exact_branch_completion.md), but without the final CE1 inequality excluding a
second boundary overlap.

## 3. Branch results that do not use the CE1-only inequality

The calculations in `401b`, Sections 3--7 use only the conditions in the
last display, the center identity, and the exact cap and component selectors.
They do not use $s\ge1-R$ or $s>\rho-u$. They therefore remain valid here.
In particular:

1. If the right label is $L$ or $T_-$, then

   $$
   B_1\le X,
   \qquad
   X:=\rho-u.
   $$

2. Left $T_-$ and left $L$ against right $T_+^{hi}$ or right Full satisfy
   $B_5+B_1<1$.
3. Left Full against right $T_+^{hi}$ or right Full is impossible.
4. Left $T_+^{hi}$ against right Full is impossible.

If both labels are in $\{L,T_-\}$, then directly

$$
B_5+B_1\le s+u=1-w<1.
$$

The two cases needing a replacement for the CE1-only inequality are handled
next.

## 4. Right low label when $s\le X$

The case $s>X$ is immediate: $B_1\le X<s$, while left Full has
$B_5=1-s$ and left $T_+^{hi}$ has $B_5<1-s$. Low left labels were already
handled above.

Assume from now on that

$$
s\le X=\rho-u.
$$

### 4.1. Endpoint calculation

Set

$$
c_X:=c_5(X)=X+2\delta
$$

and

$$
f(c,z)=c^4-c^2+zc-z^2.
$$

We claim

$$
c_X>\frac{\sqrt3}{2},
\qquad
f(c_X,X)>0.
$$

For fixed $R$, both $X=\rho-u$ and $c_X=X+2\delta$ decrease with $u$. At
the limiting endpoint $u=R$, put $\kappa=\delta$. Then

$$
X_0=\frac{1-2\kappa}{1+\kappa},
\qquad
c_0=\frac{1+2\kappa^2}{1+\kappa}.
$$

The inequality $c_0>\sqrt3/2$ follows after squaring from

$$
16\kappa^4+13\kappa^2-6\kappa+1>0;
$$

the quadratic $13\kappa^2-6\kappa+1$ is positive and the quartic term is
nonnegative. Direct substitution gives

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

because $X<c_X$ and $c_X\ge c_0>\sqrt3/2$. Hence the claim holds for
$u<R$.

Define

$$
\ell(c)=\frac c2\left(1-\sqrt{4c^2-3}\right).
$$

The polynomial

$$
H_c(z)=z^2-cz+c^2-c^4
$$

has roots $\ell(c)$ and $c-\ell(c)$. Since

$$
H_{c_X}(X)=-f(c_X,X)<0,
$$

we have

$$
\ell(c_X)<X<c_X-\ell(c_X).
$$

In particular,

$$
\ell(c_X)<c_X-X=2\delta.
$$

Since $c_5$ is strictly decreasing in $s$, the assumptions $s\le X$ and
$c_5(s)<1$ imply $c_X\le c_5(s)<1$. Therefore

$$
2\delta=c_X-X<1-X.
$$

### 4.2. Staying on the selected Cell-L component

For $\sqrt3/2\le c\le1$, write

$$
c=h(z):=\sqrt{1-z+z^2},
\qquad
0\le z\le\frac12.
$$

Then $\ell(c)=zh(z)$. Since the actual value satisfies

$$
c_5(s)\in[c_X,1)
$$

and $h$ decreases on $[0,1/2]$, its parameter satisfies

$$
0<z\le z_X<\frac12.
$$

Along the center line, the input corresponding to $z$
is

$$
s(z)=s_0+\frac{1-R}{R}(1-h(z)),
\qquad
s_0:=\frac{R-u+\eta}{R}>0.
$$

The functions $s(z)$ and $zh(z)$ are strictly increasing, whereas the
$q=0$ transition input

$$
a_{tr}(z)=(1-z)h(z)
$$

is strictly decreasing. Let $z_X$ correspond to $c_X$. The endpoint
inequality above says

$$
s(z_X)=X<c_X-\ell(c_X)=a_{tr}(z_X).
$$

Hence for every $0\le z\le z_X$,

$$
s(z)<a_{tr}(z).
$$

We also verify that the smaller coordinate in the Cell-L equation is really
$b(z)=zh(z)$. Put

$$
\phi(z)=s(z)-zh(z),
\qquad
k=\frac{1-R}{R}.
$$

At $z=0$, $\phi(0)=s_0>0$, while at $z_X$ the endpoint root ordering gives
$\phi(z_X)=X-\ell(c_X)>0$. Moreover

$$
\phi'(z)=\frac{(k+z)(1-2z)}{2h(z)}-h(z).
$$

If $k\le2$, then

$$
(k+z)(1-2z)
\le(2+z)(1-2z)
\le2h(z)^2,
$$

so $\phi'\le0$. If $k>2$, then $\phi'=0$ is equivalent to

$$
k=K(z):=\frac{2-3z+4z^2}{1-2z},
$$

and

$$
K'(z)=\frac{1+8z-8z^2}{(1-2z)^2}>0.
$$

Thus $\phi$ first increases and then decreases, so its minimum is at an
endpoint. In both cases

$$
b(z)<s(z).
$$

The exact selector factorization from `401b` is

$$
\frac{q}{h(z)^2}
=
\left(\frac{s(z)}{h(z)}-(1-z)\right)
P_z\left(\frac{s(z)}{h(z)}\right),
$$

where $P_z$ has nonnegative coefficients and is positive at every
nondegenerate point. Since $s(z)<a_{tr}(z)$, this gives $q<0$. Therefore the
candidate lies on the selected Cell-L frontier. To make maximality explicit,
the endpoint bounds give

$$
s+b
\le X+\ell(c_X)<1,
$$

and hence

$$
d=s^2+sb+b^2<(s+b)^2<1.
$$

Thus all Cell-L conditions hold with $m=b$, $F_L=0$, and $q<0$. Moreover

$$
\frac{\partial F_L}{\partial b}=c-2b=c(1-2z)>0,
$$

so every immediate increase of $b$ is infeasible. The interval-fiber theorem
in `2007` rules out any later re-entry. Therefore the uncapped maximum is
$zh(z)$. If the cap $b\le1-s$ cuts earlier, the capped safe value is only
smaller. Consequently

$$
B_5\le z h(z)\le z_Xh(z_X)=\ell(c_X)<1-X.
$$

Together with $B_1\le X$, this proves

$$
B_5+B_1<1.
$$

## 5. Excluding the high/high pair

For $0\le z\le1/2$, let $c_L(z)$ be the unique root in
$[\sqrt3/2,1]$ of

$$
f(c,z)=c^4-c^2+zc-z^2=0.
$$

As proved in `401b`, $c_L$ is strictly convex. A realized left
$T_+^{hi}$ point requires

$$
s<\frac12,
\qquad
c_5(s)\le c_L(s).
$$

Set

$$
s_0=\frac{R-u+\eta}{R}.
$$

A realized left high label gives

$$
0<s_0<s<\frac12,
$$

because $u<R$ and $\eta>0$, while $\gamma_5>0$ gives $s>s_0$.
Thus $c_L(s_0)$ lies in its stated domain, and $c_5(s_0)=1$. Define

$$
g(z)=c_5(z)-c_L(z).
$$

The function $g$ is concave. At the left endpoint,

$$
g(s_0)=1-c_L(s_0)>0.
$$

For the right $T_+^{hi}$ label, `401b`, Section 5 proves the exact bound

$$
u\le\min\{R\rho,\rho/2\}.
$$

If $0<R\le1/2$, then

$$
c_5(1/2)
\ge
\frac{2-(1+R)\rho-R/2}{1-R}
>\frac78.
$$

The last inequality is equivalent to

$$
9+3R>8(1+R)\rho.
$$

After squaring, the difference is

$$
P(R)=17-10R+9R^2-64R^3-64R^4.
$$

On $[0,1/2]$,

$$
P'(R)=-10+18R-192R^2-256R^3<0,
$$

and $P(1/2)=9/4>0$.

If $1/2\le R<1$, then

$$
c_5(1/2)
\ge
\frac{4-3\rho-R}{2(1-R)}
>\frac78.
$$

The last inequality is equivalent to $3+R>4\rho$, and

$$
(3+R)^2-16\rho^2=(1-R)(15R-7)>0.
$$

Finally,

$$
f(7/8,1/2)=\frac{33}{4096}>0,
$$

and $f$ is strictly increasing in $c$ on $[\sqrt3/2,1]$. Hence

$$
c_L(1/2)<7/8<c_5(1/2),
$$

so $g(1/2)>0$. Concavity gives $g(s)>0$ throughout
$[s_0,1/2]$, contradicting the required high-label ordering. Thus
$(T_+^{hi},T_+^{hi})$ is impossible.

## 6. Assembly

The exact capped safe labels are

$$
L,
\qquad
T_-,
\qquad
T_+^{hi},
\qquad
\mathrm{Full}.
$$

Both-low is immediate. Sections 3--4 cover every pair with a right low
label. The reused `401b` calculations cover left low versus right high or
Full, left Full versus right high or Full, and left high versus right Full.
Section 5 excludes high/high. Therefore

$$
\widehat B_{c_5}(y)+\widehat B_{c_1}(1-v)<1.
$$

Reflection proves the case in which the interval on $e_{5,0}$ is the unique
active gap.

$$
\Box
$$
