# CE Classification Helper Spec

Status: Implementation note

Input:

- C-triangle geometry;
- hexagon edge list;
- tolerance.

Output:

- positive-length overlap intervals;
- CE type;
- degeneracy flags.

Rule:

$$
\mathrm{length}(T_C\cap e_i)>0
$$

counts as an edge overlap. Point-only overlap does not count.
