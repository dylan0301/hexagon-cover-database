# Main Theorem

Status: Proven

## Theorem

The regular side-$1$ hexagon $H$ cannot be covered by seven open unit
equilateral triangles. Equivalently, for every $L>1$, the regular side-$L$
hexagon $H_L$ cannot be covered by seven closed unit equilateral triangles.

The equivalence is proved in
[`1003`](../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md).

## Proof

Assume that seven open unit equilateral triangles cover $H$. Denote the
original open roles by

$$
U_C,U_0,\ldots,U_5,
$$

where $O\in U_C$ and $V_i\in U_i$, and put

$$
T_C=\overline{U_C},
\qquad
T_i=\overline{U_i}.
$$

The seven distinguished points $O,V_0,\ldots,V_5$ are pairwise at distance at
least one, while two points in one open unit triangle are at distance strictly
below one. Hence the seven roles are distinct. Apply the exact-trace
normalization and classifications in
[`1101`](../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md) and
[`1201`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md). The
closed C triangle is exactly one of CE0, CE1, CE2, and each normalized closed
V triangle is exactly one of Vd0, Vd1, Vd2, and T3-like. We retain the open
roles whenever openness or endpoint ownership is used.

Let $(A_i,B_i,C_i)$ be the actual maximal reaches of $T_i$ and define

$$
N_+=\left|\{i:A_i+B_i>1\}\right|.
$$

Let $d$ count Vd1/Vd2 roles, let $t$ count T3-like roles, and put
$N_{\rm sp}=d+t$. A boundary gap is the nonempty closed complement between
the two incident open V traces on one edge; equality of their closed endpoints
therefore gives a singleton gap. Let $N_{\rm gap}$ be the number of gap edges.
Boundary locality and openness give

$$
N_{\rm gap}=0
\quad\Longleftrightarrow\quad
U_0,\ldots,U_5\text{ cover }\partial H.
\tag{1}
$$

Every gap belongs to the open C role, so the center classification gives
$N_{\rm gap}=0$ in CE0, at most one in CE1, and at most two in CE2. The strict
handoff theorem
[`1214`](../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
passes from the actual reaches to strict selected lower bounds without changing
the exact-one supercritical index and, when $N_+\ge2$, permits a selection with
at least two selected supercritical roles.

The proof uses the area interface
[`2400`](../2XXX_geometric_lemmas/24XX_area_loss/2400_zero_gap_area_loss_interface.md),
the length interface
[`2531`](../2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md),
and the finite-witness interface
[`2610`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md).
The shared neighboring bound has the direct proof `2008b`; the conditional
CE1 return and exact zero-gap certificate remain local dependencies.

By N0 in
[`2612`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md),
Theorem 7.1, every skeleton cover has $N_+\ge1$. N0 uses B/C and does not
use the alternative complementary-gap family A.

### Zero boundary gaps

The six V roles cover the perimeter by (1). If $N_+=1$, the type-independent
nine-point terminal F in `2610` applies. If $N_+\ge2$, the multiple-ascent
area theorem `2400` applies. Neither route requires a center-type or V-type
split. Both exclude coverage of the full hexagon.

### Nonzero boundary gaps

Normalize the C triangle's unique midpoint to $M_k$. The count and
midpoint-supplier reduction in
[`2613`](../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2613_midpoint_supplier_reduction.md)
uses N0 and the skeleton budget to give $N_+=1$ and $N_{\rm sp}\le1$.
Write $\sigma$ for the unique supercritical index.

If $\sigma=k$, apply the center-aligned path theorem in `2612`, Theorem 7.0:
C for one gap and B for two. Its five nonsupercritical path roles need no
V-type refinement.

Otherwise `2613` gives a unique adjacent positive-support supplier $T_\tau$
of $M_\sigma$. A T3-like supplier must have $\tau=k$ and is excluded by
the local ratio adapter
[`4130_new`](../4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md)
followed by D. A Vd2 supplier is excluded by the common CE1/CE2 perimeter
row P3 in `2531`. A Vd1 supplier at $k$ uses
[`4143_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4143_new_Vd1_rescuer_finite_enclosure.md)
and the same D theorem. A Vd1 supplier away from $k$ has a center-free
shared edge; its local margins in
[`4144_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4144_new_two_chart_replacement_and_router.md)
permit the two-vertex replacement, preserving the skeleton and producing
actual $N_+'=0$, contrary to N0.

These cases exhaust the unique supplier's classified type and position.
All hypothetical covers are impossible. The scaling equivalence in `1003`
gives the expanded closed formulation. $\square$
