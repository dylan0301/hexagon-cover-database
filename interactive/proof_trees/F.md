# [F] The zero-gap nine-point obstruction

[\[MAIN\]](README.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Enclosure language.** A **witness** is a chosen point used to contradict the cover. **Forced into $U_C$** means the cover and previously stated geometry imply that membership. A **candidate** is any other open unit equilateral triangle tested against the same fixed witnesses; it need not complete a cover with the old V triangles. $\operatorname{conv}(K)$ is the convex hull, the set of all convex combinations of points of $K$. For a nonempty compact set $K$ (closed and bounded here), $\Lambda(K)$ is the least side length of a closed equilateral triangle containing it. Thus $K\subset U_C$ gives $\Lambda(K)<1$ by shrinking its three sides slightly.
- **Capacity.** $c_{\max}(p,q)$ is the largest own-spoke reach possible for a closed unit equilateral triangle that contains a hexagon vertex and reaches at least $p,q$ along its two incident edges. More formally, in coordinates based at that vertex, choose unit vectors $u,v$ meeting at $120^\circ$; it is the largest $c$ such that $\{0,pu,qv,c(u+v)\}$ fits in a closed unit equilateral triangle. $C_+(p,q),C_-(p,q)$ are the corresponding maximal reaches on the two neighboring spokes, measured from each target spoke's vertex toward $O$. A **capacity bound** is an upper bound on one of these reaches.
- **Handoff and ascent.** Write a chosen common boundary point as $X_i(x_i)$, with $0<x_i<1$. The V triangle at $V_i$ then realizes the lower demands $(a_i,b_i)=(1-x_{i-1},x_i)$. An **ascent** is $x_i>x_{i-1}$, equivalent to $a_i+b_i>1$; a descent reverses that inequality. A **frontier witness** is a fixed point proved to be outside all open V triangles. The construction lemma below supplies three such points $Q_-,Q_0,Q_+$; these are names, not subtraction or addition operations.
- **Contact terms.** A supporting line touches a convex hull and leaves it on one side. An exposed disk tangent is a line tangent to the disk that also supports the entire hull with the extra points. The inner points named $A,B,C$ below are geometric points, not the numerical reaches $A_i,B_i,C_i$.

**Input:** the six vertex triangles cover the perimeter, exactly one actual vertex role is supercritical, and all seven triangles cover the full hexagon. **No C-type or V-type pattern is assumed.**

## Tree

- **Choose strict boundary handoffs.**
    - Select a point in each overlap of adjacent open vertex traces.
    - Write selected demands as $(a_i,b_i)=(1-x_{i-1},x_i)$.
    - Preserve the unique actual supercritical index as the unique selected ascent.
    - **CALCULATION LEAF:** the strict selection theorem — [\[HANDOFFS\]](details/handoffs.md).
- **Use the one-ascent order.**
    - Rotate so the ascent is at role $4$.
    - Then $x_3<x_2<x_1<x_0<x_5<x_4$.
    - Put $a=1-x_3$, $b=x_4$, $p=1-b$, and $q=1-a$.
    - Every selected role has both boundary demands at least the common pair $(p,q)$.
    - The unique ascent gives $a+b>1$.
    - The two strict handoff points in $U_4$ give $a^2+ab+b^2<1$.
- **Force six symmetric radial points.**
    - Put $c_*=c_{\max}(p,q)$ and $D_i=(1-c_*)V_i$.
    - Own and neighboring reach bounds exclude each $D_i$ from every open vertex role.
    - Therefore $D_0,\ldots,D_5\in U_C$.
    - **CALCULATION LEAF:** common-pair radial forcing — [\[F-CALC\]](details/F-certificate.md).
- **Obtain a disk by convexity, not pointwise exclusion.**
    - The six radial points form a regular hexagon.
    - Its convex hull contains the centered disk of radius $\eta=(\sqrt3/2)(1-c_*)$.
    - Hence this entire disk lies in $U_C$.
- **Force three asymmetric points near the unique supercritical role.**
    - Construct the fixed frontier points $Q_-,Q_0,Q_+$.
    - Exclude them from all vertex roles using the actual handoffs and local signs.
    - Full-hexagon coverage forces all three into $U_C$.
    - **CALCULATION LEAF:** witness construction and exclusions — [\[F-CALC\]](details/F-certificate.md).
- **Exclude enclosure of the disk and three points.**
    - If $c_*\le2/3$, the disk alone requires enclosing side at least $3(1-c_*)\ge1$.
    - Otherwise choose inner points $A\in(Q_0,Q_-)$, $B=Q_0$, $C\in(Q_0,Q_+)$.
        - Their disk-plus-triangle hull is contained in the original witness hull.
        - **CALCULATION LEAF:** exact inner-point construction and line bounds — [\[F-CALC\]](details/F-certificate.md).
    - Reduce minimum enclosing triangles to four relevant contacts — [\[CALIPERS\]](CALIPERS.md).
        - A side through $AB$.
        - A side through $BC$.
        - An exposed disk tangent through $A$.
        - An exposed disk tangent through $C$.
    - Each contact requires side length at least $1$.
        - Point–point contacts use supporting-line bounds.
        - Point–disk contacts use the exact polynomial positivity certificate.
        - **CALCULATION LEAF:** the finite exact certificate — [\[F-CALC\]](details/F-certificate.md).
- **Finish by the common compact-open contradiction** — [\[WITNESS\]](WITNESS.md).

## Scope that matters later

The nine directly forced points are $D_0,\ldots,D_5,Q_-,Q_0,Q_+$. The disk is an auxiliary subset of their convex hull. The asymmetric points require **full-hexagon coverage**, so F cannot replace N0 after a construction that preserves only the skeleton.

---

**Proof sources:** [31058](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md) · [31057](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31057_terminal_nine_point_enclosure.md) · [2611](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2611_four_contact_disk_enclosure.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
