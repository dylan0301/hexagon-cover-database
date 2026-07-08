# CE2, $N_+=1$, $T_0$ Supercritical And Adjacent $T_1$ Vd1/Vd2

Status: Proven

This file proves the adjacent remaining placement in the
[`4140`](4140_CE2_Nplus1_exactly_one_Vd1_Vd2_TODO.md) branch:

$$
T_C\text{ is CE2},\qquad T_0\text{ is the unique supercritical row},
\qquad T_1\text{ is the unique Vd1/Vd2 row}.
$$

The reflected placement with $T_5$ Vd1/Vd2 is identical.

The proof uses the local type conventions from
[`../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md),
the local boundary coordinates from
[`../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md`](../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md),
the admissible-set radial envelope from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md),
and the CE2 interval-pair model from
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md).

## Statement

Assume a reduced 414X cover candidate satisfies

$$
T_C\text{ is CE2},\qquad T_C\cap\{M_0,\dots,M_5\}=\{M_0\},
$$

$$
T_0\text{ is the unique supercritical row},\qquad T_1\text{ is the unique Vd1/Vd2 row},
$$

and

$$
T_2,T_3,T_4,T_5
$$

are Vd0 rows satisfying

$$
a_i+b_i\le1,\qquad i=2,3,4,5.
$$

Then the seven role triangles cannot cover the hexagon perimeter together with
the two diagonal targets $r_1$ and $r_2$.  In particular, the adjacent
$T_0$-supercritical, $T_1$-Vd1/Vd2 placement is impossible in the 414X branch.

## CE2 variables and diagonal lengths

Write the normalized CE2 boundary intervals as

$$
T_C\cap e_{5,0}=[x,u],\qquad T_C\cap e_{0,1}=[y,v].
$$

Set

$$
S=x+y,\qquad D=\sqrt{x^2+xy+y^2}.
$$

The CE2 parameterization gives

$$
0<x<u<1,\qquad 0<y<v<1,
$$

$$
(u+v)S-xy=D,
$$

$$
uS\ge x,\qquad vS\ge y,
$$

and

$$
uS<x+\frac y2,\qquad vS<y+\frac x2.
$$

Set

$$
E:=vS-y.
$$

Substitution into the CE2 half-plane model gives the center-triangle lengths on
$r_1$ and $r_2$, measured from $O$ toward the corresponding vertex:

$$
d_1^C=\frac{E}{x},\qquad d_2^C=\frac{E}{S}.
$$

Thus the uncovered vertex-side demands are

$$
q_1=1-d_1^C,\qquad q_2=1-d_2^C.
$$

## Boundary demands

Let $(a_0,b_0)$ be the boundary coordinates of $T_0$.  Since $T_0$ is
supercritical,

$$
a_0+b_0>1.
$$

The adjacent endpoint distance condition gives

$$
a_0^2+a_0b_0+b_0^2\le1.
$$

On $e_{0,1}$, coverage by $T_0$, $T_C$, and $T_1$ forces

$$
a_1\ge A,
$$

where

$$
A=
\begin{cases}
1-b_0,& b_0<y,\\[2mm]
\max(0,1-\max(b_0,v)),& b_0\ge y.
\end{cases}
$$

On $e_{5,0}$, coverage by $T_0$, $T_C$, and $T_5$ forces

$$
b_5\ge H,
$$

where

$$
H=
\begin{cases}
1-a_0,& a_0<x,\\[2mm]
\max(0,1-\max(a_0,u)),& a_0\ge x.
\end{cases}
$$

Because $u<1$ and $T_0$ is strictly supercritical, $H>0$ in a genuine
candidate.

For ordinary nonsupercritical Vd0 rows, $a_i+b_i\le1$.  Together with
$b_i+a_{i+1}\ge1$, this propagates the $b_5$ lower bound backward:

$$
b_5\ge H\Longrightarrow b_4\ge H\Longrightarrow b_3\ge H
\Longrightarrow b_2\ge H\Longrightarrow b_1\ge H.
$$

Thus

$$
\boxed{a_1\ge A,\qquad b_1\ge H.}
$$

## Local Vd1/Vd2 adjacent-ray bound

Normalize $T_1$ at $V_1$ and choose a touched adjacent ray.  In local
coordinates $(X,Y)$ there is $t>0$ and

$$
d=\sqrt{t^2+t+1}
$$

such that the corner-side normal form is

$$
X-(t+1)Y\le a,
$$

$$
tY-(t+1)X\le tb,
$$

and

$$
tX+Y\le d-a-tb.
$$

Here $a=a_1$ and $b=b_1$ after choosing the side corresponding to the touched
adjacent ray.

If the outgoing adjacent ray has positive-length intersection, then

$$
(t+1)a+tb<(t+1)(d-1)-t^2.
$$

Since $(t+1)a+tb\ge t(a+b)$,

$$
a+b<\frac{(t+1)(d-1)-t^2}{t}.
$$

The right side is $<1/2$ because this is equivalent to

$$
(t+1)d<t^2+\frac{3t}{2}+1,
$$

and

$$
\left(t^2+\frac{3t}{2}+1\right)^2-(t+1)^2(t^2+t+1)=\frac{t^2}{4}>0.
$$

The incoming adjacent ray gives the reflected inequality

$$
ta+t(t+1)b<(t+1)(d-t)-1.
$$

Since the left side is at least $t(a+b)$, the same squared comparison gives
$a+b<1/2$.  Hence every Vd1/Vd2 row satisfies

$$
\boxed{a_1+b_1<\frac12.}
$$

Combining with $a_1\ge A$ and $b_1\ge H$ gives

$$
\boxed{A+H<\frac12.}
$$

## Local radial-envelope bound for $T_2$

Let

$$
p=\frac12+A,\qquad h=H.
$$

Then $p\ge1/2$, $h\ge0$, $p+h<1$, and $p\ge h$.  Let
$c_{\max}(p,h)$ be the admissible-set radial envelope under lower edge bounds
$p,h$.  We prove

$$
\boxed{c_{\max}(p,h)\le1-\frac h3.}
$$

Set $c_0=1-h/3$ and work in the ordered half $h\le p$ of the admissible-set
formulas.

In the $q<0$ branch, the boundary value is the first positive root of

$$
P(c)=c^4-c^2+hc-h^2.
$$

If $q<0$, then $h<3/8$; otherwise $p\ge1/2$ gives

$$
q=s^4-s^2+ph\ge\left(h+\frac12\right)^4-\left(h+\frac12\right)^2+\frac h2\ge0.
$$

At $c_0$,

$$
P(c_0)=\frac{h}{81}\left(h^3-12h^2-63h+27\right)>0
$$

for $0<h\le3/8$, since the cubic is decreasing there and equals $891/512$ at
$3/8$.  Hence the first positive root is $<c_0$, so $c_{\max}<c_0$.  The case
$h=0$ is trivial.

In the $q\ge0$ branch, the boundary inequality is

$$
(s^2-1)c^2+pc-p^2\le0,\qquad s=p+h.
$$

At $c_0=1-h/3$ this expression is

$$
G=\frac{2h^3+2h^2p-12h^2-12hp+15h+9}{9}.
$$

For fixed $h\in[0,1/2]$, $G$ is linear and decreasing in $p$, so its minimum
for $1/2\le p\le1-h$ occurs at $p=1-h$.  There

$$
G=\frac{2h(1-h)}3\ge0.
$$

Thus $c_0$ lies at or beyond the first boundary root, and

$$
\boxed{c_{\max}\left(\frac12+A,H\right)\le1-\frac H3.}
$$

## Outer ratio target

We prove

$$
\boxed{d_2^C<\frac H3.}
$$

### Branch I: $H=1-u$

In this branch $a_0\ge x$ and $a_0\le u$.  Define

$$
K:=x+2y-xy-D.
$$

Since

$$
d_2^C=\frac{D+xy-uS-y}{S}
$$

and $D+xy-y=S-K$,

$$
d_2^C=1-u-\frac KS=H-\frac KS.
$$

Thus

$$
\frac{d_2^C}{H}=1-\frac{K}{SH}.
$$

Let

$$
b_\circ(x)=\frac{-x+\sqrt{4-3x^2}}2,\qquad h(x)=b_\circ(x)-\frac12.
$$

We claim

$$
H\le \min\left(\frac yS,h(x)\right).
$$

The inequality $H\le y/S$ follows from $H=1-u$ and $uS\ge x$.  To prove
$H\le h(x)$, use $A+H<1/2$.  If the $e_{0,1}$ tail is produced by $b_0$, then
$b_0>1/2+H$; since $a_0\ge x$ and $a_0^2+a_0b_0+b_0^2\le1$, we have
$b_0\le b_\circ(x)$, hence $H<h(x)$.  If the tail is produced by $v$, then
$v>1/2+H$; since $T_C$ contains boundary points at parameters $x$ and $v$,
$x^2+xv+v^2\le1$, so $v\le b_\circ(x)$ and again $H<h(x)$.

Set

$$
m=\min\left(\frac yS,h(x)\right).
$$

We prove

$$
\frac{K}{Sm}>\frac23.
$$

If $y/S\le h(x)$, set $r=y/x$.  Then $r\le h(x)/(1-h(x))$ and $r\le1$.  Since

$$
\sqrt{1+r+r^2}\le1+\frac r2+\frac{r^2}{2},
$$

we obtain

$$
\frac Ky\ge \frac32-x-\frac r2
\ge \frac32-x-\frac{h(x)}{2(1-h(x))}.
$$

Writing $b=h(x)+1/2=b_\circ(x)$, the function

$$
F(b)=\frac{-b+\sqrt{4-3b^2}}2+\frac{b-1/2}{3-2b}
$$

is decreasing on $1/2\le b\le1$; differentiating gives

$$
F'(b)=\frac{2}{(3-2b)^2}-\frac12-\frac{3b}{2\sqrt{4-3b^2}}<0.
$$

After clearing positive denominators this last inequality reduces to a
polynomial inequality in $1-b$ and $2b-1$ with nonnegative coefficients.  Thus

$$
F(b)\le F\left(\frac12\right)=\frac{\sqrt{13}-1}{4},
$$

and therefore

$$
\frac Ky\ge\frac{7-\sqrt{13}}4>\frac23.
$$

In this subcase $Sm=y$, so $K/(Sm)>2/3$.

If $h(x)\le y/S$, then $m=h(x)$.  For fixed $x$, the function

$$
g(y)=\frac{x+2y-xy-\sqrt{x^2+xy+y^2}}{x+y}
$$

is increasing in $y$, because

$$
g'(y)=\frac{x(2(1-x)D+x-y)}{2S^2D}>0.
$$

The positivity is immediate when $y\le x$; when $y>x$, use $D\ge y$ to get
$2(1-x)D+x-y\ge x+(1-2x)y>0$.  Let $y_0$ be defined by

$$
\frac{y_0}{x+y_0}=h(x).
$$

Since $h(x)\le y/S$, $y\ge y_0$, so

$$
\frac{K(x,y)}{S h(x)}\ge\frac{K(x,y_0)}{(x+y_0)h(x)}=\frac{K(x,y_0)}{y_0}>rac23,
$$

where the last inequality is the boundary value from the previous subcase.
Thus $K/(Sm)>2/3$ in all cases.

Since $H\le m$,

$$
\frac{K}{SH}\ge\frac{K}{Sm}>\frac23.
$$

Therefore

$$
\frac{d_2^C}{H}=1-\frac{K}{SH}<\frac13,
$$

so $d_2^C<H/3$ in Branch I.

### Branch II: $H=1-a_0$

Now $a_0=1-H$.  The $e_{0,1}$ demand $A$ cannot be produced by $b_0$: if
$A=1-b_0$, then

$$
A+H=2-a_0-b_0<\frac12,
$$

so $a_0+b_0>3/2$, contradicting

$$
a_0+b_0\le\frac2{\sqrt3}
$$

from $a_0^2+a_0b_0+b_0^2\le1$.  Hence $A=1-v$ and

$$
v>\frac12+H.
$$

For $A$ to be determined by $v$, $T_0$ must reach the start $y$ of the CE2
interval on $e_{0,1}$, so

$$
b_0\ge y.
$$

Using $a_0=1-H$ and the disk condition gives

$$
(1-H)^2+(1-H)y+y^2\le1.
$$

Equivalently,

$$
H^2-(2+y)H+y+y^2\le0.
$$

Let

$$
L(y)=\frac{2+y-\sqrt{4-3y^2}}2.
$$

Since $H<1/2$, this quadratic inequality gives

$$
H\ge L(y).
$$

The CE2 inequality $uS\ge x$ gives

$$
v=\frac{D+xy}{S}-u\le\frac{D+xy-x}{S}.
$$

Since $v>1/2+H\ge1/2+L(y)$, we have

$$
\frac{D+xy-x}{S}>\frac12+L(y).
$$

We use the following analytic lemma.

### Analytic lemma

Let $0<y<1$ and

$$
L=\frac{2+y-\sqrt{4-3y^2}}2.
$$

Let $x>0$, $S=x+y$, and $D=\sqrt{x^2+xy+y^2}$.  If

$$
\frac{D+xy-x}{S}>\frac12+L,
$$

then

$$
\frac{D+xy-x-y}{S}<\frac L3.
$$

Set

$$
r=\frac xy,\qquad R=\sqrt{r^2+r+1},\qquad r_0=\frac{3-4L}{3+4L}.
$$

Then

$$
\frac{D+xy-x}{S}=\frac{R-r(1-y)}{r+1},
\qquad
\frac{D+xy-x-y}{S}=\frac{R-r(1-y)-1}{r+1}.
$$

If $0<r\le r_0$, then

$$
R\le1+\frac r2+\frac{r^2}{2},
$$

so

$$
\frac{R-r(1-y)-1}{r+1}\le
\frac{r(y-1/2+r/2)}{r+1}.
$$

The right side is convex in $r$ on $[0,r_0]$, so its maximum is at an endpoint.
At $r=0$ it is $0$.  At $r=r_0$,

$$
\frac L3-\frac{r_0(y-1/2+r_0/2)}{r_0+1}
=\frac{N(L)}{6(3+4L)},
$$

where

$$
N(L)=16L^2y-8L^2+18L-9y,
\qquad
 y=\frac{L-1+\sqrt{1+6L-3L^2}}2.
$$

Writing $s=\sqrt{1+6L-3L^2}$, one has $N(0)=0$ and

$$
2sN'(L)=s(48L^2-64L+27)-144L^3+240L^2+59L-27.
$$

On $0<L<1/2$, $48L^2-64L+27>0$ and

$$
s\ge1+3L-6L^2,
$$

so

$$
2sN'(L)\ge2L(-144L^3+192L^2-33L+38)>0.
$$

Thus $N(L)>0$, proving the lemma when $r\le r_0$.

If $r\ge r_0$, then

$$
\frac{R-r(1-y)}{r+1}\le\frac12+L.
$$

After squaring the positive equivalent inequality, the squared difference is a
convex quadratic in $r$.  At $r=r_0$, after substituting

$$
y=\frac{L-1+\sqrt{1+6L-3L^2}}2,
$$

its value and derivative are bounded below by

$$
2(16L^4+8L^3+69L^2-48L+9)>0
$$

and

$$
2(8L^3+14L^2-20L+9)>0.
$$

Therefore the squared difference is positive for all $r\ge r_0$, so the
hypothesis of the lemma cannot hold in this range.  The analytic lemma follows.

Applying it gives

$$
\frac{D+xy-x-y}{S}<\frac{L(y)}3.
$$

Since

$$
d_2^C=v-\frac yS\le\frac{D+xy-x-y}{S},
$$

we get

$$
d_2^C<\frac{L(y)}3\le\frac H3.
$$

Thus $d_2^C<H/3$ also in Branch II.  The outer ratio target is proved.

## Excluding $r_2$ coverage

In vertex-to-center coordinates, $r_2$ can be covered only by

$$
[0,c_2]\quad\text{from }T_2,
$$

$$
[\ell_2,u_2]\quad\text{from }T_1\text{ if }T_1\text{ touches }r_2,
$$

and

$$
[q_2,1]\quad\text{from }T_C,
\qquad q_2=1-d_2^C.
$$

Therefore full coverage of $r_2$ requires either $c_2\ge q_2$, or else
$T_1$ bridges to the center interval, in particular $u_2\ge q_2$.

If $T_1$ bridges, then in the corner normal form

$$
u_2=\frac{d-a_1-tb_1-1}{t}\ge q_2=1-d_2^C.
$$

Thus

$$
a_1+tb_1\le d-1-t+td_2^C.
$$

Since $d<t+1$, this implies

$$
a_1+tb_1<td_2^C t.
$$

As $b_1\ge H$ and $a_1\ge0$, this gives $H<d_2^C$, contradicting
$d_2^C<H/3$.  Hence $T_1$ cannot bridge.

If $T_2$ alone reaches the CE2 center interval, then $c_2\ge q_2$.  The edge
$e_{1,2}$ gives

$$
a_2\ge1-b_1.
$$

Since $a_1+b_1<1/2$ and $a_1\ge A$,

$$
a_2>\frac12+A.
$$

Backward boundary propagation gives $b_2\ge H$.  By monotonicity of the
admissible-set radial envelope,

$$
c_2\le c_{\max}\left(\frac12+A,H\right)\le1-\frac H3.
$$

The outer ratio target gives

$$
1-\frac H3<1-d_2^C=q_2.
$$

Thus $c_2<q_2$, a contradiction.  Both possible ways to cover $r_2$ are
impossible, proving the adjacent obstruction.

## Boundary cases

The contradiction is strict.  Vd1/Vd2 requires positive-length adjacent-ray
intersection, giving $a_1+b_1<1/2$.  CE2 has strict positive boundary intervals
and $H>0$ for a genuine supercritical $T_0$ branch.  Endpoint-only adjacent-ray
contacts do not count as Vd1/Vd2 positive length.

## Numerical check

Independent numerical checks sampled CE2 parameters $(x,u,y,v)$ using

$$
(u+v)(x+y)-xy=\sqrt{x^2+xy+y^2}
$$

and the CE2 inequalities, sampled supercritical $(a_0,b_0)$ satisfying

$$
a_0+b_0>1,
\qquad
 a_0^2+a_0b_0+b_0^2\le1,
$$

and computed $A,H,d_2^C$.  The checks tested

$$
A+H<\frac12\Longrightarrow d_2^C<\frac H3,
$$

and

$$
c_{\max}\left(\frac12+A,H\right)<1-d_2^C.
$$

No violation was found.  The numerical check is not used as an input to the
proof.
