# Failed Near-Tight Shortcuts

Status: Failed

This file records shortcuts that were tested for the close-to-tight finite-$x$ algorithm-1 proof and should not be reused without new hypotheses.

## False $x$-Convexity Target

A natural target was

$$
\partial_{xx}\left(L_{P_3P_5}^{+}-1-xC_1\right)\ge0.
$$

This is false. Stable numerical second differences found negative values near

$$
x\approx0.0996531090,\qquad k\approx0.7337580741,\qquad s\approx0.7573579540,\qquad \tau\approx0.7961371735.
$$

The residual is still positive there, but it is not convex in $x$.

## Componentwise Diagonal Linear Bounds

Another tempting route was to prove each diagonal radius satisfies its tangent linear lower bound, for example

$$
r_j\ge xd_j.
$$

This is false. In some finite-$x$ regions, diagonal radii fall below their tangent linear approximations. The full residual remains positive because the $P_3P_5$ side and rotated support coefficients compensate for the diagonal shortfall.

## Global Convex Programming

The finite-$x$ function is a lower envelope of pair-tie algebraic candidates, with support-regime switches. Numerical Hessian tests in the variables $(k,s,\tau)$ are indefinite. A global convex-programming proof is therefore not compatible with the observed geometry.

## Raw Interval Root Formulas

Direct interval evaluation of the selected $309$ line-circle quadratic roots over boxes in $(x,k)$ or $(x,k,s,\tau)$ gives severe dependency overestimates. On moderate boxes, the discriminant interval can cross below zero even when pointwise roots are valid. Future certificates should use implicit differentiation or Taylor models for selected roots.
