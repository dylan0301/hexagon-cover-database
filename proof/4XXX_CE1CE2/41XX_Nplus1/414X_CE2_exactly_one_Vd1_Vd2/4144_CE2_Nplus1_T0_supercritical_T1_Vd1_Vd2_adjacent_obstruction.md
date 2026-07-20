# CE2, $N_+=1$, $T_0$ Supercritical And Adjacent $T_1$ Vd1/Vd2

Status: Proven

This file proves the adjacent remaining placement in the
[`4140`](4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md) branch:

$$
T_C\text{ is CE2},\qquad T_0\text{ is the unique supercritical row},
\qquad T_1\text{ is the unique Vd1/Vd2 row}.
$$

The reflected placement with $T_5$ Vd1/Vd2 is identical.

The proof uses the Vd1/Vd2 normal form from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md),
the boundary caps from
[`../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md),
the exact admissible-set radial envelope from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md),
the half-edge rational envelope from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md),
and the CE2 interval-pair model from
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md).

## Statement

Assume a reduced 414X cover candidate satisfies

$$
T_C\text{ is CE2},\qquad T_C\cap\{M_0,\dots,M_5\}=\{M_0\},
$$

$$
T_0\text{ is the unique supercritical row},\qquad
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
the two diagonal targets $r_1$ and $r_2$. In particular, the adjacent
$T_0$-supercritical, $T_1$-Vd1/Vd2 placement is impossible in the 414X branch.

## 1. CE2 variables and diagonal lengths

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

Put

$$
E=vS-y.
$$

The center-triangle lengths on $r_1$ and $r_2$, measured from $O$ toward the
corresponding vertex, are

$$
d_1^C=\frac Ex,\qquad d_2^C=\frac ES.
$$

Thus the uncovered vertex-side demands are

$$
q_1=1-d_1^C,\qquad q_2=1-d_2^C.
$$

## 2. Boundary demands

Let $(a_0,b_0)$ be the boundary coordinates of $T_0$. Since $T_0$ is
supercritical,

$$
a_0+b_0>1,
$$

while the adjacent endpoint distance condition gives

$$
a_0^2+a_0b_0+b_0^2\le1.
$$

On $e_{0,1}$, coverage by $T_0,T_C,T_1$ forces

$$
a_1\ge A,
$$

where

$$
A=
\begin{cases}
1-b_0,& b_0<y,\\
\max\left\{0,1-\max\{b_0,v\}\right\},& b_0\ge y.
\end{cases}
$$

On $e_{5,0}$, coverage by $T_0,T_C,T_5$ forces

$$
b_5\ge H,
$$

where

$$
H=
\begin{cases}
1-a_0,& a_0<x,\\
\max\left\{0,1-\max\{a_0,u\}\right\},& a_0\ge x.
\end{cases}
$$

Because $u<1$ and $T_0$ is strictly supercritical, $H>0$ in a genuine
candidate.

For ordinary nonsupercritical Vd0 rows, $a_i+b_i\le1$. Together with the
boundary handoffs $b_i+a_{i+1}\ge1$, this propagates the $b_5$ lower bound
backward:

$$
b_5\ge H\Longrightarrow b_4\ge H\Longrightarrow b_3\ge H
\Longrightarrow b_2\ge H\Longrightarrow b_1\ge H.
$$

Therefore

$$
\boxed{a_1\ge A,\qquad b_1\ge H.}
$$

The Vd1/Vd2 boundary cap gives

$$
\boxed{a_1+b_1<\frac12.}
$$

Consequently

$$
\boxed{A+H<\frac12.}
$$

## 3. The rational radial envelope for $T_2$

Put

$$
p=\frac12+A,\qquad h=H.
$$

Then

$$
\frac12\le p<1,\qquad 0<h\le p,\qquad p+h<1.
$$

Indeed $p+h<1$ follows from $A+H<1/2$, while
$p-h=1/2+A-H>0$. The half-edge rational-envelope theorem in `2012` therefore
gives

$$
\boxed{
c_{\max}\left(\frac12+A,H\right)\le1-\frac H3.
}
$$

This is used only in the necessary direction

$$
(p,h,c)\in\mathcal A
\Longrightarrow
c\le c_{\max}(p,h)\le1-\frac h3.
$$

No realizability or equality at the rational cap is asserted.

## 4. The outer ratio target

We prove

$$
\boxed{d_2^C<\frac H3.}
$$

There are two possible sources of the boundary tail $H$.

### 4.1. Branch I: $H=1-u$

Here $a_0\ge x$ and $a_0\le u$. Define

$$
K=x+2y-xy-D.
$$

Since

$$
d_2^C=\frac{D+xy-uS-y}{S}
$$

and $D+xy-y=S-K$, one has

$$
d_2^C=1-u-\frac KS=H-\frac KS,
$$

hence

$$
\frac{d_2^C}{H}=1-\frac{K}{SH}.
$$

Put

$$
b_\circ(x)=\frac{-x+\sqrt{4-3x^2}}2,
\qquad
h(x)=b_\circ(x)-\frac12.
$$

We first claim

$$
H\le\min\left\{\frac yS,h(x)\right\}.
$$

The inequality $H\le y/S$ follows from $H=1-u$ and $uS\ge x$. To prove
$H\le h(x)$, use $A+H<1/2$. If the $e_{0,1}$ tail is produced by $b_0$, then
$b_0>1/2+H$. Since $a_0\ge x$ and
$a_0^2+a_0b_0+b_0^2\le1$, one has $b_0\le b_\circ(x)$ and hence
$H<h(x)$. If the tail is produced by $v$, then $v>1/2+H$. The center triangle
contains boundary points at parameters $x$ and $v$, so
$x^2+xv+v^2\le1$, whence $v\le b_\circ(x)$ and again $H<h(x)$.

Set

$$
m=\min\left\{\frac yS,h(x)\right\}.
$$

We show

$$
\frac{K}{Sm}>\frac23.
$$

Suppose first that $y/S\le h(x)$ and put $r=y/x$. Then

$$
r\le\frac{h(x)}{1-h(x)},\qquad r\le1.
$$

The exact inequality

$$
\sqrt{1+r+r^2}\le1+\frac r2+\frac{r^2}{2}
$$

follows because the difference of the squares is
$r^2(r+1)^2/4$. Therefore

$$
\frac Ky\ge\frac32-x-\frac r2
\ge\frac32-x-\frac{h(x)}{2(1-h(x))}.
$$

Write $b=h(x)+1/2=b_\circ(x)$. Since the diameter relation is symmetric,
$x=b_\circ(b)$. Define

$$
F(b)=\frac{-b+\sqrt{4-3b^2}}2+\frac{b-1/2}{3-2b}.
$$

On $1/2\le b\le1$,

$$
F'(b)=\frac{2}{(3-2b)^2}-\frac12-
\frac{3b}{2\sqrt{4-3b^2}}<0.
$$

For completeness, put $z=1-b\in[0,1/2]$. After moving the rational term and
squaring the nonnegative sides, the last sign is equivalent for $z>0$ to

$$
\begin{aligned}
&9(1-z)^2(1+2z)^4\\
&\qquad-
\left(3-4z-4z^2\right)^2
\left(1+6z-3z^2\right)>0.
\end{aligned}
$$

The left side is $zP(z)$, where the Bernstein coefficients of the degree-$5$
polynomial $P$ on $[0,1/2]$ are

$$
24,\qquad 50,\qquad \frac{364}{5},\qquad
\frac{434}{5},\qquad \frac{432}{5},\qquad72.
$$

They are all positive. Hence

$$
F(b)\le F\left(\frac12\right)=\frac{\sqrt{13}-1}{4},
$$

and therefore

$$
\frac Ky\ge\frac{7-\sqrt{13}}4>\frac23.
$$

In this subcase $Sm=y$, so $K/(Sm)>2/3$.

Now suppose that $h(x)\le y/S$, so $m=h(x)$. For fixed $x$, define

$$
g(y)=\frac{x+2y-xy-\sqrt{x^2+xy+y^2}}{x+y}.
$$

Then

$$
g'(y)=\frac{x\left(2(1-x)D+x-y\right)}{2S^2D}>0.
$$

The sign is immediate when $y\le x$. When $y>x$, use $D\ge y$ to obtain

$$
2(1-x)D+x-y\ge x+(1-2x)y
=x(1-y)+y(1-x)>0.
$$

Let $y_0$ be defined by

$$
\frac{y_0}{x+y_0}=h(x).
$$

Since $h(x)\le y/S$, one has $y\ge y_0$, and hence

$$
\frac{K(x,y)}{S h(x)}
\ge
\frac{K(x,y_0)}{(x+y_0)h(x)}
=
\frac{K(x,y_0)}{y_0}
>\frac23,
$$

where the last inequality is the boundary value from the preceding subcase.
Thus $K/(Sm)>2/3$ in all cases. Since $H\le m$,

$$
\frac{K}{SH}\ge\frac{K}{Sm}>\frac23.
$$

Consequently

$$
\frac{d_2^C}{H}=1-\frac{K}{SH}<\frac13,
$$

so $d_2^C<H/3$ in Branch I.

### 4.2. Branch II: $H=1-a_0$

Now $a_0=1-H$. The $e_{0,1}$ demand $A$ cannot equal $1-b_0$: otherwise

$$
A+H=2-a_0-b_0<\frac12
$$

would imply $a_0+b_0>3/2$, contradicting

$$
a_0+b_0\le\frac2{\sqrt3},
$$

which follows from $a_0^2+a_0b_0+b_0^2\le1$. Hence $A=1-v$ and

$$
v>\frac12+H.
$$

For $A$ to be determined by $v$, the row $T_0$ must reach the start $y$ of the
CE2 interval on $e_{0,1}$, so $b_0\ge y$. The disk condition gives

$$
(1-H)^2+(1-H)y+y^2\le1.
$$

Equivalently,

$$
H^2-(2+y)H+y+y^2\le0.
$$

Put

$$
L(y)=\frac{2+y-\sqrt{4-3y^2}}2.
$$

Since $H<1/2$, the quadratic inequality gives

$$
H\ge L(y).
$$

The CE2 inequality $uS\ge x$ gives

$$
v=\frac{D+xy}{S}-u\le\frac{D+xy-x}{S}.
$$

Thus

$$
\frac{D+xy-x}{S}>\frac12+L(y).
$$

We use the following exact analytic lemma.

#### Analytic lemma

Let $0<y<1$ and

$$
L=\frac{2+y-\sqrt{4-3y^2}}2.
$$

For $x>0$, put $S=x+y$ and $D=\sqrt{x^2+xy+y^2}$. If

$$
\frac{D+xy-x}{S}>\frac12+L,
$$

then

$$
\frac{D+xy-x-y}{S}<\frac L3.
$$

First,

$$
\frac{D+xy-x}{S}<1.
$$

Indeed both sides in $D<2x+y-xy$ are positive, and

$$
(2x+y-xy)^2-D^2
=x\left(y(3-2y)+x(1-y)(3-y)\right)>0.
$$

Hence the premise forces $0<L<1/2$. Set

$$
r=\frac xy,\qquad R=\sqrt{r^2+r+1},\qquad
r_0=\frac{3-4L}{3+4L}.
$$

Then

$$
\frac{D+xy-x}{S}=\frac{R-r(1-y)}{r+1},
\qquad
\frac{D+xy-x-y}{S}=\frac{R-r(1-y)-1}{r+1}.
$$

Suppose first that $0<r\le r_0$. Since

$$
R\le1+\frac r2+\frac{r^2}{2},
$$

one obtains

$$
\frac{R-r(1-y)-1}{r+1}
\le
\frac{r(y-1/2+r/2)}{r+1}.
$$

The right side is convex in $r$ because its second derivative is

$$
\frac{2(1-y)}{(1+r)^3}>0.
$$

Its maximum on $[0,r_0]$ is therefore at an endpoint. The value at $0$ is
zero. At $r=r_0$,

$$
\frac L3-
\frac{r_0(y-1/2+r_0/2)}{r_0+1}
=
\frac{N(L)}{6(3+4L)},
$$

where

$$
N(L)=16L^2y-8L^2+18L-9y,
\qquad
y=\frac{L-1+\sqrt{1+6L-3L^2}}2.
$$

Write $s=\sqrt{1+6L-3L^2}$. Then $N(0)=0$ and

$$
2sN'(L)=
 s(48L^2-64L+27)-144L^3+240L^2+59L-27.
$$

On $0<L<1/2$, one has $48L^2-64L+27>0$ and

$$
s\ge1+3L-6L^2,
$$

because the right side is positive and the difference of the squares is
$36L^3(1-L)$. Therefore

$$
2sN'(L)
\ge
2L\left(-144L^3+192L^2-33L+38\right)>0.
$$

The Bernstein coefficients of the last cubic on $[0,1/2]$ are

$$
38,\qquad \frac{65}{2},\qquad 43,\qquad \frac{103}{2},
$$

so its positivity is exact. Thus $N(L)>0$, proving the lemma when
$r\le r_0$.

It remains to show that the premise cannot hold for $r\ge r_0$. Put

$$
J(r)=\frac{R-r(1-y)}{r+1}.
$$

Its derivative has the sign of

$$
\frac{r-1}{2R}-(1-y).
$$

The function $(r-1)/(2R)$ is strictly increasing because

$$
\frac{d}{dr}\left(\frac{r-1}{2R}\right)
=\frac{3(r+1)}{4R^3}>0.
$$

Hence $J$ decreases and then increases, with at most one turning point. Its
maximum on $[r_0,\infty)$ is attained at $r_0$ or in the limit. The limiting
value is $y$, and

$$
y<\frac12+L
$$

because

$$
(3-y)^2-(4-3y^2)=4y^2-6y+5>0.
$$

At $r=r_0$, the bound $R\le1+r/2+r^2/2$ gives

$$
\frac12+L-J(r_0)
\ge
\frac{N(L)}{(3+4L)^2}>0.
$$

Thus $J(r)<1/2+L$ for every $r\ge r_0$, contradicting the premise. The
analytic lemma is proved.

Applying the lemma gives

$$
\frac{D+xy-x-y}{S}<\frac{L(y)}3.
$$

Since

$$
d_2^C=v-\frac yS
\le
\frac{D+xy-x-y}{S},
$$

we obtain

$$
d_2^C<\frac{L(y)}3\le\frac H3.
$$

Thus the outer ratio target holds in Branch II as well.

## 5. Excluding coverage of $r_2$

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

Therefore full coverage of $r_2$ requires either $c_2\ge q_2$, or else $T_1$
bridges to the center interval, in particular $u_2\ge q_2$.

Suppose first that $T_1$ bridges. Orient the normal form from `2014` so that
$r_2$ is the supported adjacent arm. For some $t>0$ and
$d=\sqrt{t^2+t+1}$, its upper endpoint is

$$
u_2=\frac{d-a_1-tb_1-1}{t}\ge q_2=1-d_2^C.
$$

Thus

$$
a_1+tb_1\le d-1-t+td_2^C.
$$

Since $d<t+1$,

$$
a_1+tb_1<td_2^C t.
$$

But $b_1\ge H$ and $a_1\ge0$, so $Ht<d_2^Ct$, hence $H<d_2^C$, contrary to
$d_2^C<H/3$. Therefore $T_1$ cannot bridge.

If $T_2$ alone reaches the center interval, then $c_2\ge q_2$. The edge
$e_{1,2}$ gives

$$
a_2\ge1-b_1.
$$

Since $a_1+b_1<1/2$ and $a_1\ge A$,

$$
a_2>\frac12+A.
$$

Backward boundary propagation gives $b_2\ge H$. Coordinatewise down-closedness
of the admissible set and monotonicity of its radial envelope therefore give

$$
c_2\le c_{\max}\left(\frac12+A,H\right)
\le1-\frac H3.
$$

The outer ratio target gives

$$
1-\frac H3<1-d_2^C=q_2.
$$

Thus $c_2<q_2$, a contradiction. Both possible ways to cover $r_2$ are
impossible, proving the adjacent obstruction.

## 6. Boundary cases

The contradiction is strict. Vd1/Vd2 requires positive-length adjacent-ray
intersection, giving $a_1+b_1<1/2$. CE2 has strict positive boundary intervals
and $H>0$ for a genuine supercritical $T_0$ branch. Endpoint-only adjacent-ray
contacts do not count as Vd1/Vd2 positive length.

$$
\Box
$$
