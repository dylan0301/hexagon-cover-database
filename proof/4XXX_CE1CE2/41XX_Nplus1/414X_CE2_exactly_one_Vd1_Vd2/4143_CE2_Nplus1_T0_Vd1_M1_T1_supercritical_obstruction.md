# CE2, $N_+=1$, $T_0$ Vd1 With $M_1\in T_0$ And $T_1$ Supercritical

Status: Proven

This file proves the normalized adjacent-rescue Vd1 subcase in the
[`4140`](4140_CE2_Nplus1_exactly_one_Vd1_Vd2_TODO.md) branch.

The local type conventions are those of
[`../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md),
the local $(a,b,c)$ coordinates are those of
[`../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md`](../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md),
and the free strict supercritical envelope is the one recorded in
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

Then these seven role triangles cannot cover the hexagon perimeter.

By reflection, the same conclusion holds for the branch

$$
T_0\text{ Vd1},\qquad M_5\in T_0,\qquad T_5\text{ supercritical}.
$$

## Normalized $V_0$ coordinates

Use local coordinates

$$
X=V_0+x(V_5-V_0)+y(V_1-V_0).
$$

Then

$$
V_0=(0,0),\qquad V_5=(1,0),\qquad V_1=(0,1),
$$

$$
O=(1,1),
$$

and

$$
M_1=\left(\frac12,1\right).
$$

The metric is

$$
\|(x,y)\|^2=x^2+y^2-xy.
$$

The relevant boundary edge and adjacent rays are

$$
e_{5,0}=\{(x,0):0\le x\le1\},
$$

$$
r_1=\{(x,1):0\le x\le1\},
\qquad
r_5=\{(1,y):0\le y\le1\}.
$$

In the branch under consideration, $T_0$ has positive-length intersection with
$r_1$ and no positive-length intersection with $r_5$.

## Local Vd1 normal form

Let $a,b$ be the actual adjacent boundary reaches of $T_0$. First suppose
$a=b=0$. The CE2 interval on $e_{0,1}$ starts at a strictly positive
coordinate. Since $T_0$ supplies no initial boundary interval, $T_1$ must
cover the whole edge from $V_1$, so its incoming reach satisfies $a_1\ge1$.
The diameter bound

$$
a_1^2+a_1b_1+b_1^2\le1
$$

then forces $a_1=1$ and $b_1=0$, contradicting the strict supercritical
condition $a_1+b_1>1$. Thus the exceptional vertex-degenerate branch from
`4145` is impossible here.

Assume $a+b>0$. The dichotomy proved in
[`4145_Vd1_Vd2_corner_side_normal_form.md`](4145_Vd1_Vd2_corner_side_normal_form.md)
puts $T_0$ in the corner-side normal form. Let $W$ be its unique outside
vertex. The two sides incident to $W$ determine nonnegative intercepts
$\alpha,\beta$ on the adjacent edge-lines. The actual boundary coverage on
$e_{5,0}$ is denoted by $a$ and satisfies

$$
a\le\alpha.
$$

The corresponding coverage on $e_{0,1}$ is not used below.

The standard corner-side reduction is as follows.  The two unit side directions
issuing from $W$ have positive local coordinates and meet at angle $60^\circ$.
After reflecting the local picture if needed, they may be represented by

$$
(t+1,1),\qquad (t,t+1)
$$

for some $t>0$.  Their difference is $(1,-t)$, and all three vectors have
squared metric length

$$
D=t^2+t+1.
$$

Set

$$
d=\sqrt D.
$$

The triangle is therefore represented by

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

On $r_1$, points have the form $(x,1)$.  The first inequality is automatic on
$0\le x\le1$, because

$$
x-(t+1)\le -t\le\alpha.
$$

The second side gives the lower bound

$$
x\ge\frac{t(1-\beta)}{t+1},
$$

and the third side gives the upper bound

$$
x\le\frac{d-\alpha-t\beta-1}{t}.
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

On $r_5$, points have the form $(1,y)$.  The second side is nonbinding on the
unit segment because it gives only

$$
y\le1+\frac1t+\beta>1.
$$

The first and third sides give

$$
y\ge\frac{1-\alpha}{t+1}
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

Since this is the Vd1 $r_1$-branch, $T_0\cap r_5$ has no positive length.

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
interval implies $U_5\le0$.  Since $U_5\ge1-t/2$, we get $t\ge2$.  Thus in all
cases

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

Since $a\le\alpha$, it is enough to prove $\alpha\le A(c)$.

From

$$
\alpha+t\beta\le d-1-\frac t2
$$

and

$$
t\beta\ge t-c(t+1),
$$

we get

$$
\alpha\le d-1-\frac{3t}{2}+c(t+1).
$$

Set

$$
F(t,c):=\sqrt{t^2+t+1}-1-\frac{3t}{2}+c(t+1).
$$

Then

$$
\alpha\le F(t,c).
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

Since $\alpha\ge0$ and $\alpha\le F(t,c)\le L(c)$, every feasible row has
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
\alpha\le L(c)\le A(c).
$$

Since $a\le\alpha$,

$$
\boxed{a\le A(c).}
$$

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

is increasing for $z\ge0$.  Since $a\le\alpha\le F(t,c)$ and
$\delta\ge\delta_0+\alpha/t$, we get

$$
\frac{a}{a+\delta}\le\frac{\alpha}{\alpha+\delta}\le
\frac{\alpha}{\alpha+\delta_0+\alpha/t}\le
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
envelope is undefined at radial coordinate $1/2$.

Point-only contacts on $r_5$ do not affect the Vd1 type, because Vd1 excludes
positive-length $r_5$ intersection only.  The $t\ge1$ proof above treats both
$\alpha\le1$ and $\alpha>1$, so it does not require the outside-vertex side to
cut the actual unit segment $e_{5,0}$ before the vertex $V_5$.

## Numerical check

The numerical check sampled the normal-form variables $t,\alpha,\beta$ subject
to

$$
t\ge1,
\qquad
\alpha,\beta\ge0,
$$

$$
c\le\frac12\le u,
$$

positive-length $r_1$ intersection, and no positive-length $r_5$ intersection.
For each retained sample it checked

$$
a\le A(c)
$$

and

$$
\frac{a}{a+1-u}\le A(c),
$$

with $a$ taken as the actual initial boundary coverage on $e_{5,0}$, hence
$a\le\alpha$.

A second sampler used the CE2 slack variables $\lambda,X,Y$ from the side model
and retained only hiding samples satisfying

$$
S\le a<T,
\qquad
Y\ge\lambda(1-u).
$$

It then checked

$$
T\le A(c).
$$

No counterexample was found.  These numerical checks are not used in the proof;
they are recorded only as independent consistency tests of the formulas above.
