# T3-like Area-Conjecture Package

Status: Strategy / conditional package

This folder records the CE0 area route for the case with exactly one
supercritical vertex row and one T3-like vertex row.

The package is separate from `../../32XX_Nplus_ge2/`.  The `640` package
handles configurations with at least two supercritical rows.  This package
handles the complementary CE0 pattern in which the center triangle is CE0,
exactly one vertex row satisfies $a_i+b_i>1$, and one nonsupercritical vertex
row is T3-like.

No midpoint condition is imposed on the T3-like row in this package.  The
T3-like hypothesis means only

$$
(o,n)=(2,1),
$$

where $o$ is the number of vertices of the local unit triangle outside $H$ and
$n$ is the number of adjacent rays with positive-length intersection.

## CE0 perimeter model

Use the CE0 six-point model recorded in
`../../32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md`.
Choose one cut point on each boundary edge:

$$
X_i=V_i+x_i(V_{i+1}-V_i), \qquad 0\le x_i\le1, \qquad i=0,\dots,5.
$$

The induced vertex row at $V_i$ is

$$
(a_i,b_i)=(1-x_{i-1},x_i),
$$

with indices modulo $6$.  Hence

$$
a_i+b_i>1 \quad\Longleftrightarrow\quad x_i>x_{i-1}.
$$

## Local inputs used by this package

The final CE0 certificate in this folder is conditional on two local inputs.

### Input 1: Vd0 square-loss bounds

For Vd0 rows, assume the same square-loss bounds used by the `640` conditional
area certificate:

$$
a+b\le1 \quad\Longrightarrow\quad G_{\mathrm{Vd0}}(a,b)\ge \min(a,b)^2,
$$

and

$$
a+b>1 \quad\Longrightarrow\quad G_{\mathrm{Vd0}}(a,b)\ge \max(a,b)^2,
$$

where $G=1-f$ is normalized outside area.

These bounds are not proved in this folder.  They remain the same local proof
obligation recorded in
`../../32XX_Nplus_ge2/3202_area_function_and_monotonicity.md`.

### Input 2: full T3-like tangent-envelope conjecture

The local T3-like input is the no-midpoint tangent-envelope conjecture stated in
[`3122_full_T3_like_tangent_envelope_conjecture.md`](3122_full_T3_like_tangent_envelope_conjecture.md)
(Status: Lemma target).

That conjecture implies the proved analytic loss bound in
[`3123_T3_like_loss_from_envelope.md`](3123_T3_like_loss_from_envelope.md)
(Status: Proven analytic inequality conditional on local envelope):

$$
a,b\ge m \quad\Longrightarrow\quad
G_{\mathrm{T3}}(a,b)\ge 2m-4m^2.
$$

It also implies that T3-like rows are nonsupercritical:

$$
a+b\le1.
$$

## Main conditional theorem

Under the two local inputs above, the main theorem in
[`3124_CE0_one_supercritical_T3_certificate.md`](3124_CE0_one_supercritical_T3_certificate.md)
(Status: Proven analytic inequality conditional on local inputs) proves:

$$
\boxed{
\begin{gathered}
T_C\text{ is CE0},\\
\left\lvert \left\lbrace\, i : a_i+b_i>1 \,\right\rbrace \right\rvert=1,\\
\text{one row is T3-like and all other rows are Vd0}
\end{gathered}
\quad\Longrightarrow\quad
\sum_{i=0}^5 G_i>1.
}
$$

Therefore the six vertex triangles contribute strictly less than five
unit-triangle areas inside $H$.  The CE0 center triangle contributes at most one
unit-triangle area inside $H$, so the seven triangles contribute strictly less
than the normalized area $6$ of $H$.

## Files

| File | Recorded status | Notes |
|---|---|---|
| [`3122_full_T3_like_tangent_envelope_conjecture.md`](3122_full_T3_like_tangent_envelope_conjecture.md) | Lemma target | States the no-midpoint T3-like tangent-envelope conjecture and derives the candidate tangent branch formulas. |
| [`3123_T3_like_loss_from_envelope.md`](3123_T3_like_loss_from_envelope.md) | Proven analytic inequality conditional on local envelope | Proves the analytic consequences of the tangent envelope needed globally: nonsupercriticality and the loss bound $G_{\mathrm{T3}}\ge2m-4m^2$. |
| [`3124_CE0_one_supercritical_T3_certificate.md`](3124_CE0_one_supercritical_T3_certificate.md) | Proven analytic inequality conditional on local inputs | Proves the CE0 one-supercritical T3-like area contradiction under the two local inputs. |
| [`3125_failures_and_open_obligations.md`](3125_failures_and_open_obligations.md) | Reference | Records the precise failure modes and remaining proof obligations. |
| [`3126_CE0_no_Vd1_Vd2_with_T3_like.md`](3126_CE0_no_Vd1_Vd2_with_T3_like.md) | Strategy / incomplete | Records the separate directed-graph strategy for CE0 with no Vd1/Vd2 and at least one T3-like row. |

## Status warning

This folder contains a complete proof of the global analytic implication from
the stated local inputs.  It does not prove the full T3-like tangent-envelope
conjecture and does not prove the Vd0 square-loss bounds.  Consequently it is
not an unconditional proof of the CE0 T3-like case until those local inputs are
proved or certified.
