# CE2, $N_+=1$, One-Vd1 Adjacent-Rescue Obstruction

Status: Proven

This file records the normalized Vd1 midpoint-rescue obstruction used in the
CE2, $N_+=1$, exactly-one-Vd1/Vd2 branch.

It does **not** close the full
[`4140`](4140_CE2_Nplus1_exactly_one_Vd1_Vd2_TODO.md) branch.  It closes the
following normalized adjacent-rescue subcase and its reflection.

## Statement

Assume a seven-role cover is in the CE2, $N_+=1$, exactly-one-Vd1/Vd2 branch,
with roles

$$
T_C,T_0,T_1,\dots,T_5.
$$

Normalize the CE2 center so that

$$
T_C\cap\{M_0,\dots,M_5\}=\{M_0\},
$$

and so that its two positive boundary intervals are on $e_{5,0}$ and
$e_{0,1}$.

Assume further that, after reflection if necessary,

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
a_i+b_i\le1,\qquad i=2,3,4,5.
$$

Then the seven roles cannot cover the hexagon perimeter.  By reflection, the
same conclusion holds for the branch with $M_5\in T_0$ and $T_5$ the unique
supercritical row.

The proof uses the free strict supercritical envelope from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md)
and the CE1/CE2 side model used in
[`../413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md`](../413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md).

## Local coordinates for the Vd1 row

Use the normalized $V_0$ coordinates

$$
X=V_0+x(V_5-V_0)+y(V_1-V_0).
$$

Thus

$$
V_0=(0,0),\qquad V_5=(1,0),\qquad V_1=(0,1),\qquad O=(1,1),
$$

and the metric is

$$
\|(x,y)\|^2=x^2+y^2-xy.
$$

The adjacent boundary edges are

$$
e_{5,0}=\{(x,0):0\le x\le1\},
\qquad
e_{0,1}=\{(0,y):0\le y\le1\},
$$

and the adjacent rays are

$$
r_5=\{(1,y):0\le y\le1\},
\qquad
r_1=\{(x,1):0\le x\le1\}.
$$

A Vd1 row has exactly one triangle vertex outside $H$ and positive-length
intersection with exactly one adjacent ray.  In this normalized branch the
positive adjacent-ray intersection is on $r_1$, not on $r_5$.

Let $W$ be the unique outside vertex of $T_0$.  The two sides incident to $W$
are the two sides which face the $V_0$ corner.  They determine two nonnegative
intercepts $\alpha,\beta$ on the two adjacent edge-lines.  The actual boundary
coverage on $e_{5,0}$ is denoted by $a$; it satisfies

$$
a\le\alpha.
$$

The corresponding coverage on $e_{0,1}$ is not needed below.

After reflecting the local picture if necessary, the two unit side directions
issuing from $W$ may be written as

$$
(t+1,1),\qquad (t,t+1)
$$

for some $t>0$.  Their difference is $(1,-t)$.  All three vectors have squared
metric length

$$
D=t^2+t+1.
$$

Set

$$
d=\sqrt D.
$$

The triangle is therefore represented by the half-plane system

$$
x-(t+1)y\le\alpha,
$$

$$
ty-(t+1)x\le t\beta,
$$

and

$$
tx+y\le d-\alpha-t\beta.
$$

The first side cuts the $e_{5,0}$ line at $(\alpha,0)$, and the second side
cuts the $e_{0,1}$ line at $(0,\beta)$.

## The parameter satisfies $t\ge1$

On $r_1$, a point has the form $(x,1)$.  The first side is nonbinding there,
because

$$
x-(t+1)\le -t\le\alpha
$$

for $0\le x\le1$.  The second side gives the lower bound

$$
x\ge \frac{t(1-\beta)}{t+1},
$$

and the third side gives the upper bound

$$
x\le \frac{d-\alpha-t\beta-1}{t}.
$$

Let

$$
T_0\cap r_1=[c,u]
$$

where the coordinate is measured from $V_1$ toward $O$.  Since $M_1\in T_0$,

$$
c\le\frac12\le u.
$$

Also,

$$
t\beta\ge t-c(t+1).
$$

Indeed, if $\beta\le1$, then $c=t(1-\beta)/(t+1)$ and equality holds.  If
$\beta>1$, then $c=0$ and $t\beta>t=t-c(t+1)$.

The condition $M_1=(1/2,1)\in T_0$ gives, from the third side,

$$
\alpha+t\beta\le d-1-\frac t2.
$$

On $r_5$, a point has the form $(1,y)$.  The second side is nonbinding on the
unit segment because it gives only

$$
y\le 1+\frac1t+\beta>1.
$$

The first and third sides give

$$
y\ge \frac{1-\alpha}{t+1}
$$

and

$$
y\le d-\alpha-t\beta-t.
$$

Set

$$
U_5=d-\alpha-t\beta-t.
$$

From the midpoint inequality above,

$$
U_5\ge1-\frac t2.
$$

Because the row is Vd1 on the $r_1$ branch, $T_0\cap r_5$ has no positive
length.

If $\alpha\le1$, then $(1-\alpha)/(t+1)\ge0$, so no positive $r_5$ interval
implies

$$
U_5\le\frac{1-\alpha}{t+1}\le\frac1{t+1}.
$$

Consequently,

$$
1-\frac t2\le\frac1{t+1},
$$

which is equivalent to $t\ge1$.

If $\alpha>1$, then $(1-\alpha)/(t+1)<0$.  In that case no positive $r_5$
interval implies $U_5\le0$.  Since $U_5\ge1-t/2$, we get $t\ge2$.  Hence in all
cases

$$
\boxed{t\ge1.}
$$

## The local edge inequality

Define

$$
B(c)=\frac{c+\sqrt{c^2-8c+4}}2,
\qquad
A(c)=1-B(c).
$$

The function $B$ is the strict free supercritical outgoing-edge envelope from
`2010` on $0\le c<1/2$.

We first prove

$$
\boxed{a\le A(c).}
$$

Since $a\le\alpha$, it is enough to prove $\alpha\le A(c)$.

From

$$
\alpha+t\beta\le d-1-\frac t2
$$

and

$$
t\beta\ge t-c(t+1),
$$

we obtain

$$
\alpha\le d-1-\frac{3t}{2}+c(t+1).
$$

Define

$$
F(t,c)=\sqrt{t^2+t+1}-1-\frac{3t}{2}+c(t+1).
$$

Then

$$
\alpha\le F(t,c).
$$

For $t\ge1$,

$$
\frac{\partial F}{\partial t}
=
\frac{2t+1}{2\sqrt{t^2+t+1}}-\frac32+c.
$$

Since $c\le1/2$,

$$
\frac{\partial F}{\partial t}
\le
\frac{2t+1}{2\sqrt{t^2+t+1}}-1.
$$

But

$$
(2t+1)^2<4(t^2+t+1),
$$

so

$$
\frac{2t+1}{2\sqrt{t^2+t+1}}<1.
$$

Hence $F$ is strictly decreasing in $t$ on $[1,\infty)$, and therefore

$$
F(t,c)\le F(1,c)=\sqrt3-\frac52+2c.
$$

Set

$$
L(c)=\sqrt3-\frac52+2c.
$$

Thus

$$
0\le\alpha\le L(c)
$$

for every feasible row in this branch.

We now compare $L(c)$ with $A(c)$.  In fact,

$$
2L(c)\le A(c)
$$

for $0\le c\le1/2$.  This inequality is equivalent to

$$
\sqrt{c^2-8c+4}\le12-4\sqrt3-9c.
$$

The right side is positive on $0\le c\le1/2$, since its minimum there is
$15/2-4\sqrt3>0$.  Squaring is therefore valid.  The squared difference is

$$
(12-4\sqrt3-9c)^2-(c^2-8c+4)=4Q(c),
$$

where

$$
Q(c)=20c^2+(18\sqrt3-52)c+47-24\sqrt3.
$$

On $0\le c\le1/2$,

$$
Q'(c)=40c+18\sqrt3-52\le 18\sqrt3-32<0.
$$

Thus $Q$ is decreasing, so its minimum occurs at $c=1/2$.  There,

$$
Q\left(\frac12\right)=26-15\sqrt3>0,
$$

because $26^2>15^2\cdot3$.  Therefore $Q(c)>0$ throughout the interval and

$$
2L(c)\le A(c).
$$

Since $0\le\alpha\le L(c)$, we conclude

$$
\alpha\le A(c),
$$

and hence

$$
\boxed{a\le A(c).}
$$

## A stronger local inequality

Let

$$
\delta=1-u,
$$

where $u$ is the upper endpoint of $T_0\cap r_1$, measured from $V_1$ toward
$O$.

A Vd1 row in this branch cannot contain $O$.  If it contained both $V_0$ and
$O$, then the distance-one pair $V_0,O$ would be two vertices of the unit
triangle.  The third vertex would be $V_1$ or $V_5$, giving no outside vertex
of $T_0$ and hence not Vd1.  Therefore $u<1$ and $\delta>0$.

The third side gives

$$
u=\frac{d-\alpha-t\beta-1}{t}.
$$

Consequently,

$$
\delta
=
\frac{t+1+\alpha+t\beta-d}{t}.
$$

Using $t\beta\ge t-c(t+1)$,

$$
\delta\ge
\frac{2t+1+\alpha-c(t+1)-d}{t}
=
\delta_0+\frac{\alpha}{t},
$$

where

$$
\delta_0=\frac{2t+1-c(t+1)-d}{t}.
$$

Since $c\le1/2$,

$$
2t+1-c(t+1)-d
\ge
\frac{3t+1}{2}-d.
$$

For $t\ge1$,

$$
\left(\frac{3t+1}{2}\right)^2-(t^2+t+1)=\frac{5t^2+2t-3}{4}>0.
$$

Hence $\delta_0>0$.

For fixed $t,c$, the function

$$
z\mapsto \frac{z}{z+\delta_0+z/t}
$$

is increasing for $z\ge0$.  Since $a\le\alpha\le F(t,c)$ and
$\delta\ge\delta_0+\alpha/t$, we have

$$
\frac{a}{a+\delta}\le\frac{\alpha}{\alpha+\delta}\le
\frac{\alpha}{\alpha+\delta_0+\alpha/t}\le
\frac{F(t,c)}{F(t,c)+1/2}.
$$

The last denominator is correct because

$$
\delta_0+\frac{F(t,c)}{t}=\frac12.
$$

As above, $0\le F(t,c)\le L(c)$, and $z/(z+1/2)$ is increasing for $z\ge0$.
Thus

$$
\frac{a}{a+\delta}\le\frac{L(c)}{L(c)+1/2}\le2L(c)\le A(c).
$$

Therefore

$$
\boxed{
\frac{a}{a+\delta}\le A(c).
}
$$

Equivalently,

$$
\boxed{
\frac{a}{a+1-u}\le A(c).
}
$$

## CE2 hiding inequality

Let the CE2 center interval on $e_{5,0}$ be

$$
T_C\cap e_{5,0}=[S,T].
$$

Let $h$ be the boundary length on $e_{5,0}$ that $T_5$ is forced to cover,
measured from $V_5$ toward $V_0$.  If $T_5$ must reach the point with
$V_0$-based coordinate $y$, then

$$
h=1-y.
$$

We prove

$$
\boxed{h\ge B(c).}
$$

The cases $T\le a$ and $a<S$ are immediate.  In either case, the open boundary
gap after the $T_0$ interval forces $T_5$ to reach the point with $V_0$-based
coordinate $a$.  Therefore

$$
h\ge1-a\ge1-A(c)=B(c).
$$

It remains to handle the only hiding case,

$$
S\le a<T.
$$

Use the CE1/CE2 side model.  There are parameters

$$
0<\lambda<1,
\qquad
\rho=\sqrt{1-\lambda+\lambda^2},
$$

and nonnegative center slacks

$$
X\ge0,\qquad Y\ge0,
$$

such that

$$
S=\frac{X+Y+1-\rho}{1-\lambda},
\qquad
T=X+\lambda.
$$

Moreover, if $d_1$ is the length of $T_C\cap r_1$, measured from $O$ toward
$V_1$, then

$$
d_1\le\frac{Y}{\lambda}.
$$

The first point of $T_0\cap r_1$ measured from $O$ toward $V_1$ is

$$
\delta=1-u.
$$

The rows $T_2,T_3,T_4,T_5$ are Vd0 rows and have no positive-length support on
$r_1$.  The supercritical row $T_1$ contains no local midpoint, so it cannot
cover a neighborhood of $M_1$ on $r_1$.  Since $T_C$ contains $O$ and excludes
$M_1$, convexity also prevents $T_C$ from covering any point on the $V_1$-side
of $M_1$: otherwise the segment from that point to $O$ would contain $M_1$.
Thus the $O$-side gap on $r_1$ before the $T_0$ interval must be covered by
$T_C$, and hence

$$
d_1\ge\delta.
$$

Therefore

$$
Y\ge\lambda\delta.
$$

From $S\le a$,

$$
X\le (1-\lambda)a-Y-1+\rho.
$$

Using $Y\ge\lambda\delta$ gives

$$
X\le (1-\lambda)a-\lambda\delta-1+\rho.
$$

Since $X\ge0$ and $\rho\le1$,

$$
\lambda\delta\le(1-\lambda)a.
$$

Equivalently,

$$
\lambda\le\frac{a}{a+\delta}.
$$

Also,

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

In the hiding case $T>a$, this inequality forces $u>a$.  Hence

$$
T\le a+\frac{a}{a+\delta}(u-a).
$$

Since $\delta=1-u$, the right-hand side simplifies to

$$
a+\frac{a}{a+\delta}(u-a)=\frac{a}{a+\delta}.
$$

By the stronger local inequality,

$$
\frac{a}{a+\delta}\le A(c).
$$

Thus

$$
T\le A(c).
$$

In the hiding case $h=1-T$, and therefore

$$
h=1-T\ge1-A(c)=B(c).
$$

This proves $h\ge B(c)$ in all cases.

## Supercritical envelope and boundary contradiction

Let $c_1$ be the own-radial coverage coordinate of the supercritical row
$T_1$ on $r_1$, measured from $V_1$ toward $O$.

Since $T_0\cap r_1=[c,u]$, the segment of $r_1$ from $V_1$ up to coordinate
$c$ is not covered by $T_0$.  The rows $T_2,T_3,T_4,T_5$ are Vd0 and have no
positive-length support on $r_1$.  The center triangle $T_C$ cannot cover any
point on the $V_1$-side of $M_1$, as explained above.  Hence coverage of $r_1$
forces

$$
c_1\ge c.
$$

If $c=1/2$, then $c_1\ge1/2$, which is incompatible with a strict
supercritical row under the free supercritical envelope.  Thus a putative
cover has

$$
0\le c<\frac12.
$$

The strict free supercritical envelope gives

$$
b_1<B(c_1).
$$

The function $B$ is strictly decreasing on $[0,1/2]$; this is the derivative
check recorded in the exactly-one-T3-like boundary obstruction.  Since
$c_1\ge c$,

$$
\boxed{b_1<B(c).}
$$

Together with $h\ge B(c)$, this gives

$$
h-b_1>0.
$$

Now sum the ordinary boundary obligations.  The edge $e_{1,2}$ gives

$$
a_2\ge1-b_1.
$$

The three full edges $e_{2,3}$, $e_{3,4}$, and $e_{4,5}$ give

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

Adding these five inequalities yields

$$
\sum_{i=2}^5(a_i+b_i)
=
a_2+(b_2+a_3)+(b_3+a_4)+(b_4+a_5)+b_5
\ge
(1-b_1)+1+1+1+h.
$$

Therefore

$$
\sum_{i=2}^5(a_i+b_i)\ge4+(h-b_1)>4.
$$

But $T_2,T_3,T_4,T_5$ are nonsupercritical Vd0 rows, so

$$
a_i+b_i\le1,\qquad i=2,3,4,5,
$$

and hence

$$
\sum_{i=2}^5(a_i+b_i)\le4.
$$

This contradiction proves that the normalized Vd1 adjacent-rescue branch cannot
cover the hexagon perimeter.

## Boundary cases

The argument uses strictness only in the supercritical envelope step.  The
local inequalities $a\le A(c)$ and $a/(a+1-u)\le A(c)$ are closed inequalities.
The strict contradiction comes from

$$
b_1<B(c)\le h.
$$

Point-only contacts on $r_1$ or $e_{5,0}$ do not affect the argument, because
both Vd1 and the perimeter covering constraints are measured by positive-length
intervals in the open-boundary accounting.

## Numerical check

A direct sampler over the above normal form was used only as a check.  The
sampler retained parameters satisfying:

$$
t\ge1,
\qquad
c\le\frac12\le u,
$$

positive-length $r_1$ intersection, and no positive-length $r_5$ intersection.
It tested the two quantities

$$
a-A(c)
$$

and

$$
T-A(c)
$$

in the CE2 hiding model.  No positive value was found.  The numerical check is
not used in the proof above; it only supports the algebraic inequalities.
