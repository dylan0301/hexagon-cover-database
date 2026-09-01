# Prompt For Simplifying Strategy 2 With Rational Envelopes

Read and analyze this repository:

https://github.com/dylan0301/hexagon-cover-database

## Mission

Find, prove, and integrate simpler rational-envelope arguments for every case
owned by Strategy 2 in the arranged paper.  Use the canonical `3105X`
rational-upper-envelope method as a model for the style of simplification,
but do not assume that its formulas or its special parameter domain transfer
to Strategy 2.

The target paper section is

`arrange/paper_draft/04_strategy2_exact_demand.tex`.

The current Strategy 2 proofs are already rigorous and analytic.  They do not
have an active interval-arithmetic, adaptive-subdivision, branch-and-bound, or
machine-certificate dependency.  The purpose of this task is therefore not to
repair an incomplete proof or to claim removal of a dependency that is already
absent.  The purpose is to replace long radical, selected-root, contact-label,
and case-by-case calculations by shorter rational relaxations wherever those
relaxations remain strong enough to prove the same terminal contradiction.

Do not assume that one rational bound will handle every case.  Separate bounds
for different admissible-set cells, parameter ranges, or terminal branches are
acceptable.  Search actively for counterexamples and loss of strength before
rewriting a proof.  A rigorous demonstration that a proposed relaxation is too
weak is useful progress.  Keep the current Proven proof as the active fallback
for every case that does not receive a complete and genuinely simpler
replacement.

## Working And Output Contract

Work directly in the repository.  The authoritative proof corpus must lead the
paper: record a new reusable inequality or a changed branch proof in `proof/`
before or together with its use in `arrange/paper_draft/`.  Make only surgical
changes supported by a complete proof or an exact, independently checkable
certificate.

Partial success is allowed.  If two of the five Strategy 2 terminal families
admit clean rational-envelope proofs and the other three do not, integrate the
two complete improvements, retain the three existing proofs unchanged, and
report exactly why the unsuccessful relaxations failed.

At the end, provide both:

1. repository changes containing every accepted proof simplification, rigorous
   counterexample, or substantive reusable result; and
2. a detailed mathematical report containing the complete case audit,
   successful and failed bounds, implication directions, repository changes,
   verification results, commit hash, and push result.

Preserve all pre-existing user changes.  Do not rewrite unrelated prose,
rename established concepts, change the case classification, delete fallback
proofs, or change proof status unless the exact source justifies the change.

## Current Resolution

The following facts describe the starting point and must remain accurate.

- The main theorem and every terminal Strategy 2 source listed in
  `arrange/paper_draft/source_ledger.md` currently have recorded status
  `Proven`.
- `04_strategy2_exact_demand.tex` explicitly states that every estimate in
  that section is analytic and that no empirical branch catalogue or
  machine-assisted certificate is used.
- The old `407b_T_hi_Tminus_qright_threshold_certificate.py` and
  `4108_ce1_terminal_verifier.py` scripts are optional historical
  cross-checks, not active paper dependencies.
- `3105X_self_contained_direct_Vd0_nine_point/` is the canonical current
  direct nine-point package.  In particular, `31055` replaces the exact
  radial value by branchwise rational upper envelopes, and `31056` proves the
  resulting signs with fixed global positive-basis identities rather than
  interval subdivision or branch-and-bound.
- Much of Strategy 2 propagates the boundary-output fibers $B_c(a)$,
  $F_c(a)$, and $G_c(a)$ rather than evaluating $c_{\max}(a,b)$ directly.
  Consequently, a rational upper bound for $c_{\max}$ cannot be substituted
  mechanically into the existing proofs.
- The zero-gap CE1/CE2, $N_+=1$, all-Vd0 case is owned by the
  center-independent `31058` obstruction in Strategy 4.  It is not a Strategy
  2 rational-envelope target.
- The CE2 exactly-one-Vd1/Vd2 branch is a Strategy 1/2 hybrid.  Strategy 2
  owns only the complementary no-additional-positive-support placements in
  which, if the unique exceptional role is Vd2, it has no neighboring-midpoint
  rescue.  Do not absorb the Strategy 1 subcases into this task.

An index or `Reference` file supplies navigation only.  Follow its links to
the numbered proof sources and preserve their recorded statuses.

## Required Reading

Before proposing formulas, read completely:

- `AGENTS.md` and `README.md`;
- `proof/0XXX_main/0000_main_theorem.md`;
- `proof/0XXX_main/0001_proof_tree_index.md`;
- `proof/0XXX_main/0002_status_and_dependencies.md`;
- `proof/09XX_appendices/0910_notation_dictionary.md`;
- `proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md`;
- `arrange/ams_paper_generation_guide.md`;
- `arrange/paper_draft/04_strategy2_exact_demand.tex`;
- `arrange/paper_draft/07_exhaustive_assembly.tex`; and
- `arrange/paper_draft/source_ledger.md`.

Read the canonical comparison method completely:

- `proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31050_self_contained_direct_Vd0_nine_point_index.md`;
- `proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31054_four_cap_enclosure_reduction.md`;
- `proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31055_rational_radial_envelopes_and_mixed_reduction.md`;
- `proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31056_global_analytic_mixed_positivity.md`; and
- `proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31057_terminal_nine_point_enclosure.md`.

The older
`proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/31037_rational_cmax_upper_envelope.md`
may be read for provenance, but `31055` is the self-contained active source.

Read the shared local geometry used by Strategy 2:

- `proof/1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md`;
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/20XX_index.md`;
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`;
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2006_T3_like_midpoint_lemma.md`;
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`;
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md`;
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md`;
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md`;
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2013_T3_like_side_tradeoff.md`;
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md`;
- `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2015_Vd2_neighbor_midpoint_cap.md`;
- `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md`;
- `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md`;
- `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md`; and
- `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2108_CE2_two_endpoint_capped_loss.md`.

Then read the terminal packages listed in the next section, including their
local index files and every numbered source used by their Proven assembly.

## Exact Scope And Case Inventory

Audit every item of `prop:demand-branches` in
`04_strategy2_exact_demand.tex`.

### 1. CE1/CE2, $N_+=0$, all Vd0

The authoritative package is

`proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`.

The scope includes the elementary no-active-gap case, the CE1 one-active-gap
case, both orientations of the CE2 one-active-gap case, and the CE2
two-active-gap case.  The one-side and two-endpoint capped-loss lemmas `2107`
and `2108` are central candidate simplification targets.

### 2. CE1/CE2, $N_+=0$, at least one T3-like and no Vd1/Vd2

The authoritative package is

`proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md`.

Audit the exact four-label `Full`, $L$, $T_-$, and $T_+^{\mathrm{hi}}$
inequality, including the one-variable comparison that already replaced the
former interval subdivision.  Do not reintroduce the historical interval
script as a proof dependency.

### 3. CE1/CE2, $N_+=1$, all Vd0 with at least one boundary gap

Read and audit:

- `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md`;
- `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4102_CE2_two_gap_completion.md`;
- `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4106_CE1_one_gap_five_map_completion.md`; and
- `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4107_CE2_one_gap_five_map_completion.md`.

The CE1 right-oriented chain, CE2 right-gap chain, reflected CE2 left-gap
chain, and CE2 two-gap state must all remain explicit.  Every five-map proof
must retain all five actual-row transitions rather than naming only a formal
composition.  A V-gap may be a singleton; do not assume positive length.

### 4. CE1/CE2, $N_+=1$, exactly one T3-like and no Vd1/Vd2

Read and audit:

- `proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md`;
- `proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4131_midpoint_forcing_reduction.md`; and
- `proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md`.

Audit both the T3-like radial/boundary comparison and its use of the strict
free-supercritical envelope.  A rational relaxation that loses the
nonattainment or terminal strictness is not a valid replacement.

### 5. Complementary CE2 exactly-one-Vd1/Vd2 placements

Read and audit:

- `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md`;
- `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`;
- `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`;
- `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md`;
- `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`; and
- `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`.

The adjacent placement contains the main direct Strategy 2 use of
$c_{\max}$.  The nonadjacent `4146` route instead uses the diameter endpoint
bound, the exact CE2 extent comparison, and the Vd1/Vd2 corner normal form.
The pair-replacement `4147` route uses a direct admissible-set half-square
consequence.  Audit these mechanisms separately rather than presuming that
one common $c_{\max}$ envelope controls all three.

The additional-positive-support obstruction `414a` and the Vd2
neighboring-midpoint obstruction `4149` belong to Strategy 1.  Preserve that
hybrid routing and do not claim them as consequences of a Strategy 2 bound.

## The `3105X` Model And Its Limits

In `31055`, the strict domain is

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1.
$$

With complementary variables $p=1-b$, $q=1-a$, $s=p+q$,
$m=\min\{p,q\}$, $M=\max\{p,q\}$, and

$$
\chi=s^4-s^2+mM,
$$

the exact radial value

$$
c_*:=c_{\max}(p,q)
$$

is bounded by

$$
\bar c_L
=
s-
\frac{\chi}{4s^3-2s+m}
\qquad(\chi\le0),
$$

and

$$
\bar c_T
=
s-
\frac{\chi}{1-m}
\qquad(\chi\ge0).
$$

The first proof uses convexity and a tangent-line estimate on the selected
quartic root.  The second uses an exact factorization of the radical branch.
The application then proves the desired overlap for a smaller object obtained
monotonically from the upper bound.

Reuse this proof philosophy, not these formulas.  The inequalities
$mM>(1-s)(2-s)$, $m>1-s$, and $s>2/3$ are special consequences of the
`3105X` domain: $(p,q)$ are complements of a supercritical,
diameter-feasible pair $(a,b)$.  A generic capped Strategy 2 input $(u,v)$
with $u+v\le1$ does not inherit those additional complement inequalities.
Every new envelope must have its own exact domain proof, cell selector,
denominator signs, transition behavior, and monotone implication into the
terminal obstruction.

Also study `2012_high_radial_low_root_bounds.md`.  Its rational trial-point
and root-sign method is already a Strategy 2 example of the desired
simplification style.

## Proof-Safe Implication Direction

On a nonempty diameter-feasible fiber, let the exact radial envelope be

$$
c_{\max}(a,b)
=
\max_{\substack{
0\le c\le1\\
(a,b,c)\in\mathcal A
}}
c.
$$

Suppose a candidate rational function satisfies

$$
c_{\max}(a,b)\le\bar c(a,b)
$$

on a proved domain.  This gives a necessary relaxed feasibility condition

$$
(a,b,c)\in\mathcal A
\quad\Longrightarrow\quad
c\le\bar c(a,b).
$$

It does not prove that the relaxed triples are realizable.  It cannot be used
to assert equality, existence of a maximizing triangle, a contact type, or a
selected algebraic component.

For fixed $a,c$, let $I_c(a)\subseteq[0,1-a]$ be a proved union of cells or
subdomains on which the rational envelope is valid.  Before using it as a
complete relaxed fiber, prove that $I_c(a)$ contains every $b$ for which
$(a,b,c)\in\mathcal A$ and $a+b\le1$.  Then define

$$
\bar F_c(a)
=
\sup_{\substack{
b\in I_c(a)\\
a^2+ab+b^2\le1\\
c\le\bar c(a,b)
}}
b.
$$

The containment of every exact-feasible capped $b$ in this relaxed domain is
what gives the safe directions

$$
F_c(a)\le\bar F_c(a),
\qquad
\bar G_c(a):=1-\bar F_c(a)\le G_c(a).
$$

If a candidate envelope covers only selected cells, use the existing exact map
or another proved upper cap on every omitted cell and take the largest of the
resulting output caps.  Do not silently discard an exact-feasible cell.

Now let an actual row have reaches $(A,B,C)$, let $a,c$ be lower demands, and
assume

$$
A\ge a,
\qquad
C\ge c,
\qquad
A+B\le1.
$$

Exact admissibility and the monotonicity of $F_c$ give

$$
B
\le
F_c(A)
\le
F_c(a)
\le
\bar F_c(a).
$$

If the next boundary handoff gives $A'\ge1-B$, then

$$
A'
\ge
1-B
\ge
1-\bar F_c(a)
=
\bar G_c(a).
$$

Thus compositions of $\bar G_c$ provide safe lower bounds on returning
demands, but they may be too weak to close a strict terminal inequality.  Prove
the direction at every link, verify that every relaxed iterate stays in the
proved domain, and prove a positive terminal margin; do not replace this audit
by informal monotonicity language.

For strict-supercritical rows, separately derive and prove any relaxed version
of the nonattained envelope in `2010`.  A closed upper bound without a strict
gap may not replace the existing supremum argument.

## Milestone 1: Dependency And Use-Site Audit

Before deriving a new formula, make a complete table of every Strategy 2 use
of:

- $c_{\max}(a,b)$;
- $B_c(a)$, $F_c(a)$, and $G_c(a)$;
- the four selected labels and their transition points;
- the free strict-supercritical envelope;
- the one-side and two-endpoint capped-loss lemmas; and
- a radical or implicit selected root that enters a terminal sign.

For each use site record:

1. exact parameter domain and open or closed boundary faces;
2. admissible-set cell or union of cells involved;
3. whether the proof needs an upper bound, lower bound, equality, existence,
   selector, monotonicity, or nonattainment;
4. the required strict terminal margin;
5. every reflected orientation or singleton-gap endpoint; and
6. the authoritative proof source and manuscript location.

This table is the completeness checklist for the rest of the task.

## Milestone 2: Falsification And Candidate Discovery

Use exact symbolic manipulation and high-precision numerical exploration to
locate tight configurations and test candidate rational envelopes.  Explore
every cell boundary, order-change locus, Full-face transition, limiting open
face, and reflected orientation relevant to the use-site table.

Numerical work is for candidate discovery and falsification only.  It is not a
proof and must not change a status.  When a proposed envelope fails, seek an
exact rational or algebraic counterexample and record:

- the exact parameter values;
- the active cell and selected root;
- the sign showing failure;
- whether a restricted-domain version survives; and
- which Strategy 2 terminal cases are affected.

Do not spend time building a global proof around a bound that fails a basic
boundary or tightness audit.

## Milestone 3: Derive Rational Envelopes

Try, in a proof-safe order:

1. tangent or secant bounds for the selected quartic root on a proved convex
   or concave interval;
2. rational trial points whose substitution has a factorable exact sign;
3. rational upper bounds for radicals with all sides and squaring signs
   recorded;
4. domain-specific bounds that exploit the center-trace inequalities of a
   single terminal family; and
5. piecewise envelopes meeting exactly on cell-transition boundaries.

Prefer rational functions with coefficients in $\mathbb Q$.  Fixed algebraic
constants such as $\sqrt3$ are acceptable only when their sign comparisons are
handled exactly and the resulting proof is still materially simpler.

For every candidate prove:

- denominator positivity;
- selected-root and cell conditions;
- all squaring and clearing-denominator signs;
- continuity or the correct one-sided behavior at transitions;
- validity on every claimed boundary face; and
- the exact implication into $\bar F_c$, $\bar G_c$, or the other relaxed
  terminal quantity.

Do not require a single global envelope when two or three simple branchwise
bounds give a shorter proof.

## Milestone 4: Case-By-Case Closure Program

Proceed in the following order unless the dependency audit proves that another
order is strictly better.

### A. Shared capped-map relaxation

Determine whether a small reusable catalogue of rational $\bar F_c$ or
$\bar G_c$ bounds can replace repeated exact label checks without erasing the
genuine high-$c$ downward jump.  State precisely which labels and parameter
ranges remain exact fallbacks.

### B. The CE1 and CE2 one-gap chains

Test the rational maps on `4106` and `4107`.  For every successful replacement
write the starting endpoint demand, all five relaxed scalar iterates, all five
actual-row inequalities, the returning row-$0$ demand, and the strict
incompatibility with row $0$ capacity.  Treat CE1, CE2 right-gap, and reflected
CE2 left-gap separately.  Retain singleton gaps.

### C. The capped-loss arguments

Audit `2107` and `2108`, then their uses in `4013` and `4102`.  A replacement
must prove the same strict sum below one on the full stated domain.  If a
rational estimate covers only the non-tight region, combine it with a short
exact argument on the remaining region only when the combined proof is
shorter and clearer than the existing one.

### D. The `407X` four-label inequality

Test whether rational labelwise envelopes collapse the existing `Full`, $L$,
$T_-$, and $T_+^{\mathrm{hi}}$ table.  Preserve the exact selected component
and the transition discontinuity.  Do not replace the current analytic
one-variable finish with interval subdivision.

### E. The `413X` exactly-one-T3 branch

Test rational bounds for the T3-like radial/edge comparison and the
strict-supercritical output.  Preserve midpoint forcing, the normalization,
and the nonattained strict terminal inequality.

### F. The `414X` complementary placements

Begin with the explicit adjacent-placement estimate

$$
c_{\max}\left(\frac12+A,H\right)
\le
1-\frac H3.
$$

Determine whether a reusable rational envelope proves this comparison more
directly.  Separately test whether rational estimates simplify `4146`'s
diameter/extent comparison or `4147`'s admissible-set half-square consequence;
do not presume that either route is governed by the same $c_{\max}$ envelope.
Preserve all placement alternatives and the Strategy 1/2 hybrid boundary.

## Milestone 5: Acceptance Criteria For A Replacement

Adopt a rational-envelope proof only if all of the following hold:

1. it covers the complete domain and every orientation claimed;
2. every implication direction and strict inequality is proved;
3. it depends only on sources with sufficient recorded status;
4. it is shorter or conceptually clearer than the existing exact proof;
5. any exact computation is independently reproducible and described as such;
6. it introduces no interval arithmetic, adaptive subdivision, pruning, or
   branch-and-bound as an active proof dependency; and
7. the old proof remains available until the replacement and paper build have
   passed the final audit.

Exact deterministic symbolic computation, integer-polynomial identities, or
global positive-basis identities are permitted.  Prefer a direct analytic
inequality when it is genuinely simpler.  Do not manufacture a large
certificate merely to call its inputs rational.

## Repository Integration

Create a new proof note only when it contains a substantive exact result.

- If one reusable theorem serves multiple Strategy 2 packages, use the
  currently available destination
  `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2016_strategy2_rational_envelope_bounds.md`
  and add it to `20XX_index.md` and `proof/MANIFEST.txt`.
- If a result is genuinely branch-specific, keep it in the owning `401X`,
  `407X`, `410X`, `413X`, or `414X` package.  Follow that package's local
  numbering and index conventions rather than forcing it into `2016`.
- Put reproducible helper programs beside the proof package they support.
  Do not retain exploratory scratch files with no reproducibility role.
- Use `Status: Proven` only for a complete proof or independently checkable
  exact certificate.  Use `Empirical`, `Lemma target`, or `Failed` when that is
  the strongest justified label.
- Update every affected local index, dependency ledger, main status table, and
  `proof/MANIFEST.txt` only to the extent required by the accepted result.
- Do not change the main theorem's status or case classification merely
  because an alternative proof became shorter.

After proof integration, update the arranged paper surgically:

- simplify `arrange/paper_draft/04_strategy2_exact_demand.tex` only for
  accepted replacements;
- synchronize `arrange/paper_draft/source_ledger.md` and
  `arrange/ams_paper_generation_guide.md`;
- place genuinely necessary long exact formulas in
  `arrange/paper_draft/appendix_exact_formulas.tex` and certificate material in
  `arrange/paper_draft/appendix_certificates.tex`;
- modify `arrange/paper_draft/07_exhaustive_assembly.tex` only if a source
  label or routing description actually changes; and
- regenerate the tracked `arrange/paper_draft/main.pdf` from the accepted
  sources.

Do not remove the current proof text until its replacement is complete.  When
only part of a proof is simplified, preserve the untouched exact portion and
make the new dependency boundary explicit.

## Forbidden Shortcuts And Warnings

- Do not claim that Strategy 2 currently depends on interval arithmetic or
  branch-and-bound.
- Do not copy the `31055` formulas outside their proved strict domain.
- Do not infer realizability, equality, contact type, or a selected root from
  the necessary condition $c\le\bar c(a,b)$.
- Do not reverse the directions $F_c\le\bar F_c$ and
  $\bar G_c\le G_c$.
- Do not compose relaxed maps before proving that every actual-row handoff has
  the required direction.
- Do not identify actual maximal reaches $(A_i,B_i,C_i)$ with smaller demand
  variables $(a_i,b_i,c_i)$.
- Do not silently replace open roles by closed roles or lose strictness at an
  endpoint.
- Do not discard singleton V-gaps or merge the two CE2 one-gap orientations.
- Do not smooth away the genuine downward jump in the high-radial capped map.
- Do not use a formal radical root without proving the geometric component
  selector.
- Do not square, divide, clear a denominator, or apply monotonicity without
  recording the needed sign and domain conditions.
- Do not treat a numerical optimizer, plot, random search, or floating-point
  sample as a proof.
- Do not promote an optional historical verifier to an active dependency.
- Do not claim global noncoverage of the skeleton from a branch-specific
  argument.
- Do not delete failed routes, counterexamples, or existing exact fallbacks.
- Do not commit unrelated pre-existing changes, create a feature branch, open
  a pull request, or force-push.

## Verification

For every accepted repository change:

- run every added exact derivation and verifier command;
- record exact outputs, polynomial digests, or coefficient checks needed for
  reproducibility;
- confirm that every relative Markdown link resolves;
- confirm that every new retained proof or helper is listed in
  `proof/MANIFEST.txt` and every manifest entry exists;
- run the relevant LaTeX and Markdown style searches from `AGENTS.md` on all
  changed files;
- run `git diff --check`;
- inspect `git diff --stat`, `git status --short`, and the complete diff of
  every changed file;
- confirm that each recorded status agrees with its exact source;
- compile from `arrange/paper_draft/` with
  `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex`;
- inspect the build for errors, undefined references, undefined citations,
  missing inputs, missing fonts, and stale output; and
- confirm that the tracked `main.pdf` was regenerated after the final source
  change.

The final paper must still display every five-link one-gap chain, preserve all
terminal cases in the exhaustive assembly, and state computation no more
strongly than its certificate justifies.

## Direct Commit And Push To `main`

Work directly on `main` and publish the accepted result without a feature
branch or pull request.

At the beginning:

1. run `git branch --show-current`, `git status --short`, and inspect all
   pre-existing changes;
2. if the current branch is not `main`, switch with `git switch main` only when
   doing so is safe for every pre-existing change; otherwise stop and report
   the exact blocker rather than working or committing on the wrong branch;
3. run `git fetch origin`;
4. run `git rev-list --left-right --count origin/main...main` and inspect
   `git log --oneline origin/main..main`;
5. if local `main` is ahead or diverged because of any pre-existing commit,
   stop before editing or pushing it as part of this task;
6. if the worktree is clean and local `main` is only behind, fast-forward with
   `git pull --ff-only origin main`;
7. if changing branches or fast-forwarding would disturb pre-existing work,
   preserve that work, do not discard, reset, stash, or overwrite it, and stop
   before editing until `main` can be synchronized safely; and
8. record the exact baseline so task-owned changes can be separated later.

Before committing:

1. rerun the complete verification above;
2. stage only explicit task-owned files or hunks; never use an indiscriminate
   `git add -A` or `git add .`;
3. inspect `git diff --cached --check`, `git diff --cached --stat`, and the
   complete staged diff;
4. confirm that no unrelated or pre-existing change is staged; and
5. commit directly on `main` with the message
   `Audit Strategy 2 rational envelope simplifications`.

Then run `git fetch origin` again, inspect
`git rev-list --left-right --count origin/main...main`, and inspect the full
outgoing range `git log --oneline origin/main..main`.  Before pushing, that
range must contain exactly the single task commit and no pre-existing commit.
If `origin/main` has not advanced, push with `git push origin main`.  If it has
advanced, never force-push.  Rebase the single task commit onto the updated
`origin/main` only when the worktree is clean and the rebase is conflict-free,
rerun the full verification, confirm again that the outgoing range contains
only the task commit, and then push.  If a conflict occurs or unrelated work
cannot be separated safely, run `git rebase --abort` if a rebase is active,
then stop and report the exact blocker instead of overwriting another change.

After a successful push, record `git rev-parse HEAD`, confirm that local
`main` and `origin/main` point to that commit, and include the commit hash and
push result in the final report.

## Final Report

Organize the final report as:

1. initial repository, branch, status, and dependency audit;
2. complete Strategy 2 use-site table;
3. exact statement of every proposed rational envelope and its domain;
4. counterexample and tightness search, with exact failures distinguished
   from numerical evidence;
5. proof of every accepted envelope, including selectors and denominator
   signs;
6. derivation of each relaxed $\bar F_c$ and $\bar G_c$ map and the safe
   propagation direction;
7. a five-family matrix with the old mechanism, proposed simplification,
   success or failure, adopted proof, and retained fallback;
8. full CE1/CE2 one-gap chain audit, including both CE2 orientations;
9. capped-loss, `407X`, `413X`, and `414X` results;
10. failed approaches, rigorous counterexamples, and remaining opportunities;
11. proof-corpus and arranged-paper files changed;
12. verifier, style, link, manifest, and XeLaTeX results; and
13. commit hash, confirmation of the push to `origin/main`, and the strongest
    conclusion justified without changing the theorem's recorded status.

The task is successful if it rigorously simplifies one or more Strategy 2
cases while preserving complete case coverage, or if it rigorously shows why
the natural rational relaxations are too weak and records a reusable exact
result.  It is not successful to replace a current analytic proof by an
uncertified approximation, a longer opaque certificate, or an overstated
claim.
