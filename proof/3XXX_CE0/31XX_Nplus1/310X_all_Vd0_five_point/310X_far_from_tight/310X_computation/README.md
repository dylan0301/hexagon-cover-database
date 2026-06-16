# 310X Computation Helpers

Status: Experiment

This folder contains helper code for the CE0, $N_+=1$, all-Vd0 algorithm-2 route. These scripts are colocated with the proof package they support.

The scripts do not by themselves upgrade any mathematical statement to `Proven`. A Markdown claim is proof-level only when its file carries a proven status. Numerical and interval outputs remain empirical or certificate-outline material unless the certificate data and verifier are recorded and independently checkable.

## Files

| File | Role | Proof status |
|---|---|---|
| `interval_decimal.py` | Small outward-rounded Decimal interval arithmetic helper. | Experiment. |
| `verify_strict_branch_line_identities.py` | SymPy checks for algebraic identities used in [`../3105_strict_branch_line_realization.md`](../3105_strict_branch_line_realization.md). | Helper for a proven local lemma. |
| `algo2_numeric_model.py` | High-precision numerical model for the algorithm-2 two-variable construction and lower-bound functions. | Empirical helper. |
| `verify_transition_strip_certificate_arithmetic.py` | Checks that the recorded endpoint and curvature constants in [`../3109_algorithm2_transition_strip_certificate.md`](../3109_algorithm2_transition_strip_certificate.md) imply positive interpolation margins. | Verifies only the arithmetic layer of the certificate outline. |

## Typical Commands

From this directory:

```text
python verify_strict_branch_line_identities.py
python algo2_numeric_model.py
python verify_transition_strip_certificate_arithmetic.py
```

The numerical model prints the transition point for $p=0.1$ by default. To evaluate another point, use:

```text
python algo2_numeric_model.py --p 0.15
python algo2_numeric_model.py --p 0.12 --q 0.83
```

## Remaining Certificate Gap

The transition-strip proof outline still lacks a full repository-grade interval certificate. In particular, the endpoint and curvature enclosures in [`../3109_algorithm2_transition_strip_certificate.md`](../3109_algorithm2_transition_strip_certificate.md) need saved interval subdivision data or verifier code that checks them from first principles, including the selected-root branch checks for the 309 line-circle equations.
