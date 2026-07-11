# The hole never fits, version 2: tight witnesses, implicit points

This is the design outline for the **second-generation proof** of the
hole-set theorem. It assumes nothing from the reader beyond §§1–3 of
`proof_outline.md` (the objects, the fitting criterion F > h, and the
two-parameter reduction — those carry over verbatim). What changes is
everything after that: **which points witness the inequality, how they are
described, and what kind of certificate proves the final claims.**

The v1 proof (currently being finished) works, but its case table is large
— about 56 angle-interval cases across five parameter regions, many split
further — and the document explains *why* v1 is large and how v2 collapses
it.

---

## 1. Diagnosis: where v1's cases come from

In v1, every witness point is an **explicit formula**: a rational function
of (s,t) *approximating* a geometric feature of the hole, plus a small
inward push to keep it safely inside. Three consequences:

1. **Finite reach.** A fitted formula tracks its feature well only on part
   of the parameter region and part of the angle range; where the fit
   drifts, its margin dies and a new case with a new fit must take over.
   Most of v1's interval subdivisions, tie boundaries, and repair rounds
   exist to manage fit drift — not geometry.
2. **Arbitrary constants.** The inward pushes (a pull of sg/20 here, a
   factor 201/200 there, a +1/40 in a chord offset) are safety margins for
   the fit error. They are mathematically harmless but inelegant, and they
   *cost margin*: each push moves the bound away from the truth, and lost
   margin is exactly what forces extra cases in tight zones.
3. **Slack certificates.** Because the bound B(θ) sits strictly below the
   true F(θ), certificates must absorb the gap; near the corner (where the
   true margin already vanishes like s) there is little gap to give away,
   and v1's hardest repairs (the "needle") were fights over exactly this.

The cure for all three at once: **use the true extremal points
themselves.**

---

## 2. Implicit witnesses

**The observation.** The hole's boundary is made of finitely many arcs of
explicitly known algebraic curves: straight chords, unit circles around
division points, and limaçon arcs (quartic curves), plus hexagon edges.
Two kinds of points on this boundary are canonical:

* **vertices** — intersection points of two boundary curves, described by
  the system "P₁(x,y;s,t) = 0 and P₂(x,y;s,t) = 0" (two polynomial
  equations), plus a branch choice;
* **tangency points** — the point of a curve where the outward normal has
  a prescribed direction u, described by "P(x,y;s,t) = 0 and
  ⟨∇P(x,y), u⟩ ∥ u" — again two polynomial equations (the second is a
  cross product set to zero).

Neither kind of point has, in general, coordinates that are rational
functions of (s,t) — that is *why* v1 had to approximate. But both kinds
are **exactly described by polynomial conditions**. Call a witness given
this way an **implicit witness**: a symbol x accompanied by its defining
equations E(x; s,t) = 0 and branch-selecting inequalities.

**Why this is enough.** The lower-bounding step of the proof (the
selection lemma) never needed formulas — it needs only *facts* about the
witness that are expressible as polynomial constraints:

> F(θ) ≥ ⟨x₀, u(θ)⟩ + ⟨x₁, u(θ+120°)⟩ + ⟨x₂, u(θ+240°)⟩
> whenever x₀, x₁, x₂ lie in the (closed) hole.

If the xₖ are implicit witnesses on the hole's boundary, the inequality to
certify becomes:

> **for all** (s,t) in the cell **and all** points x₀,x₁,x₂ satisfying
> their defining equations and branch conditions:
> ⟨x₀,u₀⟩ + ⟨x₁,u₁⟩ + ⟨x₂,u₂⟩ − h ≥ 0.

This is a polynomial nonnegativity claim in more variables (s, t, and two
coordinates per witness), **with polynomial equations among them**. Such
claims are certifiable (§4). No formula for x is ever written down.

**Why this is tight.** Choose as witness the *tangency point* of the
feature that actually carries the support in the given direction. Then the
bound ⟨x,u⟩ is not an approximation of the support value — it **is** the
support value. The bound B(θ) equals F(θ) identically on the whole angular
range where that feature is the carrier. Coverage of the range no longer
depends on any fit's reach; it ends exactly where the geometry changes
carrier. Tight witnesses also cost nothing at the corner: B − h vanishes
exactly as fast as F − h, no faster.

**Three bonuses.**

* Some carriers need no implicitness at all: the support of a **unit
  circle** around an anchor point B is exactly ⟨B,u⟩ + 1 (rational!); the
  support of a **line** piece is attained at a vertex; hexagon corners are
  constants. Only limaçon tangencies and chord/limaçon vertices genuinely
  need equations.
* **Validity is largely free.** A vertex of the hole's boundary is on the
  boundary of its two defining sets and outside the others by the very
  structure of the arrangement; a tangency point of a hole-boundary arc is
  on that arc. What remains to check ("this arc really bounds the hole
  here", "the point is outside the four non-adjacent sets") consists of
  fat-margin claims — the delicate part of v1 validity (points hovering
  1/250 away from a set) disappears, because on-boundary points are
  admissible: the hole is closed and support values are attained on
  closures.
* **No arbitrary constants anywhere.** Every object in the proof is
  canonical: a curve, an intersection, a tangency. The only fitted objects
  remaining are the *case boundaries*, and even most of those become
  canonical (below).

---

## 3. The case map, version 2

A case is now a **carrier regime**: a region of (s,t) × θ where the three
support carriers (which curve/vertex attains each of the three support
values) are constant. Within one regime, ONE selection of three implicit
witnesses covers everything, tightly. Case boundaries are of two kinds,
both canonical:

* **carrier handoffs in θ** — the angle where the support argmax jumps
  from one feature to another (e.g. from a chord vertex to a limaçon
  tangency). At the handoff *both* carriers attain the same support, so
  certificates from both sides remain valid slightly across it: the cut
  needs no precision. (This is the self-adjusting behavior the fixed
  fitted cuts of v1 lacked; with tight witnesses it comes for free,
  because a tight bound stays tight up to the true handoff.)
* **feature births/deaths in (s,t)** — the loci where an arc appears on or
  vanishes from the hole's boundary. These are the *same* geometric loci
  as v1's cell cuts (the window-existence conditions 4R₀²−3, 4R_p²−3,
  2(s+1−t)−√3): v1's cell map survives, now with a principled reading.

Measured on the working geometry (the explorer's carrier labels), a
typical (s,t) sees **4 to 8 carrier regimes** across θ ∈ [0°,120°], and
the regime *sequence* is stable across large parts of parameter space. The
expected v2 table: five parameter cells (possibly fewer — IIIb1/IIIb2 may
merge once fitted-witness drift is gone), times 4–8 carrier regimes each,
with **no tie/split sub-cases** driven by fit reach. Rough target:
**~25–35 cases total, none of them repairs** — versus v1's ~56 leaves plus
sides.

The corner (s → 0) again needs no special case: the tight needle witness
is the limaçon tangency itself, which is exactly the point v1's "star"
formulas were chasing with rational approximations.

---

## 4. Certificates for implicit conditions

The final claims have the shape

> q(z) ≥ 0 for all z = (s, t, x₀, y₀, …) in the set
> { cell inequalities gᵢ(z) ≥ 0 } ∩ { defining equations Eⱼ(z) = 0 }.

Two certificate technologies handle equations natively; both have working
prototypes in this repository.

**(a) Positivstellensatz / SOS with equality multipliers** (primary).
Exhibit an identity

> q = σ₀ + Σᵢ σᵢ·gᵢ + Σⱼ λⱼ·Eⱼ

where each σ is a **sum of squares** of polynomials (visibly nonnegative)
and the λⱼ are *arbitrary* polynomials (the equations contribute with any
sign, since Eⱼ = 0 on the set). Checking the identity is polynomial
expansion plus checking each σ is an SOS (exact symmetric-matrix
factorization). Crucially, SOS certificates can prove **nonnegativity
with zeros** — q may touch 0 at the tangency optimum, which is exactly
what "tight" means; the strict version at the corner factors out s first,
as in v1's zoom chart. The `sos_mosek.py` module (numeric search →
rational reconstruction → exact re-verification) is the starting backend;
`lift_handelman.py` (linear-programming search with free equality columns)
is the low-degree alternative.

**(b) Elimination + the v1 engine** (fallback, per claim). Resultants
eliminate the witness coordinates from {q ≤ c} ∩ {E = 0}, producing a
single polynomial condition in (s,t) (and the cut parameter) that the
existing exact Bernstein engine certifies as in v1. Elimination raises
degree (the limaçon is quartic; tangency systems roughly square it), but
the v1 campaign established that the Bernstein engine is nearly
degree-insensitive; what it cannot do is certify claims that *touch* zero
— so route (b) applies to the fat-margin claims and route (a) to the tight
ones.

The **verifier contract** stays as in v1 (re-derive everything from the
definitions, re-check by an independent path), with one addition to the
trusted base: the branch-selection argument — that the defining system
plus inequalities pins the intended point (finitely many solutions,
correct branch). This is a per-witness lemma with a short resultant-based
proof, checked once.

---

## 5. What carries over from v1 unchanged

* the reduction to two parameters, the mirror symmetry, the region T½,
  and the fitting criterion (all of §§1–3 of the v1 outline);
* the five-cell partition loci (now read as feature-birth/death curves)
  and the machine-checked coverage logic;
* the exact Bernstein engine, the zoom (blow-up) chart at the corner, and
  the counterexample-driven design loop;
* the verifier architecture and the certificate inventory format;
* the diagnostic tooling (explorer, case visualizer, carrier labels) —
  the carrier labels in `hole_explorer.html` are precisely the v2 case
  data.

What is *discarded*: all fitted witness formulas (the ~40-entry catalog),
all inward-push constants, all fit-driven interval subdivisions, ties,
and region splits — replaced by ~a dozen implicit witness definitions
(curve pairs + branch data) and the carrier-regime table.

---

## 6. Work plan (v2 track, runs alongside v1 completion)

1. **Carrier atlas.** Sweep the working geometry to tabulate, per cell,
   the carrier sequence over θ and the (s,t)-loci where it changes
   (data exists in the explorer's labeling machinery; make it exact).
2. **Implicit witness definitions.** For each carrier: its curve equation
   P, the tangency/vertex system E, branch-selection inequalities, and
   the one-time branch lemma. (Limaçon tangency, limaçon×chord vertex,
   chord×circle vertex, plus the exact rational carriers.)
3. **Pilot regime.** Prove one full carrier regime end-to-end with the
   SOS-with-equalities backend (suggested pilot: the dip regime around
   θ ≈ 70° in cell IIIa, where v1 needed several fitted cases and the
   carrier structure is clean: chord tangency + two circle carriers with
   exact supports).
4. **Corner regime.** Prove the needle regime tightly (limaçon tangencies
   both sides, s factored out, SOS on the cofactor) — the decisive test
   that v2 kills v1's hardest zone.
5. **Scale out; write the v2 table; port the verifier** (add the SOS
   checker: expand identity + exact PSD check of the Gram matrices).

Risks to watch: SOS rational reconstruction robustness (mitigation:
Handelman-with-equalities for low degrees; per-claim fallback (b));
degree growth in eliminated forms (mitigation: keep claims per-slot —
one carrier per certificate — so systems stay in ≤ 4 variables plus
(s,t)); branch bookkeeping (mitigation: the per-witness branch lemma is
one resultant computation each, done once and checked by the verifier).

---

*Status: design document. The v1 proof (explicit witnesses + exact
Bernstein interval certificates) is being completed independently and
remains the reference; v2 aims to be the proof one would publish.*
