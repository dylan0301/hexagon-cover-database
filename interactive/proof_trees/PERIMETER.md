# [PERIMETER] The Vd2 supplier cannot cover enough boundary

[\[MAIN\]](README.md) · [\[SUPPLIER\]](SUPPLIER.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Neighboring support and supplier.** The neighboring spokes for a V triangle at $V_i$ are $r_{i-1},r_{i+1}$. It has **positive adjacent support** if its closure meets one of those spokes in an interval of positive length. A **neighboring supplier of $M_j$** is specifically a triangle $U_i$ with $i=j-1$ or $j+1$ and $M_j\in U_i$. “Rescuer” means the same thing here. Supplying a midpoint implies positive support by openness; positive support alone does not imply supplying that midpoint. $N_{\rm sp}$ counts V triangles having positive adjacent support.
- **Type labels.** CE0, CE1, CE2 count the boundary edges met by $T_C$ in positive length; they do not count gaps. For a V triangle let $o$ count its vertices outside $H$, and $n$ its neighboring spokes met in positive length. Vd0 means $n=0$; Vd1 means $(o,n)=(1,1)$; Vd2 means $(1,2)$; T3-like means $(2,1)$. The names are labels, not additional assumptions.
- **Perimeter contribution.** This is the length of a closed triangle's intersection with $\partial H$, the boundary of $H$. A **cap** is an upper bound for that length. The hexagon perimeter is $6$. Adding triangle contributions can overcount overlap, so a total below $6$ rules out a cover.

**Input:** a nonzero-gap placement with exactly one supercritical role and a Vd2 role that covers a neighboring midpoint.

## Tree

- **Use the neighboring-midpoint cap.**
    - A Vd2 role containing that midpoint contributes boundary length strictly below $1/3$.
    - **CALCULATION LEAF:** the local rescue-dependent cap — [\[BOUNDS\]](details/length-area-bounds.md).
- **Bound all other boundary contributions.**
    - The CE1/CE2 center contributes less than $1/2$.
    - The unique supercritical role contributes at most $2/\sqrt3$.
    - The other four nonsupercritical vertex roles contribute at most $1$ each.
- **Sum.**
    - Total boundary capacity is below $1/2+1/3+2/\sqrt3+4$.
    - This is less than $6$, since $12<7\sqrt3$.
    - But the hexagon perimeter has length $6$.
- **Contradiction.**
    - This is a length obstruction, not a finite-witness construction.

---

**Proof sources:** [2531](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md) · [2500](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
