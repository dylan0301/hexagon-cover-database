# [REPLACE-CALC] Two charts and five strict preservation margins

[\[MAIN\]](../README.md) · [\[REPLACEMENT\]](../REPLACEMENT.md) · [\[NOTATION\]](../NOTATION.md) · [\[USE\]](../USING.md) · [\[GLOSSARY\]](../GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Neighboring support and supplier.** The neighboring spokes for a V triangle at $V_i$ are $r_{i-1},r_{i+1}$. It has **positive adjacent support** if its closure meets one of those spokes in an interval of positive length. A **neighboring supplier of $M_j$** is specifically a triangle $U_i$ with $i=j-1$ or $j+1$ and $M_j\in U_i$. “Rescuer” means the same thing here. Supplying a midpoint implies positive support by openness; positive support alone does not imply supplying that midpoint. $N_{\rm sp}$ counts V triangles having positive adjacent support.
- **Type labels.** CE0, CE1, CE2 count the boundary edges met by $T_C$ in positive length; they do not count gaps. For a V triangle let $o$ count its vertices outside $H$, and $n$ its neighboring spokes met in positive length. Vd0 means $n=0$; Vd1 means $(o,n)=(1,1)$; Vd2 means $(1,2)$; T3-like means $(2,1)$. The names are labels, not additional assumptions.
- **Paths and boundary handoffs.** A path is an ordered consecutive group of V triangles, connected by the hexagon edges between their vertices. On a gap-free connecting edge their open traces overlap: $B_i+A_{i+1}>1$. A **handoff** is a point selected inside this overlap, covered by both triangles. **Path monotonicity** means the increasing $A_i$ and decreasing $B_i$ obtained by combining these overlaps with nonsupercriticality. An edge is **center-free** when $U_C$ covers no point in its relative interior (the edge with its endpoints removed).
- **Local notation.** A chart is a vertex-based coordinate system. Here the theorem calls certain actual preservation requirements $a,c,B,r$; they are its own declared scalar variables, not the generic freely selected $a_i,b_i$. The two adjacent charts are $X_0(x,y)=V_0+x(V_5-V_0)+y(V_1-V_0)$ and $X_1(x,y)=V_1+x(V_0-V_1)+y(V_2-V_1)$. A template is an explicitly defined triangle in those coordinates. A strict margin is a positive difference that must survive the small displacement $\varepsilon$.

**Below the oral cutoff.** Source 2614 supplies a scalar replacement theorem; source 4144 verifies that the away Vd1 placement meets its inputs. Return to [\[REPLACEMENT\]](../REPLACEMENT.md).

## Tree

- **Establish the scalar inputs.**
    - In the two adjacent vertex charts, let $a,c$ be the first role's incoming boundary and own-radial reaches to preserve.
    - Let $B$ be the second role's outgoing boundary reach, and $r$ the radial demand needed to overlap the unchanged center.
    - Verify $a<1/2$, $a+c<1$, $a+B<1$, and $r<\max\{1-a,1-B\}$.
    - Placement-specific verification: source [4144](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4144_new_two_chart_replacement_and_router.md).
- **Choose strict parameters — source [2614](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2614_two_vertex_replacement.md).**
    - Choose $a<p_2<1-B$ with $\max\{p_2,1-p_2\}>r$.
    - Choose $a<p_1<\min\{p_2,1/2,1-c\}$.
    - Choose $\varepsilon>0$ smaller than all five quantities:
        - $p_1-a$.
        - $p_2-p_1$.
        - $1-B-p_2$.
        - $1-p_1-c$.
        - $\max\{p_2,1-p_2\}-r$.
- **Use the correct template in each vertex chart.**
    - For $p\le1/2$, the minus template is $\operatorname{int}\operatorname{conv}\{(0,1-p),(1,1-p),(0,-p)\}+(-\varepsilon,0)$.
    - For $p>1/2$, the plus template is $\operatorname{int}\operatorname{conv}\{(p,0),(p,1),(p-1,0)\}+(0,-\varepsilon)$.
    - Here $\operatorname{int}$ removes the sides and vertices, $\operatorname{conv}$ means convex hull, and adding a vector translates every point. Use the minus template at $p_1$ in $X_0$ and the appropriate template at $p_2$ in $X_1$.
    - The minus template has incoming, outgoing, and own-radial reaches $(p-\varepsilon,1-p,1-p)$.
    - The plus template has reaches $(p,1-p-\varepsilon,p)$.
    - Both have actual boundary sum $1-\varepsilon$ and no positive adjacent support.
    - The two physical vertex charts are different; their axes must not be identified.
- **Check the five affected skeleton pieces.**
    - Incoming boundary and own spoke at the first vertex.
    - Shared edge: the two new reaches sum to at least $1-p_1+p_2-\varepsilon>1$.
    - Outgoing boundary and own spoke at the second vertex.
    - Every other skeleton piece is unchanged.
- **Read the conclusion.**
    - With four untouched nonsupercritical roles, the output has actual $N_+'=0$.
    - The output gap rank may change; full interior coverage is not claimed.
    - Finish with [\[N0\]](../N0.md).

---

**Proof sources:** [2614](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2614_two_vertex_replacement.md) · [4144](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4144_new_two_chart_replacement_and_router.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](../README.md) Return to the main tree.
