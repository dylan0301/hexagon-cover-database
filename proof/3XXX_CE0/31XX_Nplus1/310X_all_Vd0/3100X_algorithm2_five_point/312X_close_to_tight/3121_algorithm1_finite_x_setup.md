# Algorithm-1 Finite-$x$ Setup Near The Vertex Limit

Status: Lemma target

This file states the finite-$x$ close-to-tight target for the CE0, $N_+=1$, all-Vd0 branch. The tangent inequality is proved in [`3125_algorithm1_limit_tangent_gap.md`](3125_algorithm1_limit_tangent_gap.md), but the finite-$x$ remainder estimate is not yet proved.

## Near-Limit Scaling

Near the lower vertex-limit corner, write

$$
a_4=(1+k)x,\qquad b_4=1-x.
$$

The valid domain is

$$
0<x\le0.1,\qquad 0\le k\le k_{\max}(x),
$$

where

$$
k_{\max}(x)=\frac{-(1+x)+\sqrt{1+6x-3x^2}}{2x}.
$$

The remaining variables are encoded by

$$
0\le s\le\tau\le1.
$$

## Tangent Coefficient

The tangent coefficient is

$$
C_1(k,s,\tau)=\max(d_0,d_1)+d_2-\frac{3-k}{2},
$$

where

$$
d_0=\max\left(\frac12,1-k+k\tau\right),
$$

$$
d_1=\max\left(\frac{1+k-k\tau}{2},1+k-2k\tau+ks\right),
$$

and

$$
d_2=\max\left(\frac{1+k-ks}{2},1+k-2ks\right).
$$

The proved tangent result is

$$
C_1(k,s,\tau)\ge\frac14.
$$

## Finite-$x$ Target

The desired close-to-tight finite-$x$ inequality is

$$
f_{\mathrm{algo1}}(x,k,s,\tau)\ge1+xC_1(k,s,\tau).
$$

This target remains open.

## Dominant Branch Decomposition

Numerical experiments show that the dominant support branch is the $P_3P_5$ side, with the two rotated sides supported by $D_2$ and whichever of $D_0,D_1$ is more exposed.

For this branch, write the residual as

$$
R_+=L_+-1-xC_1.
$$

The working decomposition is

$$
R_+\ge P_{\mathrm{res}}+E_{01}+E_2.
$$

Here

$$
P_{\mathrm{res}}=P-\left(1-\frac{3-k}{2}x\right),
$$

where $P$ is the normalized $P_3P_5$-side contribution,

$$
E_{01}=\begin{cases}c_0r_0-xd_0,& d_0\ge d_1,\\ c_1r_1-xd_1,& d_1>d_0,\end{cases}
$$

and

$$
E_2=c_2r_2-xd_2.
$$

The current proof route uses the working bounds

$$
E_{01}\ge-2x^2,
$$

and

$$
E_2\ge-kx^2,
$$

which reduce the dominant-branch target to

$$
P_{\mathrm{res}}\ge(2+k)x^2.
$$

The diagonal remainder bounds are recorded in [`3122_diagonal_remainder_progress.md`](3122_diagonal_remainder_progress.md). The final two-variable target is recorded in [`3123_pres_final_two_variable_target.md`](3123_pres_final_two_variable_target.md).
