# The hole never fits: an outline of the proof, in plain terms

This document explains the structure of the proof that the *hole* left
uncovered by the six corner sets of the hexagon can never be covered by one
more unit triangle. It is written to be readable on its own: every term is
defined before it is used. The full technical details (exact formulas,
certificates, verification code) live elsewhere in this repository; this
outline is the map. An interactive picture of everything described here is
in `hole_cases.html` (and the plain hole explorer in `hole_explorer.html`).

---

## 1. The objects

**The hexagon.** Let H be the regular hexagon with vertices
V₀, V₁, …, V₅ at distance 1 from the center O, with V₀ = (1,0) and the
vertices numbered counterclockwise. Every edge of H has length 1. The
distance from the center to each edge is

> h = √3⁄2 ≈ 0.866,

a constant that appears throughout.

**Unit triangle.** "Unit triangle" always means an equilateral triangle of
side length 1 (any position, any rotation). Its height is exactly h.

**Division points.** On each edge Vᵢ → Vᵢ₊₁ of the hexagon we mark one
point pᵢ, at distance aᵢ from Vᵢ (so 0 < aᵢ < 1). These six numbers
a₀, …, a₅ are the parameters of the whole problem.

**The corner sets.** At each vertex Vᵢ sits a set Kᵢ — the "ab-set"
K(a,b) studied in this repository: the union of all unit triangles that
contain three specific anchor points near that vertex, intersected with
the 120° wedge at the vertex. For this outline the only things one needs
to know about K(a,b) are:

* it is determined by two numbers a, b ∈ (0,1) (how far its two anchor
  points sit along the two edges at that vertex);
* it **shrinks** when a grows and when b grows (monotonicity);
* its boundary consists of finitely many explicitly known arcs — straight
  chords, circular arcs of radius 1, and arcs of a quartic curve (a
  "limaçon", the curve traced by a point rigidly attached to a rotating
  unit triangle). Each arc has an exact equation.

**The hole.** S is what remains of the hexagon after removing all six
corner sets:

> S = H \ (K₀ ∪ K₁ ∪ … ∪ K₅).

**The claim.** *For every admissible choice of the six division parameters,
the hole S does not fit inside any unit triangle.* ("Admissible" includes a
mild non-degeneracy condition made precise below.)

---

## 2. The measuring tool: one number per direction

**Support value.** For a direction u (a unit vector) and a bounded set S,
the *support value* h_S(u) is the largest value of the dot product ⟨x, u⟩
over points x of S. Geometrically: slide a line perpendicular to u toward S
from far away; h_S(u) records where it first touches.

**The fitting functional.** Fix an angle θ and take the three directions
u(θ), u(θ+120°), u(θ+240°), where u(α) = (cos α, sin α). Define

> F_S(θ) = h_S(u(θ)) + h_S(u(θ+120°)) + h_S(u(θ+240°)).

This one number answers the fitting question. A classical fact (a form of
Viviani's theorem — inside an equilateral triangle, the three distances to
the sides sum to the height):

> **Fitting criterion.** S fits inside some unit triangle whose sides face
> the directions u(θ+120°k) if and only if F_S(θ) ≤ h.

Since every unit triangle faces three such directions for some θ, the claim
becomes a clean inequality:

> **Theorem (restated).** F_S(θ) > h for every θ and every admissible
> parameter choice.

F is periodic in θ with period 120°, so only θ ∈ [0°, 120°] matters.

---

## 3. Step one: six parameters become two

The corner set Kᵢ shrinks when its parameters grow. Consequently, if we
**enlarge** every corner set, the hole **shrinks**, and a shrunken hole is
only *easier* to cover. So if even the shrunken hole satisfies F > h, the
original does too.

Let

> s = the smallest of a₀,…,a₅,  t = the largest.

Enlarging each corner set to the most generous shape compatible with (s,t)
replaces the six-parameter hole by a two-parameter one, written S̃(s,t):
the hexagon minus

* one **sliver** K(t, 1−s) placed at V₀ (built from the *largest*
  parameter — it is the smallest of the six sets, hence the name), and
* five identical **petals** K(s, 1−t) at V₁,…,V₅ (built from the smallest
  parameter — the largest possible sets).

Since S̃(s,t) ⊆ S always, it suffices to prove F_{S̃(s,t)} > h. From now on
S means S̃(s,t) and the problem lives in the plane of pairs (s,t).

**The parameter region T.** The admissible pairs form

> T = { (s,t) : 0 < s ≤ t, and R₀² ≤ 1 },  where R₀² = t² + t(1−s) + (1−s)².

R₀ is the distance between the sliver's two anchor points; R₀ ≤ 1 is the
non-degeneracy condition. The region T is a curved sliver of the
(s,t)-plane pinched at the origin: near s = 0 it forces t < ≈ 2s.

**Mirror symmetry.** Replacing every aᵢ by 1−a₅₋ᵢ reflects the whole
configuration across a symmetry axis of the hexagon. Therefore it is
enough to prove the theorem on the half

> T½ = T ∩ { s + t ≤ 1 }.

**Where equality threatens.** As s → 0 (all division points sliding into
the corners), the hole converges to the triangle O V₀ V₅ — one sixth of
the hexagon — and F(90°) → h exactly. The inequality degenerates at the
corner (s,t) → (0,0) of parameter space, with margin shrinking like a
constant times s. Any proof must be *exact* there; no numerical slack
survives the corner. This is the hard part of the whole enterprise.

---

## 4. Step two: bounding F from below with finitely many points

F is a sum of three support values, and each support value is a maximum
over the hole. So for **any** three points w₀, w₁, w₂ in the hole (one
*witness* per direction),

> F(θ) ≥ ⟨w₀, u(θ)⟩ + ⟨w₁, u(θ+120°)⟩ + ⟨w₂, u(θ+240°)⟩.

We call a chosen triple (w₀, w₁, w₂) a **team**. The right-hand side
simplifies: rotating each term back,

> F(θ) ≥ B(θ) = ⟨w, u(θ)⟩ where w = w₀ + R₋₁₂₀ w₁ + R₋₂₄₀ w₂

(R_α = rotation by α). One team thus produces a single plane vector w —
depending on (s,t) — and the lower bound B(θ) is "the component of w in
direction u(θ)", a pure cosine curve in θ. It beats h on an arc of
directions around w. Different teams cover different arcs.

**The plan in one sentence:** choose finitely many witness points in the
hole, given by explicit formulas in (s,t); divide the angle range [0°,120°]
into intervals; on each interval use one team; verify that the team's
bound clears h on that interval for every (s,t) — and make every
verification an exact polynomial inequality.

Two devices turn "for every θ in the interval" and "the witness is in the
hole" into finitely many polynomial facts.

**The arc lemma (handles all θ in an interval at once).** Describe an
interval endpoint not by its angle but by the *direction vector*
d = (1−q², 2q), where q = tan(θ/2) — the "tan-half" encoding. If q is a
rational number (or a rational function of s and t), then d has polynomial
entries and, pleasantly, its length is exactly 1+q². If, at both endpoint
directions d₁, d₂ of an interval (less than 180° wide),

> ⟨w, dⱼ⟩ − h·(1+qⱼ²) > 0,

then B(θ) > h for **every** θ in the interval (a cosine curve exceeding h
at two points within a half-turn exceeds it between them, by concavity).
So each interval costs exactly two polynomial inequalities. Interval
endpoints may depend on (s,t): near the corner the dangerous angles move,
and there the cuts are formulas like q = 1 − 3t/4 that track them.

**Witness validity (the point really is in the hole).** A point w is in
the hole when it is (i) inside the hexagon — six linear inequalities — and
(ii) outside each of the six corner sets. "Outside K" is certified by one
of three mechanisms, each again reducing to polynomial inequalities:

* **distance**: w is farther than 1 from one of K's anchor points — every
  unit triangle has diameter 1, so no unit triangle covers both, hence
  w ∉ K (one quadratic inequality);
* **cone**: w is outside the 120° wedge of that vertex (linear);
* **the same machinery one level down**: the fitting criterion applied to
  the four points {anchors of K} ∪ {w} shows no unit triangle covers all
  four — proved by the same team-plus-arc-lemma method.

So the entire proof compiles down to statements of one single kind:

> *a specific polynomial in s and t (with coefficients in ℚ adjoined √3)
> is strictly positive on a region cut out by finitely many polynomial
> inequalities.*

---

## 5. Step three: proving polynomial positivity exactly

Numerical checks (grids, floating point) convince but do not prove. Each
positivity claim is proved by **exact interval arithmetic in Bernstein
form**, which works as follows.

**Bernstein coefficients.** A polynomial restricted to a rectangle can be
rewritten as a weighted average of finitely many *Bernstein coefficients*
(exact rational numbers, computable from the polynomial's coefficients by
finitely many additions and multiplications). Two facts make them useful:

* the polynomial's values on the rectangle always lie between the smallest
  and largest Bernstein coefficient;
* the coefficients for the two halves of a rectangle are exact averages of
  the original ones (so splitting a rectangle is cheap and exact).

**The procedure.** To prove "p > 0 on the part of a rectangle where the
region inequalities g₁ ≥ 0, …, g_k ≥ 0 hold": compute Bernstein
coefficients of p and of every gⱼ on the rectangle.

* If all coefficients of p are positive — p > 0 on the whole rectangle;
  done there.
* If some gⱼ has all coefficients negative — the rectangle misses the
  region entirely; discard it.
* Otherwise split the rectangle in half and repeat on both halves.

Every number in this computation is an exact rational (times √3 where
needed); there is no floating point and no rounding anywhere. The
procedure either terminates with a finite list of rectangles proving the
claim, or produces an exact point where the claim fails — a
*counterexample*, pinpointing a design error. (This second behavior was
used heavily: every flaw found during the campaign came with the exact
coordinates of a failing configuration.)

**The corner needs one extra idea.** Near (s,t) = (0,0) the margins vanish
(like a multiple of s), so no rectangle around the corner can ever have
all-positive coefficients. The cure is a **zoom substitution** t = s(1+v):
in the new coordinates (s, v) the corner becomes an ordinary edge, the
polynomial factors as s^k · P(s,v) with P strictly positive, and the
procedure applies to P. (Algebraic geometers call this a blow-up.) All
corner-cell claims go through this chart.

**Independent verification.** A separate checker re-derives every
polynomial from the witness formulas and the case table — not from the
generator's output — and re-proves every claim with the rectangle-splitting
order reversed, so no verdict depends on one code path or one particular
rectangle decomposition. It also checks the bookkeeping: that the cells
cover the parameter region (a short logical argument over the defining
inequalities), that each cell's angle intervals chain from 0° to 120°
without gaps, and that every witness used by a team has all its validity
certificates.

---

## 6. The witnesses

The catalog holds about thirty witness formulas, each an explicit
expression in (s,t) with coefficients in ℚ(√3), each anchored to a
geometric feature of the hole (a pocket, a chord, an arc it hugs).
Representative examples, writing g = t − s:

* **the center** (0,0) — in the hole for all parameters;
* **star points**: points on the petals' inner limaçon arcs (the arcs
  sweeping closest to the center), pulled slightly inside; the pull is a
  rational function of size ≈ sg/20, vanishing exactly as fast as the
  hole thins at the corner;
* **the dip point**: the middle of the sliver's chord, pushed outward into
  the shallow pocket beyond it by (4/15)(1−R₀²) + s²/16;
* **chord points**: points just inside the straight boundary pieces of the
  sets, at fitted positions along the chord;
* **corner points at distance 1**: points placed exactly at distance
  201/200 from an anchor point of a neighboring set — making "outside that
  set" a one-line distance certificate;
* **constant points**: in the parameter zone where all margins are fat,
  six fixed points suffice.

Each witness used by a cell carries validity certificates on that cell
(hexagon + six sets, by the mechanisms of §4).

---

## 7. The case map

**Five cells.** The parameter half-region T½ splits into five cells along
exact geometric loci (each the locus of a geometric event, not an
arbitrary threshold). With R_p² = s² + s(1−t) + (1−t)² (the petal analogue
of R₀²):

| cell | where | character |
|------|-------|-----------|
| I | 4R₀²−3 ≥ ½ and 4R_p²−3 ≥ 1/20 and s ≤ 2/5 | the corner cell: contains (s,t) → 0, margins vanish, needs the zoom chart |
| IIIa | 4R₀²−3 ≤ ½ and s ≤ 2/5 | the sliver's orientation window is narrow |
| IIIb1 / IIIb2 | 4R_p²−3 ≤ 1/20 and 4R₀²−3 ≥ ½ and s ≤ 2/5, split by 2(s+1−t) ⋛ √3 | the petals' orientation windows die (two sub-regimes) |
| IV | s ≥ 2/5 | near-halfway divisions; hole margins are fat (≈ 0.34+) |

Coverage is a four-line logical argument: if s ≥ 2/5 the point is in IV;
otherwise if 4R₀²−3 ≤ ½ it is in IIIa; otherwise if 4R_p²−3 ≤ 1/20 it is
in IIIb1 or IIIb2 according to the sign of 2(s+1−t) − √3; otherwise it is
in I. (Cells are closed and may overlap along their boundary curves; every
certificate holds on its cell's full closed region.)

Two lessons from the certification campaign are baked into these
definitions. The petal cut sits at 1/20 rather than 0 because in the thin
band 0 ≤ 4R_p²−3 ≤ 1/20 the petal-based witnesses degenerate — that band
provably belongs with IIIb. And the IIIb cells carry the constraint
4R₀²−3 ≥ ½ explicitly, because early region definitions overlapped IIIa's
territory, where IIIb's witnesses are not valid — an unsoundness caught by
the validity certificates and eliminated by matching the regions to the
coverage logic exactly.

**Leaves.** Within each cell, the angle range [0°, 120°] is divided into
intervals — *leaves* — with one team per leaf, or, where no single team
spans a leaf for all (s,t) in the cell, a split of the cell by an explicit
polynomial *side condition* with one team per side. Current table sizes:
cell I has 5 leaves (with parameter-dependent interval endpoints around
the dangerous θ ≈ 90° "needle"), IIIa has 4, IIIb1 has 21, IIIb2 has 11,
IV has 15 (across four fat-margin sub-bands). In IIIb1's middle sits an
intrinsically delicate band (margins ~10⁻³ over a wide angle range) that
genuinely requires its fine subdivision — the complexity of the table
reflects the geometry, not sloppy bookkeeping.

Every leaf contributes two endpoint inequalities per team (§4), each
proved by the Bernstein procedure (§5) on the cell (through the zoom chart
for cell I). The side conditions and interval endpoints are part of the
checked data: the verifier confirms the intervals chain 0° → 120° in every
cell and on every side of every split.

---

## 8. Current status

**Proved (exact certificates, machine-checked):**

* all leaf certificates of cells IIIa, IIIb1, IIIb2 and IV — 78 units,
  each 4–5 exact positivity proofs;
* cell I: the shoulder (θ from 0° to ≈ 51.5°, four units) and the left and
  middle needle structure — certified through the zoom chart;
* the cell-coverage logic and all arc-chain bookkeeping;
* the majority of the witness-validity certificates (hexagon + per-set),
  including every witness of the fat-margin cells.

**In progress (final items):**

* cell I's last piece: the deep corner tip (s < 0.04) of the rim near
  θ ≈ 100–120°, where the boosted star witnesses provably fall short by
  ≈ 10⁻³ and either a corner-specific case or a small witness adjustment
  is being certified;
* eight witness-validity certificates for the tightest witnesses (all
  eight *verified geometrically valid*; the remaining work is certificate
  generation, now being rerun with the linear endpoint form of §4);
* the independent verifier's full end-to-end pass (running for the
  completed cells), and the final write-up.

**Soundness incidents found and fixed by the machinery itself** (the
reason the layered design exists): a region-overlap error that let one
cell's certificates quantify over another cell's territory (caught by a
validity certificate failing where the witness genuinely left the hole);
one witness formula invalid in a sliver near a degenerate corner (the
witness was retired — the one leaf using it was re-certified with a
different team); and several between-grid-point design flaws surfaced as
exact counterexamples during certification and repaired by local case
splits. In every instance the exact layer caught what numerics had missed.

**Where things live.** Witness catalog: `wit_v5.py` / `witnesses_v5.js`
(exact twin modules), `wit_iv.py` (cell IV). Case tables: `leaves.py`,
`leaves_iv.py`. Engine: `bernstein.py`. Generators: `gen_bern.py`,
`gen_validity.py`. Verifier: `verify_bern.py`. Certificates:
`certs_bern/`. Design journal: `notes/geom_cells_design.md`. Architecture
specification: `PROOF_CERTS.md`. Visualizations: `hole_cases.html` (case
map + witness teams), `hole_explorer.html` (the hole itself).
