# Support Isolation After the $T_0$ T3-Like Reduction

Status: Proven

This file records the support-isolation progress for the branch

$$
T_C\text{ is CE1 or CE2},\qquad N_+=0,
$$

with no Vd1/Vd2 rows and at least one T3-like vertex row.

It is used after the reduction in
[`4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md`](4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md), which proves that, after normalizing

$$
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\},
$$

one has

$$
T_0\text{ is T3-like}.
$$

We then reflect across the line through $O,V_0$ if necessary and assume

$$
T_0\text{ has positive-length support on }r_1=[O,V_1].
$$

This file deliberately does **not** assume $M_1\in T_0$ or $M_5\in T_0$.  The half-skeleton midpoint inventory in
[`../../../1XXX_foundations/12XX_V_triangle/1205_midpoint_subsets.md`](../../../1XXX_foundations/12XX_V_triangle/1205_midpoint_subsets.md)
concerns maximal normalized triangles over $S_{1/2}$ only, not maximal triangles over the full skeleton $S$.

## 1. Dependencies

We use the following recorded dependencies.

1. The CE1/CE2 exact-one-midpoint dependency:
   [`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md).
   Its hypothesis $O\in\mathrm{int}(T_C)$ is supplied by the original open
   center role before closure.

2. The T3-like midpoint exclusion:
   [`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2006_T3_like_midpoint_lemma.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2006_T3_like_midpoint_lemma.md):
   
   $$
   T_i\text{ T3-like}\quad\Longrightarrow\quad M_i\notin T_i.
   $$

3. T3-like rows are nonsupercritical:
   [`../../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md`](../../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md).

4. Vd0, Vd1, Vd2, and T3-like are exhaustive for original vertex roles:
   [`../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).

The two strict diagonal caps formerly imported from the practically-proven
`2520` note are proved next, so this file no longer depends on that status.

## 2. Exact diagonal caps

### Lemma 2.1: center contribution

The normalized CE1/CE2 center role satisfies

$$
\mathcal H^1(T_C\cap D)<\frac32.
$$

### Proof

Use the direct side model proved in
[`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md), with
$0<\lambda<1$ and

$$
\rho=\sqrt{1-\lambda+\lambda^2}.
$$

Put

$$
C_0=F_0(O),
\qquad
C_1=F_1(O),
\qquad
C_2=F_2(O).
$$

Then

$$
C_0+C_1+C_2=\rho.
$$

Direct substitution on the six unit-speed rays from $O$ gives the center
exit lengths

$$
\begin{aligned}
\gamma_0&=C_1,\\
\gamma_1&=\min\left\{\frac{C_1}{1-\lambda},\frac{C_2}{\lambda}\right\},\\
\gamma_2&=C_2,\\
\gamma_3&=\min\left\{\frac{C_0}{\lambda},\frac{C_2}{1-\lambda}\right\},\\
\gamma_4&=C_0,\\
\gamma_5&=\min\left\{\frac{C_0}{1-\lambda},\frac{C_1}{\lambda}\right\}.
\end{aligned}
$$

Therefore

$$
\sum_{i=0}^5\gamma_i
\le
\rho+\frac{C_2}{\lambda}
+\frac{C_0}{\lambda}
+\frac{C_0}{1-\lambda}.
$$

The positive-length interval on $e_{0,1}$ is equivalent to

$$
C_0+(1-\lambda)C_2<\rho(1-\rho).
$$

Consequently

$$
\sum_{i=0}^5\gamma_i
<
\rho+
\frac{\rho(1-\rho)}{\lambda(1-\lambda)}.
$$

Since

$$
\lambda(1-\lambda)=1-\rho^2,
$$

the right side is

$$
\rho+\frac{\rho}{1+\rho}\le\frac32.
$$

The last inequality follows because $x+x/(1+x)$ is increasing and
$\rho\le1$. Distinct rays meet only at $O$, a set of zero length, so their
exit lengths add to $\mathcal H^1(T_C\cap D)$. This proves the strict cap.

### Lemma 2.2: T3-like contribution

Every T3-like row satisfies

$$
\mathcal H^1(T_i\cap D)<\frac12.
$$

### Proof

Rotate and reflect to the selected T3-like orientation. Use parameters
$D>1$, $0<R<1$, and $\alpha\ge0$ satisfying

$$
R^2-DR+D^2=1,
$$

and put

$$
p=\frac1D-\alpha,
\qquad
q=1-p=\alpha+\frac{D-1}{D}.
$$

The own-ray contribution is $\alpha D/R$. The selected adjacent-ray interval
has endpoints

$$
c=\frac{Dq}{R},
\qquad
u=q+\frac{1-R}{D}.
$$

Positive adjacent support gives $c<u$. Multiplication by $DR$ and use of
$D^2-DR=1-R^2$ yields

$$
q<\frac{R}{1+R}.
$$

The type has no positive-length support on any other ray. Hence

$$
\begin{aligned}
\mathcal H^1(T_i\cap D)
&=\frac{\alpha D}{R}+u-c\\
&=q+\frac{1-R}{D}-\frac{D-1}{R}\\
&<\frac{R}{1+R}+\frac{1-R}{D}-\frac{D-1}{R}.
\end{aligned}
$$

After using $R^2-DR+D^2=1$, the last expression minus $1/2$ is

$$
-\frac{(D-1)(1-D+R)}{2R(1+R)}.
$$

This is negative. Indeed, $q\ge(D-1)/D$ together with
$q<R/(1+R)$ implies $D-1<R$. Reflection gives the other T3-like orientation.

An $N_+=0$ Vd0 row has no positive-length intersection with either adjacent
ray. Every point other than possibly $O$ on a nonadjacent ray is at distance
greater than $1$ from the row vertex, so a unit-diameter triangle containing
that vertex has no positive-length intersection there. Thus only the own ray
remains, and a Vd0 row contributes at most $1$ to $D$.

## 3. At most two T3-like rows

### Lemma 3.1

In the present branch, at most two vertex rows are T3-like.

### Proof

Let $k$ be the number of T3-like vertex rows.  Since $N_+=0$, every vertex row is nonsupercritical.  Since no row is Vd1 or Vd2, every non-T3-like vertex row is Vd0.

Let

$$
D=\bigcup_{i=0}^5 r_i
$$

be the diagonal target.  Its total length is

$$
\mathcal H^1(D)=6.
$$

By Lemmas 2.1 and 2.2, a CE1/CE2 center role contributes strictly less than
$3/2$, each T3-like row contributes strictly less than $1/2$, and each
nonsupercritical Vd0 row contributes at most $1$. Therefore the total
diagonal coverage is strictly less than

$$
{3\over2}+k\cdot {1\over2}+(6-k)\cdot 1={15-k\over2}.
$$

If $k\ge3$, this is at most $6$, contradicting coverage of $D$.

Thus $k\le2$.

## 4. $T_2$ and $T_4$ are Vd0

### Lemma 4.1

After the $4071$ reduction and the reflection normalization above,

$$
T_2\text{ is Vd0}.
$$

### Proof

Assume for contradiction that $T_2$ is T3-like. Since $T_0$ is already
T3-like, Lemma 3.1 implies that no other row can be T3-like.

By the T3-like midpoint exclusion,

$$
M_2\notin T_2.
$$

Also $M_2\notin T_C$, since $T_C$ covers exactly $M_0$ among the six radial midpoints.  The only vertex rows that can cover $M_2$ are local to $M_2$, namely $T_1,T_2,T_3$.  The row $T_2$ is excluded.  The rows $T_1,T_3$ cannot be T3-like, because that would create a third T3-like row.  Since no row is Vd1 or Vd2, $T_1,T_3$ are Vd0.  Vd0 rows have no positive-length adjacent-ray support and cannot cover an adjacent midpoint in this branch.

Thus $M_2$ would be uncovered, contradiction.  Hence $T_2$ is not T3-like.  Since no Vd1/Vd2 row exists, $T_2$ is Vd0.

### Lemma 4.2

Similarly,

$$
T_4\text{ is Vd0}.
$$

### Proof

The proof is the reflection of Lemma 4.1. If $T_4$ were T3-like, then
$M_4\notin T_4$. Its only local rescuers would be $T_3,T_5$, but neither can
be T3-like because $T_0$ and $T_4$ would already be two T3-like rows. With no
Vd1/Vd2 rows, $T_3,T_5$ are Vd0 and cannot rescue the adjacent midpoint. Thus
$M_4$ would be uncovered.

## 5. A point-contact lemma for $M_5$

### Lemma 5.1

If $T_0$ is T3-like and has positive-length adjacent support on $r_1$, then

$$
M_5\notin T_0.
$$

### Proof

Use normalized $V_0$-local coordinates

$$
X=V_0+x(V_5-V_0)+y(V_1-V_0).
$$

Thus

$$
V_0=(0,0),\qquad V_5=(1,0),\qquad V_1=(0,1),\qquad O=(1,1).
$$

For a T3-like $T_0$ with the side-through-$V_0$ normalization and adjacent support on $r_1$, write

$$
r=-R,\qquad s>0,\qquad D=s+R,
$$

with

$$
R^2-DR+D^2=1.
$$

Let $\tau\in[0,1]$ be the position of $V_0$ on the chosen side.  The triangle inequalities may be written as

$$
sx+Ry\ge0,
$$

$$
\tau+sy-Dx\ge0,
$$

and

$$
\tau-Rx+Dy\le1.
$$

On $r_5$, points have the form $(1,y)$, $0\le y\le1$.  The last two inequalities give

$$
y\ge {D-\tau\over s},\qquad y\le {1-\tau+R\over D}.
$$

Suppose $M_5\in T_0$.  In these coordinates, $M_5=(1,1/2)$.  Since $T_0$ has positive adjacent support on $r_1$, it has no positive-length support on $r_5$.  Hence the intersection with $r_5$ at $y=1/2$ must be a single point, and therefore

$$
{D-\tau\over s}={1\over2},\qquad {1-\tau+R\over D}={1\over2}.
$$

Using $s=D-R$, the first equality gives

$$
\tau={D+R\over2},
$$

while the second gives

$$
\tau=1+R-{D\over2}.
$$

Equating them yields

$$
R=2D-2.
$$

Substitution into

$$
R^2-DR+D^2=1
$$

gives

$$
3(D-1)^2=0.
$$

So $D=1$ and $R=0$, which degenerates the positive $r_1$ support.  This contradicts the T3-like support hypothesis.  Thus $M_5\notin T_0$.

## 6. $T_5$ is Vd0

### Lemma 6.1

In the present branch,

$$
T_5\text{ is Vd0}.
$$

### Proof

Assume for contradiction that $T_5$ is T3-like.  Then $T_0$ and $T_5$ are the two allowed T3-like rows, so no other row is T3-like.

By the T3-like midpoint exclusion,

$$
M_5\notin T_5.
$$

Also $M_5\notin T_C$, since $T_C$ covers exactly $M_0$ among the radial
midpoints. The only remaining local rescuers for $M_5$ are $T_4$ and $T_0$.
By Lemma 4.2, $T_4$ is Vd0 and cannot cover the adjacent midpoint $M_5$. By
Lemma 5.1, $M_5\notin T_0$.

Thus $M_5$ would be uncovered, contradiction.  Hence $T_5$ is not T3-like.  Since no row is Vd1 or Vd2, $T_5$ is Vd0.

## 7. Radial support isolation

### Theorem 7.1

After the $4071$ reduction and the reflection normalization,

$$
r_1\text{ has positive-length support only from }T_C,T_0,T_1,
$$

and

$$
r_5\text{ has positive-length support only from }T_C,T_5.
$$

### Proof

The only vertex roles that can have positive-length support on $r_1$ are local
to that ray: $T_0,T_1,T_2$. By Lemma 4.1, $T_2$ is Vd0, so it has no
positive-length adjacent support on $r_1$. Hence only $T_C,T_0,T_1$ can
support $r_1$.

Similarly, the only vertex roles that can have positive-length support on
$r_5$ are $T_4,T_5,T_0$. By Lemmas 4.2 and 6.1, $T_4$ and $T_5$ are Vd0
except that $T_5$ supports its own radial $r_5$. The row $T_0$ is T3-like but
has selected positive adjacent support on $r_1$, so it has no positive-length
support on $r_5$. Therefore only $T_C,T_5$ can support $r_5$.

## 8. Consequence for the $r_0$ tail

The preceding lemmas do not remove all possible support on $r_0$.  The only possible additional supporter besides $T_C$ and $T_0$ is $T_1$ if $T_1$ is T3-like and chooses $r_0$ as its adjacent radial support.

Therefore the correct downstream split is:

1. If $T_1$ does not support $r_0$, then $T_0$ must cover the remaining $r_0$ tail after $T_C$.
2. If $T_1$ supports $r_0$, that additional reach only shrinks its feasible
   set. The universal nonsupercritical relaxation in `4073` therefore remains
   a valid upper bound without a separate constrained map.

No assertion that all rows other than $T_0$ are Vd0 is made here; $T_1$ remains the exceptional possible T3-like row.
