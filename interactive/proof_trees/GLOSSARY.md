# [GLOSSARY] The vocabulary of the proof

[\[MAIN\]](README.md) · [\[START\]](START.md) · [\[NOTATION\]](NOTATION.md)

## Terms used here

This page defines the specialized vocabulary. Individual argument pages repeat the definitions needed to read that page directly. A bracketed page label is a navigation name, not a mathematical variable.

## Tree

- **The objects being covered and used to cover them.**
    - **Unit hexagon:** the closed regular hexagon $H$ with all six sides of length $1$. It includes its perimeter and interior. Its center is $O=0$; its vertices $V_0,\ldots,V_5$ are ordered around the perimeter. Indices repeat modulo $6$.
    - **Unit equilateral triangle:** a triangle with three sides of length $1$, in any position and orientation.
    - **Open triangle $U$:** its interior, excluding its three sides and vertices. **Closure $T=\overline U$:** the same triangle with the sides and vertices included. Membership in $T$ need not give membership in $U$.
    - **Cover:** every point of the stated set belongs to at least one of the seven open triangles. Covering only selected points or only the boundary is weaker than covering $H$.
    - **C triangle:** the open triangle $U_C$ assigned to contain the center $O$. **V triangle:** the open triangle $U_i$ assigned to contain vertex $V_i$. A **role** is simply one of these assignments. They are distinct by the diameter argument in [SETUP](SETUP.md).
    - **Spoke $r_i$:** the segment $[O,V_i]$, not an infinite ray. **Own spoke:** $r_i$ for the triangle at $V_i$. **Neighboring spokes:** $r_{i-1},r_{i+1}$.
    - **Midpoint $M_i$:** $V_i/2$, halfway along a spoke; never the midpoint of a perimeter edge in this guide.
    - **Skeleton $S$:** the perimeter together with all six spokes. Its length is $6+6=12$ because isolated intersection points have zero length. Skeleton coverage need not cover the regions between the spokes.
- **Intersections, reaches, and gaps.**
    - **Trace:** the intersection of a triangle with the specified edge or spoke. **Positive trace/support:** an intersection containing an interval of positive length, not merely a point.
    - **Incident edges:** the two perimeter edges having the given vertex as endpoint. **Adjacent edges:** edges sharing an endpoint. **Relative interior of an edge:** that edge with both endpoints removed.
    - **Actual reaches $A_i,B_i,C_i$:** the farthest distances realized by the closed triangle $T_i$ along the preceding edge from $V_i$, the following edge from $V_i$, and the own spoke from $V_i$ toward $O$.
    - **Selected demands $a_i,b_i,c_i$:** specified lower bounds on those reaches. They are not automatically the actual maxima. A triangle **realizes** a demand when it contains the specified point at that distance.
    - **Supercritical:** $A_i+B_i>1$. **Nonsupercritical:** $A_i+B_i\le1$. $N_+$ counts supercritical V triangles. The threshold concerns boundary length, not triangle area or number of supported spokes.
    - **Boundary gap:** a nonempty portion of a perimeter edge missed by all six open V triangles. It can still be covered by $U_C$. Equality of the two closed trace endpoints leaves a **singleton gap**, a single point still requiring open coverage.
    - **Gap-free:** the open V traces cover that edge completely, so their reaches overlap strictly. **Zero-gap configuration:** the six open V triangles alone cover the whole perimeter. This does not imply CE0.
    - **Center-free edge:** $U_C$ covers no point in that edge's relative interior. It need not be an edge with a gap: the incident V triangles must cover it without help from $U_C$.
- **Support is not the same as supplying a midpoint.**
    - **Positive adjacent support:** $T_i$ meets a neighboring spoke in positive length. $N_{\rm sp}$ counts triangles with at least one such trace, not the number of supported spokes.
    - **Neighboring supplier of $M_j$:** a V triangle $U_i$ with $i=j-1$ or $j+1$ and $M_j\in U_i$. **Rescuer** is a synonym for that same coverage relationship.
    - **Example:** when $M_1\in U_0$, the triangle based at $V_0$ supplies the midpoint on $r_1$. If $T_0$ merely meets $r_1$ away from $M_1$, it has support but is not a supplier of $M_1$.
    - **One-way implication:** supplying an interior spoke midpoint openly gives a small interval around it, hence positive support. The converse is false without midpoint containment.
    - **Center-based supplier:** its vertex index is $k$, where $M_k\in U_C$. It remains a V triangle, not the C triangle. **Away supplier:** its index differs from $k$.
    - **$\sigma$ and $\tau$:** after reduction, $\sigma$ labels the unique supercritical V triangle; $\tau$ labels the neighbor containing $M_\sigma$ when $\sigma\ne k$. Their uniqueness is proved, not assumed for every configuration.
- **The classification labels.**
    - **CE0/CE1/CE2:** the closure of the C triangle meets zero, one, or two boundary edges in positive length. These count traces, not uncovered gaps.
    - For a V triangle, **$o$** counts its vertices outside $H$; **$n$** counts neighboring spokes met in positive length. A vertex on the boundary of $H$ is not outside.
    - **Vd0:** $n=0$; after an exact-trace normalization the possible outside-vertex counts are $o=1,2$.
    - **Vd1:** $(o,n)=(1,1)$. **Vd2:** $(o,n)=(1,2)$. **T3-like:** $(o,n)=(2,1)$. Their classification and normalization are in [CLASSIFICATION](CLASSIFICATION.md).
- **The finite-witness method.**
    - **Witness:** a point selected from the original configuration whose required containment helps exclude the cover. **Fixed** means it is chosen before introducing any candidate enclosing triangle.
    - **Forced into $U_C$:** logically required to belong to the original open C triangle; for example, a point in the covered set excluded from all six V triangles.
    - **Candidate:** any open unit equilateral triangle being tested for containment of the same fixed witnesses. It is not automatically a replacement C triangle completing the old cover.
    - **Convex hull $\operatorname{conv}(K)$:** all convex combinations of points of $K$, meaning averages with nonnegative coefficients summing to $1$. A triangle containing $K$ contains its convex hull.
    - **$\Lambda(K)$:** the smallest side length of a closed equilateral triangle containing nonempty compact $K$ (closed and bounded here). For finite $K$, open unit containment gives $\Lambda(K)<1$ by moving all sides slightly inward.
    - **BC, D, F:** historical names for witness arguments using at most five, four, and nine points. D is not a disk. F obtains an auxiliary disk from a convex hull; BC and D use no disk.
    - **Total radial frontier:** the endpoint closest to $O$ of all V contributions on a spoke, including both neighboring contributors. It is missed by the open V triangles. Its definition and endpoint proof are in [WITNESS](WITNESS.md).
    - **Capacity/envelope:** a bound on how far a triangle can reach while meeting specified boundary demands. $c_{\max}(p,q)$ is maximal own-spoke reach; $C_+(p,q),C_-(p,q)$ are the two neighboring-spoke versions. They are optimization functions, not extra covering triangles.
- **How the estimates are organized.**
    - **Handoff:** a chosen point in the open overlap of two V triangles on their shared edge. Its coordinate is $x_i$; it gives demands $(a_i,b_i)=(1-x_{i-1},x_i)$.
    - **Ascent/descent:** respectively $x_i>x_{i-1}$ or $x_i<x_{i-1}$ in the cyclic sequence. An ascent is equivalent to a selected boundary-demand sum greater than $1$.
    - **Path monotonicity:** nonsupercriticality and strict overlap force preceding-edge reaches to increase and following-edge reaches to decrease along a consecutive V-triangle path.
    - **Tail bound/return:** a tail bound concerns the last triangle on a path. A return propagates inequalities along the path back to an incompatible demand at the beginning.
    - **Chart/normal form:** a declared coordinate description obtained by rotation, reflection, translation, or reparameterization. The geometric points remain the same unless an actual replacement is explicitly stated.
    - **Side slack:** an affine expression whose nonnegative values define a triangle's closed side half-plane; negative values prove exclusion. It need not be Euclidean distance to the line.
    - **Radial exit:** where a candidate C triangle stops along a spoke, measured from $O$. Actual V reaches $C_i$ use the opposite origin, $V_i$.
    - **Adapter:** a lemma checking that a specific placement satisfies the hypotheses of another lemma. **Margin:** positive room in a strict inequality, needed to preserve open containment after a small change.
    - **Length/area budget:** the sum of triangle contributions cannot fall below the length/area of the set being covered. Overlaps can make this sum larger than the union; one never subtracts an unproved overlap estimate.
    - **Calipers/support contact:** rotate the three sides of an enclosing equilateral triangle and track the points or disk touching them. A supporting line leaves the whole convex set on one side. [CALIPERS](CALIPERS.md) defines the support-function formula.
    - **Certificate:** exact identities establishing the signs of required expressions throughout a parameter region. It is not a numerical scan or picture.
    - **Calculation leaf:** the displayed tree stops expanding a long derivation, but states what it assumes and proves and links the numbered source. The guide is self-contained in its vocabulary and argument interfaces, not a duplicate of every polynomial certificate.

**Source ownership:** [SETUP](SETUP.md), [CLASSIFICATION](CLASSIFICATION.md), [SUPPLIER](SUPPLIER.md), [WITNESS](WITNESS.md), and the calculation pages link the numbered mathematical sources for these definitions and implications.
