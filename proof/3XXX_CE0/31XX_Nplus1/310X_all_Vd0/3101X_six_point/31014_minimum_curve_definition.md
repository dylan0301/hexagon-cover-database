# Minimum Curve Definition

Status: Definition

This file defines the minimum curve drawn in the `Core f(a,b)` visualization.
It distinguishes the ideal mathematical minimizer relation from the sampled
pink curve drawn by the app.

## Ideal minimum relation

Let $E$ be a nonempty selected subset of

$$
\left\{P_3,P_4,P_5,D_0,D_1,D_2\right\}.
$$

Let $F_E(a,b)$ be the selected-point side-length surface from
[`31013_core_surface_definition.md`](31013_core_surface_definition.md).  For
each $a$, define the vertical domain slice

$$
\mathcal D_a=\left\{b:(a,b)\in\mathcal D\right\}.
$$

When $F_E$ is available somewhere on this slice, define

$$
\mu_E(a)=\inf_{b\in\mathcal D_a} F_E(a,b).
$$

The ideal minimum relation is

$$
\mathcal M_E=
\left\{(a,b)\in\mathcal D:F_E(a,b)=\mu_E(a)\right\}.
$$

For the default all-six graph, write $\mathcal M_6$ for the relation obtained
from $E=\left\{P_3,P_4,P_5,D_0,D_1,D_2\right\}$.

## Sampled app curve

The app draws a sampled approximation to the vertical minimum relation.  It
does not certify the exact set $\mathcal M_E$.

For sample rate `high`, `medium`, or `low`, the app uses

$$
(N_a,N_s,N_{\partial})=(128,96,64),\quad (64,48,32),\quad (32,24,16),
$$

respectively.  The default sample rate is `low`.

The $a$ samples are cosine-spaced:

$$
a_i=\frac12-\frac12\cos\left(\frac{\pi i}{N_a}\right),
\qquad 0\le i\le N_a.
$$

The vertical parameter samples start with

$$
s_j=\frac12-\frac12\cos\left(\frac{\pi j}{N_s}\right),
\qquad 0\le j\le N_s.
$$

They are enriched near the lower and upper graph-domain boundaries by adding

$$
t_k=0.12\left(\frac{k}{N_{\partial}}\right)^2,\qquad
1-t_k,\qquad 1\le k\le N_{\partial},
$$

then sorting and removing duplicates.

For a fixed sampled value $a_i$, define

$$
b_{\mathrm{low}}=1-a_i+10^{-5},
$$

and

$$
b_{\mathrm{high}}=\frac{-a_i+\sqrt{4-3a_i^2}}{2}.
$$

For each sampled $s$, the sampled $b$ value is

$$
b=b_{\mathrm{low}}+(b_{\mathrm{high}}-b_{\mathrm{low}})s.
$$

The app evaluates $F_E(a_i,b)$ at these sampled points.  It then searches only
interior $s$ samples and selects a sampled point whose side length is no larger
than the immediately previous and next sampled values in the $s$ direction. If
more than one such local sampled minimum exists for that $a_i$, the app keeps
the one with the smallest side length.  If no such point exists, that $a_i$
contributes no point to the drawn curve.

Adjacent nonmissing sampled curve points are connected by straight segments.
The app draws this sampled curve in pink.

## Status warning

The sampled minimum curve is empirical visualization data.  It should not be
used as a proof that the exact function $F_E$ has a unique minimizer, that the
displayed curve is continuous, or that the displayed curve gives a rigorous
global minimum.
