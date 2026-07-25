# CE1/CE2 All-Vd0 Boundary-Loss Obstruction

Status: Proven

## Theorem

Assume the center role is CE1 or CE2, all six vertex roles are Vd0, and

$$
a_i+b_i\le1
\qquad(i=0,\ldots,5).
$$

Then the seven roles cannot cover the hexagon. Equivalently, every CE1/CE2
all-Vd0 cover has at least one supercritical vertex row.

The proof uses one signed center normal form and splits only according to the
number of center traces containing active V-gaps.

## 1. Common boundary bookkeeping

Let $B_1$ and $B_5$ be valid upper bounds for the outgoing reaches of the two
endpoint roles on $e_{1,2}$ and $e_{4,5}$. The three middle rows must then
cover boundary length at least

$$
(1-B_1)+1+1+(1-B_5)
=4-(B_1+B_5).
$$

Their nonsupercritical row caps give total capacity at most $3$. Therefore

$$
\boxed{B_1+B_5<1}
$$

is sufficient for a contradiction.

For a nonsupercritical row, use the exact safe map

$$
\widehat B_c(a)=\min\{B_c(a),1-a\}.
$$

If its actual incoming and radial reaches are at least $a$ and $c$, the
proof-safe capped-map theorem
[`2011`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md)
gives the outgoing upper bound $\widehat B_c(a)$.

## 2. No active center gap

Suppose every positive center trace is already covered by the endpoint vertex
roles. Then the six original open vertex roles alone cover $\partial H$.

Let $U_i$ be the trace of the original open role at $V_i$ on $\partial H$.
Each $U_i$ is relatively open in the connected polygonal circle $\partial H$
and has length at most $a_i+b_i\le1$. At least two of the sets are nonempty,
and the nonempty members of a finite relatively open cover of a connected
space cannot be pairwise disjoint. Hence two traces overlap in a relatively
open set of positive length. Therefore

$$
\sum_{i=0}^5\mathcal H^1(U_i)
>
\mathcal H^1\left(\bigcup_{i=0}^5U_i\right)
=6,
$$

contrary to

$$
\sum_{i=0}^5\mathcal H^1(U_i)
\le
\sum_{i=0}^5(a_i+b_i)
\le6.
$$

Thus a candidate must have at least one active center gap.

## 3. Signed center data

Use the common normal form
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):

$$
0<R<1,
\qquad
W=1-R,
$$

$$
E=\sqrt{1-RW},
\qquad
\eta=1-E,
\qquad
P=E(1-E),
$$

$$
k=\eta+\alpha+\delta.
$$

The normalized right trace is

$$
I_R=
\left[\frac{k}{R},W+\delta\right],
$$

and the possible companion trace is

$$
I_L=
\left[\frac{k}{W},R+\alpha\right].
$$

The complementary radial demands at the two far endpoint rows are

$$
\boxed{
c_1=1-\frac{\delta}{R},
\qquad
c_5=1-\frac{\alpha}{W}.
}
$$

## 4. Exactly one active center gap

After reflection if necessary, assume $I_R$ contains an active V-gap and the
companion trace is empty or contains no V-gap. Put

$$
s=\frac{k}{R},
\qquad
\nu=1-(W+\delta)=R-\delta,
$$

and let

$$
\omega=W+\delta-\frac{k}{R}
$$

be the width of $I_R$. Then

$$
s+\nu+\omega=1.
$$

The gap containment gives

$$
b_0\ge s,
\qquad
a_1\ge\nu.
$$

Because the companion trace has no active gap, coverage on $e_{5,0}$ gives

$$
a_0+b_5\ge1.
$$

Since row $T_0$ is nonsupercritical in the present $N_+=0$ branch,

$$
a_0+b_0\le1.
$$

Consequently

$$
b_5\ge1-a_0\ge b_0\ge s.
$$

The variables of the one-side loss theorem
[`2107`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md)
are exactly $R,s,\nu,\omega$. Its second deficit simplifies to

$$
\begin{aligned}
\gamma_5
&=
\nu-\frac{R}{1+E}-\frac{R}{W}\omega\\
&=
\frac{\alpha}{W}.
\end{aligned}
$$

Thus `2107` gives

$$
\boxed{
\widehat B_{1-\alpha/W}(s)
+
\widehat B_{1-\delta/R}(\nu)
<1.
}
$$

The actual inputs of $T_5$ and $T_1$ are at least $s$ and $\nu$, so these are
valid outgoing upper bounds. Section 1 gives the contradiction.

This argument is identical for CE1 and CE2. The only distinction is that the
companion trace is absent in CE1 and present but gap-free in the CE2 one-gap
state.

## 5. Two active center gaps

This case requires $\Delta_L>0$ and is therefore CE2. Put the two far-side
inputs

$$
p=1-(R+\alpha)=W-\alpha,
$$

$$
q=1-(W+\delta)=R-\delta.
$$

Gap containment gives

$$
b_5\ge p,
\qquad
a_1\ge q.
$$

The exact radial demands are

$$
c_5=\frac pW=1-\frac{\alpha}{W},
$$

and

$$
c_1=\frac qR=1-\frac{\delta}{R}.
$$

The two-endpoint theorem
[`2108`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2108_CE2_two_endpoint_capped_loss.md)
gives

$$
\boxed{
\widehat B_{p/W}(p)
+
\widehat B_{q/R}(q)
<1.
}
$$

These are valid upper bounds for the two endpoint outputs, so Section 1 again
gives the contradiction.

The zero-, one-, and two-active-gap states exhaust CE1 and CE2. Hence the
all-Vd0, $N_+=0$ branch is impossible.

$$
\Box
$$
