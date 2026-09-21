# [D-CALC] D adapters and the four-point ending

[\[MAIN\]](../README.md) · [\[D\]](../D.md) · [\[NOTATION\]](../NOTATION.md) · [\[USE\]](../USING.md) · [\[GLOSSARY\]](../GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Neighboring support and supplier.** The neighboring spokes for a V triangle at $V_i$ are $r_{i-1},r_{i+1}$. It has **positive adjacent support** if its closure meets one of those spokes in an interval of positive length. A **neighboring supplier of $M_j$** is specifically a triangle $U_i$ with $i=j-1$ or $j+1$ and $M_j\in U_i$. “Rescuer” means the same thing here. Supplying a midpoint implies positive support by openness; positive support alone does not imply supplying that midpoint. $N_{\rm sp}$ counts V triangles having positive adjacent support.
- **Type labels.** CE0, CE1, CE2 count the boundary edges met by $T_C$ in positive length; they do not count gaps. For a V triangle let $o$ count its vertices outside $H$, and $n$ its neighboring spokes met in positive length. Vd0 means $n=0$; Vd1 means $(o,n)=(1,1)$; Vd2 means $(1,2)$; T3-like means $(2,1)$. The names are labels, not additional assumptions.
- **Enclosure language.** A **witness** is a chosen point used to contradict the cover. **Forced into $U_C$** means the cover and previously stated geometry imply that membership. A **candidate** is any other open unit equilateral triangle tested against the same fixed witnesses; it need not complete a cover with the old V triangles. $\operatorname{conv}(K)$ is the convex hull, the set of all convex combinations of points of $K$. For a nonempty compact set $K$ (closed and bounded here), $\Lambda(K)$ is the least side length of a closed equilateral triangle containing it. Thus $K\subset U_C$ gives $\Lambda(K)<1$ by shrinking its three sides slightly.
- **Normalized input.** $M_0\in U_C$, $T_1$ is the unique supercritical V triangle, and $M_1\in U_0$. The trace $T_0\cap r_1$ is parameterized by $[c,u]$ via $(1-t)V_1$, with $0<c\le1/2\le u<1$. Put $\varepsilon=1-u$ and $Y(t)=(1-t)V_0+tV_5$. An adapter verifies the four scalar and membership hypotheses below for the T3-like or Vd1 supplier. The scalar $M$ below is a bound, not a midpoint $M_i$.

**Below the oral cutoff.** The common geometric ending is recorded here; the two local supplier estimates remain separate source obligations. Return to [\[D\]](../D.md).

## Tree

- **Common adapter — source [2612](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md), Corollary 6.2.**
    - Set $\varepsilon=1-u$ and $M=(c+\sqrt{c^2-8c+4})/2$.
    - Establish $\varepsilon V_1\in U_C$, $C_1\ge c$, and $A_0+\varepsilon\le1$.
    - Establish $A_0/(A_0+\varepsilon)\le1-M$.
    - The supercritical envelope and path give $B_5\le B_1<M$.
    - Thus $A_0\le\varepsilon$ and $B_5<\varepsilon/(A_0+\varepsilon)$.
- **Verify the supplier-specific inputs separately.**
    - T3-like chart: source [4130](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md).
    - Vd1 chart: source [4143](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4143_new_Vd1_rescuer_finite_enclosure.md).
    - Do not assert these ratios for a Vd2 supplier.
- **Common four-point theorem — source [2612](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md), Theorem 6.1.**
    - Take $a\ge0$, $\varepsilon>0$, $\beta\ge0$, $s=a+\varepsilon\le1$, $a\le\varepsilon$, and $\beta\le\varepsilon/s$. In the application $a=A_0$ and $\beta=B_5$.
    - Consider $K=\{O,\varepsilon V_1,Y(a),Y(1-\beta)\}$.
    - If $a=0$ or $\beta=0$, the set includes $O$ and a vertex at distance $1$; open unit enclosure is impossible.
    - Otherwise $[\varepsilon Y(a)+a\varepsilon V_1]/s=(\varepsilon/s)V_0$ forces $M_0$ into the candidate hull with $O$.
    - Use local coordinates $X=V_0+b(V_1-V_0)+a_{\rm loc}(V_5-V_0)$ (the coordinate $a_{\rm loc}$ is not the theorem's scalar $a$). The candidate has affine side inequalities $R+\alpha-a_{\rm loc}+Wb>0$, $Rb+Wa_{\rm loc}-(\eta+\alpha+\delta)>0$, and $W+\delta-b+Ra_{\rm loc}>0$, where $0<R<1$, $W=1-R$, $E=\sqrt{1-RW}$, $\eta=1-E$, and $\alpha,\delta>0$ are side slacks at $O$.
    - The candidate's interval on $Y(t)$ is bounded by $(\eta+\alpha+\delta)/W$ and $R+\alpha$; its exit radius on $r_1$ is $\delta/R$. Thus candidate containment gives $Wa>\eta+\alpha+\delta$ and $\delta>R\varepsilon$, with $W=1-R$.
    - Hence $R<a/s$ and $\alpha<a-Rs$.
    - Thus the candidate boundary endpoint satisfies $R+\alpha<a+R(1-s)\le a/s$.
    - But containment of the other point needs $1-\beta<R+\alpha$, while $1-\beta\ge a/s$.
    - Contradiction.

---

**Proof sources:** [2612](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md) · [4130](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) · [4143](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4143_new_Vd1_rescuer_finite_enclosure.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](../README.md) Return to the main tree.
