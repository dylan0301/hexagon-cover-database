# CE0, $N_+=1$, All-Vd0 Direct Completion

Status: Proven

## Theorem

Seven open unit equilateral triangles cannot cover the side-one regular
hexagon $H$ when

- the center role $T_C$ is CE0;
- all six vertex roles $T_0,\dots,T_5$ are Vd0; and
- exactly one actual maximal boundary row is supercritical.

## Proof

Assume such a cover exists.  We first show that the six vertex roles cover
$\partial H$.

If a point $P\in\partial H$ belonged to none of the vertex roles, the full
cover would force $P\in T_C$.  Since $T_C$ is open, it would contain a plane
ball about $P$.  At a relative-interior point of an edge, this ball contains
a positive-length boundary interval.  At a vertex, it contains such an
interval on each incident edge.  Either case contradicts the CE0 definition
in
[`1101_CE_classification.md`](../../../../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md),
which forbids positive-length center-role contact with a boundary edge.
Therefore

$$
\partial H\subseteq\bigcup_{i=0}^5T_i.
$$

All six vertex roles are Vd0, and the actual-row hypothesis is exactly the
remaining assumption of the center-independent direct theorem
[`31043_center_independent_direct_nine_point_obstruction.md`](31043_center_independent_direct_nine_point_obstruction.md).
That theorem gives a contradiction. $\square$

The CE0 assumption is used only to obtain full vertex-role boundary coverage.
The nine-point obstruction itself is independent of the center class.
