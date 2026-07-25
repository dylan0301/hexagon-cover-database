# CE2 Two-Gap Completion for $N_+=1$, All Vd0

Status: Proven

This note proves the CE2 two-gap subcase of `410X` using the signed center
normal form and the exact two-endpoint loss theorem.

## 1. Setup

Assume a hypothetical seven-open-unit-triangle cover has:

- a CE2 center role;
- six Vd0 vertex roles;
- $N_+=1$;
- a V-gap, possibly a singleton, in each of the two center traces.

Normalize the unique center midpoint to $M_0$. The argument in
[`4101`](4101_CE1CE2_Nplus1_all_Vd0_strategy.md) shows that rows
$T_1,\ldots,T_5$ are nonsupercritical and $T_0$ is the unique supercritical
row.

Use the signed CE2 variables in
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
k=\eta+\alpha+\delta,
$$

with

$$
\alpha+W\delta<P,
\qquad
R\alpha+\delta<P.
$$

The two center traces are

$$
\left[\frac{k}{W},R+\alpha\right]
\subset e_{5,0},
$$

and

$$
\left[\frac{k}{R},W+\delta\right]
\subset e_{0,1}.
$$

Put their far-side inputs

$$
p=1-(R+\alpha)=W-\alpha,
$$

$$
q=1-(W+\delta)=R-\delta.
$$

Both are strictly positive.

## 2. Endpoint demands

The left V-gap is contained in the open center trace on $e_{5,0}$. Therefore
the endpoint role at $V_5$ must reach at least $p$ on that edge:

$$
b_5\ge p.
$$

Likewise the right V-gap gives

$$
a_1\ge q.
$$

The common radial-exit formulas in `2109` give

$$
c_5=1-\frac{\alpha}{W}=\frac pW,
$$

and

$$
c_1=1-\frac{\delta}{R}=\frac qR.
$$

Let

$$
\widehat B_c(a)=\min\{B_c(a),1-a\}
$$

be the exact safe map for a nonsupercritical row. Reflection of the local
coordinates for $T_5$ and the proof-safe capped-map theorem give

$$
B_5\le\widehat B_{p/W}(p),
$$

$$
B_1\le\widehat B_{q/R}(q),
$$

where $B_5$ and $B_1$ denote the outgoing reaches of $T_5$ and $T_1$ on
$e_{4,5}$ and $e_{1,2}$.

The exact two-endpoint theorem
[`2108`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2108_CE2_two_endpoint_capped_loss.md)
applies after reflecting if necessary so that its smaller weight comes first.
Its two strict endpoint hypotheses are exactly the two signed trace
inequalities above. It gives

$$
\boxed{
\widehat B_{p/W}(p)
+
\widehat B_{q/R}(q)
<1.
}
$$

Consequently

$$
\boxed{B_1+B_5<1.}
$$

## 3. Boundary contradiction

The center has no positive boundary trace on

$$
e_{1,2}\cup e_{2,3}\cup e_{3,4}\cup e_{4,5}.
$$

By Vd0 locality, after the endpoint contributions of $T_1$ and $T_5$, the
three rows $T_2,T_3,T_4$ must cover boundary length at least

$$
(1-B_1)+1+1+(1-B_5)
=4-(B_1+B_5)>3.
$$

But these rows are nonsupercritical, so

$$
(a_2+b_2)+(a_3+b_3)+(a_4+b_4)
\le3.
$$

This contradiction eliminates the CE2 two-gap state.

$$
\Box
$$
