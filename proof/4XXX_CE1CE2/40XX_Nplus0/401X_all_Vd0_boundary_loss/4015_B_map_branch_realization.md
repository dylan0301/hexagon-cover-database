# Exact Capped $B$-Map Semantics and Branch Realization

Status: Proven

This file corrects the map semantics used by the `401X` branch inventory. The
former version treated a disconnected algebraic sheet as a second geometric
radial component. That is impossible for the true down-closed admissible set.

## Exact unclassified map

Use the exact piecewise admissible set $\mathcal A$ from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md).
The exact unclassified demand map is

$$
B_c(a)=
\max_{\substack{0\le b\le1\\ {}(a,b,c)\in\mathcal A}}b.
$$

It is proved and audited in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md).

## Actual nonsupercritical map

Let $A(T),B(T),C(T)$ be the actual local reaches of a unit Vd0 triangle. The
map relevant to an $N_+=0$ row is the supremal envelope

$$
\mathsf B_c^0(a)=
\sup_{\substack{
T\text{ is Vd0}\\
A(T)\ge a\\
C(T)\ge c\\
A(T)+B(T)\le1
}}B(T),
$$

when the set is nonempty. It satisfies the safe bounds

$$
\mathsf B_c^0(a)\le B_c(a),
$$

and

$$
\mathsf B_c^0(a)\le1-a.
$$

The shortcut

$$
\max_{\substack{
0\le b\le1\\
{}(a,b,c)\in\mathcal A\\
a+b\le1
}}b
$$

restricts demands, not the actual realizing row. It is an upper relaxation,
not an exact row-class definition without an additional tightening theorem.

## Exact safe relaxation

Define

$$
\widehat B_c(a)=
\max_{\substack{
0\le b\le1-a\\
{}(a,b,c)\in\mathcal A
}}b.
$$

The exact interval-fiber statement in `2007` gives

$$
\boxed{
\widehat B_c(a)=\min\left\{B_c(a),1-a\right\}.
}
$$

This is a proof-safe upper bound for the actual row-class map:

$$
\boxed{
\mathsf B_c^0(a)\le\widehat B_c(a).
}
$$

Indeed, let $T$ occur in the supremum defining $\mathsf B_c^0(a)$ and put
$b=B(T)$. Since $a\le A(T)$ and $A(T)+B(T)\le1$,

$$
a+b\le1.
$$

The same triangle realizes the demand triple $(a,b,c)$, so
$b\le\widehat B_c(a)$. Taking the supremum proves the bound. No assertion that
the maximizing demand triple realizes the actual row class is needed.

## Exact four-label partition

Every maximizer of $\widehat B_c(a)$ belongs, with transition ties assigned in
a fixed order, to exactly one of the following four labels:

$$
\boxed{
\mathrm{Full},\qquad L,\qquad T_-,\qquad T_+^{hi}.
}
$$

To prove this, put

$$
\sigma=a+b,
\qquad
q=\sigma^4-\sigma^2+ab.
$$

The cap $b\le1-a$ gives $\sigma\le1$. Hence Cell $S$ from `2004` is absent,
and

$$
a^2+ab+b^2=\sigma^2-ab\le1
$$

is automatic. Only the exact Cells $L$ and $T$ remain.

If the cap is active, then $b=1-a$ and the label is $\mathrm{Full}$. Suppose
that $b<1-a$. A maximizing point must lie on a radial frontier of Cell $L$ or
Cell $T$. Otherwise $b$ can be increased slightly while preserving all strict
cell inequalities. The surface $q=0$ is a shared transition, not a terminal
frontier: the two exact cells agree there. The selector $c=2\max(a,b)$ is not
an additional terminal frontier. In the only potentially restrictive ordered
half $a\le b$, the Cell-$T$ inequality at $c=2b$ is

$$
b^2\left(4\sigma^2-3\right)\le0,
$$

while $q\ge0$ implies $\sigma\ge\sqrt3/2$ because

$$
q\le\sigma^4-\frac34\sigma^2.
$$

Thus selector equality can occur only on the existing Cell-$T$ frontier.

On a Cell-$L$ frontier with $b<a$, one has

$$
c^4-c^2+bc-b^2=0.
$$

Its two formal roots in $b$ are

$$
b=\frac c2\left(1\pm\sqrt{4c^2-3}\right).
$$

Only the minus root can satisfy $q\le0$. For the plus root,
$b\ge\sqrt3/4$. At $a=b$ one has

$$
q=b^2\left(16b^2-3\right)\ge0,
$$

and $q$ is strictly increasing in $a$ for $a>b$ because

$$
\frac{\partial q}{\partial a}
=4\sigma^3-2\sigma+b>0
$$

when $\sigma\ge2b\ge\sqrt3/2$. Hence the plus root contradicts $q\le0$.
The selected Cell-$L$ output is therefore

$$
b=\ell(c):=
\frac c2\left(1-\sqrt{4c^2-3}\right),
$$

which is the label $L$.

On a Cell-$T$ frontier with $b\le a$, the label is $T_-$. If $a\le b$, put
$\beta=b/c$. The frontier equation becomes

$$
\beta^2-\beta+1-\sigma^2=0.
$$

The exact component selector $c\le2b$ says $\beta\ge1/2$. Therefore

$$
\beta=
\frac{1+\sqrt{4\sigma^2-3}}2,
$$

which is precisely the genuine label $T_+^{hi}$. The other formal root has
$\beta\le1/2$ and is the discarded high-$c$ component. This proves that the
four displayed labels form a complete safe upper partition.

## The discarded Cell-2 sheet

In the ordered half $a\le b$, put

$$
s=a+b,
\qquad
d=\sqrt{4s^2-3}.
$$

The former raw inequality

$$
(s^2-1)c^2+bc-b^2\le0
$$

has roots

$$
c_- =\frac{2b}{1+d},
\qquad
c_+ =\frac{2b}{1-d}.
$$

As a quadratic inequality it accepts

$$
c\le c_-
\qquad\text{or}\qquad
c\ge c_+.
$$

But every true $c$-fiber of $\mathcal A$ is an interval starting at zero.
Therefore the high-$c$ component is not a second geometric branch. The
necessary component selector is

$$
c\le2b
$$

in this ordered half, or symmetrically

$$
c\le2\max(a,b).
$$

This selector removes the demonstrated fake sheet. By itself it does not prove
that the remaining algebraic roots are attainable or complete; the full
unclassified support-contact realization is now proved in `2007`.

In the old notation, the sheet called $T_+^{lo}$ was this fake high-$c$
component. It may not be called a realized branch of $B_c(a)$ or
$\mathsf B_c^0(a)$.

## Status of the old branch-pair inventory

The labels

$$
L,
\quad
\mathrm{Full},
\quad
T_-,
\quad
T_+^{hi},
\quad
T_+^{lo}
$$

in older `401X` and `407X` files are historical algebraic labels. The exact
safe partition proved above retains only

$$
L,
\quad
\mathrm{Full},
\quad
T_-,
\quad
T_+^{hi}.
$$

It deletes $T_+^{lo}$ without replacing it. Thus the classified-map inclusion
problem is resolved at the level needed for an upper-bound proof. Each package
must still check that its branch matrix covers all ordered pairs of these four
true labels. Numerical root selection or satisfaction of the raw Cell-$T$
polynomial is not such a branch-matrix proof.
