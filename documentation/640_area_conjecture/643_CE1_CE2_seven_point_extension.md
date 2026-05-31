# CE1/CE2 Seven-Point Extension

Status: Strategy

This file records the perimeter-coordinate reduction used by the area
conjecture strategy after the main CE0 six-point case.

This is not the main target of the package.  The main target is the CE0
six-point model in `642_CE0_six_point_main_target.md`.

## CE1 normalization

Assume $T_C$ is CE1 and normalize the unique positive-length boundary overlap
to

$$
T_C\cap e_{0,1}=[s,t],
\qquad 0<s<t<1.
$$

The interval $[s,t]$ is the active $C$-only boundary interval on $e_{0,1}$.
The ordinary single cut point on $e_{0,1}$ is replaced by the two endpoints
$s$ and $t$.

For the other five edges, choose one cut point

$$
X_i=V_i+x_i(V_{i+1}-V_i),
\qquad i=1,\dots,5,
$$

with

$$
0\le x_i\le1.
$$

Thus the seven perimeter cut points are

$$
s,\quad t,\quad x_1,\quad x_2,\quad x_3,\quad x_4,\quad x_5.
$$

## Induced vertex rows

The six vertex-triangle boundary rows are:

$$
(a_0,b_0)=(1-x_5,s),
$$

$$
(a_1,b_1)=(1-t,x_1),
$$

and, for $i=2,3,4,5$,

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

These formulas use the convention that $a_i$ is the incoming boundary length
from $V_i$ and $b_i$ is the outgoing boundary length from $V_i$.

## CE2 usage

For CE2, this seven-point reduction is conditional on the CE2 one-interval
lemma.  After normalizing and using that lemma, one CE2 boundary interval is
treated as already covered by adjacent vertex triangles.  The remaining
positive-length $C$-only interval is then normalized to $[s,t]\subset e_{0,1}$
and the same seven-point model is used.

This file does not prove the CE2 one-interval lemma.  Without that reduction,
full CE2 has two active $C$ boundary intervals and the honest perimeter model
has more cut data than this seven-point package records.

## Area inequality target

For a fixed seven-point configuration, the CE1/reduced-CE2 extension uses the
same vertex-area target as the CE0 case:

$$
\#\{i:a_i+b_i>1\}\ge2
\quad\Longrightarrow\quad
\sum_{i=0}^5 f(a_i,b_i)<5.
$$

Only the formulas for the rows $(a_i,b_i)$ differ from CE0.  If the displayed
strict inequality is proved, the six vertex triangles contribute less than five
unit-triangle areas inside $H$.  The center triangle contributes at most one
unit-triangle area, so the seven triangles contribute less than the area of
$H$.

The threshold relaxation from `644_threshold_relaxation.md` applies row by row
in the same way as in CE0:

$$
a_i+b_i\ge1+\varepsilon
\quad\Longrightarrow\quad
f(a_i,b_i)\le f(a_i,1+\varepsilon-a_i).
$$
