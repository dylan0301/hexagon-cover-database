# Body--Appendix Validity Repair Audit

Date: 2026-07-28  
Branch: `agent/body-appendix-separation`  
Base: `main` at `9f6ebc1f675419ed056e564816658e6c14ca5bb1`

## 1. Scope

This audit covers:

- every file changed on `agent/body-appendix-separation`;
- every TeX source included by `arrange/paper_draft/main.tex`;
- every active numbered proof dependency used by the final routing;
- the complete `407X` endpoint package;
- the `414X` exactly-one-Vd1/Vd2 package;
- the `3105X` exact mixed-overlap certificate and both verifier programs.

It does not certify historical files marked `Failed`, `Empirical`, `Strategy`,
or otherwise inactive in the final proof tree.

No PDF or LaTeX compilation was performed. The tracked `main.pdf` is stale and
was not modified.

## 2. Final proof model

The complete proof now consists of:

1. the reader-facing TeX body;
2. the TeX verification appendices;
3. two formally incorporated electronic supplements:
   - the exact status-bearing `407X` four-label endpoint proof, pinned by Git
     blob;
   - the exact `3105X` sparse-polynomial certificate, pinned by Git blob and
     the canonical transcript SHA-256 digest.

The body contains the definitions, geometric mechanisms, complete branch
hypotheses, exact terminal statements, and exhaustive routing. Long support,
polynomial, monotonicity, placement, and certificate calculations are outside
the body.

## 3. Defects repaired

### 3.1 Strict-supercritical transfer

The outgoing inequality

```text
B < g_c^{sc}
```

is unconditional. The following-row inequality

```text
A_next > 1-g_c^{sc}
```

now explicitly requires a center-free outgoing edge. The paper and the generic
transfer appendix no longer state the stronger false version.

### 3.2 Boundary-path budget

The corrected theorem requires:

- no center or nonincident positive-length trace on any internal path edge;
- complete external endpoint components bounded by the two endpoint
  quantities.

The active applications `4013` and `2110` now verify these hypotheses in the
text.

### 3.3 CE2 threshold routing

The proof establishes that at least one of the two threshold slots fires. It
does not assert uniqueness; both thresholds may be available.

### 3.4 Exact one-gap terminal coordinates

The exact five-row chain has terminal target

```text
Z > 1-H.
```

After capped-map duality, the reversed three-map chain has target

```text
output > 1-X.
```

The two statements are no longer conflated in the body or chain tables.

### 3.5 Strategy 1 master deficit

The body now includes the previously omitted hypothesis that every unlisted
row has boundary contribution at most one.

### 3.6 Admissible-set derivation

The new appendix gives:

- an explicit equilateral enclosure of the triangular hull;
- all four caliper support values;
- the three polynomial contact cells;
- the selected connected-component conditions;
- the radial envelope and down-closedness.

### 3.7 T3-like four-label endpoint audit

The paper no longer replaces the hard endpoint audit by a generic envelope.
The complete branch files `4073`, `4074`, `4075`, `4078`, `4079`, `407a`,
`407c`, and `407d` are formally incorporated at exact blob identifiers. The
four labels are exactly

```text
Full, L, T_-, T_+^{hi}.
```

### 3.8 Vd1--supercritical replacement

The complete proof now includes:

- the two ordered halves of the half-square admissibility lemma;
- all four strict Vd1 margins;
- the center radial-handoff inequality;
- explicit unit axis triangles;
- interiors of translated unit-axis triangles producing open
  nonsupercritical Vd0 roles;
- preservation of the shared boundary and both radial demands.

A final audit found one overstrong comparison in the old `4147` source. It has
been corrected from

```text
max(c_i,mu) < max(1-b_i,1-a)
```

to the sufficient and proved statement

```text
max(c_i,mu) <= max(1-b_i,1-a),
```

combined with the preceding strict inequality for the required center-side
demand.

### 3.9 CE2 exactly-one-Vd placement assembly

The authoritative assembly now separates:

- adjacent and nonadjacent placements with the supercritical row at `T_0`;
- the unique Vd row at `T_0`;
- the adjacent rescue pair away from `T_0`;
- the Vd2 neighboring-midpoint Strategy 1 subcase;
- the additional-short-role skeleton subcase.

The adjacent terminal is the direct quarter radial separation, not an
unsupported universal hatted-map formula. The nonadjacent terminal retains its
Vd-specific own-radial margin.

### 3.10 Strategy 4 exact certificate

The paper now includes:

- the rational upper envelopes for the exact radial value;
- the exact Gram residuals;
- the identity
  `P_X = h^2 N_X Q_X` in the `(x,h y)` coordinate normalization;
- the implication from `Q_X>=0` to common tangent support at least `h`;
- the eight integer-polynomial reduction;
- the three global analytic charts;
- the exact tensor Bernstein conversion;
- all code and data blob identifiers and the canonical transcript digest.

## 4. Proof-folder review

### Structural layer

Reviewed and accepted:

- compactness/scaling;
- distinct roles;
- center and vertex classifications;
- singleton-gap convention;
- strict handoff selection;
- unique center midpoint;
- short-role identity and exhaustive routing.

The displayed notation defect in `1214` was repaired, and its exact-one and
at-least-two constructions were rechecked.

### Strategy 1

Reviewed and accepted:

- center, supercritical, positive-support, and no-support skeleton caps;
- signed center perimeter caps;
- Vd1/Vd2 and T3-like boundary caps;
- master perimeter deficit;
- three-short-role skeleton contradiction.

### Strategy 2

Reviewed and accepted after the repairs above:

- exact admissible set and capped map;
- zero-radial raw/capped distinction;
- residual transfer and corrected path theorem;
- one-side endpoint loss;
- paired CE2 endpoint loss;
- common five-row one-gap interface;
- separate CE1 and CE2 scalar completions;
- complete `407X` endpoint audit;
- exactly-one-T3-like rescuer proof;
- adjacent and nonadjacent Vd radial separations;
- corrected explicit Vd1 replacement and exhaustive `414X` assembly.

### Strategy 3

Reviewed and accepted:

- the two orientation normal forms;
- minimum-square and supercritical maximum-square local losses;
- direct T3-like loss;
- reflection normalization;
- both cyclic area certificates.

### Strategy 4

Reviewed and accepted as an exact computer-assisted proof:

- direct six-point radial forcing;
- direct three-point asymmetric forcing;
- Newton inner witnesses;
- cap-chain reduction;
- ray order and two adjacent overlaps;
- exact mixed-overlap reduction;
- exact sparse-polynomial derivation algorithm;
- exact global Bernstein positivity algorithm.

The verifier code was inspected line by line. No arithmetic-model,
coordinate-normalization, denominator, domain-chart, or Bernstein-conversion
defect was found.

## 5. Independent calculation checks

The audit also used independent numerical or symbolic checks as error detectors.
They are not substitutes for the exact proofs.

| Claim | Check | Result |
|---|---:|---|
| explicit radial envelope | 100,000 random feasible pairs | maximum discrepancy about `1.47e-14` |
| four-label capped map | 100,000 random inputs | maximum discrepancy about `3.89e-15` |
| CE1 five-row chain | 19,711 accepted samples | no failure |
| CE2 five-row chain | 30,211 accepted samples | no failure |
| one-side endpoint loss | 37,437 accepted samples | no failure |
| paired CE2 endpoint loss | 302,563 accepted samples | no failure |
| center skeleton cap | 1,000,000 samples | maximum below `1.5` |
| supercritical skeleton cap | 500,000 samples | maximum below `1.5` |
| Strategy 4 four overlaps | 162,655 accepted samples | no failure |
| mixed Gram factorization | exact symbolic reduction | identity verified |

## 6. Paper-to-proof correspondence

Every row of the paper routing table now points to an active proved terminal:

| routing row | terminal proof |
|---|---|
| CE0, `N_+=0` | Strategy 1 cyclic perimeter deficit |
| CE0, `N_+=1`, all Vd0 | center-independent nine-point obstruction |
| CE0, `N_+=1`, a Vd1/Vd2 row | Strategy 1 perimeter deficit |
| CE0, `N_+=1`, T3-like without Vd1/Vd2 | Strategy 3 area certificate |
| CE0, `N_+>=2` | Strategy 3 area certificate |
| CE1/CE2, at least three short roles | Strategy 1 skeleton deficit |
| CE1/CE2, `N_+=0`, all Vd0 | Strategy 2 gap-rank kernel |
| CE1/CE2, `N_+=0`, a Vd1/Vd2 row | Strategy 1 perimeter deficit |
| CE1/CE2, `N_+=0`, T3-like | exact `407X` endpoint audit |
| CE1/CE2, `N_+=1`, all Vd0, zero gaps | Strategy 4 |
| CE1/CE2, `N_+=1`, all Vd0, positive gap | five-row or paired endpoint certificate |
| CE1/CE2, exactly one T3-like | common adjacent-rescuer obstruction |
| CE1, exactly one Vd1/Vd2 | Strategy 1 perimeter deficit |
| CE2, exactly one Vd1/Vd2 | complete `414X` placement assembly |

No terminal row is inferred from selected criticality; `N_+` is always computed
from actual maximal reaches.

## 7. Final assessment

No remaining mathematical gap is known in the active proof tree or in the
paper's correspondence to that tree after these repairs.

Two checks were deliberately not performed:

1. **No PDF/LaTeX compilation.** This was explicitly prohibited for the task.
   Consequently the body pagination, references, and layout remain to be
   checked in a later build.
2. **No fresh verifier execution.** The exact Strategy 4 code and authenticated
   data were reviewed and formally incorporated, but the scripts were not
   rerun in this source-only environment.

The branch should not update `main.pdf` until both checks are authorized and
completed.
