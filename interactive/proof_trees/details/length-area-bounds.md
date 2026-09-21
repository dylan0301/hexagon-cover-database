# [BOUNDS] Local length and area estimates

[\[MAIN\]](../README.md) · [\[LENGTH\]](../LENGTH.md) · [\[AREA\]](../AREA.md) · [\[PERIMETER\]](../PERIMETER.md) · [\[NOTATION\]](../NOTATION.md) · [\[USE\]](../USING.md) · [\[GLOSSARY\]](../GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Neighboring support and supplier.** The neighboring spokes for a V triangle at $V_i$ are $r_{i-1},r_{i+1}$. It has **positive adjacent support** if its closure meets one of those spokes in an interval of positive length. A **neighboring supplier of $M_j$** is specifically a triangle $U_i$ with $i=j-1$ or $j+1$ and $M_j\in U_i$. “Rescuer” means the same thing here. Supplying a midpoint implies positive support by openness; positive support alone does not imply supplying that midpoint. $N_{\rm sp}$ counts V triangles having positive adjacent support.
- **Type labels.** CE0, CE1, CE2 count the boundary edges met by $T_C$ in positive length; they do not count gaps. For a V triangle let $o$ count its vertices outside $H$, and $n$ its neighboring spokes met in positive length. Vd0 means $n=0$; Vd1 means $(o,n)=(1,1)$; Vd2 means $(1,2)$; T3-like means $(2,1)$. The names are labels, not additional assumptions.
- **Measured quantities.** A boundary contribution is the length of $T\cap\partial H$; a skeleton contribution is the length of $T\cap S$. A cap or ledger is simply an upper bound or list of bounds. Area is divided by $\sqrt3/4$, so $G_i$ is the exterior area of $T_i$ in unit-triangle area units. Lowercase $a_i,b_i$ are the realized boundary lower bounds described above. A budget compares the sum of contributions with total required length or area.

**Below the oral cutoff.** This page separates local geometric estimates from the short global additions that use them.

## Tree

- **Boundary-length ledger — sources [2500](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md) and [2531](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md).**
    - CE1: at most $\sqrt3/2-3/4$.
    - CE2: strictly below $1/2$.
    - Nonsupercritical vertex role: at most $1$.
    - Supercritical role: at most $2/\sqrt3$.
    - Vd1/Vd2: strictly below $1/2$.
    - T3-like: strictly below $1$.
    - Vd2 containing a neighboring midpoint: strictly below $1/3$.
    - Used by [\[LENGTH\]](../LENGTH.md) to separate the counted classes and by [\[PERIMETER\]](../PERIMETER.md) to close the Vd2 case.
- **Skeleton-length ledger — sources [2510](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md) and [2531](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md).**
    - CE1/CE2 center, supercritical roles, and positive-support roles each contribute strictly below $3/2$.
    - Remaining nonsupercritical Vd0 roles contribute at most $2$.
    - Add these bounds only after checking that the counted classes are disjoint — [\[LENGTH\]](../LENGTH.md).
- **Exterior-area ledger — source [2400](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/24XX_area_loss/2400_zero_gap_area_loss_interface.md) and its local square-loss dependency.**
    - Every realized selected pair satisfies $G_i\ge\min(a_i,b_i)^2$.
    - A selected supercritical pair satisfies $G_i\ge\max(a_i,b_i)^2$.
    - Used in the short cyclic aggregation in [\[AREA\]](../AREA.md).
- **Open-cover budget — source [2532](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2532_open_cover_budget.md).**
    - Keep the appropriate strictness when turning local estimates into a covering contradiction.
    - Length and area are different measures; do not treat either as an extra finite-witness family.

---

**Proof sources:** [2500](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md) · [2510](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md) · [2531](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md) · [2400](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/24XX_area_loss/2400_zero_gap_area_loss_interface.md) · [2532](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2532_open_cover_budget.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](../README.md) Return to the main tree.
