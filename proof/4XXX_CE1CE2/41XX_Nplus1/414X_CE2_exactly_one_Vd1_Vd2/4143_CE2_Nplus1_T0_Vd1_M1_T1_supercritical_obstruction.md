# CE2, $N_+=1$, $T_0$ Vd1 With $M_1\in T_0$ And $T_1$ Supercritical

Status: Proven

This file proves the normalized adjacent-rescue Vd1 subcase in
[`4140`](4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md).  The class-specific
work is now only the verification of two local Vd1 inequalities.  The center
hiding argument and the terminal boundary contradiction are supplied by the
common adjacent-rescuer theorem
[`2018`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md).

## 1. Reduced branch

Assume

$$
T_C\text{ is CE2},
\qquad
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\},
$$

$$
T_0\text{ is the unique Vd1 row},
\qquad
M_1\in T_0,
$$

$$
T_1\text{ is the unique supercritical row},
$$

and $T_2,T_3,T_4,T_5$ are nonsupercritical Vd0 rows.  We prove that the
perimeter together with $r_1$ cannot be covered.  Reflection gives the
corresponding $M_5,T_5$ placement.

## 2. Vd1 corner data

Use the corner normal form from
[`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md).
Let $a,b$ be the exact boundary reaches of $T_0$.  For a unique $t>0$, put

$$
d=\sqrt{t^2+t+1}.
$$

Then

$$
\begin{aligned}
x-(t+1)y&\le a,\\
ty-(t+1)x&\le tb,\\
tx+y&\le d-a-tb.
\end{aligned}
$$

Write

$$
T_0\cap r_1=[c,u]
$$

in the coordinate from $V_1$ toward $O$.  The exact endpoints are

$$
\boxed{
c=\frac{t(1-b)}{t+1},
\qquad
u=\frac{d-a-tb-1}{t}.
}
$$

In the preceding display, the symbol after the comma is the ordinary endpoint
$u$; equivalently the second formula is

$$
u=u=\frac{d-a-tb-1}{t}.
$$

The midpoint condition gives

$$
c\le\frac12\le u,
$$

and hence

$$
tb=t-c(t+1),
\qquad
a+tb\le d-1-\frac t2.
$$

The Vd1 hypothesis forces

$$
\boxed{t\ge1.}
$$

Indeed, if $t<1$, then the raw $r_5$ interval has positive length because

$$
d-a-tb-t
\ge
1-\frac t2
>
\frac1{t+1}
>
\frac{1-a}{t+1},
$$

contrary to one-sided adjacent support.

## 3. The two local rescuer inequalities

For $0\le c\le1/2$, put

$$
B_{\rm sc}(c)=\frac{c+\sqrt{c^2-8c+4}}2,
\qquad
A_{\rm sc}(c)=1-B_{\rm sc}(c).
$$

We prove

$$
\boxed{
a\le A_{\rm sc}(c),
\qquad
\frac{a}{a+1-u}\le A_{\rm sc}(c).
}
$$

### 3.1. Boundary reach

The endpoint inequalities give

$$
a\le d-1-\frac{3t}{2}+c(t+1)=:F(t,c).
$$

For fixed $c\le1/2$,

$$
\frac{\partial F}{\partial t}
=
\frac{2t+1}{2\sqrt{t^2+t+1}}-\frac32+c
\le
\frac{2t+1}{2\sqrt{t^2+t+1}}-1<0.
$$

Thus, for $t\ge1$,

$$
F(t,c)\le F(1,c)=\sqrt3-\frac52+2c=:L(c).
$$

Since $a\ge0$ and $a\le L(c)$, every feasible row has $L(c)\ge0$.  We claim

$$
2L(c)\le A_{\rm sc}(c).
$$

This is equivalent to

$$
\sqrt{c^2-8c+4}\le12-4\sqrt3-9c.
$$

The right side is positive on $[0,1/2]$.  After squaring, the difference of
the two sides is

$$
4Q(c),
$$

where

$$
Q(c)=20c^2+(18\sqrt3-52)c+47-24\sqrt3.
$$

On $[0,1/2]$,

$$
Q'(c)\le18\sqrt3-32<0,
$$

and

$$
Q\left(\frac12\right)=26-15\sqrt3>0.
$$

Hence $Q(c)>0$ throughout the interval and

$$
2L(c)\le A_{\rm sc}(c).
$$

Since $L(c)\ge0$,

$$
a\le L(c)\le2L(c)\le A_{\rm sc}(c).
$$

### 3.2. Hiding ratio

Put

$$
\varepsilon=1-u>0.
$$

The positivity follows because a Vd1 role containing both $V_0$ and $O$ would
have the distance-one pair $V_0,O$ as two vertices of its unit triangle, and
the third vertex would be $V_1$ or $V_5$, contradicting the Vd1 type.

Using the third side and $tb=t-c(t+1)$,

$$
\varepsilon
=
\frac{2t+1+a-c(t+1)-d}{t}
=
\varepsilon_0+\frac at,
$$

where

$$
\varepsilon_0
=
\frac{2t+1-c(t+1)-d}{t}>0.
$$

Indeed, $c\le1/2$ gives

$$
2t+1-c(t+1)-d
\ge
\frac{3t+1}{2}-d>0
$$

for $t\ge1$.  The function

$$
z\longmapsto
\frac{z}{z+\varepsilon_0+z/t}
$$

is increasing for $z\ge0$.  Since $a\le F(t,c)$ and

$$
\varepsilon_0+\frac{F(t,c)}t=\frac12,
$$

we obtain

$$
\frac{a}{a+\varepsilon}
\le
\frac{F(t,c)}{F(t,c)+1/2}
\le
\frac{L(c)}{L(c)+1/2}
\le
2L(c)
\le
A_{\rm sc}(c).
$$

Thus

$$
\boxed{
\frac{a}{a+1-u}\le A_{\rm sc}(c).
}
$$

## 4. Invocation of the common adjacent-rescuer theorem

The interval $[c,u]$ contains $M_1$, so $u\ge1/2$.  The supercritical row
$T_1$ misses $M_1$ and, since it contains $V_1$, cannot cover any point of
$r_1$ on the $O$-side of $M_1$.  The rows $T_2,T_3,T_4,T_5$ are Vd0 and
have no positive-length adjacent support on $r_1$.  Hence radial coverage
forces the center role to cover the $O$-side gap of length $1-u$ before the
Vd1 interval begins.

The two boxed inequalities of Section 3 are exactly the remaining local
hypotheses of the common adjacent-rescuer theorem `2018`.  That theorem gives
a far-side boundary demand at least $B_{\rm sc}(c)$, while the strict
supercritical envelope gives the outgoing reach of $T_1$ strictly below
$B_{\rm sc}(c)$.  Its boundary-path budget then contradicts the four
nonsupercritical row caps of $T_2,T_3,T_4,T_5$.

Therefore the normalized Vd1 adjacent-rescue placement is impossible.
Reflection proves the $M_5,T_5$ placement.

$$
\Box
$$
