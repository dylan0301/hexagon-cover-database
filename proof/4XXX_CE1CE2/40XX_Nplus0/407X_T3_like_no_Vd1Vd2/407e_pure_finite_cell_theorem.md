# Geometric Finite-Cell T3 Endpoint Wrapper

Status: Proven

This source records the canonical-notation consequence of the authenticated
`407X` calculation. Its hypotheses are the realized geometric hypotheses of
the support-isolated branch; it does not assert a universal theorem on an
arbitrary extracted real-variable cell union.

## Statement

Let $U_C,U_0,\ldots,U_5$ be original open role triangles and put
$T_C=\overline{U_C}$ and $T_i=\overline{U_i}$. Assume the geometric branch of
[`4071`](4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md)--[`4073`](4073_boundary_loss_framework.md):

- $T_C$ is CE1 or CE2 and has unique midpoint $M_0$;
- $N_+=0$, no $T_i$ is Vd1 or Vd2, and at least one $T_i$ is T3-like;
- after the proved normalization and reflection, $T_0$ is T3-like and the
  two active radial arms have the support isolation proved in `4072`.

Let $A_1,A_5,C_1,C_5$ be the actual maximal boundary and radial reaches.
For this wrapper only, write $[A_i]_{407X},[C_i]_{407X}$ for the legacy
symbols called $A_i,C_i$ in the authenticated files, and choose the canonical
selected lower bounds

$$
a_i^*:=[A_i]_{407X}\le A_i,
\qquad
c_i^*:=[C_i]_{407X}\le C_i
\qquad(i=1,5).
$$

These are exactly the realized residual boundary and radial requirements
defined in Sections 4--5 of `4073`. Then

$$
\boxed{
\overline M_{c_5^*}(a_5^*)+\overline M_{c_1^*}(a_1^*)<1.
}
$$

Consequently the seven original open triangles cannot cover the perimeter in
this branch.

## Proof

In the authenticated sources, the canonical cap $\overline M_c(a)$ is written
$\widehat B_c(a)$. The compatibility crosswalk in
[`0910`](../../../09XX_appendices/0910_notation_dictionary.md) and the cap theorem
[`2011`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md)
gives

$$
\widehat B_c(a)=\overline M_c(a).
$$

The realized residual and hit/miss alternatives in `4073` select exactly one
of the four genuine contact labels at each endpoint. The exhaustive geometric
audit in [`407d`](407d_rigor_final_assembly.md), using `4074`, `4075`, `4078`,
`4079`, `407a`, and `407c`, proves

$$
\widehat B_{[C_5]_{407X}}([A_5]_{407X})
+\widehat B_{[C_1]_{407X}}([A_1]_{407X})<1
$$

for every such realized label pair, including all branch-boundary equality
assignments. Substituting the wrapper crosswalk and replacing the legacy cap
by the canonical cap proves the displayed inequality. The boundary-loss
theorem in Section 7 of `4073` then gives the perimeter contradiction.
$\square$

The proof above deliberately invokes the geometric realization and support
isolation. No converse realization theorem, and no theorem about all points
of a larger source-only scalar domain, is claimed.
