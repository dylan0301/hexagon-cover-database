# Vertex V-Triangle Reaches and the Count $N_+$

Status: Definition

Actual maximal incoming and outgoing boundary reaches are always denoted

$$
(A_i,B_i).
$$

Selected lower-bound handoff demands are always denoted

$$
(a_i,b_i).
$$

The two alphabets are never interchanged. A vertex V triangle is
supercritical exactly when its actual reaches satisfy

$$
A_i+B_i>1.
$$

Accordingly the proof-tree count is always

$$
N_+
=
\left\lvert
\left\lbrace i:A_i+B_i>1\right\rbrace
\right\rvert.
$$

A selected demand pair with $a_i+b_i>1$ may witness a selected strict ascent,
but it never defines or redefines $N_+$.

The main branch folders are:

- [`../../0XXX_main/0001_proof_tree_index.md`](../../0XXX_main/0001_proof_tree_index.md) for $N_+=0$.
- [`../../0XXX_main/0001_proof_tree_index.md`](../../0XXX_main/0001_proof_tree_index.md) for $N_+=1$.
- [`../../0XXX_main/0001_proof_tree_index.md`](../../0XXX_main/0001_proof_tree_index.md) for $N_+\ge2$.

The local vertex-coordinate conventions are recorded in
[`1202_local_coordinates_abc.md`](1202_local_coordinates_abc.md).

The strict boundary-overlap construction connecting actual reaches to
selected handoff demands is proved in
[`1214_strict_boundary_handoff_selection.md`](1214_strict_boundary_handoff_selection.md).
That theorem proves exact-one preservation and the existence of a selection
with at least two selected supercritical V triangles when the actual count is at
least two.
