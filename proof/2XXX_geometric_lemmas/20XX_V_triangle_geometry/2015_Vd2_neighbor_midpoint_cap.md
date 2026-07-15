# Vd2 Neighbor-Midpoint Boundary Cap

Status: Proven

Use the local coordinates and exact incident-edge reaches $a,b$ from
[`2014_Vd1_Vd2_corner_normal_form.md`](2014_Vd1_Vd2_corner_normal_form.md).

## Theorem

If an original Vd2 role contains either neighboring midpoint, then

$$
\boxed{a+b<\frac13.}
$$

This is stronger than the boundary-loss threshold

$$
\frac13<\frac32-\frac2{\sqrt3}.
$$

Indeed, the last inequality is equivalent to $12<7\sqrt3$, whose square is
$144<147$.

## Proof

The normal form in `2014` gives $t>0$ and

$$
d=\sqrt{t^2+t+1},
\qquad
U=a+tb.
$$

Reflection in $x=y$ replaces $t$ by $1/t$ and swaps $a,b$ and $M_1,M_5$.
Thus we may assume only that

$$
t\ge1.
$$

The contained neighboring midpoint may then be either $M_1$ or $M_5$; these
two possibilities must be treated separately.

### The contained midpoint is $M_5$

Substitution of

$$
M_5=\left(1,\frac12\right)
$$

into the third half-plane gives

$$
U\le d-t-\frac12.
$$

Since $t\ge1$,

$$
a+b\le U\le d-t-\frac12.
$$

The last expression is decreasing because

$$
\frac{2t+1}{2d}<1.
$$

Consequently

$$
a+b\le\sqrt3-\frac32<\frac13.
$$

The final inequality follows from $6\sqrt3<11$, whose square is $108<121$.

### The contained midpoint is $M_1$

Substitution of

$$
M_1=\left(\frac12,1\right)
$$

into the second and third half-planes gives

$$
b\ge L(t):=\frac{t-1}{2t},
$$

and

$$
U\le d-1-\frac t2.
$$

Therefore

$$
a+b=U-(t-1)b
\le d-t-\frac1{2t}=:S(t).
$$

The function $S$ is increasing on $[1,\infty)$. Indeed,

$$
S'(t)=\frac{2t+1}{2d}-1+\frac1{2t^2},
$$

and $S'(t)>0$ is equivalent, after squaring positive sides, to

$$
(2t+1)^2t^4>(t^2+t+1)(2t^2-1)^2.
$$

The difference is

$$
(t+1)(t^3+3t^2-1)>0.
$$

We also use the second adjacent arm. Since a Vd2 role has positive-length
intersection with $r_5$, the raw endpoints from `2014` satisfy

$$
d-U-t>\frac{1-a}{t+1}.
$$

After substituting $a=U-tb$, this becomes

$$
U+b<\frac{(t+1)(d-t)-1}{t}.
$$

Using $b\ge L(t)$,

$$
a+b=U+b-tb<R(t),
$$

where

$$
R(t):=\frac{2(t+1)d-3t^2-t-2}{2t}.
$$

The function $R$ is decreasing on $[1,\infty)$. Its derivative has the sign
of

$$
2t^3+t^2-t-2+(2-3t^2)d.
$$

For $t\ge1$, the coefficient $2-3t^2$ is negative and

$$
d>t+\frac12.
$$

Hence the displayed numerator is strictly less than

$$
-t^3-\frac12t^2+t-1<0.
$$

Now split at $t=4/3$. If $1\le t\le4/3$, then

$$
a+b\le S(t)\le S\left(\frac43\right)
=\frac{8\sqrt{37}-41}{24}<\frac13,
$$

because $8\sqrt{37}<49$, as $64\mathbin{\cdot}37=2368<2401=49^2$.

If $t\ge4/3$, then

$$
a+b<R(t)\le R\left(\frac43\right)
=\frac{7\sqrt{37}-39}{12}<\frac13,
$$

because $7\sqrt{37}<43$, as $49\mathbin{\cdot}37=1813<1849=43^2$.

Both possible neighboring midpoints have now been treated, so the theorem
follows.

$$
\Box
$$
