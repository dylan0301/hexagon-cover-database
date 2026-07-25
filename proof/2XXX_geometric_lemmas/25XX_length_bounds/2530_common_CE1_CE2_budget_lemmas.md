# Common CE1/CE2 Boundary and Skeleton Budgets

Status: Proven

This note collects the length consequences of the signed center normal form
[`2109`](../21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md).
It replaces repeated CE1/CE2 boundary sums and isolates the small-slack domain
used in the surviving CE2 one-Vd1/Vd2 branch.

## 1. Signed center-boundary formula

Use the notation

$$
0<R<1,
\qquad
W=1-R,
\qquad
E=\sqrt{1-RW},
$$

$$
\eta=1-E,
\qquad
P=E(1-E),
$$

$$
\Delta_R=P-\alpha-W\delta>0,
\qquad
\Delta_L=P-R\alpha-\delta.
$$

The full center-boundary contribution is

$$
\boxed{
L_C:=L_{\partial H}(T_C)
=
\frac{\Delta_R}{R}
+
\frac{[\Delta_L]_+}{W}.
}
$$

### CE1

If $\Delta_L\le0$, then $R\alpha+\delta\ge P$. Multiplication by $W$ and
$\alpha\ge RW\alpha$ give

$$
\alpha+W\delta\ge WP.
$$

Thus $\Delta_R\le RP$, and hence

$$
\boxed{L_C\le P.}
$$

Because $E\ge\sqrt3/2$ and $E(1-E)$ decreases on this interval,

$$
\boxed{
L_C\le\frac{\sqrt3}{2}-\frac34.
}
$$

### CE2

If $\Delta_L>0$, then

$$
\begin{aligned}
L_C
&=
\frac{P-\alpha-W\delta}{R}
+
\frac{P-R\alpha-\delta}{W}\\
&=
\frac{P-E^2(\alpha+\delta)}{RW},
\end{aligned}
$$

because

$$
W+R^2=W^2+R=E^2.
$$

Also

$$
\frac{P}{RW}=\frac{E}{1+E}.
$$

Therefore

$$
\boxed{
L_C
=
\frac{E}{1+E}
-
\frac{E^2(\alpha+\delta)}{RW}
<\frac12.
}
$$

This proves both center-role entries of the boundary-cap table in
[`2500`](2500_boundary_length_bounds.md) from one formula.

## 2. Master perimeter-deficit lemma

Put

$$
\theta=\frac2{\sqrt3}-1.
$$

Suppose a branch has:

- an exact-$M_0$ CE1 or CE2 center role with boundary contribution $L_C$;
- $n$ supercritical Vd0 rows, each with contribution at most $2/\sqrt3$;
- $m\ge1$ distinguished nonsupercritical rows with strict contribution bounds
  $q_1,\ldots,q_m<1$;
- $6-n-m$ remaining nonsupercritical rows, each with contribution at most $1$.

If

$$
\boxed{
L_C+n\theta
\le
\sum_{j=1}^m(1-q_j),
}
$$

then the seven roles do not cover $\partial H$.

Indeed, their total boundary contribution is strictly less than

$$
\begin{aligned}
L_C+n\frac2{\sqrt3}
+
\sum_{j=1}^m q_j
+
(6-n-m)
&=
6+L_C+n\theta-
\sum_{j=1}^m(1-q_j)\\
&\le6.
\end{aligned}
$$

The strictness follows from $m\ge1$ and the strict distinguished-row bounds.
This contradicts subadditivity for a cover of the length-$6$ perimeter.

## 3. One supercritical row and one Vd1/Vd2 row

Assume a branch has exactly:

- one supercritical Vd0 row;
- one Vd1 or Vd2 row;
- four nonsupercritical Vd0 rows.

The Vd1/Vd2 boundary cap is strict and equals $1/2$. Perimeter coverage would
therefore force

$$
L_C+\theta>\frac12.
$$

Put

$$
\boxed{
\kappa=\frac12-\theta
=\frac32-\frac2{\sqrt3}.
}
$$

Every surviving candidate satisfies

$$
\boxed{L_C>\kappa.}
$$

The CE1 cap gives

$$
L_C+\theta
\le
\left(\frac{\sqrt3}{2}-\frac34\right)
+
\left(\frac2{\sqrt3}-1\right)
<\frac12.
$$

Hence every survivor is CE2. Put

$$
T=\alpha+\delta.
$$

The CE2 boundary formula and $L_C>\kappa$ give

$$
T<M(E):=
\frac{RW}{E^2}
\left(
\frac{E}{1+E}-\kappa
\right).
$$

Since $RW=1-E^2$,

$$
M(E)=
\frac{1-E}{E^2}
\left(E-\kappa(1+E)\right),
$$

and

$$
M'(E)=-\frac{E-2\kappa}{E^3}<0
$$

for $\sqrt3/2\le E<1$. Here $2\kappa<\sqrt3/2$, because this is equivalent
to $6\sqrt3<11$, whose square is $108<121$. Thus

$$
T
<
M\left(\frac{\sqrt3}{2}\right)
=
\frac{8\sqrt3}{9}-\frac32
<
\frac1{24}.
$$

The last comparison follows from $64\sqrt3<111$, whose square is
$12288<12321$. Therefore

$$
\boxed{\alpha+\delta<\frac1{24}.}
$$

There is also an orientation-sensitive estimate. Since $E/(1+E)<1/2$,

$$
T
<
\frac{RW}{E^2}
\left(\frac12-\kappa\right)
=
\frac{RW}{E^2}\theta.
$$

Now $RW/E^2\le R$ and $RW/E^2\le W$, because

$$
E^2=W+R^2=R+W^2.
$$

Also $\theta<1/6$, equivalently $12<7\sqrt3$, whose square is $144<147$.
Hence

$$
\boxed{
\alpha+\delta
<
\frac{\min\{R,W\}}6.
}
$$

These are the only global CE2 estimates used in the shortened adjacent and
non-adjacent one-Vd1/Vd2 obstructions.

## 4. CE2 total-slack and endpoint lemma

Assume $\Delta_R>0$ and $\Delta_L>0$, and put

$$
T=\alpha+\delta.
$$

Multiply

$$
\alpha+W\delta<P
$$

by $W$, multiply

$$
R\alpha+\delta<P
$$

by $R$, and add. Since

$$
W+R^2=W^2+R=E^2,
$$

we get

$$
E^2T<P=E\eta.
$$

Therefore

$$
\boxed{T<\frac{\eta}{E}.}
$$

The two initial endpoints of the CE2 traces are

$$
x=\frac{\eta+T}{W},
\qquad
y=\frac{\eta+T}{R}.
$$

Because

$$
E^2-(2R-1)^2=3RW>0,
$$

one has $|2R-1|<E$ and hence $|2R-1|T<\eta$. It follows that

$$
x-2T
=
\frac{\eta-(1-2R)T}{W}>0,
$$

and

$$
y-2T
=
\frac{\eta-(2R-1)T}{R}>0.
$$

Thus

$$
\boxed{
T<\frac12\min\{x,y\}.
}
$$

## 5. Three-short-role skeleton theorem

Call a vertex role **short** when it is either supercritical or has
positive-length intersection with an adjacent radial arm.

The proved bounds in [`2510`](2510_skeleton_length_bounds.md) are

$$
L_S(T_C)<\frac32
$$

for an exact-$M_0$ CE1/CE2 center role;

$$
L_S(T_i)<\frac32
$$

for every short vertex role; and

$$
L_S(T_i)\le2
$$

for every remaining nonsupercritical row with no adjacent-ray support.

If there are $q\ge3$ short vertex roles, then

$$
\begin{aligned}
L_S(T_C)+\sum_{i=0}^5L_S(T_i)
&<
\frac32+q\frac32+(6-q)2\\
&=
\frac{27-q}{2}\\
&\le12.
\end{aligned}
$$

Since the full skeleton has length $12$, subadditivity gives a contradiction.
Therefore

$$
\boxed{
\text{three short vertex roles imply skeleton noncoverage.}
}
$$

This single count contains the numerical cores of the at-least-two-T3-like,
mixed-positive-support, and at-least-two-supercritical CE1/CE2 branches.
