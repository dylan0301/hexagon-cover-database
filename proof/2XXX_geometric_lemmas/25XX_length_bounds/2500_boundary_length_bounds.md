# Boundary Length Bounds

Status: Proven

Let $U_C,U_0,\dots,U_5$ be the open role triangles in a hypothetical cover,
and let

$$
T_C=\overline{U_C},
\qquad
T_i=\overline{U_i}.
$$

Thus

$$
O\in\mathrm{int}(T_C),
\qquad
V_i\in\mathrm{int}(T_i).
$$

For any closed triangle $T$, define its full boundary contribution by

$$
L_{\partial H}(T)=\mathcal H^1(T\cap\partial H).
$$

Passing from an open triangle to its closure can only increase its trace.
Consequently, if the seven open role triangles cover $\partial H$, then

$$
6=\mathcal H^1(\partial H)
\le
L_{\partial H}(T_C)+\sum_{i=0}^5L_{\partial H}(T_i).
$$

Point contacts and interval endpoints have zero $\mathcal H^1$-measure. Any
assigned or reduced boundary contribution is a measurable subset of the full
trace and therefore inherits every cap proved below.

The relevant definitions are:

- CE edge type:
  [../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md](../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md).
- V-triangle type:
  [../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md](../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).
- Local row coordinates:
  [../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md](../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md).

## Theorem

The closures of the original open roles satisfy the following bounds.

| Role or local type | Hypothesis | Full boundary contribution |
|---|---|---:|
| CE0 center role | $T_C$ is CE0 | $0$ |
| CE1 center role | $T_C$ is CE1 | at most $\frac{\sqrt3}{2}-\frac34<\frac12$ |
| CE2 center role | $T_C$ is CE2 | strictly less than $\frac12$ |
| Vd0 vertex role | $a_i+b_i\le1$ | at most $1$ |
| Vd0 vertex role | $a_i+b_i>1$ | at most $\frac{2}{\sqrt3}$ |
| Vd1/Vd2 vertex role | none beyond the type hypothesis | strictly less than $\frac12$ |
| T3-like vertex role | none beyond the type hypothesis | strictly less than $1$ |

## Vertex-role boundary locality

We first prove that for every original vertex role,

$$
\boxed{L_{\partial H}(T_i)=a_i+b_i.}
$$

By symmetry, normalize to $i=0$ and use local coordinates

$$
X=V_0+x(V_1-V_0)+y(V_5-V_0).
$$

Then

$$
\lVert(x,y)\rVert^2=x^2+y^2-xy.
$$

Convexity and $V_0\in\mathrm{int}(T_0)$ show that the traces on the two
incident edges are initial intervals of lengths $b_0$ and $a_0$. It remains
to rule out positive-length trace on the other four edges.

For $0<t<1$, the squared distances from $V_0$ to relative-interior points on
$e_{1,2}$, $e_{2,3}$, and $e_{3,4}$ are respectively

$$
1+t+t^2,
\qquad
3+t^2,
\qquad
4-2t+t^2.
$$

The edge $e_{4,5}$ is the reflection of $e_{1,2}$. Every displayed quantity
is strictly greater than $1$. A point in the closure of a diameter-$1$ convex
set is at distance strictly less than $1$ from any interior point of that set:
if equality held, a short continuation through the interior point in the
opposite direction would produce two points more than $1$ apart. Hence no
relative-interior point of a nonincident edge belongs to $T_0$. This proves
the claimed equality.

## Center-role caps

### CE0

By definition, a CE0 triangle has no positive-length intersection with any
hexagon edge. Its intersection with each of the six edges is a point or is
empty, so

$$
L_{\partial H}(T_C)=0.
$$

### CE1

The exact-one-midpoint theorem in
[../21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md](../21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md)
applies because $O\in\mathrm{int}(T_C)$. After a symmetry, the CE1 trace is
an interval

$$
T_C\cap e_{0,1}=[s,t],
\qquad
0<s<t<1,
$$

and the maximal-interval theorem in
[2102_CE1_M0_e01_maximal_intervals.md](../21XX_C_triangle_geometry/2102_CE1_M0_e01_maximal_intervals.md)
proves

$$
t\le\sqrt{s^2-s+1}-(1-s)^2.
$$

Put

$$
\rho=\sqrt{s^2-s+1}.
$$

Since $\rho^2=s^2-s+1$,

$$
L_{\partial H}(T_C)=t-s
\le\rho-\rho^2=\rho(1-\rho).
$$

Here

$$
\frac{\sqrt3}{2}\le\rho<1.
$$

The function $r(1-r)$ is decreasing for $r\ge1/2$, so

$$
L_{\partial H}(T_C)
\le
\frac{\sqrt3}{2}-\frac34
<\frac12.
$$

The equality $t-s=\rho(1-\rho)$ belongs only to the maximalized interval;
the inequality above is the statement for an arbitrary CE1 role.

### CE2

The diameter argument in
[../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md](../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md)
shows that the two positively overlapped edges are adjacent. Normalize one of
them as $e_{0,1}$. The edge normal form in the exact-one-midpoint theorem has
$0<\lambda<1$, gives unique midpoint $M_0$, and has

$$
F_2=-b+\lambda a+t.
$$

The exclusion of $M_1$ gives

$$
t<1-\frac{\lambda}{2}<1.
$$

On $e_{1,2}$, parameterized by $b=1+u$, $a=u$, one has

$$
F_2=t-1-(1-\lambda)u<0.
$$

Thus the second overlapped edge cannot be $e_{1,2}$ and must be $e_{5,0}$.
After this justified normalization, write the two CE2 intervals as

$$
[x,u]\subset e_{5,0},
\qquad
[y,v]\subset e_{0,1},
$$

and put

$$
S=x+y,
\qquad
D=\sqrt{x^2+xy+y^2}.
$$

The exact interval-pair theorem in
[2103_CE2_M0_e50_e01_maximal_interval_pairs.md](../21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md)
gives

$$
(u+v)S-xy=D,
$$

as well as the center-containment inequalities

$$
uS\ge x,
\qquad
vS\ge y.
$$

Adding the latter inequalities and using the former gives

$$
D+xy=(u+v)S\ge S.
$$

Since $S-xy>0$, we may square $D\ge S-xy$. The identity

$$
D^2=S^2-xy
$$

then yields

$$
xy(2S-xy-1)\ge0.
$$

Here $x,y>0$, and hence

$$
S\ge\frac{1+xy}{2}>\frac12.
$$

Finally,

$$
\begin{aligned}
L_{\partial H}(T_C)
&=(u-x)+(v-y)\\
&=\frac{D+xy}{S}-S\\
&=\frac{D(1-D)}{S}.
\end{aligned}
$$

The left side is positive, so $0<D<1$. Therefore

$$
L_{\partial H}(T_C)
\le\frac{1}{4S}
<\frac12.
$$

## Vd0 caps

By vertex-role boundary locality,

$$
L_{\partial H}(T_i)=a_i+b_i.
$$

Thus the nonsupercritical cap is immediate. For a supercritical row, let $A$
and $B$ be its two incident-edge endpoints. The angle between the incident
edge directions is $120^\circ$, so

$$
\lVert A-B\rVert^2=a_i^2+a_ib_i+b_i^2.
$$

Both points lie in a unit equilateral triangle, whose diameter is $1$.
Consequently,

$$
1\ge a_i^2+a_ib_i+b_i^2
=\frac34(a_i+b_i)^2+\frac14(a_i-b_i)^2
\ge\frac34(a_i+b_i)^2.
$$

Hence

$$
L_{\partial H}(T_i)=a_i+b_i\le\frac{2}{\sqrt3}.
$$

The weak inequality is necessary: with $r=1/\sqrt3$, the local unit triangle

$$
\mathrm{conv}\left\{(r,0),(0,r),(-r,-r)\right\}
$$

is a Vd0 equality example.

## Vd1/Vd2 cap

Normalize at $V_0$ using

$$
X=V_0+x(V_5-V_0)+y(V_1-V_0).
$$

The local metric is again

$$
\lVert(x,y)\rVert^2=x^2+y^2-xy.
$$

Let $a,b$ be the exact incident-edge reaches. A Vd1 or Vd2 triangle has one
vertex outside $H$, two vertices in $H$, and positive-length intersection
with at least one adjacent radial arm. Since $V_0$ is an interior point of the
original role closure, both reaches are positive.

We record the needed corner-side normal form. There is a unique $t>0$, with

$$
d=\sqrt{t^2+t+1},
$$

such that the triangle is

$$
\left\{(x,y):
\begin{array}{rcl}
x-(t+1)y&\le&a,\\
ty-(t+1)x&\le&tb,\\
tx+y&\le&d-a-tb
\end{array}
\right\}.
$$

Here is a proof of the normal form. Put

$$
A=(a,0),
\qquad
B=(0,b).
$$

Let $W$ be the unique outside vertex and let $U,Z\in H$ be the other two
vertices. Since $V_0$ is in the interior, it has a barycentric expression

$$
V_0=\omega W+\mu U+\nu Z,
\qquad
\omega,\mu,\nu>0.
$$

The local coordinates of $U,Z$ are nonnegative, so both coordinates of $W$
are nonpositive. In fact they are negative. For example, if $W_x=0$, then the
barycentric identity forces $U_x=Z_x=0$. The unit segment $UZ$ would then be
the entire unit edge $e_{0,1}$, making $V_0$ a triangle vertex, contrary to
$V_0\in\mathrm{int}(T_0)$. The argument for $W_y$ is identical.

Neither $A$ nor $B$ can lie in the relative interior of $UZ$. For example, if
$A\in\mathrm{relint}(UZ)$, then the nonnegative $y$-coordinates of $U,Z$ have
a strict convex combination equal to $0$. Thus $U_y=Z_y=0$, and the unit side
$UZ$ is the whole edge $e_{5,0}$, again impossible. The argument for $B$ is
identical. Hence each of $A,B$ lies on a side incident with $W$, possibly at
the other endpoint of that side.

The points $A,B$ lie on distinct sides through $W$. Indeed, on a segment from
a point with both coordinates negative to a point with both coordinates
nonnegative, let $\tau_x$ and $\tau_y$ be the parameters at which the two
coordinates vanish. Its intersection with $y=0$ has positive $x$-coordinate
exactly when $\tau_y>\tau_x$, whereas its intersection with $x=0$ has positive
$y$-coordinate exactly when $\tau_x>\tau_y$. One segment cannot satisfy both
conditions. Relabel $U,Z$ so that

$$
A\in WU,
\qquad
B\in WZ.
$$

Put

$$
p=U-W,
\qquad
q=Z-W.
$$

Both coordinates of $p,q$ are positive, and

$$
\lVert p\rVert=\lVert q\rVert=\lVert p-q\rVert=1.
$$

Thus their physical angle is $60^\circ$. In the present local coordinates,
clockwise physical rotation through $60^\circ$ is

$$
R_{-60}(r,s)=(r-s,r).
$$

Write

$$
r=-W_x>0,
\qquad
s=-W_y>0.
$$

The side $WU$ crosses $y=0$ at positive $x$, so

$$
s p_x>r p_y.
$$

The side $WZ$ crosses $x=0$ at positive $y$, so

$$
r q_y>s q_x.
$$

Consequently,

$$
\frac{p_y}{p_x}<\frac{s}{r}<\frac{q_y}{q_x}.
$$

Of the two possible $60^\circ$ rotations, this strict slope order forces

$$
q=R_{-60}p=(p_x-p_y,p_x),
\qquad
p_x>p_y>0.
$$

Set

$$
t=\frac{p_x-p_y}{p_y}>0.
$$

The unit-length condition gives

$$
p=\frac{(t+1,1)}d,
\qquad
q=\frac{(t,t+1)}d,
\qquad
d=\sqrt{t^2+t+1}.
$$

This also proves uniqueness of $t$.

The line through $A$ parallel to $p$ and the line through $B$ parallel to $q$
are

$$
x-(t+1)y=a,
\qquad
ty-(t+1)x=tb.
$$

Their intersection is

$$
W=
\left(
-\frac{t(a+(t+1)b)}{d^2},
-\frac{(t+1)a+tb}{d^2}
\right).
$$

The third side is parallel to

$$
q-p=\frac{(-1,t)}d,
$$

so it has an equation $tx+y=c$. At $W$,

$$
tW_x+W_y=-a-tb,
$$

whereas moving one unit from $W$ to $U$ along $p$ increases $tx+y$ by

$$
tp_x+p_y=\frac{t(t+1)+1}{d}=d.
$$

Consequently

$$
c=d-a-tb.
$$

Since the origin is interior, its side of each line is the weak half-plane
displayed in the normal form. This proves the claim.

First suppose that the supported adjacent arm is

$$
y=1,
\qquad
0\le x\le1.
$$

On this arm the second and third inequalities give respectively

$$
x\ge\frac{t(1-b)}{t+1},
\qquad
x\le\frac{d-a-tb-1}{t}.
$$

Positive-length intersection forces the lower endpoint to be strictly below
the upper endpoint. After clearing the positive denominators,

$$
(t+1)a+tb<(t+1)(d-1)-t^2.
$$

Since the left side is at least $t(a+b)$,

$$
a+b<\frac{(t+1)(d-1)-t^2}{t}.
$$

The last expression is strictly less than $1/2$. Indeed, that assertion is
equivalent to

$$
(t+1)d<t^2+\frac{3t}{2}+1,
$$

and both sides are positive, while

$$
\left(t^2+\frac{3t}{2}+1\right)^2
-(t+1)^2(t^2+t+1)
=\frac{t^2}{4}>0.
$$

If instead the supported adjacent arm is $x=1$, reflect the entire
configuration and reapply the normal-form argument. The same bound follows.
Thus every original Vd1/Vd2 role satisfies

$$
L_{\partial H}(T_i)=a_i+b_i<\frac12.
$$

## T3-like cap

The exhaustive orientation analysis and Type-II formulas in
[../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md](../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md)
apply to every original T3-like role. After a reflection if necessary, they
give

$$
0<t<1,
\qquad
z=\sqrt{1-t+t^2},
$$

and parameters $\alpha,\beta>0$ with

$$
\alpha+\beta<z.
$$

The exact incident-edge reaches are

$$
A=\beta,
\qquad
B=z-\alpha-\beta.
$$

Since $0<t<1$, one has $z<1$. Hence

$$
L_{\partial H}(T_i)=A+B=z-\alpha<z<1.
$$

This proves every entry in the theorem.
