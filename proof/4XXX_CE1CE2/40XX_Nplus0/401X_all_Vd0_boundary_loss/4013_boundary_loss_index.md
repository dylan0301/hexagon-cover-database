# CE1/CE2 All-Vd0 Skeleton-Data Obstruction

Status: Proven

## Theorem: skeleton-level form

Let

$$
U_C,U_0,\ldots,U_5
$$

be open unit equilateral triangles with

$$
O\in U_C,
\qquad
V_i\in U_i
\quad(i=0,\ldots,5),
$$

and put

$$
T_C=\overline{U_C},
\qquad
T_i=\overline{U_i}.
$$

Assume:

1. the center role is CE1 or CE2;
2. every vertex role is Vd0;
3. every vertex role is nonsupercritical:
   $$
   A_i+B_i\le1
   \qquad(i=0,\ldots,5);
   $$
4. the seven open roles cover the full hexagon skeleton
   $$
   S=\partial H\cup\bigcup_{i=0}^5r_i.
   $$

Then no such configuration exists.

Consequently, seven roles satisfying the first three hypotheses cannot cover
all of $H$. Equivalently, every CE1/CE2 all-Vd0 cover of $H$ has at least one
supercritical V triangle.

The theorem is deliberately stated at skeleton level. Its proof uses boundary
traces, radial handoffs, and center-free boundary paths, but no point of
$H\setminus S$. This is the exact strength needed by geometric replacement
arguments such as `4147`.

## 1. Skeleton coverage supplies the radial demands

Let $d_i^C$ be the center reach on $r_i$, measured from $O$ toward $V_i$, and
put

$$
c_i^C=1-d_i^C.
$$

### Lemma 1.1

Under the theorem hypotheses,

$$
\boxed{C_i\ge c_i^C\qquad(i=0,\ldots,5).}
$$

### Proof

Measure $r_i$ from $V_i$ toward $O$. The center trace, when nonempty, begins
at coordinate $c_i^C$. A Vd0 role has no positive-length trace on either
adjacent radial arm. A vertex role based at a nonlocal vertex is excluded from
a positive interval of $r_i$ by the diameter-one condition. Hence, among the
six vertex roles, only $U_i$ can cover a positive interval issuing from
$V_i$ on $r_i$.

If $C_i<c_i^C$, the open interval between the end of the $U_i$ trace and the
beginning of the center trace is uncovered. This contradicts coverage of
$S$. Therefore $C_i\ge c_i^C$. $\square$

This lemma is the only radial consequence needed below. It follows from
skeleton coverage alone.

## 2. Boundary gaps and active-gap rank

On $e_{i,i+1}$, parameterized from $V_i$, the two incident open vertex traces
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

A nonempty $\Gamma_i$ is a V-gap. Equality gives a singleton V-gap and is
retained because both vertex roles are open.

Boundary locality excludes every nonincident vertex role from a
positive-length part of $e_{i,i+1}$. Since the skeleton is covered, every
nonempty V-gap lies in the open center role. Openness then places it in a
positive center trace, even when the V-gap is a singleton.

Let

$$
\mathrm{gr}\in\{0,1,2\}
$$

be the number of positive center traces containing a V-gap. One has
$\mathrm{gr}\le1$ for CE1. The three ranks are exhaustive.

| rank | exact data retained | relaxed internal chain | terminal contradiction |
|---|---|---|---|
| $0$ | six strict open handoffs | $\mathrm I^6$ | strict cyclic ascent |
| $1$ | two exact high-radial endpoint outputs | center-free $\mathrm I^3$ | one-side endpoint sum $<1$ |
| $2$ | two exact high-radial endpoint outputs | center-free $\mathrm I^3$ | paired CE2 endpoint sum $<1$ |

## 3. Rank zero: strict cyclic ascent

Suppose no positive center trace contains a V-gap. Then there is no V-gap on
any boundary edge. Hence the six open vertex traces themselves cover every
boundary edge. Openness gives the strict handoffs

$$
B_i>1-A_{i+1};
$$

equality would leave the common endpoint of the two open traces uncovered.

Since $T_i$ is nonsupercritical,

$$
1-B_i\ge A_i.
$$

Therefore

$$
A_{i+1}>1-B_i\ge A_i.
$$

Iteration gives

$$
A_0<A_1<A_2<A_3<A_4<A_5<A_0,
$$

a contradiction.

## 4. Rank one: one exact endpoint pair

Use the signed center normal form
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):

$$
0<R<1,
\qquad
W=1-R,
\qquad
E=\sqrt{1-RW},
\qquad
\eta=1-E,
\qquad
k=\eta+\alpha+\delta.
$$

After reflection, assume the active V-gap lies in

$$
I_R=\left[\frac{k}{R},W+\delta\right]\subset e_{0,1},
$$

while the companion trace on $e_{5,0}$ is absent or contains no V-gap. Put

$$
s=\frac{k}{R},
\qquad
q=R-\delta,
\qquad
\omega=W+\delta-\frac{k}{R}.
$$

Then

$$
s+q+\omega=1.
$$

Containment of the V-gap gives the weak endpoint demands

$$
B_0\ge s,
\qquad
A_1\ge q.
$$

The companion edge contains no V-gap, so its two incident open vertex traces
cover it and in particular

$$
A_0+B_5\ge1.
$$

Since $T_0$ is nonsupercritical,

$$
A_0+B_0\le1,
$$

and hence

$$
B_5\ge1-A_0\ge B_0\ge s.
$$

The signed radial exits are

$$
d_1^C=\frac{\delta}{R},
\qquad
d_5^C=\frac{\alpha}{W}.
$$

Lemma 1.1 therefore supplies the exact high-radial lower demands

$$
C_1\ge c_1:=1-\frac{\delta}{R},
\qquad
C_5\ge c_5:=1-\frac{\alpha}{W}.
$$

The one-side theorem
[`2107`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md)
applies to these signed endpoint data and gives

$$
\boxed{
g_{c_5}(1-s)+g_{c_1}(1-q)<1.
}
$$

Let $B_5^{\rm far}$ and $B_1^{\rm far}$ be the reaches of $T_5$ and $T_1$
on the two boundary edges leading away from the center traces. Reflection of
the local admissible set when needed gives

$$
B_5^{\rm far}\le g_{c_5}(1-s),
\qquad
B_1^{\rm far}\le g_{c_1}(1-q),
$$

and therefore

$$
B_1^{\rm far}+B_5^{\rm far}<1.
$$

Apply the corrected path theorem
[`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
to $T_2,T_3,T_4$. The center's only possible positive boundary traces are on
$e_{0,1}$ and $e_{5,0}$, so the internal path edges $e_{2,3},e_{3,4}$ are
center-free. Diameter locality excludes nonincident vertex roles. Coverage of
the boundary part of $S$ forces

$$
\sum_{i=2}^4(A_i+B_i)
\ge4-(B_1^{\rm far}+B_5^{\rm far})>3,
$$

contrary to the three nonsupercritical caps.

The proof is identical for CE1 and for the rank-one CE2 state. A gap-free
companion trace is absorbed into the endpoint component and never occurs on an
internal path edge.

## 5. Rank two: paired CE2 endpoints

This state is CE2-only. The skeleton-data version of the common two-gap theorem
[`2110`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2110_common_CE2_two_gap_application.md)
applies. Its proof uses only:

- the two boundary V-gaps;
- the radial lower demands supplied by Lemma 1.1;
- nonsupercriticality of $T_1,\ldots,T_5$;
- the center-free three-V-triangle boundary path.

It gives the exact paired endpoint loss and the same path contradiction.

The ranks $0,1,2$ are exhaustive, proving the skeleton-level theorem.

$$
\Box
$$
