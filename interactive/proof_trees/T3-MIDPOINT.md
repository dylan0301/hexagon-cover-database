# [T3-MIDPOINT] A T3-like role misses its own midpoint

[\[MAIN\]](README.md) · [\[MIDPOINTS\]](MIDPOINTS.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Neighboring support and supplier.** The neighboring spokes for a V triangle at $V_i$ are $r_{i-1},r_{i+1}$. It has **positive adjacent support** if its closure meets one of those spokes in an interval of positive length. A **neighboring supplier of $M_j$** is specifically a triangle $U_i$ with $i=j-1$ or $j+1$ and $M_j\in U_i$. “Rescuer” means the same thing here. Supplying a midpoint implies positive support by openness; positive support alone does not imply supplying that midpoint. $N_{\rm sp}$ counts V triangles having positive adjacent support.
- **Type labels.** CE0, CE1, CE2 count the boundary edges met by $T_C$ in positive length; they do not count gaps. For a V triangle let $o$ count its vertices outside $H$, and $n$ its neighboring spokes met in positive length. Vd0 means $n=0$; Vd1 means $(o,n)=(1,1)$; Vd2 means $(1,2)$; T3-like means $(2,1)$. The names are labels, not additional assumptions.
- **Chart and side slack.** A chart is a coordinate description, not a new geometric object. Here $X=V_0+x(V_1-V_0)+y(V_5-V_0)$, so the local wedge is $x,y\ge0$, the center has coordinates $(1,1)$, and neighboring spokes lie on $x=1$ or $y=1$. A side slack is an affine function whose nonnegative values define one closed half-plane of the triangle. A negative value proves exclusion even from the closure.

**Statement.** If an original vertex role is T3-like, then $M_i\notin T_i$. This is a short side-inequality check, not a calculation leaf.

## Tree

- **Normalize the vertex and supported spoke.**
    - Use $V_0=(0,0)$, $O=(1,1)$, $M_0=(1/2,1/2)$ in the local wedge coordinates.
    - Reflect so that the positive neighboring support is on the spoke $x=1$.
    - The T3-like orientation has the Type-II side description below, with $0<t<1$.
    - Set $z=\sqrt{1-t+t^2}$ and $\Delta=z^2$.
- **Write the relevant sides.**
    - $F(x,y)=\alpha+(1-t)x+ty\ge0$.
    - $G(x,y)=\beta+tx-y\ge0$.
    - $F+G\le z$, where $\alpha,\beta>0$ and $\alpha+\beta<z$.
    - The unique wedge vertex has first coordinate $(z-\alpha-t\beta)/\Delta$.
- **Use positive neighboring support.**
    - This first coordinate exceeds $1$.
    - Therefore $\beta<(z-\alpha-\Delta)/t<(z-z^2)/t$.
    - The identity $t(1-t)-2(z-z^2)=(1-z)^2>0$ gives $\beta<(1-t)/2$.
- **Test the own midpoint.**
    - $G(M_0)=\beta+t/2-1/2=\beta-(1-t)/2<0$.
    - Hence $M_0$ lies outside the closed triangle.
- **Undo the normalization.**
    - Every original T3-like role misses its own midpoint.
    - In the unique-supplier configuration, a T3-like supplier must therefore be based at the center midpoint index — [\[SUPPLIER\]](SUPPLIER.md).

## Why this chart is sufficient

Type I is the alternative coordinate form $F=\alpha+y-tx\ge0$, $G=\beta+x-(1-t)y\ge0$, $F+G\le z$, with the same $z=\sqrt{1-t+t^2}$. The local classification in source 1201 shows that a Type-I triangle with two outside vertices has no positive neighboring support. Hence a T3-like role must use the Type-II chart (after reflection). The endpoint orientations $t=0,1$ likewise have no positive neighboring support. No translation of the original role is used in the midpoint test.

---

**Proof sources:** [1201](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) · [2613](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2613_midpoint_supplier_reduction.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
