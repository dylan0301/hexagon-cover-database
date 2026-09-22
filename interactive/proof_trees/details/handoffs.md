# [HANDOFFS] Strict boundary handoff selection

[\[MAIN\]](../README.md) · [\[F\]](../F.md) · [\[AREA\]](../AREA.md) · [\[NOTATION\]](../NOTATION.md) · [\[USE\]](../USING.md) · [\[GLOSSARY\]](../GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Selection and margin.** A handoff is a point in $U_i\cap U_{i+1}$ on their shared boundary edge. Its coordinate $x_i$ lies strictly between $1-A_{i+1}$ and $B_i$. A strict margin is the positive distance from these endpoints. An ascent means $x_i>x_{i-1}$ around the cyclic sequence. Realizing a demand means containing the specified point at that distance.

**Below the oral cutoff.** This is a selection interface, not an area or enclosure theorem. Used by [\[F\]](../F.md) and [\[AREA\]](../AREA.md).

## Tree

- **Start from actual open boundary coverage.**
    - Each adjacent pair has a nonempty open overlap interval.
    - Select an interior handoff $X_i=V_i+x_i(V_{i+1}-V_i)$ with $0<x_i<1$.
    - The selected lower demands are $(a_i,b_i)=(1-x_{i-1},x_i)$.
- **Keep the distinction between actual and selected quantities.**
    - Actual supercriticality is $A_i+B_i>1$.
    - Selected supercriticality is $a_i+b_i>1$, equivalently $x_i>x_{i-1}$.
- **Use the precise conclusion of source [1214](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md).**
    - If there is exactly one actual supercritical role, a strict selection preserves its index and gives one selected ascent.
    - If there are at least two actual supercritical roles, a strict selection can retain at least two selected ascents.
    - Strict overlap provides positive margins; arbitrary endpoint selections are not a substitute.
- **Return to the appropriate global argument.**
    - Exactly one ascent: [\[F\]](../F.md).
    - At least two ascents: [\[AREA\]](../AREA.md).

---

**Proof sources:** [1214](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) · [2400](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/24XX_area_loss/2400_zero_gap_area_loss_interface.md) · [31058](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](../README.md) Return to the main tree.
