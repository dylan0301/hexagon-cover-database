# Core Surface Definition

Status: Definition

This file defines the three-dimensional surface displayed in the `Core f(a,b)`
mode.  The displayed quantity is a minimal enclosing equilateral-triangle side
length.  It is not the area function $f(a,b)$ used in the CE0 area-certificate
package.

## Enclosing side length

For a finite nonempty set $K\subset\mathbb R^2$, define

$$
\Lambda(K)=
\inf_{\theta\in[0,2\pi/3)}
\frac{2}{\sqrt3}
\sum_{r=0}^2
\max_{P\in K} n_r(\theta)\cdot P,
$$

where

$$
n_r(\theta)=
\left(\cos\left(\theta+\frac{2\pi r}{3}\right),
\sin\left(\theta+\frac{2\pi r}{3}\right)\right).
$$

This is the side length of the smallest closed equilateral triangle containing
$K$.

## Six-point surface

Let $K_6(a,b)$ be the six-point set defined in
[`31011_six_point_construction.md`](31011_six_point_construction.md), using
the two-line $AB$-superset point definitions for $P_3,P_4,P_5$.  The ideal
six-point core surface is

$$
F_6(a,b)=\Lambda(K_6(a,b)),
\qquad (a,b)\in\mathcal D,
$$

where $\mathcal D$ is the two-variable graph domain defined in
[`31012_core_graph_two_variable_relaxation.md`](31012_core_graph_two_variable_relaxation.md).

If one of the enabled points is missing, the value is unavailable for that
sample.

## Selected-point surfaces

The visual mode allows toggling points on or off.  For a nonempty selected set

$$
E\subseteq\left\{P_3,P_4,P_5,D_0,D_1,D_2\right\},
$$

let $K_E(a,b)$ be the corresponding subset of present points.  The selected
surface is

$$
F_E(a,b)=\Lambda(K_E(a,b)).
$$

If $E$ is empty, the side length is unavailable.  If any enabled point in $E$
is missing at a sample, the side length for that sample is unavailable.

## Rendered graph

The mathematical surface is the set

$$
\left\{(a,b,F_E(a,b)):(a,b)\in\mathcal D, F_E(a,b)\text{ is available}\right\}.
$$

The app renders a sampled and normalized mesh.  On the sampled grid, let

$$
F_{\min}=\min F_E(a,b),\qquad F_{\max}=\max F_E(a,b),
$$

where the minimum and maximum range over available sampled values.  The
displayed vertical coordinate is

$$
z=\frac{F_E(a,b)-F_{\min}}{F_{\max}-F_{\min}} H_{\mathrm{surf}},
$$

with the app constant $H_{\mathrm{surf}}=1.35$.  This normalization affects
only the drawing; the reported value is the unnormalized side length
$F_E(a,b)$.

## Status warning

The notation `Core f(a,b)` in the visual app is only a UI label.  In this
package, the side-length surface is denoted $F_6$ or $F_E$ to avoid confusion
with the area function $f(a,b)$ from the CE0 area-conjecture package.
