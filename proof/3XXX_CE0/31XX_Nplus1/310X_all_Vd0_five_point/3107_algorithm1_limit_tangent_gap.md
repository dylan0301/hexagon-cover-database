# Algorithm-1 Tangent Gap Near The Vertex Limit

Status: Proven analytic inequality

This file records the tangent-cone inequality used for the near-limit part of the all-Vd0 strategy. It does not prove a finite-$x$ remainder estimate.

## Lower Limit Scaling

Near the lower vertex-limit corner, write

$$
a_4=(1+k)x,\qquad b_4=1-x,
$$

with

$$
0\le k\le1,\qquad x\downarrow0.
$$

The remaining free variables in the CE0 all-Vd0 triangle are encoded by parameters $s,\tau$ satisfying

$$
0\le s\le\tau\le1.
$$

In algorithm 1, the three diagonal radii have the first-order form

$$
D_j=\rho_jV_j,\qquad \rho_j=xd_j+O(x^2).
$$

The coefficient functions are

$$
d_0=\max\left(\frac12,\ 1-k+k\tau\right),
$$

$$
d_1=\max\left(\frac{1+k-k\tau}{2},\ 1+k-2k\tau+ks\right),
$$

and

$$
d_2=\max\left(\frac{1+k-ks}{2},\ 1+k-2ks\right).
$$

The limiting support branch has first-order coefficient

$$
C_1(k,s,\tau)=\max(d_0,d_1)+d_2-\frac{3-k}{2}.
$$

## Inequality

For all

$$
0\le k\le1,\qquad 0\le s\le\tau\le1,
$$

one has

$$
C_1(k,s,\tau)\ge\frac14.
$$

## Proof

It is enough to prove

$$
\max(d_0,d_1)+d_2\ge\frac{7-2k}{4}.
$$

First suppose $k\le1/2$. Then

$$
d_0=1-k+k\tau
$$

and

$$
d_2=1+k-2ks.
$$

Therefore

$$
\max(d_0,d_1)+d_2\ge d_0+d_2=2+k(\tau-2s)\ge2-ks\ge2-k.
$$

Since

$$
2-k-\frac{7-2k}{4}=\frac{1-2k}{4}\ge0,
$$

the desired inequality follows.

Now suppose $k\ge1/2$.

If $ks\ge1/2$, then

$$
d_2\ge\frac{1+k-ks}{2}
$$

and

$$
d_0\ge1-k+k\tau\ge1-k+ks.
$$

Thus

$$
\max(d_0,d_1)+d_2\ge1-k+ks+\frac{1+k-ks}{2}=\frac{3-k+ks}{2}.
$$

Since $ks\ge1/2$,

$$
\frac{3-k+ks}{2}\ge\frac{7-2k}{4}.
$$

If $ks\le1/2$, then

$$
d_2=1+k-2ks.
$$

Hence

$$
\max(d_0,d_1)+d_2\ge d_0+d_2\ge2+k(\tau-2s)\ge2-ks\ge\frac32.
$$

Since $k\ge1/2$,

$$
\frac{7-2k}{4}\le\frac32.
$$

Thus the inequality holds in all cases.

## Consequence

Assuming the first-order expansion

$$
f_{\mathrm{algo1}}=1+xC_1(k,s,\tau)+O(x^2),
$$

we obtain

$$
\liminf_{x\to0^+}\frac{f_{\mathrm{algo1}}-1}{x}\ge\frac14.
$$

The finite-$x$ statement

$$
f_{\mathrm{algo1}}>1\quad\text{for }0<x\le0.1
$$

is not proved here. It requires a uniform remainder bound for the $O(x^2)$ term.
