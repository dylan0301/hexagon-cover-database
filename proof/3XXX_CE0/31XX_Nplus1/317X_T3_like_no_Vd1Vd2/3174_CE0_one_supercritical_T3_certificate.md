# CE0 One-Supercritical T3-Like Area Certificate

Status: Proven

This file proves the CE0 area contradiction for the case with exactly one
supercritical row and at least one T3-like row.  The proof is unconditional.
It uses:

- the universal local square-loss theorem in
  [`../../32XX_Nplus_ge2/3205_unconditional_local_square_loss.md`](../../32XX_Nplus_ge2/3205_unconditional_local_square_loss.md);
- the direct T3-like area-loss theorem in
  [`3175_direct_T3_like_area_loss.md`](3175_direct_T3_like_area_loss.md).

The failed coordinatewise tangent-envelope conjecture in
[`3172_full_T3_like_tangent_envelope_conjecture.md`](3172_full_T3_like_tangent_envelope_conjecture.md)
is not used.

No midpoint condition is imposed on any T3-like row.

## 1. Proven local inputs

For every local row with boundary data $(a,b)$, normalized outside area $G$
satisfies

$$
G\ge\min(a,b)^2.
$$

If the row is supercritical, then

$$
a+b>1
\quad\Longrightarrow\quad
G\ge\max(a,b)^2.
$$

For every T3-like row:

$$
a+b\le1,
$$

and, for every $0\le m\le1/2$,

$$
a,b\ge m
\quad\Longrightarrow\quad
G\ge2m-4m^2.
$$

## 2. CE0 perimeter model

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

## 3. Main theorem

Assume:

1. $T_C$ is CE0;
2. exactly one row is supercritical:
   $$
   \left\lvert
   \left\lbrace
   i:a_i+b_i>1
   \right\rbrace
   \right\rvert=1;
   $$
3. at least one row is T3-like;
4. every non-T3-like row is Vd0.

Then the six vertex triangles have total normalized outside area strictly
larger than $1$:

$$
\boxed{
\sum_{i=0}^5G_i>1.
}
$$

Consequently, the seven triangles cannot cover $H$.

### Proof

Let $p$ be the unique supercritical index and choose one T3-like index $q$.
Every T3-like row is nonsupercritical, so

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

### 3.1 Reflection normalization

The local loss bounds are symmetric in the two row coordinates.  Reflect the
cut sequence by

$$
y_i=1-x_{-i-1},
$$

with indices modulo $6$.  Then

$$
(1-y_{i-1},y_i)
=
(x_{-i},1-x_{-i-1}),
$$

which is the corresponding old row with its coordinates swapped.  The Vd0 and
T3-like types, the number of supercritical rows, and the total area estimate
are preserved.

The reflected sequence has minimum $1-M$ and maximum $1-m$.  Hence, after
reflection if necessary, we may assume

$$
\boxed{m\le1-M.}
$$

For every $i$,

$$
x_i\ge m,
$$

and

$$
1-x_{i-1}\ge1-M\ge m.
$$

Thus every row satisfies

$$
\boxed{
a_i\ge m,
\qquad
b_i\ge m.
}
$$

Also $m\le1-M\le1-m$, so $m\le1/2$.

### 3.2 Unique supercritical row

Row $0$ has data

$$
(a_0,b_0)=(1-x_5,x_0)=(1-m,M).
$$

The supercritical square-loss theorem gives

$$
G_0\ge\max(1-m,M)^2.
$$

The normalization $m\le1-M$ is equivalent to $M\le1-m$.  Therefore

$$
\boxed{G_0\ge(1-m)^2.}
$$

### 3.3 Selected T3-like row

Both coordinates of row $q$ are at least $m$.  The direct T3-like area-loss
theorem gives

$$
\boxed{G_q\ge2m-4m^2.}
$$

### 3.4 Remaining four rows

For every remaining index $i\ne0,q$, both row coordinates are at least $m$.
The universal minimum-square theorem gives

$$
G_i\ge\min(a_i,b_i)^2\ge m^2.
$$

Hence

$$
\boxed{
\sum_{\substack{i=0\\ i\ne0,q}}^5G_i\ge4m^2.
}
$$

### 3.5 Summation

Combining the three estimates,

$$
\begin{aligned}
\sum_{i=0}^5G_i
&\ge
(1-m)^2+(2m-4m^2)+4m^2
\\
&=
1+m^2.
\end{aligned}
$$

It remains to prove $m>0$.

Assume for contradiction that $m=0$.  Then row $0$ has data

$$
(a_0,b_0)=(1,M),
$$

with $M>0$.  The two required boundary points of a unit equilateral triangle
must be at mutual distance at most $1$.  Their squared distance is

$$
a_0^2+a_0b_0+b_0^2
=
1+M+M^2>1,
$$

a contradiction.  Therefore

$$
m>0.
$$

Consequently,

$$
\sum_{i=0}^5G_i
\ge1+m^2
>1.
$$

This proves the theorem.

## 4. Area contradiction

The six vertex triangles contribute normalized inside area

$$
\sum_{i=0}^5(1-G_i)
=
6-\sum_{i=0}^5G_i
<5.
$$

The CE0 center triangle contributes at most one normalized unit-triangle area.
Thus all seven triangles contribute total normalized inside area less than

$$
5+1=6.
$$

The normalized area of the side-$1$ regular hexagon is $6$.  Therefore the
seven triangles cannot cover $H$.
