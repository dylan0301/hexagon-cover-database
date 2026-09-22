# [CALIPERS] Why the enclosing candidates are finite

[\[MAIN\]](README.md) · [\[F\]](F.md) · [\[SELF-MIDPOINT\]](SELF-MIDPOINT.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Enclosure language.** A **witness** is a chosen point used to contradict the cover. **Forced into $U_C$** means the cover and previously stated geometry imply that membership. A **candidate** is any other open unit equilateral triangle tested against the same fixed witnesses; it need not complete a cover with the old V triangles. $\operatorname{conv}(K)$ is the convex hull, the set of all convex combinations of points of $K$. For a nonempty compact set $K$ (closed and bounded here), $\Lambda(K)$ is the least side length of a closed equilateral triangle containing it. Thus $K\subset U_C$ gives $\Lambda(K)<1$ by shrinking its three sides slightly.
- **Support and contact.** For a unit vector $n$, $h_K(n)=\max_{x\in K}\langle x,n\rangle$ is the support value, where $\langle x,n\rangle$ is the ordinary dot product. The line $\langle x,n\rangle=h_K(n)$ touches $K$ and leaves it on one side; $n$ is its outward normal. A **support cell** is an interval of orientations with the same support sources. A **tie** is an orientation where two sources attain one maximum. A disk tangent touches the circular boundary in one point. An **exposed** tangent also supports the whole point-and-disk convex hull.
- **The word calipers.** It names the rotating-support-line method for finding an enclosing triangle, not an additional covering assumption. The finite-point claim below is stated for a polygon with interior. A point or line segment needs its elementary degenerate treatment.

**Purpose:** keep the geometric reduction in the spoken explanation while leaving explicit contact formulas and certificates on the detail pages.

## Tree

- **Fix an orientation.**
    - Let $n_0,n_1,n_2$ be outward unit normals separated by $120^\circ$.
    - The smallest triangle with those normals containing a compact set $K$ uses support values $h_K(n_j)$.
    - Its side length is $(2/\sqrt3)\sum_{j=0}^2h_K(n_j)$.
- **For a finite point set, vary the orientation.**
    - Between support changes, the three supporting points stay fixed.
    - Their support sum has form $X\cos\phi+Y\sin\phi$.
    - Its second derivative is the negative of the sum.
    - For a nondegenerate hull the sum is positive, so there is no interior minimum on such a cell.
    - A minimum occurs at a support change: one side contains two hull vertices.
    - Hence a polygon has finitely many relevant hull-edge contacts.
        - This gives the four contacts in [\[SELF-MIDPOINT\]](SELF-MIDPOINT.md).
- **For a centered disk and finitely many points, include disk support.**
    - Each support is the maximum of the disk radius and the point projections.
    - If an orientation has disk support on all three sides, it attains the disk-only lower bound.
    - Otherwise a minimum can be chosen at a support tie.
        - **Point–point tie:** one side contains two points.
        - **Point–disk tie:** one side is tangent to the disk and contains a point.
    - There are finitely many such directions.
- **Specialize to the inner configuration in F.**
    - The points $A,B,C$ must form the specified consecutive part of the convex-hull boundary; the chosen disk tangents must support the entire hull, and the connecting lines must satisfy distance bounds. These are additional hypotheses.
    - Under these hypotheses, the four-contact theorem leaves $AB$, $BC$, and exposed tangents through $A$ or $C$.
    - This special four-contact list is not asserted for every arbitrary disk-plus-three-point set.
    - Return to [\[F\]](F.md); the actual contact inequalities are in [\[F-CALC\]](details/F-certificate.md).

---

**Proof sources:** [2004](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md) · [2005](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md) · [2609](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2609_simplified_finite_enclosure_lemmas.md) · [2611](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2611_four_contact_disk_enclosure.md) · [31057](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31057_terminal_nine_point_enclosure.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.

## Current terminal applications

[BC](BC.md) uses five points and five hull-edge calipers; [D](D.md) uses four points and four calipers. The current BC capacity calculation uses two different pairs and a reusable slack-sensitive envelope, not a uniform radius.
