# CE1/CE2, $N_+=0$, T3-Like With No Vd1/Vd2

Status: Proven

This package proves the branch

$$
T_C\text{ is CE1 or CE2},
\qquad
N_+=0,
$$

with no Vd1/Vd2 vertex role and at least one T3-like vertex role. The midpoint
normalization is

$$
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\}.
$$

The proof has three stages.

1. `4071` uses the shared T3-like tradeoff `2013` to force $T_0$ to be
   T3-like.
2. `4072` and `4073` isolate the two relevant radial arms and reduce the branch
   to one strict endpoint-sum inequality.
3. `4074`, `4075`, `4078`, `4079`, and `407a` prove the four genuine endpoint
   labels, with details in `407c` and exact assembly in `407d`.
4. `407e` proves that the same finite audit holds universally on the explicit
   real-variable cell union used by the optimization registry.

## Chain interpretation

Let $A_1,A_5$ be the two residual endpoint inputs and let $C_1,C_5$ be their
radial demands. In the canonical $g$-notation, the endpoint target is

$$
\boxed{
\widehat g_{C_1}(1-A_1)
+
\widehat g_{C_5}(1-A_5)
<1.
}
$$

The two terms are the exact hatted outgoing caps. The three interior
nonsupercritical V triangles are used only through

$$
\mathrm I^3.
$$

Thus the package is an exact-endpoint/identity-interior relaxation of the same
$g$-composition calculus as the all-Vd0 branches. The hard endpoint region is
not replaced by a weaker universal formula.

## Selected high sheet

The selected high sheet is normalized by the universal selected-$T_+$ theorem
[`2016`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2016_universal_Tplus_normal_form.md).
In particular, the historical local radical

$$
m_\beta=\sqrt{\beta^2-\beta+1}
$$

is the universal curve with $x=1-\beta$, and it admits the exact rational
parameter

$$
\beta=\frac{z(2-z)}{1-z^2},
\qquad
m_\beta=\frac{1-z+z^2}{1-z^2}.
$$

The branch proofs retain $\beta,m_\beta$ where that notation is shorter; the
independent center radical $\sqrt{r^2-r+1}$ remains necessary. The high-sheet
center variable is written explicitly as $\nu=\gamma_5$ throughout `407a`
and Section 2 of `407c`.

## Proof path

| File | Status | Role |
|---|---|---|
| [`4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md`](4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md) | Proven | Normalizes the T3-like traces and forces $T_0$ to be T3-like. |
| [`4072_support_isolation_after_T0_T3_like.md`](4072_support_isolation_after_T0_T3_like.md) | Proven | Uses the three-short-role theorem to isolate the two active radial arms. |
| [`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md) | Reduction | Derives the residual endpoint inputs and reduces to the exact hatted endpoint sum. |
| [`4074_L_Full_branch.md`](4074_L_Full_branch.md) | Proven | Proves the $(L,\mathrm{Full})$ branch. |
| [`4075_Tminus_low_lower_branch_obligations.md`](4075_Tminus_low_lower_branch_obligations.md) | Proven | Proves the $(L,L)$ and $(L,T_-)$ branches and the left-$T_-$ family. |
| [`4078_left_L_family_completion.md`](4078_left_L_family_completion.md) | Proven | Proves the remaining $(L,T_+^{hi})$ branch. |
| [`4079_first_Full_branch.md`](4079_first_Full_branch.md) | Proven | Excludes the first-coordinate $\mathrm{Full}$ branch in the hard region. |
| [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md) | Proven | Proves all four first-coordinate $T_+^{hi}$ branches using the universal selected curve. |
| [`407c_rigor_completion_details.md`](407c_rigor_completion_details.md) | Proven | Supplies the detailed Low, center-transfer, high-sheet, and threshold estimates. |
| [`407d_rigor_final_assembly.md`](407d_rigor_final_assembly.md) | Proven | Checks the exact four-label inventory and assembles the contradiction. |
| [`407e_pure_finite_cell_theorem.md`](407e_pure_finite_cell_theorem.md) | Proven | Transfers the exact inventory to every point of the explicit real-variable cell union. |
| [`407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py`](407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py) | Experiment | Optional exact rational cross-check; not a proof dependency. |

## Exhaustive analytic inventory

The exact hatted outgoing map has the four labels

$$
L,\qquad T_-,\qquad T_+^{hi},\qquad\mathrm{Full}.
$$

The hard region is $A_1+A_5\le1$. The retained proofs cover every first
label:

| First label | Complete source |
|---|---|
| $L$ | `4074`, `4075`, and `4078` |
| $T_-$ | `4075` |
| $T_+^{hi}$ | `407a`, with details in `407c` and common curvature in `2016` |
| $\mathrm{Full}$ | Excluded by `4079` |

Thus every genuine label pair is unrealizable or has total hatted outgoing
reach strictly below one. The reduction in `4073` then gives the perimeter
contradiction. The optional script remains only a redundant exact check.
