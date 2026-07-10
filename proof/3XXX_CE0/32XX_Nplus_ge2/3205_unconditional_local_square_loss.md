# Unconditional Local Square-Loss Theorem

Status: Proven

## Statement

Normalize at $V_0$.  Let

$$
P_a=e_{5,0}(a),
\qquad
P_b=e_{0,1}(b),
\qquad
0\le a,b\le1.
$$

Let $T$ be any closed unit equilateral triangle containing

$$
V_0,\qquad P_a,\qquad P_b.
$$

Write

$$
G(T)=
\frac{\mathrm{area}(T\setminus H)}{\sqrt3/4}
$$

for its normalized area outside the hexagon.  Then

$$
\boxed{G(T)\ge\min(a,b)^2.}
$$

If

$$
a+b>1,
$$

then the stronger bound holds:

$$
\boxed{G(T)\ge\max(a,b)^2.}
$$

Consequently, for the local area function from
[`3202_area_function_and_monotonicity.md`](3202_area_function_and_monotonicity.md),

$$
\boxed{f(a,b)\le1-\min(a,b)^2}
$$

for all feasible $(a,b)$, and

$$
\boxed{
a+b>1
\quad\Longrightarrow\quad
f(a,b)\le1-\max(a,b)^2.
}
$$

No structural hypothesis about a maximizing triangle is used.

## 1. Local affine coordinates

Put

$$
E_+=V_1-V_0,
\qquad
E_-=V_5-V_0,
$$

and write every point as

$$
X=V_0+xE_++yE_-.
$$

In these coordinates,

$$
V_0=(0,0),
\qquad
P_b=(b,0),
\qquad
P_a=(0,a).
$$

The vectors $E_+$ and $E_-$ have unit length and mutual angle $120^\circ$, so

$$
\lVert xE_++yE_-\rVert^2=x^2+y^2-xy.
$$

The coordinate map has determinant magnitude $\sqrt3/2$.  Therefore coordinate
area $1/2$ is Euclidean area $\sqrt3/4$, the area of a unit equilateral
triangle.  Normalized Euclidean area is consequently twice coordinate area.

In these coordinates the hexagon is

$$
H=
\left\{
(x,y):
0\le x\le2,\quad
0\le y\le2,\quad
\lvert x-y\rvert\le1
\right\}.
$$

Set

$$
W=\left\{(x,y):x\ge0,\ y\ge0\right\}.
$$

### Lemma 1.1: the hexagon reduces to the local wedge

For every unit equilateral triangle $T$ containing $V_0$,

$$
\boxed{T\cap H=T\cap W.}
$$

### Proof

Certainly $H\subset W$.  Conversely, let $(x,y)\in T\cap W$.  Since $T$
contains $(0,0)$ and has diameter $1$,

$$
x^2+y^2-xy\le1.
$$

Because $x,y\ge0$,

$$
(x-y)^2\le x^2+y^2-xy\le1,
$$

so $\lvert x-y\rvert\le1$.  Also,

$$
x^2+y^2-xy
=
\left(y-\frac x2\right)^2+\frac34x^2,
$$

hence $x\le2/\sqrt3<2$.  By symmetry, $y\le2/\sqrt3<2$.  Thus
$(x,y)\in H$.  This proves the lemma.

Therefore $G(T)$ is exactly the normalized area of $T$ outside $W$.

## 2. Exhaustive orientation split

Physical rotation by $60^\circ$ acts in the $(x,y)$ coordinates as

$$
R(x,y)=(x-y,x).
$$

The three counterclockwise directed side vectors of an equilateral triangle
are separated by $120^\circ$.  One of them has physical direction between
$60^\circ$ and $180^\circ$.  Split this sector at $120^\circ$.

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

In either case,

$$
T=Q+\mathrm{conv}\left\{0,d,Rd\right\}
$$

is a unit equilateral triangle.  The two types cover the physical direction
ranges $[120^\circ,180^\circ]$ and $[60^\circ,120^\circ]$, respectively, so
they exhaust all orientations.  Their common endpoint orientations cause no
problem.

## 3. Type I triangles

For Type I define affine side coordinates

$$
U=\alpha+y-tx,
\qquad
V=\beta+x-(1-t)y.
$$

Then

$$
T=
\left\{
U\ge0,\quad
V\ge0,\quad
U+V\le z
\right\}.
$$

The three required point-containment conditions imply

$$
\alpha\ge tb,
\qquad
\beta\ge(1-t)a,
$$

and

$$
\alpha+\beta+(1-t)b\le z,
\qquad
\alpha+\beta+ta\le z.
$$

The inverse transformation is

$$
x=
\frac{(1-t)(U-\alpha)+(V-\beta)}D,
$$

$$
y=
\frac{(U-\alpha)+t(V-\beta)}D.
$$

Thus the wedge inequalities are

$$
(1-t)U+V\ge(1-t)\alpha+\beta,
$$

$$
U+tV\ge\alpha+t\beta.
$$

For fixed $t$, increasing either $\alpha$ or $\beta$ raises both right-hand
sides and shrinks the portion of the fixed $(U,V)$ simplex corresponding to
$T\cap W$.  Hence the outside area is minimized at

$$
\alpha_0=tb,
\qquad
\beta_0=(1-t)a.
$$

At these values, the physical points $P_a,V_0,P_b$ have $(U,V)$ coordinates

$$
P_a=(a+tb,0),
$$

$$
V_0=(tb,(1-t)a),
$$

$$
P_b=(0,b+(1-t)a).
$$

The part outside $W$ is the quadrilateral with vertices

$$
(0,0),\quad
(a+tb,0),\quad
(tb,(1-t)a),\quad
(0,b+(1-t)a)
$$

in the $(U,V)$ plane.  Its $(U,V)$ area is

$$
\frac12
\left(
(1-t)a^2+t b^2+2t(1-t)ab
\right).
$$

The Jacobian magnitude from $(x,y)$ to $(U,V)$ is $D$.  Therefore every
Type I triangle satisfies

$$
\boxed{
G(T)\ge
G_I(a,b;t):=
\frac{(1-t)a^2+t b^2+2t(1-t)ab}{D}.
}
$$

### Lemma 3.1: Type I minimum-square bound

For every $a,b\ge0$,

$$
G_I(a,b;t)\ge\min(a,b)^2.
$$

### Proof

If $a\le b$, then

$$
D\left(G_I-a^2\right)
=
t\left[
b^2-a^2+(1-t)(a^2+2ab)
\right]\ge0.
$$

If $b\le a$, then

$$
D\left(G_I-b^2\right)
=
(1-t)\left[
a^2-b^2+t(2ab+b^2)
\right]\ge0.
$$

This proves the lemma.

### Lemma 3.2: Type I supercritical maximum-square bound

If $a+b>1$, then

$$
G_I(a,b;t)\ge\max(a,b)^2.
$$

### Proof

The feasibility inequalities at $\alpha_0,\beta_0$ give

$$
b+(1-t)a\le z,
\qquad
a+tb\le z.
$$

First assume $a\le b$.  Put

$$
r=\frac ab,
\qquad
t_0=\frac{1-r^2}{1+2r}.
$$

Since $a+b>1$,

$$
b>\frac1{1+r}.
$$

If $0<t<t_0$, then

$$
\left(
\frac{1+r(1-t)}{1+r}
\right)^2-D
=
\frac{t(1+2r)(t_0-t)}{(1+r)^2}>0.
$$

Hence

$$
b+(1-t)a
=
b\left(1+r(1-t)\right)
>
\frac{1+r(1-t)}{1+r}
>z,
$$

contradicting feasibility.  The endpoint $t=0$ would give
$a+b\le z=1$, also a contradiction.  Thus $t\ge t_0$.  Consequently,

$$
D\left(G_I-b^2\right)
=
(1-t)b^2
\left[
r^2-1+t(2r+1)
\right]\ge0.
$$

Therefore $G_I\ge b^2$.

Now assume $b\le a$.  Put

$$
r=\frac ba,
\qquad
t_1=\frac{r^2+2r}{1+2r}.
$$

Since $a+b>1$,

$$
a>\frac1{1+r}.
$$

If $t_1<t<1$, then

$$
\left(
\frac{1+tr}{1+r}
\right)^2-D
=
\frac{(1-t)(1+2r)(t-t_1)}{(1+r)^2}>0.
$$

Hence

$$
a+tb
=
a(1+tr)
>
\frac{1+tr}{1+r}
>z,
$$

contradicting feasibility.  The endpoint $t=1$ again forces $a+b\le1$.
Thus $t\le t_1$.  Consequently,

$$
D\left(G_I-a^2\right)
=
ta^2
\left[
r^2+2r-t(1+2r)
\right]\ge0.
$$

Therefore $G_I\ge a^2$.  This proves the lemma.

## 4. Type II triangles

For Type II define

$$
U=\alpha+(1-t)x+ty,
\qquad
V=\beta+tx-y.
$$

Then

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

Let $A$ and $B$ be the exact reaches of $T$ on the positive $y$ and $x$
axes.  On the $y$ axis, the limiting inequality is $V=\beta-y\ge0$, so

$$
A=\beta.
$$

On the $x$ axis, the limiting inequality is
$U+V=\alpha+\beta+x\le z$, so

$$
B=z-\alpha-\beta.
$$

Therefore

$$
A+B=z-\alpha\le z\le1.
$$

Since $A\ge a$ and $B\ge b$, no Type II triangle is feasible when $a+b>1$.

The inverse map is

$$
x=
\frac{(U-\alpha)+t(V-\beta)}D,
$$

$$
y=
\frac{t(U-\alpha)-(1-t)(V-\beta)}D.
$$

The simplex vertex $(z,0)$ maps to

$$
Q_1=
\left(
\frac{B+(1-t)A}{D},
\frac{A+tB}{D}
\right),
$$

which lies in $W$.  The side $U=0$ has no positive-length intersection with
the interior of $W$.  Hence

$$
T\cap W
=
\mathrm{conv}
\left\{
(0,0),\quad
(B,0),\quad
Q_1,\quad
(0,A)
\right\}.
$$

A shoelace calculation gives the normalized inside area

$$
\frac{(1-t)A^2+tB^2+2AB}{D}.
$$

Thus

$$
\boxed{
G(T)=
G_{II}(A,B;t):=
1-\frac{(1-t)A^2+tB^2+2AB}{D}.
}
$$

### Lemma 4.1: Type II minimum-square bound

For every Type II triangle,

$$
G_{II}(A,B;t)\ge\min(A,B)^2.
$$

### Proof

Set

$$
S=A+B\le z.
$$

First assume $A\le B$.  Write

$$
A=rS,
\qquad
B=(1-r)S,
\qquad
0\le r\le\frac12.
$$

Let

$$
C=(1-t)r^2+t(1-r)^2+2r(1-r).
$$

Then

$$
G_{II}=1-\frac{S^2}{D}C\ge1-C,
$$

because $S^2\le D$.  A direct factorization gives

$$
1-C-r^2D
=
(1-t)\left(1-2r+tr^2\right)\ge0.
$$

Therefore

$$
G_{II}\ge r^2D\ge r^2S^2=A^2.
$$

If $B\le A$, write $B=rS$ and $A=(1-r)S$.  The reflected calculation gives

$$
1-C-r^2D
=
t\left(1-2r+(1-t)r^2\right)\ge0,
$$

and hence $G_{II}\ge B^2$.  This proves the lemma.

Since $A\ge a$ and $B\ge b$,

$$
G(T)\ge\min(A,B)^2\ge\min(a,b)^2.
$$

## 5. Conclusion

Type I and Type II exhaust all unit equilateral triangle orientations.
Lemmas 3.1 and 4.1 prove

$$
G(T)\ge\min(a,b)^2
$$

for every admissible local triangle.  If $a+b>1$, Type II is impossible and
Lemma 3.2 gives

$$
G(T)\ge\max(a,b)^2.
$$

Taking the maximum of the normalized inside area over all admissible triangles
gives the stated bounds for $f(a,b)$.

The proof is valid on all closed boundary faces.  The only strict hypothesis is
$a+b>1$ in the maximum-square statement; equality $a+b=1$ belongs to the
minimum-square statement.
