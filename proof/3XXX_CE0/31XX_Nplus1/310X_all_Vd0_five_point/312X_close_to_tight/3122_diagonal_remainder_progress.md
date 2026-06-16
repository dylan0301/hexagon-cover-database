# Diagonal Remainder Progress In The Close-To-Tight Region

Status: Practically proven

This file records the working diagonal remainder estimates used in the close-to-tight algorithm-1 route. The estimates are treated as practically proven working dependencies, but this file does not record the full Bernstein coefficient data for every auxiliary polynomial check. A future certificate file should add those data before these estimates are upgraded to `Proven`.

## Setup

Use the near-limit variables from [`3121_algorithm1_finite_x_setup.md`](3121_algorithm1_finite_x_setup.md). The dominant-branch residual is bounded below by

$$
R_+\ge P_{\mathrm{res}}+E_{01}+E_2.
$$

The goal of this file is to record the working estimates

$$
E_{01}\ge-2x^2,
$$

and

$$
E_2\ge-kx^2.
$$

## Line-Branch Coefficients

Let

$$
P_3=(u,v),\qquad P_5=(s_5,t).
$$

Put

$$
\Delta u=s_5-u,\qquad \Delta v=v-t.
$$

The strict branch-realization and convex-order files imply

$$
\Delta u\ge0,\qquad \Delta v\ge0.
$$

Let

$$
\ell=\sqrt{\Delta u^2+\Delta u\Delta v+\Delta v^2}.
$$

The rotated support coefficients are

$$
c_1=\frac{\Delta u}{\ell},\qquad c_0=c_2=\frac{\Delta u+\Delta v}{\ell}.
$$

Thus

$$
c_0\ge1,\qquad c_2\ge1.
$$

In the lower near-tight branch, with strict $V_4$ coordinates

$$
a=1-x,\qquad b=(1+k)x,
$$

the line-branch order gives the stronger estimate

$$
c_1\ge\frac{a}{\sqrt{a^2+ab+b^2}}\ge1-x.
$$

## The $E_{01}$ Bound

Recall

$$
E_{01}=\begin{cases}c_0r_0-xd_0,&d_0\ge d_1,\\ c_1r_1-xd_1,&d_1>d_0.\end{cases}
$$

### The $d_0$-Selected Case

Let

$$
H=k(1-\tau).
$$

For $D_0$, the local pair is

$$
(a,b)=\left(x,1-(1+H)x\right).
$$

If $d_0\ge d_1$, then $H\le1/3$ and $d_0=1-H$. The local mixed branch is active, and direct algebra gives

$$
r_0\ge x(1-H)=xd_0.
$$

Since $c_0\ge1$, this gives

$$
E_{01}\ge0.
$$

### The $d_1$-Selected Case

Assume $d_1>d_0$. For $D_1$, write the local pair as

$$
(Ax,1-(A+H)x),
$$

where

$$
A=1+k-k\tau,\qquad H=k(\tau-s).
$$

Then

$$
d_1=\max\left(\frac A2,A-H\right).
$$

Using $c_1\ge1-x$, it is enough to show

$$
(1-x)r_1-xd_1\ge-2x^2.
$$

The proof splits by the actual local diagonal branch and by the tangent branch.

| Subcase | Recorded conclusion | Proof status |
|---|---|---|
| Actual mixed branch | $(1-x)r_1-xd_1\ge-2x^2$ | Bernstein-positive endpoint checks; coefficients not fully listed here. |
| Actual quartic branch and $A\le2H$ | $(1-x)r_1-xd_1\ge-2x^2$ | Quartic root comparison with Bernstein positivity; coefficients not fully listed here. |
| Actual quartic branch and $A>2H$ | $(1-x)r_1-xd_1\ge-2x^2$ | Mismatch parameter is $O(x)$; Bernstein-positive root comparison; coefficients not fully listed here. |

Thus the working estimate is

$$
E_{01}\ge-2x^2.
$$

## The $E_2$ Bound

For $D_2$, write

$$
K=1+k,\qquad H=ks.
$$

The local pair is

$$
((K-H)x,1-Kx),
$$

and

$$
d_2=\max\left(\frac{K-H}{2},K-2H\right).
$$

Since $c_2\ge1$, it is enough to prove the local diagonal estimate

$$
r_2-xd_2\ge-(K-1)x^2=-kx^2.
$$

This estimate is checked by splitting the local diagonal branch.

| Subcase | Recorded conclusion | Proof status |
|---|---|---|
| Actual mixed branch | $r_2-xd_2\ge-(K-1)x^2$ | Bernstein-positive checks on three charts. |
| Actual quartic branch and $H\ge K/3$ | $r_2-xd_2\ge-(K-1)x^2$ | Quartic root comparison with Bernstein positivity. |
| Actual quartic branch and $H<K/3$ | $r_2-xd_2\ge-(K-1)x^2$ | Transition mismatch bound and Bernstein-positive cube check. |

Thus the working estimate is

$$
E_2\ge-kx^2.
$$

## Remaining Need

To upgrade this file from `Practically proven` to `Proven`, add either the full Bernstein coefficient lists or a reproducible exact certificate for the polynomial positivity checks used above.
