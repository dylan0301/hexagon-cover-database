# [MIDPOINTS] The geometric engine of the case reduction

[\[MAIN\]](README.md) · [\[SETUP\]](SETUP.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Neighboring support and supplier.** The neighboring spokes for a V triangle at $V_i$ are $r_{i-1},r_{i+1}$. It has **positive adjacent support** if its closure meets one of those spokes in an interval of positive length. A **neighboring supplier of $M_j$** is specifically a triangle $U_i$ with $i=j-1$ or $j+1$ and $M_j\in U_i$. “Rescuer” means the same thing here. Supplying a midpoint implies positive support by openness; positive support alone does not imply supplying that midpoint. $N_{\rm sp}$ counts V triangles having positive adjacent support.
- **Type labels.** CE0, CE1, CE2 count the boundary edges met by $T_C$ in positive length; they do not count gaps. For a V triangle let $o$ count its vertices outside $H$, and $n$ its neighboring spokes met in positive length. Vd0 means $n=0$; Vd1 means $(o,n)=(1,1)$; Vd2 means $(1,2)$; T3-like means $(2,1)$. The names are labels, not additional assumptions.

**Midpoints always mean spoke midpoints:** $M_i=V_i/2$, not midpoints of boundary edges.

## Tree

- **Center midpoint containment** — [\[C-MIDPOINT\]](C-MIDPOINT.md).
    - If $O\in U_C$ and the center has a positive boundary trace, exactly one $M_k$ lies in $T_C$.
    - In fact $M_k\in U_C$, while all other midpoints lie outside $T_C$.
    - All possible center boundary traces are incident with $V_k$.
- **Supercritical own-midpoint exclusion** — [\[SELF-MIDPOINT\]](SELF-MIDPOINT.md).
    - $M_i\in T_i$ would imply $A_i+B_i\le1$.
    - Therefore a supercritical role misses its own midpoint, even in its closure.
- **T3-like own-midpoint exclusion** — [\[T3-MIDPOINT\]](T3-MIDPOINT.md).
    - Neighboring-spoke support puts the own midpoint beyond one of the triangle's sides.
    - This applies directly to the original open role and its closure.
- **A Vd0 role cannot supply a neighboring midpoint.**
    - Open containment would include a positive-length interval of the neighboring spoke.
    - That contradicts the definition $n=0$.
- **Consequence: a missed midpoint forces a supplier.**
    - If both the center and own vertex role miss $M_i$, locality leaves only $U_{i-1}$ and $U_{i+1}$.
    - A covering neighbor must be a positive-support role.
    - Combine this with the skeleton count to obtain a unique supplier — [\[SUPPLIER\]](SUPPLIER.md).

---

**Proof sources:** [2100](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md) · [2109](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md) · [2005](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md) · [1201](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) · [2613](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2613_midpoint_supplier_reduction.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
