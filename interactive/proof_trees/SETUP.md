# [SETUP] Roles, locality, and gaps

[\[MAIN\]](README.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.

**Input:** a hypothetical cover by seven open unit equilateral triangles. **Output:** the role labels, local coverage restrictions, and gap convention used throughout.

## Tree

- **Seven distinguished points force seven distinct roles.**
    - Let $O$ be the hexagon center and $V_0,\ldots,V_5$ its vertices in cyclic order.
    - They are pairwise at distance at least $1$.
    - Two points in an open unit equilateral triangle have distance strictly below $1$.
    - Thus $O\in U_C$ and $V_i\in U_i$ determine seven distinct triangles.
    - Write $T_C=\overline{U_C}$ and $T_i=\overline{U_i}$.
- **Coverage by a vertex role is local.**
    - A point in the relative interior of a nonincident boundary edge is farther than $1$ from $V_i$.
        - Hence $T_i$ has boundary traces only on the two edges incident with $V_i$.
    - A noncentral point on a nonlocal spoke is also farther than $1$ from $V_i$.
        - For example, for $0<d\le1$, $\|dV_{i\pm2}-V_i\|^2=1+d+d^2>1$.
        - Also $\|dV_{i+3}-V_i\|=1+d>1$.
    - Therefore $M_i$ can be covered only by $U_C,U_{i-1},U_i,U_{i+1}$.
- **Record actual boundary reaches.**
    - $A_i$ is the reach from $V_i$ on the preceding edge; $B_i$ is the reach on the following edge.
    - Supercritical means $A_i+B_i>1$; count such roles with $N_+$.
    - These are actual maximal reaches of the closures, not freely selected lower bounds.
- **Define gaps using the original open roles.**
    - On edge $e_{i,i+1}$, the incident open traces have parameters $[0,B_i)$ and $(1-A_{i+1},1]$.
    - If $B_i+A_{i+1}>1$, they overlap strictly and there is no gap.
    - If $B_i+A_{i+1}\le1$, their complement is the closed interval $[B_i,1-A_{i+1}]$.
        - Equality leaves a singleton gap, not a gap-free edge.
    - Every actual gap must belong to $U_C$.
        - Even a singleton forces a positive boundary trace of $U_C$, by openness.
- **Continue to the structural facts.**
    - Center and vertex types — [\[CLASSIFICATION\]](CLASSIFICATION.md).
    - Midpoint containment and exclusion — [\[MIDPOINTS\]](MIDPOINTS.md).
    - The skeleton is the perimeter plus six spokes; its total length is $12$.

---

**Proof sources:** [0000](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/0XXX_main/0000_main_theorem.md) · [1201](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) · [2500](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md) · [2612](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
