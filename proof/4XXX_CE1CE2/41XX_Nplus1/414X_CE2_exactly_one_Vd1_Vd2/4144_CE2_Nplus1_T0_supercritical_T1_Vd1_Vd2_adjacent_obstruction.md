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
T_C\text{ is CE2},
\qquad
T_C\cap\{M_0,\dots,M_5\}=\{M_0\},
$$

$$
T_0\text{ is the unique supercritical row},
\qquad
T_1\text{ is the unique Vd1/Vd2 row},
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

By reflection across the $OV_0$ axis, the same obstruction applies to the
placement

$$
T_0\text{ supercritical},\qquad T_5\text{ Vd1/Vd2}.
$$

## CE2 variables

Write the normalized CE2 boundary intervals as

$$
T_C\cap e_{5,0}=[x,u],
\qquad
T_C\cap e_{0,1}=[y,v].
$$

Set

$$
S=x+y,
\qquad
D=\sqrt{x^2+xy+y^2}.
$$

The CE2 parameterization gives

$$
0<x<u<1,
\qquad
0<y<v<1,
$$

$$
(u+v)S-xy=D,
$$

$$
uS\ge x,
\qquad
vS\ge y,
$$

and

$$
uS<x+\frac y2,
\qquad
vS<y+\frac x2.
$$

Set

$$
E:=vS-y.
$$

Substitution into the CE2 half-plane model gives the center-triangle lengths on
$r_1$ and $r_2$, measured from $O$ toward the corresponding vertex:

$$
d_1^C=\frac{E}{x},
\qquad
d_2^C=\frac{E}{S}.
$$

Equivalently, in the coordinate measured from the vertex toward $O$, the
uncovered vertex-side demands are

$$
q_1=1-d_1^C,
\qquad
q_2=1-d_2^C.
$$

Indeed, on $r_2$ the active CE2 slack is $E-qS$, so the center-side exit
coordinate is $E/S$.

## Boundary demands from $T_0$ and $T_C$

Let $(a_0,b_0)$ be the boundary coordinates of $T_0$.  Since $T_0$ is
supercritical,

$$
a_0+b_0>1.
$$

The unit-diameter condition for the two adjacent boundary endpoints gives

$$
a_0^2+a_0b_0+b_0^2\le1.
$$

On $e_{0,1}$, the cover contributions are

$$
[0,b_0]\quad\text{from }T_0,
\qquad
[y,v]\quad\text{from }T_C,
\qquad
[1-a_1,1]\quad\text{from }T_1.
$$

Therefore $T_1$ must satisfy

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

On $e_{5,0}$, the cover contributions are

$$
[0,a_0]\quad\text{from }T_0,
\qquad
[x,u]\quad\text{from }T_C,
$$

and a $V_5$-side contribution from $T_5$.  Hence

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

Since $u<1$ and $T_0$ is strictly supercritical, $H>0$ in every genuine
candidate.

For ordinary nonsupercritical Vd0 rows,

$$
a_i+b_i\le1.
$$

Together with the boundary relation

$$
b_i+a_{i+1}\ge1,
$$

this propagates the lower bound on $b_5$ backward through the Vd0 chain:

$$
b_5\ge H\Longrightarrow b_4\ge H\Longrightarrow b_3\ge H
\Longrightarrow b_2\ge H\Longrightarrow b_1\ge H.
$$

Thus every candidate satisfies

$$
\boxed{a_1\ge A,
\qquad
b_1\ge H.}
$$

## Local Vd1/Vd2 adjacent-ray bound

Let $T_1$ be normalized at $V_1$.  For the adjacent ray touched by $T_1$, the
standard corner-side normal form has a parameter $t>0$ and

$$
d=\sqrt{t^2+t+1}
$$

such that, in local coordinates $(X,Y)$ at $V_1$,

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
adjacent ray.  This is the same unit-equilateral corner normal form used for
Vd2 rows; the Vd1 case is obtained by allowing only one of the two adjacent-ray
intersections to have positive length.

If the outgoing adjacent ray has positive-length intersection, then its lower
endpoint is strictly smaller than its upper endpoint, giving

$$
(t+1)a+tb<(t+1)(d-1)-t^2.
$$

Since

$$
(t+1)a+tb\ge t(a+b),
$$

we get

$$
a+b<\frac{(t+1)(d-1)-t^2}{t}.
$$

The right-hand side is strictly less than $1/2$.  Indeed, this is equivalent
to

$$
(t+1)d<t^2+\frac{3t}{2}+1,
$$

and after squaring the positive sides the difference is

$$
\left(t^2+\frac{3t}{2}+1\right)^2-(t+1)^2(t^2+t+1)=\frac{t^2}{4}>0.
$$

The incoming adjacent ray gives the reflected inequality

$$
ta+t(t+1)b<(t+1)(d-t)-1.
$$

Since the left side is at least $t(a+b)$, it is enough to prove

$$
(t+1)(d-t)-1<\frac t2.
$$

This is again equivalent to

$$
(t+1)d<t^2+\frac{3t}{2}+1,
$$

already proved.  Therefore positive-length intersection with either adjacent
ray implies

$$
\boxed{a_1+b_1<\frac12.}
$$

Because $T_1$ is Vd1 or Vd2, it has at least one positive-length adjacent-ray
intersection.  Combining this with $a_1\ge A$ and $b_1\ge H$ gives

$$
\boxed{A+H<\frac12.}
$$

## Local radial-envelope bound for $T_2$

The only unresolved way to cover $r_2$ after excluding a bridge by $T_1$ is for
$T_2$ to reach the CE2 center interval from the $V_2$ side.  We first record a
local envelope bound for that possibility.

Let

$$
p=\frac12+A,
\qquad
h=H.
$$

Since $A+H<1/2$,

$$
p\ge\frac12,
\qquad
h\ge0,
\qquad
p+h<1,
\qquad
p\ge h.
$$

Let $c_{\max}(p,h)$ be the admissible-set radial envelope under lower edge
bounds $p,h$.  We prove

$$
\boxed{c_{\max}(p,h)\le1-\frac h3.}
$$

Set

$$
c_0=1-\frac h3.
$$

Work in the ordered half $h\le p$ of the admissible-set formulas.

### Branch $q<0$

In the $q<0$ branch, the boundary value of $c_{\max}$ is the first positive
root of

$$
P(c)=c^4-c^2+hc-h^2.
$$

If $q<0$, then $h<3/8$.  For if $h\ge3/8$, then $p\ge1/2$ gives
$s=p+h\ge7/8$, and

$$
q=s^4-s^2+ph\ge \left(h+\frac12\right)^4-\left(h+\frac12\right)^2+\frac h2
\ge0,
$$

where the last expression is increasing for $h>0$ and is already positive at
$h=3/8$.

Evaluate $P$ at $c_0$:

$$
P(c_0)=\frac{h}{81}\left(h^3-12h^2-63h+27\right).
$$

On $0\le h\le3/8$, the cubic in parentheses is decreasing and its value at
$3/8$ is $891/512>0$.  Hence $P(c_0)>0$ whenever $h>0$.  Since $P(0)=-h^2<0$
and the admissible branch ends at the first positive root, this gives

$$
c_{\max}(p,h)<c_0=1-\frac h3.
$$

For $h=0$ the desired inequality is $c_{\max}\le1$, which is immediate.

### Branch $q\ge0$

In the $q\ge0$ branch, the boundary inequality is

$$
(s^2-1)c^2+pc-p^2\le0,
\qquad s=p+h.
$$

Evaluate at $c_0=1-h/3$:

$$
G=(s^2-1)c_0^2+pc_0-p^2
=rac{2h^3+2h^2p-12h^2-12hp+15h+9}{9}.
$$

For fixed $h\in[0,1/2]$, this expression is linear and decreasing in $p$,
because the coefficient of $p$ is $2h^2-12h\le0$.  Therefore its minimum over

$$
\frac12\le p\le1-h
$$

occurs at $p=1-h$.  At this endpoint,

$$
G=\frac{2h(1-h)}3\ge0.
$$

Thus $c_0$ lies at or beyond the first boundary root, and

$$
c_{\max}(p,h)\le c_0=1-\frac h3.
$$

Combining the two branches proves

$$
\boxed{c_{\max}\left(\frac12+A,H\right)\le1-\frac H3.}
$$

## Outer ratio target

We prove

$$
\boxed{d_2^C<\frac H3.}
$$

The proof splits according to the active definition of $H$.

### Branch I: $H=1-u$

In this branch $a_0\ge x$ and $a_0\le u$.  Define

$$
K:=x+2y-xy-D.
$$

Using

$$
d_2^C=\frac{D+xy-uS-y}{S},
$$

and

$$
D+xy-y=S-K,
$$

we get

$$
d_2^C=1-u-\frac KS=H-\frac KS.
$$

Thus

$$
\frac{d_2^C}{H}=1-\frac{K}{SH}.
$$

Let

$$
b_\circ(x)=\frac{-x+\sqrt{4-3x^2}}2,
\qquad
h(x)=b_\circ(x)-\frac12.
$$

We first show

$$
H\le h(x).
$$

Since $A+H<1/2$, either the tail on $e_{0,1}$ is produced by $b_0$ and then
$b_0>1/2+H$, or it is produced by $v$ and then $v>1/2+H$.  In the first case,
$a_0\ge x$ and the unit-diameter condition for $T_0$ gives

$$
x^2+xb_0+b_0^2\le1,
$$

so $b_0\le b_\circ(x)$ and $H<h(x)$.  In the second case, the CE2 triangle
contains the two boundary points at parameters $x$ and $v$, so their distance
is at most one:

$$
x^2+xv+v^2\le1.
$$

Thus $v\le b_\circ(x)$ and again $H<h(x)$.  Hence

$$
H\le h(x).
$$

Also $uS\ge x$ gives

$$
H=1-u\le1-\frac{x}{S}=\frac yS.
$$

Therefore

$$
H\le m:=\min\left(\frac yS,h(x)\right).
$$

It remains to prove

$$
\frac{K}{Sm}>\frac23.
$$

#### Subcase I.1: $y/S\le h(x)$

Set

$$
r=\frac yx.
$$

Then $r\le h(x)/(1-h(x))$ and $r\le1$.  Since

$$
D=x\sqrt{1+r+r^2},
$$

we have

$$
\frac Ky=\frac{1+2r-xr-\sqrt{1+r+r^2}}{r}.
$$

For $0<r\le1$,

$$
\sqrt{1+r+r^2}\le1+\frac r2+\frac{r^2}{2}.
$$

Thus

$$
\frac Ky\ge \frac32-x-\frac r2
\ge
\frac32-x-\frac{h(x)}{2(1-h(x))}.
$$

Writing $b=h(x)+1/2=b_\circ(x)$ gives

$$
x=\frac{-b+\sqrt{4-3b^2}}2,
\qquad
\frac{h(x)}{2(1-h(x))}=\frac{b-1/2}{3-2b}.
$$

The function

$$
F(b)=\frac{-b+\sqrt{4-3b^2}}2+\frac{b-1/2}{3-2b}
$$

is decreasing on $1/2\le b\le1$.  Indeed,

$$
F'(b)=\frac{2}{(3-2b)^2}-\frac12-\frac{3b}{2\sqrt{4-3b^2}}<0,
$$

which follows after multiplying by the positive denominators and squaring the
remaining radical comparison.  Hence

$$
F(b)\le F\left(\frac12\right)=\frac{\sqrt{13}-1}{4}.
$$

Therefore

$$
\frac Ky\ge \frac32-\frac{\sqrt{13}-1}{4}=\frac{7-\sqrt{13}}4>\frac23.
$$

In this subcase $Sm=y$, so

$$
\frac{K}{Sm}=\frac Ky>\frac23.
$$

#### Subcase I.2: $h(x)\le y/S$

Now $m=h(x)$.  Set

$$
g(y)=\frac KS=\frac{x+2y-xy-\sqrt{x^2+xy+y^2}}{x+y}.
$$

For fixed $x$ with $h(x)>0$, direct differentiation gives

$$
g'(y)=\frac{x\left(2(1-x)D+x-y\right)}{2S^2D}>0.
$$

If $y\le x$, this is immediate.  If $y>x$, then $D\ge y$ and

$$
2(1-x)D+x-y\ge x+(1-2x)y>0,
$$

where the last inequality is clear for $x\le1/2$, and for $x>1/2$ follows from
$y<1$:

$$
x+(1-2x)y>x+(1-2x)=1-x>0.
$$

Let $y_0$ be defined by

$$
\frac{y_0}{x+y_0}=h(x),
\qquad
\text{so}\qquad
 y_0=\frac{x h(x)}{1-h(x)}.
$$

Since $h(x)\le y/S$, we have $y\ge y_0$.  By monotonicity,

$$
\frac{K(x,y)}{S}\ge\frac{K(x,y_0)}{x+y_0}.
$$

Dividing by $h(x)$, and using $(x+y_0)h(x)=y_0$, gives

$$
\frac{K(x,y)}{S h(x)}\ge\frac{K(x,y_0)}{y_0}.
$$

The right side is the boundary value from Subcase I.1, hence is greater than
$2/3$.  Thus

$$
\frac{K}{Sm}>\frac23.
$$

Combining the two subcases, $K/(Sm)>2/3$.  Since $H\le m$, we get

$$
\frac{K}{SH}\ge\frac{K}{Sm}>\frac23.
$$

Therefore

$$
\frac{d_2^C}{H}=1-\frac{K}{SH}<\frac13,
$$

so

$$
\boxed{d_2^C<\frac H3}
$$

in Branch I.

### Branch II: $H=1-a_0$

Now $a_0=1-H$.

First, the $e_{0,1}$ demand $A$ cannot be produced by $b_0$.  If
$A=1-b_0$, then

$$
A+H=2-a_0-b_0<\frac12,
$$

so

$$
a_0+b_0>\frac32.
$$

But the disk condition gives

$$
a_0^2+a_0b_0+b_0^2\le1,
$$

and hence

$$
a_0+b_0\le\frac2{\sqrt3}<\frac32,
$$

a contradiction.  Thus the active branch is

$$
A=1-v.
$$

Consequently

$$
v>\frac12+H.
$$

For $A$ to be determined by the CE2 endpoint $v$, the row $T_0$ must reach the
start $y$ of the CE2 interval on $e_{0,1}$; otherwise the gap before $y$ would
force $A=1-b_0$.  Hence

$$
b_0\ge y.
$$

Using $a_0=1-H$ and the disk condition,

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

This is the smaller root of the quadratic in $H$.  Since $H<1/2$, the quadratic
inequality gives

$$
H\ge L(y).
$$

The CE2 inequality $uS\ge x$ gives

$$
v=\frac{D+xy}{S}-u\le\frac{D+xy-x}{S}.
$$

Since $v>1/2+H\ge1/2+L(y)$, the following analytic lemma applies.

#### Analytic lemma

Let $0<y<1$ and

$$
L=L(y)=\frac{2+y-\sqrt{4-3y^2}}2.
$$

Let $x>0$, $S=x+y$, and $D=\sqrt{x^2+xy+y^2}$.  If

$$
\frac{D+xy-x}{S}>\frac12+L,
$$

then

$$
\frac{D+xy-x-y}{S}<\frac L3.
$$

To prove the lemma, set

$$
r=\frac xy,
\qquad
R=\sqrt{r^2+r+1}.
$$

Then

$$
\frac{D+xy-x}{S}=\frac{R-r(1-y)}{r+1},
$$

and

$$
\frac{D+xy-x-y}{S}=\frac{R-r(1-y)-1}{r+1}.
$$

Let

$$
r_0=\frac{3-4L}{3+4L}.
$$

Since $0<L<1/2$, $0<r_0<1$.

If $0<r\le r_0$, then

$$
R\le1+\frac r2+\frac{r^2}{2}.
$$

Therefore

$$
\frac{R-r(1-y)-1}{r+1}\le
\frac{r\left(y-\frac12+\frac r2\right)}{r+1}.
$$

The right side is convex in $r$ on $[0,r_0]$, so its maximum occurs at an
endpoint.  The endpoint $r=0$ gives $0$, and a direct substitution at $r_0$
gives

$$
\frac L3-rac{r_0\left(y-\frac12+\frac{r_0}{2}\right)}{r_0+1}>0.
$$

Indeed, after substituting

$$
y=\frac{L-1+\sqrt{1+6L-3L^2}}2,
$$

the numerator has derivative positive on $0<L<1/2$ and vanishes at $L=0$.
Thus the desired inequality holds for $r\le r_0$.

If $r\ge r_0$, then

$$
\frac{R-r(1-y)}{r+1}\le\frac12+L.
$$

This follows by squaring the positive equivalent inequality

$$
R\le \left(\frac12+L\right)(r+1)+r(1-y).
$$

The squared difference is a convex quadratic in $r$; at $r=r_0$ both its value
and derivative are positive after substituting

$$
y=\frac{L-1+\sqrt{1+6L-3L^2}}2.
$$

Thus the squared difference is positive for all $r\ge r_0$.  Hence the
hypothesis of the lemma cannot hold in this range.

This proves the analytic lemma.

Applying the lemma gives

$$
\frac{D+xy-x-y}{S}<\frac{L(y)}3.
$$

But

$$
d_2^C=v-\frac yS\le \frac{D+xy-x-y}{S}.
$$

Therefore

$$
d_2^C<\frac{L(y)}3\le\frac H3.
$$

This proves

$$
\boxed{d_2^C<\frac H3}
$$

in Branch II.

Combining Branches I and II proves the outer ratio target in all cases.

## Excluding $r_2$ coverage

The diagonal $r_2$ is covered, in vertex-to-center coordinates, by the union of
three possible intervals:

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

Therefore full coverage of $r_2$ requires either

$$
c_2\ge q_2,
$$

or else $T_1$ bridges to the center interval, in particular

$$
u_2\ge q_2.
$$

We exclude both alternatives.

### The bridge alternative

If $T_1$ bridges to the center interval, then in the same corner normal form

$$
u_2=\frac{d-a_1-tb_1-1}{t}\ge q_2=1-d_2^C.
$$

Thus

$$
a_1+tb_1\le d-1-t+td_2^C.
$$

Since $d<t+1$ for $t>0$, this implies

$$
a_1+tb_1<td_2^C\,t.
$$

As $b_1\ge H$ and $a_1\ge0$,

$$
tH<td_2^C\,t,
$$

so

$$
H<d_2^C.
$$

This contradicts the outer ratio target

$$
d_2^C<\frac H3.
$$

Hence $T_1$ cannot bridge $r_2$ to the CE2 center interval.

### The $T_2$-alone alternative

If $T_2$ alone reaches the CE2 center interval on $r_2$, then

$$
c_2\ge q_2.
$$

The edge $e_{1,2}$ gives

$$
a_2\ge1-b_1.
$$

Since

$$
a_1+b_1<\frac12
$$

and

$$
a_1\ge A,
$$

we have

$$
b_1<\frac12-A.
$$

Thus

$$
a_2>\frac12+A.
$$

Also the backward boundary propagation gives

$$
b_2\ge H.
$$

By monotonicity of the admissible-set radial envelope,

$$
c_2\le c_{\max}\left(\frac12+A,H\right).
$$

The local radial-envelope bound gives

$$
c_2\le1-\frac H3.
$$

The outer ratio target gives

$$
1-\frac H3<1-d_2^C=q_2.
$$

Therefore

$$
c_2<q_2,
$$

contradicting the $T_2$-alone alternative.

Both possible ways to cover $r_2$ are impossible.  Therefore the adjacent
$T_0$-supercritical, $T_1$-Vd1/Vd2 placement cannot cover the required target.

## Boundary cases

The final contradiction is strict.  The strictness comes from two sources:

1. Vd1/Vd2 requires positive-length adjacent-ray intersection, giving
   $a_1+b_1<1/2$.
2. CE2 has strict positive boundary intervals and midpoint-exclusion
   inequalities, so $u<1$ and the active tail $H$ is positive.

Endpoint-only contacts on the adjacent ray do not count as Vd1/Vd2 positive
length, and equality in the local adjacent-ray bound is therefore excluded.

## Numerical check

Independent numerical checks sampled the CE2 parameters $(x,u,y,v)$ using the
exact relation

$$
(u+v)(x+y)-xy=\sqrt{x^2+xy+y^2}
$$

and the CE2 inequalities, sampled supercritical $(a_0,b_0)$ satisfying

$$
a_0+b_0>1,
\qquad
 a_0^2+a_0b_0+b_0^2\le1,
$$

and then computed $A,H,d_2^C$.  The tested inequalities were

$$
A+H<\frac12\Longrightarrow d_2^C<\frac H3,
$$

and

$$
c_{\max}\left(\frac12+A,H\right)<1-d_2^C.
$$

No violation was found.  The closest samples approached the boundary faces
$H\to0$ in the two active branches, consistent with the proof above.  The
numerical check is not used as an input to the proof.
