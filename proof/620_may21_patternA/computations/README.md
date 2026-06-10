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
python proof/620_may21_patternA/computations/pattern_a_numeric_scan.py --grid 20
python proof/620_may21_patternA/computations/endpoint_taylor_check.py
python proof/620_may21_patternA/computations/bernstein_bounds.py
```
