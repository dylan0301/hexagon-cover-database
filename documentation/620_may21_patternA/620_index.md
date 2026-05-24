# May 21/22 Pattern A Four-Point Package

Status: Strategy

This folder records the current state of the May 21/22 four-point Pattern A obstruction.

The package concerns the constrained slice

$$
p=t_0=t_1,\qquad q=t_2=t_3,\qquad r=t_4=t_5,\qquad q<r,\qquad q\le p\le r,
$$

with the strict local AB-union triangle at $V_4$. It focuses on the lower outside-quarter region

$$
q<\frac14,
$$

and on the Pattern A support configuration for the four points

$$
P_3,\quad P_5,\quad G_0,\quad G_2.
$$

The current result is not a full proof of the May 21/22 target. The proven part is a reduction and endpoint theorem for Pattern A. The remaining non-endpoint monotonicity certificate is supported by Bernstein/root-isolation experiments but is not yet a complete finite certificate.

## Files

- `621_setup_and_patternA_reduction.md`
  - Defines the local coordinates, the selected $P_3,P_5$ branches, the radial points $G_0,G_2$, the Pattern A support formula, and the reduced inequalities.
- `622_radial_monotone_envelope.md`
  - Proves the monotone envelope theorem eliminating the parameter $p$ from Pattern A.
- `623_endpoint_taylor_remainder.md`
  - Proves the endpoint theorem for $0<r\le 1/200$ using Taylor remainders.
- `624_nonendpoint_bernstein_status.md`
  - Records the Bernstein certificate strategy, verified boxes, and the remaining non-endpoint gap.
- `625_numerical_tests_and_counterexamples.md`
  - Records numerical tests, earlier four-point counterexamples, and the exact status of the outside-quarter version.
- `626_current_status.md`
  - Short dependency and status table.

## Code

Prototype numerical and certification scripts are under:

- `computations/may21_patternA/README.md`
- `computations/may21_patternA/pattern_a_numeric_scan.py`
- `computations/may21_patternA/endpoint_taylor_check.py`
- `computations/may21_patternA/bernstein_bounds.py`

These scripts are not proof by themselves. They are reproducibility aids for the empirical and certificate-prototype claims in this folder.

## Status summary

Proven in this folder:

$$
\min_{q\le p\le r}\{\rho(r,p)+\rho(p,q)\}
=
\begin{cases}
\rho_2(r,q)+q, & q\ge \sigma(r),\\
r-\sigma(r)+\rho_2(\sigma(r),q), & q<\sigma(r),
\end{cases}
$$

and

$$
F_I(sr,r)>0,\qquad F_{II}(sr,r)>0
$$

on the endpoint range $0<r\le 1/200$.

Still open in this folder:

$$
\widetilde F_{I,s}>0,\quad \widetilde F_{I,r}>0,\quad
\widetilde F_{II,s}>0,\quad \widetilde F_{II,r}>0
$$

on the full remaining non-endpoint region $1/200\le r\le (\sqrt{37}-3)/8$.
