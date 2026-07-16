# CE1/CE2, $N_+=1$, All Vd0: Exact Gap Closure

Status: Proven

## Theorem

Seven open unit equilateral triangles cannot cover the side-one hexagon $H$
when the center role is CE1 or CE2, all six vertex roles are Vd0, and
$N_+=1$.

## 1. The unique supercritical row

Suppose such a cover exists. Write $U_C,U_0,\dots,U_5$ for its open roles and
put $T_C=\overline{U_C}$ and $T_i=\overline{U_i}$. For each vertex role, let
$a_i,b_i$ be its actual maximal incoming and outgoing boundary reaches, as
defined in
[`../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md`](../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md).

The exactly-one-midpoint theorem
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md)
allows us to normalize

$$
T_C\cap\left\{M_0,\dots,M_5\right\}=\left\{M_0\right\}.
$$

Fix $i\ne0$. Since $M_i$ is covered but is not in $T_C$, diameter locality
leaves only $U_{i-1},U_i,U_{i+1}$ as possible covering vertex roles. If an
adjacent role contained $M_i$, convexity and its open neighborhood at its own
vertex would give positive-length support on the adjacent radial arm,
contrary to Vd0. Hence $M_i\in U_i\subset T_i$. The midpoint self-cover theorem
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md)
therefore gives

$$
a_i+b_i\le1,
\qquad i=1,\dots,5.
$$

Because $N_+=1$, it follows that $T_0$ is the unique supercritical row:

$$
a_0+b_0>1.
$$

## 2. Boundary gaps and open endpoints

On $e_{i,i+1}$, with coordinate measured from $V_i$, the adjacent roles
$U_i,U_{i+1}$ have traces

$$
[0,b_i)
\qquad\text{and}\qquad
(1-a_{i+1},1].
$$

Thus their uncovered set is

$$
G_i=
\begin{cases}
[b_i,1-a_{i+1}],&b_i\le1-a_{i+1},\\
\varnothing,&b_i>1-a_{i+1}.
\end{cases}
$$

We call every nonempty $G_i$ a V-gap. In particular, equality gives the
singleton gap $\{b_i\}$; it must not be discarded because the triangles are
open. A missing gap is equivalent to the strict handoff
$b_i>1-a_{i+1}$.

All reaches are positive, so a nonempty $G_i$ lies in the relative interior
of its edge. Vertex-role boundary locality, proved in
[`../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md),
shows that no other vertex role can cover a relative-interior point of this
edge. Hence every V-gap must lie in an open center trace. In particular, no
gap can occur on an edge outside the CE1 or CE2 center traces.

If $[s,t]$ is the corresponding maximal trace of $T_C$, then the $U_C$ trace
is $(s,t)$. Full coverage gives
$G_i\subset(s,t)$ and therefore the weak endpoint bounds

$$
b_i\ge s,
\qquad
a_{i+1}\ge1-t.
$$

These bounds remain valid for singleton gaps. The exact CE1 and CE2 trace
descriptions are proved in
[`2105_CE1_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md)
and
[`2106_CE2_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md).

## 3. CE1

Normalize the unique maximal closed center trace to

$$
T_C\cap e_{0,1}=[s,t].
$$

There are exactly two cases.

1. If this trace contains a V-gap, the exact five-map theorem
   [`4106_CE1_one_gap_five_map_completion.md`](4106_CE1_one_gap_five_map_completion.md)
   applies to the unique-row normalization above and the weak endpoint bounds
   from Section 2. It gives a contradiction, including when the gap is a
   singleton.
2. If it contains no V-gap, then no edge has a V-gap. The adjacent vertex
   traces therefore cover every boundary edge, with strict overlap at every
   handoff. Thus the six Vd0 roles cover $\partial H$. The center-independent
   all-boundary obstruction
   [`31035_center_independent_all_boundary_obstruction.md`](../../../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/31035_center_independent_all_boundary_obstruction.md)
   applies and gives a contradiction.

Hence CE1 is impossible.

## 4. CE2

Normalize the two maximal closed center traces to

$$
T_C\cap e_{5,0}=[x,u],
\qquad
T_C\cap e_{0,1}=[y,v],
$$

with both intervals measured from $V_0$. Each interval either contains a
V-gap or does not, so the following three cases are exhaustive.

1. Both intervals contain gaps. The exact two-gap theorem
   [`4102_CE2_two_gap_completion.md`](4102_CE2_two_gap_completion.md) gives a
   contradiction.
2. Exactly one interval contains a gap. The exact right-gap theorem and its
   reflected left-gap form in
   [`4107_CE2_one_gap_five_map_completion.md`](4107_CE2_one_gap_five_map_completion.md)
   give a contradiction in either orientation.
3. Neither interval contains a gap. As in CE1, no edge has a gap, so the six
   Vd0 roles cover $\partial H$. The center-independent theorem `31035`
   again gives a contradiction.

Hence CE2 is impossible.

## 5. Conclusion and the optional route

The CE1 split and the three CE2 cases exhaust all configurations under the
theorem's hypotheses, and every case is impossible. This proves the theorem.

The reduction
[`4104_all_boundary_transfer_to_310X.md`](4104_all_boundary_transfer_to_310X.md)
sends the no-gap case to the older conjectural inequality $F_6(a,b)\ge1$.
That route remains valid but optional: the proof above uses `31035` instead
and does not assume or prove the $F_6$ inequality.

$$
\Box
$$
