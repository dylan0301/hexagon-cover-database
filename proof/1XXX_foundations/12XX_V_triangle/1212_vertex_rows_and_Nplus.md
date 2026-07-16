# Vertex Rows And Supercritical Count

Status: Definition

When no smaller handoff demands are present, a branch may write

$$
(a_i,b_i)
$$

for the actual maximal incoming and outgoing boundary reaches of the vertex
role $T_i$ at $V_i$.  When actual reaches and smaller selected demands occur
in the same argument, write

$$
(A_i,B_i)
$$

for the actual reaches and reserve $(a_i,b_i)$ for the selected demands.

For the $N_+$ split, the row entries are always the actual maximal reaches of
$T_i$, not smaller lower-bound demands introduced by a relaxation. If a
propagation map uses demands $(x,b)$, it must quantify the actual reaches
separately before imposing a nonsupercritical or supercritical row class.

An actual row is supercritical when its actual reaches have sum greater than
$1$.  Thus, in mixed notation,

$$
A_i+B_i>1,
$$

while in a file where $(a_i,b_i)$ denotes the actual reaches the same
condition is written $a_i+b_i>1$.  The proof-tree split always counts actual
rows:

$$
N_+
=
\left\lvert
\left\lbrace i:A_i+B_i>1\right\rbrace
\right\rvert
$$

in mixed notation, or equivalently

$$
N_+
=
\left\lvert
\left\lbrace i:a_i+b_i>1\right\rbrace
\right\rvert
$$

when the lowercase pair denotes actual reaches.  A supercritical selected
demand pair is useful inside a lower-bound argument, but it does not redefine
$N_+$.

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
with at least two selected supercritical rows when the actual count is at
least two.
