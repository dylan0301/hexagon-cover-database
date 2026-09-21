# [BC-CALC] BC calculation leaves

[\[MAIN\]](../README.md) · [\[BC\]](../BC.md) · [\[NOTATION\]](../NOTATION.md) · [\[USE\]](../USING.md) · [\[GLOSSARY\]](../GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Enclosure language.** A **witness** is a chosen point used to contradict the cover. **Forced into $U_C$** means the cover and previously stated geometry imply that membership. A **candidate** is any other open unit equilateral triangle tested against the same fixed witnesses; it need not complete a cover with the old V triangles. $\operatorname{conv}(K)$ is the convex hull, the set of all convex combinations of points of $K$. For a nonempty compact set $K$ (closed and bounded here), $\Lambda(K)$ is the least side length of a closed equilateral triangle containing it. Thus $K\subset U_C$ gives $\Lambda(K)<1$ by shrinking its three sides slightly.
- **Total radial frontier.** Put $Z_i(c)=(1-c)V_i$. For $j=i-1,i+1$, let $u_{j\to i}$ be the largest $c$ of a positive-length trace $T_j\cap r_i$, or $0$ when that trace is absent. Define $\gamma_i=\max\{C_i,u_{i-1\to i},u_{i+1\to i}\}$ and $\widehat P_i=(1-\gamma_i)V_i$. This is the endpoint closest to $O$ after accounting for all V triangles that can reach that spoke, not just $T_i$.
- **Capacity.** $c_{\max}(p,q)$ is the largest own-spoke reach possible for a closed unit equilateral triangle that contains a hexagon vertex and reaches at least $p,q$ along its two incident edges. More formally, in coordinates based at that vertex, choose unit vectors $u,v$ meeting at $120^\circ$; it is the largest $c$ such that $\{0,pu,qv,c(u+v)\}$ fits in a closed unit equilateral triangle. $C_+(p,q),C_-(p,q)$ are the corresponding maximal reaches on the two neighboring spokes, measured from each target spoke's vertex toward $O$. A **capacity bound** is an upper bound on one of these reaches.
- **Paths and boundary handoffs.** A path is an ordered consecutive group of V triangles, connected by the hexagon edges between their vertices. On a gap-free connecting edge their open traces overlap: $B_i+A_{i+1}>1$. A **handoff** is a point selected inside this overlap, covered by both triangles. **Path monotonicity** means the increasing $A_i$ and decreasing $B_i$ obtained by combining these overlaps with nonsupercriticality. An edge is **center-free** when $U_C$ covers no point in its relative interior (the edge with its endpoints removed).
- **Type labels.** CE0, CE1, CE2 count the boundary edges met by $T_C$ in positive length; they do not count gaps. For a V triangle let $o$ count its vertices outside $H$, and $n$ its neighboring spokes met in positive length. Vd0 means $n=0$; Vd1 means $(o,n)=(1,1)$; Vd2 means $(1,2)$; T3-like means $(2,1)$. The names are labels, not additional assumptions.
- **Normalized input and terminology.** The selected gap is on $e_{0,1}$, $M_0\in U_C$, and $T_1,\ldots,T_5$ are nonsupercritical; edges $e_{1,2},\ldots,e_{4,5}$ have no gaps. A tail premise is the bound at the last V triangle $T_5$ on this path. A return transfers inequalities along the path until they contradict the starting boundary sum. Recovering an own demand means proving it must be supplied by $T_i$, after both neighboring possibilities have been bounded away.

**Below the oral cutoff.** This page is a guide to the exact written obligations, not a reproduction of all derivations. Return to [\[BC\]](../BC.md) for the geometric tree.

## Tree

- **Shared-anchor transfer — source [2018b](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018b_shared_gap_anchor_transfer.md).**
    - Input: original perimeter coverage and the selected gap placement.
    - Output used here: $B_5>B_0/2$. The source proves a sharper intermediate capacity bound, but this explicit inequality is the only tail input used by BC.
    - This supplies an explicit hypothesis of the pure BC enclosure theorem before introducing a candidate.
- **Neighboring-demand recovery — sources [2008b](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008b_direct_neighbor_domination.md) and [2612](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md).**
    - For $p,q\ge0$ with $p+q\le1$, $C_+(p,q),C_-(p,q)\le1-\min(p,q)\le c_{\max}(p,q)$.
    - Candidate containment of a total frontier gives a demand on a maximum.
    - Exclude both neighboring contributors before assigning the demand to the own role.
- **CE2 candidate thresholds — source [2612](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md), Sections 5.2 and 8.**
    - For a candidate $U'$ containing the fixed witnesses and $O$, let $d'_i$ be the largest $t$ with $tV_i\in\overline{U'}$. The CE2 inequality proves $\gamma_2<1-d'_2$ or $\gamma_4<1-d'_4$; each contradicts containment of the corresponding fixed frontier.
    - At least one of the fixed frontiers on $r_2,r_4$ lies beyond the candidate exit.
- **CE1 candidate return — sources [2612](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md) and [4102](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4102_new_CE1_direct_radial_certificate.md).**
    - First recover the own demands on $r_4,r_3$.
    - Use only the first return step to obtain the lower tail demand on $B_3$.
    - That demand excludes neighboring supply on $r_2$; recover the third own demand.
    - Only now invoke the full conditional selected return.
    - Preserve all selected-branch hypotheses; do not apply the full return to prove one of its own assumptions.

---

**Proof sources:** [2018b](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018b_shared_gap_anchor_transfer.md) · [2008b](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008b_direct_neighbor_domination.md) · [2612](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md) · [4102](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4102_new_CE1_direct_radial_certificate.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](../README.md) Return to the main tree.
