# Final $P_{\mathrm{res}}$ Two-Variable Target

Status: Lemma target

This file records the final reduced close-to-tight target after the diagonal remainder estimates in [`3122_diagonal_remainder_progress.md`](3122_diagonal_remainder_progress.md).

## Statement

The remaining target is

$$
P_{\mathrm{res}}(x,k)\ge(2+k)x^2.
$$

Equivalently, with

$$
a=1-x,\qquad b=(1+k)x,
$$

it is

$$
P(a,b)\ge a^2-ab+\frac32b.
$$

Here

$$
P(a,b)=\frac{\Delta u(1-v)+\Delta v(1-u)}{\sqrt{\Delta u^2+\Delta u\Delta v+\Delta v^2}},
$$

where

$$
P_3=(u,v),\qquad P_5=(s,t),
$$

and

$$
\Delta u=s-u,\qquad \Delta v=v-t.
$$

The domain is

$$
0<x\le0.1,\qquad 0\le k\le k_{\max}(x),
$$

where

$$
k_{\max}(x)=\frac{-(1+x)+\sqrt{1+6x-3x^2}}{2x}.
$$

Equivalently,

$$
0.9\le a<1,\qquad 1-a\le b,\qquad a^2+ab+b^2\le1.
$$

## Scaled Margin

Define

$$
M(x,k)=\frac{P_{\mathrm{res}}(x,k)-(2+k)x^2}{x^2}.
$$

The target is

$$
M(x,k)\ge0.
$$

## Proven Boundary And Limit Pieces

As $x\to0$,

$$
M(x,k)\to M_0(k)=\frac{7k^2-10k+7}{8}.
$$

The minimum of $M_0$ is

$$
\frac37.
$$

At $k=0$, the selected roots simplify and one has the stronger boundary inequality

$$
P_{\mathrm{res}}(x,0)\ge\frac{11}{5}x^2
$$

for

$$
0\le x\le\frac1{10}.
$$

On the upper validity boundary

$$
a^2+ab+b^2=1,
$$

the margin simplifies to

$$
M(x,k)=\frac{k^2+k-1}{2}.
$$

In the near-tight strip, this boundary occurs only for $k\ge k_{\max}(0.1)$, and the displayed expression is positive there.

## Numerical Interior Structure

Numerical experiments show that $M$ is minimized near

$$
x=0.1,\qquad k\approx0.5587569262,
$$

where

$$
M\approx0.1490310954.
$$

The most promising proof target is the monotonicity

$$
\partial_xM(x,k)\le0.
$$

If this monotonicity is proved, then the target follows from the safe boundary $x=0.1$ and the safe upper boundary $a^2+ab+b^2=1$.

## Root-Bound Alternative

A second possible route is to bound the selected line parameters $\lambda,\mu$ on the two line pieces by simple upper bounds of the form

$$
\lambda\le\frac2{\sqrt3}-x\left(\frac52-\frac65k\right),
$$

and

$$
\mu\le\frac2{\sqrt3}-x\left(\frac52-\frac{19}{10}k\right).
$$

Numerically, the side contribution $P$ decreases in both selected parameters on the relevant root region. If the root bounds and this monotonicity are certified, the final inequality becomes root-free.

## Current Status

This target remains open. Direct interval arithmetic with the explicit quadratic root formulas overestimates the selected-root discriminants. A successful proof likely needs implicit differentiation or Taylor models for the selected $P_3,P_5$ roots.
