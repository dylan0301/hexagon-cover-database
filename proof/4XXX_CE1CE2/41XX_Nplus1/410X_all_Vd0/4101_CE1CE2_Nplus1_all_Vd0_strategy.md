# CE1/CE2, $N_+=1$, All Vd0: Exact Gap Closure

Status: Proven

This note gives the complete case split for `410X`. Every state containing a
V-gap is excluded by the exact gap certificates in this package. In the
remaining no-gap state, the six Vd0 roles cover all of $\partial H$, so the
proved center-independent residual-core theorem `31035` applies. Thus every
case in `410X` is impossible.

## Package ledger

| File | Status | Role |
|---|---|---|
| [`4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](4101_CE1CE2_Nplus1_all_Vd0_strategy.md) | Proven | Hypotheses, exhaustive gap split, and assembly of all terminal contradictions. |
| [`4102_CE2_two_gap_completion.md`](4102_CE2_two_gap_completion.md) | Proven | Excludes the CE2 state in which both center intervals contain V-gaps. |
| [`4104_all_boundary_transfer_to_310X.md`](4104_all_boundary_transfer_to_310X.md) | Reduction | Optional transfer of the no-gap state to the still-open six-point target `4104-F`; not used in the branch closure. |
| [`4106_CE1_one_gap_five_map_completion.md`](4106_CE1_one_gap_five_map_completion.md) | Proven | Excludes the CE1 one-gap state by an exact five-map inequality and Bernstein certificate. |
| [`4107_CE2_one_gap_five_map_completion.md`](4107_CE2_one_gap_five_map_completion.md) | Proven | Excludes both reflected CE2 one-gap states. |
| [`4108_ce1_terminal_verifier.py`](4108_ce1_terminal_verifier.py) | Experiment | Reconstructs the exact rational Bernstein tensors used in `4106`. |
| [`../../../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/31035_center_independent_all_boundary_obstruction.md`](../../../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/31035_center_independent_all_boundary_obstruction.md) | Proven | Excludes every no-gap state from full Vd0 boundary coverage and exactly one supercritical actual row. |

## 1. Hypotheses and the unique supercritical row

Assume that seven open unit equilateral triangles cover the full side-one
hexagon $H$.  Choose an open center role $T_C$ containing $O$ and six Vd0
vertex roles $T_0,\dots,T_5$.  Assume

$$
T_C\text{ is CE1 or CE2},
\qquad
N_+=1.
$$

Here $(a_i,b_i)$ are the actual maximal incoming and outgoing boundary
reaches of $T_i$, in the sense of
[`../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md`](../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md).

For compact local calculations, replace each open role by its associated
closed unit triangle. This is an immediate containment relaxation; the strict
center domains used below still come from the original open center role.

The exactly-one-midpoint theorem
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md)
allows the normalization

$$
T_C\cap\{M_0,\dots,M_5\}=\{M_0\}.
$$

For $i\ne0$, radial locality therefore puts $M_i$ in $T_i$.  The midpoint
self-cover theorem
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md)
gives

$$
a_i+b_i\le1,
\qquad i\ne0.
$$

Since $N_+=1$, the unique supercritical row is $T_0$.

Let $d_i$ be the center role's radial exit toward $V_i$ and put

$$
c_i=1-d_i.
$$

Convexity of radial intersections shows that the actual radial reach of
$T_i$ is at least $c_i$.  Lowering the actual demand to $c_i$ enlarges the
feasible row set, so it is a valid relaxation.

For every nonsupercritical row $i\ne0$, define

$$
F_i(a)=\min\{B_{c_i}(a),1-a\},
\qquad
G_i(a)=1-F_i(a).
$$

The exact map $B_c$ is proved in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md),
and the capped relaxation and monotonicity of $G_i$ are proved in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md).

## 2. Boundary gaps

On $e_{i,i+1}$, measured from $V_i$, the two adjacent open vertex roles have
traces

$$
[0,b_i)
\qquad\text{and}\qquad
(1-a_{i+1},1].
$$

Consequently their uncovered set is

$$
\boxed{[b_i,1-a_{i+1}]}
$$

when $b_i\le1-a_{i+1}$, and is empty when
$b_i>1-a_{i+1}$.  We call every nonempty such set a V-gap.  This convention
includes the singleton equality case $b_i=1-a_{i+1}$, which cannot be
discarded for open triangles.

The interval notation $[s,t]$ used for a center trace means the trace of the
closed triangle associated with the open center role; the open role contains
the relative interior $(s,t)$.  Full boundary coverage puts every V-gap in
that open center trace.  In particular, if the closed center interval
$[s,t]$ contains the gap, then

$$
b_i\ge s,
\qquad
a_{i+1}\ge1-t.
$$

The center formulas and all of their strict domains are proved in
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md)
and
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md).
The gap certificates `4102`, `4106`, and `4107` use only these weak endpoint
bounds, so they include singleton V-gaps.

## 3. Exhaustive CE1 split

A CE1 role has one maximal closed boundary trace, normalized to

$$
\overline{T_C}\cap e_{0,1}=[s,t].
$$

- If the trace contains a V-gap, including a singleton gap, `4106` propagates
  the five nonsupercritical capped maps from $1-t$ and proves that the
  resulting lower bound for $a_0$ is strictly greater than the exact upper
  bound allowed by the same $T_0$ with $b_0\ge s$.  This is a contradiction.
- If it contains no V-gap, the two adjacent open vertex traces cover their
  whole edge and overlap strictly at their handoff. Outside the center edge,
  the original full cover and Vd0 boundary locality already force coverage by
  the vertex roles. Hence the six vertex roles cover all of $\partial H$, and
  `31035` applies.

These two alternatives are exhaustive.

## 4. Exhaustive CE2 split

Normalize the two maximal closed center traces as

$$
\overline{T_C}\cap e_{5,0}=[x,u],
\qquad
\overline{T_C}\cap e_{0,1}=[y,v],
$$

with both coordinates measured from $V_0$.  Each trace either contains a
V-gap, possibly a singleton, or does not, so exactly one of the following
occurs.

1. Both contain gaps.  `4102` proves this impossible by the strict
   two-endpoint capped-loss inequality.
2. Exactly one contains a gap.  `4107` proves the right-gap five-map
   inequality on the full strict CE2 domain; reflection across the axis
   through $V_0$ gives the left-gap inequality.  Both orientations are
   impossible.
3. Neither contains a gap. The adjacent vertex roles cover both center edges
   and, by the same locality argument as in CE1, all of $\partial H$.
   Therefore `31035` applies.

Thus every CE2 state is routed either to a proved gap certificate or to the
proved no-gap obstruction.

## 5. No-gap closure

In the remaining no-gap state, the six vertex roles cover $\partial H$.
The original seven triangles cover all of $H$, all six vertex roles are Vd0,
and $N_+=1$ means that exactly one actual maximal boundary row is
supercritical. Therefore every hypothesis of
[`31035_center_independent_all_boundary_obstruction.md`](../../../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/31035_center_independent_all_boundary_obstruction.md)
holds. That theorem gives an immediate contradiction.

More explicitly, its strict handoffs produce parameters satisfying

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1.
$$

The theorem then forces the compact residual-core witness

$$
K_{\mathrm{wit}}(a,b)
\subseteq T_C
$$

while the proven enclosure theorem gives

$$
\Lambda\left(K_{\mathrm{wit}}(a,b)\right)\ge1.
$$

A compact subset of the open unit equilateral triangle $T_C$ has enclosing
side strictly below $1$, which is impossible.

The optional reduction in `4104` still produces the older conjectural target
$F_6(a,b)\ge1$. The argument above does not prove that inequality; it bypasses
it with $K_{\mathrm{wit}}$. Hence the `3101X` six-point problem remains open
as an optional route, but it is not a dependency of `410X`.

The CE1 one-gap/no-gap alternatives and the three CE2 gap-count alternatives
are exhaustive. Since every terminal case is now covered by a `Proven`
source, the CE1/CE2, $N_+=1$, all-Vd0 branch is proved impossible.
