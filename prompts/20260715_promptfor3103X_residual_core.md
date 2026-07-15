# Prompt For Executing The `3103X` Residual-Core Strategy

Read and analyze this repository:

https://github.com/dylan0301/hexagon-cover-database

You may inspect the Triangle mode in the following visual repository and the
local `3102X_fable5proof` explorers for geometric intuition, but neither is a
proof source:

https://github.com/dylan0301/hexagon-cover-visual/tree/gulgu

## Mission

Close, refute, or make the strongest rigorous progress toward closing the
independent `3103X` residual-core and forced-disk route for the branch

$$
T_C\text{ is CE0},\qquad N_+=1,
$$

with all six vertex roles Vd0.

The canonical strategy note is

`proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/31030_CE0_all_Vd0_residual_core_strategy.md`.

The three terminal obligations are:

1. construct a nonzero symmetric witness $P(a,b)$ and prove its uniform
   membership in $\mathcal C_{\mathrm{sym}}(a,b)$;
2. define $Q_-(a,b),Q_0(a,b),Q_+(a,b)$ exactly and prove their uniform
   membership in $\mathcal C_{\mathrm{asym}}(a,b)$; and
3. prove
   $$
   \Lambda\left(K_{\mathrm{wit}}(a,b)\right)\ge1
   $$
   throughout the full strict parameter domain.

Do not assume these targets are true. Search actively for counterexamples
before investing in a global proof. A rigorous counterexample to a proposed
witness or inequality is a successful result and must be recorded honestly.

## Working And Output Contract

Work directly in the repository and edit the proof package when the result
justifies an edit. You may add reproducible computation or certificate helpers
inside the `3103X` package. Do not commit, push, open a pull request, or modify
unrelated files.

At the end, provide both:

1. repository changes containing the rigorous results, exact counterexamples,
   or substantive recorded progress; and
2. a detailed mathematical report explaining all successful and failed work,
   computations, certificates, file changes, and remaining obligations.

Preserve all existing user changes. Keep every proof status exactly as strong
as its recorded justification permits.

## Current Resolution

The package currently records:

- `31030` is `Status: Strategy` and is the authoritative repository-facing
  description of this route.
- `31031_original_residual_core_draft.md` is a verbatim provenance copy. It is
  not an authoritative status source and must remain byte-for-byte unchanged.
- `4104_all_boundary_transfer_to_310X.md` is `Status: Reduction` and supplies
  strict handoffs plus the interior-uncovered transfer into $T_C$.
- `20091_ab_union_curve_a_plus_b_gt_1.md`,
  `20095_exact_caliper_certificate.md`, and
  `31012_core_graph_two_variable_relaxation.md` are `Status: Proven`.
- the symmetric witness, asymmetric witnesses, and terminal enclosure
  inequality remain `Lemma target` obligations inside the `Strategy` note.

A Reduction proves its routing statement, not its terminal target. Do not
reprove recorded Proven inputs unless an exact audit identifies a concrete
error.

## Required Reading

First read completely:

- `AGENTS.md` and `README.md`;
- `proof/0XXX_main/0000_main_theorem.md`;
- `proof/0XXX_main/0001_proof_tree_index.md`;
- `proof/0XXX_main/0002_status_and_dependencies.md`;
- `proof/09XX_appendices/0910_notation_dictionary.md`;
- `proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md`;
- `31030_CE0_all_Vd0_residual_core_strategy.md` and the provenance-only
  `31031_original_residual_core_draft.md`;
- the local `310X` and `3101X` index notes.

Then inspect at least:

- `1000_problem_statement.md`, `1101_CE_classification.md`,
  `1201_V_triangle_types.md`, and `1212_vertex_rows_and_Nplus.md`;
- `2004_admissible_set.md` and `2005_midpoint_self_cover_lemma.md`;
- the `2009X_ab_set` index together with `20091` and `20095`;
- `2600_minimum_enclosing_triangle_tools.md` and the proved local tools it
  cites;
- `31011_six_point_construction.md`,
  `31012_core_graph_two_variable_relaxation.md`,
  `31013_core_surface_definition.md`, and
  `31016_fixed_angle_g_strategy.md`;
- `4104_all_boundary_transfer_to_310X.md`; and
- the `908X` skeleton counterexample warning.

The empirical `20092` and `20093` named-curve material, plots, visual code,
and imported `3102X` material may suggest candidates, but none may be cited as
proof without a new independently checkable certificate.

## Proof-Safe Setup

Use the selected strict handoff data from `31030` and `4104`. Rotate the unique
supercritical row to $V_4$ and put

$$
a=a_4=1-x_3,
\qquad
b=b_4=x_4.
$$

The strict domain is

$$
\mathcal D
=
\left\{
(a,b):
0<a,b<1,
\ a+b>1,
\ a^2+ab+b^2<1
\right\}.
$$

The handoff chain is

$$
x_3<x_2<x_1<x_0<x_5<x_4.
$$

For each row, use the closed, cone-clipped exact union $R_i(u,v)$. Preserve
the direction of antitonicity:

$$
u'\ge u,\quad v'\ge v
\quad\Longrightarrow\quad
R_i(u',v')\subseteq R_i(u,v).
$$

The model cores are

$$
\mathcal C_{\mathrm{asym}}(a,b)
=
\mathrm{int}(H)
\setminus
\left(
\mathrm{int}\left(R_4(a,b)\right)
\cup
\bigcup_{i\ne4}
\mathrm{int}\left(R_i(1-b,1-a)\right)
\right)
$$

and

$$
\mathcal C_{\mathrm{sym}}(a,b)
=
\mathrm{int}(H)
\setminus
\bigcup_{i=0}^5
\mathrm{int}\left(R_i(1-b,1-a)\right).
$$

Do not replace these by complements of open triangles or by complements on
all of $H$. The plane-interior and closed-union conventions are what make the
transfer into the open center role $T_C$ valid.

## Milestone 1: Audit Concrete Witness Candidates

Begin with the candidates already suggested by the neighboring proved
six-point reduction, but audit rather than assume them.

Put

$$
p=1-b,
\qquad
q=1-a,
\qquad
c_*=c_{\max}(p,q),
$$

where $c_{\max}$ is the exact radial envelope proved in `2004`.

### Symmetric candidate

Test

$$
P(a,b)=(1-c_*)V_0
$$

and its six rotations

$$
P_k=\mathrm{Rot}_{k\pi/3}P,
\qquad k=0,\dots,5.
$$

Prove or refute, throughout all of $\mathcal D$,

$$
P_k\in\mathcal C_{\mathrm{sym}}(a,b)
\qquad(k=0,\dots,5).
$$

For every point, verify membership in $\mathrm{int}(H)$ and exclusion from the
interior of all six comparison row unions. If symmetry reduces the work, prove
the symmetry and the parameter-order preservation explicitly.

### Asymmetric candidates

Test the existing relaxed points

$$
\left(Q_-,Q_0,Q_+\right)
=
\left(P_3^{\mathrm{rel}},P_4,P_5^{\mathrm{rel}}\right)
$$

from `31011` and `31012`, where $P_4$ is the exact line--line junction from
the strict frontier in `20091`.

Prove or refute

$$
Q_-,Q_0,Q_+
\in
\mathcal C_{\mathrm{asym}}(a,b)
$$

throughout $\mathcal D$. Prove exclusion from the distinguished strict row
union and from every one of the five comparison row unions. Frontier
membership for $R_4(a,b)$ alone is insufficient.

Lock the coordinate convention before calculating: `31011` places the copy
$\mathcal U_{AB}(b,a)$ at $V_4$, whereas `20091` states its theorem as
$\mathcal U_{AB}(a,b)$. Audit every swap, reflected formula, circle center,
line coefficient, and selected intersection.

Do not assume $a\le b$. Either treat both halves directly or prove a complete
reflection carrying the formulas, core memberships, and final support
functional from one half to the other.

If any candidate is false, produce an exact rational, algebraic, or certified
interval counterexample. Stop using that candidate. Then either derive a
correct replacement or record the precise failed claim and remaining design
problem.

## Milestone 2: Falsification And Numerical Geometry

Before attempting the terminal proof, implement a proof-safe numerical model
from the exact `20091` and `20095` descriptions. Do not use the empirical
named-curve catalog as ground truth.

Scan the full domain, with special attention to:

- $a+b\to1^+$;
- $a^2+ab+b^2\to1^-$;
- the symmetric line $a=b$;
- the asymmetric limits $(a,b)\to(0,1)$ and $(1,0)$;
- selector and support-label transition loci; and
- configurations where a proposed witness approaches another row union.

For every proposed witness, compute signed membership margins against every
row union. For the witness configuration, compute the optimized enclosing
side length and the active support labels.

A grid, plot, optimizer result, or floating-point margin is only `Empirical`.
Turn an apparent counterexample into an exact symbolic calculation or a
directed-rounding interval certificate before declaring a universal claim
false. Retain reproducible scripts and their invocation instructions only when
they materially support a recorded result.

## Milestone 3: Forced Disk And Enclosure Inequality

Proceed only after the witness memberships survive Milestones 1 and 2.

For the proposed symmetric point,

$$
\lVert P\rVert=1-c_*,
$$

so the six rotations force the centered disk of radius

$$
r(a,b)=\frac{\sqrt3}{2}(1-c_*).
$$

If a replacement symmetric point is used, replace this by
$r=(\sqrt3/2)\lVert P\rVert$ and prove the corresponding sixfold convex-hull
statement.

For

$$
K_{\mathrm{wit}}
=
\mathcal D(a,b)
\cup
\left\{Q_-,Q_0,Q_+\right\},
$$

write the support function as

$$
h_{K_{\mathrm{wit}}}(n)
=
\max\left\{
r,
\left\langle Q_-,n\right\rangle,
\left\langle Q_0,n\right\rangle,
\left\langle Q_+,n\right\rangle
\right\}.
$$

Derive a finite, exhaustive partition by:

- active support label in each of the three directions;
- enclosing-triangle orientation;
- the selected algebraic branch for every witness coordinate; and
- all parameter transition surfaces.

Prune empty cells rigorously. Prefer a short analytic proof using monotonicity,
convexity, calculus, or exact algebra. If that is not available, construct a
finite interval-arithmetic or semialgebraic certificate proving

$$
\Lambda\left(K_{\mathrm{wit}}(a,b)\right)
\ge1
$$

on all of $\mathcal D$.

A computational certificate must include:

- a finite covering of the full parameter and orientation domain;
- outward-rounded enclosures for radicals and witness coordinates;
- proof of every selector and active-support condition, or subdivision at its
  boundary;
- explicit handling of strict-domain limits and equality faces;
- a small independent verifier or independently checkable exact identities;
  and
- reproducible commands and recorded output.

## Repository Integration

Create numbered notes only when they contain a substantive result. Use these
reserved destinations:

- `31032_symmetric_witness_construction.md`;
- `31033_asymmetric_witness_construction.md`;
- `31034_witness_enclosure_inequality.md`.

Use the status actually justified by each file: `Proven`, `Lemma target`,
`Empirical`, or `Failed`. An exact proved counterexample may support a Proven
counterexample statement while the refuted proposed route is recorded as
Failed; do not conflate those meanings.

Place reusable experiment or certificate helpers in a package-local
`3103X_computation/` folder. Do not create empty note shells or retain scratch
files with no reproducibility role.

After substantive changes:

1. update the obligation and dependency ledger in `31030`;
2. add relative links and recorded statuses to the relevant local navigation;
3. update the main status table only if the package status genuinely changes;
4. add every retained note, verifier, and required artifact to
   `proof/MANIFEST.txt`; and
5. keep the `310X` and main proof-tree descriptions synchronized when their
   recorded meaning changes.

Keep a failed witness or counterexample in the active `3103X` package by
default. Do not move it to `9XXX_failed_ideas` unless explicitly instructed.

Before and after all work, compute the checksum of
`31031_original_residual_core_draft.md` and confirm that it is unchanged.

## Forbidden Shortcuts And Warnings

- Do not infer model-core membership from `31012` convex-hull containment.
- Do not infer exclusion from all rows merely from membership on the
  distinguished $AB$-union frontier.
- Do not use `20092`, `20093`, a plot, or visual code as a proved boundary
  description.
- Do not identify actual maximal row reaches with the smaller selected
  handoff demands.
- Do not reverse the antitone inclusion direction for row unions.
- Do not replace $\mathrm{int}(H)$ or the interiors of the closed row unions
  by an unproved open/closed variant.
- Do not assume the model cores are compact or invoke a radial maximizer
  without first producing an appropriate compact subset.
- Do not claim the forced disk lies in either model core; it is forced into
  $T_C$ by convexity of the six rotated witnesses.
- Do not strengthen the midpoint lemma to a strict radial-depth bound below
  $1/2$.
- Do not square inequalities, choose radical roots, divide, or clear
  denominators without recording the necessary sign conditions.
- Do not claim skeleton noncoverage from this full-$H$ route.
- Do not mark `31030`, `3103X`, the all-Vd0 branch, or the main theorem Proven
  unless every required terminal dependency has a complete proof-level
  source.

## Verification

For every repository change:

- run all added experiment and verifier commands;
- check that every relative Markdown link resolves;
- check that every manifest entry exists and every retained new file is
  listed;
- run the repository LaTeX/style searches from `AGENTS.md` on changed files;
- run `git diff --check`;
- inspect `git diff --stat`, `git status --short`, and the full diff for each
  changed file; and
- confirm that every changed status agrees with its source proof or
  certificate.

Do not commit or push the changes.

## Final Report

Organize the final report as:

1. repository status and dependency audit;
2. exact restatement of the domain, cores, and three targets;
3. candidate formulas and coordinate/reflection audit;
4. symmetric witness membership proof or counterexample;
5. asymmetric witness membership proofs or counterexamples;
6. numerical search, active configurations, and limiting families;
7. exact active-support partition for $K_{\mathrm{wit}}$;
8. analytic proof or rigorous certificate for the enclosure inequality;
9. failed approaches, exact counterexamples, and remaining gaps;
10. repository files changed and verification results; and
11. strongest conclusion justified for `3103X`, the all-Vd0 branch, and the
    main theorem.

The outcome is successful if it rigorously closes all three obligations,
rigorously falsifies a required claim and records the failure, or proves a
substantive earlier obligation while leaving every unresolved status honest.
