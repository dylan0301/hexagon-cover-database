# Direct T3-Like Area-Loss Theorem

Status: Proven

## Statement

Let $T$ be a closed unit equilateral $V_0$-triangle of T3-like type:

$$
(o,n)=(2,1).
$$

Let $a,b$ be required lower bounds for its two adjacent boundary reaches, and
write

$$
G(T)=
\frac{\mathrm{area}(T\setminus H)}{\sqrt3/4}.
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

The proof is direct.  It does not use the failed coordinatewise
tangent-envelope conjecture in
[`3172_full_T3_like_tangent_envelope_conjecture.md`](3172_full_T3_like_tangent_envelope_conjecture.md).

## 1. Local coordinates and orientation forms

Use the $V_0$-local coordinates from
[`../../32XX_Nplus_ge2/3205_unconditional_local_square_loss.md`](../../32XX_Nplus_ge2/3205_unconditional_local_square_loss.md):

$$
X=V_0+x(V_1-V_0)+y(V_5-V_0).
$$

Then

$$
V_0=(0,0),
$$

the two adjacent boundary edges are the positive coordinate axes, and

$$
T\cap H=T\cap
\left\{
(x,y):x\ge0,\ y\ge0
\right\}.
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

every orientation is represented by one of the following two types.

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

We first show that a T3-like triangle cannot have Type I orientation.

## 2. Type I cannot be T3-like

For Type I use the affine coordinates

$$
U=\alpha+y-tx,
\qquad
V=\beta+x-(1-t)y,
$$

so that

$$
T=
\left\{
U\ge0,\quad
V\ge0,\quad
U+V\le z
\right\}.
$$

Since $V_0\in T$,

$$
\alpha\ge0,
\qquad
\beta\ge0,
\qquad
\alpha+\beta\le z.
$$

Let $Q_0,Q_1,Q_2$ be the triangle vertices corresponding respectively to

$$
(U,V)=(0,0),\qquad (0,z),\qquad (z,0).
$$

The inverse formulas give

$$
Q_0=
\left(
-\frac{(1-t)\alpha+\beta}{D},
-\frac{\alpha+t\beta}{D}
\right),
$$

$$
Q_1=
\left(
\frac{z-(1-t)\alpha-\beta}{D},
\frac{tz-\alpha-t\beta}{D}
\right),
$$

and

$$
Q_2=
\left(
\frac{(1-t)z-(1-t)\alpha-\beta}{D},
\frac{z-\alpha-t\beta}{D}
\right).
$$

The first coordinate of $Q_1$ is nonnegative because

$$
z-(1-t)\alpha-\beta
=
(z-\alpha-\beta)+t\alpha\ge0.
$$

The second coordinate of $Q_2$ is nonnegative because

$$
z-\alpha-t\beta
=
(z-\alpha-\beta)+(1-t)\beta\ge0.
$$

Except for the degenerate case $\alpha=\beta=0$, the vertex $Q_0$ lies outside
the local wedge and hence outside $H$.  In the degenerate case
$\alpha=\beta=0$, all three vertices lie in the wedge, so the triangle is not
T3-like.

Suppose now that exactly two vertices lie outside $H$.  Then exactly one of
$Q_1,Q_2$ lies outside the wedge.

If $Q_1$ is outside, then its second coordinate is negative:

$$
\alpha+t\beta>tz.
$$

The sole wedge vertex is $Q_2$, and

$$
(Q_2)_x
\le
\frac{(1-t)z}{D}
=
\frac{1-t}{z}
\le1,
$$

while

$$
(Q_2)_y
=
\frac{z-\alpha-t\beta}{D}
<
\frac{(1-t)z}{D}
=
\frac{1-t}{z}
\le1.
$$

If $Q_2$ is outside, then

$$
(1-t)\alpha+\beta>(1-t)z.
$$

The sole wedge vertex is $Q_1$, and

$$
(Q_1)_x
<
\frac{tz}{D}
=
\frac t z
\le1,
$$

while

$$
(Q_1)_y
\le
\frac{tz}{D}
=
\frac t z
\le1.
$$

Every other vertex of the clipped polygon $T\cap H$ lies on one of the two
positive coordinate axes.  Such an axis point has coordinate at most $1$,
because its Euclidean distance from $V_0$ equals that coordinate and a unit
equilateral triangle has diameter $1$.

Thus, whenever a Type I triangle has exactly two vertices outside $H$, every
point of $T\cap H$ satisfies

$$
x\le1,
\qquad
y\le1.
$$

It has no positive-length intersection with either adjacent ray.  Hence it has
$n=0$, not $n=1$.

Therefore:

$$
\boxed{\text{Every T3-like triangle has Type II orientation.}}
$$

## 3. Exact Type II geometry

For Type II use

$$
U=\alpha+(1-t)x+ty,
\qquad
V=\beta+tx-y,
$$

so that

$$
T=
\left\{
U\ge0,\quad
V\ge0,\quad
U+V\le z
\right\}.
$$

Let $A$ and $B$ be the exact reaches of $T$ on the positive $y$ and $x$ axes.
As in the square-loss proof,

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

Since the required boundary coordinates satisfy $a\le A$ and $b\le B$, this
immediately proves

$$
a+b\le A+B\le1.
$$

Thus every T3-like row is nonsupercritical.

The unique triangle vertex in the wedge is

$$
Q=
\left(
\frac{B+(1-t)A}{D},
\frac{A+tB}{D}
\right).
$$

The clipped polygon is

$$
T\cap H
=
\mathrm{conv}
\left\{
(0,0),\quad
(B,0),\quad
Q,\quad
(0,A)
\right\}.
$$

The axis reaches satisfy $A,B\le1$.  Therefore positive-length intersection
with the adjacent ray $x=1$ occurs exactly when $Q_x>1$, and positive-length
intersection with the adjacent ray $y=1$ occurs exactly when $Q_y>1$.

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

In particular $0<t<1$.  Since $S\le z$,

$$
A<
\frac{z-D}{t}.
$$

Define

$$
L=\frac{z-D}{t}
=
\frac{z(1-z)}t.
$$

## 4. Reduction to the tangent boundary

The normalized inside area is

$$
I(S,A)=
\frac{(1-t)A^2+t(S-A)^2+2A(S-A)}D.
$$

Therefore

$$
G(S,A)=1-I(S,A).
$$

For fixed $t$ and $A$,

$$
\frac{\partial I}{\partial S}
=
\frac{2\left(tS+(1-t)A\right)}D>0.
$$

Hence $G(S,A)$ decreases as $S$ increases.  Since $S\le z$,

$$
G(S,A)\ge G(z,A).
$$

At $S=z$,

$$
G(z,A)
=
\frac{tA^2+(1-t)(z-A)^2}{D}.
$$

Its derivative with respect to $A$ is

$$
\frac{\partial G(z,A)}{\partial A}
=
\frac{2\left(A-(1-t)z\right)}D.
$$

Moreover,

$$
(1-t)z-L
=
\frac{z(z-D)}t>0.
$$

Since the ray-hit inequality gives $A<L$, the function $G(z,A)$ is decreasing
throughout the relevant range.  Therefore

$$
G(T)=G(S,A)>G(z,L).
$$

The strict inequality is not needed below; we retain the weaker bound

$$
\boxed{G(T)\ge G(z,L).}
$$

Now set

$$
s=\frac{1-z}{t}.
$$

Because $0<t<1$ and $z=\sqrt{1-t+t^2}$,

$$
0<s<\frac12.
$$

Indeed, $s>0$ follows from $z<1$, and $s<1/2$ is equivalent to

$$
z>1-\frac t2,
$$

whose square is the strict inequality

$$
1-t+t^2>
1-t+\frac{t^2}{4}.
$$

The identities

$$
z=1-ts
$$

and

$$
z^2=1-t+t^2
$$

give

$$
t=\frac{1-2s}{1-s^2},
\qquad
z=\frac{s^2-s+1}{1-s^2}.
$$

Consequently,

$$
L=zs
=
\frac{s(s^2-s+1)}{1-s^2}
=:A(s),
$$

and

$$
z-L
=
\frac{s^2-s+1}{1+s}
=:B(s).
$$

At the boundary value $A=L$, the wedge vertex is

$$
Q=(1,1-s).
$$

Therefore the normalized inside area of the boundary quadrilateral is

$$
F(s)=A(s)+B(s)-B(s)s
=
\frac{(s^2-s+1)^2}{1-s^2}.
$$

Thus

$$
G(z,L)=1-F(s).
$$

The actual reach satisfies

$$
A\ge a\ge m
$$

and $A<L=A(s)$, so

$$
A(s)>m.
$$

It remains only to bound the loss of this one-dimensional boundary family.

## 5. Boundary-family loss estimate

Write

$$
G(s)=1-F(s).
$$

A direct simplification gives

$$
G(s)-\left(2A(s)-4A(s)^2\right)
=
\frac{s^2
\left(
5s^4-8s^3+13s^2-8s+2
\right)}
{(1-s^2)^2}.
$$

For $0\le s\le1/2$,

$$
-8s^3\ge-4s^2,
$$

so

$$
5s^4-8s^3+13s^2-8s+2
\ge
9s^2-8s+2.
$$

The last quadratic has minimum $2/9$ at $s=4/9$.  Hence

$$
\boxed{G(s)\ge2A(s)-4A(s)^2.}
$$

We also need a uniform bound when $A(s)$ passes $1/4$.  First,

$$
A(s)\le s
$$

on $[0,1/2]$, because this is equivalent to $2s^2-s\le0$.  Thus
$A(s)\ge1/4$ implies $s\ge1/4$.  On $[1/4,1/2]$,

$$
G(s)-\frac14
=
\frac{(1-2s)
\left(
2s^3-3s^2+6s-1
\right)}
{4(1-s^2)}.
$$

The cubic factor is strictly increasing because

$$
\frac{\mathrm d}{\mathrm ds}
\left(
2s^3-3s^2+6s-1
\right)
=
6(s^2-s+1)>0,
$$

and at $s=1/4$ it equals $11/32$.  Therefore

$$
\boxed{
A(s)\ge\frac14
\quad\Longrightarrow\quad
G(s)\ge\frac14.
}
$$

Define

$$
\psi(u)=2u-4u^2.
$$

The function $\psi$ is increasing on $[0,1/4]$, and

$$
\psi(u)\le\frac14
$$

for every $u\in[0,1/2]$.

If $A(s)\le1/4$, then $m<A(s)\le1/4$, so

$$
G(s)\ge\psi(A(s))\ge\psi(m).
$$

If $A(s)\ge1/4$, then

$$
G(s)\ge\frac14\ge\psi(m).
$$

In both cases,

$$
G(s)\ge2m-4m^2.
$$

Combining this with the reduction in Section 4 gives

$$
\boxed{G(T)\ge2m-4m^2.}
$$

This proves the theorem.

## 6. Boundary cases

For $m=0$, the loss inequality is the trivial statement $G(T)\ge0$.  The proof
above handles $m>0$, which is the case used in the CE0 one-supercritical
assembly.

The equality boundary $Q_x=1$ is not itself T3-like, because the adjacent-ray
intersection has zero length there.  It is used only as a limiting lower bound:
every genuine T3-like triangle has $Q_x>1$ and hence strictly larger loss than
the corresponding boundary value.
