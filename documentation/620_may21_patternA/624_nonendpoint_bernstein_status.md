# Non-Endpoint Bernstein Certificate Status

Status: Empirical

This file records the current status of the non-endpoint derivative certification for Pattern A. The endpoint range $0<r\le1/200$ is proved in `623_endpoint_taylor_remainder.md`. The remaining region is

$$
\frac1{200}\le r\le r_*:=\frac{\sqrt{37}-3}{8}.
$$

The method here is a certificate prototype. It has verified representative boxes and small slabs, but it is not yet a complete finite certificate of the full remaining domain.

## 1. Derivative targets

Set $q=sr$ and define

$$
\widetilde F_I(s,r)=F_I(sr,r),
\qquad
\widetilde F_{II}(s,r)=F_{II}(sr,r).
$$

The monotone proof would follow from

$$
\widetilde F_{I,s}>0,
\qquad
\widetilde F_{I,r}>0,
$$

on Region I, and

$$
\widetilde F_{II,s}>0,
\qquad
\widetilde F_{II,r}>0,
$$

on Region II.

The derivative formulas are

$$
\widetilde F_{I,s}=r\bigl(h_B(r,sr)+1-\tau_q(sr,r)\bigr),
$$

$$
\widetilde F_{I,r}=h_A(r,sr)+s h_B(r,sr)+s-\tau_r(sr,r)-s\tau_q(sr,r),
$$

$$
\widetilde F_{II,s}=r\bigl(h_B(\sigma(r),sr)-\tau_q(sr,r)\bigr),
$$

and

$$
\widetilde F_{II,r}=1-\sigma'(r)+\sigma'(r)h_A(\sigma(r),sr)+s h_B(\sigma(r),sr)-\tau_r(sr,r)-s\tau_q(sr,r).
$$

Here $h=\rho_2$.

## 2. Quartic resultant roots

For $P_3$, eliminate $u$ from

$$
F_A(u,v)=0,
\qquad
C_2(u,v)=0
$$

to get a quartic

$$
R_A(v;s,r)=0.
$$

For $P_5$, eliminate $u$ from

$$
F_B(u,v)=0,
\qquad
C_5(u,v)=0
$$

to get

$$
R_B(v;s,r)=0.
$$

The branch is selected by filtering the quartic roots with

$$
P_A,Q_A,S_A\ge0,
\qquad D_A^2\le1,
$$

and

$$
P_B,Q_B,S_B\ge0,
\qquad D_B^2\le1.
$$

Then the root closest to $V_4$ is used.

## 3. Bernstein root certification

For a polynomial $P$ on a box $B$, convert $P$ to Bernstein form on $B$. If all Bernstein coefficients are positive, then $P>0$ on $B$; if all are negative, then $P<0$ on $B$.

The prototype uses Bernstein bounds for

$$
R_A(v_-;s,r),\quad R_A(v_+;s,r),\quad \partial_vR_A(v;s,r),
$$

and similarly for $R_B$, to isolate a unique selected root interval.

A key improvement is to bound recovered rational coordinates by Bernstein inequalities. If

$$
u=\frac{N(v,s,r)}{D(v,s,r)}
$$

and $D<0$ on the box, then $\ell\le u\le h$ is certified by Bernstein signs of

$$
N-D\ell\le0,
\qquad
N-Dh\ge0.
$$

This is much sharper than ordinary interval evaluation of $N/D$.

## 4. Certified example boxes

### Region I

For

$$
s\in[0.68,0.6801],
\qquad
r\in[0.1,0.1001],
$$

the Bernstein certificate gives

$$
\widetilde F_{I,s}\in[0.15434,0.17891],
$$

and

$$
\widetilde F_{I,r}\in[0.31934,0.57874].
$$

For

$$
s\in[0.805733,0.806233],
\qquad
r\in[0.1,0.10025],
$$

it gives

$$
\widetilde F_{I,s}\in[0.10744,0.18616],
$$

and

$$
\widetilde F_{I,r}\in[0.25048,1.17501].
$$

For

$$
s\in[0.70,0.7002],
\qquad
r\in[0.25,0.2502],
$$

it gives

$$
\widetilde F_{I,s}\in[0.67450,0.74391],
$$

and

$$
\widetilde F_{I,r}\in[0.53934,0.86993].
$$

### Region II

For

$$
s\in[0.60,0.6001],
\qquad
r\in[0.1,0.1001],
$$

it gives

$$
\widetilde F_{II,s}\in[0.01645,0.03892],
$$

and

$$
\widetilde F_{II,r}\in[0.29576,0.51801].
$$

For

$$
s\in[0.55,0.5501],
\qquad
r\in[0.2,0.2001],
$$

it gives

$$
\widetilde F_{II,s}\in[0.10734,0.13222],
$$

and

$$
\widetilde F_{II,r}\in[0.45751,0.58444].
$$

For

$$
s\in[0.65,0.65005],
\qquad
r\in[0.38,0.38005],
$$

it gives

$$
\widetilde F_{II,s}\in[0.21305,0.22978],
$$

and

$$
\widetilde F_{II,r}\in[0.75043,0.80573].
$$

## 5. Small slabs certified by prototype

The prototype certified the full slab

$$
s\in[0.68,0.682],
\qquad
r\in[0.1,0.101]
$$

in Region I with subdivision $\Delta s=\Delta r=2\cdot10^{-4}$. All $50$ boxes certified, with

$$
\min\widetilde F_{I,s}\ge0.14173793082605884,
$$

and

$$
\min\widetilde F_{I,r}\ge0.1901465463129695.
$$

It also certified

$$
s\in[0.60,0.602],
\qquad
r\in[0.1,0.101]
$$

in Region II with the same subdivision. All $50$ boxes certified, with

$$
\min\widetilde F_{II,s}\ge0.004965950880400615,
$$

and

$$
\min\widetilde F_{II,r}\ge0.18512557344643624.
$$

## 6. Remaining gap

The full non-endpoint region has not yet been covered. The current prototype recomputes Bernstein coefficients box-by-box and is too slow for a full finite cover. A complete certificate should cache Bernstein coefficients on parent boxes and use de Casteljau subdivision for child boxes.

Thus this file is empirical/certificate-prototype status, not a proof of the non-endpoint region.
