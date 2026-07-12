# CE2 No-Support-to-Vd0 Normalization Target

Status: Lemma target

This note isolates the classification step needed between the general
positive-support split in `414a` and the reduced all-other-rows-Vd0 assembly
in `4148`.

## Statement

Assume an original open-cover role system is in CE2 with $N_+=1$, has exactly
one Vd1/Vd2 row, and has no other positive-adjacent-support row. For every
remaining vertex role with no adjacent-ray support, including the unique
supercritical row, construct or select a Vd0 replacement that preserves:

- both assigned adjacent boundary reaches;
- the center-induced own-radial demand;
- the full target coverage used by the branch; and
- its row-sum class: $a_i+b_i\le1$ for an ordinary row, and
  $a_i+b_i>1$ for the unique supercritical row.

The replacements must be simultaneous or accompanied by an argument that
successive replacements do not destroy earlier coverage.

## Why this target is needed

The displayed labels in `1201` are not literally exhaustive for an original
nonmaximalized role. In particular, a no-support role, whether ordinary or
supercritical, can have outside-vertex data

$$
(o,n)=(3,0)
$$

can occur without being called Vd0. The local files assembled in `4148` and
the classified input of `4013` are stated for Vd0 rows. Absence of adjacent
support alone does not supply the missing normalization.

The strengthened `414a` proves that every candidate with an additional
positive-support row is impossible. Thus this normalization target is the
only remaining classification bridge before the reduced `4148` case split
can be applied.
