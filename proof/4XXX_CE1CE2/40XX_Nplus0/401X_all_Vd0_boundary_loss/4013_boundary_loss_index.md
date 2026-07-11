# CE1/CE2 Vd0 Boundary-Loss Package

Status: Strategy

This folder records the proposed proof package for the CE1/CE2, all-Vd0
boundary-loss obstruction. The exact capped-map theorem in `4015` now resolves
the former Cell-$T$ component error: the fake lower sheet is deleted and the
four genuine upper labels are exhaustive. The package is still not proved,
because its recorded ordered-pair calculations do not cover every genuine
pair, some certificate-backed calculations were not reproducible in the
strict environment, and the CE2 replacement exits remain unrouted.

The target local statement is:

$$
\mathrm{CE1/CE2}+\text{all six }V_i\text{ are Vd0}+\text{all }a_i+b_i\le 1 \quad\Longrightarrow\quad \text{boundary-loss contradiction.}
$$

For CE2, the replacement theorem in `2104` removes a two-gap system only up to
possible V-type and $N_+$ exits. Those exits remain an assembly obligation.

Equivalently, under the CE1/CE2 reductions recorded here, any successful all-Vd0 covering must have at least one vertex triangle with

$$
a_i+b_i>1.
$$

## Boundary-loss reduction

Work under the contradiction assumptions

$$
\mathrm{CE1/CE2}+\text{all six }V_i\text{ are Vd0}+\text{all }a_i+b_i\le1.
$$

After normalization, the active $C$-boundary interval is

$$
T_C\cap e_{0,1}=[s,t], \qquad u=1-t, \qquad w=t-s>0.
$$

The adjacent maximal Vd0 contributions are

$$
B_5=\mathsf B^0_{1-\gamma_5}(s),
\qquad
B_1=\mathsf B^0_{1-\gamma_1}(u),
$$

where

$$
\mathsf B^0_c(a)
=
\sup_{\substack{
A(T)\ge a\\
C(T)\ge c\\
A(T)+B(T)\le1\\
T\text{ is Vd0}
}}B(T).
$$

Let

$$
F=B_5+B_1.
$$

The reduction in
[`4014_setup_and_reduction.md`](4014_setup_and_reduction.md)
(Status: Strategy) shows conditionally that $F<1$ gives the boundary
contradiction: the portion left for $V_2,V_3,V_4$ has length $4-F>3$, while

$$
(a_2+b_2)+(a_3+b_3)+(a_4+b_4)\le3.
$$

Therefore the branch analysis target is

$$
F<1.
$$

The exact safe relaxation and its complete four-label partition are proved in
[`4015_B_map_branch_realization.md`](4015_B_map_branch_realization.md)
(Status: Proven).

## Exact branch-matrix reaudit

The true safe upper map has only the labels

$$
L,
\qquad
T_-,
\qquad
T_+^{hi},
\qquad
\mathrm{Full}.
$$

The labels $L$ and $T_-$ both satisfy $b\le a$. Therefore every pair in
$\{L,T_-\}^2$ obeys the exact estimate

$$
B_5+B_1\le s+u=1-w<1.
$$

The pair $(\mathrm{Full},\mathrm{Full})$ is also impossible. Right Full gives

$$
ru\le\max\left\{u,1-u\right\}.
$$

Since $r>1$, this forces $u<1/2$ and $u\le1/(r+1)$. Left Full requires

$$
\gamma_5\ge\min\left\{s,1-s\right\}.
$$

Because $\gamma_5<u<1-s$, this forces $s\le1/2$ and $\gamma_5\ge s$. But

$$
\gamma_5-s
=2u-1-\delta+w\frac{r-2}{r-1}.
$$

For $1<r\le2$ the right side is negative. For $r>2$, use $w<1-u$ and
$u\le1/(r+1)$ to obtain

$$
\gamma_5-s
<-\frac1{(r-1)(r+1)}-\delta<0,
$$

again a contradiction.

The complete audit of the remaining ordered pairs is:

| Left label | Right label | Reaudit result |
|---|---|---|
| $L$ | $L$ or $T_-$ | Proved above. |
| $T_-$ | $L$ or $T_-$ | Proved above. |
| $L$ | $T_+^{hi}$ or Full | Recorded in `4016`; the interval-backed part was not reproduced in the strict environment. |
| $T_-$ | Full | Recorded in `4016`. |
| $T_-$ | $T_+^{hi}$ | Open genuine ordered pair. |
| $T_+^{hi}$ | $L$, $T_-$, $T_+^{hi}$, or Full | Recorded in `4016`, including two impossibility claims. |
| Full | $L$ or $T_-$ | Recorded in `4016`; the Full-$L$ certificate was not reproduced in the strict environment. |
| Full | $T_+^{hi}$ | Open; no proof is recorded. |
| Full | Full | Proved impossible above. |

The first open pair is not vacuous. An exact CE1-domain witness is obtained by
taking the `2105` parameter

$$
R=\frac25,
\qquad
\lambda=R=\frac25,
\qquad
s=\frac{687}{1000},
\qquad
t=\frac{689}{1000}.
$$

Thus

$$
u=1-t=\frac{311}{1000},
\qquad
w=t-s=\frac1{500},
\qquad
\rho=\frac{\sqrt{19}}5.
$$

These values satisfy every inequality in the exact CE1 domain of
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md).
The two exact radial demands are

$$
c_1=\frac{311}{400},
\qquad
c_5=\frac{7071-1000\sqrt{19}}{3000}.
$$

The selected Cell-$T$ roots are

$$
B_5=
-s+
\frac{\sqrt{s^2-sc_5+c_5^2}}{c_5},
$$

and, with

$$
\Delta_1=
\left(2uc_1^2+c_1\right)^2
-4\left(1-c_1^2\right)\left(1-u^2\right)c_1^2,
$$

$$
B_1=
\frac{2uc_1^2+c_1-\sqrt{\Delta_1}}
{2\left(1-c_1^2\right)}.
$$

Direct exact substitution gives

$$
B_5=0.217191501619\ldots
\quad(T_-),
\qquad
B_1=0.594587510271\ldots
\quad(T_+^{hi}).
$$

The branch selectors satisfy $q>0$, $B_5<s$, $B_1>u$, and $c_1<2B_1$.
Moreover $B_5+B_1<0.812$. Thus the witness is not a counterexample to the
target inequality; it proves that the missing ordered branch has nonempty
domain and needs a proof.

## Files

| File | Recorded status | Notes |
|---|---|---|
| [`4014_setup_and_reduction.md`](4014_setup_and_reduction.md) | Strategy | Target, notation, C-triangle parameterization, and proven reduction to $F<1$. |
| [`4015_B_map_branch_realization.md`](4015_B_map_branch_realization.md) | Proven | Exact safe capped map, four-label partition, and withdrawal of the fake high-$c$ sheet. |
| [`4016_proven_branch_lemmas.md`](4016_proven_branch_lemmas.md) | Strategy | Historical algebraic inequalities; two genuine ordered pairs, incomplete sketches, and noncanonical certificate dependencies remain. |
| [`4017_remaining_Tplus_obligations.md`](4017_remaining_Tplus_obligations.md) | Reference | Historical record of the discarded lower-sheet obligations and failed approaches; cross-read with [`4019_lower_sheet_completion_proofs.md`](4019_lower_sheet_completion_proofs.md) as algebraic history only. |
| [`4018_computational_verification.md`](4018_computational_verification.md) | Empirical | Numerical checks, interval-certificate status, and code references. |
| [`4019_lower_sheet_completion_proofs.md`](4019_lower_sheet_completion_proofs.md) | Reference | Historical calculations on the now-discarded lower sheet. |
| [`401aX_boundary_loss_experiments/401a0_README.md`](401aX_boundary_loss_experiments/401a0_README.md) | Experiment | Experiment helpers for the package. |

## Historical branch calculations

The following algebraic cells have recorded calculations in this package:

- $(L,\mathrm{Full})$.
- $(T_-,\mathrm{Full})$.
- $(\mathrm{Full},L)$, using a local analytic horn proof plus a finite interval certificate for the far region.
- $(\mathrm{Full},T_-)$.
- $(\mathrm{Full},\mathrm{Full})$ is impossible.
- $D_1$ is not an independent maximal branch.
- $(L,T_+)$.
- $(T_+,\mathrm{Full})$ is impossible.
- $(T_+^{hi},L)$ and $(T_+^{lo},L)$.
- $(T_+^{hi},T_-)$.
- $(T_+^{hi},T_+^{hi})$ is impossible.
- $(T_+^{lo},T_-)$.
- $(T_+^{lo},T_+^{hi})$.
- $(T_+^{lo},T_+^{lo})$.

The exact upper-map inclusion is now proved in `4015`. The package remains
Strategy until the two open genuine ordered pairs, the non-reproduced
certificate-backed steps, the $r>1$ center-geometry reduction, and the CE2
replacement exits are all certified.
