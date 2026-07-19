# Direct Vd0 Radial Forcing

Status: Proven

This note derives the common radial demand from an exact-one handoff chain and
then excludes the resulting six radial witnesses from the six actual open
vertex roles.

## 1. Exact-one handoffs

Let $H$ be the side-$1$ regular hexagon centered at $O=0$, with cyclic
vertices $V_0,\dots,V_5$. Let $T_i$ be an open unit equilateral triangle
containing $V_i$, and suppose the six vertex roles cover $\partial H$.

Assume exactly one actual row is supercritical. Rotate its index to $4$ and
choose the strict handoffs supplied by
[`1214_strict_boundary_handoff_selection.md`](../../../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md):

$$
X_i=V_i+x_i(V_{i+1}-V_i),
\qquad
0<x_i<1,
\qquad
X_i\in T_i\cap T_{i+1}.
\tag{1}
$$

The selected incoming and outgoing demands of row $i$ are

$$
a_i=1-x_{i-1},
\qquad
b_i=x_i.
\tag{2}
$$

Every selected row except row $4$ is strictly nonsupercritical. Therefore
$x_i<x_{i-1}$ for $i\ne4$, and the six handoffs satisfy

$$
x_3<x_2<x_1<x_0<x_5<x_4.
\tag{3}
$$

Put

$$
a=1-x_3,
\qquad
b=x_4,
\qquad
p=1-b=1-x_4,
\qquad
q=1-a=x_3.
\tag{4}
$$

The two anchors $X_3,X_4\in T_4$ have $V_4$-local coordinates $(0,a)$ and
$(b,0)$. Since two points of an open unit equilateral triangle are at
distance strictly less than $1$,

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1.
\tag{5}
$$

Equation (3) says that every $x_j$ lies in $[x_3,x_4]$. Thus every selected
row, including row $4$, obeys

$$
a_i=1-x_{i-1}\ge1-x_4=p,
\qquad
b_i=x_i\ge x_3=q.
\tag{6}
$$

## 2. The common radial value

Set

$$
s=p+q,
\qquad
m=\min\{p,q\},
\qquad
M=\max\{p,q\},
\qquad
\chi=s^4-s^2+pq.
\tag{7}
$$

Then

$$
0<p,q<1,
\qquad
0<s<1,
\qquad
0<m\le M,
\qquad
m<\frac12.
\tag{8}
$$

Expanding the last inequality in (5) after substituting $a=1-q$ and
$b=1-p$ gives

$$
pq>(1-s)(2-s).
\tag{9}
$$

In particular,

$$
m>1-s,
\qquad
s>1-m.
\tag{10}
$$

Indeed, if $m\le1-s$, then $M<1$ would give

$$
mM\le(1-s)M<1-s<(1-s)(2-s),
$$

contrary to (9). The second inequality in (10) is the rearrangement of the
first.

Also

$$
p^2+pq+q^2=s^2-pq<s^2<1.
\tag{11}
$$

Consequently the exact radial-envelope theorem
[`2004_admissible_set.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md)
applies on its subcritical domain. With $h=\sqrt3/2$, let $C_L(m)$ be the
unique root in $[h,1]$ of

$$
z^4-z^2+mz-m^2=0.
\tag{12}
$$

The exact common radial value is

$$
c_*=c_{\max}(p,q)
=
\begin{cases}
C_L(m),&\chi\le0,\\[1mm]
\displaystyle\frac{2M}{1+\sqrt{4s^2-3}},&\chi>0.
\end{cases}
\tag{13}
$$

At $\chi=0$ the two expressions agree and equal $s$.

### Radial bounds

The value in (13) satisfies

$$
0<c_*<1,
\qquad
c_*>1-m.
\tag{14}
$$

On the $C_L$ branch, $c_*\ge h>0$, while the polynomial in (12) has value
$m(1-m)>0$ at $1$. The selected root is therefore strictly below $1$.

Suppose instead that $\chi>0$. Since $pq\le s^2/4$,

$$
\chi\le s^2\left(s^2-\frac34\right),
$$

so $s>h$. Put $E=\sqrt{4s^2-3}$. The identity

$$
s^2E^2-(M-m)^2=4\chi>0
$$

gives $sE>M-m$. Hence

$$
s(1+E)>s+M-m=2M,
$$

and (13) gives $0<c_*<s<1$. This proves the first part of (14).

For the second part, first suppose $\chi\le0$. If $s<h$, then

$$
c_*\ge h>s>1-m.
$$

If $s\ge h$, the polynomial in (12), evaluated at $s$, is

$$
s^4-s^2+ms-m^2=s^4-s^2+mM=\chi\le0.
$$

Its unique selected root and its positive value at $1$ imply
$c_*\ge s>1-m$.

Finally suppose $\chi>0$, retain $E$, put $t=1-s$, and define

$$
A_0=\frac{2M}{1-m}-1.
$$

Here $A_0>0$: indeed $2s>2h>1+m$, so
$2M=2(s-m)>1-m$. Direct expansion gives

$$
A_0^2-E^2
=
\frac{4t\left\{(1-m)(1-2m)+m(2-m)t\right\}}{(1-m)^2}>0.
$$

Thus $A_0>E$, and

$$
\frac{c_*}{1-m}
=
\frac{2M}{(1-m)(1+E)}
=
\frac{1+A_0}{1+E}>1.
$$

This completes the proof of (14).

## 3. Direct radial-forcing theorem

Assume every $T_i$ is Vd0. Define

$$
D_i=(1-c_*)V_i,
\qquad
i=0,\dots,5.
\tag{15}
$$

Then

$$
D_i\notin\bigcup_{j=0}^5T_j
\qquad(i=0,\dots,5).
\tag{16}
$$

To prove this, fix $i$. In the local corner coordinates at $V_i$, the sum
of the incoming and outgoing unit directions points from $V_i$ to $O$.
Thus radial demand $c$ is the global point $(1-c)V_i$.

Suppose first that $D_i\in T_i$. By (14), $D_i$ lies in the relative
interior of $OV_i$. Openness supplies $\varepsilon>0$, with
$c_*+\varepsilon<1$, such that

$$
(1-c_*-\varepsilon)V_i\in T_i.
\tag{17}
$$

The same role contains $V_i,X_{i-1},X_i$. By (6), convexity, and passage to
the closure, the closed unit triangle $\overline{T_i}$ contains the incoming
and outgoing demand points at distances $p$ and $q$, together with the
radial demand point at distance $c_*+\varepsilon$. Hence it realizes the
local demand triple $(p,q,c_*+\varepsilon)$. This contradicts the definition
of $c_*=c_{\max}(p,q)$. Therefore

$$
D_i\notin T_i.
\tag{18}
$$

For $T_{i-1}$ and $T_{i+1}$, the arm $OV_i$ is an adjacent radial arm. If
one of these open roles contained $D_i$, a small plane ball about $D_i$
inside that role would meet $OV_i$ in a positive-length interval. This is
excluded by the Vd0 definition in
[`1201_V_triangle_types.md`](../../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).
Thus

$$
D_i\notin T_{i-1}\cup T_{i+1}.
\tag{19}
$$

For the remaining roles put $r=1-c_*>0$. At cyclic distance two,

$$
\left\lVert rV_i-V_{i\pm2}\right\rVert^2=1+r+r^2>1,
\tag{20}
$$

and at the opposite vertex,

$$
\left\lVert rV_i-V_{i+3}\right\rVert=1+r>1.
\tag{21}
$$

Every $T_j$ contains $V_j$, and two points of an open unit equilateral
triangle have distance strictly below its diameter $1$. Equations
(20)--(21) therefore exclude $D_i$ from the remaining three vertex roles.
Together with (18)--(19), this proves (16).

## 4. Consequence for a seven-role cover

Suppose an additional open unit equilateral triangle $T_C$ and the six
vertex roles cover $H$. Equation (14) puts every $D_i$ in
$\mathrm{int}(H)$, while (16) excludes all six vertex roles. Consequently,

$$
D_0,\dots,D_5\in T_C.
\tag{22}
$$

The six points form a regular hexagon of circumradius $1-c_*$. Its convex
hull contains the centered closed disk of radius $h(1-c_*)$. Since $T_C$ is
convex, (22) gives

$$
\boxed{
\mathcal D_\eta
=
\left\{P:\lVert P\rVert\le\eta\right\}
\subset T_C,
\qquad
\eta=h(1-c_*).
}
\tag{23}
$$

This proves the direct radial-forcing statement. $\square$
