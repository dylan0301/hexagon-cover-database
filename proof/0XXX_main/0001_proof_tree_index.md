# Proof Tree Index

Status: Reference

This is a numbered proof-structure tree. It is navigation only: a branch is not
proved merely because it appears here, and proof status is inherited from the
numbered source notes.

## Spine

Under a hypothetical seven-triangle cover, choose role triangles

$$
T_C,T_0,\dots,T_5.
$$

Classify $T_C$ as CE0, CE1, or CE2. The CE1 and CE2 cases are recorded
together in the combined 4XXX branch. Inside each active branch, define
perimeter rows $(a_i,b_i)$ and compute

$$
N_+=
\left\lvert
\left\lbrace
i:a_i+b_i>1
\right\rbrace
\right\rvert.
$$

Then split first by CE0 or by the combined CE1/CE2 branch; inside each branch
split by $N_+=0$, $N_+=1$, or $N_+\ge2$; inside each $N_+$ branch split by
Vd0, Vd1/Vd2, and T3-like vertex-role patterns.

## Setup

- `1XXX`: foundations
  - `1003`: open-unit and shrunken-closed equivalence
  - `1101`: CE0, CE1, CE2 classification
  - `1201`: Vd0, Vd1, Vd2, and T3-like types
  - `1202`: local coordinates $(a,b,c)$
- `2XXX`: geometric lemmas
  - `20XX`: V-triangle geometry
    - `2004`: exact piecewise support-contact admissible set
    - `2005`: proved midpoint self-cover criterion
    - `2006`: T3-like midpoint lemma
    - `2007`: exact piecewise $B_c(a)$ map and classified-map semantics
    - `2008`: neighbor-ray maximum formula
    - `2009X`: ab-set package, including the ab-union curve for $a+b>1$
    - `2010`: proved free strict-supercritical outgoing supremum
  - `21XX`: C-triangle geometry
    - `2100`: proved CE1/CE2 exactly-one-midpoint lemma with $O$ interior
    - `2101`: maximal C-triangles over the half skeleton
    - `2102`: CE1 interval certificate
    - `2103`: CE2 interval-pair certificate
    - `2104`: CE2 two-gap replacement theorem
    - `2105`: CE1 exact center and radial formulas
    - `2106`: CE2 exact center and radial formulas
  - `25XX`: length bounds
    - `2500`: boundary length bounds
    - `2510`: skeleton length bounds
    - `2520`: diagonal length bounds
  - `26XX`: enclosing-triangle tools
    - `2607`: minimal enclosing equilateral quadrilateral lemma

## CE0 Branch

- `3XXX`: CE0
  - `30XX`: CE0, $N_+=0$
    - `3010`: boundary-length obstruction
  - `31XX`: CE0, $N_+=1$
    - all Vd0
      - `310X`: all-Vd0 package
        - `3100X`: existing algorithm-2 five-point route
        - `3101X`: six-point construction and core graph definitions
    - at least one Vd1/Vd2
      - `314X`: boundary-length obstruction
    - at least one T3-like and no Vd1/Vd2
      - `317X`: unconditional direct area-loss route
      - `3172`: failed coordinatewise tangent-envelope conjecture
      - `3175`: direct T3-like area-loss theorem
  - `32XX`: CE0, $N_+\ge2$
    - `3205`: unconditional local square-loss theorem
    - `3208`: six-row strict area certificate
    - `3201`: proven branch assembly
  - `33XX`: old CE0 Vd1/Vd2 chain proof

## CE1/CE2 Branch

- `4XXX`: CE1/CE2
  - `40XX`: CE1/CE2, $N_+=0$
    - all Vd0
      - `401X`: exact CE1 matrix and all CE2 no-gap, one-gap, and two-gap states proved
    - at least one Vd1/Vd2
      - `404X`: CE1 and CE2 boundary-length obstructions
    - at least one T3-like and no Vd1/Vd2
      - `407X`: proven exact four-label $T_0$-T3-like reassembly
  - `41XX`: CE1/CE2, $N_+=1$
    - all Vd0
      - `410X`: exact gap-propagation and CE2 replacement strategy
      - `9630`: 5 point conjecture counterexample
    - Vd1/Vd2 branches
      - `411X`: CE1 at-least-one and CE2 at-least-two boundary-length obstructions
      - `414X`: additional positive-support branch closed by `414a`; the complementary branch closes through the now-proved `4013` package
    - at least two T3-like and no Vd1/Vd2
      - `412X`: shared CE1/CE2 diagonal obstruction
    - exactly one T3-like and no Vd1/Vd2
      - `413X`: shared CE1/CE2 boundary obstruction (`4131`, `4132`)
  - `42XX`: CE1/CE2, $N_+\ge2$
    - `4200`: shared CE1/CE2 skeleton-length route

## Failed-Idea Warnings

- `9XXX`: failed ideas and empirical warnings
  - `908X`: skeleton covering counterexample
  - `962X`: May 21 four-point route fails for CE0, $N_+=1$, all Vd0
  - `9630`: May 25 five-point route fails for CE1/CE2 all-Vd0
  - `964X`: CE1/CE2 area-conjecture route failure
- `3172`: exact counterexample to the full T3-like coordinatewise tangent
  envelope; the `317X` branch is closed by the direct area theorem in `3175`
  instead.
