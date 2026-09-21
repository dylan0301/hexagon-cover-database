# [D] Four points forced by a neighboring midpoint supplier

[\[MAIN\]](README.md) · [\[SUPPLIER\]](SUPPLIER.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Neighboring support and supplier.** The neighboring spokes for a V triangle at $V_i$ are $r_{i-1},r_{i+1}$. It has **positive adjacent support** if its closure meets one of those spokes in an interval of positive length. A **neighboring supplier of $M_j$** is specifically a triangle $U_i$ with $i=j-1$ or $j+1$ and $M_j\in U_i$. “Rescuer” means the same thing here. Supplying a midpoint implies positive support by openness; positive support alone does not imply supplying that midpoint. $N_{\rm sp}$ counts V triangles having positive adjacent support.
- **Type labels.** CE0, CE1, CE2 count the boundary edges met by $T_C$ in positive length; they do not count gaps. For a V triangle let $o$ count its vertices outside $H$, and $n$ its neighboring spokes met in positive length. Vd0 means $n=0$; Vd1 means $(o,n)=(1,1)$; Vd2 means $(1,2)$; T3-like means $(2,1)$. The names are labels, not additional assumptions.
- **Enclosure language.** A **witness** is a chosen point used to contradict the cover. **Forced into $U_C$** means the cover and previously stated geometry imply that membership. A **candidate** is any other open unit equilateral triangle tested against the same fixed witnesses; it need not complete a cover with the old V triangles. $\operatorname{conv}(K)$ is the convex hull, the set of all convex combinations of points of $K$. For a nonempty compact set $K$ (closed and bounded here), $\Lambda(K)$ is the least side length of a closed equilateral triangle containing it. Thus $K\subset U_C$ gives $\Lambda(K)<1$ by shrinking its three sides slightly.
- **Paths and boundary handoffs.** A path is an ordered consecutive group of V triangles, connected by the hexagon edges between their vertices. On a gap-free connecting edge their open traces overlap: $B_i+A_{i+1}>1$. A **handoff** is a point selected inside this overlap, covered by both triangles. **Path monotonicity** means the increasing $A_i$ and decreasing $B_i$ obtained by combining these overlaps with nonsupercriticality. An edge is **center-free** when $U_C$ covers no point in its relative interior (the edge with its endpoints removed).
- **Placement and interval.** “Center-based supplier” means the supplying V triangle has index $k$, where $M_k\in U_C$. It is not the C triangle. After rotating or reflecting, take $k=0$ and the missed midpoint to be $M_1$. The supported interval $[c,u]$ denotes $\{(1-t)V_1:c\le t\le u\}\subset T_0$, with $t$ measured from $V_1$ toward $O$. Its endpoint closest to $O$ is $(1-u)V_1$. A local **adapter** is a lemma checking the hypotheses of the common four-point theorem for one supplier type.

**Input:** the unique supplier is based at the center midpoint index and is either T3-like or Vd1. **Conclusion:** a fixed set of at most four points is forced into $U_C$, but cannot fit in any open unit equilateral triangle.

## Tree

- **Normalize the placement.**
    - The center's midpoint is $M_0$.
    - $T_1$ is uniquely supercritical and misses $M_1$.
    - The open supplier $U_0$ contains $M_1$ on spoke $r_1$; $T_0$ denotes its closure.
    - The other four V triangles $T_2,T_3,T_4,T_5$ are nonsupercritical; along edges $e_{1,2},e_{2,3},e_{3,4},e_{4,5}$ the C triangle supplies no boundary coverage.
- **Read the supported interval.**
    - Write its actual coordinates on $r_1$ as $[c,u]$, measured from $V_1$ toward $O$.
    - It reaches the midpoint: $0<c\le1/2\le u<1$.
    - Put $\varepsilon=1-u$; the O-side endpoint is $P=\varepsilon V_1$.
- **Establish the common rescuer input.**
    - Force $P\in U_C$ and establish $C_1\ge c$.
    - Define the scalar $M=(c+\sqrt{c^2-8c+4})/2$. Verify $A_0+\varepsilon\le1$ and $A_0/(A_0+\varepsilon)\le1-M$. This $M$ is not a midpoint $M_i$.
    - **T3-like supplier:** use its own local chart.
    - **Vd1 supplier:** use its different local chart.
    - **CALCULATION LEAF:** the two adapters are separate; their conclusion is common — [\[D-CALC\]](details/D-calculations.md).
- **Propagate the boundary restriction.**
    - The bound $B_1<M$ on the supercritical triangle, followed by the gap-free boundary inequalities, gives $B_5\le B_1<M$.
    - The ratio bound forces an actual gap on $e_{5,0}$.
    - With $Y(t)=(1-t)V_0+tV_5$, the gap endpoints are $Y(A_0)$ and $Y(1-B_5)$.
- **Fix four witnesses.**
    - $K_D=\{O,\varepsilon V_1,Y(A_0),Y(1-B_5)\}$.
    - All four belong to $U_C$ — [\[WITNESS\]](WITNESS.md).
- **Apply the common four-point geometry.**
    - The geometric hypotheses include $A_0\le\varepsilon$ and $B_5\le\varepsilon/(A_0+\varepsilon)$.
    - A convex combination of $Y(A_0)$ and $\varepsilon V_1$ lies on $r_0$ at radius $\varepsilon/(A_0+\varepsilon)\ge1/2$.
    - Together with $O$, this forces $M_0$ into any candidate containing the set.
    - The candidate's midpoint, radial exit, and boundary endpoints impose incompatible side inequalities.
    - **CALCULATION LEAF:** the short signed-side ending is recorded in [\[D-CALC\]](details/D-calculations.md).
- **Conclude the contradiction.**
    - The four-point theorem gives $\Lambda(K_D)\ge1$.
    - Open containment in $U_C$ gives $\Lambda(K_D)<1$.

## Do not merge the wrong steps

Explain the four-point geometry once, but retain the different local ratio verifications for T3-like and Vd1 suppliers. No disk is used. A Vd2 supplier is not assigned this theorem: it has the separate [\[PERIMETER\]](PERIMETER.md) exit.

---

**Proof sources:** [2610](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md) · [2612](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md) · [4130](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) · [4143](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4143_new_Vd1_rescuer_finite_enclosure.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
