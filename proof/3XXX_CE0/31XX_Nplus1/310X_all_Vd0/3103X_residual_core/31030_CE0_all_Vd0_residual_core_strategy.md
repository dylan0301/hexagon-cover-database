# CE0 All-Vd0 Residual-Core Closure

Status: Proven

This note closes the CE0, $N_+=1$, all-Vd0 branch by reducing it to the
center-class-independent all-boundary theorem in
[`31035_center_independent_all_boundary_obstruction.md`](31035_center_independent_all_boundary_obstruction.md).
The original research blueprint is preserved verbatim in
[`31031_original_residual_core_draft.md`](31031_original_residual_core_draft.md)
for provenance. Statements in that imported draft have no corpus status unless
they are proved in an explicitly linked numbered source.

## 1. Branch hypotheses

Use the role notation from
[`1000_problem_statement.md`](../../../../1XXX_foundations/10XX_global_conventions/1000_problem_statement.md):

$$
T_C,T_0,\dots,T_5.
$$

Assume a hypothetical cover of $H$ by these seven open unit equilateral
triangles satisfies

$$
T_C\text{ is CE0},
\qquad
N_+=1,
$$

and every vertex role $T_i$ is Vd0. The CE classification is proved in
[`1101_CE_classification.md`](../../../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md),
the vertex-role classification is proved in
[`1201_V_triangle_types.md`](../../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md),
and the actual-row convention is recorded in
[`1212_vertex_rows_and_Nplus.md`](../../../../1XXX_foundations/12XX_V_triangle/1212_vertex_rows_and_Nplus.md).

Thus the six Vd0 roles have exactly one supercritical actual maximal boundary
row.

## 2. CE0 forces full vertex-role boundary coverage

We claim that

$$
\partial H\subseteq\bigcup_{i=0}^5T_i.
\tag{1}
$$

Suppose instead that $P\in\partial H$ lies in none of the six vertex roles.
The full-cover hypothesis gives $P\in T_C$. Because $T_C$ is open, a plane
ball about $P$ lies in $T_C$. If $P$ is in the relative interior of a
hexagon edge, the intersection of that ball with the edge is a
positive-length interval. If $P$ is a hexagon vertex, the ball contains a
positive-length interval on each incident edge. In either case, $T_C$ meets a
boundary edge of $H$ in positive length, contrary to the CE0 definition.
This proves (1).

## 3. Application of the center-independent theorem

The hypothetical branch configuration now satisfies every hypothesis of
[`31035_center_independent_all_boundary_obstruction.md`](31035_center_independent_all_boundary_obstruction.md):

- the seven open unit equilateral triangles cover all of $H$;
- the six vertex roles are Vd0;
- by (1), those six roles cover $\partial H$; and
- $N_+=1$ gives exactly one supercritical actual row.

That theorem constructs strict boundary handoffs, places the resulting
two-parameter row in

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1,
$$

and forces the compact residual-core witness

$$
K_{\mathrm{wit}}(a,b)
=
\mathcal D(a,b)
\mathbin\cup
\left\{Q_-(a,b),Q_0(a,b),Q_+(a,b)\right\}
$$

into $T_C$. The symmetric and asymmetric witness theorems
[`31032`](31032_symmetric_witness_construction.md) and
[`31033`](31033_asymmetric_witness_construction.md), together with the
terminal enclosure theorem
[`31034`](31034_witness_enclosure_inequality.md), give

$$
\Lambda\left(K_{\mathrm{wit}}(a,b)\right)\ge1.
$$

But a compact subset of an open unit equilateral triangle has minimum
enclosing equilateral side length strictly below $1$. This is a contradiction.
Therefore the CE0, $N_+=1$, all-Vd0 branch cannot occur.

## 4. Dependency ledger

| Item | Recorded status | Role |
|---|---|---|
| Center-independent all-boundary theorem in [`31035`](31035_center_independent_all_boundary_obstruction.md) | Proven | Converts full Vd0 boundary coverage and exactly one actual supercritical row into the terminal contradiction. |
| Symmetric witness construction in [`31032`](31032_symmetric_witness_construction.md) | Proven | Supplies six uniform core witnesses and the forced central disk used by `31035`. |
| Asymmetric witness construction in [`31033`](31033_asymmetric_witness_construction.md) | Proven | Supplies exact formulas and uniform core membership for $Q_-,Q_0,Q_+$. |
| Enclosure inequality in [`31034`](31034_witness_enclosure_inequality.md) | Proven | Proves $\Lambda(K_{\mathrm{wit}})\ge1$ throughout the strict domain. |
| Imported source draft in [`31031`](31031_original_residual_core_draft.md) | Reference only | Preserves provenance; its empirical observations are not used as proof. |

All dependencies used by this branch closure are proven. No statement about
the center class is used after CE0 supplies (1).
