# CE0 Conditional Area Certificate

Status: Proven analytic inequality

This file proves the final CE0 six-point area inequality under explicit local
square-loss upper bounds for the area function `f(a,b)` from
[`3202_area_function_and_monotonicity.md`](3202_area_function_and_monotonicity.md).

It does **not** prove those local upper bounds.  The local bounds remain a
separate proof obligation, recorded in
[`3207_current_status.md`](3207_current_status.md).

## Local square-loss hypothesis

Assume the following two pointwise bounds for all local vertex rows under
consideration:

1. If

   $$
   a+b\le 1,
   $$

   then

   $$
   f(a,b)\le 1-\min(a,b)^2.
   $$

2. If

   $$
   a+b>1,
   $$

   then

   $$
   f(a,b)\le 1-\max(a,b)^2.
   $$

Equivalently, with

$$
g(a,b)=1-f(a,b),
$$

the forced normalized local area loss satisfies

$$
a+b\le1 \quad\Longrightarrow\quad g(a,b)\ge\min(a,b)^2,
$$

and

$$
a+b>1 \quad\Longrightarrow\quad g(a,b)\ge\max(a,b)^2.
$$

The proof below uses only the square-loss hypothesis and the CE0 six-point row
formulas.

## CE0 six-point notation

Use the CE0 six-point perimeter model from
[`3203_CE0_six_point_main_target.md`](3203_CE0_six_point_main_target.md).
Thus one cut point is chosen on each edge:

$$
X_i=V_i+x_i(V_{i+1}-V_i), \qquad 0\le x_i\le1, \qquad i=0,\dots,5,
$$

with indices modulo $6$.

The induced local row at $V_i$ is

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

Therefore

$$
a_i+b_i=1-x_{i-1}+x_i,
$$

so

$$
a_i+b_i>1 \quad\Longleftrightarrow\quad x_i>x_{i-1}.
$$

## Theorem 647.1: conditional CE0 area certificate

Assume the local square-loss hypothesis above.  Let

$$
x_0,\dots,x_5\in[0,1]
$$

and set

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

If at least two rows are supercritical, i.e.

$$
\left\lvert \left\lbrace\, i : a_i+b_i>1 \,\right\rbrace \right\rvert\ge2,
$$

then

$$
\sum_{i=0}^5 f(a_i,b_i)<\frac{99}{20}<5.
$$

Equivalently,

$$
\sum_{i=0}^5 f(1-x_{i-1},x_i)<\frac{99}{20}<5.
$$

## Proof

Define the row losses

$$
G_i=1-f(1-x_{i-1},x_i).
$$

It is enough to prove

$$
\sum_{i=0}^5G_i>\frac{21}{20},
$$

because then

$$
\sum_{i=0}^5 f(1-x_{i-1},x_i) =6-\sum_{i=0}^5G_i <6-\frac{21}{20} =\frac{99}{20}.
$$

For each $i$, there are two cases.

If

$$
x_i\le x_{i-1},
$$

then

$$
1-x_{i-1}+x_i\le1,
$$

so the subcritical square-loss bound gives

$$
G_i\ge\min(1-x_{i-1},x_i)^2.
$$

If

$$
x_i>x_{i-1},
$$

then

$$
1-x_{i-1}+x_i>1,
$$

so the supercritical square-loss bound gives

$$
G_i\ge\max(1-x_{i-1},x_i)^2.
$$

Now set

$$
m=\min_i x_i, \qquad M=\max_i x_i.
$$

The local function is symmetric:

$$
f(a,b)=f(b,a),
$$

because reflecting the hexagon through the symmetry axis through a vertex swaps
the incoming and outgoing boundary sides.

Use this symmetry to normalize the cut sequence.  Define

$$
y_i=1-x_{-i-1},
$$

with indices modulo $6$.  Then

$$
\min_i y_i=1-M, \qquad \max_i y_i=1-m.
$$

Also,

$$
y_i>y_{i-1} \quad\Longleftrightarrow\quad x_{-i}>x_{-i-1},
$$

so the number of supercritical rows is unchanged.  Moreover,

$$
(1-y_{i-1},y_i)=(x_{-i},1-x_{-i-1}),
$$

which is the corresponding old row with the two coordinates swapped.  Since
$f(a,b)=f(b,a)$,

$$
\sum_{i=0}^5 f(1-y_{i-1},y_i) = \sum_{i=0}^5 f(1-x_{i-1},x_i).
$$

Therefore, after replacing $x$ by $y$ if necessary, we may assume

$$
m\le1-M.
$$

Under this normalization, for every $i$,

$$
x_i\ge m
$$

and

$$
1-x_{i-1}\ge1-M\ge m.
$$

Thus both entries of every row are at least $m$.  From the two loss estimates
above, this implies the baseline bound

$$
G_i\ge m^2 \qquad\text{for all }i.
$$

Because there is at least one strict ascent $x_i>x_{i-1}$, the cyclic sequence is
not constant.  Hence some minimum plateau is exited: there is an index $p$ such
that

$$
x_{p-1}=m, \qquad x_p>m.
$$

For this row $p$,

$$
G_p\ge\max(1-x_{p-1},x_p)^2.
$$

Since $x_{p-1}=m$,

$$
G_p\ge(1-m)^2.
$$

By hypothesis, there is another strict ascent.  Choose $q\ne p$ with

$$
x_q>x_{q-1}.
$$

Then

$$
(1-x_{q-1})+x_q =1+(x_q-x_{q-1}) >1.
$$

Therefore

$$
\max(1-x_{q-1},x_q)>\frac12.
$$

Since row $q$ is supercritical,

$$
G_q\ge\max(1-x_{q-1},x_q)^2>\frac14.
$$

The remaining four rows still satisfy $G_i\ge m^2$.  Hence

$$
\sum_{i=0}^5G_i > 4m^2+(1-m)^2+\frac14.
$$

Finally,

$$
4m^2+(1-m)^2+\frac14 =5m^2-2m+\frac54 =5\left(m-\frac15\right)^2+\frac{21}{20} \ge\frac{21}{20}.
$$

Thus

$$
\sum_{i=0}^5G_i>\frac{21}{20},
$$

and therefore

$$
\sum_{i=0}^5 f(1-x_{i-1},x_i)<\frac{99}{20}<5.
$$

This proves the theorem.

## Corollary 647.2: conditional CE0 area contradiction

Assume the local square-loss hypothesis and the CE0 six-point model.  If at
least two CE0 rows satisfy $a_i+b_i>1$, then the six vertex triangles contribute
less than $99/20$ unit-triangle areas inside $H$.

The center triangle contributes at most one unit-triangle area.  Hence the seven
unit triangles contribute less than

$$
\frac{99}{20}+1=\frac{119}{20}<6.
$$

Since the normalized area of $H$ is $6$, such a CE0 configuration cannot cover
$H$.

## Dependencies and non-claims

This file depends on:

- the definition of $f(a,b)$ in
  [`3202_area_function_and_monotonicity.md`](3202_area_function_and_monotonicity.md);
- the CE0 row formulas in
  [`3203_CE0_six_point_main_target.md`](3203_CE0_six_point_main_target.md);
- the local square-loss hypothesis stated above.

This file does not prove:

- the local square-loss hypothesis;
- the structural conjecture for local maximizers $T(a,b)$.
