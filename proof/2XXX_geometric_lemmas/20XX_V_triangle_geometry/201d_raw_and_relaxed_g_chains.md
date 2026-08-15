# Canonical and Relaxed $g$-Composition Chains

Status: Proven

This note fixes one notation for every Strategy 2 transfer.  The historical
map $g_c$ remains in its original **boundary-defect coordinate**, and a
superscript $\vee$ changes to the complementary incoming-reach coordinate used
by the paper.  Nonsupercriticality is imposed directly in two radial branches;
there is no second transfer family.

- If the selected radial demand satisfies $c\le1/2$, use the direct inequality
  $B\le1-A$.
- If $c>1/2$, the raw map already lies below the diagonal and gives the exact
  nonsupercritical output bound.

Center intervals, the free strict-supercritical envelope, affine selected-
$T_+$ bounds, and threshold bounds are decorations of this single raw
$g$-family.

## 1. Local demand coordinates

Let $\mathcal A\subseteq[0,1]^3$ be the exact local admissible set from
[`2004`](2004_admissible_set.md).  A triple $(a,b,c)\in\mathcal A$ means that
one closed unit equilateral triangle can realize

- incoming boundary demand $a$;
- outgoing boundary demand $b$;
- own-radial demand $c$.

The coordinates are lower-bound demands.  If an actual V triangle has maximal
reaches $(A,B,C)$, then it realizes every triple with

$$
0\le a\le A,
\qquad
0\le b\le B,
\qquad
0\le c\le C.
$$

For an incoming reach $a$, write

$$
x=1-a.
$$

The variable $x$ is the incoming boundary **defect**.

## 2. The raw defect map and midpoint threshold

For $0\le x,c\le1$, define

$$
\boxed{
g_c(x)
=
\max\left\{
y\in[0,1]:(1-x,y,c)\in\mathcal A
\right\}.
}
$$

Thus $g_c(x)$ is the largest outgoing reach compatible with incoming defect
$x$ and radial demand $c$.  In the notation of
[`2007`](2007_max_b_map.md),

$$
\boxed{g_c(x)=B_c(1-x).}
$$

Because $\mathcal A$ is coordinatewise down-closed, $g_c$ is nondecreasing in
$x$ and nonincreasing in $c$.

The radial midpoint gives the exact diagonal threshold:

$$
\boxed{
 c\ge\frac12
 \quad\Longrightarrow\quad
 g_c(x)\le x,
 \qquad
 g_{1/2}(x)=x.
}
$$

### Proof

If $(1-x,y,c)\in\mathcal A$ and $c\ge1/2$, the realizing triangle contains
the radial midpoint $(u+v)/2$.  The midpoint self-cover theorem
[`2005`](2005_midpoint_self_cover_lemma.md) gives

$$
(1-x)+y\le1,
$$

so $y\le x$.

For the reverse inequality at $c=1/2$, put $a=1-x$ and $b=x$.  In the exact
Cell-$T$ description of `2004`,

$$
s=a+b=1,
\qquad
 d=a^2+ab+b^2\le1,
\qquad
 q=ab\ge0.
$$

With $M=\max\{a,b\}\ge1/2$,

$$
F_T(a,b,1/2)=M(1/2-M)\le0,
\qquad
1/2\le2M.
$$

Hence $(a,b,1/2)\in\mathcal A$, proving $g_{1/2}(x)\ge x$.  The preceding
upper bound gives equality.

## 3. Complement duals and technical aliases

For any map $f:[0,1]\to[0,1]$, define

$$
\boxed{f^\vee(a)=1-f(1-a).}
$$

The involution $a\mapsto1-a$ conjugates an outgoing upper bound in defect
coordinates to a following incoming lower bound.  In particular,

$$
g_c^\vee(a)=1-g_c(1-a).
$$

For $c\ge1/2$, the midpoint threshold gives

$$
\boxed{g_c^\vee(a)\ge a.}
$$

Older exact contact-cell files may retain the aliases

$$
\boxed{
B_c(a)=g_c(1-a),
\qquad
F_c(a)=
\begin{cases}
1-a,&c\le1/2,\\
B_c(a),&c>1/2,
\end{cases}
\qquad
G_c(a)=1-F_c(a).
}
$$

The exact branchwise identity

$$
F_c(a)=\min\{B_c(a),1-a\}
$$

is proved in [`2011`](2011_capped_demand_map.md).  These are technical aliases,
not a second transfer family.

## 4. Actual-V triangle transfer

Let an actual V triangle have maximal reaches $(A,B,C)$ and suppose

$$
A\ge a,
\qquad
C\ge c.
$$

Then $(a,B,c)\in\mathcal A$, so

$$
\boxed{B\le g_c(1-a).}
$$

If no center interval intervenes on the next boundary edge, coverage gives

$$
A_{\rm next}\ge1-B,
$$

and therefore

$$
\boxed{A_{\rm next}\ge g_c^\vee(a).}
$$

This raw statement is valid for every V triangle.

Now assume that the actual V triangle is nonsupercritical:

$$
A+B\le1.
$$

Then

$$
B\le1-A\le1-a.
$$

Combining this direct bound with the midpoint threshold gives the exact
branchwise form

$$
\boxed{
B\le
\begin{cases}
1-a,&0\le c\le1/2,\\
g_c(1-a),&1/2<c\le1.
\end{cases}
}
$$

On a center-free next edge,

$$
\boxed{
A_{\rm next}\ge
\begin{cases}
a,&0\le c\le1/2,\\
g_c^\vee(a)\ge a,&1/2<c\le1.
\end{cases}
}
$$

Thus the low-radial identity propagation is just $B\le1-A$, while the
high-radial propagation is the raw $g_c^\vee$ transfer.

## 5. The zero-radial warning

At $c=0$, the exact diameter formula is

$$
B_0(a)=\frac{-a+\sqrt{4-3a^2}}2,
$$

so

$$
g_0(x)
=
\frac{x-1+\sqrt{1+6x-3x^2}}2.
$$

For $0<x<1$,

$$
1+6x-3x^2-(1+x)^2=4x(1-x)>0,
$$

and hence

$$
\boxed{g_0(x)>x.}
$$

Taking complement duals gives

$$
g_0^\vee(a)<a
\qquad(0<a<1).
$$

Therefore the raw zero-radial map must not be used for a nonsupercritical
identity handoff.  The correct argument is the direct inequality
$B\le1-A$.

## 6. Center-assisted transfers

Let $\mathcal R_J$ be the residual-demand operator of
[`2019`](2019_interval_component_and_path_budget.md), where $J$ is empty or a
closed center interval.  Define only the raw center-assisted transfer

$$
\boxed{
g_{c,J}^\vee(a)
=
\mathcal R_J\!\left(g_c(1-a)\right).
}
$$

The edge-handoff lemma and monotonicity of $\mathcal R_J$ give

$$
A_{\rm next}\ge g_{c,J}^\vee(a)
$$

for every V triangle.  If the triangle is nonsupercritical, the sharper
branchwise statement is

$$
\boxed{
A_{\rm next}\ge
\begin{cases}
\mathcal R_J(1-a),&0\le c\le1/2,\\
g_{c,J}^\vee(a),&1/2<c\le1.
\end{cases}
}
$$

Since $\mathcal R_\varnothing(p)=1-p$, this reduces to the center-free
branchwise transfer above.

## 7. The free strict-supercritical envelope

For fixed $0\le c<1/2$, the strict-supercritical defect region is

$$
\{x:g_c(x)>x\}.
$$

Indeed, with incoming reach $1-x$, strict supercriticality is equivalent to
$b>x$.  The interval-fiber property permits such a $b$ exactly when
$g_c(x)>x$.

Define

$$
\boxed{
g_c^{\rm sc}
=
\sup_{\substack{0\le x\le1\\g_c(x)>x}}g_c(x).
}
$$

The free strict-supercritical theorem
[`2010`](2010_free_supercritical_max_b.md) gives

$$
\boxed{
g_c^{\rm sc}
=
\frac{c+\sqrt{c^2-8c+4}}2,
\qquad
0\le c<\frac12.
}
$$

The supremum is not attained.  Hence every actual strict-supercritical
V triangle with radial demand at least $c$ satisfies

$$
\boxed{B<g_c^{\rm sc}.}
$$

On a center-free next edge,

$$
\boxed{A_{\rm next}>1-g_c^{\rm sc}.}
$$

The historical aliases are

$$
B_{\rm sc}(c)=g_c^{\rm sc},
\qquad
A_{\rm sc}(c)=1-g_c^{\rm sc}.
$$

## 8. Composition and lower relaxations

For maps listed in geometric V-triangle order, write

$$
\boxed{
[\Phi_1\mid\cdots\mid\Phi_r](x)
=
(\Phi_r\circ\cdots\circ\Phi_1)(x).
}
$$

The leftmost slot acts first.  Write $\mathrm I^k$ for $k$ consecutive
identity slots.

### Relaxed-composition lemma

Suppose actual incoming demands satisfy

$$
x_j\ge\Phi_j(x_{j-1})
\qquad(1\le j\le r),
$$

where every $\Phi_j$ is nondecreasing.  If

$$
\underline\Phi_j\le\Phi_j,
$$

then

$$
\boxed{
x_r
\ge
[\underline\Phi_1\mid\cdots\mid\underline\Phi_r](x_0).
}
$$

#### Proof

Put

$$
y_0=x_0,
\qquad
y_j=\underline\Phi_j(y_{j-1}).
$$

If $x_{j-1}\ge y_{j-1}$, monotonicity gives

$$
x_j
\ge
\Phi_j(x_{j-1})
\ge
\Phi_j(y_{j-1})
\ge
\underline\Phi_j(y_{j-1})
=
y_j.
$$

Induction proves the claim.

## 9. Decorated high-radial lower relaxations

The reusable affine and threshold relaxations occur only for
$c=1-d>1/2$, so they are decorations of the raw transfer $g_{1-d}^\vee$.

### Affine selected-$T_+$ relaxation

On a selected-$T_+$ arc on which the coefficient $\lambda$ has been proved
valid, write

$$
\boxed{
g_{1-d}^{\vee,\lambda}(x)
=
x+\lambda(x-d)
\le
g_{1-d}^\vee(x).
}
$$

The CE1 one-gap proof sets $m_3=d_3^C$ and uses

$$
g_{1-\alpha}^{\vee,\,1-4\alpha},
\qquad
g_{1-m_3}^{\vee,\,1-5m_3}.
$$

The superscript $\lambda$ denotes a certified lower relaxation, not an
additional exact map.

### Threshold relaxation

For $0<d<1-\sqrt3/2$, let $e(d)$ be the low-root threshold from
[`2012`](2012_high_radial_low_root_bounds.md).  Define

$$
\boxed{
g_{1-d}^{\vee,\rm th}(x)
=
\begin{cases}
x,&x\le e(d),\\
1-e(d),&x>e(d).
\end{cases}
}
$$

The high-demand threshold gives

$$
\boxed{
g_{1-d}^{\vee,\rm th}
\le
g_{1-d}^\vee.
}
$$

Quarter-radial and Vd-corner estimates play the same role at terminal slots:
they replace an exact V-triangle transfer by a simpler branch-specific lower
bound.  The branch tables state those terminal bounds directly rather than
assigning another permanent function letter.

## 10. Full six-V-triangle branch register

For each $i\in\mathbb Z/6\mathbb Z$, parametrize the outgoing edge by

$$
\xi_i(t)=V_i+t(V_{i+1}-V_i),
\qquad 0\le t\le1,
$$

and let

$$
J_i^C=\xi_i^{-1}(T_C\cap e_{i,i+1})
$$

be the empty or closed scalar center interval.  Point contacts are retained as
degenerate intervals.

Each slot is recorded directly:

- for an arbitrary or supercritical role, use the raw transfer
  $g_{c_i,J_i^C}^\vee$;
- for a nonsupercritical role with $c_i\le1/2$, use
  $a\mapsto\mathcal R_{J_i^C}(1-a)$;
- for a nonsupercritical role with $c_i>1/2$, use the same raw transfer
  $g_{c_i,J_i^C}^\vee$.

The complete branch word is displayed in geometric V-triangle order,

$$
[\Phi_0\mid\Phi_1\mid\Phi_2\mid\Phi_3\mid\Phi_4\mid\Phi_5]
=
\Phi_5\circ\Phi_4\circ\Phi_3\circ\Phi_2\circ\Phi_1\circ\Phi_0,
$$

with each $\Phi_i$ chosen by the preceding branch rule.  The branch
proposition determines whether this word is used cyclically, cut at a center
trace and replaced by endpoint inequalities, or truncated to the exact
five-V-triangle subchain followed by a terminal cap.

An identity slot records a weaker individual handoff.  It is licensed only
when the handoff edge is center-free, every nonincident role has zero-length
trace there, and the current role is nonsupercritical.  In the low-radial
branch it follows directly from $B\le1-A$; in the high-radial branch it follows
from $g_c^\vee\ge\mathrm I$.  Thus the slot says only

$$
A_{i+1}\ge A_i.
$$

For the $N_+=1$ all-Vd0 one-gap branch, the five ordinary roles have radial
demands strictly above $1/2$.  Its exact subchain is therefore

$$
[g_{c_1}^\vee\mid g_{c_2}^\vee\mid g_{c_3}^\vee
 \mid g_{c_4}^\vee\mid g_{c_5}^\vee],
$$

and the remaining supercritical role is closed by its independent terminal
diameter cap.  This is the same proved certificate with the unnecessary second
transfer notation removed.
