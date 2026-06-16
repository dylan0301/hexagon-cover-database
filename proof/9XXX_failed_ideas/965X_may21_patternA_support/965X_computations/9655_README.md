# May 21/22 Pattern A computation helpers

This folder contains prototype scripts for the May 21/22 Pattern A support package.

Status: Experiment

The scripts are not a proof by themselves. They support the numerical scans, Taylor coefficient checks, and Bernstein-bounding prototypes described in the Markdown notes.

Dependencies: `9657_endpoint_taylor_check.py` uses `sympy`.

Files:

- `9658_pattern_a_numeric_scan.py`: branch-filtered numerical scan for the reduced Pattern A functions and finite-difference derivatives.
- `9657_endpoint_taylor_check.py`: exact-rational Taylor polynomial bounds used in the endpoint proof.
- `9656_bernstein_bounds.py`: generic Bernstein coefficient utilities used in the non-endpoint certificate prototype.

Run examples:

```bash
python proof/9XXX_failed_ideas/965X_may21_patternA_support/965X_computations/9658_pattern_a_numeric_scan.py --grid 20
python proof/9XXX_failed_ideas/965X_may21_patternA_support/965X_computations/9657_endpoint_taylor_check.py
python proof/9XXX_failed_ideas/965X_may21_patternA_support/965X_computations/9656_bernstein_bounds.py
```
