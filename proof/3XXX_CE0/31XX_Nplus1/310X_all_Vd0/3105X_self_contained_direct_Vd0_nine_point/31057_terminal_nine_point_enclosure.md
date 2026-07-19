# Terminal Nine-Point Enclosure Theorem

Status: Proven

## Theorem

Assume

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1.
\tag{1}
$$

Put

$$
p=1-b,
\qquad
q=1-a,
\qquad
c_*=c_{\max}(p,q),
\qquad
h=\frac{\sqrt3}{2},
$$

$$
\eta=h(1-c_*),
\qquad
\mathcal D_\eta
=
\left\{X:\left\lVert X\right\rVert\le\eta\right\}.
$$

Let $Q_-(a,b),Q_0(a,b),Q_+(a,b)$ be the exact asymmetric witnesses defined
in
[`31053_direct_asymmetric_witness_forcing.md`](31053_direct_asymmetric_witness_forcing.md),
and set

$$
K_{\mathrm{wit}}(a,b)
=
\mathcal D_\eta
\mathbin\cup
\left\{Q_-(a,b),Q_0(a,b),Q_+(a,b)\right\}.
\tag{2}
$$

Then

$$
\boxed{
\Lambda\left(K_{\mathrm{wit}}(a,b)\right)\ge1,
}
\tag{3}
$$

where $\Lambda(K)$ is the least side length of a closed equilateral triangle
containing the compact set $K$.

## Proof

The support formula proved in
[`31054_four_cap_enclosure_reduction.md`](31054_four_cap_enclosure_reduction.md)
is

$$
\Lambda(K)
=
\frac1h
\min_{\left\lVert n\right\rVert=1}
\sum_{j=0}^2h_K(R^j n),
\tag{4}
$$

where $R$ is rotation through $2\pi/3$.  The disk in (2) gives

$$
\Lambda(K_{\mathrm{wit}})
\ge3(1-c_*).
$$

Thus (3) is immediate when $c_*\le2/3$.

Assume $c_*>2/3$.  The Newton construction in `31054` gives points

$$
A\in(Q_0,Q_-),
\qquad
B=Q_0,
\qquad
C\in(Q_0,Q_+),
$$

and the inner compact convex set

$$
\widehat K
=
\mathrm{conv}
\left(
\mathcal D_\eta\mathbin\cup\{A,B,C\}
\right)
\subseteq
\mathrm{conv}(K_{\mathrm{wit}}).
\tag{5}
$$

Consequently

$$
\Lambda(K_{\mathrm{wit}})\ge\Lambda(\widehat K).
\tag{6}
$$

For

$$
S=\widehat K+R\widehat K+R^2\widehat K,
\qquad
W=C+RA,
$$

the same note proves that $S$ contains the full rotational orbits of

$$
\mathbb D(A,2\eta),
\quad
\mathbb D(B,2\eta),
\quad
\mathbb D(C,2\eta),
\quad
\mathbb D(W,\eta).
\tag{7}
$$

It also proves that the rays

$$
A, B, C, W, RA
$$

occur in this cyclic order, that the necessary determinants are positive,
that $\left\lVert A\right\rVert,\left\lVert C\right\rVert>\eta$, and that
the first two consecutive cap overlaps hold:

$$
I(A,2\eta)
\longleftrightarrow
I(B,2\eta)
\longleftrightarrow
I(C,2\eta).
\tag{8}
$$

It remains to prove the mixed overlaps ending the chain.

By
[`31055_rational_radial_envelopes_and_mixed_reduction.md`](31055_rational_radial_envelopes_and_mixed_reduction.md),
the active radial cell has a rational upper envelope $\bar c$ satisfying

$$
c_*\le\bar c<1.
$$

Hence

$$
0<\bar\eta=h(1-\bar c)\le\eta,
$$

and the three relevant disks in (7) contain

$$
\mathbb D(C,2\bar\eta),
\qquad
\mathbb D(W,\bar\eta),
\qquad
\mathbb D(RA,2\bar\eta).
\tag{9}
$$

The exact Gram calculation in `31055` reduces the two smaller-disk mixed
residuals to

$$
Q_A\ge0,
\qquad
Q_C\ge0,
$$

and then to eight integer-polynomial signs with strictly positive omitted
denominators.  The three-chart theorem
[`31056_global_analytic_mixed_positivity.md`](31056_global_analytic_mixed_positivity.md)
proves all eight signs by twenty global Bernstein identities.  Therefore the
two smaller-disk caps overlap:

$$
I(C,2\bar\eta)
\longleftrightarrow
I(W,\bar\eta)
\longleftrightarrow
I(RA,2\bar\eta).
\tag{10}
$$

Increasing the radii from $\bar\eta$ to $\eta$ only enlarges the caps, so
(10) proves

$$
I(C,2\eta)
\longleftrightarrow
I(W,\eta)
\longleftrightarrow
I(RA,2\eta).
\tag{11}
$$

Equations (8) and (11) give four consecutive overlaps from the ray of $A$ to
the ray of $RA$.  The cap-order argument in `31054` shows that these caps
cover that sector.  Rotating by $R$ covers the unit circle.  Thus
$h_S(n)\ge h$ for every unit normal $n$, and (4) gives

$$
\Lambda(\widehat K)\ge1.
$$

Equation (6) proves (3). $\square$

## Certificate character

The two adjacent overlaps are proved by explicit analytic inequalities.  The
mixed overlaps use rational upper envelopes, exact symbolic elimination, and
twenty global positive-basis identities on three fixed charts.  No interval
arithmetic, adaptive subdivision, pruning, or branch-and-bound enters the
proof.
