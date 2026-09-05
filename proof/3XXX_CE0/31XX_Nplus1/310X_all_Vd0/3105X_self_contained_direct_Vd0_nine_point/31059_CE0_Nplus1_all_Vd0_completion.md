# CE0, $N_+=1$, Type-Independent Completion

Status: Proven

## Theorem

Seven open unit equilateral triangles cannot cover the side-one regular
hexagon $H$ when the original open roles are $U_C,U_0,\ldots,U_5$, their
closures are $T_C=\overline{U_C}$ and $T_i=\overline{U_i}$,
$O\in U_C$, $V_i\in U_i$, and

- the closed C triangle $T_C$ is CE0; and
- exactly one actual maximal boundary V triangle is supercritical.

## Proof

Assume that such a cover exists.  We first prove that the six vertex roles
cover the entire boundary.

Suppose that a point $P\in\partial H$ belongs to none of the vertex roles.
The full cover then forces $P\in U_C$.  Because $U_C$ is open, it contains a
plane ball about $P$.  If $P$ lies in the relative interior of a boundary
edge, this ball contains a positive-length interval of that edge.  If $P$ is
a vertex, it contains a positive-length boundary interval on each incident
edge.  Either conclusion contradicts the CE0 definition in
[`1101_CE_classification.md`](../../../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md),
which forbids positive-length center-role contact with every boundary edge.
Therefore

$$
\partial H\subseteq\bigcup_{i=0}^5U_i.
$$

The six roles cover $\partial H$, and exactly one actual V triangle is
supercritical.  These are precisely the hypotheses of the center-independent
direct nine-point theorem
[`31058_center_independent_direct_nine_point_obstruction.md`](31058_center_independent_direct_nine_point_obstruction.md),
which gives a contradiction. $\square$

The CE0 assumption is used only to obtain full boundary coverage by the six
vertex roles.  The nine-point obstruction itself makes no assumption on the
center class or the V-type pattern. The historical filename is retained
so existing citations continue to resolve.
