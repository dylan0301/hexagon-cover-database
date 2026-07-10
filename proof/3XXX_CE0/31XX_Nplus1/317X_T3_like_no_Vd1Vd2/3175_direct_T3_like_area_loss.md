# Direct T3-Like Area-Loss Theorem

Status: Proven

## Statement

Let $T$ be a closed unit equilateral $V_0$-triangle of T3-like type:

$$
(o,n)=(2,1).
$$

Let $a,b$ be required lower bounds for its adjacent boundary reaches, and write

$$
G(T)=\frac{\mathrm{area}(T\setminus H)}{\sqrt3/4}.
$$

Then:

1. every T3-like row is nonsupercritical:
   $$
   \boxed{a+b\le1;}
   $$
2. for every $0\le m\le1/2$, if
   $$
   a\ge m,
   \qquad
   b\ge m,
   $$
   then
   $$
   \boxed{G(T)\ge2m-4m^2.}
   $$

The proof is direct. It does not use the failed coordinatewise tangent-envelope
conjecture in
[`3172_full_T3_like_tangent_envelope_conjecture.md`](3172_full_T3_like_tangent_envelope_conjecture.md).

## 1. Local coordinates and orientation forms

Use the $V_0$-local coordinates from
[`../../32XX_Nplus_ge2/3205_unconditional_local_square_loss.md`](../../32XX_Nplus_ge2/3205_unconditional_local_square_loss.md):

$$
X=V_0+x(V_1-V_0)+y(V_5-V_0).
$$

Then $V_0=(0,0)$, the adjacent boundary edges are the positive coordinate
axes, and

$$
T\cap H=T\cap W,
\qquad
W=\left\{(x,y):x\ge0,\ y\ge0\right\}.
$$

Physical rotation by $60^\circ$ is

$$
R(x,y)=(x-y,x).
$$

For

$$
0\le t\le1,
\qquad
D=1-t+t^2,
\qquad
z=\sqrt D,
$$

every orientation is represented by one of the following two forms.

### Type I

$$
d=\frac1z(1,t),
\qquad
Rd=\frac1z(1-t,1).
$$

### Type II

$$
d=\frac1z\left(t,-(1-t)\right),
\qquad
Rd=\frac1z(1,t).
$$

Indeed, among the six oriented side directions of an equilateral triangle,
one lies in the physical angular sector from $60^\circ$ through $180^\circ$.
Type II covers the sub-sector from $60^\circ$ through $120^\circ$, and Type I
covers the sub-sector from $120^\circ$ through $180^\circ$.

## 2. Type I cannot be T3-like

For Type I define

$$
U=\alpha+y-tx,
\qquad
V=\beta+x-(1-t)y.
$$

Then

$$
T=\left\{U\ge0,\ V\ge0,\ U+V\le z\right\}.
$$

Since $V_0\in T$,

$$
\alpha\ge0,
\qquad
\beta\ge0,
\qquad
\alpha+\beta\le z.
$$

Let $Q_0,Q_1,Q_2$ be the vertices corresponding respectively to

$$
(U,V)=(0,0),
\qquad
(0,z),
\qquad
(z,0).
$$

The inverse transformation gives

$$
Q_0=\left(-\frac{(1-t)\alpha+\beta}{D},-\frac{\alpha+t\beta}{D}\right),
$$

$$
Q_1=\left(\frac{z-(1-t)\alpha-\beta}{D},\frac{tz-\alpha-t\beta}{D}\right),
$$

and

$$
Q_2=\left(\frac{(1-t)z-(1-t)\alpha-\beta}{D},\frac{z-\alpha-t\beta}{D}\right).
$$

The first coordinate of $Q_1$ is nonnegative because

$$
z-(1-t)\alpha-\beta=(z-\alpha-\beta)+t\alpha\ge0,
$$

and the second coordinate of $Q_2$ is nonnegative because

$$
z-\alpha-t\beta=(z-\alpha-\beta)+(1-t)\beta\ge0.
$$

If $\alpha=\beta=0$, all three vertices lie in $W$, so the triangle is not
T3-like. Otherwise $Q_0\notin W$. If exactly two vertices lie outside $H$,
then exactly one of $Q_1,Q_2$ lies outside $W$.

### Case 2.1: $Q_1\notin W$

The first coordinate of $Q_1$ is nonnegative, so its second coordinate is
negative:

$$
\alpha+t\beta>tz.
$$

The sole vertex of $T$ in $W$ is $Q_2$. We have

$$
(Q_2)_y<\frac{(1-t)z}{D}=\frac{1-t}{z}\le1.
$$

Also

$$
(Q_2)_x\le\frac{1-t}{z}.
$$

If $t>0$, then

$$
D-(1-t)^2=t>0,
$$

so $(1-t)/z<1$. If $t=0$, the inequality
$\alpha+t\beta>tz$ gives $\alpha>0$, and therefore

$$
(Q_2)_x=1-\alpha-\beta<1.
$$

Thus in all cases

$$
(Q_2)_x<1,
\qquad
(Q_2)_y<1.
$$

### Case 2.2: $Q_2\notin W$

The second coordinate of $Q_2$ is nonnegative, so its first coordinate is
negative:

$$
(1-t)\alpha+\beta>(1-t)z.
$$

The sole vertex of $T$ in $W$ is $Q_1$. We have

$$
(Q_1)_x<\frac{tz}{D}=\frac t z\le1,
$$

and

$$
(Q_1)_y\le\frac t z.
$$

If $t<1$, then

$$
D-t^2=1-t>0,
$$

so $t/z<1$. If $t=1$, the outside condition gives $\beta>0$, and hence

$$
(Q_1)_y=1-\alpha-\beta<1.
$$

Thus again

$$
(Q_1)_x<1,
\qquad
(Q_1)_y<1.
$$

In either case, $T\cap W$ is the convex hull of the sole wedge vertex and
points on the two positive coordinate axes. Every axis-intersection point has
coordinate at most $1$, because its Euclidean distance from $V_0$ equals that
coordinate and the triangle has diameter $1$. The sole non-axis wedge vertex
has both coordinates strictly below $1$. Therefore each of the lines $x=1$
and $y=1$ meets $T\cap W$ in at most one point. Neither adjacent ray has
positive-length intersection with $T$.

Hence every Type I triangle with $o=2$ has $n=0$. In particular,

$$
\boxed{\text{a T3-like triangle cannot have Type I orientation.}}
$$

## 3. Exact Type II geometry

For Type II define

$$
U=\alpha+(1-t)x+ty,
\qquad
V=\beta+tx-y.
$$

Then

$$
T=\left\{U\ge0,\ V\ge0,\ U+V\le z\right\}.
$$

Since $V_0\in T$,

$$
\alpha\ge0,
\qquad
\beta\ge0,
\qquad
\alpha+\beta\le z.
$$

Let $A$ and $B$ be the exact reaches of $T$ on the positive $y$ and $x$ axes.
On the $y$ axis the limiting inequality is $V=\beta-y\ge0$, while on the
$x$ axis the limiting inequality is $U+V=\alpha+\beta+x\le z$. Hence

$$
A=\beta,
\qquad
B=z-\alpha-\beta.
$$

Set

$$
S=A+B=z-\alpha.
$$

Then

$$
\boxed{A+B=S\le z\le1.}
$$

Since $a\le A$ and $b\le B$,

$$
\boxed{a+b\le A+B\le1.}
$$

This proves T3-like nonsupercriticality.

The triangle vertex in $W$ is

$$
Q=\left(\frac{B+(1-t)A}{D},\frac{A+tB}{D}\right).
$$

Because $o=2$, the other two triangle vertices lie outside $W$. Therefore

$$
T\cap H=T\cap W=\mathrm{conv}\left\{(0,0),(B,0),Q,(0,A)\right\}.
$$

The endpoint orientations cannot be T3-like. For $t=0$, the three triangle
vertices are

$$
(-\alpha,A),
\qquad
(-\alpha,A-1),
\qquad
(1-\alpha,A).
$$

If $o=2$, then $\alpha>0$, and the unique wedge vertex has $x<1$ and $y\le1$;
there is no adjacent-ray interval. If $\alpha=0$, at most one vertex is outside
$H$. Thus $t=0$ is not T3-like. The case $t=1$ is its reflection. Consequently,

$$
0<t<1.
$$

For $0<t<1$, none of the three triangle sides is parallel to either coordinate
ray. Since $A,B\le1$, positive-length intersection with $x=1$ occurs exactly
when $Q_x>1$, and positive-length intersection with $y=1$ occurs exactly when
$Q_y>1$.

Because $n=1$, reflection across the $V_0$ symmetry axis allows us to assume

$$
Q_x>1,
\qquad
Q_y\le1.
$$

The first inequality is

$$
S-tA>D.
$$

Since $S\le z$,

$$
A<\frac{z-D}{t}.
$$

Define

$$
L=\frac{z-D}{t}=\frac{z(1-z)}t.
$$

## 4. Reduction to a one-dimensional boundary family

The normalized inside area is

$$
I(S,A)=\frac{(1-t)A^2+t(S-A)^2+2A(S-A)}D,
$$

so

$$
G(S,A)=1-I(S,A).
$$

For fixed $t$ and $A$,

$$
\frac{\partial I}{\partial S}=\frac{2\left(tS+(1-t)A\right)}D>0.
$$

Thus $G(S,A)$ decreases as $S$ increases. Since $S\le z$,

$$
G(S,A)\ge G(z,A).
$$

At $S=z$,

$$
G(z,A)=\frac{tA^2+(1-t)(z-A)^2}{D},
$$

and

$$
\frac{\partial G(z,A)}{\partial A}=\frac{2\left(A-(1-t)z\right)}D.
$$

Moreover,

$$
(1-t)z-L=\frac{z(z-D)}t>0.
$$

Since $A<L$, the function $G(z,A)$ is decreasing throughout the relevant
interval. Therefore

$$
G(T)=G(S,A)>G(z,L).
$$

For the non-strict estimate used below,

$$
\boxed{G(T)\ge G(z,L).}
$$

Set

$$
s=\frac{1-z}{t}.
$$

Because $0<t<1$,

$$
0<s<\frac12.
$$

Indeed, $s>0$ follows from $z<1$, and $s<1/2$ is equivalent to

$$
z>1-\frac t2,
$$

whose square is

$$
1-t+t^2>1-t+\frac{t^2}{4}.
$$

The identities $z=1-ts$ and $z^2=1-t+t^2$ give

$$
t=\frac{1-2s}{1-s^2},
\qquad
z=\frac{s^2-s+1}{1-s^2}.
$$

Consequently,

$$
L=zs=\frac{s(s^2-s+1)}{1-s^2}=:A(s),
$$

and

$$
z-L=\frac{s^2-s+1}{1+s}=:B(s).
$$

At $S=z$ and $A=L$, the wedge vertex is

$$
Q=(1,1-s).
$$

The normalized inside area of this limiting quadrilateral is

$$
F(s)=A(s)+B(s)-sB(s)=\frac{(s^2-s+1)^2}{1-s^2}.
$$

Write

$$
G(s)=1-F(s).
$$

The actual reach satisfies

$$
A\ge a\ge m
$$

and $A<L=A(s)$, so

$$
A(s)>m.
$$

## 5. Loss estimate on the boundary family

A direct simplification gives

$$
G(s)-\left(2A(s)-4A(s)^2\right)=\frac{s^2\left(5s^4-8s^3+13s^2-8s+2\right)}{(1-s^2)^2}.
$$

For $0\le s\le1/2$,

$$
-8s^3\ge-4s^2,
$$

and therefore

$$
5s^4-8s^3+13s^2-8s+2\ge9s^2-8s+2.
$$

The last quadratic has minimum $2/9$ at $s=4/9$. Hence

$$
\boxed{G(s)\ge2A(s)-4A(s)^2.}
$$

We also need a uniform estimate after $A(s)$ passes $1/4$. On $[0,1/2]$,

$$
A(s)\le s,
$$

because this is equivalent to $2s^2-s\le0$. Thus $A(s)\ge1/4$ implies
$s\ge1/4$. For $1/4\le s\le1/2$,

$$
G(s)-\frac14=\frac{(1-2s)\left(2s^3-3s^2+6s-1\right)}{4(1-s^2)}.
$$

The cubic factor is strictly increasing because

$$
\frac{\mathrm d}{\mathrm ds}\left(2s^3-3s^2+6s-1\right)=6(s^2-s+1)>0,
$$

and at $s=1/4$ it equals $11/32$. Therefore

$$
\boxed{A(s)\ge\frac14\quad\Longrightarrow\quad G(s)\ge\frac14.}
$$

Define

$$
\psi(u)=2u-4u^2.
$$

The function $\psi$ is increasing on $[0,1/4]$, and $\psi(u)\le1/4$ for every
$u\in[0,1/2]$.

If $A(s)\le1/4$, then $m<A(s)\le1/4$, so

$$
G(s)\ge\psi(A(s))\ge\psi(m).
$$

If $A(s)\ge1/4$, then

$$
G(s)\ge\frac14\ge\psi(m).
$$

Thus in both cases

$$
G(s)\ge2m-4m^2.
$$

Combining this with the reduction in Section 4 yields

$$
\boxed{G(T)\ge2m-4m^2.}
$$

This proves the theorem.

## 6. Boundary cases

For $m=0$, the loss inequality is the trivial statement $G(T)\ge0$. The proof
above applies directly for $m>0$, which is the case used in the CE0
one-supercritical assembly.

The boundary value $Q_x=1$ is not itself T3-like: because $0<t<1$, no side is
parallel to the ray, so the intersection with $x=1$ has zero length. It is used
only as a limiting lower-loss comparison. Every genuine T3-like triangle has
$Q_x>1$ and strictly larger loss than the corresponding limiting value.
