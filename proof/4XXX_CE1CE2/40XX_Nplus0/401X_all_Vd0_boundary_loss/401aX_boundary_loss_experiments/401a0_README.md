# CE Vd0 Boundary-Loss Experiments

Status: Experiment

This folder contains scripts supporting `proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/`.

## Files

- `401a4_verify_full_L_interval.py`: interval verifier for the far region of the branch $(\mathrm{Full},L)$.
- `401a1_attempt_interval_L_Tplus_loss_exact_corrected.py`: corrected interval verifier for the compact part of $(L,T_+)$ using the exact right-side $T_+$ loss equation.
- `401a3_refined_branch_sampler.py`: selector-aware demand-map sampler for exploratory numerical checks; it does not certify the actual-coordinate classified map.
- `401a2_full_L_interval_certificate.json`: short metadata record for the recorded $(\mathrm{Full},L)$ interval run.  The verifier regenerates the certified box decomposition.

## Notes

The scripts use Python and `mpmath.iv`.  They are research helpers, not a polished proof assistant backend.

Run from the repository root:

```bash
python proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/401aX_boundary_loss_experiments/401a4_verify_full_L_interval.py
python proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/401aX_boundary_loss_experiments/401a1_attempt_interval_L_Tplus_loss_exact_corrected.py
python proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/401aX_boundary_loss_experiments/401a3_refined_branch_sampler.py
```

The sampler is empirical.  The interval scripts are certificate-style checks; repository-grade certification would require freezing the interval backend and, if desired, storing a full terminal-box certificate.
