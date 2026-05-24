# Current Status of the May 21/22 Pattern A Package

Status: Reference

## Proven

### Pattern A scalar reduction

Under the selected $P_3,P_5$ branches and Pattern A contact structure,

$$
L_A\ge1
$$

is equivalent to

$$
\rho(r,p)+\rho(p,q)\ge\tau(q,r).
$$

See `621_setup_and_patternA_reduction.md`.

### Elimination of $p$

The minimum over $q\le p\le r$ is

$$
\min_{q\le p\le r}\{\rho(r,p)+\rho(p,q)\}
=
\begin{cases}
\rho_2(r,q)+q, & q\ge\sigma(r),\\
r-\sigma(r)+\rho_2(\sigma(r),q), & q<\sigma(r).
\end{cases}
$$

See `622_radial_monotone_envelope.md`.

### Endpoint theorem

For $0<r\le1/200$,

$$
F_I(sr,r)>0,
\qquad
F_{II}(sr,r)>0.
$$

See `623_endpoint_taylor_remainder.md`.

## Empirical / certificate prototype

For the non-endpoint region

$$
\frac1{200}\le r\le\frac{\sqrt{37}-3}{8},
$$

Bernstein certificate prototypes prove derivative positivity on sample boxes and small slabs, but no full finite cover has been recorded.

The target derivative signs are

$$
\widetilde F_{I,s}>0,
\qquad
\widetilde F_{I,r}>0,
$$

and

$$
\widetilde F_{II,s}>0,
\qquad
\widetilde F_{II,r}>0.
$$

See `624_nonendpoint_bernstein_status.md`.

## Not yet proved

The following is still open in this package:

$$
F_I(q,r)\ge0
\quad\text{and}\quad
F_{II}(q,r)\ge0
$$

on the full non-endpoint lower outside-quarter region.

Consequently, this folder does not yet prove the full May 21/22 four-point obstruction.

## Recommended next task

Complete a finite Bernstein certificate cover for the derivative signs on

$$
\frac1{200}\le r\le\frac{\sqrt{37}-3}{8}.
$$

The implementation should cache Bernstein coefficients on parent boxes and use de Casteljau subdivision for child boxes.
