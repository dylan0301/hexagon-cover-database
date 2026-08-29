# Radial Witnesses and Gap-Enclosure Lemmas

Status: Proven

This note contains the finite-point geometry used by the nonzero-gap proof
packages.  It does not infer an enclosure inequality from a previously proved
case exclusion.  Every witness is explicitly excluded from the six open V
roles, and every terminal inequality is proved from support functions and the
exact local admissible set.

Throughout,

$$
h=\frac{\sqrt3}{2},
$$

and $\mathsf R$ denotes counterclockwise rotation through $2\pi/3$.  For a
compact plane set $K$, let $\Lambda(K)$ be the least side length of a closed
equilateral triangle containing $K$.

## 1. Support formula

For every nonempty compact $K$,

$$
\boxed{
\Lambda(K)=\frac1h\min_{\lVert n\rVert=1}
\sum_{j=0}^2h_K(\mathsf R^jn),
}
$$

where

$$
h_K(n)=\max_{X\in K}\langle X,n\rangle.
$$

Indeed, for fixed outward normals $n,\mathsf Rn,\mathsf R^2n$, the least
supporting equilateral triangle has side

$$
\frac1h\sum_{j=0}^2h_K(\mathsf R^jn).
$$

Minimizing over the orientation proves the formula.  This is the same gauge
as in [`2600`](2600_minimum_enclosing_triangle_tools.md).

## 2. Exact disk-plus-point formula

Let

$$
\mathcal D_\eta=\{X:\lVert X\rVert\le\eta\}
$$

and let $G$ have norm $\rho$.  Then

$$
\boxed{
\Lambda(\mathcal D_\eta\cup\{G\})=
\begin{cases}
\dfrac{3\eta}{h},&\rho\le2\eta,\\[3mm]
\dfrac{3\eta+\sqrt{3(\rho^2-\eta^2)}}{2h},&\rho>2\eta.
\end{cases}}
$$

### Proof

For a unit vector $n$, put

$$
s_j=\langle G,\mathsf R^jn\rangle.
$$

Then $s_0+s_1+s_2=0$ and

$$
\sum_{j=0}^2s_j^2=\frac32\rho^2.
$$

The support sum is

$$
\sum_{j=0}^2\max\{\eta,s_j\}.
$$

If $\rho\le2\eta$, orient the three projections as
$\rho/2,\rho/2,-\rho$; all three disk supports are active and the minimum is
$3\eta$.

Assume $\rho>2\eta$.  On each open angular cell with fixed active support
labels the support sum is a constant plus one cosine, or a constant minus one
cosine.  An interior critical point is therefore a maximum.  A minimum occurs
when one point projection equals $\eta$.  The other two normalized
projections are determined by their sum and sum of squares, and the active one
is

$$
\frac{-\eta+\sqrt{3(\rho^2-\eta^2)}}2.
$$

The minimum support sum is therefore

$$
2\eta+\frac{-\eta+\sqrt{3(\rho^2-\eta^2)}}2,
$$

which gives the displayed formula after division by $h$.  $\square$

## 3. Type-aware radial witnesses

Let the closed V role $T_i=\overline{U_i}$ contain selected boundary anchors
at reaches $a_i,b_i$.  Let

$$
c_{\max}(a_i,b_i)
$$

be the exact own-ray capacity from
[`2004`](../20XX_V_triangle_geometry/2004_admissible_set.md).  If the preceding
role $T_{i-1}$ has positive support on $r_i$, let its capacity on that ray be

$$
C_+(a_{i-1},b_{i-1});
$$

if the following role $T_{i+1}$ has positive support on $r_i$, let its
capacity be

$$
C_-(a_{i+1},b_{i+1})=C_+(b_{i+1},a_{i+1}).
$$

The exact neighboring-ray formula is proved in
[`2008`](../20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md).
Undefined neighboring capacities are omitted.  Define

$$
\Gamma_i=
\max\left\{
 c_{\max}(a_i,b_i),
 C_+(a_{i-1},b_{i-1}),
 C_-(a_{i+1},b_{i+1})
\right\}
$$

with only the support terms permitted by the actual V types, and put

$$
D_i=(1-\Gamma_i)V_i.
$$

### Theorem 3.1

For every $i$,

$$
\boxed{D_i\notin U_0\cup\cdots\cup U_5.}
$$

Hence, under a seven-role cover,

$$
\boxed{D_i\in U_C.}
$$

### Proof

If $D_i\in U_i$, openness gives a slightly more inward point of $r_i$ in
$U_i$.  Together with the two selected boundary anchors this realizes an
own-radial demand strictly larger than $c_{\max}(a_i,b_i)$, a contradiction.

If $D_i\in U_{i-1}$ and $T_{i-1}$ has no positive support on $r_i$, openness
would create such support.  If that support is permitted, openness increases
the neighboring-ray coordinate beyond
$C_+(a_{i-1},b_{i-1})$.  Both alternatives are impossible.  The reflected
argument excludes $U_{i+1}$.

Write $D_i=dV_i$.  For a vertex at cyclic distance two,

$$
\lVert dV_i-V_{i\pm2}\rVert^2=1+d+d^2>1,
$$

and for the opposite vertex,

$$
\lVert dV_i-V_{i+3}\rVert=1+d>1.
$$

A unit equilateral triangle has diameter one, so the three nonlocal roles are
also excluded.  Full coverage forces $D_i\in U_C$.  $\square$

## 4. Common-pair domination

Let $p,q\ge0$ with $p+q\le1$, and put

$$
c_*=c_{\max}(p,q),
\qquad
m=\min\{p,q\}.
$$

Then

$$
\boxed{c_*\ge1-m.}
$$

Indeed, assume $q=m\le p$.  In the exact minimum-side formula of `2004`, the
radial demand $c=1-q$ gives

$$
L_{OA}=q+\max\{p,1-q\}=1,
$$

because $p+q\le1$.  Thus $(p,q,1-q)$ is admissible.  The reflected argument
handles $p=m$.

Moreover,

$$
\boxed{C_+(p,q)\le1-m,
\qquad C_-(p,q)\le1-m.}
$$

This follows directly from the exact formula in `2008`.  If $q\le p$, every
branch of $C_+(p,q)$ is at most $1-q$.  If $p\le q$, the plateau root
satisfies $p(a)\le1-a$, while the linear and radical branches are no larger;
thus $C_+(p,q)\le1-p$.  Reflection gives the second inequality.

Consequently

$$
\boxed{C_+(p,q),C_-(p,q)\le c_{\max}(p,q).}
$$

By coordinatewise antitonicity, the same conclusion holds for every actual
boundary pair that dominates $(p,q)$.

## 5. Complementary-gap obstruction

Let

$$
J(p,q)=[X(q),X(1-p)]\subset e_{0,1},
$$

where $X(t)=V_0+t(V_1-V_0)$, and put

$$
d=1-c_*,
\qquad
\eta=hd.
$$

### Theorem 5.1

$$
\boxed{
\Lambda\left(\mathcal D_\eta\cup J(p,q)\right)\ge1.
}
$$

### Proof

The farther endpoint of $J(p,q)$ from $O$ has squared norm

$$
\rho^2=1-m+m^2.
$$

We first prove

$$
\boxed{3c_*(1-c_*)\ge m(1-m).}
$$

We already know $c_*\ge1-m\ge1/2$.  If $c_*\le h$, then

$$
3c_*(1-c_*)\ge3h(1-h)>\frac14\ge m(1-m).
$$

Assume $c_*>h$.  Put

$$
t_\pm(c)=\frac c2\left(1\pm\sqrt{4c^2-3}\right).
$$

We claim that every admissible subcritical pair with radial coordinate $c>h$
has

$$
m\le t_-(c).
$$

Use the algebraic cells of `2004`, with $M=\max\{p,q\}$ and $s=m+M\le1$.
In Cell L,

$$
f_c(m):=c^4-c^2+cm-m^2\le0.
$$

The roots of $f_c$ are $t_-(c),t_+(c)$.  The alternative
$m\ge t_+(c)$ is incompatible with the Cell-L selector.  Indeed
$t_+(c)>\sqrt3/4$, and for $M\ge m$ the selector quantity

$$
s^4-s^2+mM
$$

is increasing in $M$ and is at least

$$
16m^4-3m^2>0.
$$

Cell L requires this quantity to be nonpositive.  Hence $m\le t_-(c)$.

In Cell T,

$$
F_T=(s^2-1)c^2+Mc-M^2\le0.
$$

The identity

$$
f_c(m)-F_T
=(c-s)\left(Mc^2-M+c^3+c^2m+m\right)
$$

has nonpositive first factor, because the selected Cell-T value satisfies
$c\le s$.  The second factor is positive: Cell T gives $c\ge M$, and

$$
c^3\ge c(1-c^2)\ge M(1-c^2)
$$

because $c^2>1/2$.  Thus $f_c(m)\le F_T\le0$.  The high-root alternative is
excluded as above, so again $m\le t_-(c)$.

Let

$$
g(c)=t_-(c).
$$

A direct calculation gives

$$
\begin{aligned}
3c(1-c)-g(c)(1-g(c))
&=\frac{c(1-c)}2
\left(5-2c-2c^2+\sqrt{4c^2-3}\right)\\
&\ge0
\end{aligned}
$$

for $h<c<1$.  Since $0\le m\le g(c)<1/2$,

$$
m(1-m)\le g(c)(1-g(c))\le3c(1-c).
$$

This proves the boxed scalar inequality.

Apply the disk-plus-point formula.  In its second branch,

$$
\Lambda(\mathcal D_{hd}\cup\{G\})\ge1
$$

is equivalent, after one squaring, to

$$
3d(1-d)\ge1-\rho^2=m(1-m).
$$

Since $d=1-c_*$, this is the inequality just proved.  In the first branch,
$\rho\le2hd$ implies $d\ge1/2$, so $3d\ge1$.  Thus the conclusion holds in
both branches.  Since the farther endpoint belongs to $J(p,q)$, the theorem
follows.  $\square$

## 6. CE2 two-gap short-ray obstruction

Use the signed CE2 center variables from
[`2109`](../21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):

$$
0<R<1,
\qquad W=1-R,
$$

$$
E=\sqrt{1-RW},
\qquad \eta=1-E,
\qquad P=E(1-E),
$$

and

$$
\alpha+W\delta<P,
\qquad
R\alpha+\delta<P.
$$

Put

$$
p=W-\alpha,
\qquad
q=R-\delta,
\qquad
e=\min\{\alpha,\delta\}.
$$

### Theorem 6.1

If the pair $(p,q)$ is realized as common lower boundary data, then

$$
\boxed{c_{\max}(p,q)<1-e.}
$$

Consequently the radial point on $r_2$ or $r_4$ forced by the common pair lies
strictly beyond the corresponding CE2 center exit.

### Proof

The identity $RW=\eta+P$ and the two CE2 inequalities give

$$
Wq=RW-W\delta>\eta+\alpha,
$$

and

$$
Rp=RW-R\alpha>\eta+\delta.
$$

Hence

$$
p,q>\eta+e.
$$

Let $M=\max\{R,W\}$.  Since $\alpha,\delta\ge e$,

$$
P>(1+M)e.
$$

Because $P=E\eta$ and

$$
(1+M)^2-3E^2=(2M-1)(2-M)\ge0,
$$

we obtain

$$
\eta>\sqrt3e,
$$

and therefore

$$
\boxed{p,q>(1+\sqrt3)e.}
$$

Also

$$
e<\frac{P}{1+M}
\le\frac{2\sqrt3-3}{6}=:e_*.
$$

Set $c=1-e$ and

$$
f_c(t)=c^4-c^2+ct-t^2.
$$

Its two roots are

$$
t_\pm=\frac c2\left(1\pm\sqrt{4c^2-3}\right).
$$

Put $t_0=(1+\sqrt3)e$.  Direct expansion gives

$$
f_{1-e}(t_0)=eB(e),
$$

where

$$
B(e)=e^3-4e^2-3\sqrt3e+\sqrt3-1.
$$

On $[0,e_*]$, one has $B'(e)<0$ and

$$
B(e_*)=\frac{302\sqrt3-501}{72}>0.
$$

Moreover $t_0<c/2$.  Hence

$$
t_-<t_0<p,q.
$$

Since

$$
p+q=1-\alpha-\delta\le1-2e=c-e,
$$

we also have

$$
p,q<t_+.
$$

Therefore

$$
f_c(p)>0,
\qquad
f_c(q)>0.
$$

Now $c>p+q$.  The four finite-caliper side lengths in `2004` are

$$
q+c,
\qquad
p+c,
\qquad
\frac{c^2}{\sqrt{p^2-pc+c^2}},
\qquad
\frac{c^2}{\sqrt{q^2-qc+c^2}}.
$$

The first two exceed one because $p,q>e$.  The last two exceed one precisely
because $f_c(p),f_c(q)>0$.  Thus $(p,q,c)$ is not admissible, proving

$$
c_{\max}(p,q)<c=1-e.
$$

If $e=\delta$, the point $(1-c_{\max})V_2$ lies farther than $\delta$ from
$O$, while the center reaches exactly $\delta$ on $r_2$.  If $e=\alpha$, the
same conclusion holds on $r_4$.  $\square$
