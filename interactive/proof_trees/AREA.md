# [AREA] Two ascents force too much exterior area

[\[MAIN\]](README.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Handoff, ascent, and loss.** A handoff is a point $X_i(x_i)$ in the open overlap of the V triangles on edge $e_{i,i+1}$. It gives selected demands $(a_i,b_i)=(1-x_{i-1},x_i)$. An ascent is $x_i>x_{i-1}$, equivalent to their sum being greater than $1$. A minimum plateau is a consecutive block attaining the minimum cyclic value. $G_i=\operatorname{area}(T_i\setminus H)/(\sqrt3/4)$ is the exterior area of V triangle $i$, in units of a unit equilateral triangle's area. A loss is area outside $H$, not an overlap deduction.

**Input:** no boundary gaps and $N_+\ge2$. Normalize the area of one unit equilateral triangle to $1$; then the hexagon has area $6$.

## Tree

- **Select strict boundary handoffs preserving at least two supercritical roles** — [\[HANDOFFS\]](details/handoffs.md).
    - Write $(a_i,b_i)=(1-x_{i-1},x_i)$.
    - A selected supercritical role is exactly an ascent $x_i>x_{i-1}$.
- **Use the local exterior-area estimates.**
    - Write $G_i$ for the normalized area of $T_i$ outside $H$.
    - Every role satisfies $G_i\ge\min(a_i,b_i)^2$.
    - A selected supercritical role satisfies $G_i\ge\max(a_i,b_i)^2$.
    - **CALCULATION LEAF:** the geometric square-loss bounds — [\[BOUNDS\]](details/length-area-bounds.md).
- **Aggregate around the cycle.**
    - Put $m=\min_i x_i$, $M=\max_i x_i$.
    - Reflection exchanges the two demand coordinates, so assume $m\le1-M$.
    - Every selected coordinate is then at least $m$.
    - An ascent leaving a minimum plateau contributes at least $(1-m)^2$.
    - A second ascent contributes strictly more than $1/4$.
    - The remaining four roles each contribute at least $m^2$.
    - Therefore $\sum_iG_i>(1-m)^2+1/4+4m^2=5(m-1/5)^2+21/20>1$.
- **Compare inside area.**
    - The six vertex triangles have total area inside $H$ below $5$.
    - The center contributes at most $1$.
    - The union cannot cover a hexagon of area $6$.
    - Contradiction.

## Presentation cutoff

Keep the aggregation above in the main explanation: it is short. The calculation leaf is the proof of the local square-loss estimates, not this cyclic sum.

---

**Proof sources:** [2400](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/24XX_area_loss/2400_zero_gap_area_loss_interface.md) · [2532](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/25XX_length_bounds/2532_open_cover_budget.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
