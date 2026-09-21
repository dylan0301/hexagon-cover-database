# [SUPPLIER] One missed midpoint determines the remaining cases

[\[MAIN\]](README.md) · [\[MIDPOINTS\]](MIDPOINTS.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Neighboring support and supplier.** The neighboring spokes for a V triangle at $V_i$ are $r_{i-1},r_{i+1}$. It has **positive adjacent support** if its closure meets one of those spokes in an interval of positive length. A **neighboring supplier of $M_j$** is specifically a triangle $U_i$ with $i=j-1$ or $j+1$ and $M_j\in U_i$. “Rescuer” means the same thing here. Supplying a midpoint implies positive support by openness; positive support alone does not imply supplying that midpoint. $N_{\rm sp}$ counts V triangles having positive adjacent support.
- **Type labels.** CE0, CE1, CE2 count the boundary edges met by $T_C$ in positive length; they do not count gaps. For a V triangle let $o$ count its vertices outside $H$, and $n$ its neighboring spokes met in positive length. Vd0 means $n=0$; Vd1 means $(o,n)=(1,1)$; Vd2 means $(1,2)$; T3-like means $(2,1)$. The names are labels, not additional assumptions.
- **Indices used in the case split.** $k$ is the index of the unique midpoint $M_k$ contained by $U_C$ when a gap exists. After the count reduction, $\sigma$ is the unique supercritical index. When $\sigma\ne k$, $\tau$ names the unique neighboring supplier, so $\tau\in\{\sigma-1,\sigma+1\}$ and $M_\sigma\in U_\tau$. “At $k$” means based at vertex $V_k$, not physically located at midpoint $M_k$.
- **Paths and boundary handoffs.** A path is an ordered consecutive group of V triangles, connected by the hexagon edges between their vertices. On a gap-free connecting edge their open traces overlap: $B_i+A_{i+1}>1$. A **handoff** is a point selected inside this overlap, covered by both triangles. **Path monotonicity** means the increasing $A_i$ and decreasing $B_i$ obtained by combining these overlaps with nonsupercriticality. An edge is **center-free** when $U_C$ covers no point in its relative interior (the edge with its endpoints removed).

**Input:** a skeleton cover with at least one gap. **Output:** one supercritical role, at most one positive-support role, and the exhaustive placement routing.

## A concrete supplier example

If $T_C$ and $T_1$ both miss $M_1$, but $M_1\in U_0$, then **$U_0$ supplies $M_1$**. It is a neighboring supplier because $V_0$ and $V_1$ are consecutive hexagon vertices. The point lies on $r_1$, not on $U_0$'s own spoke $r_0$. Merely meeting $r_1$ near $O$ would not make $U_0$ a supplier unless it actually contained $M_1$.

## Tree

- **Identify the unique center midpoint.**
    - By [\[C-MIDPOINT\]](C-MIDPOINT.md), $M_k\in U_C$ and every other midpoint is outside $T_C$.
- **Use the count bound.**
    - [\[LENGTH\]](LENGTH.md) gives $N_++N_{\rm sp}\le2$.
    - [\[N0\]](N0.md) gives $N_+\ge1$.
    - Positive-support roles and supercritical roles are disjoint.
- **Exclude $N_+\ge2$.**
    - Choose a supercritical index $\sigma\ne k$.
    - Its role misses $M_\sigma$ — [\[SELF-MIDPOINT\]](SELF-MIDPOINT.md).
    - The center also misses $M_\sigma$ — [\[C-MIDPOINT\]](C-MIDPOINT.md).
    - Locality forces an adjacent open role to cover $M_\sigma$.
    - Open containment makes that role a positive-support role, distinct from all supercritical roles.
    - Thus $N_++N_{\rm sp}\ge3$, contrary to the count bound.
- **Conclude $N_+=1$ and $N_{\rm sp}\le1$.**
    - Let $\sigma$ denote the unique supercritical index.
    - If $\sigma=k$, apply [\[BC\]](BC.md).
    - Otherwise a neighbor $U_\tau$ must cover $M_\sigma$.
        - It is a positive-support role.
        - The count bound makes it unique.
        - In particular $\tau\in\{\sigma-1,\sigma+1\}$.
- **Classify only that unique supplier.**
    - **T3-like.**
        - It misses its own midpoint $M_\tau$ — [\[T3-MIDPOINT\]](T3-MIDPOINT.md).
        - If $\tau\ne k$, the center misses $M_\tau$ too.
        - Any covering neighbor would be a second positive-support role, impossible.
        - Hence $\tau=k$; apply [\[D\]](D.md).
    - **Vd1 at $k$.**
        - Apply [\[D\]](D.md) using the Vd1 local ratio input.
    - **Vd1 away from $k$.**
        - Both $\sigma$ and $\tau$ differ from $k$.
        - Their shared boundary edge is not incident with $V_k$.
        - All possible center traces are incident with $V_k$, so this edge is center-free.
        - Apply [\[REPLACEMENT\]](REPLACEMENT.md), then [\[N0\]](N0.md).
    - **Vd2.**
        - Covering the neighboring midpoint gives the stronger cap used in [\[PERIMETER\]](PERIMETER.md).
- **These supplier cases are exhaustive.**
    - No additional global six-triangle type grid is needed.

---

**Proof sources:** [2613](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2613_midpoint_supplier_reduction.md) · [2531](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md) · [2614](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2614_two_vertex_replacement.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
