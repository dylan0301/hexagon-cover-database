# CE1/CE2, $N_+=0$, T3-Like With No Vd1/Vd2

Status: Proven

This package proves the branch

$$
T_C\text{ is CE1 or CE2},
\qquad
N_+=0,
\qquad
N_{\rm gap}\in\{1,2\},
$$

with no Vd1/Vd2 vertex role and at least one T3-like vertex role. The midpoint
normalization is

$$
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\}.
$$

This is the active nonzero-gap Method 2 invocation.  If
$N_{\rm gap}=0$, the six open V roles cover $\partial H$, and the common
$N_+=0$ boundary-complete consequence
[`2500`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md#boundary-complete-zero-gap-consequences)
closes the case by Method 1, independently of the T3-like count.  The
zero-gap case is therefore not owned by `407X` in the exhaustive routing.

The proof has four stages.

1. `4071` uses the shared T3-like tradeoff `2013` to force $T_0$ to be
   T3-like.
2. `4072` and `4073` isolate the two relevant radial arms and reduce the branch
   to one strict endpoint-sum inequality.
3. `4074`, `4075`, `4078`, `4079`, and `407a` prove the four genuine endpoint
   labels, with details in `407c` and exact assembly in `407d`.
4. `407e` restates the proved geometric finite-cell consequence in the
   canonical public notation; it makes no arbitrary-real-domain claim.

## Chain interpretation

Let $A_1,A_5,C_1,C_5$ be the actual maximal boundary and radial reaches, and
choose the realized residual lower bounds

$$
a_j^*\le A_j,
\qquad
c_j^*\le C_j
\qquad(j\in\{1,5\}).
$$

At endpoint $j$, use the direct $\mathrm{Lin}$ value $1-a_j^*$ when
$c_j^*\le1/2$, and use the raw value $M_{c_j^*}(a_j^*)$ when
$c_j^*>1/2$.  The sum of these two branchwise endpoint contributions is
strictly below one.

Thus no additional transfer symbol is needed.  The three interior
nonsupercritical V triangles are used only through

$$
\mathrm I^3.
$$

Thus the package is an exact-endpoint/identity-interior relaxation of the same
$g$-composition calculus as the all-Vd0 branches. The hard endpoint region is
not replaced by a weaker universal formula.

In the CE1 case, a possible point-only contact of the closed C triangle on
the companion edge is discarded from the boundary-trace interval. Such a
closure-only contact is not a point of the original open role $U_C$ and has
zero trace length, so it supplies neither open coverage nor a positive
C-triangle boundary trace. This is why `4073` takes the companion interval to
be empty in CE1.

The authenticated files `4073`, `4074`, `4075`, `4078`, `4079`, `407a`,
`407c`, and `407d` retain their recorded bytes. Their symbols
$B_c,\widehat B_c,F_c,G_c$ and their four historical labels are interpreted
only through the wrapper crosswalk in `0910`; their local $q$ is not a public
count.

## Selected high sheet

The selected high sheet is normalized by the universal selected-$Q_+$ theorem
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
| [`4072_support_isolation_after_T0_T3_like.md`](4072_support_isolation_after_T0_T3_like.md) | Proven | Uses the direct $N_++N_{\rm sp}$ theorem to isolate the two active radial arms. |
| [`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md) | Reduction | Derives the residual endpoint inputs and reduces to the exact branchwise endpoint sum. |
| [`4074_L_Full_branch.md`](4074_L_Full_branch.md) | Proven | Authenticated source for the canonical $(\mathrm{Const},\mathrm{Lin})$ branch. |
| [`4075_Tminus_low_lower_branch_obligations.md`](4075_Tminus_low_lower_branch_obligations.md) | Proven | Authenticated source for the canonical $(\mathrm{Const},\mathrm{Const})$ and $(\mathrm{Const},Q_-)$ branches and the left-$Q_-$ family. |
| [`4078_left_L_family_completion.md`](4078_left_L_family_completion.md) | Proven | Authenticated source for the remaining canonical $(\mathrm{Const},Q_+)$ branch. |
| [`4079_first_Full_branch.md`](4079_first_Full_branch.md) | Proven | Authenticated source excluding the first-coordinate $\mathrm{Lin}$ branch in the hard region. |
| [`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md) | Proven | Authenticated source for all four first-coordinate $Q_+$ branches using the universal selected curve. |
| [`407c_rigor_completion_details.md`](407c_rigor_completion_details.md) | Proven | Supplies the detailed Low, center-transfer, high-sheet, and threshold estimates. |
| [`407d_rigor_final_assembly.md`](407d_rigor_final_assembly.md) | Proven | Checks the exact four-label inventory and assembles the contradiction. |
| [`407e_pure_finite_cell_theorem.md`](407e_pure_finite_cell_theorem.md) | Proven | Canonical wrapper for the realized geometric finite-cell consequence; no universal extracted-domain claim. |
| [`407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py`](407X_computation/407b_T_hi_Tminus_qright_threshold_certificate.py) | Experiment | Optional exact rational cross-check; not a proof dependency. |

## Exhaustive analytic inventory

In canonical notation, the exact branchwise outgoing bound has the four labels

$$
\mathrm{Const},\qquad Q_-,\qquad Q_+,\qquad\mathrm{Lin}.
$$

The hard region is $a_1^*+a_5^*\le1$. The retained proofs cover every first
label:

| First label | Complete source |
|---|---|
| $\mathrm{Const}$ | `4074`, `4075`, and `4078` |
| $Q_-$ | `4075` |
| $Q_+$ | `407a`, with details in `407c` and common curvature in `2016` |
| $\mathrm{Lin}$ | Excluded by `4079` |

Thus every genuine label pair is unrealizable or has total branchwise outgoing
reach strictly below one. The reduction in `4073` then gives the perimeter
contradiction for the active nonzero-gap branch. The optional script remains
only a redundant exact check.
