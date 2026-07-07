# Computational Verification for the CE1/CE2 Vd0 Boundary-Loss Package

Status: Empirical

This file records numerical checks and code references for the branch analysis
in `401X_all_Vd0_boundary_loss/`.  Numerical results in this file are not proof
unless explicitly paired with a finite interval certificate or a proven analytic
lemma.

The formerly open lower-sheet $T_+$ cases are now proved analytically in
`556_lower_sheet_completion_proofs.md`.  The lower-sheet numerical observations
below should be read as historical evidence that guided the proof, not as the
current proof status.

## 1. Code location

The supporting scripts are in:

- `experiments/README.md`
- `experiments/verify_full_L_interval.py`
- `experiments/full_L_interval_certificate.json`
- `experiments/attempt_interval_L_Tplus_loss_exact_corrected.py`
- `experiments/refined_branch_sampler.py`

## 2. Strict branch sampling

The strict branch sampler uses the corrected definition

$$
B(a,c)=\max\{b:(a,b,c)\in\mathcal A,\ a+b\le1\}
$$

rather than treating every algebraic root as a branch realization.

The strict sampler was used to check which branch pairs appear numerically after enforcing:

- C-geometry formulas for $\gamma_1,\gamma_5$.
- Exact Full conditions.
- Low, $T_-$, and $T_+$ branch realization conditions.
- The removal of $D_1$ as an independent branch.

Representative findings:

- The fake branch $(\mathrm{Full},\mathrm{Full})$ disappears after exact Full conditions are enforced.
- $D_1$ appears only as a switching surface, not as a maximal branch.
- $(T_+^{hi},T_+^{hi})$ was not found, consistent with its analytic impossibility proof.
- Lower-sheet $T_+$ cases are realized but stay visibly below $F=1$ in sampling.

These strict sampling results are empirical and are not used as proof in the
final lower-sheet completion.

## 3. Interval certificate for $(\mathrm{Full},L)$

The file `verify_full_L_interval.py` certifies the far region of the branch
$(\mathrm{Full},L)$.  The tight horn is handled analytically in
`553_proven_branch_lemmas.md`.

The far-region bad set is reduced to

$$
\Delta(R,\eta)\le0, \qquad H(R,\eta)\ge0.
$$

The interval certificate subdivides the rectangle and certifies each terminal
box by proving either

$$
\inf \Delta>0
$$

or

$$
\sup H<0.
$$

Recorded run:

$$
2307\text{ certified boxes},\qquad 0\text{ unresolved boxes}.
$$

The JSON certificate records the terminal boxes and the reason for each box.

## 4. Corrected interval proof for $(L,T_+)$

The branch $(L,T_+)$ is proved by a combination of:

- an analytic $T_+$ horn proof for $r\ge10$;
- a finite interval certificate for $1<r<10$.

The corrected interval script uses variables

$$
R={1\over r}, \qquad x=ru, \qquad \tau=x(1+R)-1, \qquad \eta=\gamma_5.
$$

The corrected C-geometry formula is

$$
w={1-R\over R}(u-\delta_R-\eta), \qquad \delta_R={R\over\sqrt{1-R+R^2}+1}.
$$

An earlier failed script used the wrong formula without the factor $1/R$.

The proof uses the exact $T_+$ loss equation.  Write the right $T_+$ output as

$$
B_1=1-u-d.
$$

Then

$$
E(d)=y\tau-Ad-(1-c^2)d^2,
$$

and the loss root is certified by checking either

$$
\ell<u
$$

or

$$
E(\ell-u)>0.
$$

Recorded terminal classifications:

$$
199\text{ boxes certified by }\ell<u,
$$

$$
489\text{ boxes certified by exact }T_+\text{ loss},
$$

$$
679\text{ C-infeasible boxes},
$$

$$
305\text{ Low-infeasible boxes},
$$

and

$$
0\text{ unresolved boxes}.
$$

This is treated as a computer-assisted certificate for the compact part of
$(L,T_+)$.

## 5. Historical numerical status of lower-sheet cases

Before `556_lower_sheet_completion_proofs.md`, strict sampling found the
following formerly remaining branches:

$$
(T_+^{lo},T_-),
$$

$$
(T_+^{lo},T_+^{hi}),
$$

and

$$
(T_+^{lo},T_+^{lo}).
$$

Representative high values were:

$$
(T_+^{lo},T_+^{hi}):\quad F\approx0.91965,
$$

and

$$
(T_+^{lo},T_+^{lo}):\quad F\approx0.91093.
$$

These values suggested a visible gap.  The final proof does not rely on these
numbers; it proves all three branches analytically in
`556_lower_sheet_completion_proofs.md`.

## 6. What would count as evidence of an error

Any one of the following would invalidate or require revision of this package:

- A strict maximal-branch sample with $F\ge1$ in any branch marked proved.
- A point in the $(\mathrm{Full},L)$ certificate rectangle satisfying both $\Delta\le0$ and $H\ge0$.
- A point in the corrected $(L,T_+)$ compact region where neither $\ell<u$ nor $E(\ell-u)>0$ holds while all branch conditions hold.
- A realized $D_1$ point that is maximal without also lying on a $T_-$ or $T_+$ radial frontier.
- A realized $(T_+^{hi},T_+^{hi})$ point satisfying all C-geometry and branch-realization conditions.
- A realized lower-sheet branch satisfying all branch-realization conditions and violating one of the analytic inequalities in `556_lower_sheet_completion_proofs.md`.

## 7. Reproduction notes

Run from the repository root:

```bash
python proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/401aX_boundary_loss_experiments/401a4_verify_full_L_interval.py
python proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/401aX_boundary_loss_experiments/401a1_attempt_interval_L_Tplus_loss_exact_corrected.py
python proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/401aX_boundary_loss_experiments/401a3_refined_branch_sampler.py
```

The first two scripts are intended as certificate-style verifiers.  The sampler
is exploratory.
