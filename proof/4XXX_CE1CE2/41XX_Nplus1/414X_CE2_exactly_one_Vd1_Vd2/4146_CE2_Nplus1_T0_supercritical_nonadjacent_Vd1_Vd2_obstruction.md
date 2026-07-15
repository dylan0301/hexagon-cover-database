# CE2, $N_+=1$, $T_0$ Supercritical And Non-Adjacent Vd1/Vd2

Status: Proven

This file proves the non-adjacent placements in the
[`4140`](4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md) branch:

$$
T_C\text{ is CE2},\qquad T_0\text{ is the unique supercritical row},
\qquad T_\tau\text{ is the unique Vd1/Vd2 row},
\qquad \tau\in\{2,3,4\}.
$$

It uses the Vd1/Vd2 corner normal form from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md),
the boundary cap from
[`../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md),
and the CE2 interval-pair model from
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md).

## Statement

Assume a reduced 414X candidate satisfies

$$
T_C\text{ is CE2},
\qquad
T_C\cap\{M_0,\dots,M_5\}=\{M_0\},
$$

$$
T_0\text{ is the unique supercritical row},
\qquad
T_\tau\text{ is the unique Vd1/Vd2 row for }\tau\in\{2,3,4\},
$$

and every other vertex row is Vd0 and nonsupercritical. Then the seven roles
cannot cover the hexagon perimeter together with $r_\tau$.

## CE2 notation

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

The CE2 interval-pair model gives

$$
0<x<u<1,
\qquad
0<y<v<1,
$$

$$
(u+v)S-xy=D,
$$

and

$$
uS\ge x,
\qquad
vS\ge y.
$$

Let

$$
P:=vS-y,
\qquad
Q:=uS-x.
$$

Then $P,Q\ge0$ and

$$
P+Q=(u+v-1)S.
$$

The center-triangle lengths on the non-adjacent diagonals, measured from $O$
toward the corresponding vertex, are

$$
d_2^C=\frac{P}{S},
$$

$$
d_4^C=\frac{Q}{S},
$$

and

$$
d_3^C=\min\left(\frac{P}{y},\frac{Q}{x}\right).
$$

For $r_2$ and $r_4$ this follows from the active CE2 slacks $P-qS$ and
$Q-qS$.  For $r_3$ the active slacks are $P-qy$ and $Q-qx$.

## Boundary demands

Let $(a_0,b_0)$ be the boundary coordinates of the supercritical row $T_0$.
Then

$$
a_0+b_0>1
$$

and the distance between the two adjacent boundary endpoints gives

$$
a_0^2+a_0b_0+b_0^2\le1.
$$

Define the farthest already-covered extents on the two CE2-active edges by

$$
B:=1-A,
\qquad
U:=1-H.
$$

Equivalently,

$$
B=
\begin{cases}
b_0,& b_0<y,\\
\max(b_0,v),& b_0\ge y,
\end{cases}
$$

and

$$
U=
\begin{cases}
a_0,& a_0<x,\\
\max(a_0,u),& a_0\ge x.
\end{cases}
$$

Boundary coverage and propagation through ordinary nonsupercritical Vd0 rows
force

$$
a_\tau\ge A,
\qquad
b_\tau\ge H.
$$

Both $A$ and $H$ are positive. The CE2 endpoints satisfy $u,v<1$. If an
alternative endpoint were supplied by $a_0=1$ or $b_0=1$, the diameter bound

$$
a_0^2+a_0b_0+b_0^2\le1
$$

would force the other coordinate to be zero, contradicting the strict
supercritical condition $a_0+b_0>1$.

By the Vd1/Vd2 boundary cap in `2500`,

$$
a_\tau+b_\tau<\frac12.
$$

Hence

$$
A+H<\frac12.
$$

## Boundary extent lemma

Define

$$
b_\circ(z)=\frac{-z+\sqrt{4-3z^2}}2.
$$

This is the larger nonnegative solution of

$$
z^2+zw+w^2=1.
$$

We prove

$$
B\le b_\circ(x),
\qquad
U\le b_\circ(y).
$$

It is enough to prove the first inequality; the second is its reflection.

If $B=v$, then $T_C$ contains the boundary point with coordinate $x$ on
$e_{5,0}$ and the boundary point with coordinate $v$ on $e_{0,1}$.  Their
squared distance is

$$
x^2+xv+v^2.
$$

Since both points lie in a unit equilateral triangle,

$$
x^2+xv+v^2\le1,
$$

so

$$
v\le b_\circ(x).
$$

Thus $B\le b_\circ(x)$ in this case.

If $B=b_0$, suppose first that $a_0<x$.  Then $U=a_0$, and

$$
A+H=(1-b_0)+(1-a_0)<\frac12
$$

would imply

$$
a_0+b_0>\frac32.
$$

But

$$
a_0^2+a_0b_0+b_0^2\le1
$$

implies

$$
a_0+b_0\le\frac2{\sqrt3}<\frac32,
$$

a contradiction.  Hence $a_0\ge x$.  The disk inequality and the monotonicity
of $b_\circ$ give

$$
b_0\le b_\circ(a_0)\le b_\circ(x).
$$

Therefore $B\le b_\circ(x)$ in all cases.

## CE2 comparison lemma

We prove that for $0<x,y<1$,

$$
\frac{D+xy}{S}+b_\circ(x)<2.
$$

Let

$$
b=b_\circ(x),
\qquad
R=2-b.
$$

It is enough to prove

$$
D<R(x+y)-xy.
$$

Set

$$
F(y)=R(x+y)-xy-D.
$$

The expression before the square root is positive.  Squaring is legitimate, so
consider

$$
G(y)=\left(xR+(R-x)y\right)^2-(x^2+xy+y^2).
$$

The coefficient of $y^2$ is

$$
(R-x)^2-1.
$$

Since $b+x\ge1$, we have $R-x=2-b-x\le1$.  Thus $G$ is concave in $y$, so its
minimum on $0\le y\le1$ occurs at an endpoint.

At $y=0$,

$$
G(0)=x^2(R^2-1)>0.
$$

At $y=1$, the inequality $G(1)>0$ is equivalent, using
$b^2+xb+x^2=1$, to

$$
b(x^2+3x+4)+x^3+x^2-x-4<0.
$$

Substitute

$$
b=\frac{-x+\sqrt{4-3x^2}}2.
$$

The last inequality becomes

$$
\sqrt{4-3x^2}<\frac{-x^3+x^2+6x+8}{x^2+3x+4}.
$$

Both sides are positive.  Squaring gives

$$
\left(-x^3+x^2+6x+8\right)^2
-(4-3x^2)(x^2+3x+4)^2
=4x^2(x^4+4x^3+9x^2+11x+8)>0.
$$

Thus $G(1)>0$.  Since $G$ is concave and positive at both endpoints,
$G(y)>0$ for $0<y<1$.  Therefore

$$
D<R(x+y)-xy,
$$

and hence

$$
\frac{D+xy}{S}+b_\circ(x)<2.
$$

By reflection,

$$
\frac{D+xy}{S}+b_\circ(y)<2.
$$

## Consequence for $A$ and $H$

Since

$$
u+v=\frac{D+xy}{S},
$$

and

$$
B\le b_\circ(x),
\qquad
U\le b_\circ(y),
$$

the CE2 comparison lemma gives

$$
u+v+B<2,
\qquad
u+v+U<2.
$$

Because $B=1-A$ and $U=1-H$, this is

$$
u+v-1<A,
\qquad
u+v-1<H.
$$

Thus

$$
\boxed{u+v-1<\min(A,H).}
$$

Let

$$
m=\min(A,H).
$$

Then

$$
u+v-1<m.
$$

## Non-adjacent diagonal inequalities

Since

$$
P+Q=(u+v-1)S,
$$

we have

$$
P+Q<mS.
$$

Because $P,Q\ge0$,

$$
d_2^C=\frac{P}{S}\le\frac{P+Q}{S}<m,
$$

and

$$
d_4^C=\frac{Q}{S}\le\frac{P+Q}{S}<m.
$$

For $r_3$, suppose for contradiction that

$$
d_3^C=\min\left(\frac{P}{y},\frac{Q}{x}\right)\ge m.
$$

Then

$$
P\ge my,
\qquad
Q\ge mx.
$$

Adding gives

$$
P+Q\ge m(x+y)=mS,
$$

contradicting $P+Q<mS$.  Hence

$$
d_3^C<m.
$$

Therefore

$$
\boxed{d_\tau^C<\min(A,H),\qquad \tau=2,3,4.}
$$

## Final contradiction

Let $\tau\in\{2,3,4\}$ and suppose $T_\tau$ is the unique Vd1/Vd2 row.
The boundary propagation gives

$$
a_\tau\ge A,
\qquad
b_\tau\ge H.
$$

In the Vd1/Vd2 corner normal form `2014`, the own-radial reach satisfies

$$
c_\tau=\frac{d-a_\tau-tb_\tau}{t+1},
\qquad
 d=\sqrt{t^2+t+1}.
$$

Since $d<t+1$,

$$
c_\tau<1-\frac{a_\tau+tb_\tau}{t+1}\le1-\min(A,H).
$$

The center triangle covers length $d_\tau^C$ from the center side of $r_\tau$,
so the vertex-side demand is

$$
q_\tau=1-d_\tau^C.
$$

Since

$$
d_\tau^C<\min(A,H),
$$

we get

$$
q_\tau>1-\min(A,H)>c_\tau.
$$

Thus $r_\tau$ is not covered.  This contradiction eliminates all non-adjacent
placements $\tau=2,3,4$.

$$
\Box
$$
