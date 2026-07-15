# Vd1/Vd2 Corner Normal Form

Status: Proven

This note isolates the corner geometry used by the CE2 Vd1/Vd2 packages.
Throughout, $T$ is the closure of an original open $V_0$-role, so

$$
V_0\in\mathrm{int}(T).
$$

Use local coordinates

$$
X=V_0+x(V_5-V_0)+y(V_1-V_0).
$$

Then

$$
V_0=(0,0),\qquad V_5=(1,0),\qquad V_1=(0,1),\qquad O=(1,1),
$$

and

$$
\lVert(x,y)\rVert^2=x^2+y^2-xy.
$$

Let $a,b$ be the exact reaches of $T$ from $V_0$ on $e_{5,0}$ and
$e_{0,1}$.

## Theorem

If $T$ is Vd1 or Vd2, there is a unique $t>0$ such that, with

$$
d=\sqrt{t^2+t+1},
$$

one has

$$
\boxed{
T=\left\{(x,y):
\begin{aligned}
x-(t+1)y&\le a,\\
ty-(t+1)x&\le tb,\\
tx+y&\le d-a-tb
\end{aligned}
\right\}.
}
$$

Moreover,

$$
0<a<1,\qquad 0<b<1.
$$

The raw endpoint formulas on the three local radial arms are

$$
c_0=\frac{d-a-tb}{t+1}
$$

on $r_0=[V_0,O]$,

$$
\lambda_1=\frac{t(1-b)}{t+1},
\qquad
\mu_1=\frac{d-a-tb-1}{t}
$$

on $r_1=[V_1,O]$, with coordinate measured from $V_1$, and

$$
\lambda_5=\frac{1-a}{t+1},
\qquad
\mu_5=d-a-tb-t
$$

on $r_5=[V_5,O]$, with coordinate measured from $V_5$. Intersecting these
raw intervals with $[0,1]$ gives the actual ray traces.

Finally, positive-length intersection with either adjacent radial arm implies

$$
\boxed{a+b<\frac12.}
$$

## Proof of the normal form

A Vd1 or Vd2 triangle has one vertex $W$ outside $H$ and two vertices
$U,Z$ in $H$. Because $V_0$ is an interior point, its barycentric expression

$$
V_0=\omega W+\mu U+\nu Z
$$

has

$$
\omega,\mu,\nu>0,
\qquad
\omega+\mu+\nu=1.
$$

The local coordinates of $U,Z$ are nonnegative. Hence both coordinates of
$W$ are nonpositive. They are in fact negative. For example, if $W_x=0$,
the barycentric identity forces $U_x=Z_x=0$. Then the unit side $UZ$ is the
whole edge $e_{0,1}$, placing $V_0$ on the boundary of $T$, a contradiction.
The argument for $W_y$ is identical.

Since $V_0$ is interior, both incident-edge traces contain nontrivial initial
intervals, so

$$
A=(a,0),\qquad B=(0,b)
$$

are well-defined with $a,b>0$. Neither $A$ nor $B$ can lie in the relative
interior of the side $UZ$. If, for example, $A\in\mathrm{relint}(UZ)$, the
nonnegative $y$-coordinates of $U,Z$ have a strict convex combination equal
to zero. Thus $U_y=Z_y=0$, so $UZ=e_{5,0}$ and again $V_0\in\partial T$.
The argument for $B$ is the same.

Thus $A$ and $B$ lie on sides incident with $W$. They lie on distinct sides.
Indeed, along a segment from a point with two negative coordinates to a point
with two nonnegative coordinates, a positive crossing of $y=0$ occurs after
the crossing of $x=0$, whereas a positive crossing of $x=0$ occurs after the
crossing of $y=0$. One segment cannot have both orders. Relabel $U,Z$ so that

$$
A\in WU,
\qquad
B\in WZ.
$$

Put

$$
p=U-W,
\qquad
q=Z-W.
$$

Both coordinates of $p,q$ are positive, and

$$
\lVert p\rVert=\lVert q\rVert=\lVert p-q\rVert=1.
$$

Thus the physical angle from $p$ to $q$ is $60$ degrees. In the present
coordinates, clockwise physical rotation through $60$ degrees is

$$
R_{-60}(r,s)=(r-s,r).
$$

Write $r=-W_x>0$ and $s=-W_y>0$. The two positive axis crossings give

$$
\frac{p_y}{p_x}<\frac{s}{r}<\frac{q_y}{q_x}.
$$

Of the two possible $60$-degree rotations, this slope order forces

$$
q=R_{-60}p=(p_x-p_y,p_x),
\qquad
p_x>p_y>0.
$$

Set

$$
t=\frac{p_x-p_y}{p_y}>0.
$$

Unit normalization gives

$$
p=\frac{(t+1,1)}d,
\qquad
q=\frac{(t,t+1)}d,
\qquad
d=\sqrt{t^2+t+1}.
$$

This also proves uniqueness of $t$. The two side lines through $A$ and $B$
are

$$
x-(t+1)y=a,
\qquad
ty-(t+1)x=tb.
$$

Their intersection is $W$. The third side is parallel to

$$
q-p=\frac{(-1,t)}d,
$$

so it has equation $tx+y=k$. At $W$ the left side equals $-a-tb$, and
moving from $W$ to $U$ increases it by

$$
tp_x+p_y=d.
$$

Therefore $k=d-a-tb$. The three half-planes containing the origin are exactly
those in the theorem.

Because $V_0$ is interior to a set of diameter $1$, every other point of $T$
is at distance strictly less than $1$ from $V_0$. In particular neither
$V_5$ nor $V_1$ belongs to $T$, and hence $a,b<1$.

## Ray formulas and the half-unit cap

Substitution of $(s,s)$ gives the own-ray formula. On $r_1$, substitute
$(x,y)=(s,1)$. The first inequality is automatic on $0\le s\le1$, and the
other two give

$$
s\ge\lambda_1,
\qquad
s\le\mu_1.
$$

The $r_5$ formulas follow similarly from $(x,y)=(1,s)$.

If $T$ has positive-length intersection with $r_1$, then

$$
\lambda_1<\mu_1.
$$

Clearing positive denominators gives

$$
(t+1)a+tb<(t+1)(d-1)-t^2.
$$

Since the left side is at least $t(a+b)$,

$$
a+b<\frac{(t+1)(d-1)-t^2}{t}.
$$

The last expression is less than $1/2$. This is equivalent to

$$
(t+1)d<t^2+\frac{3t}{2}+1,
$$

and both sides are positive, while

$$
\left(t^2+\frac{3t}{2}+1\right)^2
-(t+1)^2(t^2+t+1)=\frac{t^2}{4}>0.
$$

Reflection in $x=y$ handles positive-length intersection with $r_5$.
Therefore every Vd1 or Vd2 original role has $a+b<1/2$.

$$
\Box
$$
