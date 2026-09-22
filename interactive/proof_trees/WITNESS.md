# [WITNESS] The common fixed-point enclosure contradiction

[\[MAIN\]](README.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Enclosure language.** A **witness** is a chosen point used to contradict the cover. **Forced into $U_C$** means the cover and previously stated geometry imply that membership. A **candidate** is any other open unit equilateral triangle tested against the same fixed witnesses; it need not complete a cover with the old V triangles. $\operatorname{conv}(K)$ is the convex hull, the set of all convex combinations of points of $K$. For a nonempty compact set $K$ (closed and bounded here), $\Lambda(K)$ is the least side length of a closed equilateral triangle containing it. Thus $K\subset U_C$ gives $\Lambda(K)<1$ by shrinking its three sides slightly.
- **Total radial frontier.** Put $Z_i(c)=(1-c)V_i$. For $j=i-1,i+1$, let $u_{j\to i}$ be the largest $c$ of a positive-length trace $T_j\cap r_i$, or $0$ when that trace is absent. Define $\gamma_i=\max\{C_i,u_{i-1\to i},u_{i+1\to i}\}$ and $\widehat P_i=(1-\gamma_i)V_i$. This is the endpoint closest to $O$ after accounting for all V triangles that can reach that spoke, not just $T_i$.

**Purpose:** explain this argument once, then reuse it for BC, D, and F. For compact $K$, write $\Lambda(K)$ for the least side length of a closed equilateral triangle containing $K$.

## Tree

- **Choose a fixed set from the original configuration.**
    - The points are chosen before introducing an arbitrary enclosing candidate.
    - They cannot be moved in response to that candidate.
- **Force the set into the original center triangle.**
    - Some anchors are already known to belong to $U_C$.
    - Gap endpoints are missed by all open vertex roles, so they belong to $U_C$.
    - Radial frontier points are chosen beyond every relevant vertex-role contribution.
        - Include neighboring contributions, not only the own-spoke reach.
    - Any remaining interior witnesses require full-hexagon coverage to force them into $U_C$.
- **Suppose an arbitrary open unit candidate contains the same set.**
    - Candidate containment gives geometric demands.
    - The appropriate enclosure theorem proves $\Lambda(K)\ge1$.
    - The candidate need not form a cover together with the old vertex roles; use only established candidate-containment consequences.
- **Use compactness and openness.**
    - If $K\subset U_C$, its distance from each side is positive.
    - Move all three sides inward slightly to obtain a smaller closed equilateral triangle still containing $K$.
    - Hence $\Lambda(K)<1$, a contradiction.
- **The active witness families.**
    - [\[BC\]](BC.md): at most five points; skeleton coverage suffices; no disk.
    - [\[D\]](D.md): at most four points; skeleton coverage suffices; no disk.
    - [\[F\]](F.md): at most nine points; uses full-hexagon coverage; a disk is obtained by convexity from six radial points.

## Total radial frontier

For the spoke $r_i$, let $\gamma_i$ be the maximum of the own radial reach and the two actual neighboring O-side endpoints, measured from $V_i$ toward $O$. Then $\widehat P_i=(1-\gamma_i)V_i$ is missed by every open vertex role. Under skeleton coverage it belongs to $U_C$. This is not automatically the own endpoint $(1-C_i)V_i$.

---

**Proof sources:** [2610](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md) · [2612](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md) · [31058](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
