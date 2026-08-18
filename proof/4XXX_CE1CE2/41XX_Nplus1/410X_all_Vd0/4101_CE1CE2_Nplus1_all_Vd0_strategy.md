# CE1/CE2, $N_+=1$, All Vd0: Exact Gap Closure

Status: Proven

## Theorem

Seven open unit equilateral triangles cannot cover the side-one hexagon $H$
when the center role is CE1 or CE2, all six vertex roles are Vd0, and
$N_+=1$.

The active proof depends only on the active-gap rank $N_{\rm gap}$, the number
of center traces that contain an active V-gap. Together with the $N_+=0$
theorem `4013`, the all-Vd0 kernel is

| actual V-triangle count | $N_{\rm gap}=0$ | $N_{\rm gap}=1$ | $N_{\rm gap}=2$ |
|---|---|---|---|
| $N_+=0$ | strict identity cycle | one-side exact-endpoint chain | common CE2 paired-endpoint chain |
| $N_+=1$ | center-independent nine-point obstruction | common five-V-triangle chain with a sign-dependent relaxation | common CE2 paired-endpoint chain |

The column $N_{\rm gap}=2$ is CE2-only. The canonical $g$-family is proved in
[`201d`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md).

## 1. Unique supercritical V triangle

Suppose such a cover exists. Write $U_C,U_0,\ldots,U_5$ for the open roles and
put

$$
T_C=\overline{U_C},
\qquad
T_i=\overline{U_i}.
$$

By the exactly-one-midpoint theorem
[`2100`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md),
normalize the exact center midpoint to

$$
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\}.
$$

Fix $i\ne0$. Since $M_i$ is covered but not in $T_C$, diameter locality leaves
only $U_{i-1},U_i,U_{i+1}$ as possible vertex roles containing it. If
$M_i\in U_j$ for $j\in\{i-1,i+1\}$, openness and convexity would give
$\mathcal H^1(T_j\cap r_i)>0$, contrary to Vd0.
Therefore

$$
M_i\in U_i\subset T_i.
$$

The midpoint self-cover theorem gives

$$
A_i+B_i\le1
\qquad(i=1,\ldots,5).
$$

Since $N_+=1$, V triangle $T_0$ is uniquely supercritical:

$$
\boxed{A_0+B_0>1.}
$$

## 2. Gap rank

On $e_{i,i+1}$, parametrized from $V_i$, the two incident open vertex traces
are

$$
[0,B_i)
\qquad\text{and}\qquad
(1-A_{i+1},1].
$$

Their missed set is

$$
\Gamma_i=
\begin{cases}
[B_i,1-A_{i+1}],&B_i\le1-A_{i+1},\\
\varnothing,&B_i>1-A_{i+1}.
\end{cases}
$$

A nonempty $\Gamma_i$ is a V-gap. Equality gives a singleton gap and is
retained because the roles are open. By boundary locality every V-gap lies in
a positive center trace.

Use the signed center normal form
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):

$$
I_R=\left[\frac{k}{R},W+\delta\right],
\qquad
I_L=\left[\frac{k}{W},R+\alpha\right],
$$

where

$$
\Delta_R=P-\alpha-W\delta>0,
\qquad
\Delta_L=P-R\alpha-\delta.
$$

The center is CE1 exactly when $\Delta_L\le0$ and CE2 exactly when
$\Delta_L>0$. Let $N_{\rm gap}$ be the number of these positive traces that
contain a V-gap. Then

$$
N_{\rm gap}\in\{0,1,2\},
$$

with $N_{\rm gap}\le1$ in CE1.

## 3. Rank zero: no active gap

If no center trace contains a V-gap, then no boundary edge has a V-gap. The
six Vd0 vertex roles alone cover $\partial H$, and exactly one actual V triangle is
supercritical. The center-independent direct nine-point obstruction
[`31058`](../../../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md)
gives a contradiction.

This is the only all-Vd0 cell in the kernel that is not closed by a relaxed
$g$-chain.

## 4. Rank one: the common five-V-triangle chain

After reflection, assume the active gap lies in $I_R$ and the companion trace
is absent or gap-free. Put

$$
X=R-\delta,
\qquad
H=\frac{k}{2R},
\qquad
m_3=\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\},
$$

and

$$
\begin{aligned}
c_1&=1-\frac{\delta}{R},&
c_2&=1-\delta,&
c_3&=1-m_3,\\
c_4&=1-\alpha,&
c_5&=1-\frac{\alpha}{W}.
\end{aligned}
$$

The common actual-V triangle theorem
[`4105`](4105_CE1_CE2_one_gap_five_V_triangle_interface.md) performs the exact chain

$$
\boxed{
[\Phi_{c_1}
\mid
\Phi_{c_2}
\mid
\Phi_{c_3}
\mid
\Phi_{c_4}
\mid
\Phi_{c_5}](X).
}
$$

It connects every formal iterate to the corresponding actual V triangle and compares
the returning demand with the exact capacity of $T_0$.

The first and fifth maps are relaxed to $\mathrm I$. Exact high-radial duality
reverses the remaining three slots and reduces both center classes to

$$
\boxed{
[\Phi_{1-\alpha}
\mid
\Phi_{1-m_3}
\mid
\Phi_{1-\delta}](H)
>
1-X.
}
$$

The sign of $\Delta_L$ determines only how this common target is relaxed.

### 4.1. CE1 relaxation

If $\Delta_L\le0$, the center is CE1. On the easy $L$ and $Q_-$ labels the
target is already exceeded. On the only surviving selected-$Q_+$ branch,
[`4106`](4106_CE1_one_gap_five_map_completion.md) proves the two affine lower
bounds

$$
\Phi_{1-\alpha}^{\,1-4\alpha}
\le
\Phi_{1-\alpha}^{
$$

and

$$
g_}{1-m_3}^{\vee,\,1-5m_3}
\le
\Phi_{1-m_3}
$$

at the realized inputs. The resulting value exceeds $e(\delta)$, so the final
slot is relaxed to

$$
\Phi_{1-\delta}^{\rm th}.
$$

Thus the hard branch is summarized by the single decorated chain

$$
\boxed{
[\Phi_{1-\alpha}^{\,1-4\alpha}
\mid
\Phi_{1-m_3}^{\,1-5m_3}
\mid
\Phi_{1-\delta}^{\rm th}](H)
>
1-X.
}
$$

### 4.2. CE2 relaxation

If $\Delta_L>0$, the center is CE2. The total-slack two-threshold theorem
[`4107`](4107_CE2_one_gap_five_map_completion.md) proves that one of the V triangle
$T_4$ and V triangle $T_2$ thresholds fires, while every other V triangle is needed only
through extensivity. In original V-triangle order the two possible lower chains are

$$
\boxed{
[\mathrm I
\mid
\mathrm I
\mid
\mathrm I
\mid
\Phi_{1-\alpha}^{\rm th}
\mid
\mathrm I](X)
>
1-H
}
$$

or

$$
\boxed{
[\mathrm I
\mid
\Phi_{1-\delta}^{\rm th}
\mid
\mathrm I
\mid
\mathrm I
\mid
\mathrm I](X)
>
1-H.
}
$$

Reflection exchanges

$$
R\longleftrightarrow W,
\qquad
\alpha\longleftrightarrow\delta
$$

and reverses the five V triangles, so the other CE2 orientation is identical.

Thus every rank-one state is impossible, including singleton gaps.

## 5. Rank two: two active gaps

This state is CE2-only. V triangles $T_1,\ldots,T_5$ are nonsupercritical Vd0 V triangles,
so the common two-gap theorem
[`2110`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2110_common_CE2_two_gap_application.md)
applies directly. It keeps the two endpoint high-radial outgoing bounds exact,
relaxes the three middle V triangles to $\mathrm I^3$, and invokes the paired
endpoint loss `2108`.

The ranks $N_{\rm gap}=0,1,2$ are exhaustive. Therefore the CE1/CE2,
$N_+=1$, all-Vd0 branch is impossible.

The older reduction
[`4104`](4104_all_boundary_transfer_to_310X.md) remains optional and is not an
active dependency.

$$
\Box
$$
