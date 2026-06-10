# CE Vd0 Boundary-Loss Experiments

Status: Computational helpers

This folder contains scripts supporting `proof/550_CE_Vd0_boundary_loss/`.

## Files

- `verify_full_L_interval.py`: interval verifier for the far region of the branch $(\mathrm{Full},L)$.
- `attempt_interval_L_Tplus_loss_exact_corrected.py`: corrected interval verifier for the compact part of $(L,T_+)$ using the exact right-side $T_+$ loss equation.
- `refined_branch_sampler.py`: strict branch-realization sampler for exploratory numerical checks.
- `full_L_interval_certificate.json`: short metadata record for the recorded $(\mathrm{Full},L)$ interval run.  The verifier regenerates the certified box decomposition.

## Notes

The scripts use Python and `mpmath.iv`.  They are research helpers, not a polished proof assistant backend.

Run from the repository root:

```bash
python proof/550_CE_Vd0_boundary_loss/experiments/verify_full_L_interval.py
python proof/550_CE_Vd0_boundary_loss/experiments/attempt_interval_L_Tplus_loss_exact_corrected.py
python proof/550_CE_Vd0_boundary_loss/experiments/refined_branch_sampler.py
```

The sampler is empirical.  The interval scripts are certificate-style checks; repository-grade certification would require freezing the interval backend and, if desired, storing a full terminal-box certificate.
