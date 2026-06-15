# CE1/CE2 Seven-Point Area Model

Status: Failed

This file archives the seven-point perimeter-coordinate model from the failed
CE1/reduced-CE2 area-conjecture route.

This is not a live proof route.  The successful area certificate in the current
proof tree is the CE0 six-point conditional certificate in
[`../../3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md`](../../3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md).

## CE1 normalization

Assume $T_C$ is CE1 and normalize the unique positive-length boundary overlap
to

$$
T_C\cap e_{0,1}=[s,t], \qquad 0<s<t<1.
$$

The interval $[s,t]$ is the active $C$-only boundary interval on $e_{0,1}$.
The ordinary single cut point on $e_{0,1}$ is replaced by the two endpoints
$s$ and $t$.

For the other five edges, choose one cut point

$$
X_i=V_i+x_i(V_{i+1}-V_i), \qquad i=1,\dots,5,
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

## Failed area target

For a fixed seven-point configuration, the failed route tried to use the same
vertex-area target as the CE0 case:

$$
\left\lvert \left\lbrace\, i : a_i+b_i>1 \,\right\rbrace \right\rvert\ge2 \quad\Longrightarrow\quad \sum_{i=0}^5 f(a_i,b_i)<5.
$$

Only the formulas for the rows $(a_i,b_i)$ differ from CE0.  The displayed
strict inequality is not certified in this repository and should not be used as
a CE1/CE2 proof route.
