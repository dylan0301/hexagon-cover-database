# CE0 One-Supercritical T3-like Area Certificate

Status: Proven

This file proves the global CE0 area contradiction for the case with exactly one
supercritical row and at least one T3-like row, assuming the local inputs
recorded in
[`3171_T3_like_area_certificate_index.md`](3171_T3_like_area_certificate_index.md).

No midpoint condition is imposed on any T3-like row.

## Local hypotheses

Throughout this file, normalized outside area is denoted by $G$.

### Hypothesis Vd0-square-loss

For every Vd0 row with local boundary data $(a,b)$,

$$
a+b\le1 \quad\Longrightarrow\quad G_{\mathrm{Vd0}}(a,b)\ge \min(a,b)^2,
$$

and

$$
a+b>1 \quad\Longrightarrow\quad G_{\mathrm{Vd0}}(a,b)\ge \max(a,b)^2.
$$

### Hypothesis T3-envelope

Assume the full T3-like tangent-envelope conjecture from
[`3172_full_T3_like_tangent_envelope_conjecture.md`](3172_full_T3_like_tangent_envelope_conjecture.md).

By [`3173_T3_like_loss_from_envelope.md`](3173_T3_like_loss_from_envelope.md),
this implies:

1. every T3-like row is nonsupercritical:

   $$
   a+b\le1;
   $$

2. for every $0\le m\le1/2$,

   $$
   a,b\ge m \quad\Longrightarrow\quad
   G_{\mathrm{T3}}(a,b)\ge 2m-4m^2.
   $$

3. for every $0\le m\le1/2$,

   $$
   a,b\ge m \quad\Longrightarrow\quad
   G_{\mathrm{T3}}(a,b)\ge m^2.
   $$

## CE0 model

Let $T_C$ be CE0.  Choose one cut point on each edge:

$$
X_i=V_i+x_i(V_{i+1}-V_i),
\qquad
0\le x_i\le1,
\qquad
i=0,\dots,5.
$$

The induced row at $V_i$ is

$$
(a_i,b_i)=(1-x_{i-1},x_i),
$$

with indices modulo $6$.  Hence

$$
a_i+b_i>1
\quad\Longleftrightarrow\quad
x_i>x_{i-1}.
$$

## Theorem 653.1: one-supercritical T3-like CE0 certificate

Assume:

1. $T_C$ is CE0;
2. exactly one row is supercritical:

   $$
   \left\lvert \left\lbrace i : a_i+b_i>1 \right\rbrace \right\rvert=1;
   $$

3. at least one row is T3-like;
4. every non-T3-like row is Vd0;
5. the Vd0-square-loss hypothesis and the T3-envelope hypothesis hold.

Then the six vertex triangles have total normalized outside area strictly larger
than $1$:

$$
\boxed{
\sum_{i=0}^5 G_i>1.
}
$$

Consequently,

$$
\sum_{i=0}^5 (1-G_i)<5.
$$

Thus the six vertex triangles contribute strictly less than five
unit-triangle areas inside $H$.

### Proof

Let $p$ be the unique supercritical index and choose one T3-like index $q$.
By Lemma 652.1, every T3-like row is nonsupercritical.  Hence

$$
q\ne p.
$$

By cyclic symmetry, rotate the indices so that

$$
p=0.
$$

Then

$$
x_0>x_5,
$$

and for every $i=1,\dots,5$,

$$
x_i\le x_{i-1}.
$$

Therefore

$$
x_0\ge x_1\ge x_2\ge x_3\ge x_4\ge x_5.
$$

Set

$$
M=x_0,
\qquad
m=x_5.
$$

Thus $M>m$.

### Reflection normalization

The local loss bounds used here are symmetric in the two row coordinates.  The
Vd0 square-loss hypotheses use only $\min(a,b)$ and $\max(a,b)$, and the T3
local envelope includes both reflected branches.  Therefore the total loss
estimate is invariant under the reflection

$$
y_i=1-x_{-i-1},
$$

where indices are modulo $6$.

Under this reflection, local rows transform as

$$
(1-y_{i-1},y_i)=(x_{-i},1-x_{-i-1}),
$$

which is the corresponding old row with its two coordinates swapped.  The Vd0
and T3-like type assumptions are preserved by reflection.

The minimum and maximum of the reflected sequence are

$$
\min_i y_i=1-M,
\qquad
\max_i y_i=1-m.
$$

Thus, after replacing $x$ by its reflected sequence if necessary, we may assume

$$
\boxed{m\le1-M.}
$$

This replacement preserves the hypotheses and the desired inequality.

Now, for every $i$,

$$
x_i\ge m,
$$

and since $x_{i-1}\le M$,

$$
1-x_{i-1}\ge1-M\ge m.
$$

Hence every row satisfies

$$
\boxed{a_i\ge m,
\qquad
b_i\ge m.}
$$

Since $m\le1-M\le1$, we also have $m\le1/2$.

### Loss of the unique supercritical row

Row $0$ has local data

$$
(a_0,b_0)=(1-x_5,x_0)=(1-m,M).
$$

It is non-T3-like, hence Vd0.  By the supercritical Vd0-square-loss bound,

$$
G_0\ge \max(1-m,M)^2.
$$

The normalization $m\le1-M$ is equivalent to $M\le1-m$, so

$$
\boxed{G_0\ge(1-m)^2.}
$$

### Loss of the selected T3-like row

The selected T3-like row is some $q\in\{1,2,3,4,5\}$.  Since both its row
coordinates are at least $m$, Theorem 652.4 gives

$$
\boxed{G_q\ge2m-4m^2.}
$$

### Loss of the remaining four rows

There are exactly four indices $i$ with

$$
i\ne0,
\qquad
i\ne q.
$$

Each of these rows is nonsupercritical.  If row $i$ is Vd0, then the
subcritical Vd0-square-loss bound gives

$$
G_i\ge \min(a_i,b_i)^2.
$$

Since $a_i,b_i\ge m$,

$$
G_i\ge m^2.
$$

If row $i$ is T3-like, then Corollary 652.5 gives the same bound

$$
G_i\ge m^2.
$$

Therefore

$$
\boxed{
\sum_{\substack{i=0\\ i\ne 0,q}}^5 G_i\ge4m^2.
}
$$

### Summation

Combining the three estimates gives

$$
\sum_{i=0}^5G_i
\ge
(1-m)^2+(2m-4m^2)+4m^2.
$$

Simplifying,

$$
(1-m)^2+(2m-4m^2)+4m^2
=1-2m+m^2+2m
=1+m^2.
$$

Thus

$$
\sum_{i=0}^5G_i\ge1+m^2.
$$

It remains to prove $m>0$.

### Strictness

Assume for contradiction that $m=0$.  Then the unique supercritical row has
local data

$$
(a_0,b_0)=(1,M),
$$

with

$$
M=x_0>x_5=m=0.
$$

Every admissible local vertex row satisfies the necessary quadratic inequality

$$
a^2+ab+b^2\le1.
$$

Applying this to row $0$ gives

$$
1+M+M^2\le1,
$$

which is impossible for $M>0$.  Hence

$$
m>0.
$$

Therefore

$$
\sum_{i=0}^5G_i\ge1+m^2>1.
$$

This proves the theorem.

## Corollary 653.2: CE0 area contradiction

Under the hypotheses of Theorem 653.1, the seven triangles cannot cover $H$.

### Proof

The six vertex triangles contribute normalized inside area

$$
\sum_{i=0}^5(1-G_i)
=6-\sum_{i=0}^5G_i
<5.
$$

The CE0 center triangle contributes at most one normalized unit-triangle area
inside $H$.  Hence all seven triangles contribute less than

$$
5+1=6
$$

normalized unit-triangle areas inside $H$.

The normalized area of the side-$1$ regular hexagon $H$ is $6$.  Therefore the
seven triangles cannot cover $H$.

This proves the corollary.
