# High-Radial Low-Root Bounds

Status: Proven

This note isolates the scalar consequences of the exact capped demand map in
[`2011_capped_demand_map.md`](2011_capped_demand_map.md) used by the CE1 and
CE2 five-map arguments.  It also records the rational half-edge radial
envelope used by the adjacent complementary CE2 placement.

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

## Half-edge rational radial envelope

Let

$$
c_{\max}(a,b)=\max\{c\in[0,1]:(a,b,c)\in\mathcal A\}
$$

be the exact radial envelope from
[`2004_admissible_set.md`](2004_admissible_set.md).

### Theorem

Suppose

$$
\frac12\le p<1,
\qquad
0\le h\le p,
\qquad
p+h<1.
$$

Then

$$
\boxed{c_{\max}(p,h)\le1-\frac h3.}
$$

The inequality is strict when the selected admissible-set component is Cell
$T$.

### Proof

Put

$$
s=p+h,
\qquad
d=p^2+ph+h^2,
\qquad
q=s^4-s^2+ph.
$$

Because $s<1$,

$$
d=s^2-ph<1.
$$

Only the two nonsupercritical cells of `2004` can occur.  Since $p\ge h$, in
Cell $L$, where $q\le0$, the selected radial value is the unique root
$C_L(h)\in[\sqrt3/2,1]$ of

$$
P_h(c):=c^4-c^2+hc-h^2=0.
$$

The convention is $C_L(0)=1$.  In Cell $T$, where $q>0$, the selector
$c\le2p$ keeps the smaller geometric root

$$
C_T(p,h)=\frac{2p}{1+\sqrt{4s^2-3}}.
$$

On $q=0$ the two formulas agree.

First consider Cell $L$.  If $h=0$, then $C_L(0)=1$.  Assume $h>0$.  We claim
that Cell $L$ forces $h<3/8$.  Otherwise $p\ge1/2$, $h\ge3/8$, and
$s\ge7/8$.  On this region,

$$
\frac{\partial q}{\partial p}=4s^3-2s+h
\ge
4\left(\frac78\right)^3
-2\left(\frac78\right)
+\frac38
=\frac{167}{128}>0.
$$

Consequently $q(p,h)\ge q(1/2,h)$.  Moreover

$$
\frac{d}{dh}q\left(\frac12,h\right)
=h(4h^2+6h+1)>0,
$$

and hence

$$
q(p,h)
\ge q\left(\frac12,\frac38\right)
=\frac{33}{4096}>0,
$$

contrary to the Cell-$L$ condition.

Set

$$
c_0=1-\frac h3.
$$

Direct substitution gives

$$
P_h(c_0)
=
\frac h{81}\left(h^3-12h^2-63h+27\right).
$$

The cubic in parentheses is decreasing on $[0,3/8]$, because its derivative
is $3h^2-24h-63<0$, and its value at $3/8$ is $891/512>0$.  Thus
$P_h(c_0)>0$.  Also $c_0>7/8>\sqrt3/2$, and

$$
P_h'(c)=c(4c^2-2)+h>0
\qquad(c\ge\sqrt3/2).
$$

The selected root therefore satisfies $C_L(h)<c_0$.  Together with the case
$h=0$, this proves the Cell-$L$ inequality.

Now assume Cell $T$.  Since $ph\le s^2/4$, the inequality $q>0$ implies
$s^2>3/4$, so

$$
r=\sqrt{4s^2-3}
$$

is real and positive.  Put

$$
\delta=\frac{p-h}{s}.
$$

The exact identity

$$
\frac q{s^2}=\frac{r^2-\delta^2}{4}
$$

shows that $0\le\delta<r$.  Write

$$
\delta=wr,
\qquad
0\le w<1.
$$

Then

$$
p=\frac{s(1+wr)}2,
\qquad
h=\frac{s(1-wr)}2,
$$

and

$$
C_T(p,h)=\frac{s(1+wr)}{1+r}.
$$

For fixed $s,r$, define

$$
\Psi(w)=C_T(p,h)+\frac h3.
$$

A direct differentiation gives

$$
\Psi'(w)=\frac{sr(5-r)}{6(1+r)}>0.
$$

Therefore

$$
\Psi(w)<\Psi(1)=\frac{s(7-r)}6.
$$

The hypothesis $p\ge1/2$ gives

$$
s(1+wr)=2p\ge1,
$$

and therefore $s(1+r)\ge1$.  This forces $r>1/8$.  Indeed, if $r\le1/8$,
then, using $s^2=(r^2+3)/4$,

$$
4s^2(1+r)^2
=(r^2+3)(1+r)^2
\le\frac{193}{64}\frac{81}{64}
=\frac{15633}{4096}<4,
$$

contradicting $s(1+r)\ge1$.

Finally,

$$
144-(r^2+3)(7-r)^2
=(1-r)(r^3-13r^2+39r-3).
$$

On $[1/8,1]$, the cubic factor is increasing because its derivative
$3r^2-26r+39$ is at least $16$, and its value at $1/8$ is $857/512>0$.
Since $1/8<r<1$, the displayed difference is positive.  Both sides being
positive, we obtain

$$
\frac{s(7-r)}6<1.
$$

Thus

$$
C_T(p,h)+\frac h3<1,
$$

which is the strict Cell-$T$ estimate.  This proves the theorem.

## Exact failure outside the half-edge domain

The lower bound $p\ge1/2$ is essential.  Take

$$
p=h=\frac25.
$$

Then

$$
d=\frac{12}{25}<1,
\qquad
s=\frac45<1,
\qquad
q=-\frac{44}{625}<0,
$$

so the selected component is Cell $L$.  At

$$
c_0=1-\frac{(2/5)}3=\frac{13}{15},
$$

one has

$$
P_{2/5}\left(\frac{13}{15}\right)
=-\frac{14}{50625}<0.
$$

Moreover $13/15>\sqrt3/2$ because $676>675$, and $P_{2/5}$ is strictly
increasing on $[\sqrt3/2,1]$.  Since

$$
P_{2/5}(1)=\frac6{25}>0,
$$

the selected Cell-$L$ root lies strictly above $13/15$.  Hence

$$
\boxed{
c_{\max}\left(\frac25,\frac25\right)
>\frac{13}{15}.
}
$$

This is an exact counterexample, not numerical evidence.

## Scope of the rational envelope

The theorem applies to the adjacent complementary placement in
[`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](../../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md),
where

$$
p=\frac12+A,
\qquad
h=H,
\qquad
0\le H\le\frac12+A,
\qquad
\frac12+A+H<1.
$$

It gives exactly

$$
c_{\max}\left(\frac12+A,H\right)\le1-\frac H3.
$$

The implication is only the necessary one

$$
(p,h,c)\in\mathcal A
\quad\Longrightarrow\quad
c\le c_{\max}(p,h)\le1-\frac h3.
$$

No converse, equality, realizability, contact type, or selected component is
asserted.  The counterexample above prevents substituting this same envelope
on the full nonsupercritical fibers underlying $B_c$, $F_c$, and $G_c$.
Accordingly, no relaxed $\bar F_c$ or $\bar G_c$ map is defined here, and no
strict-supercritical nonattainment argument is replaced.
