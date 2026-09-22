# [NOTATION] Notation and logical scopes

[\[MAIN\]](README.md) · [\[USE\]](USING.md)

## Terms used here

This is an index of symbols, not required prior reading. Each argument page supplies its own definitions. For ordinary-language explanations and examples, use [GLOSSARY](GLOSSARY.md). A **role** is a triangle assigned to the center or a vertex. A **trace** is its intersection with the named edge or spoke. A **supplier** must contain the named midpoint in its open triangle, not merely approach that spoke.

## Tree

- **Hexagon and roles.**
    - $H$: the regular side-$1$ hexagon; $O=0$: its center.
    - $V_i=(\cos(i\pi/3),\sin(i\pi/3))$; all indices are modulo $6$.
    - $r_i=[O,V_i]$; $M_i=V_i/2$ is a spoke midpoint.
    - $e_{i,i+1}=[V_i,V_{i+1}]$; $X_i(t)=(1-t)V_i+tV_{i+1}$.
    - $U_C,U_i$: original open role triangles; $T_C,T_i$: their closures.
- **Actual versus selected reaches.**
    - $A_i,B_i$: actual preceding-edge and following-edge reaches from $V_i$.
    - $C_i$: actual own-spoke reach, measured from $V_i$ toward $O$.
    - $a_i,b_i,c_i$: selected lower demands, not automatically actual maxima.
    - $N_+=\#\{i:A_i+B_i>1\}$.
- **Types and gaps.**
    - CE0/CE1/CE2 count positive-length center boundary traces.
    - Vd0 has no positive adjacent-spoke support.
    - Vd1, Vd2, and T3-like are the positive-support classes — [\[CLASSIFICATION\]](CLASSIFICATION.md).
    - $N_{\rm sp}$ counts these positive-support roles.
    - A gap is a nonempty complement of the incident open V traces on one edge, including a singleton.
- **Midpoint-supplier routing.**
    - $k$: unique center midpoint index in a nonzero-gap placement.
    - $\sigma$: unique supercritical index after the count reduction.
    - $\tau$: the neighboring vertex index with $M_\sigma\in U_\tau$ and $\tau=\sigma\pm1$, unique after the reduction when $\sigma\ne k$.
- **Witnesses and enclosure.**
    - $\widehat P_i$: total radial frontier including neighboring contributions — [\[WITNESS\]](WITNESS.md).
    - $\Lambda(K)$: least side length of a closed equilateral triangle containing compact $K$.
    - BC, D, F: active witness families of at most five, four, and nine points.
    - The letter D in a page label names a witness family; it is not a disk.
- **Coverage strength.**
    - Skeleton coverage: perimeter plus the six spokes.
    - Full-hexagon coverage: every point of $H$.
    - N0, BC, D, and the replacement contradiction use skeleton coverage.
    - F and the final area contradiction concern full-hexagon coverage.

---

**Proof sources:** [0000](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/0XXX_main/0000_main_theorem.md) · [2610](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md) · [2612](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
