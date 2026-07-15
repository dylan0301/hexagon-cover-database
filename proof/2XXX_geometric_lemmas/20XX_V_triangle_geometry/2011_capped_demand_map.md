# Exact Capped Nonsupercritical Demand Map

Status: Proven

This note gives the branch-independent capped demand map used throughout the
CE1/CE2 boundary-loss arguments. It is a specialization of the exact
admissible set in [`2004_admissible_set.md`](2004_admissible_set.md), with
the component selector from that theorem retained throughout.

The definition and four-label partition below apply for every
$0\le a,c\le1$. The closed piecewise catalog is stated only in the
high-radial range $1/2<c<1$ used by the later five-map arguments. At
$c\le1/2$ and at the endpoints $c=1/2,1$, the globally exact formula remains
$F_c(a)=\min\left\{B_c(a),1-a\right\}$ with $B_c$ supplied by `2007`; no
unstated continuation of the high-radial display is intended.

## 1. Definitions

For $0\le a,c\le1$, let $B_c(a)$ be the exact unclassified map proved in
[`2007_max_b_map.md`](2007_max_b_map.md).
Define

$$
F_c(a)=\min\left\{B_c(a),1-a\right\},
\qquad
G_c(a)=1-F_c(a).
$$

Equivalently, the interval-fiber theorem in `2007` gives

$$
F_c(a)=
\max_{\substack{
0\le b\le1-a\\
{}(a,b,c)\in\mathcal A
}}b.
$$

Thus $F_c$ is the exact demand-coordinate cap. It is the proof-safe upper
relaxation for a nonsupercritical Vd0 row; no assertion that its maximizing
triangle belongs to that row class is needed.

More precisely, let $A(T),B(T),C(T)$ be the actual local reaches of any
vertex-role triangle, and suppose

$$
A(T)\ge a,
\qquad
C(T)\ge c,
\qquad
A(T)+B(T)\le1.
$$

Then the same triangle realizes the demand triple $(a,B(T),c)$, while

$$
B(T)\le1-A(T)\le1-a.
$$

Hence

$$
\boxed{B(T)\le F_c(a).}
$$

Taking suprema proves the same bound for any actual nonsupercritical row
class. This is the only passage from demand coordinates to classified rows
used downstream.

The exact-cell proof below also gives an exhaustive four-label partition of
every maximizer:

$$
\boxed{
\mathrm{Full},\qquad L,\qquad T_-,\qquad T_+.
}
$$

The genuine selected $T_+$ component is called $T_+^{hi}$ in the older
branch files. The other formal quadratic component, formerly called
$T_+^{lo}$, violates the selector
$c\le2\max\left\{a,b\right\}$ and is not a geometric
branch. Transition ties may be assigned in the order displayed in the
piecewise catalog; they do not create a fifth label.

For $1/2<c<1$, put

$$
\ell(c)=
\frac c2
\left(
1-\sqrt{4c^2-3}
\right),
$$

$$
r(c)=
\frac c2
\left(
1+\sqrt{4c^2-3}
\right)
=c-\ell(c),
$$

whenever $c\ge\sqrt3/2$, and put

$$
h(c)=
\frac{2c}{\sqrt{16c^2-3}+1}
=
\frac{c\left(\sqrt{16c^2-3}-1\right)}
{2(4c^2-1)}.
$$

The two nonconstant contact values are

$$
T_-(a,c)=
\frac{\sqrt{a^2-ac+c^2}}c-a
$$

and

$$
T_+(a,c)=
\frac{2(1-a^2)c^2}
{2ac^2+c+\sqrt{\Delta(a,c)}},
$$

where

$$
\Delta(a,c)=
(2ac^2+c)^2
-4(1-c^2)(1-a^2)c^2.
$$

The formula for $T_+$ is the rationalized lower quadratic root. On its
domain it is equal to

$$
\frac{2ac^2+c-\sqrt{\Delta(a,c)}}{2(1-c^2)},
$$

but the rationalized form remains stable as $c$ approaches $1$.

For later comparisons on a selected $T_-$ branch, define

$$
\Psi^-_{a,c}(x)
=c^2(a+x)^2-(a^2-ac+c^2).
$$

For $c>0$ and $a,x\ge0$, the displayed formula for $T_-$ gives the exact
root-order test

$$
\boxed{
T_-(a,c)<x
\quad\Longleftrightarrow\quad
\Psi^-_{a,c}(x)>0.
}
$$

Indeed, both sides of
$\sqrt{a^2-ac+c^2}<c(a+x)$ are nonnegative, so it may be squared without
changing its direction. Moreover

$$
\frac{\partial}{\partial x}\Psi^-_{a,c}(x)=2c^2(a+x)\ge0,
$$

with strict increase unless $a=x=0$. This supplies the monotonicity used in
downstream root-order arguments.

## 2. Exact high-radial catalog

### 2.1. The range $1/2<c\le\sqrt3/2$

For every $0\le a\le1$,

$$
\boxed{
F_c(a)=
\begin{cases}
1-a,
& 0\le a\le1-c,\\
T_+(a,c),
& 1-c<a<h(c),\\
h(c),
& a=h(c),\\
T_-(a,c),
& h(c)<a<c,\\
1-a,
& c\le a\le1.
\end{cases}
}
$$

At the middle equality,

$$
T_+(h(c),c)=T_-(h(c),c)=h(c).
$$

### 2.2. The range $\sqrt3/2<c<1$

For every $0\le a\le1$,

$$
\boxed{
F_c(a)=
\begin{cases}
1-a,
& 0\le a\le1-c,\\
T_+(a,c),
& 1-c<a\le\ell(c),\\
\ell(c),
& \ell(c)<a<r(c),\\
T_-(a,c),
& r(c)\le a<c,\\
1-a,
& c\le a\le1.
\end{cases}
}
$$

The assignment at $a=\ell(c)$ is essential:

$$
F_c(\ell(c))=T_+(\ell(c),c)=r(c),
$$

whereas

$$
\lim_{a\mathbin{\downarrow}\ell(c)}F_c(a)=\ell(c).
$$

Thus $F_c$ has a genuine downward jump immediately to the right of
$a=\ell(c)$. At the other transition,

$$
T_-(r(c),c)=\ell(c),
$$

so the $L$ and $T_-$ pieces agree.

When $c=\sqrt3/2$, all three middle contacts meet:

$$
\ell(c)=r(c)=h(c)=\frac c2.
$$

## 3. Reduction to the exact $L$ and $T$ cells

Write

$$
b=F_c(a),
\qquad
s=a+b,
\qquad
m=\min\left\{a,b\right\},
\qquad
M=\max\left\{a,b\right\},
$$

and

$$
q=s^4-s^2+ab.
$$

The cap gives $s\le1$. Hence Cell $S$ of `2004` is absent, and the diameter
condition is automatic because

$$
a^2+ab+b^2=s^2-ab\le1.
$$

The only remaining exact cells are

$$
q\le0,
\qquad
F_L=c^4-c^2+mc-m^2\le0,
$$

and

$$
q\ge0,
\qquad
F_T=(s^2-1)c^2+Mc-M^2\le0,
\qquad
c\le2M.
$$

First suppose the cap is active, so $b=1-a$ and $s=1$. Then $q=ab\ge0$
and

$$
F_T=M(c-M).
$$

Thus the Full face is feasible exactly when

$$
c\le\max\left\{a,1-a\right\}.
$$

Because $c>1/2$, this is equivalent to

$$
a\le1-c
\qquad\text{or}\qquad
a\ge c.
$$

This proves the two Full ranges in the catalog.

Now assume

$$
1-c<a<c.
$$

The cap is not feasible. A maximizing point must therefore lie on
$F_L=0$ or $F_T=0$. Indeed, at a point strict in every radial inequality,
$b$ can be increased. The interface $q=0$ is shared by the two cells and is
not a missing frontier. Nor can $c=2M$ create an additional terminal face:
at selector equality,

$$
F_T=M^2(4s^2-3),
$$

while $q\ge0$ and $ab\le s^2/4$ imply $s\ge\sqrt3/2$. Hence $F_T\le0$ at
selector equality only when $F_T=0$ already.

## 4. The $L$ contact

The equation $F_L=0$, viewed as an equation in $m$, is

$$
m^2-cm+c^2-c^4=0.
$$

Its discriminant is

$$
c^2(4c^2-3).
$$

It therefore has no real contact when $c<\sqrt3/2$. When
$c\ge\sqrt3/2$, its roots are precisely $\ell(c)$ and $r(c)$, and

$$
F_L=-(m-\ell(c))(m-r(c)).
$$

The formal range $m\ge r(c)$ is incompatible with $q\le0$, except at the
single meeting point $c=\sqrt3/2$ and $m=M=\sqrt3/4$. Indeed,
$r(c)\ge\sqrt3/4$. At $M=m$ one has

$$
q=m^2(16m^2-3)\ge0,
$$

and for $M\ge m$ the derivative of $q$ with respect to $M$ is

$$
4(m+M)^3-2(m+M)+m
\ge32m^3-3m>0.
$$

Here the first inequality uses that $4z^3-2z$ is increasing for
$z\ge2m\ge\sqrt3/2$, and the last uses $m\ge\sqrt3/4$. Thus the selected
$L$ component has

$$
m\le\ell(c).
$$

On the radial frontier it has $m=\ell(c)$. If $a>\ell(c)$, this forces
$b=\ell(c)$. We now verify exactly that this point satisfies $q\le0$ until
$a=r(c)$. Put

$$
\theta=\frac{\ell(c)}c,
\qquad
y=\frac{a+\ell(c)}c.
$$

The root equation for $\ell(c)$ gives

$$
c^2=1-\theta+\theta^2,
$$

and $\ell(c)\le a\le r(c)$ is equivalent to
$2\theta\le y\le1$. Direct expansion factors the cell selector as

$$
\frac q{c^2}
=(y-1)J(\theta,y),
$$

where

$$
J(\theta,y)
=(1-\theta+\theta^2)(y^3+y^2)
-\theta(1-\theta)y+\theta^2.
$$

Since $1-\theta+\theta^2\ge3/4$ and $0<\theta\le1/2$,

$$
J(\theta,y)
\ge\frac34y^2-\theta y+\theta^2
=\frac34\left(y-\frac{2\theta}{3}\right)^2
+\frac{2\theta^2}{3}>0.
$$

Thus $q\le0$, with equality exactly when $y=1$, or $a=r(c)$. At that
endpoint the two subcritical cells agree and $a+b=c$. Hence, at fixed $c$,
the ordered transition pair is

$$
(a,b)=(r(c),\ell(c)).
$$

At $a=\ell(c)$, the same $L$ frontier permits $b$ to increase all the way
to the other ordered transition pair

$$
(a,b)=(\ell(c),r(c)).
$$

This proves the constant $L$ interval, the exceptional value at its left
endpoint, and the tie at its right endpoint.

## 5. The two $T$ contacts and their selectors

### 5.1. The ordered range $a\le b$

Here $M=b$, and $F_T=0$ is

$$
(c^2-1)b^2+(2ac^2+c)b+(a^2-1)c^2=0.
$$

Equivalently,

$$
(1-c^2)b^2-(2ac^2+c)b+(1-a^2)c^2=0.
$$

The discriminant is $\Delta(a,c)$, and the selected lower root is
$T_+(a,c)$. It is the root below the cap: in this ordered central range,

$$
F_T(a,0,c)<0
$$

and, at $b=1-a$,

$$
F_T=(1-a)(c-(1-a))>0.
$$

Thus the cap lies strictly between the two formal quadratic roots, so the
upper root is not selected.

The order boundary $b=a$ gives

$$
(4c^2-1)a^2+ca-c^2=0.
$$

Its positive root is exactly $a=h(c)$. The other possible endpoint is
$q=0$. As proved above, this endpoint exists only for
$c\ge\sqrt3/2$, and in the ordered half it is

$$
(a,b)=(\ell(c),r(c)).
$$

The endpoints occur after the lower Full face and before $a=c$. For
$1/2<c\le\sqrt3/2$, let

$$
K_c(z)=(4c^2-1)z^2+cz-c^2.
$$

This polynomial is strictly increasing for $z\ge0$, its positive root is
$h(c)$, and

$$
K_c(1-c)=(2c-1)^2(c^2-c-1)<0.
$$

Also $h(c)<c$ follows directly from the displayed formula for $h$. Hence

$$
1-c<h(c)<c.
$$

For $c>\sqrt3/2$, the $L$ polynomial satisfies

$$
(1-c)^2-c(1-c)+c^2-c^4
=(1-c)(c^3+c^2-2c+1)>0.
$$

The cubic has value $7/4-5\sqrt3/8>0$ at $c=\sqrt3/2$, and its derivative
$3c^2+2c-2$ is positive and increasing thereafter.
Because $1-c<c/2$, this places $1-c$ strictly to the left of the lower
root. Thus

$$
1-c<\ell(c)<r(c)<c.
$$

If $c<\sqrt3/2$, the $L$ equation has no real root, so no $q=0$ radial
frontier exists and the first endpoint is the order boundary
$a=b=h(c)$. If $c>\sqrt3/2$, the $q=0$ point has
$r(c)>\ell(c)$, so it is reached while $a<b$ and therefore strictly before
the order boundary. At $c=\sqrt3/2$ the two endpoints coincide. The
component selector is valid throughout: in the first regime the formula for
$h$ gives

$$
b\ge h(c)\ge\frac c2,
$$

where the last inequality is equivalent to $c\le\sqrt3/2$; in the second
regime $b\ge r(c)>c/2$. This proves exactly the two displayed $T_+$ ranges.

### 5.2. The ordered range $b\le a$

Here $M=a$, and $F_T=0$ becomes

$$
((a+b)^2-1)c^2+ac-a^2=0.
$$

The positive solution is

$$
b=\frac{\sqrt{a^2-ac+c^2}}c-a=T_-(a,c).
$$

The same two selectors determine its lower endpoint. When
$c\le\sqrt3/2$, it begins at $a=h(c)$, where $a=b$. When
$c>\sqrt3/2$, it begins at the other $q=0$ pair

$$
(a,b)=(r(c),\ell(c)).
$$

In both cases $c\le2a$. It ends at

$$
T_-(c,c)=1-c,
$$

which is the Full contact at $a=c$. This proves the $T_-$ ranges and
completes the catalog.

## 6. Equality faces and monotonicity

For later selector arguments, the equality values are

$$
T_+(1-c,c)=c,
\qquad
T_-(c,c)=1-c,
$$

$$
T_+(h(c),c)=T_-(h(c),c)=h(c),
$$

and, when $c>\sqrt3/2$,

$$
T_+(\ell(c),c)=r(c),
\qquad
T_-(r(c),c)=\ell(c).
$$

All radicals in these identities are nonnegative on the stated domains.
The denominator of the stable $T_+$ formula is positive, so its
rationalization does not change the selected root.

Coordinatewise down-closure of $\mathcal A$ implies that $B_c(a)$ and
$F_c(a)$ are nonincreasing in $a$. Therefore $G_c$ is nondecreasing. The cap
also gives

$$
G_c(a)\ge a.
$$

## 7. Exact capped duality

For every $a,z,c\in[0,1]$,

$$
\boxed{
G_c(a)\le z
\quad\Longleftrightarrow\quad
G_c(1-z)\le1-a.
}
$$

Indeed,

$$
G_c(a)\le z
\quad\Longleftrightarrow\quad
F_c(a)\ge1-z.
$$

By the interval-fiber property, the latter says exactly that
$(a,1-z,c)\in\mathcal A$ and $a+1-z\le1$. Reflection of the exact
admissible set changes this to $(1-z,a,c)\in\mathcal A$ with the same cap,
which is equivalent to $F_c(1-z)\ge a$ and hence to the right-hand side.

## 8. Scalar-root lemma

Put

$$
\mu=\frac{2\sqrt3-3}{4}<\frac18
$$

and, for $0<X<1-\sqrt3/2$, define

$$
e(X)=\ell(1-X).
$$

Then, for $0<X\le\mu$,

$$
\boxed{
X<e(X)<\frac{2X}{1-2X}.
}
$$

To prove this, let

$$
p_X(z)=z^2-(1-X)z+(1-X)^2-(1-X)^4.
$$

Its roots are $e(X)$ and $(1-X)-e(X)$. Since $X<1/8$, one has
$X<(1-X)/2$, and

$$
p_X(X)=X(1-3X+4X^2-X^3)>0.
$$

Therefore $X<e(X)$. For

$$
U=\frac{2X}{1-2X},
$$

the Cell-$L$ expression has the exact value

$$
(1-X)^4-(1-X)^2+(1-X)U-U^2
=
\frac{X^2P(X)}{(1-2X)^2},
$$

where

$$
P(X)=4X^4-20X^3+37X^2-28X+3.
$$

The polynomial $P$ is strictly decreasing on $[0,\mu]$. Its endpoint value
is

$$
P(\mu)=\frac{8217}{64}-74\sqrt3>0,
$$

and the last strict inequality is certified by

$$
\left(\frac{8217}{64}\right)^2-3\mathbin{\cdot}74^2
=\frac{230001}{4096}>0.
$$

For completeness, the monotonicity follows from

$$
P'(X)=16X^3-60X^2+74X-28
<\frac{16}{512}+\frac{74}{8}-28<0
$$

on $0\le X\le\mu<1/8$.

Hence the Cell-$L$ expression is positive, or equivalently
$p_X(U)<0$. Thus $U$ lies strictly between the two roots and $e(X)<U$.

Two further exact comparisons used in the CE1 estimates are

$$
e(X)\le2X+5X^2
\qquad
\left(0<X\le\frac18\right),
$$

and

$$
e(X)<2X+3X^2
\qquad
\left(0<X\le\frac1{10}\right).
$$

They follow respectively from

$$
p_X(2X+5X^2)=X^2(3X+4)(8X-1)\le0
$$

and

$$
p_X(2X+3X^2)=X^2(8X^2+19X-2)<0.
$$

For the last sign, $8X^2+19X-2$ is increasing and remains negative through
$X=1/10$. In both displays the trial point is therefore between the two
roots of the monic polynomial $p_X$.

## 9. High-demand threshold lemma

Let

$$
0<X<1-\frac{\sqrt3}{2},
\qquad
c=1-X,
\qquad
e(X)=\ell(c).
$$

Then

$$
\boxed{
a>e(X)
\quad\Longrightarrow\quad
F_{1-X}(a)\le e(X).
}
$$

Equivalently,

$$
a>e(X)
\quad\Longrightarrow\quad
G_{1-X}(a)\ge1-e(X).
$$

The proof is immediate from the selected high-$c$ catalog. On
$e(X)<a<r(1-X)$ the value is exactly $e(X)$. At and beyond
$r(1-X)$, monotonicity gives a value at most $e(X)$. The strict input
inequality is necessary, because the equality face is

$$
F_{1-X}(e(X))=r(1-X)>e(X).
$$
