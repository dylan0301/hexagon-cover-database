# Supercritical Vertex-Loss Lemma

Status: Proven analytic inequality

This file proves the supercritical half of the square-loss local input used by
the CE0 area certificate, conditional on the supercritical structural
hypothesis from
[`3202_area_function_and_monotonicity.md`](3202_area_function_and_monotonicity.md).

## Statement

Let $H$ be the regular hexagon of side length $1$, normalized at $V_0$.  For
$0\le a,b\le1$, define

$$
P_a=e_{5,0}(a), \qquad P_b=e_{0,1}(b).
$$

Let

$$
A_\Delta=\frac{\sqrt3}{4}
$$

be the area of a unit equilateral triangle.  Define

$$
f(a,b)=\max_T \frac{\mathrm{area}(T\cap H)}{A_\Delta},
$$

where the maximum is over closed unit equilateral triangles $T$ containing

$$
V_0,\qquad P_a,\qquad P_b.
$$

Define the normalized outside-area loss

$$
g(a,b)=1-f(a,b).
$$

Assume the following supercritical structural hypothesis:

> If $a+b>1$, then a maximizing triangle $T(a,b)$ for $f(a,b)$ can be chosen
> with one of its vertices exactly at $P_a$ or $P_b$.

Then

$$
a+b>1 \quad\Longrightarrow\quad g(a,b)\ge \max(a,b)^2.
$$

Equivalently,

$$
a+b>1 \quad\Longrightarrow\quad f(a,b)\le 1-\max(a,b)^2.
$$

## Proof

Work in local coordinates at $V_0$.  Put

$$
u=V_1-V_0, \qquad v=V_5-V_0.
$$

A point is written as $V_0+xu+yv$.  In these coordinates,

$$
V_0=(0,0),\qquad P_b=(b,0),\qquad P_a=(0,a).
$$

The two adjacent supporting half-planes of $H$ at $V_0$ are

$$
x\ge0 \qquad\text{and}\qquad y\ge0.
$$

Let

$$
W=\left\{(x,y):x\ge0,\ y\ge0\right\}.
$$

Then $H\subset W$.  Hence, for every triangle $T$,

$$
T\setminus W\subset T\setminus H,
$$

and therefore

$$
\mathrm{area}(T\setminus H)\ge\mathrm{area}(T\setminus W).
$$

It is enough to prove the required lower bound for the area of $T\setminus W$.

The linear map from $(x,y)$-coordinates to Euclidean coordinates has

$$
\left\lvert \det(u,v)\right\rvert=\frac{\sqrt3}{2}.
$$

Therefore Euclidean area divided by $A_\Delta=\sqrt3/4$ is exactly twice the
corresponding $(x,y)$-coordinate area.  Normalized area computations may be
done in $(x,y)$-coordinates.

We prove the case where $P_b=(b,0)$ is a vertex of $T$.  The case where
$P_a=(0,a)$ is a vertex follows by reflection, which swaps $a$ and $b$.

Assume then that

$$
Q=P_b=(b,0)
$$

is a vertex of $T$.

Since $T$ contains $V_0=(0,0)$, $P_a=(0,a)$, and $a+b>1$, the two other
vertices of $T$ cannot both lie in the closed half-plane $y\ge0$.  If they did,
then the intersection of $T$ with the line $x=0$ would have height at most
$1-b$, contradicting $a>1-b$.

Thus one of the two other vertices lies below $y=0$, and the other lies above
$y=0$.  Name them $R$ and $S$, with

$$
R_y<0<S_y.
$$

The relevant orientation is the one in which, for some $0<t<1$ and $\rho>0$,

$$
R=Q+(-\rho,-t\rho),
$$

and rotation by $60^\circ$ gives

$$
S=Q+(-t\rho,(1-t)\rho).
$$

In the $(x,y)$-coordinates, the Euclidean squared length of a vector $(X,Y)$ is

$$
X^2+Y^2-XY,
$$

because the basis vectors have unit length and mutual angle $120^\circ$.
Therefore the side-length condition for $QR$ is

$$
\rho^2(1-t+t^2)=1.
$$

Set

$$
D=1-t+t^2, \qquad z=\sqrt D.
$$

Then $\rho=1/z$, so the vertices are

$$
Q=(b,0),
$$

$$
R=\left(b-\frac1z,\,-\frac t z\right),
$$

and

$$
S=\left(b-\frac t z,\,\frac{1-t}{z}\right).
$$

Since $T$ contains $V_0=(0,0)$, the line segment $T\cap\left\{y=0\right\}$
contains $[0,b]$.  This implies

$$
b\le z.
$$

Let $Y$ denote the largest $y$-coordinate such that

$$
(0,Y)\in T.
$$

Since $P_a=(0,a)\in T$, we have $a\le Y$.  Because $a+b>1$, it follows that

$$
Y+b>1.
$$

We now compute the normalized area of $T\setminus W$ in two cases.

## Case 1: $S_x\ge0$

The condition $S_x\ge0$ is

$$
b-\frac t z\ge0,
$$

equivalently $b\ge t/z$.  The line $x=0$ meets the side $RS$ at height

$$
Y=\frac{z-b}{1-t}.
$$

The region $T\cap W$ is the quadrilateral with vertices

$$
(0,0),\qquad Q=(b,0),\qquad S=\left(b-\frac t z,\frac{1-t}{z}\right),\qquad (0,Y).
$$

A direct shoelace calculation gives the normalized outside area

$$
G_W=\frac{\mathrm{area}(T\setminus W)}{A_\Delta}=\frac{1-2bz+b^2}{1-t}.
$$

We prove $G_W\ge Y^2$ and $G_W\ge b^2$.

First,

$$
G_W-Y^2=\frac{t(2bz-b^2-t)}{(1-t)^2}.
$$

It is enough to show

$$
2bz-b^2-t\ge0.
$$

Equivalently,

$$
b^2-2bz+t\le0.
$$

The roots of the quadratic $b^2-2bz+t$ are

$$
z-(1-t) \qquad\text{and}\qquad z+(1-t).
$$

Indeed, $z^2-t=(1-t)^2$.  Also,

$$
\bigl(z-(1-t)\bigr)\bigl(z+(1-t)\bigr)=t.
$$

Hence

$$
z-(1-t)=\frac{t}{z+(1-t)}\le \frac t z.
$$

Since this case assumes $b\ge t/z$, we get

$$
b\ge z-(1-t).
$$

Also $b\le z<z+(1-t)$.  Therefore $b$ lies between the two roots, so

$$
b^2-2bz+t\le0.
$$

Thus

$$
G_W\ge Y^2.
$$

Second,

$$
G_W-b^2=\frac{1-2bz+b^2t}{1-t}.
$$

Since $Y+b>1$, and

$$
Y=\frac{z-b}{1-t},
$$

we have

$$
\frac{z-b}{1-t}+b>1.
$$

This is equivalent to

$$
z-bt>1-t.
$$

Thus

$$
bt<z-(1-t).
$$

Since $t>0$,

$$
b<\frac{z-(1-t)}{t}.
$$

Using

$$
\bigl(z-(1-t)\bigr)\bigl(z+(1-t)\bigr)=t,
$$

we obtain

$$
\frac{z-(1-t)}{t}=\frac1{z+(1-t)}.
$$

Therefore

$$
b<\frac1{z+(1-t)}.
$$

The quadratic

$$
1-2bz+b^2t
$$

has smaller positive root $1/(z+(1-t))$.  Hence

$$
1-2bz+b^2t>0.
$$

Therefore

$$
G_W>b^2.
$$

Combining the two estimates,

$$
G_W\ge \max(Y,b)^2.
$$

Since $a\le Y$, we conclude

$$
G_W\ge \max(a,b)^2.
$$

## Case 2: $S_x<0$

The condition $S_x<0$ is

$$
b-\frac t z<0,
$$

equivalently $b<t/z$.  Now the line $x=0$ meets the side $QS$, and the largest
$y$-coordinate in $T\cap\left\{x=0\right\}$ is

$$
Y=\frac{b(1-t)}{t}.
$$

The region $T\cap W$ is the triangle with vertices

$$
(0,0),\qquad (b,0),\qquad (0,Y).
$$

Thus its normalized area is

$$
\frac{\mathrm{area}(T\cap W)}{A_\Delta}=bY=\frac{b^2(1-t)}{t}.
$$

Since the normalized area of $T$ is $1$, we get

$$
G_W=\frac{\mathrm{area}(T\setminus W)}{A_\Delta}=1-\frac{b^2(1-t)}{t}.
$$

We again prove $G_W\ge Y^2$ and $G_W\ge b^2$.

First,

$$
G_W-b^2=1-\frac{b^2(1-t)}{t}-b^2=1-\frac{b^2}{t}=\frac{t-b^2}{t}.
$$

Since $b<t/z$, we have

$$
b^2<\frac{t^2}{z^2}=\frac{t^2}{D}.
$$

But

$$
D=1-t+t^2\ge t,
$$

because $D-t=(1-t)^2\ge0$.  Therefore

$$
\frac{t^2}{D}\le t.
$$

Hence $b^2<t$.  Thus

$$
G_W>b^2.
$$

Second,

$$
G_W-Y^2=1-\frac{b^2(1-t)}{t}-\frac{b^2(1-t)^2}{t^2}=\frac{t^2-b^2(1-t)}{t^2}.
$$

Again, since $b<t/z$, we have

$$
b^2<\frac{t^2}{D}.
$$

Also

$$
D=1-t+t^2\ge1-t.
$$

Therefore

$$
\frac{t^2}{D}\le \frac{t^2}{1-t}.
$$

Hence

$$
b^2<\frac{t^2}{1-t}.
$$

Equivalently,

$$
b^2(1-t)<t^2.
$$

Thus

$$
G_W>Y^2.
$$

Combining the two estimates,

$$
G_W\ge \max(Y,b)^2.
$$

Since $a\le Y$, we conclude

$$
G_W\ge \max(a,b)^2.
$$

## Conclusion

In both cases,

$$
\frac{\mathrm{area}(T\setminus W)}{A_\Delta}\ge\max(a,b)^2.
$$

Since $H\subset W$, we have

$$
\frac{\mathrm{area}(T\setminus H)}{A_\Delta}\ge\frac{\mathrm{area}(T\setminus W)}{A_\Delta}.
$$

Therefore, if $T$ is a unit equilateral triangle containing

$$
V_0,\qquad P_a,\qquad P_b,
$$

with $a+b>1$, and if $P_b$ is a vertex of $T$, then

$$
\frac{\mathrm{area}(T\setminus H)}{A_\Delta}\ge\max(a,b)^2.
$$

By reflection across the symmetry axis through $V_0$, the identical statement
holds if $P_a$ is a vertex of $T$.

Now assume the supercritical structural hypothesis.  For $a+b>1$, choose a
maximizing triangle $T(a,b)$ for $f(a,b)$ with one vertex at $P_a$ or $P_b$.
Then

$$
f(a,b)=\frac{\mathrm{area}(T(a,b)\cap H)}{A_\Delta},
$$

so

$$
g(a,b)=1-f(a,b)=\frac{\mathrm{area}(T(a,b)\setminus H)}{A_\Delta}.
$$

By the vertex-loss estimate above,

$$
g(a,b)\ge \max(a,b)^2.
$$

Thus

$$
a+b>1 \quad\Longrightarrow\quad g(a,b)\ge \max(a,b)^2.
$$

This proves the lemma.
