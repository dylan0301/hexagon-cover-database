# Bulk redesign: geometric cuts + SOS certificates

Status: design document (2026-07-07). Replaces the s/t box tiling of
`gen_bulk.py` / `gen_bulk_strip.py` (now retired) by a small number of
cells cut along catalog curves, each carrying one witness-triple
certificate compiled by `sos_mosek.sos_certify` (exact over Q(sqrt3),
MOSEK-powered).

## 1. The parameter region

Reduced parameters (s,t) = (a5, a0) on
T = { 0 < s <= t,  R0^2 = t^2 + t(1-s) + (1-s)^2 <= 1 },
with the mirror reduction s + t <= 1 (touches T only at the tip
(1/2, 1/2)). T is a narrow curved triangle from the equality corner
(0,0) to the tip; the upper boundary is the conic R0^2 = 1.

Ground-truth fitting margins min_phi F_S - h grow fast away from the
corner: ~0.026 at s = 0.05, ~0.16 at s = 0.2, ~0.43 at the tip. The
corner is the only thin zone.

## 2. Structural facts (numerically established, to be cited by the
   generator)

* The sliver K0 = K(t, 1-s) is **band IV on all of T** — its treatment
  (chord + dip corner + end lobes) is uniform; no case split ever needed
  for K0.
* The parametric petal K~ = K(s, 1-t) traverses exactly 9 catalog cases
  over T. Interfaces, in (s,t):
  - line  t - s = 1 - sqrt3/2          (band I/II, sigma~ = sqrt3/2)
  - conic s^2 + s(1-t) + (1-t)^2 = 3/4 (band II/III, R~^2 = 3/4)
  - cubic (4 - t) * R~^2 = 3           (G3s; splits III.4' / III.2')
  - quintic Gpoly(1-t, s) = 0          (G4s; the +lA flush line)
  - line  t = 1/2                      (sB; opens the tip cluster)
  - cubic w-(s, 1-t) = 0               (band-I subcases)
  The "e" regime sigma~ < 1/2 never occurs on T.
* Witness-validity zero-contours of the corner-zone witnesses track the
  G3s cubic and the R~^2 = 3/4 conic (see overlay_val.png) — validity
  certificates flip exactly at catalog interfaces, so cells must not
  straddle them.

## 3. Support structure = witness triples

At the minimizing phi*, the three rotated support values of F_S are
realized by (all are catalog-curve intersections):

| cell (case of K~)   | phi*        | supports                          |
|---------------------|-------------|-----------------------------------|
| III.4' (diagonal)   | ~94 deg     | star pair St1, St3 (E_AO arcs of  |
|                     |             | petals 1,3) + V5-gap corner       |
| III.2' / II.1'+lA   | ~10-28 deg  | V0-gap corner (r~0.75) + star pair|
| II.1'               | ~35 deg     | V0-gap + antipodal mid point +    |
|                     |             | V5-side gap                       |
| tip (t > 1/2)       | ~53 deg     | V0-gap + two symmetric r=0.36 pts |

Witness pool for the redesign:
* **St_i**: star points on the E_AO limacon arcs of petals i (near the
  center). Exact: limacon point at rational tan-half parameter, or the
  intersection E_AO(i) ∩ E_AO(i+1).
* **G_k**: gap corner at hexagon vertex V_k — deepest hole point between
  petals k and k+1; intersection of the two adjacent petal boundary
  arcs (which arcs depends on the cell's catalog case — hence the cuts).
* **Wdip**: sliver chord dip (uniform, K0 is always band IV).

Their coordinates are algebraic over Q(sqrt3)(s,t): adjoin them as new
variables x, y with their defining polynomial equations (the eq-real-2
pattern in sos_mosek tests: q >= 0 on {gens >= 0} ∩ {E1 = E2 = 0}).

## 4. Certificate compilation per cell

For each cell (intersection of catalog half-spaces above):
1. **Fitting**: 3 arcs of phi covering [0, 120), split at two
   unnormalized directions (cheap tilt cuts); per arc the selection
   sinusoid of the cell's witness triple; the arc lemma reduces to the
   two endpoint inequalities — polynomials in (s, t, witness coords).
2. **Validity**: each witness vs each petal: selection or disk
   certificates, again with adjoined coordinates.
3. All discharged by `sos_certify(q, [s,t,x,y,...], gens=cell_gens,
   eqs=witness_eqs, deg<=3)`; `verify_sos` re-checks each certificate
   independently; the verifier gains a check_sos_gram routine (exact
   LDL^T over Q(sqrt3) + identity match).

Cell generators: the catalog interface polynomials with the correct
signs, plus R0slack = 1 - R0^2, dg = 2s - t, g = t - s, s.

Smoke test (passed): the degree-6 disk certificate Wdip-vs-K3 was
discharged by a single `sos_certify` call over the whole band-II cell
{R~^2 <= 3/4, t-s <= 1-sqrt3/2, t <= 1/2} ∩ T, exact and independently
verified (255 s) — one certificate where the box tiling needed dozens.

## 5. Corner zone (open work item)

The corner cell (s small) keeps the existing witness recipe; its
certificates must vanish at (0,0) (equality) and at t = s (star points
ride petal boundaries). Current status: the generic Handelman and the
exact-SOS reconstruction both fail exactly on the corner-most
subintervals; MOSEK finds numeric certificates (stage 1 feasible), so
the representation exists — the exact rounding of the degenerate face
is the missing piece. Candidate attacks, in order:
1. dedicated tangency certificates for boundary-riding pairs
   (Wst1-vs-K1 etc.): the selection sinusoid minus h is a perfect
   square-like expression along the arc — certify the *identity*
   rather than an inequality;
2. blow-up coordinates at the corner (t = kappa * s, kappa in [1, 2]:
   divide certificates by the known vanishing order in s);
3. sel-tree thresholds made absolute (not 0.12 * bestmin) near the
   corner.

## 6. Artifacts

* extent maps + overlays: scratchpad `extent_recipe.npz`,
  `extent_gt.npz`, `overlay_fit.png`, `overlay_val.png`,
  `extent_*.png` (corner-recipe fitting margin dies at s ~ 0.06;
  validity holds to s ~ 0.1-0.3 and flips on catalog curves).
* `sos_mosek.py` — exact SOS certifier + `verify_sos` + `suggest_squares`.
