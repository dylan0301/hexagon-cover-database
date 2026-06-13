# May 21/22 Pattern A Four-Point Package

Status: Strategy

This folder records the current state of the May 21/22 four-point Pattern A obstruction.

The package concerns the constrained slice

$$
p=t_0=t_1,\qquad q=t_2=t_3,\qquad r=t_4=t_5,\qquad q<r,\qquad q\le p\le r,
$$

with the strict local AB-union triangle at $V_4$. It focuses on the lower outside-quarter region

$$
q<\frac14,
$$

and on the Pattern A support configuration for the four points

$$
P_3,\quad P_5,\quad G_0,\quad G_2.
$$

The exact nondegenerate strict $AB$-union frontier formula used for the
$R_4$ boundary, including the two unit-circle arcs and two line segments, is
recorded in
[../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009_ab_union_curve_a_plus_b_gt_1.md](../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009_ab_union_curve_a_plus_b_gt_1.md).

The current result is not a full proof of the May 21/22 target. The proven part is a reduction and endpoint theorem for Pattern A. The remaining non-endpoint monotonicity certificate is supported by Bernstein/root-isolation experiments but is not yet a complete finite certificate.

## Working strategy

The reduced Pattern A problem is treated in two regimes.

First, near the endpoint $r=0$, direct interval arithmetic is too coarse. The branch conditions for the selected $P_3$ and $P_5$ points become nearly sharp there; for example, inequalities such as $Q_A\ge0$ can have very small slack. Instead, `623_endpoint_taylor_remainder.md` expands the selected branches and the function $\tau(sr,r)$ as Taylor series in $r$. The proof then shows that the positive low-order terms dominate the higher-order error terms on

$$
0<r\le\frac1{200}.
$$

A typical example of the logic is: after writing

$$
F_I(sr,r)=P_I^{(5)}(s,r)+E_I(s,r),
$$

one proves a concrete lower bound for the fifth-order polynomial $P_I^{(5)}$ and a concrete upper bound for the remainder $E_I$. If the polynomial lower bound is larger than the possible error, then $F_I>0$ throughout the endpoint box. This is why the endpoint part is recorded as a proven analytic inequality rather than a numerical experiment.

Second, away from the endpoint, the intended method is a finite subdivided-box certificate. The non-endpoint region is

$$
\frac1{200}\le r\le\frac{\sqrt{37}-3}{8}.
$$

On this region the goal is not to sample many points, but to cover the whole domain by boxes in $(s,r)$ and certify each box. A simple model example is: if a polynomial $P(s,r)$ is converted to Bernstein form on a rectangle and every Bernstein coefficient is positive, then $P>0$ on the whole rectangle. In the actual Pattern A problem, this idea is used to certify root isolation, branch selection, coordinate bounds, and the derivative signs

$$
\widetilde F_{I,s}>0,\quad \widetilde F_{I,r}>0,\quad \widetilde F_{II,s}>0,\quad \widetilde F_{II,r}>0.
$$

For branch selection, the quartic equations for $P_3$ and $P_5$ may have several algebraic roots. The certificate must show that the chosen root interval contains the selected root and that the active inequalities, such as $P_A,Q_A,S_A\ge0$ and $D_A^2\le1$, hold on the whole box. For recovered coordinates such as

$$
u=\frac{N(v,s,r)}{D(v,s,r)},
$$

the sharper strategy is to certify bounds like $\ell\le u\le h$ by Bernstein signs of polynomial inequalities, rather than by ordinary interval evaluation of $N/D$.

Thus the intended proof architecture is:

1. reduce Pattern A to scalar inequalities;
2. eliminate $p$ by the monotone envelope theorem;
3. prove the tight endpoint range by Taylor expansions with rigorous remainders;
4. prove the remaining non-endpoint range by a finite Bernstein/root-isolation certificate.

Only steps 1, 2, and the endpoint part of step 3 are currently proved in this folder. Step 4 is still empirical/certificate-prototype status until a complete finite box cover is recorded.

## Files

- `621_setup_and_patternA_reduction.md`
  - Defines the local coordinates, the selected $P_3,P_5$ branches, the radial points $G_0,G_2$, the Pattern A support formula, and the reduced inequalities.
- `622_radial_monotone_envelope.md`
  - Proves the monotone envelope theorem eliminating the parameter $p$ from Pattern A.
- `623_endpoint_taylor_remainder.md`
  - Proves the endpoint theorem for $0<r\le 1/200$ using Taylor remainders.
- `624_nonendpoint_bernstein_status.md`
  - Records the Bernstein certificate strategy, verified boxes, and the remaining non-endpoint gap.
- `625_numerical_tests_and_counterexamples.md`
  - Records numerical tests, earlier four-point counterexamples, and the exact status of the outside-quarter version.
- `626_current_status.md`
  - Short dependency and status table.
- `627_original_prompt_context.md`
  - Records the original May 21/22 visualization prompts, including the sector-enlarged intuition, midpoint-window alternative, five-point variant, and quadrilateral lemma reference.
- `628_reduction_prompt_spec.md`
  - Self-contained rigorous May 21/22 reduction specification imported from the `proof2/conj0521-reduction-prompt.md` source.
- `629_alternate_strategies_spec.md`
  - Self-contained Strategy A / Strategy B specification imported from the `proof2/conj0521-alternate-strategies-prompt.md` source.

## External prompt sources imported

The original prompt material is summarized in `627_original_prompt_context.md`.  The more rigorous `proof2` prompt sources are recorded in `628_reduction_prompt_spec.md` and `629_alternate_strategies_spec.md`.

The quadrilateral lemma itself is recorded as a proven local lemma in:

- `../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2607_minimal_enclosing_equilateral_quadrilateral_lemma.md`

## Code

Prototype numerical and certification scripts are under:

- `proof/9XXX_failed_ideas/962X_may21_four_point_failure/962X_computations/9629_README.md`
- `proof/9XXX_failed_ideas/962X_may21_four_point_failure/962X_computations/9632_pattern_a_numeric_scan.py`
- `proof/9XXX_failed_ideas/962X_may21_four_point_failure/962X_computations/9631_endpoint_taylor_check.py`
- `proof/9XXX_failed_ideas/962X_may21_four_point_failure/962X_computations/9630_bernstein_bounds.py`

These scripts are not proof by themselves. They are reproducibility aids for the empirical and certificate-prototype claims in this folder.

## Status summary

Proven in this folder:

$$
\min_{q\le p\le r}\{\rho(r,p)+\rho(p,q)\} = \begin{cases} \rho_2(r,q)+q, & q\ge \sigma(r),\\ r-\sigma(r)+\rho_2(\sigma(r),q), & q<\sigma(r), \end{cases}
$$

and

$$
F_I(sr,r)>0,\qquad F_{II}(sr,r)>0
$$

on the endpoint range $0<r\le 1/200$.

Still open in this folder:

$$
\widetilde F_{I,s}>0,\quad \widetilde F_{I,r}>0,\quad \widetilde F_{II,s}>0,\quad \widetilde F_{II,r}>0
$$

on the full remaining non-endpoint region $1/200\le r\le (\sqrt{37}-3)/8$.
