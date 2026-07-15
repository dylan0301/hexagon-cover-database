# CE2, $N_+=1$, $T_0$ Vd1 With $M_1\in T_0$ And $T_1$ Supercritical

Status: Proven

This file proves the normalized adjacent-rescue Vd1 subcase in the
[`4140`](4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md) branch.

The proof uses the Vd1 corner normal form in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md)
and the free strict-supercritical envelope in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md).

## Statement

Assume a reduced 414X perimeter-cover candidate has the following normalized
form:

$$
T_C\text{ is CE2},
$$

$$
T_C\cap\{M_0,\dots,M_5\}=\{M_0\},
$$

$$
T_0\text{ is the unique Vd1 row},
\qquad
M_1\in T_0,
$$

$$
T_1\text{ is the unique supercritical row},
$$

and

$$
T_2,T_3,T_4,T_5
$$

are Vd0 rows satisfying

$$
a_i+b_i\le1,
\qquad
 i=2,3,4,5.
$$

Then these seven role triangles cannot cover the hexagon perimeter together
with the radial arm $r_1$.

By reflection, the same conclusion holds for the branch

$$
T_0\text{ Vd1},\qquad M_5\in T_0,\qquad T_5\text{ supercritical}.
$$

## Local Vd1 data

Use the normalized coordinates of `2014`. Let $a,b$ be the exact boundary
reaches of $T_0$. The normal form gives $t>0$ and

$$
d=\sqrt{t^2+t+1}
$$

such that

$$
\begin{aligned}
x-(t+1)y&\le a,\\
ty-(t+1)x&\le tb,\\
tx+y&\le d-a-tb.
\end{aligned}
$$

Write

$$
T_0\cap r_1=[c,u]
$$

in the coordinate from $V_1$ toward $O$. Then

$$
c=\frac{t(1-b)}{t+1},
\qquad
u=\frac{d-a-tb-1}{t}.
$$

The midpoint condition gives

$$
c\le\frac12\le u,
$$

and hence

$$
tb=t-c(t+1),
\qquad
a+tb\le d-1-\frac t2.
$$

Because $a<1$, the raw lower endpoint on $r_5$ is positive. If $t<1$, the
last inequality gives

$$
d-a-tb-t\ge1-\frac t2>\frac1{t+1}>
\frac{1-a}{t+1},
$$

forcing positive-length $r_5$ support. This contradicts the Vd1 hypothesis.
Therefore

$$
\boxed{t\ge1.}
$$

## The local comparison functions

For $0\le s\le1/2$, define

$$
B(s):=\frac{s+\sqrt{s^2-8s+4}}2,
\qquad
A(s):=1-B(s).
$$

The function $B$ is the nonattained free strict-supercritical outgoing-edge
supremum on $0\le s<1/2$.

We shall prove

$$
\boxed{a\le A(c)}
$$

and the stronger auxiliary estimate

$$
\boxed{\frac{a}{a+1-u}\le A(c)}.
$$

The latter is the estimate needed when the CE2 boundary interval hides the gap
after $T_0$ on $e_{5,0}$.

## Proof of $a\le A(c)$

From

$$
a+tb\le d-1-\frac t2
$$

and

$$
tb=t-c(t+1),
$$

we get

$$
a\le d-1-\frac{3t}{2}+c(t+1).
$$

Set

$$
F(t,c):=\sqrt{t^2+t+1}-1-\frac{3t}{2}+c(t+1).
$$

Then

$$
a\le F(t,c).
$$

For fixed $c\le1/2$,

$$
\frac{\partial F}{\partial t}
=
\frac{2t+1}{2\sqrt{t^2+t+1}}-\frac32+c
\le
\frac{2t+1}{2\sqrt{t^2+t+1}}-1.
$$

Since

$$
(2t+1)^2<4(t^2+t+1),
$$

the last expression is strictly negative.  Thus $F(t,c)$ is decreasing in $t$
for $t\ge1$, and therefore

$$
F(t,c)\le F(1,c)=\sqrt3-\frac52+2c.
$$

Write

$$
L(c):=\sqrt3-\frac52+2c.
$$

Since $a\ge0$ and $a\le F(t,c)\le L(c)$, every feasible row has
$L(c)\ge0$.

We prove the stronger estimate

$$
2L(c)\le A(c)
$$

for $0\le c\le1/2$.  Let

$$
R(c):=\sqrt{c^2-8c+4}.
$$

The inequality $2L(c)\le A(c)$ is equivalent to

$$
R(c)\le12-4\sqrt3-9c.
$$

The right-hand side is positive on $0\le c\le1/2$, since its minimum there is
$15/2-4\sqrt3>0$.  Squaring is legitimate.  The squared difference is

$$
(12-4\sqrt3-9c)^2-(c^2-8c+4)=4Q(c),
$$

where

$$
Q(c)=20c^2+(18\sqrt3-52)c+47-24\sqrt3.
$$

On $0\le c\le1/2$,

$$
Q'(c)=40c+18\sqrt3-52\le20+18\sqrt3-52=18\sqrt3-32<0.
$$

Thus $Q$ is decreasing on this interval.  Its minimum occurs at $c=1/2$, where

$$
Q\left(\frac12\right)=26-15\sqrt3>0.
$$

Therefore $Q(c)>0$ throughout $0\le c\le1/2$, so

$$
2L(c)\le A(c).
$$

Combining the inequalities gives

$$
a\le L(c)\le A(c).
$$

Thus $\boxed{a\le A(c)}$.

## The auxiliary estimate

Set

$$
\delta:=1-u.
$$

A Vd1 row in this branch cannot contain $O$.  If it contained both $V_0$ and
$O$, then the distance-one pair $V_0,O$ would be two vertices of the unit
triangle.  The third vertex would be $V_1$ or $V_5$, giving no outside vertex
of $T_0$ and hence not Vd1.  Therefore $u<1$ and $\delta>0$.

The third side gives

$$
u=\frac{d-a-tb-1}{t}.
$$

Consequently,

$$
\delta
=
\frac{t+1+a+tb-d}{t}.
$$

Using $tb=t-c(t+1)$,

$$
\delta=
\frac{2t+1+a-c(t+1)-d}{t}
=
\delta_0+\frac{a}{t},
$$

where

$$
\delta_0:=\frac{2t+1-c(t+1)-d}{t}.
$$

Because $c\le1/2$,

$$
2t+1-c(t+1)-d
\ge
\frac{3t+1}{2}-d.
$$

For $t\ge1$,

$$
\left(\frac{3t+1}{2}\right)^2-(t^2+t+1)=\frac{5t^2+2t-3}{4}>0.
$$

Hence

$$
\delta_0>0.
$$

The function

$$
z\mapsto \frac{z}{z+\delta_0+z/t}
$$

is increasing for $z\ge0$. Since $a\le F(t,c)$ and
$\delta=\delta_0+a/t$, we get

$$
\frac{a}{a+\delta}
\le
\frac{F(t,c)}{F(t,c)+1/2}.
$$

The denominator is $F(t,c)+1/2$ because

$$
\delta_0+\frac{F(t,c)}t=\frac12.
$$

Since $F(t,c)\le L(c)$ and $z\mapsto z/(z+1/2)$ is increasing for $z\ge0$,

$$
\frac{a}{a+\delta}
\le
\frac{L(c)}{L(c)+1/2}.
$$

Also,

$$
\frac{L(c)}{L(c)+1/2}\le2L(c),
$$

because $L(c)+1/2\ge1/2$.  From the previous section,

$$
2L(c)\le A(c).
$$

Therefore

$$
\boxed{\frac{a}{a+\delta}\le A(c).}
$$

Since $\delta=1-u$, this is

$$
\boxed{\frac{a}{a+1-u}\le A(c).}
$$

## CE2 hiding inequality

Write the CE2 center interval on $e_{5,0}$ as

$$
T_C\cap e_{5,0}=[S,T].
$$

Let $h$ denote the forced boundary reach of $T_5$ on $e_{5,0}$, measured from
$V_5$ toward $V_0$.

There are three cases.

### Case 1: $T\le a$

The Vd1 row covers the far endpoint of the CE2 interval.  The remaining tail of
$e_{5,0}$ forces

$$
h\ge1-a.
$$

Since $a\le A(c)$,

$$
h\ge1-A(c)=B(c).
$$

### Case 2: $a<S$

The CE2 interval begins after the end of the $T_0$ boundary interval.  The open
gap after coordinate $a$ again forces

$$
h\ge1-a\ge B(c).
$$

### Case 3: $S\le a<T$

This is the only hiding case.  We prove

$$
T\le A(c).
$$

Use the CE1/CE2 side model recorded in the proven exactly-one-T3-like
obstruction
[`../413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md`](../413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md).
There are parameters

$$
0<\lambda<1,
\qquad
\rho=\sqrt{1-\lambda+\lambda^2},
$$

and nonnegative slacks

$$
X\ge0,
\qquad
Y\ge0,
$$

such that

$$
S=\frac{X+Y+1-\rho}{1-\lambda},
\qquad
T=X+\lambda.
$$

Also, if $d_1$ is the length of $T_C\cap r_1$ measured from $O$ toward $V_1$,
then

$$
d_1\le\frac{Y}{\lambda}.
$$

The first point of $T_0\cap r_1=[c,u]$ measured from $O$ toward $V_1$ is

$$
\delta=1-u.
$$

The rows $T_2,T_3,T_4,T_5$ are Vd0 and have no positive-length support on
$r_1$.  The supercritical row $T_1$ cannot cover $M_1$.  The center triangle
$T_C$ contains $O$ and excludes $M_1$; by convexity, it cannot cover any point
strictly on the $V_1$-side of $M_1$, because the segment from such a point to
$O$ contains $M_1$.  Hence the $O$-side radial gap of length $\delta$ before
the Vd1 interval must be covered by $T_C$, and so

$$
d_1\ge\delta.
$$

Therefore

$$
Y\ge\lambda\delta.
$$

From $S\le a$,

$$
X\le(1-\lambda)a-Y-1+\rho.
$$

Using $Y\ge\lambda\delta$ gives

$$
X\le(1-\lambda)a-\lambda\delta-1+\rho.
$$

Since $X\ge0$ and $\rho\le1$,

$$
\lambda\delta\le(1-\lambda)a.
$$

Equivalently,

$$
\lambda\le\frac{a}{a+\delta}.
$$

Now

$$
T=X+\lambda
\le
(1-\lambda)a-\lambda\delta-1+\rho+\lambda.
$$

Since $\delta=1-u$,

$$
T\le a+\rho-1+\lambda(u-a).
$$

As $\rho\le1$,

$$
T\le a+\lambda(u-a).
$$

In the hiding case $T>a$, the last inequality forces $u>a$.  Hence, using
$\lambda\le a/(a+\delta)$,

$$
T\le a+\frac{a}{a+\delta}(u-a).
$$

Because $\delta=1-u$,

$$
a+\frac{a}{a+\delta}(u-a)=\frac{a}{a+\delta}.
$$

Thus

$$
T\le\frac{a}{a+\delta}.
$$

The auxiliary estimate gives

$$
\frac{a}{a+\delta}\le A(c).
$$

Therefore

$$
T\le A(c).
$$

Since in the hiding case $h\ge1-T$, we obtain

$$
h\ge1-A(c)=B(c).
$$

Combining all cases,

$$
\boxed{h\ge B(c).}
$$

## Supercritical envelope and boundary contradiction

Let $c_1$ be the own-radial coverage coordinate of the supercritical row $T_1$
on $r_1=[V_1,O]$, measured from $V_1$ toward $O$.

The interval $T_0\cap r_1=[c,u]$ leaves the segment from $V_1$ to coordinate
$c$ uncovered by $T_0$.  The rows $T_2,T_3,T_4,T_5$ are Vd0 and have no
positive-length support on $r_1$.  The center triangle $T_C$ cannot cover a
point of $r_1$ strictly on the $V_1$-side of $M_1$, because $O\in T_C$ and
convexity would then force $M_1\in T_C$, contrary to the exact-midpoint
normalization.  Hence perimeter and skeleton coverage force

$$
c_1\ge c.
$$

If $c=1/2$, then $c_1\ge1/2$, impossible for a strict supercritical row under
the free strict supercritical envelope.  Thus in a genuine candidate

$$
0\le c<\frac12.
$$

The strict supercritical envelope gives

$$
b_1<B(c_1).
$$

The function $B$ is strictly decreasing on $[0,1/2]$.  Indeed,

$$
B'(s)=\frac12\left(1+\frac{s-4}{\sqrt{s^2-8s+4}}\right)<0,
$$

because

$$
(4-s)^2-(s^2-8s+4)=12>0.
$$

Since $c_1\ge c$,

$$
\boxed{b_1<B(c).}
$$

The CE2 hiding analysis proved

$$
h\ge B(c),
$$

so

$$
h-b_1>0.
$$

Now sum the boundary obligations along the four ordinary Vd0 rows.  The edge
$e_{1,2}$ gives

$$
a_2\ge1-b_1.
$$

The full ordinary edges give

$$
b_2+a_3\ge1,
$$

$$
b_3+a_4\ge1,
$$

and

$$
b_4+a_5\ge1.
$$

The $e_{5,0}$ analysis gives

$$
b_5\ge h.
$$

Adding,

$$
\sum_{i=2}^5(a_i+b_i)
=
a_2+(b_2+a_3)+(b_3+a_4)+(b_4+a_5)+b_5
$$

satisfies

$$
\sum_{i=2}^5(a_i+b_i)
\ge
(1-b_1)+1+1+1+h
=
4+(h-b_1)>4.
$$

But $T_2,T_3,T_4,T_5$ are nonsupercritical Vd0 rows, hence

$$
a_i+b_i\le1,
\qquad
 i=2,3,4,5.
$$

Therefore

$$
\sum_{i=2}^5(a_i+b_i)\le4,
$$

a contradiction.  This proves the normalized $T_0$ Vd1, $M_1\in T_0$,
$T_1$ supercritical obstruction.

## Boundary cases

The proof is strict at the final step because $T_1$ is strictly
supercritical, so the free envelope gives $b_1<B(c_1)$ rather than a closed
inequality.  The case $c=1/2$ is excluded because the strict supercritical
feasible set is empty at radial coordinate $1/2$.

Point-only contacts on $r_5$ do not affect the Vd1 type, because Vd1 excludes
positive-length $r_5$ intersection only. The exact normal form has $a<1$, so
the $t\ge1$ argument includes all endpoint configurations relevant to an
original open role.

$$
\Box
$$
