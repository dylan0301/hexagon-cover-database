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
- Local V triangle coordinates:
  [../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md](../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md).

## Theorem

The closures of the original open roles satisfy the following bounds.

| Role or local type | Hypothesis | Full boundary contribution |
|---|---|---:|
| CE0 center role | $T_C$ is CE0 | $0$ |
| CE1 center role | $T_C$ is CE1 | at most $\frac{\sqrt3}{2}-\frac34<\frac12$ |
| CE2 center role | $T_C$ is CE2 | strictly less than $\frac12$ |
| Vd0 vertex role | $A_i+B_i\le1$ | at most $1$ |
| Vd0 vertex role | $A_i+B_i>1$ | at most $\frac{2}{\sqrt3}$ |
| Vd1/Vd2 vertex role | none beyond the type hypothesis | strictly less than $\frac12$ |
| T3-like vertex role | none beyond the type hypothesis | strictly less than $1$ |

## Vertex-role boundary locality

We first prove that for every original vertex role,

$$
\boxed{L_{\partial H}(T_i)=A_i+B_i.}
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
incident edges are initial intervals of lengths $B_0$ and $A_0$. It remains
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
L_{\partial H}(T_i)=A_i+B_i.
$$

Thus the nonsupercritical cap is immediate. For a supercritical V triangle, let $A$
and $B$ be its two incident-edge endpoints. The angle between the incident
edge directions is $120^\circ$, so

$$
\lVert A-B\rVert^2=A_i^2+A_ib_i+B_i^2.
$$

Both points lie in a unit equilateral triangle, whose diameter is $1$.
Consequently,

$$
1\ge A_i^2+A_ib_i+B_i^2
=\frac34(A_i+B_i)^2+\frac14(A_i-B_i)^2
\ge\frac34(A_i+B_i)^2.
$$

Hence

$$
L_{\partial H}(T_i)=A_i+B_i\le\frac{2}{\sqrt3}.
$$

The weak inequality is necessary: with $r=1/\sqrt3$, the local unit triangle

$$
\mathrm{conv}\left\{(r,0),(0,r),(-r,-r)\right\}
$$

is a Vd0 equality example.

## Vd1/Vd2 cap

Let $A_i,B_i$ be the exact incident-edge reaches of an original Vd1 or
Vd2 vertex role.  The shared corner-normal-form theorem
[`2014_Vd1_Vd2_corner_normal_form.md`](../20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md)
proves directly, including both reflected adjacent-support orientations, that

$$
A_i+B_i<\frac12.
$$

Therefore

$$
L_{\partial H}(T_i)=A_i+B_i<\frac12.
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

## Boundary-complete (zero-gap) consequences

Call the six V roles **boundary-complete** when

$$
\partial H\subset U_0\cup\cdots\cup U_5.
$$

With the canonical gap count in
[`0910`](../../09XX_appendices/0910_notation_dictionary.md), this is equivalent
in a hypothetical cover to $N_{\rm gap}=0$. One direction is immediate.
Conversely, if the V roles miss a boundary point, that point is not a vertex
because $V_i\in U_i$ for every $i$. The open C role must cover the missed
point, and openness then gives a positive-length C-triangle trace around it.
The complement of the two incident V traces is a nonempty closed interval,
possibly a singleton, and hence is a boundary gap inside that positive C
trace. Thus the zero-gap branches are exactly the boundary-complete branches.

The following two consequences do not depend on the CE type of $T_C$.

### Corollary

Suppose the six open V roles are boundary-complete. Then neither of the
following cases can occur:

1. $N_+=0$;
2. $N_+=1$ and at least one V role is Vd1 or Vd2.

### Proof

On $e_{i,i+1}$ only the two incident V roles can contain a
relative-interior point. Their relatively open traces cover the edge, so
connectedness forces a positive-length overlap. Hence

$$
1<B_i+A_{i+1}.
$$

Summing cyclically gives the strict boundary requirement

$$
6<\sum_{i=0}^5(A_i+B_i).
\tag{1}
$$

If $N_+=0$, every summand on the right side of (1) is at most $1$, a
contradiction.

Now suppose $N_+=1$ and choose a Vd1/Vd2 role. Its boundary trace is strictly
less than $1/2$, so it is not the unique supercritical role. The unique
supercritical role is therefore Vd0 and contributes at most $2/\sqrt3$. Each
of the other four nonsupercritical roles contributes at most $1$ by
vertex-role boundary locality. Boundary coverage would consequently require

$$
6
\le
\sum_{i=0}^5L_{\partial H}(T_i)
<
\frac12+\frac2{\sqrt3}+4
<6,
$$

again a contradiction. $\square$
