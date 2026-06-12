# CE1/CE2 Two-Supercritical Set-Cover Strategy

Status: Strategy

This note records a possible certificate-producing computational route for the
branch

$$
T_C\text{ is CE1 or CE2}, \qquad \#\{i:a_i+b_i>1\}\ge2.
$$

The working observation is that previously found almost-covering candidates
appear to have exactly one supercritical row $a_i+b_i>1$, whether the center
case is CE0, CE1, or CE2.  The branch with two or more supercritical
V-triangles has not produced tight candidates.

The suspected mechanism is that supercritical V-rows tend to need Vd1/Vd2-type
adjacent-ray behavior, or comparably strong local pressure, to cover the
half-skeleton.  With two such rows, the vertex triangles become inefficient
enough that a tight covering should fail.

## Discrete half-skeleton target

Choose a finite test set

$$
Q\subset S_{1/2}
$$

containing $O$, the six midpoints, and a discrete mesh of boundary points.  If
no admissible seven-triangle configuration covers $Q$ under the branch
conditions, then no such configuration covers all of $S_{1/2}$.

The mesh should be refined around:

- the CE1 or CE2 active boundary intervals;
- midpoint-neighborhood holes;
- adjacent-ray contact regions for Vd1/Vd2 candidates;
- points where earlier almost-covering configurations nearly close all gaps.

## Candidate enumeration

Use the maximal-triangle search framework from
`../../9XXX_failed_ideas/980X_experiment_plans/9807_maximal_half_skeleton_search.md` and
`../../9XXX_failed_ideas/980X_experiment_plans/9808_maximal_C_triangle_search.md`.

For each case, enumerate finite coverage masks on $Q$:

- one CE1 or CE2 center-triangle mask;
- six vertex-triangle masks, one for each $V_i$;
- the local type of each vertex mask, including Vd0, Vd1, Vd2, and T3-like
  possibilities;
- the row data $(a_i,b_i)$ and whether $a_i+b_i>1$.

The set-covering instance should keep only tuples satisfying

$$
\#\{i:a_i+b_i>1\}\ge2.
$$

For CE2, the certificate must state whether it assumes the CE2 one-interval
lemma.  Without that assumption, both CE2 boundary intervals must remain in the
enumerated center data.

## Set-covering certificate

Solve the resulting finite set-covering problem with the role constraints:

- exactly one center-triangle candidate;
- one candidate for each of the six vertex roles;
- every point of $Q$ covered by at least one chosen candidate;
- CE1 or CE2 center type;
- at least two supercritical rows.

An infeasible solver result is only evidence unless the finite candidate list
dominates the continuous triangle families.  A proof-level certificate should
include:

- exact or interval-certified coverage masks for all points of $Q$;
- a dominance certificate showing every continuous admissible triangle has the
  same or smaller coverage mask than some enumerated candidate;
- the set-covering infeasibility certificate;
- separate handling of boundary degeneracies and equality cases
  $a_i+b_i=1$.

This certificate format should follow
`../../9XXX_failed_ideas/980X_experiment_plans/9809_symbolic_certificate_format.md` and the numerical
evidence policy in `../../0XXX_main/0005_numerical_evidence_policy.md`.

## Relation to other strategies

This strategy is complementary to the area-conjecture route in
`../../3XXX_CE0/32XX_Nplus_ge2/`, which also studies the case with at least two
supercritical rows.  The present route tries instead to certify finite
half-skeleton noncoverage directly.

It is also motivated by the proven CE0 + Vd1/Vd2 half-skeleton obstruction in
`601_CE0_Vd1_Vd2_half_skeleton_theorem.md`, but it does not extend that theorem.
Any Vd1/Vd2 pressure found here must be recorded as a new certified local
condition or kept as computational evidence.
