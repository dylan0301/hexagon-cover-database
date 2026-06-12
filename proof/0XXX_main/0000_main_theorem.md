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
[`../1XXX_foundations/1003_open_unit_vs_shrunken_closed_equivalence.md`](../1XXX_foundations/1003_open_unit_vs_shrunken_closed_equivalence.md).

## Proof-tree spine

Under a hypothetical cover, choose one center role and six vertex roles:

$$
T_C,T_0,\dots,T_5.
$$

The intended proof first classifies $T_C$ as CE0, CE1, or CE2. Inside each CE
branch it defines the vertex perimeter rows $(a_i,b_i)$ and splits by

$$
N_+=\#\{i:a_i+b_i>1\}.
$$

The branch folders are:

- [`../3XXX_CE0/3000_CE0_index.md`](../3XXX_CE0/3000_CE0_index.md): CE0.
- [`../4XXX_CE1/4000_CE1_index.md`](../4XXX_CE1/4000_CE1_index.md): CE1.
- [`../5XXX_CE2/5000_CE2_index.md`](../5XXX_CE2/5000_CE2_index.md): CE2.

Local definitions and support targets are collected in:

- [`../1XXX_foundations/`](../1XXX_foundations/).
- [`../2XXX_geometric_lemmas/2000_geometric_lemmas_index.md`](../2XXX_geometric_lemmas/2000_geometric_lemmas_index.md).
- [`../9XXX_failed_ideas/9000_failed_idea_index.md`](../9XXX_failed_ideas/9000_failed_idea_index.md).

## Status warning

This scaffold records the intended proof tree. A branch is not proved merely
because it appears here. Proof status is inherited only from the cited source
files, using the conventions in
[`../1XXX_foundations/1006_proof_status_conventions.md`](../1XXX_foundations/1006_proof_status_conventions.md).
