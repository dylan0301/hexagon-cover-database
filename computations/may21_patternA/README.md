# May 21/22 Pattern A computation helpers

This folder contains prototype scripts for the documentation package `documentation/620_may21_patternA/`.

Status: experimental / reproducibility aid.

The scripts are not a proof by themselves. They support the numerical scans, Taylor coefficient checks, and Bernstein-bounding prototypes described in the Markdown notes.

Files:

- `pattern_a_numeric_scan.py`: branch-filtered numerical scan for the reduced Pattern A functions and finite-difference derivatives.
- `endpoint_taylor_check.py`: exact-rational Taylor polynomial bounds used in the endpoint proof.
- `bernstein_bounds.py`: generic Bernstein coefficient utilities used in the non-endpoint certificate prototype.

Run examples:

```bash
python computations/may21_patternA/pattern_a_numeric_scan.py --grid 20
python computations/may21_patternA/endpoint_taylor_check.py
python computations/may21_patternA/bernstein_bounds.py
```
