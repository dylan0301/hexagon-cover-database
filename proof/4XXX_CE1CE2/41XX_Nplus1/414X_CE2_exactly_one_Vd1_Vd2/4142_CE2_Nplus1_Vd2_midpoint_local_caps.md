# CE2, $N_+=1$, Vd2 Midpoint Local Caps

Status: Proven

This file records the local caps used in the
[`4140`](4140_CE2_Nplus1_exactly_one_Vd1_Vd2_TODO.md) branch to remove the
Vd2 midpoint-rescue subcases from the remaining CE2, $N_+=1$,
exactly-one-Vd1/Vd2 analysis.

The result is purely local.  It concerns a normalized $V_0$-triangle $T_0$ of
type Vd2 and its adjacent boundary coverages

$$
a=\text{coverage on }e_{5,0}\text{ from }V_0,\qquad
b=\text{coverage on }e_{0,1}\text{ from }V_0.
$$

The local type conventions are those of
[`../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md)
and the local $(a,b,c)$ coordinates are those of
[`../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md`](../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md).

## Statement

Let $T_0$ be a Vd2 triangle at $V_0$.

1. If the exact local midpoint subset is either

   $$
   \{M_0,M_1\}
   \qquad\text{or}\qquad
   \{M_0,M_5\},
   $$

   then

   $$
   \boxed{
   a+b<\frac{29-7\sqrt{13}}{12}.
   }
   $$

2. If the exact local midpoint subset is

   $$
   \{M_5,M_0,M_1\},
   $$

   then

   $$
   \boxed{
   a+b\le\sqrt3-\frac32.
   }
   $$

Both constants are below the perimeter-threshold value

$$
\frac32-\frac2{\sqrt3}.
$$

Indeed,

$$
\frac{29-7\sqrt{13}}{12}
<
\frac32-\frac2{\sqrt3},
\qquad
\sqrt3-\frac32
<
\frac32-\frac2{\sqrt3}.
$$

Thus either local cap is strong enough for the reduced perimeter accounting in
the 414X branch.

## Local coordinates

Use the affine local coordinates

$$
X=V_0+x(V_5-V_0)+y(V_1-V_0).
$$

Thus

$$
V_0=(0,0),\qquad V_5=(1,0),\qquad V_1=(0,1),
$$

$$
O=(1,1),
$$

and

$$
M_0=\left(\frac12,\frac12\right),\qquad
M_1=\left(\frac12,1\right),\qquad
M_5=\left(1,\frac12\right).
$$

The metric is

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

The local midpoint subsets in the statement are symmetric under the reflection
$x\leftrightarrow y$, which swaps $M_1$ and $M_5$ and swaps $a$ and $b$.

## Vd2 normal form

A Vd2 triangle has exactly one vertex outside $H$ and positive-length
intersection with both adjacent rays $r_5$ and $r_1$.  In the midpoint-rescue
subcases treated here, the unique outside vertex is the $V_0$-corner vertex of
the triangle: the two sides incident to it are exactly the two sides which
terminate the initial intervals on $e_{5,0}$ and $e_{0,1}$.

Indeed, if the side terminating one initial boundary interval were not incident
to the unique outside vertex, then the side through the outside vertex on that
side of the corner would separate $T_0$ from one adjacent ray, leaving at most a
point contact.  This contradicts the Vd2 condition that both adjacent rays have
positive-length intersection.  The same argument also excludes an outside
vertex in only one of the two exterior half-strips; otherwise the opposite
adjacent ray is separated from the triangle except for a possible endpoint
contact.

Therefore, after reflecting if necessary, there is a parameter

$$
t\ge1
$$

such that $T_0$ is represented by the three half-plane inequalities

$$
x-(t+1)y\le a,
$$

$$
ty-(t+1)x\le tb,
$$

and

$$
tx+y\le \sqrt{t^2+t+1}-a-tb.
$$

To check that this is a unit equilateral triangle, set

$$
D=t^2+t+1.
$$

The two side directions issuing from the outside vertex are

$$
(t+1,1),\qquad (t,t+1),
$$

and their difference is

$$
(1,-t).
$$

Each has squared metric length $D$.  After division by $\sqrt D$, these are
three unit side directions of a unit equilateral triangle.  The third
half-plane constant is chosen so that the side opposite the outside vertex is
at unit side distance.

The first side cuts $e_{5,0}$ at $(a,0)$ and the second side cuts $e_{0,1}$ at
$(0,b)$, so $a$ and $b$ are precisely the adjacent boundary coverage
coordinates.

## The one-adjacent midpoint cap

It is enough by reflection to prove the case in which the adjacent midpoint is
$M_1$ and $t\ge1$.  Thus assume

$$
M_1=\left(\frac12,1\right)\in T_0.
$$

Substituting $M_1$ into the second half-plane gives

$$
t-\frac{t+1}{2}\le tb,
$$

so

$$
b\ge L(t):=\frac{t-1}{2t}.
$$

Substituting $M_1$ into the third half-plane gives

$$
\frac t2+1\le \sqrt D-a-tb,
$$

or

$$
a+tb\le C_1(t):=\sqrt D-1-\frac t2.
$$

Write

$$
U=a+tb.
$$

Then

$$
a+b=U-(t-1)b.
$$

Since $t\ge1$ and $b\ge L(t)$,

$$
a+b\le U-(t-1)L(t).
$$

First suppose the upper value $U=C_1(t)$ is compatible with positive
$r_5$-intersection.  Then

$$
a+b\le C_1(t)-(t-1)L(t)
=
\sqrt D-t-\frac1{2t}.
$$

Define

$$
S_1(t):=\sqrt{t^2+t+1}-t-\frac1{2t}.
$$

For $t\ge1$,

$$
S_1'(t)=\frac{2t+1}{2\sqrt D}-1+\frac1{2t^2}.
$$

The inequality $S_1'(t)\ge0$ is equivalent to

$$
\frac{2t+1}{\sqrt D}\ge 2-\frac1{t^2}.
$$

Both sides are positive for $t\ge1$.  After squaring and multiplying by
$t^4D$, this becomes

$$
(2t+1)^2t^4\ge D(2t^2-1)^2.
$$

The difference is

$$
(2t+1)^2t^4-D(2t^2-1)^2=(t+1)(t^3+3t^2-1)>0
$$

for $t\ge1$.  Hence $S_1$ is strictly increasing on $[1,\infty)$.

Now determine where the upper value $U=C_1(t)$ ceases to be compatible with
positive $r_5$-intersection.  On $r_5$, write points as $(1,y)$.  The first and
third half-planes give

$$
y\ge\frac{1-a}{t+1}
$$

and

$$
y\le\sqrt D-a-tb-t.
$$

Thus positive-length intersection with $r_5$ requires

$$
\sqrt D-a-tb-t>\frac{1-a}{t+1}.
$$

At $U=C_1(t)$ and $b=L(t)$ this compatibility boundary is

$$
\sqrt D=\frac{D}{2}.
$$

Equivalently,

$$
D=4,
$$

or

$$
t^2+t-3=0.
$$

Set

$$
t_*=\frac{\sqrt{13}-1}{2}.
$$

Then $D(t_*)=4$.  Therefore, throughout the compatible range
$1\le t\le t_*$,

$$
a+b\le S_1(t)\le S_1(t_*).
$$

Since $D(t_*)=4$ and $t_*^2+t_*=3$,

$$
S_1(t_*)=2-t_*-\frac1{2t_*}
=
\frac{29-7\sqrt{13}}{12}.
$$

It remains to treat $t>t_*$.  In this range, positive $r_5$-intersection gives

$$
\sqrt D-U-t>\frac{1-U+tb}{t+1}.
$$

Equivalently,

$$
U+b<\frac{(t+1)(\sqrt D-t)-1}{t}.
$$

Using $b\ge L(t)$, we obtain

$$
a+b=U+b-tb
<
\frac{(t+1)(\sqrt D-t)-1}{t}-tL(t).
$$

The right-hand side simplifies to

$$
R(t):=\frac{2(t+1)\sqrt D-3t^2-t-2}{2t}.
$$

Differentiate:

$$
R'(t)=
\frac{
2t^3-3t^2\sqrt D+t^2-t+2\sqrt D-2
}{
2t^2\sqrt D
}.
$$

The numerator is

$$
2t^3+t^2-t-2+(2-3t^2)\sqrt D.
$$

For $t\ge1$, the coefficient $2-3t^2$ is negative and

$$
\sqrt D>t+\frac12.
$$

Hence the numerator is strictly less than

$$
2t^3+t^2-t-2+(2-3t^2)\left(t+\frac12\right)
=
-t^3-\frac12t^2+t-1<0.
$$

Thus $R$ is strictly decreasing on $[1,\infty)$.  Since
$R(t_*)=S_1(t_*)$, for $t>t_*$ we have

$$
a+b<R(t)<R(t_*)=S_1(t_*).
$$

Combining the two ranges gives

$$
a+b<\frac{29-7\sqrt{13}}{12}.
$$

By reflection, the same bound holds when the exact local midpoint subset is
$\{M_0,M_5\}$.

## The three-midpoint cap

Assume now

$$
M_5,M_0,M_1\in T_0.
$$

By reflection, take $t\ge1$ as above.  The condition $M_1\in T_0$ still gives

$$
b\ge L(t)=\frac{t-1}{2t}.
$$

The condition

$$
M_5=\left(1,\frac12\right)\in T_0
$$

gives, from the third half-plane,

$$
t+\frac12\le\sqrt D-a-tb,
$$

or

$$
a+tb\le C_5(t):=\sqrt D-t-\frac12.
$$

Therefore

$$
a+b
=
U-(t-1)b
\le
C_5(t)-(t-1)L(t).
$$

Define

$$
S_3(t):=C_5(t)-(t-1)L(t)
=
\sqrt{t^2+t+1}-\frac{3t}{2}+\frac12-\frac1{2t}.
$$

Then

$$
S_3'(t)
=
\frac{2t+1}{2\sqrt D}
-\frac32
+\frac1{2t^2}.
$$

For $t\ge1$,

$$
\frac{2t+1}{\sqrt D}\le2
$$

because

$$
(2t+1)^2\le4(t^2+t+1).
$$

Hence

$$
S_3'(t)
\le
1-\frac32+\frac1{2t^2}
=
-\frac12+\frac1{2t^2}
\le0.
$$

So $S_3$ is nonincreasing on $[1,\infty)$.  Its maximum occurs at $t=1$.
Consequently,

$$
a+b\le S_3(1)=\sqrt3-\frac32.
$$

This proves the three-midpoint cap.

## Boundary cases and degeneracies

In the one-adjacent case, the displayed cap is a strict supremum.  Equality
would force both

$$
t=t_*=\frac{\sqrt{13}-1}{2}
$$

and equality in the $r_5$-intersection inequality, so the $r_5$ intersection
would collapse to a point.  That is not Vd2, because Vd2 requires positive
length on both adjacent rays.

In the three-midpoint case, equality occurs at $t=1$ and is compatible with
positive-length intersections with both adjacent rays.  It is therefore a
closed local cap, not merely a strict supremum.

## Numerical check

For the one-adjacent cap,

$$
t_*=\frac{\sqrt{13}-1}{2},\qquad D(t_*)=4.
$$

The boundary values are

$$
b_*=\frac{t_*-1}{2t_*},
$$

and

$$
a_*=
\sqrt{D(t_*)}-1-\frac{t_*}{2}-t_*b_*.
$$

They satisfy

$$
a_*+b_*=\frac{29-7\sqrt{13}}{12}.
$$

Numerically,

$$
a_*+b_*=0.313428422646006\ldots.
$$

The strict Vd2 examples approach this value from below as
$t\to t_*^-$, with positive $r_5$ and $r_1$ intersections.

For the three-midpoint cap, taking $t=1$ and

$$
a=b=\frac12\left(\sqrt3-\frac32\right)
$$

gives

$$
a+b=\sqrt3-\frac32=0.232050807568877\ldots.
$$

A direct substitution into the three half-plane inequalities verifies that
$M_5,M_0,M_1\in T_0$ and that both adjacent-ray intersections have positive
length.
