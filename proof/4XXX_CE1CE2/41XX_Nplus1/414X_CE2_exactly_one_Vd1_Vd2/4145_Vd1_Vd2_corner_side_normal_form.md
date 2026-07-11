# Vd1/Vd2 Corner-Side Normal Form

Status: Proven

This file records the local normal form used by
[`4142_CE2_Nplus1_Vd2_midpoint_local_caps.md`](4142_CE2_Nplus1_Vd2_midpoint_local_caps.md),
[`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md),
[`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md), and
[`4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`](4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md).

The point is to connect the corner-side half-plane model with the standard
center-and-angle parameterization of a closed unit equilateral triangle, and to
record the adjacent-ray inequality used repeatedly in the 414X branch.

## Statement

Normalize at $V_0$ and use local coordinates

$$
X=V_0+x(V_5-V_0)+y(V_1-V_0).
$$

Then

$$
\|(p,q)\|^2=p^2+q^2-pq.
$$

Let $t>0$, $a\ge0$, $b\ge0$, and

$$
d=\sqrt{t^2+t+1}.
$$

The closed region

$$
\boxed{
\begin{aligned}
x-(t+1)y&\le a,\\
ty-(t+1)x&\le tb,\\
tx+y&\le d-a-tb
\end{aligned}}
$$

is a closed unit equilateral triangle.  Its adjacent boundary coverages from
$V_0$ are exactly $a$ on $e_{5,0}$ and $b$ on $e_{0,1}$ whenever the displayed
corner is the local corner at $V_0$.

Conversely, let a Vd1 or Vd2 row have actual adjacent boundary reaches $a,b$.
There is an exact dichotomy:

1. if $a+b>0$, the row has this form after possibly reflecting
   $x\leftrightarrow y$;
2. if $a=b=0$, a vertex-degenerate Vd1 configuration may fall outside this
   normal form and must be handled separately.

## Derivation from vertices

The three boundary lines are

$$
L_1:x-(t+1)y=a,
$$

$$
L_2:ty-(t+1)x=tb,
$$

and

$$
L_3:tx+y=d-a-tb.
$$

Their pairwise intersections are

$$
Q_-=
\left(
-\frac{t(a+(t+1)b)}{d^2},
-\frac{(t+1)a+tb}{d^2}
\right),
$$

$$
Q_5=
\left(
\frac{(t+1)(d-tb)-ta}{d^2},
\frac{d-(t+1)a-tb}{d^2}
\right),
$$

and

$$
Q_1=
\left(
\frac{t(d-a)-t(t+1)b}{d^2},
\frac{(t+1)d-(t+1)a-tb}{d^2}
\right).
$$

A direct subtraction gives

$$
Q_5-Q_- = \frac{(t+1,1)}d,
$$

$$
Q_1-Q_- = \frac{(t,t+1)}d,
$$

and

$$
Q_1-Q_5 = \frac{(-1,t)}d.
$$

Each of the three displayed vectors has local squared length one.  Indeed,

$$
(t+1)^2+1-(t+1)=d^2,
$$

$$
t^2+(t+1)^2-t(t+1)=d^2,
$$

and

$$
(-1)^2+t^2-(-1)t=d^2.
$$

Thus the three vertices form a unit equilateral triangle in the hexagon metric.
The three half-planes above choose the triangle containing the local corner
$V_0=(0,0)$.

The side $L_1$ cuts $e_{5,0}$ at $(a,0)$ and the side $L_2$ cuts $e_{0,1}$ at
$(0,b)$.  Hence the adjacent boundary interval endpoints are exactly $a$ and
$b$.

## Center and rotation angle

The center in local coordinates is

$$
P_{\mathrm{loc}}=\frac{Q_-+Q_5+Q_1}{3}.
$$

Thus

$$
P_{\mathrm{loc}}=\left(
\frac{-at-bt(t+1)+\frac d3(2t+1)}{d^2},
\frac{-(t+1)a-tb+\frac d3(t+2)}{d^2}
\right).
$$

In physical coordinates,

$$
P_{\mathrm{phys}}=V_0+P_x(V_5-V_0)+P_y(V_1-V_0).
$$

The physical image of a local vector $(p,q)$ is

$$
\Phi(p,q)=p(V_5-V_0)+q(V_1-V_0)
=\left(-\frac{p+q}{2},\frac{\sqrt3}{2}(q-p)\right).
$$

One side direction is $(t+1,1)/d$ in local coordinates.  Its physical image is

$$
\frac1d\left(-\frac{t+2}{2},-\frac{\sqrt3 t}{2}\right).
$$

Let $\phi(t)$ be its polar angle:

$$
\cos\phi(t)=-\frac{t+2}{2d},
\qquad
\sin\phi(t)=-\frac{\sqrt3 t}{2d}.
$$

In the standard center-angle parameterization, the triangle vertices are

$$
P_{\mathrm{phys}}+\frac1{\sqrt3}
\left(
\cos\left(\theta+\frac\pi2+\frac{2\pi k}{3}\right),
\sin\left(\theta+\frac\pi2+\frac{2\pi k}{3}\right)
\right),
\qquad k=0,1,2.
$$

Choosing

$$
\theta(t)=\phi(t)-\frac{4\pi}{3}
\pmod{2\pi}
$$

makes these three vertices equal to the physical images of $Q_-$, $Q_5$, and
$Q_1$, up to cyclic order.  Hence the displayed half-plane model is exactly the
center-and-rotation model specialized to the corner-side branch.

## Proof of the dichotomy

Let $W$ be the unique vertex of the row triangle outside $H$, and let $U,Z$ be
the other two vertices. Thus $U,Z\in H$. In the local coordinates above, the
tangent cone of $H$ at $V_0$ is

$$
x\ge0,
\qquad
y\ge0.
$$

Assume first that $a+b>0$. Then $V_0$ is not a vertex of the row triangle. If
it were, positive boundary reach would force an incident unit side to lie on
one of the two unit hexagon edges at $V_0$. That side would equal the whole
hexagon edge. The equilateral choice with one outside vertex lies outside the
supporting line of that edge and has no positive-length adjacent-ray
intersection, contradicting Vd1/Vd2.

Write the positive barycentric relation

$$
V_0=\omega W+\mu U+\nu Z,
\qquad
\omega>0,
\qquad
\mu,\nu\ge0,
\qquad
\omega+\mu+\nu=1.
$$

Since $U$ and $Z$ have nonnegative local coordinates, this relation forces

$$
W_x\le0,
\qquad
W_y\le0.
$$

The opposite side $UZ$ lies in the convex hexagon. It cannot cut either
adjacent supporting edge in its relative interior unless its line coincides
with that hexagon edge: a noncoincident line would cross from the interior to
the exterior. If it coincides, its unit length again makes it the whole
hexagon edge, and the outside equilateral choice has $n=0$. Therefore the two
sides terminating the adjacent boundary intervals are the sides incident to
$W$.

Their two directions point from the southwest tangent cone into the local
first quadrant. The equilateral angle relation gives, after reflection if
necessary, positive multiples of

$$
(t+1,1),
\qquad
(t,t+1)
$$

for a unique $t>0$. Unit normalization gives the three displayed half-planes.
This proves the normal form whenever $a+b>0$.

The exception $a=b=0$ is real. Put $r=1/\sqrt3$. Then

$$
\mathrm{conv}\left\{
(0,0),
(-r,r),
(r,2r)
\right\}
$$

is a unit equilateral triangle with one outside vertex and positive-length
intersection with $r_1$. It is Vd1, contains the neighboring midpoint
$M_1=(1/2,1)$, and is not in the southwest corner-side form. Downstream uses
must therefore split off $a=b=0$ before invoking the normal form.

## Adjacent-ray bound

In this normal form, if the outgoing adjacent ray has positive-length
intersection, the lower endpoint is strictly smaller than the upper endpoint.
This gives

$$
(t+1)a+tb<(t+1)(d-1)-t^2.
$$

Since

$$
(t+1)a+tb\ge t(a+b),
$$

we have

$$
a+b<\frac{(t+1)(d-1)-t^2}{t}.
$$

The right-hand side is strictly less than $1/2$.  Indeed this is equivalent to

$$
(t+1)d<t^2+\frac{3t}{2}+1,
$$

and after squaring the positive sides,

$$
\left(t^2+\frac{3t}{2}+1\right)^2-(t+1)^2(t^2+t+1)=\frac{t^2}{4}>0.
$$

The incoming adjacent-ray case is the reflection and gives the same bound.
Hence every nondegenerate Vd1/Vd2 row satisfies

$$
\boxed{a+b<\frac12}
$$

whenever it has positive-length adjacent-ray intersection.  In endpoint-only
closure cases the corresponding weak inequality $a+b\le1/2$ holds.

The exceptional case has $a+b=0$, so the same strict bound is trivially true
there even though the half-plane parameterization need not apply.
