# [C-MIDPOINT] Exactly one center midpoint

[\[MAIN\]](README.md) · [\[MIDPOINTS\]](MIDPOINTS.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Trace and side slack.** A trace is the intersection with a hexagon edge; positive length excludes a singleton. An affine **side slack** is a linear expression plus a constant, chosen so $F\ge0$ describes one triangle half-plane and $F>0$ its interior. It need not equal Euclidean distance to the side. The local coordinates $(b,a)$ below have origin $V_0$ and basis $V_1-V_0,V_5-V_0$, so the global center $O$ has coordinates $(1,1)$.

**Statement.** If $O\in\operatorname{int}(T_C)$ and $T_C$ has a positive-length trace on a boundary edge, then exactly one spoke midpoint lies in $T_C$, and that midpoint lies in its interior. The hypothesis that $O$ is interior is essential.

## Tree

- **Normalize one positive trace to $e_{0,1}$.**
    - Use $X=V_0+b(V_1-V_0)+a(V_5-V_0)$.
    - Reflect if necessary to obtain $0<\lambda<1$; set $\rho=\sqrt{1-\lambda+\lambda^2}$.
    - Let the trace endpoints be $s<t$ in edge parameters.
    - The triangle is defined by three nonnegative affine side slacks:
        - $F_1=\lambda b+(1-\lambda)a-\lambda s$.
        - $F_2=-b+\lambda a+t$.
        - $F_0=(1-\lambda)b-a+\rho+\lambda s-t$.
    - Their sum is $\rho$.
- **Evaluate the slacks at the center.**
    - Put $\kappa_j=F_j(O)>0$; thus $\kappa_0+\kappa_1+\kappa_2=\rho$.
    - Positive trace length is equivalent to $\kappa_0+(1-\lambda)\kappa_2<P$, where $P=\rho(1-\rho)$.
    - Since $P=\lambda(1-\lambda)\rho/(1+\rho)$:
        - $\kappa_0<P<\lambda(1-\lambda)/2$.
        - $\kappa_2<P/(1-\lambda)<\lambda/2$.
        - $\kappa_1>\rho-P/(1-\lambda)=\rho(\rho-\lambda)/(1-\lambda)>1/2$.
    - The last comparison follows from $2\rho(\rho-\lambda)-(1-\lambda)=(1-\lambda)(\rho-\lambda)/(\rho+\lambda)>0$.
- **Substitute the six midpoint coordinates into the side inequalities.**
    - $M_0$ needs $\kappa_1\ge1/2$; the strict inequality puts it inside.
    - $M_1$ needs $\kappa_2\ge\lambda/2$; it fails.
    - $M_2$ needs $\kappa_2\ge1/2$; it fails.
    - $M_3$ needs $\kappa_0\ge\lambda/2$; it fails.
    - $M_4$ needs $\kappa_0\ge1/2$; it fails.
    - $M_5$ needs $\kappa_0\ge(1-\lambda)/2$; it fails.
- **Locate any companion boundary trace.**
    - The center classification permits only a trace adjacent to $e_{0,1}$.
    - On $e_{1,2}$, parameterized by $a=q,b=1+q$, the side slack is $F_2=t-1-(1-\lambda)q$.
    - Since $t=\kappa_2+1-\lambda<1-\lambda/2$, this slack is negative.
    - Thus the only possible companion edge is $e_{5,0}$.
- **Undo the symmetry.**
    - There is a unique index $k$ with $M_k\in U_C$.
    - All other $M_i$ lie outside $T_C$.
    - Every possible gap lies on one of the two edges incident with $V_k$.

## Why the open-center hypothesis stays visible

The closed triangle $\operatorname{conv}\{O,V_0,V_1\}$ contains both $M_0$ and $M_1$ and overlaps a boundary edge. It is not a counterexample: $O$ lies on its boundary, not in its interior.

---

**Proof sources:** [2100](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md) · [2109](https://github.com/dylan0301/hexagon-cover-database/blob/f7fe2f89cde04903cba8ba347bd0645abee9b905/proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
