# Canonical and Relaxed $g$-Composition Chains

Status: Proven

This note fixes one notation for every Strategy 2 transfer.  The historical
map $g_c$ is kept in its original **boundary-defect coordinate**.  A hat
imposes the nonsupercritical diagonal cap, and a superscript $\vee$ changes
from defect coordinates to the complementary incoming-reach coordinates used
by the paper.  Center intervals, the free strict-supercritical envelope,
affine selected-$T_+$ bounds, and threshold bounds are decorations of this
single $g$-family.

No distinction between supercritical and nonsupercritical V triangles is built into
the definition of the raw map $g_c$.

## 1. Local demand coordinates

Let $\mathcal A\subseteq[0,1]^3$ be the exact local admissible set from
[`2004`](2004_admissible_set.md).  A triple $(a,b,c)\in\mathcal A$ means that
one closed unit equilateral triangle can realize

- incoming boundary demand $a$;
- outgoing boundary demand $b$;
- own-radial demand $c$.

The coordinates are lower-bound demands.  If an actual V triangle has maximal reaches
$(A,B,C)$, then it realizes every triple with

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

## 2. Raw and capped defect maps

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

Because the admissible set is coordinatewise down-closed, $g_c$ is
nondecreasing in $x$ and nonincreasing in $c$.

For a nonsupercritical V triangle the outgoing reach is also at most its incoming
defect.  Define the capped defect map

$$
\boxed{
\widehat g_c(x)=\min\{g_c(x),x\}.
}
$$

Hence

$$
\widehat g_c(x)\le x.
$$

The hat is the only notation used for the nonsupercritical cap.

## 3. Complement duals

For any map $f:[0,1]\to[0,1]$, define its complement dual by

$$
\boxed{
f^\vee(a)=1-f(1-a).
}
$$

The involution $a\mapsto1-a$ conjugates defect-coordinate upper bounds to
incoming-reach lower bounds.  In particular,

$$
g_c^\vee(a)=1-g_c(1-a),
$$

and

$$
\widehat g_c^\vee(a)=1-\widehat g_c(1-a).
$$

Since $\widehat g_c\le\mathrm I$,

$$
\boxed{\widehat g_c^\vee\ge\mathrm I.}
$$

The symbols used in older exact files are aliases:

$$
\boxed{
B_c(a)=g_c(1-a),
\qquad
F_c(a)=\widehat g_c(1-a),
\qquad
G_c(a)=\widehat g_c^\vee(a).
}
$$

Thus $B_c,F_c,G_c$ are not a second family of maps.  They are the outgoing,
capped-outgoing, and capped-dual views of the same $g$-family.  Exact
contact-cell files may retain these aliases when that keeps their formulas
short.

## 4. Actual-V triangle transfer

Let an actual V triangle have maximal reaches $(A,B,C)$.

### Raw V triangle

Suppose

$$
A\ge a,
\qquad
C\ge c.
$$

Then $(a,B,c)\in\mathcal A$, and therefore

$$
B\le g_c(1-a).
$$

If no center interval intervenes on the next boundary edge, coverage gives

$$
A_{\rm next}\ge1-B.
$$

Consequently

$$
\boxed{
A_{\rm next}\ge g_c^\vee(a).
}
$$

This statement is valid for every V triangle.

Equivalently, if $x=1-a$ and $x_{\rm next}=1-A_{\rm next}$, then

$$
\boxed{
x_{\rm next}\le g_c(x).
}
$$

### Nonsupercritical V triangle

If the V triangle is nonsupercritical, then

$$
A+B\le1.
$$

The preceding hypotheses give

$$
B\le1-A\le1-a,
$$

and hence

$$
B\le\widehat g_c(1-a).
$$

Therefore

$$
\boxed{
A_{\rm next}\ge\widehat g_c^\vee(a)\ge a.
}
$$

Equivalently,

$$
\boxed{
x_{\rm next}\le\widehat g_c(x)\le x.
}
$$

The increasing reach chain and the decreasing defect chain are the same
argument in complementary coordinates.

## 5. The zero-radial map

At $c=0$, the exact diameter formula is

$$
B_0(a)=\frac{-a+\sqrt{4-3a^2}}2.
$$

Thus

$$
\boxed{
g_0(x)
=
B_0(1-x)
=
\frac{x-1+\sqrt{1+6x-3x^2}}2.
}
$$

For $0<x<1$,

$$
1+6x-3x^2-(1+x)^2
=
4x(1-x)>0,
$$

so

$$
\boxed{g_0(x)>x.}
$$

Geometrically, the two demanded boundary points are at distance one and form
two vertices of the extremal unit equilateral triangle.  The extremal demand is
strictly supercritical:

$$
(1-x)+g_0(x)>1.
$$

After imposing the nonsupercritical cap,

$$
\boxed{\widehat g_0(x)=x.}
$$

Taking complement duals gives

$$
g_0^\vee(a)<a
\quad(0<a<1),
\qquad
\boxed{\widehat g_0^\vee(a)=a.}
$$

This is the precise resolution of the former notation conflict: the raw
historical $g_0$ lies above the diagonal, while its hatted nonsupercritical
version is the identity.

## 6. Center-assisted transfers

Let $\mathcal R_J$ be the residual-demand operator of
[`2019`](2019_interval_component_and_path_budget.md), where $J$ is empty or a
closed center interval.  Define

$$
\boxed{
g_{c,J}^\vee(a)
=
\mathcal R_J\!\left(g_c(1-a)\right),
}
$$

and

$$
\boxed{
\widehat g_{c,J}^\vee(a)
=
\mathcal R_J\!\left(\widehat g_c(1-a)\right).
}
$$

The edge-handoff lemma and monotonicity of $\mathcal R_J$ give

$$
A_{\rm next}\ge g_{c,J}^\vee(a)
$$

for every V triangle, and

$$
A_{\rm next}\ge\widehat g_{c,J}^\vee(a)
$$

when the V triangle is nonsupercritical.  Since
$\mathcal R_{\varnothing}(p)=1-p$,

$$
g_{c,\varnothing}^\vee=g_c^\vee,
\qquad
\widehat g_{c,\varnothing}^\vee=\widehat g_c^\vee.
$$

No additional alphabet is needed for center-assisted propagation.

## 7. The free strict-supercritical envelope

For fixed $0\le c<1/2$, the strict-supercritical defect region is

$$
\left\{x:g_c(x)>x\right\}.
$$

Indeed, with incoming reach $1-x$, strict supercriticality is

$$
(1-x)+b>1
\quad\Longleftrightarrow\quad
b>x.
$$

The interval-fiber property permits such a $b$ exactly when
$g_c(x)>x$.

Define the single scalar envelope

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

The supremum is not attained.  Hence every actual strict-supercritical V triangle
with radial demand at least $c$ satisfies

$$
\boxed{B<g_c^{\rm sc}.}
$$

On a center-free next edge,

$$
\boxed{
A_{\rm next}>1-g_c^{\rm sc}.
}
$$

The old two-symbol notation is only the alias

$$
B_{\rm sc}(c)=g_c^{\rm sc},
\qquad
A_{\rm sc}(c)=1-g_c^{\rm sc}.
$$

Reader-facing arguments should use the single scalar $g_c^{\rm sc}$ and its
complement instead of introducing both $A_{\rm sc}$ and $B_{\rm sc}$.

## 8. Composition and lower relaxations

For maps listed in geometric V-triangle order, write

$$
\boxed{
[\Phi_1\mid\cdots\mid\Phi_r](x)
=
(\Phi_r\circ\cdots\circ\Phi_1)(x).
}
$$

Thus the leftmost slot acts first.  Write $\mathrm I^k$ for $k$ consecutive
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

If $x_{j-1}\ge y_{j-1}$, then monotonicity gives

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

## 9. Decorated lower relaxations

The exact nonsupercritical reach transfer is
$\widehat g_{1-d}^\vee$.  To avoid new function letters, its two reusable lower
relaxations are denoted by superscripts.

### Affine selected-$T_+$ relaxation

On a selected-$T_+$ arc on which the coefficient $\lambda$ has been proved
valid, write

$$
\boxed{
\widehat g_{1-d}^{\vee,\lambda}(x)
=
x+\lambda(x-d)
\le
\widehat g_{1-d}^\vee(x).
}
$$

The CE1 one-gap proof sets $m_3:=d_3^C$ and uses

$$
\widehat g_{1-\alpha}^{\vee,\,1-4\alpha},
\qquad
\widehat g_{1-m_3}^{\vee,\,1-5m_3}.
$$

The superscript $\lambda$ denotes a certified lower relaxation, not an
additional exact map.

### Threshold relaxation

For $0<d<1-\sqrt3/2$, let $e(d)$ be the low-root threshold from
[`2012`](2012_high_radial_low_root_bounds.md).  Define

$$
\boxed{
\widehat g_{1-d}^{\vee,\rm th}(x)
=
\begin{cases}
x,&x\le e(d),\\
1-e(d),&x>e(d).
\end{cases}
}
$$

Extensivity and the high-demand threshold give

$$
\boxed{
\widehat g_{1-d}^{\vee,\rm th}
\le
\widehat g_{1-d}^\vee.
}
$$

Quarter-radial and Vd-corner estimates play the same role at terminal slots:
they replace an exact V triangle transfer by a simpler branch-specific lower bound.
The branch tables state those terminal bounds directly rather than assigning
another permanent function letter.

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
degenerate intervals.  For a selected radial demand $c_i$, define

$$
\Phi_i^{\rm raw}=g_{c_i,J_i^C}^{\vee},
\qquad
\Phi_i^{\rm ns}=\widehat g_{c_i,J_i^C}^{\vee}.
$$

Use $\Phi_i^{\rm ns}$ when $T_i$ is nonsupercritical and
$\Phi_i^{\rm raw}$ otherwise.  The complete branch word is always displayed in
geometric V-triangle order as

$$
[\Phi_0\mid\Phi_1\mid\Phi_2\mid\Phi_3\mid\Phi_4\mid\Phi_5]
=\Phi_5\circ\Phi_4\circ\Phi_3\circ\Phi_2\circ\Phi_1\circ\Phi_0.
$$

The branch proposition determines how this word is used: cyclic composition,
a cut at a center trace followed by endpoint inequalities, or the exact
five-V-triangle subchain followed by a terminal cap.  Merely writing the word
does not assert an additional universal inequality beyond those branch
propositions.

An identity slot records a weaker *individual handoff*.  It is licensed only
when

$$
J_i^C=\varnothing,
$$

all nonincident boundary traces have been excluded on $e_{i,i+1}$, and $T_i$
is nonsupercritical.  Under precisely these hypotheses the generalized
handoff lemma and nonsupercritical extensivity give

$$
A_{i+1}\ge \widehat g_{c_i}^{\vee}(A_i)\ge A_i.
$$

Thus replacing the $i$th displayed function by $\mathrm I$ means that this
one inequality is weakened to $A_{i+1}\ge A_i$.  It is not, by itself, a
pointwise comparison between the two formal compositions; the corresponding
terminal proof supplies the valid global argument.

For the $N_+=1$ all-Vd0 one-gap branch, the full word has the raw
center-assisted slot $g_{c_0,J_0^C}^{\vee}$ followed by the five hatted slots
$\widehat g_{c_i,J_i^C}^{\vee}$ for $1\le i\le5$.  The one-gap proof retains
that exact five-V-triangle subchain and closes the remaining $T_0$ slot with
its independent terminal diameter cap.  Hence the six-slot reader register is
a faithful expansion of the proved certificate, not a new theorem.
