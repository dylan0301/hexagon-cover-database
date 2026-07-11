# Vertex Rows And Supercritical Count

Status: Strategy

When a branch is represented by perimeter handoff data, write

$$
(a_i,b_i)
$$

for the incoming and outgoing boundary lengths assigned to the vertex role
$T_i$ at $V_i$.

For the $N_+$ split, these are the actual selected row reaches of $T_i$, not
smaller lower-bound demands introduced by a relaxation. If a propagation map
uses demands $(x,b)$, it must quantify the actual reaches separately before
imposing a nonsupercritical or supercritical row class.

A row is supercritical when

$$
a_i+b_i>1.
$$

The proof-tree split uses

$$
N_+=\left\lvert \left\lbrace i : a_i+b_i>1 \right\rbrace \right\rvert.
$$

The main branch folders are:

- [`../../0XXX_main/0001_proof_tree_index.md`](../../0XXX_main/0001_proof_tree_index.md) for $N_+=0$.
- [`../../0XXX_main/0001_proof_tree_index.md`](../../0XXX_main/0001_proof_tree_index.md) for $N_+=1$.
- [`../../0XXX_main/0001_proof_tree_index.md`](../../0XXX_main/0001_proof_tree_index.md) for $N_+\ge2$.

The local vertex-coordinate conventions are recorded in
[`1202_local_coordinates_abc.md`](1202_local_coordinates_abc.md).
