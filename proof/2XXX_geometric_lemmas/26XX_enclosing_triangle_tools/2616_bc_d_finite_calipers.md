# Five-point BC and four-point D finite-caliper obstructions

Status: Proven

This source replaces the CE1/CE2 candidate normal forms in the BC and D
terminal enclosure arguments. Original-cover incidence and midpoint placement
remain separate hypotheses. It uses the finite caliper theorem in
[2609](2609_simplified_finite_enclosure_lemmas.md), the support-cell argument in
[2607](2607_minimal_enclosing_equilateral_quadrilateral_lemma.md), and the
capacity inequality and rational envelope in
[2615](2615_slack_sensitive_radial_envelope.md). No disk is used.

## 1. Conventions and finite calipers

Put $O=0$, $V_i=(\cos(i\pi/3),\sin(i\pi/3))$, $M_0=V_0/2$,
$G_w=(1-w)V_0+wV_1$, $Y(w)=V_0-wV_1$, and $h=\sqrt3/2$.
Let $R$ be rotation through $120$ degrees and $J$ rotation through $90$ degrees.
For finite $F$, write
$$W_F(n)=\sum_{j=0}^2\max_{p\in F}\langle p,R^jn\rangle.$$
The least equilateral enclosure side is
$$\Lambda(F)=\min_{n\ne0}\frac{W_F(n)}{h\|n\|}.$$
It suffices to test the outward normals to the nonzero hull edges.
This is the finite-point theorem, not a numerical orientation scan.
Compact containment in an open unit triangle implies $\Lambda(F)<1$.

Write $C_0(a,b)=c_{\max}(a,b)$ for the own-ray **capacity function**, not the
actual reach $C_i$ of an original triangle. Put $f(a,b)=1-C_0(a,b)$.
The inequalities in [2008b](../20XX_V_triangle_geometry/2008b_direct_neighbor_domination.md)
give $C_\pm(a,b)\le1-\min(a,b)\le C_0(a,b)$ and antitonicity of capacity.

## 2. Five-point geometric theorem

**Theorem 2.1.** Suppose $0<x\le y<1$ and $x/2\le z\le y$. Put
$$r=f(1-y,z),\qquad t=f(1-z,x/2),$$
$$F_5=\{M_0,G_x,G_y,rV_2,tV_4\}.$$
Then $\Lambda(F_5)>1$. The count is at most five, since $x=y$ is permitted.

**Proof.** The deficit bounds give
$$0<r\le\min(y,1-y),\qquad0<t\le x/2.$$
Write $M=M_0$, $P=rV_2$, $Q=tV_4$, and $k=y-r$. In coordinates these are
$$M=(1/2,0),\quad G_x=(1-x/2,hx),\quad G_y=(1-y/2,hy),$$
$$P=(-r/2,hr),\quad Q=(-t/2,-ht).$$
For $x<y$ the hull order is $M,G_x,G_y,P,Q$. Consecutive signed cross
products are positive under the displayed bounds. When $x=y$, discard the
zero edge $G_xG_y$; the other four edge calculations remain valid.
The five exact caliper side lengths are
$$
\begin{aligned}
L_1&=\frac{1-x+2xy+\max\{r(1-2x),2tx\}}{\sqrt{1-2x+4x^2}},\\
L_2&=1+r+t,\\
L_3&=\frac{r+t+\max\{1/2,1-x(1-k)\}}{\sqrt{1-k+k^2}},\\
L_4&=\frac{rt+t+ry+\max\{r/2,r-(r+t)x,t^2\}}{\sqrt{r^2+rt+t^2}},\\
L_5&=\frac{1+t+2ty+\max\{r,2t^2\}}{\sqrt{1+2t+4t^2}}.
\end{aligned}
$$
They correspond respectively to $MG_x,G_xG_y,G_yP,PQ,QM$.
One obtains them by rotating each outward edge normal twice by $120$ degrees
and taking the largest point projection in each direction.
For the only capacity-dependent caliper, use
$$n=(-hk,1-k/2),\qquad\|n\|^2=1-k+k^2.$$
The three supports divided by $h$ are $r$, $t$, and
$\max\{1/2,1-x(1-k)\}$, proving the expression for $L_3$.

Four calipers are elementary. Clearly $L_2>1$. The numerator of $L_1$ is
strictly greater than $1-x+2x^2$, and
$$(1-x+2x^2)^2-(1-2x+4x^2)=x^2(2x-1)^2\ge0.$$
Thus $L_1>1$. For $L_5$, use $y\ge x\ge2t$ and
$$(1+t+2t^2)^2-(1+2t+4t^2)=t^2(1+2t)^2>0.$$
For $L_4$, put $v=t/r>0$, use $y\ge x$, and omit the $t^2$ entry of its maximum:
$$L_4\ge\frac{t+v+x+\max\{1/2,1-(1+v)x\}}{\sqrt{1+v+v^2}}.$$
The expression $x+\max\{1/2,1-(1+v)x\}$ is minimized at
$x=1/[2(1+v)]$. Hence its numerator exceeds
$$g(v)=v+1/2+\frac1{2(1+v)},$$
and
$$g(v)^2-(1+v+v^2)=\frac{v^2}{4(1+v)^2}>0.$$
Thus $L_4>1$.

Finally [2615](2615_slack_sensitive_radial_envelope.md) proves
$$2(r+t)>(1-y+r)(2x-y+r).$$
Equivalently $r+t>(1-k)(x-k/2)$. Therefore
$$r+t+\max\{1/2,1-x(1-k)\}>1-k/2+k^2/2\ge\sqrt{1-k+k^2},$$
where the last squared difference is $k^2(1-k)^2/4$. Thus $L_3>1$ also.
Every nonzero hull-edge caliper exceeds one, including the singleton-gap
case. This proves the theorem. $\square$

## 3. Five fixed witnesses from the original BC configuration

**Theorem 3.1.** Use the original open-role conventions of
[2612](2612_fixed_witness_unification.md). Assume $J_0$ is an actual gap,
$A_i+B_i\le1$ for $1\le i\le5$, four middle handoffs
$B_i+A_{i+1}>1$ for $1\le i\le4$, and $B_5\ge B_0/2$.
Put
$$x=B_0,\qquad y=1-A_1,\qquad z=B_3,$$
$$r=f(1-y,z),\qquad t=f(1-z,x/2),\qquad \widehat t=\min\{t,A_3\},$$
$$K_{BC}^{(5)}=\{M_0,G_x,G_y,rV_2,\widehat tV_4\}.$$
Then $\Lambda(K_{BC}^{(5)})>1$. Under skeleton coverage with the distinguished
C midpoint $M_0$, these fixed points all belong to $U_C$.

**Proof.** Path monotonicity gives increasing $A_1,\ldots,A_5$ and decreasing
$B_1,\ldots,B_5$. Consequently $0<x\le y<1$ and $x/2\le z\le y$.
Let $\rho_i=f(A_i,B_i)$. Applied at each neighbor's own pair, the comparison
$C_\pm\le1-\min(A,B)$ bounds the actual total inward reach on $r_i$ by
$$1-\min\{\rho_i,\min(A_{i-1},B_{i-1}),\min(A_{i+1},B_{i+1})\}.$$
Using $\rho_i\le\min(A_i,B_i)$ and path monotonicity, this is
$$1-\min\{\rho_i,A_{i-1},B_{i+1}\}.$$
The bounded-frontier lemma of [2612](2612_fixed_witness_unification.md)
therefore forces that latter radius times $V_i$ into $U_C$.

Since $(A_2,B_2)\ge(1-y,z)$, antitonicity gives $r\le\rho_2$; also
$r\le1-y=A_1$ and $r\le z=B_3$. Thus $rV_2$ is missed by every open V role.
Likewise $(A_4,B_4)\ge(1-z,x/2)$ gives $t\le\rho_4$, and
$t\le x/2\le B_5$. Clipping by $A_3$ makes $\widehat tV_4$ safe for the
remaining neighboring supplier. The two gap endpoints and the midpoint
are already in $U_C$ under the theorem's covering hypotheses.

If $A_3\ge t$, Theorem 2.1 applies directly. If $A_3<t$, then
$A_3\ge A_1=1-y$, and
$$\|G_y-A_3V_4\|^2\ge\|G_y-(1-y)V_4\|^2=1+(1-y)(2-y)>1.$$
The diameter obstruction completes this case. Thus the five fixed points
always have enclosure side greater than one. No center-candidate normal
form, own-demand recovery, or CE1 return is used. $\square$

The midpoint anchor is a structural assumption, not a point asserted to be
V-excluded. The tail inequality is a hypothesis of the pure theorem;
[2018b](../20XX_V_triangle_geometry/2018b_shared_gap_anchor_transfer.md)
provides it from original perimeter coverage. Both gap ranks and arbitrary
V types on the nonsupercritical path are permitted. The old six-point set
still obstructs enclosure: this new set lies in its convex hull, since its
radial points are no farther out than the actual total endpoints and the
origin is in the old witness hull. No claim of minimal point count is made.

## 4. Stronger four-point D theorem

**Theorem 4.1.** If $a\ge0$, $\varepsilon>0$, $\beta\ge0$, and
$$\beta\le\frac{\varepsilon}{a+\varepsilon},$$
then
$$\Lambda\{O,\varepsilon V_1,Y(a),Y(1-\beta)\}\ge1.$$
Neither $a\le\varepsilon$ nor $a+\varepsilon\le1$ is required.

**Proof.** If $a=0$, the set contains $O,V_0$. Put $s=a+\varepsilon$.
If $s\ge1$, then
$$\|Y(a)-\varepsilon V_1\|^2=1-s+s^2\ge1.$$
These are diameter obstructions. Otherwise let $v=a/s$, so $0<s,v<1$.
The ratio condition gives $1-\beta\ge v$, and $a=sv\le v$.
Thus $Y(v)$ lies in the segment $[Y(a),Y(1-\beta)]$.
It suffices to enclose the smaller quadrilateral, in cyclic order,
$$O,\quad Q=Y(v),\quad A=Y(sv),\quad P=s(1-v)V_1.$$
Its four outward normals may be chosen as
$$(-hv,v/2-1),\quad v(1-s)(h,-1/2),\quad(hs,1-s/2),\quad s(1-v)(-h,1/2).$$
The maximizing support triples in those directions and their two rotations
are respectively $(O,A,P)$, $(A,P,O)$, $(A,O,Q)$, and $(O,Q,A)$.
They give the exact four caliper sides
$$\frac1{\sqrt{1-v+v^2}},\qquad1+s(1-v),\qquad
\frac1{\sqrt{1-s+s^2}},\qquad1+v(1-s).$$
All are strictly greater than one because $0<s,v<1$.
The finite caliper theorem proves the nondegenerate case; the diameter
cases give the weak inequality in the full statement. $\square$

The D placement adapters must still force the actual supported endpoint and
both gap endpoints and prove the ratio bound. Size inequalities may remain
useful for that forcing, even though they are not needed by Theorem 4.1.
The two original supplier charts, their strict margins, and all replacement
arguments are unchanged.

## 5. Exact checks and scope

The analytic proofs above supply hull completeness, domain coverage, and
open/closed endpoint logic. `verify_finite_calipers.py` checks the displayed
polynomial identities, hull turns, support formulas, and the clipping identity.
The capacity algebra is independently checked by the two programs accompanying
2615. None of these checks is a proof-assistant formalization. Existing zero-gap
certificates and the structural CE1/CE2 classification remain separate; only
these two terminal enclosure arguments cease to depend on the center normal form.
