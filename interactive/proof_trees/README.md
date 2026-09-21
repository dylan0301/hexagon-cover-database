# [MAIN] Seven triangles cannot cover the hexagon

[\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Neighboring support and supplier.** The neighboring spokes for a V triangle at $V_i$ are $r_{i-1},r_{i+1}$. It has **positive adjacent support** if its closure meets one of those spokes in an interval of positive length. A **neighboring supplier of $M_j$** is specifically a triangle $U_i$ with $i=j-1$ or $j+1$ and $M_j\in U_i$. “Rescuer” means the same thing here. Supplying a midpoint implies positive support by openness; positive support alone does not imply supplying that midpoint. $N_{\rm sp}$ counts V triangles having positive adjacent support.
- **Type labels.** CE0, CE1, CE2 count the boundary edges met by $T_C$ in positive length; they do not count gaps. For a V triangle let $o$ count its vertices outside $H$, and $n$ its neighboring spokes met in positive length. Vd0 means $n=0$; Vd1 means $(o,n)=(1,1)$; Vd2 means $(1,2)$; T3-like means $(2,1)$. The names are labels, not additional assumptions.
- **Indices used in the case split.** $k$ is the index of the unique midpoint $M_k$ contained by $U_C$ when a gap exists. After the count reduction, $\sigma$ is the unique supercritical index. When $\sigma\ne k$, $\tau$ names the unique neighboring supplier, so $\tau\in\{\sigma-1,\sigma+1\}$ and $M_\sigma\in U_\tau$. “At $k$” means based at vertex $V_k$, not physically located at midpoint $M_k$.
- **Page names.** BC, D, and F are historical labels for contradictions using at most six, four, and nine fixed points. N0 is the theorem excluding $N_+=0$, not a new numerical variable. A **calculation leaf** states an exact lemma's inputs and output, while leaving its long derivation in the linked numbered proof source.

New to the proof? [START](START.md) explains the problem and vocabulary without assuming the role names. Every argument page repeats its local setup.

**Claim.** Seven open equilateral triangles of side $1$ cannot cover the regular hexagon of side $1$.

[START](START.md) · [GLOSSARY](GLOSSARY.md)

**Click a bracketed label to open its tree.** Midpoint proofs are expanded. A **CALCULATION LEAF** marks the point where the oral explanation stops; its linked page identifies the exact written calculation. Read [\[USE\]](USING.md) for the offline browser view.

## Tree

- **Assume a cover exists.**
    - **1. Identify the roles and the local geometry** — [\[SETUP\]](SETUP.md).
        - The center and six vertices occupy seven distinct open triangles.
        - Classify boundary traces and neighboring-spoke support — [\[CLASSIFICATION\]](CLASSIFICATION.md).
        - Prove the midpoint containment and exclusion facts — [\[MIDPOINTS\]](MIDPOINTS.md).
    - **2. Establish N0: a skeleton cover must have $N_+\ge1$** — [\[N0\]](N0.md).
        - With no gaps: sum the strict boundary overlaps.
        - With a gap: use the center-aligned six-point obstruction [\[BC\]](BC.md).
    - **3. Split by boundary gaps.**
        - **No boundary gaps.**
            - $N_+=1$: force the nine-point obstruction [\[F\]](F.md).
            - $N_+\ge2$: force excessive exterior area — [\[AREA\]](AREA.md).
        - **At least one boundary gap.**
            - The center contains exactly one spoke midpoint $M_k$ — [\[C-MIDPOINT\]](C-MIDPOINT.md).
            - The skeleton budget gives $N_++N_{\rm sp}\le2$ — [\[LENGTH\]](LENGTH.md).
            - A second supercritical role would require a neighboring V triangle to contain its missed midpoint.
                - Therefore $N_+=1$ and $N_{\rm sp}\le1$ — [\[SUPPLIER\]](SUPPLIER.md).
            - Let $\sigma$ be the unique supercritical index.
                - **$\sigma=k$:** apply [\[BC\]](BC.md).
                - **$\sigma\ne k$:** $M_\sigma$ lies in exactly one neighboring open V triangle $U_\tau$ (its supplier) — [\[SUPPLIER\]](SUPPLIER.md).
                    - **T3-like supplier:** its own midpoint exclusion forces $\tau=k$; apply [\[D\]](D.md).
                    - **Vd1 supplier at $k$:** apply [\[D\]](D.md).
                    - **Vd1 supplier away from $k$:** preserve the skeleton by [\[REPLACEMENT\]](REPLACEMENT.md), then contradict [\[N0\]](N0.md).
                    - **Vd2 supplier:** its midpoint-rescue perimeter cap gives [\[PERIMETER\]](PERIMETER.md).
    - **Every possible cover leads to a contradiction.**

## Shared tools

- [\[WITNESS\]](WITNESS.md) explains the common fixed-point enclosure contradiction behind BC, D, and F.
- [\[CALIPERS\]](CALIPERS.md) explains why only finitely many enclosing-triangle contacts need consideration.

## Scope

This is a linked presentation of the repository's proof, not a new proof or an independent verification of all calculation leaves. The presentation follows repository snapshot `c9baa75d090ee888fa85b575bdfb061f244197d0`, checked on **2026-09-21**. This directory is the presentation layer; numbered proof sources remain the mathematical authority.

---

**Proof sources:** [0000](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/0XXX_main/0000_main_theorem.md) · [0003](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/0XXX_main/0003_reusable_lemma_catalog.md) · [2613](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2613_midpoint_supplier_reduction.md). All source links are pinned to the same repository snapshot.
