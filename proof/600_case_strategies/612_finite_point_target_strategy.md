# Finite Point Target Strategy

Status: Strategy

Given a candidate skeleton cover, take the union of the seven triangles. If a gap remains, add a finite test point in the gap.

The May 24, 2026 counterexample in `../800_computation/811_skeleton_cover_counterexample.md` supplies such a skeleton cover. This strategy should now be read as a way to strengthen the target beyond $S$, not as a proof that $S$ itself cannot be covered.

Current target:

$$
S_{\{0.382,0.5,0.634\}}=S_{1/2}\cup\{P_i(0.382),P_i(0.634):i=0, \dots,5\}.
$$

Goal:

$$
\text{prove seven unit triangles cannot cover this finite target.}
$$
