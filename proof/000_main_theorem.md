# Main Theorem Proof Scaffold

Status: Strategy

This folder is a paper-style scaffold for the intended proof of the main
theorem. It does not replace the existing research notes. Existing files remain
the source of truth for definitions, proof status, computations, and failed
approaches.

## Main theorem target

$$
\boxed{\text{The regular side-}1\text{ hexagon }H\text{ cannot be covered by seven open unit equilateral triangles.}}
$$

The equivalent expanded closed-triangle target is:

$$
\boxed{\text{For every }L>1,\ H_L\text{ cannot be covered by seven closed unit equilateral triangles.}}
$$

The equivalence is proved in
[`100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`](100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md).

## Proof-tree spine

Under a hypothetical cover, choose one center role and six vertex roles:

$$
T_C,T_0,\dots,T_5.
$$

The intended proof first classifies $T_C$ as CE0, CE1, or CE2, defines the
vertex perimeter rows $(a_i,b_i)$, and then splits by

$$
N_+=\#\{i:a_i+b_i>1\}.
$$

The branch folders are:

- [`100_Nplus0/`](100_Nplus0/): no supercritical row.
- [`200_Nplus1/`](200_Nplus1/): exactly one supercritical row.
- [`300_Nplus_ge2/`](300_Nplus_ge2/): at least two supercritical rows.

Local definitions and support targets are collected in:

- [`010_setup/`](010_setup/).
- [`400_local_lemmas/`](400_local_lemmas/).
- [`500_finite_point_algorithms/`](500_finite_point_algorithms/).
- [`900_failed_and_empirical/`](900_failed_and_empirical/).

## Status warning

This scaffold records the intended proof tree. A branch is not proved merely
because it appears here. Proof status is inherited only from the cited source
files, using the conventions in
[`100_foundations/106_proof_status_conventions.md`](100_foundations/106_proof_status_conventions.md).
