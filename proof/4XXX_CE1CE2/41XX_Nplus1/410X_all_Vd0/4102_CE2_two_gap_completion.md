# CE2 Two-Gap Completion for $N_+=1$, All Vd0

Status: Proven

This note proves the CE2 two-gap subcase of `410X`. The exact endpoint
inequality proved for `401X` applies unchanged because the exceptional
supercritical row is $T_0$, while the endpoint and remainder rows used below
are $T_1,\dots,T_5$.

## 1. Hypotheses and normalization

Begin with the full side-one hexagon $H$ covered by seven open unit
equilateral triangles. Assume the center role is CE2, every vertex role is
Vd0, and

$$
N_+=1.
$$

Normalize the unique center midpoint to $M_0$. The exactly-one-midpoint
theorem in
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md)
gives

$$
T_C\cap\left\{M_0,\dots,M_5\right\}=\left\{M_0\right\}.
$$

For $i\ne0$, diameter locality leaves only $T_{i-1},T_i,T_{i+1}$ as
possible vertex roles containing $M_i$. An original open adjacent role
$T_{i-1}$ or $T_{i+1}$ containing $M_i$ would have positive-length support
on the adjacent radial arm, contrary to the Vd0 definition in
[`../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).
Thus $M_i\in T_i$. The midpoint self-cover theorem in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md)
then gives

$$
a_i+b_i\le1,
\qquad i=1,\dots,5.
$$

Since $N_+=1$, $T_0$ is the unique supercritical row.

Use the exact CE2 intervals from
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md):

$$
T_C\cap e_{5,0}=[x,u],
\qquad
T_C\cap e_{0,1}=[y,v],
$$

where both parameters are measured from $V_0$. Assume that both intervals
contain V-gaps.

## 2. Far-end inputs

Put

$$
S_0=x+y,
\qquad
R=\frac{x}{S_0},
$$

and

$$
p=1-u,
\qquad
q=1-v.
$$

The left gap is an interval

$$
(a_0,1-b_5)\subset[x,u],
$$

so

$$
b_5\ge1-u=p.
$$

The right gap is an interval

$$
(b_0,1-a_1)\subset[y,v],
$$

so

$$
a_1\ge1-v=q.
$$

The exact radial formulas in `2106` give

$$
c_5=1-\frac{uS_0-x}{y}
=\frac{p}{1-R},
$$

and

$$
c_1=1-\frac{vS_0-y}{x}
=\frac qR.
$$

Let

$$
\widehat B_c(a)=\min\left\{B_c(a),1-a\right\}
$$

be the proved safe upper map for a nonsupercritical Vd0 row. Reflection of
the local coordinates for $T_5$ and the two endpoint demands above give

$$
B_5\le\widehat B_{p/(1-R)}(p),
\qquad
B_1\le\widehat B_{q/R}(q),
$$

where $B_5$ and $B_1$ denote the reaches of $T_5$ and $T_1$ on
$e_{4,5}$ and $e_{1,2}$, respectively.

The safe-map inequality is proved in
[`2011_capped_demand_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md).

## 3. Import of the exact endpoint theorem

The exact reduction in
[`../../40XX_Nplus0/401X_all_Vd0_boundary_loss/401c_CE2_remaining_obligations.md`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss/401c_CE2_remaining_obligations.md)
uses only:

- the strict CE2 endpoint domain from `2106`;
- the two far-end inputs $p$ and $q$;
- nonsupercriticality of $T_1$ and $T_5$; and
- the exact four-label partition of $\widehat B$.

It does not use $a_0+b_0\le1$. In its normalized variables

$$
w=1-R,
\qquad
r=R,
\qquad
K=\sqrt{1-wr},
$$

$$
p=w\alpha,
\qquad
q=r\beta,
$$

the two strict endpoint inequalities are consequences of $x<u$, $y<v$, and
the CE2 coupling alone. The complete selected-branch theorem in
[`../../40XX_Nplus0/401X_all_Vd0_boundary_loss/401e_CE2_two_gap_completion.md`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss/401e_CE2_two_gap_completion.md)
therefore applies verbatim and proves

$$
\boxed{
\widehat B_{p/(1-R)}(p)
+
\widehat B_{q/R}(q)
<1.
}
$$

The exceptional row $T_0$ does not occur in this inequality.

## 4. Boundary contradiction

The center role has no positive-length boundary trace on

$$
e_{1,2}\cup e_{2,3}\cup e_{3,4}\cup e_{4,5}.
$$

Isolated contacts do not affect boundary length. By Vd0 and diameter
boundary locality, no non-endpoint vertex role has positive-length support on
a boundary edge. After the endpoint contributions of $T_1$ and $T_5$, the
portion of these
four edges left for $T_2,T_3,T_4$ has length at least

$$
(1-B_1)+1+1+(1-B_5)
=4-(B_1+B_5)>3.
$$

But the three rows are nonsupercritical, so their total boundary contribution
is at most

$$
(a_2+b_2)+(a_3+b_3)+(a_4+b_4)\le3.
$$

This is a contradiction. Hence an all-Vd0 CE2, $N_+=1$ system cannot have a
V-gap in both center intervals.

$$
\Box
$$

## 5. Scope

The proof starts from the original full-$H$ cover and uses only its necessary
boundary and radial consequences. It does not replace $T_0$ and therefore
does not need to preserve the interior cover under the skeleton replacement
from `2104`. The simultaneous replacement remains a valid skeleton theorem,
but it is not a dependency of this completion.
