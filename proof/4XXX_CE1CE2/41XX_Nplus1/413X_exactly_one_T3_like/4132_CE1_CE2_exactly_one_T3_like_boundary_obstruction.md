# CE1/CE2, $N_+=1$, Exactly One T3-Like: Boundary Obstruction

Status: Proven

This file proves the shared CE1/CE2 boundary obstruction after the midpoint
reduction in
[`4131_midpoint_forcing_reduction.md`](4131_midpoint_forcing_reduction.md).

No numerical or sampling input is used.

## 1. Statement

Work after the reduction in `4131`. Thus, after reflection if necessary,

$$
T_0\text{ is T3-like},\qquad M_1\in T_0,
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

Then the seven role triangles cannot cover the hexagon perimeter. In
particular, the CE1/CE2, $N_+=1$, exactly-one-T3-like branch is impossible.

The proof uses only the free supercritical outgoing-edge envelope from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md).
The sharper fixed-incoming map from `2007` is not needed.

## 2. Local coordinates for the T3-like row

Use the normalized $V_0$ coordinates

$$
X=V_0+x(V_5-V_0)+y(V_1-V_0).
$$

Thus $V_0=(0,0)$, $V_5=(1,0)$, $V_1=(0,1)$, and $O=(1,1)$.
The metric is

$$
\|(x,y)\|^2=x^2+y^2-xy.
$$

The edges adjacent to $V_0$ are

$$
e_{5,0}=\{(x,0):0\le x\le1\},
\qquad
e_{0,1}=\{(0,y):0\le y\le1\},
$$

and the adjacent radial arm $r_1=[V_1,O]$ is

$$
r_1=\{(\eta,1):0\le\eta\le1\},
$$

where $\eta$ is distance from $V_1$ toward $O$.

By the T3-like normalization convention, assume that $V_0$ lies on a side of
$T_0$. Let that side have unit direction

$$
w=(r,s),
\qquad
r^2+s^2-rs=1.
$$

In the branch $M_1\in T_0$ and $T_0$ has positive-length intersection with
$r_1$ but not with $r_5$, take

$$
r<0<s.
$$

Set

$$
R=-r,\qquad D=s-r=s+R.
$$

Then

$$
R^2-DR+D^2=1.
$$

The branch containing $M_1$ is the root

$$
R=\frac{D+E}{2},\qquad E=\sqrt{4-3D^2}.
$$

Let $0\le\tau\le1$ be the position of $V_0$ on the chosen side. The triangle
has vertices

$$
-\tau w,\qquad (1-\tau)w,\qquad -\tau w+z,
$$

where

$$
z=(s,s-r).
$$

A point $(x,y)$ lies in $T_0$ if and only if

$$
sx-ry\ge0,
$$

$$
\tau+sy-(s-r)x\ge0,
$$

and

$$
\tau+rx+(s-r)y\le1.
$$

Let

$$
a=\frac{\tau}{D}.
$$

Then

$$
T_0\cap e_{5,0}=[0,a].
$$

On $r_1$, the intersection is

$$
T_0\cap r_1=[c,u],
$$

with the coordinate measured from $V_1$ toward $O$, where

$$
c=\frac{D(1+a)-1}{R},
\qquad
u=1-\frac RD+a.
$$

Since $M_1$ has $r_1$-coordinate $1/2$ and $M_1\in T_0$,

$$
c\le\frac12\le u.
$$

Equivalently,

$$
\frac{E}{2D}\le a\le\frac{4-3D+E}{4D}.
$$

Similarly,

$$
T_0\cap e_{0,1}=\left[0,\frac{1-\tau}{D}\right].
$$

Therefore the boundary coordinates of $T_0$ on $e_{5,0}$ and $e_{0,1}$ sum to

$$
a+\frac{1-\tau}{D}=\frac1D.
$$

Since T3-like rows are nonsupercritical, this gives

$$
D\ge1.
$$

The equation $E=\sqrt{4-3D^2}$ gives

$$
D\le\frac2{\sqrt3}.
$$

Thus

$$
1\le D\le\frac2{\sqrt3}.
$$

Finally, the own-radial exit coordinate of $T_0$ on $r_0=[V_0,O]$, measured
from $V_0$ toward $O$, is

$$
x_0:=\frac{aD}{R}.
$$

## 3. The T3-like radial-edge inequality

For $0\le c\le1/2$, define

$$
B(c):=\frac{c+\sqrt{c^2-8c+4}}2.
$$

This is the closed free supercritical outgoing-edge envelope from `2010`.
Set

$$
A(c):=1-B(c).
$$

Then

$$
c=\frac{A(c)(2-A(c))}{1+A(c)}.
$$

Indeed, the root equation from `2010` is

$$
B(c)^2-cB(c)+2c-1=0.
$$

Substituting $B(c)=1-A(c)$ gives

$$
A(c)^2+(c-2)A(c)+c=0,
$$

or equivalently

$$
c=\frac{A(c)(2-A(c))}{1+A(c)}.
$$

Let

$$
\Phi(X)=\frac{X(2-X)}{1+X}.
$$

On $0\le X\le1/2$,

$$
\Phi'(X)=\frac{2-2X-X^2}{(1+X)^2}\ge0.
$$

We prove

$$
\boxed{x_0\le A(c).}
$$

First,

$$
x_0=\frac{aD}{R}\le\frac12.
$$

Indeed, using the upper bound on $a$,

$$
x_0\le \frac{4-3D+E}{4R}.
$$

Since $2R=D+E$, the inequality

$$
\frac{4-3D+E}{4R}\le\frac12
$$

is equivalent to $D\ge1$.

It remains to prove

$$
\Phi(x_0)\le c.
$$

A direct substitution using

$$
R=\frac{D+E}{2}
$$

gives

$$
c-\Phi(x_0)
=
\frac{2N(D,a)}{(D+E)(2Da+D+E)},
$$

where

$$
N(D,a)=4D^2a^2+D^2a+D^2-DEa+DE-2Da-D-E.
$$

The denominator is positive. We prove $N(D,a)\ge0$.

For fixed $D$, $N(D,a)$ is a convex quadratic in $a$, with critical point

$$
a_0=\frac{2+E-D}{8D}.
$$

The lower endpoint of the allowed $a$-interval is

$$
a_L=\frac{E}{2D}.
$$

The relation $a_0\le a_L$ is equivalent to

$$
D\le\frac87.
$$

### Case 1: $1\le D\le 8/7$

In this range $N(D,a)$ is increasing for $a\ge a_L$. Hence

$$
N(D,a)\ge N(D,a_L).
$$

Substitution gives

$$
2N(D,a_L)=4-D^2-2D-(4-3D)E.
$$

Both $4-D^2-2D$ and $(4-3D)E$ are nonnegative on $1\le D\le8/7$.
Moreover,

$$
(4-D^2-2D)^2-(4-3D)^2E^2
=
4(D-1)(7D^3-10D^2-8D+12).
$$

The cubic

$$
p(D)=7D^3-10D^2-8D+12
$$

is decreasing on $[1,8/7]$, because

$$
p'(D)=21D^2-20D-8<0
$$

on this interval. Since

$$
p(8/7)=\frac{12}{49}>0,
$$

we have $p(D)>0$ on the interval. Therefore

$$
4-D^2-2D\ge (4-3D)E,
$$

and hence

$$
N(D,a_L)\ge0.
$$

Thus $N(D,a)\ge0$ in Case 1.

### Case 2: $8/7\le D\le 2/\sqrt3$

In this range the critical point $a_0$ lies in the allowed $a$-interval. The
upper endpoint condition follows from

$$
a_0\le\frac{4-3D+E}{4D},
$$

which is equivalent to

$$
6-5D+E\ge0,
$$

and this holds because $D\le2/\sqrt3<6/5$.

Thus

$$
N(D,a)\ge N(D,a_0).
$$

Substitution gives

$$
16N(D,a_0)
=
15D^2+18DE-12D-E^2-20E-4.
$$

Using $E^2=4-3D^2$, this becomes

$$
16N(D,a_0)
=
2\bigl((9D-10)E+9D^2-6D-4\bigr).
$$

For $D\ge8/7$,

$$
9D-10\ge\frac27>0
$$

and

$$
9D^2-6D-4\ge 9\left(\frac87\right)^2-6\left(\frac87\right)-4
=\frac{44}{49}>0.
$$

Therefore

$$
N(D,a_0)>0,
$$

and Case 2 is proved.

In all cases,

$$
N(D,a)\ge0.
$$

Therefore

$$
\Phi(x_0)\le c.
$$

Since $\Phi$ is increasing on $[0,1/2]$ and $\Phi(A(c))=c$, we conclude

$$
x_0\le A(c).
$$

This proves the T3-like radial-edge inequality.

## 4. The supercritical $T_1$ bound

Let $c_1$ be the own-radial coverage coordinate of $T_1$ on $r_1=[V_1,O]$,
measured from $V_1$ toward $O$. Since $T_0$ enters $r_1$ at coordinate $c$,
the interval of $r_1$ from $V_1$ up to coordinate $c$ is not covered by
$T_0$. The Vd0 rows $T_2,T_3,T_4,T_5$ have no positive-length adjacent-ray
support on $r_1$, and $T_C$ cannot cover a positive interval through $M_1$
because its exact midpoint set excludes $M_1$. Hence coverage of $r_1$ forces

$$
c_1\ge c.
$$

If $c=1/2$, then no strict supercritical row can realize radial coordinate at
least $c$, by the strict form of the `2010` envelope. Thus a putative cover in
this branch must have

$$
0\le c<\frac12.
$$

The strict supercritical envelope in `2010` gives

$$
b_1<B(c_1).
$$

The function $B$ is strictly decreasing on $[0,1/2]$. Indeed,

$$
B'(c)=\frac12\left(1+\frac{c-4}{\sqrt{c^2-8c+4}}\right)<0,
$$

because

$$
(4-c)^2-(c^2-8c+4)=12>0.
$$

Therefore, since $c_1\ge c$,

$$
\boxed{b_1<B(c).}
$$

## 5. The forced $T_5$ reach on $e_{5,0}$

Let

$$
T_C\cap e_{5,0}=[S,T]
$$

when $T_C$ is CE2. In the CE1 case this interval is empty, except possibly
for point contacts, which do not change the positive-length boundary
obligation.

Recall that

$$
T_0\cap e_{5,0}=[0,a].
$$

Let $h$ denote the boundary length on $e_{5,0}$ that $T_5$ is forced to cover,
measured from $V_5$ toward $V_0$. Thus if $T_5$ must reach the point with
$V_0$-based coordinate $y$, then

$$
h=1-y.
$$

We prove

$$
\boxed{h\ge B(c).}
$$

### CE1 case

If $T_C$ is CE1, then it has no positive-length overlap with $e_{5,0}$. The
edge portion beyond $T_0\cap e_{5,0}=[0,a]$ forces $T_5$ to reach coordinate
$a$. Hence

$$
h=1-a.
$$

Since $a\le x_0\le A(c)$,

$$
h=1-a\ge1-A(c)=B(c).
$$

### CE2 case 1: $T\le a$

Here $T_0$ covers both endpoints of the $C$-interval on $e_{5,0}$. The
remaining tail again forces $T_5$ to reach coordinate $a$, so

$$
h=1-a\ge B(c).
$$

### CE2 case 3: $a<S$

Here $T_0$ covers neither endpoint of the $C$-interval. The open gap after
coordinate $a$ forces $T_5$ to reach coordinate $a$, hence

$$
h=1-a\ge B(c).
$$

### CE2 case 2: $S\le a<T$

This is the only case in which $T_5$ need only reach the far endpoint $T$ of
the $C$-interval. We prove

$$
T\le A(c).
$$

Use the CE1/CE2 side model from the exact-$M_0$ center-triangle geometry.
There are parameters

$$
0<\lambda<1,\qquad \rho=\sqrt{1-\lambda+\lambda^2},
$$

and nonnegative center slacks

$$
X:=C_0\ge0,\qquad Y:=C_2\ge0,
$$

such that, for the $e_{5,0}$ interval,

$$
S=\frac{X+Y+1-\rho}{1-\lambda},
\qquad
T=X+\lambda.
$$

Also, if $d_1$ is the length of $T_C\cap r_1$ measured from $O$ toward
$V_1$, then

$$
d_1\le \frac{Y}{\lambda}.
$$

Let

$$
\delta:=\frac RD-a.
$$

This is the first point of $T_0\cap r_1$ measured from $O$ toward $V_1$.
Since all rows other than $T_C,T_0,T_1$ have no positive-length support on
$r_1$, and since the supercritical row $T_1$ cannot cover $M_1$, the
$O$-side gap before $T_0$ must be covered by $T_C$. Hence

$$
d_1\ge\delta.
$$

Therefore

$$
Y\ge\lambda\delta=\lambda\left(\frac RD-a\right).
$$

From $S\le a$,

$$
X\le(1-\lambda)a-Y-1+\rho.
$$

Consequently,

$$
T=X+\lambda
\le
\lambda+(1-\lambda)a-\lambda\left(\frac RD-a\right)-1+\rho.
$$

Thus

$$
T\le a+\rho-1+\lambda\left(1-\frac RD\right).
$$

The same inequalities, together with $X\ge0$, give

$$
0\le a-\lambda\frac RD-1+\rho.
$$

Hence

$$
\lambda\frac RD\le a+\rho-1\le a,
$$

so

$$
\lambda\le\frac{aD}{R}=x_0.
$$

Since $1-R/D=s/D\ge0$ and $\rho\le1$,

$$
T\le a+\lambda\frac{s}{D}
\le
a+x_0\frac{s}{D}.
$$

Using $x_0=aD/R$,

$$
T\le a+\frac{aD}{R}\frac{s}{D}
=
a+\frac{as}{R}
=
\frac{a(R+s)}{R}
=
\frac{aD}{R}
=
x_0.
$$

By the T3-like radial-edge inequality,

$$
x_0\le A(c).
$$

Therefore

$$
T\le A(c).
$$

In this case $T_5$ must reach coordinate $T$, so

$$
h=1-T\ge1-A(c)=B(c).
$$

The proof of $h\ge B(c)$ is complete in all cases.

## 6. Boundary budget contradiction

The edge $e_{1,2}$ is covered from the $V_1$ side by $T_1$ up to coordinate
$b_1$. Hence the row $T_2$ must contribute at least

$$
1-b_1
$$

on that edge, so

$$
a_2\ge1-b_1.
$$

The three full edges $e_{2,3}$, $e_{3,4}$, and $e_{4,5}$ force

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

Finally, the $e_{5,0}$ analysis gives

$$
b_5\ge h.
$$

Adding these five inequalities gives

$$
\sum_{i=2}^5(a_i+b_i)
=
a_2+(b_2+a_3)+(b_3+a_4)+(b_4+a_5)+b_5
\ge
(1-b_1)+1+1+1+h.
$$

Thus

$$
\sum_{i=2}^5(a_i+b_i)\ge4+(h-b_1).
$$

But Sections 4 and 5 prove

$$
h\ge B(c)>b_1.
$$

Therefore

$$
\sum_{i=2}^5(a_i+b_i)>4.
$$

This contradicts the reduction from `4131`, which gives

$$
a_i+b_i\le1,\qquad i=2,3,4,5,
$$

and hence

$$
\sum_{i=2}^5(a_i+b_i)\le4.
$$

The contradiction proves that the CE1/CE2, $N_+=1$, exactly-one-T3-like
branch cannot cover the hexagon perimeter.
