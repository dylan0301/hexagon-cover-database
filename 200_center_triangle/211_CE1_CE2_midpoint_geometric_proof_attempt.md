# CE1 / CE2 Exactly-One-Midpoint: Geometric Proof Attempt

Status: Strategy

Lemma recorded as proven in [`../500_half_skeleton_lemmas/503_CE1_CE2_exactly_one_midpoint_lemma.md`](../500_half_skeleton_lemmas/503_CE1_CE2_exactly_one_midpoint_lemma.md):

$$
T_C\text{ is CE1 or CE2}\implies \#\{i:M_i\in T_C\}=1.
$$

Geometric plan:

1. Normalize the CE1 or CE2 edge overlap using $D_6$.
2. Use convexity of $T_C$ and the six radial midpoint positions.
3. If two nonadjacent midpoints are covered, use the segment between them to force additional radial or boundary coverage.
4. If two adjacent midpoints are covered, use the equilateral side directions to force either CE0 failure or too many edge overlaps.
5. Show that CE1 and CE2 allow exactly one midpoint in the nondegenerate regime.

Current status: retained as the geometric proof route, not as the authoritative proof write-up.
