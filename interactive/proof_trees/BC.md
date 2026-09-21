# [BC] The six-point selected-gap obstruction

[\[MAIN\]](README.md) · [\[N0\]](N0.md) · [\[SUPPLIER\]](SUPPLIER.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Enclosure language.** A **witness** is a chosen point used to contradict the cover. **Forced into $U_C$** means the cover and previously stated geometry imply that membership. A **candidate** is any other open unit equilateral triangle tested against the same fixed witnesses; it need not complete a cover with the old V triangles. $\operatorname{conv}(K)$ is the convex hull, the set of all convex combinations of points of $K$. For a nonempty compact set $K$ (closed and bounded here), $\Lambda(K)$ is the least side length of a closed equilateral triangle containing it. Thus $K\subset U_C$ gives $\Lambda(K)<1$ by shrinking its three sides slightly.
- **Total radial frontier.** Put $Z_i(c)=(1-c)V_i$. For $j=i-1,i+1$, let $u_{j\to i}$ be the largest $c$ of a positive-length trace $T_j\cap r_i$, or $0$ when that trace is absent. Define $\gamma_i=\max\{C_i,u_{i-1\to i},u_{i+1\to i}\}$ and $\widehat P_i=(1-\gamma_i)V_i$. This is the endpoint closest to $O$ after accounting for all V triangles that can reach that spoke, not just $T_i$.
- **Paths and boundary handoffs.** A path is an ordered consecutive group of V triangles, connected by the hexagon edges between their vertices. On a gap-free connecting edge their open traces overlap: $B_i+A_{i+1}>1$. A **handoff** is a point selected inside this overlap, covered by both triangles. **Path monotonicity** means the increasing $A_i$ and decreasing $B_i$ obtained by combining these overlaps with nonsupercriticality. An edge is **center-free** when $U_C$ covers no point in its relative interior (the edge with its endpoints removed).
- **Type labels.** CE0, CE1, CE2 count the boundary edges met by $T_C$ in positive length; they do not count gaps. For a V triangle let $o$ count its vertices outside $H$, and $n$ its neighboring spokes met in positive length. Vd0 means $n=0$; Vd1 means $(o,n)=(1,1)$; Vd2 means $(1,2)$; T3-like means $(2,1)$. The names are labels, not additional assumptions.
- **Candidate exit and return.** A radial exit is the farthest point of a candidate triangle on a spoke, measured from $O$. A transverse threshold compares such an exit with the required radial witnesses. The CE1 **return argument** transfers inequalities along the path and returns to the starting triangle with an impossible boundary demand. A selected branch is one explicitly specified parameter case of that calculation; it is not a freely chosen triangle.

**Geometric message:** the gap pulls the center toward the boundary; the nonsupercritical path forces radial points that such a candidate cannot all contain.

**Input in the main proof:** a skeleton cover with a gap, center midpoint $M_k$, and all vertex roles except possibly $T_k$ nonsupercritical. This includes both the N0 application and the aligned one-supercritical application.

## Tree

- **Normalize the center midpoint to $M_0$.**
    - All possible gaps are on $e_{5,0}$ and $e_{0,1}$ — [\[C-MIDPOINT\]](C-MIDPOINT.md).
    - Select either actual gap and reflect so it is on $e_{0,1}$.
    - The ordered path is $T_1,T_2,T_3,T_4,T_5$; these triangles are nonsupercritical and their four connecting edges have no gaps.
- **Transfer demands along the path.**
    - Define the boundary deficit $s_i=1-A_i-B_i$ and the overlap excess $\omega_i=B_i+A_{i+1}-1$.
    - The exact identities are $A_{i+1}-A_i=s_i+\omega_i$ and $B_i-B_{i+1}=s_{i+1}+\omega_i$.
    - On a gap-free nonsupercritical path, $s_i\ge0$ and $\omega_i>0$.
    - Therefore $A$ increases and $B$ decreases along the path.
- **Supply the tail premise from the original cover.**
    - The pure six-point theorem needs $B_5\ge B_0/2$.
    - Original perimeter coverage gives the stronger strict bound through the shared gap anchor.
    - **CALCULATION LEAF:** the shared-anchor estimate — [\[BC-CALC\]](details/BC-calculations.md).
- **Fix the six witnesses.**
    - $M_0$.
    - The two selected-gap endpoints $X_0(B_0)$ and $X_0(1-A_1)$.
    - The three total radial frontiers $\widehat P_2,\widehat P_3,\widehat P_4$.
    - The midpoint belongs to $U_C$; all other witnesses are missed by every vertex role — [\[WITNESS\]](WITNESS.md).
- **Introduce an arbitrary open unit candidate containing these points.**
    - The origin is in the witness convex hull, so the candidate contains $O$ too.
    - The gap endpoints give positive boundary trace; the midpoint anchor selects the unique midpoint $M_0$.
    - Use the candidate's own coordinates, keeping the six witnesses fixed.
    - Boundary containment and the tail bound propagate lower demands down the path.
- **Exclude the candidate.**
    - **CE2 candidate:** a transverse threshold makes at least one required radial exit too short.
        - **CALCULATION LEAF:** the two CE2 threshold comparisons — [\[BC-CALC\]](details/BC-calculations.md).
    - **CE1 candidate:** use the return argument in the correct order.
        - Recover the first two own-radial demands from total-frontier containment and neighboring bounds.
        - Apply only the first return step.
        - Recover the third own-radial demand.
        - Apply the full conditional return; a nonsupercritical role would need boundary sum greater than $1$.
        - **CALCULATION LEAF:** the selected CE1 return — [\[BC-CALC\]](details/BC-calculations.md).
- **Conclude $\Lambda(K_{BC})\ge1$.**
    - But $K_{BC}\subset U_C$ implies $\Lambda(K_{BC})<1$ — [\[WITNESS\]](WITNESS.md).
    - Contradiction.

## Fixed set and scope

$$
K_{BC}=\{M_0,X_0(B_0),X_0(1-A_1),\widehat P_2,\widehat P_3,\widehat P_4\}.
$$

The same set handles one or two gaps. It does not add endpoints from the unselected gap. There is no disk, and the five path roles need no separate V-type cases. BC is independent of N0 and replacement.

---

**Proof sources:** [2018b](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018b_shared_gap_anchor_transfer.md) · [2612](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md) · [4102](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4102_new_CE1_direct_radial_certificate.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
