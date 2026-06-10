# Full Skeleton Noncoverage Postmortem

Status: Failed

The attempted strategy was:

$$
\text{prove seven open unit equilateral triangles cannot cover }S.
$$

Since

$$
H\supset S,
$$

this would have implied the main theorem. The May 24, 2026 counterexample
recorded in `../800_computation/811_skeleton_cover_counterexample.md`
numerically refutes this strategy.

The counterexample gives seven closed equilateral triangles with side
strictly less than $1$ covering every boundary edge and every radial segment
of the full skeleton

$$
S=\partial H\cup [V_0,V_3]\cup [V_1,V_4]\cup [V_2,V_5].
$$

Therefore any future finite-target or propagation strategy must use a stronger
target than $S$, add extra hypotheses, or aim directly at covering $H$ rather
than the skeleton alone.

This postmortem does not invalidate conditional half-skeleton lemmas. It only
records that full-skeleton noncoverage is not a valid global obstruction.
