# May 21/22 Pattern A computation helpers

This folder contains prototype scripts for the documentation package this proof package.

Status: experimental / reproducibility aid.

The scripts are not a proof by themselves. They support the numerical scans, Taylor coefficient checks, and Bernstein-bounding prototypes described in the Markdown notes.

Dependencies: `endpoint_taylor_check.py` uses `sympy`.

Files:

- `pattern_a_numeric_scan.py`: branch-filtered numerical scan for the reduced Pattern A functions and finite-difference derivatives.
- `endpoint_taylor_check.py`: exact-rational Taylor polynomial bounds used in the endpoint proof.
- `bernstein_bounds.py`: generic Bernstein coefficient utilities used in the non-endpoint certificate prototype.

Run examples:

```bash
python proof/9XXX_failed_ideas/962X_may21_four_point_failure/962X_computations/9632_pattern_a_numeric_scan.py --grid 20
python proof/9XXX_failed_ideas/962X_may21_four_point_failure/962X_computations/9631_endpoint_taylor_check.py
python proof/9XXX_failed_ideas/962X_may21_four_point_failure/962X_computations/9630_bernstein_bounds.py
```
