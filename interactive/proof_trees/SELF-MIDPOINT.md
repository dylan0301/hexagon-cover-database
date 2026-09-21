# [SELF-MIDPOINT] A supercritical role misses its own midpoint

[\[MAIN\]](README.md) · [\[MIDPOINTS\]](MIDPOINTS.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Enclosure language.** A **witness** is a chosen point used to contradict the cover. **Forced into $U_C$** means the cover and previously stated geometry imply that membership. A **candidate** is any other open unit equilateral triangle tested against the same fixed witnesses; it need not complete a cover with the old V triangles. $\operatorname{conv}(K)$ is the convex hull, the set of all convex combinations of points of $K$. For a nonempty compact set $K$ (closed and bounded here), $\Lambda(K)$ is the least side length of a closed equilateral triangle containing it. Thus $K\subset U_C$ gives $\Lambda(K)<1$ by shrinking its three sides slightly.
- **Supported edge.** A supporting line touches a convex set and leaves that set on one side. A hull edge is an edge of its convex hull. A contact orientation fixes a triangle side along such a line and chooses the other two sides just far enough out to enclose the set. The local origin $0$ below is the translated vertex $V_i$, not the hexagon center.

**Statement.** For a closed unit vertex triangle, $M_i\in T_i$ implies $A_i+B_i\le1$. Thus $A_i+B_i>1$ excludes $M_i$ from the closure.

## Tree

- **Assume the contrary.**
    - Translate $V_i$ to $0$ and choose unit edge directions $u,v$ meeting at $120^\circ$.
    - Put $a=A_i$, $b=B_i$, $P=au$, $Q=bv$, and $M=(u+v)/2$.
    - Assume $a+b>1$ and that a closed unit triangle contains $0,P,M,Q$.
    - These points form the quadrilateral $K=\operatorname{conv}\{0,P,M,Q\}$.
- **Reduce the enclosing orientation to four contacts** — [\[CALIPERS\]](CALIPERS.md).
    - The minimum occurs with a side supported along a hull edge.
    - Check $0P$, $PM$, $MQ$, and $Q0$.
- **The edge $0P$ requires side length greater than $1$.**
    - Its required length is $L_{0P}=b+\max\{a,1/2\}$.
    - If $a\ge1/2$, this is $a+b>1$.
    - If $a<1/2$, then $b>1-a>1/2$, so again $L_{0P}>1$.
    - The edge $Q0$ is symmetric.
- **The edge $PM$ also requires side length greater than $1$.**
    - Set $d_a=\sqrt{4a^2-2a+1}$.
    - If $a\le1/2$, then $L_{PM}=(a+b)/d_a>1$ because $d_a\le1$.
    - If $a>1/2$, then $L_{PM}=(2a^2+b)/d_a$.
        - Since $b>1-a$, the numerator exceeds $2a^2-a+1$.
        - The identity $(2a^2-a+1)^2-d_a^2=a^2(2a-1)^2\ge0$ completes the comparison.
    - The edge $MQ$ is symmetric.
- **All four candidates require side length greater than $1$.**
    - Contradiction.
    - Therefore midpoint containment forces $A_i+B_i\le1$.

## Exact scope

This uses actual maximal reaches and gives a weak inequality for a closed triangle. Strict inequalities for selected lower bounds require the separate positive-margin argument; they are not silently substituted here.

---

**Proof sources:** [2005](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md) · [2004](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
