# A type-independent two-vertex skeleton replacement

Status: Proven

## Scalar input

Use adjacent vertex charts $V_0,V_1$. Suppose changing these two roles can
affect only $e_{5,0},e_{0,1},e_{1,2},r_0,r_1$. The shared edge is
center-free. Let $a,c,B,r\in[0,1)$ be the actual incoming boundary and own
radial reaches to preserve at $V_0$, the actual outgoing reach to preserve
at $V_1$, and the own-radial demand needed to overlap the unchanged C
interval on $r_1$. Assume

$$a<1/2,\qquad a+c<1,\qquad a+B<1,\qquad
r<\max\{1-a,1-B\}.$$

Then two open unit equilateral replacements preserve the skeleton and have
actual boundary sums strictly below one, with no positive adjacent support.
No CE2-only hypothesis is used.

## Choice of strict margins

Choose $a<p_2<1-B$ with $\max\{p_2,1-p_2\}>r$. This is possible because
the supremum of that maximum on $(a,1-B)$ is $\max\{1-a,1-B\}$.
Next choose $a<p_1<\min\{p_2,1/2,1-c\}$, and choose $\varepsilon>0$
smaller than each of

$$p_1-a,\quad p_2-p_1,\quad1-B-p_2,\quad
1-p_1-c,\quad\max\{p_2,1-p_2\}-r.$$

## The two different vertex charts

Put

$$X_0(x,y)=V_0+x(V_5-V_0)+y(V_1-V_0),$$
$$X_1(x,y)=V_1+x(V_0-V_1)+y(V_2-V_1).$$

Both use the metric $x^2+y^2-xy$. For $p\le1/2$ use

$$D^-_{p,\varepsilon}
=\operatorname{int}\operatorname{conv}\{(0,1-p),(1,1-p),(0,-p)\}
+(-\varepsilon,0),$$

and for $p>1/2$ use

$$D^+_{p,\varepsilon}
=\operatorname{int}\operatorname{conv}\{(p,0),(p,1),(p-1,0)\}
+(0,-\varepsilon).$$

The three unshifted sides have unit length. Substitution in their open
half-planes gives actual reaches and boundary sums

| Template | Incoming | Outgoing | Own radial | Sum |
|---|---:|---:|---:|---:|
| minus | $p-\varepsilon$ | $1-p$ | $1-p$ | $1-\varepsilon$ |
| plus | $p$ | $1-p-\varepsilon$ | $p$ | $1-\varepsilon$ |

For minus the inequalities are $x>-\varepsilon$, $y<1-p$,
$y>x+\varepsilon-p$. For plus they are $y>-\varepsilon$, $x<p$,
$x>y+\varepsilon+p-1$. They contain the chart origin. The neighboring
support lines are $(z,1)$ and $(1,z)$, $0\le z\le1$; the displayed
inequalities exclude positive traces on them.

Define $U'_0=X_0(D^-_{p_1,\varepsilon})$ and
$U'_1=X_1(D^-_{p_2,\varepsilon})$ for $p_2\le1/2$, or
$U'_1=X_1(D^+_{p_2,\varepsilon})$ for $p_2>1/2$.
The margins imply the template restrictions $\varepsilon<p$ in the minus
case and $\varepsilon<1-p$ in the plus case.

## Preservation, including endpoints

The new incoming reach at $V_0$ exceeds $a$, and its own reach exceeds $c$.
The two new shared-edge reaches have sum at least

$$1-p_1+p_2-\varepsilon>1,$$

so the open traces overlap strictly. The outgoing reach at $V_1$ exceeds
$B$ in either chart, and its own reach $\max\{p_2,1-p_2\}$ exceeds $r$,
so it overlaps the unchanged C interval. These are exactly the five affected
pieces. Every other skeleton piece is unchanged. Both new roles are
nonsupercritical Vd0 by their actual reaches and lack of adjacent support.
This proves the replacement. $\square$

The gap rank is an output, not an invariant. If the four untouched roles
are nonsupercritical, the replacement produces $N_+'=0$ and is contradicted
by N0 in [`2612`](2612_fixed_witness_unification.md). Full-hexagon coverage
is not claimed for the replacement.
