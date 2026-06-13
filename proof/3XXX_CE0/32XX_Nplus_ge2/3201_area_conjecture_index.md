# Area Conjecture Package

Status: Strategy

This folder records the successful CE0 conditional area-certificate route for
perimeter cut-point configurations.

The main target is the CE0 six-point case.  In CE0 the center triangle has no
positive-length boundary overlap, so the perimeter data is one ordinary cut
point on each of the six boundary edges.

This package does not prove the full area conjecture or the structural formula
for the local maximizer $T(a,b)$.  It records a conditional CE0 analytic
certificate: if the local square-loss bounds for $f(a,b)$ are supplied, then
the CE0 six-point target with at least two supercritical rows follows.  That
conditional certificate is in
[`3208_CE0_conditional_area_certificate.md`](3208_CE0_conditional_area_certificate.md)
(Status: Proven analytic inequality).

The CE0 area-conjecture target is:

$$
\left\lvert \left\lbrace\, i : a_i+b_i>1 \,\right\rbrace \right\rvert\ge2 \quad\Longrightarrow\quad \sum_{i=0}^5 f(a_i,b_i)<5.
$$

## Main CE0 target

Choose one cut point on each boundary edge:

$$
X_i=V_i+x_i(V_{i+1}-V_i), \qquad i=0,\dots,5.
$$

The six cut points determine six vertex rows

$$
(a_i,b_i)=(1-x_{i-1},x_i), \qquad i=0,\dots,5,
$$

with indices modulo $6$.  In the CE0 case, the shared target becomes

$$
\left\lvert \left\lbrace\, i : a_i+b_i>1 \,\right\rbrace \right\rvert\ge2 \quad\Longrightarrow\quad \sum_{i=0}^5 f(a_i,b_i)<5.
$$

Here $f(a,b)$ is the normalized maximum area inside $H$ for a unit vertex
triangle forced to contain the corresponding local boundary data.

If the displayed strict inequality is proved under the correct hypotheses,
then the six vertex triangles contribute less than five unit-triangle areas
inside $H$.  The remaining center triangle contributes at most one
unit-triangle area, so the seven triangles contribute less than the area of
$H$.

The conditional CE0 certificate in
[`3208_CE0_conditional_area_certificate.md`](3208_CE0_conditional_area_certificate.md)
(Status: Proven analytic inequality)
proves the stronger bound

$$
\sum_{i=0}^5 f(a_i,b_i)<\frac{99}{20}
$$

under the local square-loss hypothesis stated there.

## Files

| File | Recorded status | Notes |
|---|---|---|
| [`3202_area_function_and_monotonicity.md`](3202_area_function_and_monotonicity.md) | Strategy / lemma target | Defines $f(a,b)$, records monotonicity, and states the structural conjecture for the local maximizing triangle. |
| [`3203_CE0_six_point_main_target.md`](3203_CE0_six_point_main_target.md) | Strategy | Defines the main CE0 six-point perimeter model and its area target. |
| [`3206_area_conjecture_proof_tree.md`](3206_area_conjecture_proof_tree.md) | Reference | Records the CE0 conditional-certificate proof tree. |
| [`3207_current_status.md`](3207_current_status.md) | Reference | Lists dependencies, open obligations, and what is not yet proved. |
| [`3208_CE0_conditional_area_certificate.md`](3208_CE0_conditional_area_certificate.md) | Proven analytic inequality | Proves the CE0 six-point inequality under the local square-loss hypothesis for $f(a,b)$. |
