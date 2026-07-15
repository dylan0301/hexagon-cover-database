# High-Radial Low-Root Bounds

Status: Proven

This note isolates the scalar consequences of the exact capped demand map in
[`2011_capped_demand_map.md`](2011_capped_demand_map.md) used by the CE1 and
CE2 five-map arguments.

Put

$$
\mu=\frac{2\sqrt3-3}{4}<\frac18
$$

and, for $0<X<1-\sqrt3/2$, define the low Cell-$L$ root

$$
e(X)=\ell(1-X).
$$

## Root bounds

For $0<X\le\mu$,

$$
\boxed{
X<e(X)<\frac{2X}{1-2X}.
}
$$

Let

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

The polynomial $P$ is strictly decreasing on $[0,\mu]$. Indeed,

$$
P'(X)=16X^3-60X^2+74X-28
<\frac{16}{512}+\frac{74}{8}-28<0.
$$

At the right endpoint,

$$
P(\mu)=\frac{8217}{64}-74\sqrt3>0,
$$

because

$$
\left(\frac{8217}{64}\right)^2-3\mathbin{\cdot}74^2
=\frac{230001}{4096}>0.
$$

Hence the Cell-$L$ expression is positive, or equivalently $p_X(U)<0$.
Thus $U$ lies strictly between the two roots and $e(X)<U$.

Two further exact comparisons are

$$
\boxed{
e(X)\le2X+5X^2
\qquad
\left(0<X\le\frac18\right),
}
$$

and

$$
\boxed{
e(X)<2X+3X^2
\qquad
\left(0<X\le\frac1{10}\right).
}
$$

They follow from

$$
p_X(2X+5X^2)=X^2(3X+4)(8X-1)\le0
$$

and

$$
p_X(2X+3X^2)=X^2(8X^2+19X-2)<0.
$$

For the last sign, $8X^2+19X-2$ is increasing and remains negative through
$X=1/10$. In both displays the trial point lies between the two roots of the
monic polynomial $p_X$.

## High-demand threshold

For

$$
0<X<1-\frac{\sqrt3}{2},
$$

one has

$$
\boxed{
a>e(X)
\quad\Longrightarrow\quad
F_{1-X}(a)\le e(X),
}
$$

or equivalently

$$
\boxed{
a>e(X)
\quad\Longrightarrow\quad
G_{1-X}(a)\ge1-e(X).
}
$$

Indeed, the selected high-radial catalog in `2011` gives
$F_{1-X}(a)=e(X)$ when

$$
e(X)<a<1-X-e(X).
$$

At and beyond the right endpoint, monotonicity gives a value at most $e(X)$.
The strict input inequality is necessary because

$$
F_{1-X}(e(X))=1-X-e(X)>e(X).
$$
