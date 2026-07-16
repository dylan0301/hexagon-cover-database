# CE0 Six-Point Area Certificate

Status: Proven

This file proves the CE0 six-point area inequality from the two local
square-loss bounds for the area function $f(a,b)$ defined in
[`3202_area_function_and_monotonicity.md`](3202_area_function_and_monotonicity.md).

Those local bounds are proved unconditionally in
[`3205_unconditional_local_square_loss.md`](3205_unconditional_local_square_loss.md).
Therefore the CE0 conclusion in this file is unconditional.

The passage from actual maximal reaches to simultaneous selected demands is
proved in the strict boundary-handoff theorem
[`../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md`](../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md).

## 1. Proven local square-loss input

For every local vertex row,

$$
f(a,b)\le1-\min(a,b)^2.
$$

If the row is supercritical, then

$$
a+b>1
\quad\Longrightarrow\quad
f(a,b)\le1-\max(a,b)^2.
$$

Equivalently, with

$$
g(a,b)=1-f(a,b),
$$

the normalized local area loss satisfies

$$
g(a,b)\ge\min(a,b)^2
$$

for every feasible row, and

$$
a+b>1
\quad\Longrightarrow\quad
g(a,b)\ge\max(a,b)^2.
$$

## 2. CE0 strict handoff selection

Let $T_C$ be CE0, and let $A_i,B_i$ be the actual maximal incoming and
outgoing reaches of the vertex triangle $T_i$.  The CE0 condition implies
that the six vertex roles cover $\partial H$: otherwise a boundary point
covered only by the open triangle $T_C$ would give a positive-length edge
interval in $T_C$.

Suppose the actual supercritical count satisfies

$$
\left\lvert
\left\lbrace i:A_i+B_i>1\right\rbrace
\right\rvert\ge2.
$$

The at-least-two theorem in `1214` supplies one cut point on each boundary
edge,

$$
X_i=V_i+x_i(V_{i+1}-V_i),
\qquad
i=0,\dots,5,
$$

with indices modulo $6$.  The selected lower-bound demands at $V_i$ are

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

They satisfy

$$
0<a_i<A_i,
\qquad
0<b_i<B_i,
$$

and the closure of the actual triangle $T_i$ contains both selected edge
anchors.  Thus that closure is feasible for the local function $f(a_i,b_i)$,
and the normalized inside area of the actual role is at most $f(a_i,b_i)$.

For selected rows,

$$
a_i+b_i=1-x_{i-1}+x_i,
$$

so

$$
a_i+b_i>1
\quad\Longleftrightarrow\quad
x_i>x_{i-1}.
$$

The choice guaranteed by `1214` has at least two such strict ascents.

## 3. Six-row theorem

Let

$$
x_0,\dots,x_5\in[0,1]
$$

and set

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

Assume every pair $(a_i,b_i)$ is feasible for a unit equilateral vertex
triangle.

If at least two rows are supercritical, that is,

$$
\left\lvert
\left\lbrace
i:a_i+b_i>1
\right\rbrace
\right\rvert
\ge2,
$$

then

$$
\boxed{
\sum_{i=0}^5 f(a_i,b_i)<\frac{99}{20}<5.
}
$$

### Proof

Define

$$
G_i=1-f(1-x_{i-1},x_i).
$$

It is enough to prove

$$
\sum_{i=0}^5G_i>\frac{21}{20},
$$

because then

$$
\sum_{i=0}^5 f(1-x_{i-1},x_i)
=
6-\sum_{i=0}^5G_i
<
6-\frac{21}{20}
=
\frac{99}{20}.
$$

If

$$
x_i\le x_{i-1},
$$

then the row is nonsupercritical and the minimum-square bound gives

$$
G_i\ge\min(1-x_{i-1},x_i)^2.
$$

If

$$
x_i>x_{i-1},
$$

then the row is supercritical and the maximum-square bound gives

$$
G_i\ge\max(1-x_{i-1},x_i)^2.
$$

Set

$$
m=\min_i x_i,
\qquad
M=\max_i x_i.
$$

The local function is symmetric:

$$
f(a,b)=f(b,a).
$$

Reflect the cut sequence by

$$
y_i=1-x_{-i-1},
$$

with indices modulo $6$.  Then

$$
\min_i y_i=1-M,
\qquad
\max_i y_i=1-m,
$$

and

$$
y_i>y_{i-1}
\quad\Longleftrightarrow\quad
x_{-i}>x_{-i-1}.
$$

Thus the number of supercritical rows is unchanged.  Moreover,

$$
(1-y_{i-1},y_i)
=
(x_{-i},1-x_{-i-1}),
$$

which is the corresponding old row with its coordinates swapped.  Hence the
sum of the six local area values is preserved.

After replacing $x$ by its reflected sequence if necessary, assume

$$
m\le1-M.
$$

For every $i$,

$$
x_i\ge m
$$

and

$$
1-x_{i-1}\ge1-M\ge m.
$$

Thus both entries of every row are at least $m$, and the local bounds imply

$$
G_i\ge m^2
\qquad
\text{for all }i.
$$

Because the cyclic sequence is not constant, some minimum plateau is exited.
There is an index $p$ such that

$$
x_{p-1}=m,
\qquad
x_p>m.
$$

For this supercritical row,

$$
G_p
\ge
\max(1-x_{p-1},x_p)^2
\ge
(1-m)^2.
$$

By hypothesis there is another strict ascent.  Choose $q\ne p$ with

$$
x_q>x_{q-1}.
$$

Then

$$
(1-x_{q-1})+x_q
=
1+(x_q-x_{q-1})
>1.
$$

Therefore

$$
\max(1-x_{q-1},x_q)>\frac12,
$$

and hence

$$
G_q>\frac14.
$$

The remaining four rows satisfy $G_i\ge m^2$.  Consequently,

$$
\sum_{i=0}^5G_i
>
4m^2+(1-m)^2+\frac14.
$$

Finally,

$$
\begin{aligned}
4m^2+(1-m)^2+\frac14
&=
5m^2-2m+\frac54
\\
&=
5\left(m-\frac15\right)^2+\frac{21}{20}
\\
&\ge
\frac{21}{20}.
\end{aligned}
$$

Thus

$$
\sum_{i=0}^5G_i>\frac{21}{20},
$$

which proves

$$
\sum_{i=0}^5 f(a_i,b_i)<\frac{99}{20}<5.
$$

## 4. CE0 area contradiction

If $T_C$ is CE0 and at least two actual vertex rows are supercritical, apply
the strict handoff selection from Section 2.  The selected sequence has at
least two strict ascents, so the six-row theorem applies.  Since each actual
vertex triangle is feasible for its selected pair, the six vertex triangles
contribute less than $99/20$ normalized unit-triangle areas inside $H$.

The center triangle contributes at most one normalized unit-triangle area.
Hence all seven triangles contribute less than

$$
\frac{99}{20}+1
=
\frac{119}{20}
<6.
$$

The normalized area of the side-$1$ regular hexagon is $6$.  Therefore such a
CE0 configuration cannot cover $H$.
