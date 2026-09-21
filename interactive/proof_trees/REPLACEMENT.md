# [REPLACEMENT] Remove the supercritical role while preserving the skeleton

[\[MAIN\]](README.md) · [\[SUPPLIER\]](SUPPLIER.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Neighboring support and supplier.** The neighboring spokes for a V triangle at $V_i$ are $r_{i-1},r_{i+1}$. It has **positive adjacent support** if its closure meets one of those spokes in an interval of positive length. A **neighboring supplier of $M_j$** is specifically a triangle $U_i$ with $i=j-1$ or $j+1$ and $M_j\in U_i$. “Rescuer” means the same thing here. Supplying a midpoint implies positive support by openness; positive support alone does not imply supplying that midpoint. $N_{\rm sp}$ counts V triangles having positive adjacent support.
- **Type labels.** CE0, CE1, CE2 count the boundary edges met by $T_C$ in positive length; they do not count gaps. For a V triangle let $o$ count its vertices outside $H$, and $n$ its neighboring spokes met in positive length. Vd0 means $n=0$; Vd1 means $(o,n)=(1,1)$; Vd2 means $(1,2)$; T3-like means $(2,1)$. The names are labels, not additional assumptions.
- **Indices used in the case split.** $k$ is the index of the unique midpoint $M_k$ contained by $U_C$ when a gap exists. After the count reduction, $\sigma$ is the unique supercritical index. When $\sigma\ne k$, $\tau$ names the unique neighboring supplier, so $\tau\in\{\sigma-1,\sigma+1\}$ and $M_\sigma\in U_\tau$. “At $k$” means based at vertex $V_k$, not physically located at midpoint $M_k$.
- **Paths and boundary handoffs.** A path is an ordered consecutive group of V triangles, connected by the hexagon edges between their vertices. On a gap-free connecting edge their open traces overlap: $B_i+A_{i+1}>1$. A **handoff** is a point selected inside this overlap, covered by both triangles. **Path monotonicity** means the increasing $A_i$ and decreasing $B_i$ obtained by combining these overlaps with nonsupercriticality. An edge is **center-free** when $U_C$ covers no point in its relative interior (the edge with its endpoints removed).
- **Replacement and margins.** A replacement changes two open V triangles and keeps the C triangle and four other V triangles fixed. A strict margin is positive excess in an inequality, large enough to keep a required point inside an open triangle. A prime, as in $N_+'$, refers to the new configuration. “Gap rank” means the number of edges with gaps, not a linear-algebra rank.

**Input:** a Vd1 supplier $T_\tau$ away from the center midpoint index $k$, adjacent to the uniquely supercritical $T_\sigma$. **Output:** another skeleton cover with actual $N_+'=0$.

## Tree

- **Identify the center-free shared edge.**
    - Both $\tau$ and $\sigma$ differ from $k$.
    - Their shared edge is not incident with $V_k$.
    - All possible center boundary traces are incident with $V_k$ — [\[C-MIDPOINT\]](C-MIDPOINT.md).
    - Hence this shared edge receives no center coverage.
- **Keep the center and four other vertex roles fixed.**
    - Only the supplier and supercritical roles are replaced.
    - Use two separate local vertex charts; do not identify their coordinates.
- **Establish the scalar replacement inputs.**
    - The local geometry must give enough boundary and radial slack.
    - **CALCULATION LEAF:** the Vd1 adapter and scalar inequalities — [\[REPLACE-CALC\]](details/replacement-margins.md).
- **Construct two nonsupercritical open unit replacements.**
    - Preserve the incoming boundary reach of the first role.
    - Preserve its own radial reach.
    - Make the two new traces overlap strictly on their shared edge.
    - Preserve the outgoing boundary reach of the second role.
    - Preserve its overlap with the unchanged center on the second spoke.
    - **CALCULATION LEAF:** the two templates and five strict margins — [\[REPLACE-CALC\]](details/replacement-margins.md).
- **Read the output using actual reaches.**
    - Both replaced roles have actual boundary sum below $1$ and no positive adjacent support.
    - The four unchanged roles are already nonsupercritical.
    - Thus the new skeleton cover has $N_+'=0$.
- **Apply N0** — [\[N0\]](N0.md).
    - N0 prohibits every such skeleton cover, regardless of the output gap rank.
    - Contradiction.

## What is not preserved

Neither full interior coverage nor the number of gap edges is claimed to be preserved. Neither is needed. This branch must end with N0, not with the full-interior nine-point theorem F.

---

**Proof sources:** [2613](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2613_midpoint_supplier_reduction.md) · [2614](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2614_two_vertex_replacement.md) · [4144](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4144_new_two_chart_replacement_and_router.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
