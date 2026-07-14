# V-Triangle Types

Status: Proven

For a $V_i$-triangle, define

$$
o=\left\lvert \left\lbrace \text{vertices of }T_i\text{ outside }H \right\rbrace \right\rvert,
$$

and

$$
n=\left\lvert \left\lbrace \text{adjacent rays }r_{i-1},r_{i+1}
\text{ having positive-length intersection with }T_i \right\rbrace \right\rvert.
$$

Every original vertex role has

$$
1\le o\le3.
$$

Indeed, an original vertex role comes from an open triangle containing the
extreme point $V_i$, so $V_i$ lies in the interior of its closed triangle. If
all three triangle vertices belonged to the convex hexagon $H$, the whole
triangle would belong to $H$, which is impossible for a subset of $H$ having
the extreme point $V_i$ in its interior.

The zero-adjacent-support class is

$$
\boxed{
\mathrm{Vd0}: n=0,
}
$$

or equivalently

$$
\mathrm{Vd0}:
(o,n)=(1,0),(2,0),\text{ or }(3,0).
$$

The positive-support names are

$$
\mathrm{Vd1}: (o,n)=(1,1),
$$

$$
\mathrm{Vd2}: (o,n)=(1,2),
$$

and

$$
\mathrm{T3\text{-}like}: (o,n)=(2,1).
$$

Thus a T3-like $V_i$-triangle has positive-length intersection with exactly one
of the adjacent half-diagonals $r_{i-1}$ and $r_{i+1}$. Among the six
half-diagonals, it can have positive-length intersection only with its own ray
$r_i$ and exactly one of $r_{i-1}$ and $r_{i+1}$. Equivalently, after rotating
indices to $i=0$, it can meet only $OV_0$ and exactly one of $OV_1$ and $OV_5$
in positive length. Indeed, every point other than $O$ on a nonlocal ray
$r_j$, with $j\notin\{i-1,i,i+1\}$, is at distance strictly greater than $1$
from $V_i$. A unit triangle containing $V_i$ has diameter $1$, so its contact
with any such ray has zero length.

## Local wedge lemma

Rotate to $i=0$ and use coordinates

$$
X=V_0+x(V_1-V_0)+y(V_5-V_0).
$$

Then $V_0=(0,0)$,

$$
\lVert(x,y)\rVert^2=x^2+y^2-xy,
$$

and

$$
H=\left\{(x,y):0\le x\le2,\ 0\le y\le2,\ -1\le x-y\le1\right\}.
$$

The local cone and adjacent rays are

$$
W=\left\{(x,y):x\ge0,\ y\ge0\right\},
$$

$$
r_1=\left\{(1,y):0\le y\le1\right\},
\qquad
r_5=\left\{(x,1):0\le x\le1\right\}.
$$

Because $V_0\in T$, every point of the unit triangle $T$ has distance at most
$1$ from $V_0$. Inside that unit ball, membership in $H$ is equivalent to
membership in $W$. The nontrivial direction follows from

$$
x^2+y^2-xy
=\left(y-\frac{x}{2}\right)^2+\frac{3x^2}{4}
=\left(x-y\right)^2+xy.
$$

Thus $x,y\ge0$ and $\lVert(x,y)\rVert\le1$ imply $x,y<2$ and
$\lvert x-y\rvert\le1$.

We will use the following support observation. If $T\cap r_1$ has positive
length, then at least one vertex of $T$ lies in $H$. To see this, let $m$ be
the maximum $x$-coordinate of the vertices of $T$. If $m>1$, a maximizing
vertex $P=(m,y)$ satisfies

$$
m^2+y^2-my\le1.
$$

This forces $0<y<1$: for $y\le0$ the left side is greater than $1$, while for
$y\ge1$ its expression as $(m-y)^2+my$ is greater than $1$. Hence $P\in W$
and therefore $P\in H$. If $m=1$, positive-length intersection with the
supporting line $x=1$ means that an entire side of $T$ lies on that line. Its
two endpoint vertices satisfy

$$
1+y^2-y\le1,
$$

so $0\le y\le1$ and both endpoints belong to $H$. The same statement holds
with $x$ and $y$ interchanged for $r_5$.

Moreover, if both adjacent rays have positive-length intersection with $T$,
then at least two vertices of $T$ belong to $H$. Otherwise there would be a
unique vertex of $T$ in $H$. The preceding argument rules out a supporting
side on either $x=1$ or $y=1$, since that would already give two vertices in
$H$. The unique vertex would therefore have to satisfy $x>1$ to support
$r_1$, and also $y>1$ to support $r_5$. This is impossible because

$$
x^2+y^2-xy=(x-y)^2+xy>1.
$$

## Exhaustiveness theorem

Every original vertex role belongs to exactly one of

$$
\boxed{\mathrm{Vd0},\quad \mathrm{Vd1},\quad \mathrm{Vd2},\quad
\mathrm{T3\text{-}like}.}
$$

Indeed, $n\in\{0,1,2\}$. If $n\ge1$, the local wedge lemma gives at least one
triangle vertex in $H$, so $o\le2$. If $n=2$, it gives at least two triangle
vertices in $H$, so $o\le1$. Combining these facts with $1\le o\le3$ leaves
exactly

$$
\begin{array}{c|c}
n&\text{possible values of }o\\
\hline
0&1,2,3\\
1&1,2\\
2&1.
\end{array}
$$

These are precisely the four named classes. In particular,

$$
(o,n)=(2,2),\ (3,1),\ (3,2)
$$

are unattainable.

## T3-like translation normalization

We now prove the normalization used in later T3-like arguments.

### Theorem

Let $T$ be the closed unit triangle associated with an original T3-like
$V_i$-role. There is a translate $T'$ of $T$, with the same side length and
orientation, such that

$$
V_i\text{ lies in the relative interior of a side of }T',
$$

$$
T\cap H\subsetneq T'\cap H,
$$

and $T'$ still has type $(o,n)=(2,1)$. Thus replacing $T$ by $T'$ preserves
the entire old closed trace in $H$ and strictly enlarges that trace.  If the
original role is viewed as an open triangle, every old interior point in $H$
other than $V_i$ remains interior to the translate; $V_i$ itself becomes a
boundary point.  The normalization is therefore a closed-trace domination
tool, not a literal replacement for the role triangle at $V_i$ in an open
cover.

### Orientation normal forms

It is enough to work at $V_0$. Put

$$
D=1-t+t^2,
\qquad
z=\sqrt D,
\qquad
0\le t\le1.
$$

In these coordinates physical rotation by $60^\circ$ is

$$
R(x,y)=(x-y,x).
$$

After relabelling the vertices of the equilateral triangle, every orientation
has one of the following two forms. For Type I the two side vectors from one
vertex are

$$
\frac{1}{z}(1,t),
\qquad
\frac{1}{z}(1-t,1),
$$

and for Type II they are

$$
\frac{1}{z}\left(t,-(1-t)\right),
\qquad
\frac{1}{z}(1,t).
$$

In each pair the vectors have unit norm and differ by a physical
$60^\circ$ rotation. As $t$ runs from $0$ to $1$, the Type II first vector
runs through the angular sector from $60^\circ$ to $120^\circ$, and the
Type I first vector runs through the sector from $120^\circ$ to $180^\circ$.
For an equilateral triangle there are three ordered side directions $d$ for
which the other side from the same vertex is $Rd$; they differ by
$120^\circ$. One of them lies in the sector from $60^\circ$ to $180^\circ$
(with the duplicated endpoints assigned to either form), so the two forms are
exhaustive.

In Type I, set

$$
U=\alpha+y-tx,
\qquad
V=\beta+x-(1-t)y,
$$

and write

$$
T=\left\{U\ge0,\ V\ge0,\ U+V\le z\right\}.
$$

In Type II, set

$$
U=\alpha+(1-t)x+ty,
\qquad
V=\beta+tx-y,
$$

with the same three inequalities. Inverting the two linear equations for
$U$ and $V$ gives exactly the side-vector pairs displayed above, so these
inequalities describe unit equilateral triangles. Since $V_0$ is interior to
the original role,

$$
\alpha>0,
\qquad
\beta>0,
\qquad
\alpha+\beta<z.
$$

### Type I is not T3-like

For Type I, the vertices corresponding to $(U,V)=(0,0),(0,z),(z,0)$ are

$$
Q_0=\left(-\frac{(1-t)\alpha+\beta}{D},
-\frac{\alpha+t\beta}{D}\right),
$$

$$
Q_1=\left(\frac{z-(1-t)\alpha-\beta}{D},
\frac{tz-\alpha-t\beta}{D}\right),
$$

and

$$
Q_2=\left(\frac{(1-t)z-(1-t)\alpha-\beta}{D},
\frac{z-\alpha-t\beta}{D}\right).
$$

The vertex $Q_0$ lies outside $W$, the first coordinate of $Q_1$ is
nonnegative, and the second coordinate of $Q_2$ is nonnegative. Suppose a
Type I triangle has $o=2$. If $Q_1$ is the second outside vertex, then

$$
\alpha+t\beta>tz,
$$

and the sole vertex $Q_2$ in $W$ has both coordinates strictly below $1$.
Indeed, both are at most $(1-t)/z$; this is less than $1$ when $t>0$, and the
strict inequalities in the displayed formulas handle $t=0$. If instead
$Q_2$ is the second outside vertex, the reflected calculation shows that both
coordinates of the sole wedge vertex $Q_1$ are strictly below $1$: they are at
most $t/z<1$ for $t<1$, with the formulas giving strictness at $t=1$.

The proof of the support observation gives the slightly sharper fact needed
here: if $r_1$ has positive-length intersection and there is only one triangle
vertex in $H$, then that vertex has $x>1$; the supporting-side alternative
would put two vertices in $H$.  The reflected statement for $r_5$ requires
$y>1$.  Since the sole wedge vertex found above has both coordinates below
$1$, neither adjacent ray can have positive-length intersection with $T$.
Hence Type I with $o=2$ has $n=0$ and cannot be T3-like.

### Translation in Type II

A T3-like triangle therefore has Type II form. Before choosing its Type II
parameters, reflect in $x=y$ if necessary so that its positive adjacent
support is on $r_1$. Its two outside vertices and its unique wedge vertex are

$$
P_0=\left(\frac{-\alpha-t\beta}{D},
\frac{-t\alpha+(1-t)\beta}{D}\right),
$$

$$
P_1=\left(\frac{-\alpha+t(z-\beta)}{D},
\frac{-t\alpha-(1-t)(z-\beta)}{D}\right),
$$

and

$$
Q=\left(\frac{z-\alpha-t\beta}{D},
\frac{t(z-\alpha)+(1-t)\beta}{D}\right).
$$

Here $(P_0)_x<0$, $(P_1)_y<0$, and both coordinates of $Q$ are positive.
The endpoint cases $t=0$ and $t=1$ give a unique wedge vertex with both
coordinates below $1$.  The sharper support conclusion proved in the local
wedge lemma then rules out positive adjacent support, so these cases cannot be
T3-like. Thus

$$
0<t<1.
$$

The exact reaches of $T$ along the positive $y$- and $x$-axes are

$$
A=\beta,
\qquad
B=z-\alpha-\beta.
$$

Both are strictly below $1$. More generally, if a point lies in the interior
of a convex set of diameter $1$, its distance from every point of that set is
strictly below $1$: otherwise a small continuation from the interior point in
the opposite direction would produce two points more than $1$ apart. Apply
this observation to the interior point $V_0$ and the two axis endpoints.

For $0<t<1$, no side of $T$ is parallel to either adjacent ray, and

$$
T\cap W=\mathrm{conv}\left\{(0,0),(B,0),Q,(0,A)\right\}.
$$

Consequently, positive-length intersection with $r_1$ is equivalent to
$Q_x>1$, and positive-length intersection with $r_5$ is equivalent to
$Q_y>1$. Our reflection choice gives

$$
Q_x>1,
\qquad
Q_y\le1.
$$

Define $T'$ by keeping $t$ and $\beta$ fixed and replacing $\alpha$ by $0$ in
the Type II inequalities. The two linear parts defining $U$ and $V$ have
nonzero determinant, so this change of the two affine constants is exactly a
translation of $T$; it does not rotate or resize the triangle. At the origin,

$$
U'=0,
\qquad
0<V'=\beta<z,
$$

so $V_0$ lies in the relative interior of the side $U'=0$.

For every $(x,y)\in W$,

$$
U'=(1-t)x+ty\ge0,
\qquad
V'=V,
\qquad
U'+V'=U+V-\alpha.
$$

It follows immediately that

$$
T\cap W\subset T'\cap W.
$$

The old $x$-axis reach was $B$, while the new reach is $B+\alpha$. Since
$B<1$ and $\alpha>0$, a point with

$$
B<x<\min\left\{B+\alpha,1\right\}
$$

lies in $(T'\cap H)\setminus T$. Because $H\subset W$, this proves

$$
T\cap H\subsetneq T'\cap H.
$$

There is also no hidden open-triangle loss away from $V_0$.  If
$(x,y)\in H\setminus\{V_0\}$ was in the interior of $T$, then $x,y\ge0$ and
$U',V'>0$: the only point of $W$ at which
$U'=(1-t)x+ty$ vanishes is the origin.  Moreover
$U'+V'=U+V-\alpha<z$. Thus the point remains in the interior of $T'$.

It remains to check that the translation preserves the type. The two vertices
of $T'$ corresponding to $P_0$ and $P_1$ still satisfy

$$
(P'_0)_x=-\frac{t\beta}{D}<0,
\qquad
(P'_1)_y=-\frac{(1-t)(z-\beta)}{D}<0,
$$

while both coordinates of $Q'$ are positive.  Since $V_0,Q'\in T'$ and $T'$
has diameter $1$, the local wedge lemma puts $Q'$ in $H$.  Hence exactly the
other two vertices are outside $H$, so $o=2$. The new wedge
vertex also satisfies $Q'_x>Q_x>1$. From $Q_x>1$ we have

$$
t\beta<z-\alpha-D.
$$

Therefore

$$
\begin{aligned}
tD(1-Q'_y)
&=tD-t^2z-t(1-t)\beta\\
&>tD-t^2z-(1-t)(z-\alpha-D)\\
&=D(1-z)+(1-t)\alpha>0.
\end{aligned}
$$

Thus $Q'_y<1$, so $T'$ supports $r_1$ in positive length and does not support
$r_5$ in positive length. Hence $n=1$, completing the normalization proof.
