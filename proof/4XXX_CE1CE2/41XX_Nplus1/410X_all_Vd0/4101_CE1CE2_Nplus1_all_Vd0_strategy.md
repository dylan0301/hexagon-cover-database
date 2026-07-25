# CE1/CE2, $N_+=1$, All Vd0: Exact Gap Closure

Status: Proven

## Theorem

Seven open unit equilateral triangles cannot cover the side-one hexagon $H$
when the center role is CE1 or CE2, all six vertex roles are Vd0, and
$N_+=1$.

The center geometry is expressed by the signed common normal form
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md).
The one-gap actual-row induction is the common theorem
[`4105`](4105_CE1_CE2_one_gap_five_row_interface.md). The CE1 and CE2 files
`4106` and `4107` now contain only the two sign-dependent scalar completions.

## 1. Unique supercritical row

Suppose such a cover exists. Write $U_C,U_0,\ldots,U_5$ for the open roles and
put

$$
T_C=\overline{U_C},
\qquad
T_i=\overline{U_i}.
$$

The exactly-one-midpoint theorem allows the normalization

$$
T_C\cap\left\{M_0,\ldots,M_5\right\}=\left\{M_0\right\}.
$$

Fix $i\ne0$. Since $M_i$ is covered but not in $T_C$, diameter locality leaves
only $U_{i-1},U_i,U_{i+1}$ as possible vertex roles containing it. If an
adjacent role contained $M_i$, openness and convexity would give
positive-length support on the adjacent radial arm, contrary to Vd0.
Therefore $M_i\in U_i\subset T_i$. The midpoint self-cover theorem gives

$$
a_i+b_i\le1,
\qquad i=1,\ldots,5.
$$

Since $N_+=1$, row $T_0$ is uniquely supercritical:

$$
a_0+b_0>1.
$$

## 2. Gaps and open endpoints

On $e_{i,i+1}$, with coordinate measured from $V_i$, the adjacent open
vertex traces are

$$
[0,b_i)
\qquad\text{and}\qquad
(1-a_{i+1},1].
$$

Their missed set is

$$
G_i=
\begin{cases}
[b_i,1-a_{i+1}],&b_i\le1-a_{i+1},\\
\varnothing,&b_i>1-a_{i+1}.
\end{cases}
$$

A nonempty $G_i$ is a V-gap. Equality gives a singleton gap and is retained,
because the triangles are open. A missing gap is exactly the strict handoff
$b_i>1-a_{i+1}$.

By boundary locality, every V-gap lies in a positive center trace. If the
corresponding maximal closed center trace is $[s,t]$, gap containment gives

$$
b_i\ge s,
\qquad
a_{i+1}\ge1-t.
$$

These weak endpoint bounds include singleton gaps.

## 3. One signed center model

Use the variables of `2109`:

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

The normalized positive trace and the possible companion trace are

$$
I_R=\left[\frac{k}{R},W+\delta\right],
$$

and

$$
I_L=\left[\frac{k}{W},R+\alpha\right].
$$

Define

$$
\Delta_R=P-\alpha-W\delta>0,
$$

and

$$
\Delta_L=P-R\alpha-\delta.
$$

Then

$$
T_C\text{ is CE1}
\quad\Longleftrightarrow\quad
\Delta_L\le0,
$$

while

$$
T_C\text{ is CE2}
\quad\Longleftrightarrow\quad
\Delta_L>0.
$$

Thus there are only three gap patterns to consider: no active trace, exactly
one active trace, and two active traces. The last is possible only in CE2.

## 4. No active gap

If neither positive center trace contains a V-gap, then no edge has a V-gap.
The six Vd0 roles therefore cover every boundary edge with a strict handoff.
Hence the six vertex roles alone cover $\partial H$.

The center-independent direct nine-point obstruction
[`31058`](../../../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_Vd0_nine_point_obstruction.md)
then gives a contradiction.

## 5. Exactly one active gap

After reflection if necessary, suppose the active gap lies in $I_R$ and the
companion trace is empty or gap-free. The common actual-row theorem
[`4105`](4105_CE1_CE2_one_gap_five_row_interface.md) gives the five successive
nonsupercritical transitions through rows $1,2,3,4,5$ and reduces the branch
to one three-map scalar target.

If $\Delta_L\le0$, this is the CE1 sign. The selected-$T_+$ chord proof in
[`4106`](4106_CE1_one_gap_five_map_completion.md) proves the scalar target,
including every selected label and singleton gaps.

If $\Delta_L>0$, this is the CE2 sign with a gap-free companion trace. The
short total-slack and two-threshold proof in
[`4107`](4107_CE2_one_gap_five_map_completion.md) proves the same target.
Reflection exchanges

$$
R\longleftrightarrow W,
\qquad
\alpha\longleftrightarrow\delta,
$$

and reverses rows $1,\ldots,5$, so it also proves the other CE2 orientation.

Thus every exactly-one-gap state is impossible.

## 6. Two active gaps

Two active gaps require $\Delta_L>0$ and hence CE2. The paired endpoint
requirements share the same center triangle and the same supercritical row,
so they are not two independent one-gap chains. The exact rank-two endpoint
loss theorem is applied in
[`4102`](4102_CE2_two_gap_completion.md), which gives a boundary-length
contradiction for the three middle nonsupercritical rows.

Thus the two-gap state is impossible.

## 7. Conclusion

The no-gap, one-gap, and two-gap patterns exhaust CE1 and CE2. Every pattern
is impossible, proving the theorem.

The older reduction
[`4104`](4104_all_boundary_transfer_to_310X.md) to the conjectural inequality
$F_6(a,b)\ge1$ remains optional and is not used.

$$
\Box
$$
