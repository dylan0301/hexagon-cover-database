# [F-CALC] F forcing and exact contact certificate

[\[MAIN\]](../README.md) · [\[F\]](../F.md) · [\[NOTATION\]](../NOTATION.md) · [\[USE\]](../USING.md) · [\[GLOSSARY\]](../GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Enclosure language.** A **witness** is a chosen point used to contradict the cover. **Forced into $U_C$** means the cover and previously stated geometry imply that membership. A **candidate** is any other open unit equilateral triangle tested against the same fixed witnesses; it need not complete a cover with the old V triangles. $\operatorname{conv}(K)$ is the convex hull, the set of all convex combinations of points of $K$. For a nonempty compact set $K$ (closed and bounded here), $\Lambda(K)$ is the least side length of a closed equilateral triangle containing it. Thus $K\subset U_C$ gives $\Lambda(K)<1$ by shrinking its three sides slightly.
- **Capacity.** $c_{\max}(p,q)$ is the largest own-spoke reach possible for a closed unit equilateral triangle that contains a hexagon vertex and reaches at least $p,q$ along its two incident edges. More formally, in coordinates based at that vertex, choose unit vectors $u,v$ meeting at $120^\circ$; it is the largest $c$ such that $\{0,pu,qv,c(u+v)\}$ fits in a closed unit equilateral triangle. $C_+(p,q),C_-(p,q)$ are the corresponding maximal reaches on the two neighboring spokes, measured from each target spoke's vertex toward $O$. A **capacity bound** is an upper bound on one of these reaches.
- **Parameters and witnesses.** The selected boundary demands of the unique supercritical V triangle are $a,b$, with $0<a,b<1$, $a+b>1$, and $a^2+ab+b^2<1$. Put $p=1-b$, $q=1-a$, $c_*=c_{\max}(p,q)$, $h=\sqrt3/2$, and $\eta=h(1-c_*)$. The disk is $\mathcal D_\eta=\{x:\|x\|\le\eta\}$. The construction lemma supplies fixed witnesses $Q_-,Q_0,Q_+$ outside all open V triangles. Later $A,B,C$ name three points inside their convex hull, not boundary reaches.
- **Exact-check terminology.** A supporting line touches a convex hull and leaves it on one side; $d_{AB}$ is the distance from $O$ to the line through points $A,B$. A support value is the maximum dot product in a specified unit-normal direction. Exposure means a tangent supports the whole hull, not just the disk. A **residual** is the expression left after moving all terms of the required inequality to one side. A **certificate** is an exact identity proving that residual has the required sign, not a numerical sample.

**Below the oral cutoff.** These are the fixed mathematical verification obligations, not numerical experiments. Return to [\[F\]](../F.md) for their role in the proof.

## Tree

- **Common-pair radial forcing — sources [31051](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31051_direct_radial_forcing.md), [2008b](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008b_direct_neighbor_domination.md), [2608](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md).**
    - Establish exclusion of all six radial witnesses using both own and neighboring capacities.
    - The disk is then obtained from their convex hull.
- **Asymmetric frontier witnesses — source [31053](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31053_direct_asymmetric_witness_forcing.md).**
    - Define the fixed $Q_-,Q_0,Q_+$ from the strict two-parameter domain.
    - Prove exclusion from every vertex role using handoffs, fixed-line signs, and distance bounds.
- **Inner-point construction — source [31054](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31054_four_cap_enclosure_reduction.md).**
    - Use the fixed-start ($k=1/2$) Newton inner points $A\in(Q_0,Q_-)$, $B=Q_0$, $C\in(Q_0,Q_+)$.
    - Verify that $A,B,C$ occur consecutively on the relevant convex boundary, and $d_{AB},d_{BC}\ge h-2\eta>\eta$.
    - Here $h=\sqrt3/2$ and $\eta$ is the actual comparison-disk radius.
- **Four-contact theorem — source [2611](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2611_four_contact_disk_enclosure.md).**
    - Verify its exposure and ordered-chain hypotheses; do not rely only on the picture.
    - The two point–point contacts have support sum at least $h$.
- **Two tangent residuals — sources [31055](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31055_rational_radial_envelopes_and_mixed_reduction.md) and [31056](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31056_global_analytic_mixed_positivity.md).**
    - First replace the actual radius by a suitable rigorously bounded comparison radius. Then rewrite the tangent inequalities using dot products and squared lengths (the Gram calculation).
    - Use the single rational radius envelope and reduce to one ordered residual. The active exact proof uses one cubic endpoint comparison, four quadratic mixed-derivative comparisons, a cubic curvature comparison, and retained increment/Taylor bounds. Chebyshev coefficient sums and reconstruction identities are checked over the rationals; no separately stored SOS or Bernstein witness is an input.
    - The radius-transfer lemma proves that the two tangent inequalities remain valid when passing from the comparison radius to the actual radius $\eta$.
    - Sampling, interval scans, or a floating-point plot do not replace these exact identities.
- **Terminal assembly — source [31057](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31057_terminal_nine_point_enclosure.md).**
    - Every one of the four contacts has support sum at least $h$.
    - The minimum enclosing side is at least $1$.
    - Apply the compact-open contradiction to finish [\[F\]](../F.md).

---

**Proof sources:** [31057](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31057_terminal_nine_point_enclosure.md) · [31058](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md) · [2611](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2611_four_contact_disk_enclosure.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](../README.md) Return to the main tree.

## Active source and scope

The current source is [3105b](https://github.com/dylan0301/hexagon-cover-database/blob/chatgpt/f-explicit-comparison-20260923155000/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105b_explicit_comparison_enclosure.md); the older pinned `31054`--`31056` links
above identify the historical junction-start proof. The original frontier points
are unchanged; the comparison points and auxiliary radius change together.
The actual disk is retained for exposed-hull geometry and line contacts.
[Current numerical viewer](https://github.com/dylan0301/hexagon-cover-database/blob/chatgpt/f-explicit-comparison-20260923155000/interactive/f_explicit_comparison.html); it is not a proof.
