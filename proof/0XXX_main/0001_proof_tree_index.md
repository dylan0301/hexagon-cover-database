# Proof Tree Index

Status: Navigation

This is a numbered proof-structure tree. It is navigation only: a branch is not
proved merely because it appears here, and proof status is inherited from the
numbered source notes.

## Spine

Under a hypothetical seven-triangle cover, choose role triangles

$$
T_C,T_0,\dots,T_5.
$$

Classify $T_C$ as CE0, CE1, or CE2. Inside each CE branch, define perimeter
rows $(a_i,b_i)$ and compute

$$
N_+=\left\lvert \left\lbrace\, i : a_i+b_i>1 \,\right\rbrace \right\rvert.
$$

Then split first by CE0, CE1, or CE2; inside each CE branch split by
$N_+=0$, $N_+=1$, or $N_+\ge2$; inside each $N_+$ branch split by Vd0,
Vd1/Vd2, and T3-like vertex-role patterns.

## Setup

- `0XXX`: main scaffold
  - `0000`: main theorem scaffold
  - `0001`: proof tree index
  - `0002`: status and dependencies
- `1XXX`: foundations
  - `1003`: open-unit and shrunken-closed equivalence
  - `1006`: proof status conventions
  - `1101`: CE0, CE1, CE2 classification
  - `1201`: Vd0, Vd1, Vd2, and T3-like types
  - `1202`: local coordinates $(a,b,c)$
  - `1212`: vertex rows and $N_+$
  - `1213`: T3-like rows are nonsupercritical
- `2XXX`: geometric lemmas
  - `20XX`: V-triangle geometry
    - `2005`: midpoint self-cover criterion
    - `2006`: T3-like midpoint lemma
    - `2008`: neighbor-ray maximum formula
    - `2009`: ab-union curve for $a+b>1$
  - `21XX`: C-triangle geometry
    - `2100`: CE1/CE2 exactly-one-midpoint lemma
    - `2101`: maximal C-triangles over the half skeleton
    - `2102`: CE1 interval certificate
    - `2103`: CE2 interval-pair certificate
  - `25XX`: length bounds
    - `2500`: boundary length bounds
    - `2510`: skeleton length bounds
    - `2520`: diagonal length bounds
  - `26XX`: enclosing-triangle tools
    - `2607`: minimal enclosing equilateral quadrilateral lemma

## CE0 Branch

- `3XXX`: CE0
  - `30XX`: CE0, $N_+=0$
    - all Vd0
      - `3010`: perimeter-length obstruction
    - at least one Vd1/Vd2
      - no separate live branch; covered by the same $N_+=0$ length shortage structure
    - at least one T3-like and no Vd1/Vd2
      - no separate live branch; covered by the same $N_+=0$ length shortage structure
  - `31XX`: CE0, $N_+=1$
    - all Vd0
      - `310X`: algorithm-2 finite-point route
      - `3104`: May 21 four-point warning
    - at least one Vd1/Vd2
      - `314X`: boundary-length obstruction
    - at least one T3-like and no Vd1/Vd2
      - `317X`: conditional area-certificate route
      - `3174`: one-supercritical T3 certificate
  - `32XX`: CE0, $N_+\ge2$
    - all Vd0
      - `3208`: conditional area certificate
    - at least one Vd1/Vd2
      - `3208`: conditional area certificate
    - at least one T3-like and no Vd1/Vd2
      - `3208`: conditional area certificate
    - remaining local input
      - `3204`: supercritical vertex-loss lemma
  - `33XX`: old CE0 Vd1/Vd2 chain proof
    - `3301`: half-skeleton theorem
    - `3302`: rhombus geometry
    - `3303`: frontier perturbation
    - `3304`: chain inequalities
    - `3305`: midpoint-hole subcases
    - `3306`: assembly

## CE1 Branch

- `4XXX`: CE1
  - `40XX`: CE1, $N_+=0$
    - all Vd0
      - `401X`: boundary-loss package
      - `4013`: boundary-loss index
    - at least one Vd1/Vd2
      - `404X`: boundary-length obstruction
    - at least one T3-like and no Vd1/Vd2
      - open branch; no valid obstruction recorded here yet
  - `41XX`: CE1, $N_+=1$
    - all Vd0
      - `410X`: open branch
      - `9630`: May 25 five-point warning
    - at least one Vd1/Vd2
      - `411X`: boundary-length obstruction
    - at least two T3-like and no Vd1/Vd2
      - `412X`: shared CE1/CE2 diagonal obstruction
    - exactly one T3-like and no Vd1/Vd2
      - `413X`: open branch
  - `42XX`: CE1, $N_+\ge2$
    - all Vd0
      - `4200`: shared CE1/CE2 skeleton-length route
    - at least one Vd1/Vd2
      - `4200`: shared CE1/CE2 skeleton-length route
    - at least one T3-like and no Vd1/Vd2
      - `4200`: shared CE1/CE2 skeleton-length route

## CE2 Branch

- `5XXX`: CE2
  - `50XX`: CE2, $N_+=0$
    - all Vd0
      - `500X`: boundary-loss reference
    - at least one Vd1/Vd2
      - `501X`: length-route target
    - at least one T3-like and no Vd1/Vd2
      - `502X`: open branch
  - `51XX`: CE2, $N_+=1$
    - all Vd0
      - `510X`: open branch
      - `9630`: May 25 five-point warning
    - at least two Vd1/Vd2
      - `511X`: length-route target
    - exactly one Vd1/Vd2
      - `512X`: open branch
    - at least two T3-like and no Vd1/Vd2
      - `513X`: shared CE1/CE2 diagonal route
    - exactly one T3-like and no Vd1/Vd2
      - `514X`: open branch
  - `52XX`: CE2, $N_+\ge2$
    - all Vd0
      - `5200`: shared CE1/CE2 skeleton-length route
    - at least one Vd1/Vd2
      - `5200`: shared CE1/CE2 skeleton-length route
    - at least one T3-like and no Vd1/Vd2
      - `5200`: shared CE1/CE2 skeleton-length route

## Failed-Idea Warnings

- `9XXX`: failed ideas and empirical warnings
  - `908X`: full-skeleton noncoverage is not a standalone route
  - `962X`: May 21 four-point route fails for CE0, $N_+=1$, all Vd0
  - `9630`: May 25 five-point route fails for CE1/CE2 all-Vd0
  - `964X`: CE1/CE2 area-conjecture route failure
