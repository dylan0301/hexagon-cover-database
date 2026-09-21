# [CLASSIFICATION] Local classes without a large case grid

[\[MAIN\]](README.md) · [\[SETUP\]](SETUP.md) · [\[NOTATION\]](NOTATION.md) · [\[USE\]](USING.md) · [\[GLOSSARY\]](GLOSSARY.md)

## Terms used here

- **Geometry and triangles.** $H$ is the closed regular hexagon of side $1$, with center $O=0$ and vertices $V_0,\ldots,V_5$ in cyclic order. Indices are modulo $6$ (so $V_6=V_0$). A **spoke** is $r_i=[O,V_i]$; its midpoint is $M_i=V_i/2$. The boundary edge $e_{i,i+1}=[V_i,V_{i+1}]$ has parameterization $X_i(t)=(1-t)V_i+tV_{i+1}$, $0\le t\le1$.
- **C triangle and V triangles.** $U_C$ is an open unit equilateral triangle containing $O$; $U_i$ is one containing $V_i$. A **role** means one of these assigned triangles. Their closures $T_C,T_i$ include their sides and vertices; the open triangles do not. Coverage always uses the open triangles. A **trace** is intersection with the stated edge or spoke; the **relative interior** of an edge removes its endpoints.
- **Reaches and criticality.** $A_i$ and $B_i$ are the actual lengths reached by $T_i$ from $V_i$ toward $V_{i-1}$ and $V_{i+1}$, respectively. $C_i$ is its actual distance along its own spoke from $V_i$ toward $O$. **Supercritical** means $A_i+B_i>1$; **nonsupercritical** means $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. Lowercase $a_i,b_i,c_i$ are selected lower bounds, not necessarily these maxima.
- **Gaps and skeleton.** A **boundary gap** is a nonempty part of an edge missed by all six open V triangles. On $e_{i,i+1}$ it is $X_i([B_i,1-A_{i+1}])$ when $B_i+A_{i+1}\le1$; equality leaves one missing point. The **skeleton** is $S=\partial H\cup\bigcup_i r_i$, of length $12$. Skeleton coverage need not cover points between the spokes.
- **Trace, incidence, and coordinates.** A trace is the intersection of a triangle with the edge or spoke being discussed; positive trace means positive length, not a single contact point. Two edges are adjacent when they share a vertex. A **local wedge** is the $120^\circ$ corner region at a hexagon vertex. The local coordinates below are coefficients along the two edge directions, not Cartesian coordinates. Their origin is $V_0$, not the global center $O$.

**Purpose:** identify the few local types, without splitting the global proof into all possible six-role type patterns.

## Tree

- **Classify the center by positive-length boundary traces.**
    - Relative-interior points of nonadjacent hexagon edges are more than distance $1$ apart.
        - For edges $e_{0,1}$ and $e_{2,3}$, their squared distance minus $1$ is $(1-t)(2-t)+s(s+t)>0$, for $0<t,s<1$.
        - For opposite edges, it is $(t+s-1)^2+2>0$.
    - A unit triangle has diameter $1$; it cannot meet two nonadjacent edges in positive length.
    - Among any three hexagon edges, two are nonadjacent.
    - Therefore the center has at most two positive traces, and two such traces are adjacent.
        - **CE0:** no positive trace.
        - **CE1:** exactly one positive trace.
        - **CE2:** exactly two positive traces.
    - These are trace classes, not gap counts; a center trace can overlap boundary already covered by vertex roles.
- **Classify a vertex triangle by which neighboring spokes it meets in positive length (its support).**
    - Let $n$ count adjacent spokes met in positive length; let $o$ count triangle vertices outside $H$.
    - Since $V_i$ is an interior point of its triangle but an extreme point of $H$, at least one triangle vertex is outside $H$.
    - Work in local coordinates $V_0=(0,0)$, $O=(1,1)$, with metric $x^2+y^2-xy$.
        - Within distance $1$ of $V_0$, membership in $H$ is equivalent to $x,y\ge0$.
        - Adjacent spokes lie on $x=1$ and $y=1$.
    - **One adjacent support requires at least one vertex in $H$.**
        - A vertex with $x>1$ and distance at most $1$ lies in the local wedge, hence in $H$.
        - If the maximal $x$ equals $1$, positive support requires a whole side on $x=1$; its endpoints lie in $H$.
    - **Two adjacent supports require at least two vertices in $H$.**
        - Otherwise the same unique inside vertex would need $x>1$ and $y>1$.
        - But $x^2+y^2-xy=(x-y)^2+xy>1$.
    - The possibilities are therefore:
        - **Vd0:** $n=0$, with $o=1,2$, or initially $3$.
        - **Vd1:** $(o,n)=(1,1)$.
        - **Vd2:** $(o,n)=(1,2)$.
        - **T3-like:** $(o,n)=(2,1)$.
- **Normalize a raw $(3,0)$ role without changing coverage.**
    - Inside the local wedge, only one triangle side cuts out the trace; the other two side inequalities are redundant there.
    - Translate parallel to that active side until a triangle vertex first reaches an endpoint of the cut.
    - The active cutting line is unchanged; the first new contact lies on its already-excluded open boundary.
    - Hence both the open trace and the closed trace in $H$ stay unchanged.
    - The resulting role has $(o,n)=(2,0)$; all actual reaches and $N_+$ are preserved.
    - This is exact-trace normalization, not the different T3-like closed-trace domination translation.
- **Use the classes only when they matter.**
    - Positive-support roles are Vd1, Vd2, and T3-like; their number is $N_{\rm sp}$.
    - Their boundary caps make them nonsupercritical — [\[LENGTH\]](LENGTH.md).
    - Their midpoint behavior is explained in [\[MIDPOINTS\]](MIDPOINTS.md).

---

**Proof sources:** [1101](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md) · [1201](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) · [2500](https://github.com/dylan0301/hexagon-cover-database/blob/c9baa75d090ee888fa85b575bdfb061f244197d0/proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md). All source links are pinned to the same repository snapshot.

[\[MAIN\]](README.md) Return to the main tree.
