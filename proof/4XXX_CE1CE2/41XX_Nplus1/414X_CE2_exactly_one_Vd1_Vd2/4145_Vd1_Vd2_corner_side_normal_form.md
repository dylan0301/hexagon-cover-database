# Vd1/Vd2 Corner-Side Normal Form

Status: Proven

This file records the local normal form used by
[`4142_CE2_Nplus1_Vd2_midpoint_local_caps.md`](4142_CE2_Nplus1_Vd2_midpoint_local_caps.md),
[`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md), and
[`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md).

The point is to connect the corner-side half-plane model with the standard
center-and-angle parameterization of a closed unit equilateral triangle.

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

Conversely, any Vd1 or Vd2 row in the corner-side branch, i.e. with its unique
outside vertex equal to the intersection of the two sides cutting the two
adjacent boundary intervals at $V_0$, has this form after possibly reflecting
$x\leftrightarrow y$.

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
P_{\rm loc}=\frac{Q_-+Q_5+Q_1}{3}.
$$

Thus

$$
P_{\rm loc}=\left(
\frac{-at-bt(t+1)+\frac d3(2t+1)}{d^2},
\frac{-(t+1)a-tb+\frac d3(t+2)}{d^2}
\right).
$$

In physical coordinates,

$$
P_{\rm phys}=V_0+P_x(V_5-V_0)+P_y(V_1-V_0).
$$

The physical image of a local vector $(p,q)$ is

$$
\Phi(p,q)=p(V_5-V_0)+q(V_1-V_0)
=\left(-\frac{p+q}{2},\frac{\sqrt3}{2}(q-p)\right).
$$

One side direction is $(t+1,1)/d$ in local coordinates.  Its physical image is

$$
\frac1d\left(-\frac{t+2}{2},-\frac{\sqrt3\,t}{2}\right).
$$

Let $\phi(t)$ be its polar angle:

$$
\cos\phi(t)=-\frac{t+2}{2d},
\qquad
\sin\phi(t)=-\frac{\sqrt3\,t}{2d}.
$$

In the standard center-angle parameterization, the triangle vertices are

$$
P_{\rm phys}+\frac1{\sqrt3}
\left(
\cos\left(\theta+\frac\pi2+\frac{2\pi k}{3}\right),
\sin\left(\theta+\frac\pi2+\frac{2\pi k}{3}\right)
\right),
\qquad k=0,1,2.
$$

Choosing

$$
\theta(t)=\phi(t)-\frac{4\pi}{3}\pmod{2\pi}
$$

makes these three vertices equal to the physical images of $Q_-$, $Q_5$, and
$Q_1$, up to cyclic order.  Hence the displayed half-plane model is exactly the
center-and-rotation model specialized to the corner-side branch.

## Why this covers the Vd1/Vd2 corner branch

For a Vd2 row, both adjacent rays have positive-length intersection and there
is exactly one outside vertex.  In the local corner branch, that outside vertex
is the intersection of the two sides which terminate the adjacent boundary
intervals at $V_0$.  The two sides through that vertex have side directions
which, after reflection if necessary, can be written as positive multiples of
$(t+1,1)$ and $(t,t+1)$ for a unique $t>0$.  Scaling to unit side length gives
the normal form above.

For a Vd1 row in the same corner branch, exactly one of the two adjacent-ray
intersections has positive length.  The same side geometry applies; only one of
the two adjacent-ray interval inequalities is required to be strict.

This proves the normal form used in the 414X local obstruction files.
