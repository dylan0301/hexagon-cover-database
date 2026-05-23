# Maximal C-Triangles Over the Half-Skeleton

Status: Definition / proof target

A $C$-triangle is a closed unit equilateral triangle constrained to contain $O$.

Maximality is measured over

$$
S_{1/2}=\partial H\cup\{O,M_0,\dots,M_5\}.
$$

## CE0

$$
T_C\cap\partial H=\varnothing.
$$

Maximality is by midpoint coverage and complementary-distance domination.

## CE1

Normalize the unique edge overlap to $e_{0,1}$:

$$
T_C\cap e_{0,1}=[s_{01},t_{01}].
$$

Maximality is interval inclusion:

$$
[s,t]\preceq[s',t']\iff s'\le s,\quad t'\ge t.
$$

### CE1 exact midpoint subset \(\{M_0\}\), normalized to \(e_{0,1}\)

The full proof and numerical check for the normalized target

\[
T_C\cap\{M_0,\dots,M_5\}=\{M_0\},
\qquad
T_C\text{ has positive-length boundary overlap only on }e_{0,1},
\]

is recorded in
[`213_CE1_M0_e01_maximal_intervals.md`](213_CE1_M0_e01_maximal_intervals.md).

For this subcase, the maximal feasible intervals are exactly

\[
\boxed{
[s,t]=
\left[
s,\,
\sqrt{s^2-s+1}-(1-s)^2
\right],
\qquad 0<s<1.
}
\]

The endpoints \(s=0\) and \(s=1\) are limiting degeneracies, not feasible positive-length CE1 intervals.

## CE2

Normalize the two overlaps to adjacent edges:

$$
T_C\cap e_{5,0}=[s_{50},t_{50}],
$$

$$
T_C\cap e_{0,1}=[s_{01},t_{01}].
$$

Maximality is product interval inclusion:

$$
([s_{50},t_{50}],[s_{01},t_{01}])\preceq
([s'_{50},t'_{50}],[s'_{01},t'_{01}])
$$

iff both intervals are contained in the primed intervals.

This file supports the CE1/CE2 exactly-one-midpoint proof write-up.
