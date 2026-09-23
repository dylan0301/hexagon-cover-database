# Slack-sensitive radial envelope and coupled BC capacity inequality

Status: Proven

## Statement and scope

Write $C_0(a,b)=c_{\max}(a,b)$ for the own-ray capacity defined and proved in
[2004](../20XX_V_triangle_geometry/2004_admissible_set.md).
Only nonsupercritical pairs $a+b\le1$ occur here. Antitonicity and
$C_0(a,b)\ge1-\min(a,b)$ come from
[2008b](../20XX_V_triangle_geometry/2008b_direct_neighbor_domination.md).
This source owns the reusable rational envelope and its coupled application.
The finite-caliper geometry and the original-cover forcing are separate in
[2616](2616_bc_d_finite_calipers.md). Neither argument uses signed center coordinates.

**Theorem.** Suppose
\[
0<x\le y<1,\qquad x/2\le z\le y,
\]
and define
\[
r=1-C_0(1-y,z),\qquad t=1-C_0(1-z,x/2).
\]
Then, in fact strictly,
\[
\boxed{2(r+t)>(1-y+r)(2x-y+r).}\tag{19}
\]
Consequently, for \(k=y-r\),
\[
\boxed{r+t+\max\{1/2,1-x(1-k)\}>\sqrt{1-k+k^2}.}\tag{16}
\]
The proof is analytic, with exact rational polynomial checks. It uses the
local capacity formula, not the CE1/CE2 normal form for an enclosing center
triangle. The accompanying `verify_bc_envelope.py` and `verify_bc_capacity_calculus.py` audit the polynomial identities
and signs; it is not a floating-point search or a substitute for the domain
and concavity arguments below.

Put
\[
u=x/2,\qquad f(a,b)=1-C_0(a,b),
\]
so the domain is
\[
0<u,\quad 2u\le y<1,\quad u\le z\le y,
\]
and the desired positive quantity is
\[
P(y,r,t):=2(r+t)-(1-y+r)(4u-y+r).
\]
Both arguments of each capacity are nonnegative and have sum at most one.
In particular, \(0<r,t\le1/2\). At fixed \(u,y\),
\[
P_r=1-4u+2y-2r\ge1-2r\ge0,\qquad P_t=2.\tag{A}
\]
Therefore lower bounds on either radius may be substituted throughout.

## 1. Local capacity tools

Let \(h=\sqrt3/2\). For \(0\le m\le1/2\), define
\[
\ell(m)=1-c(m),\qquad c(m)\in[h,1],
\]
where \(c(m)\) is the unique root in this interval of
\[
F(c,m):=c^4-c^2+mc-m^2=0.
\]
Also set
\[
q(m)=\frac{m(1-m)}2,\qquad b(m)=\frac m2-\frac25m^2.
\]

### 1.1. Deficit bounds

For \(a+b\le1\), with \(m=\min(a,b)\),
\[
\boxed{q(m)\le\ell(m)\le f(a,b)\le m.}\tag{B}
\]
Moreover,
\[
\boxed{b(m)\le\ell(m)\quad(0\le m\le3/8).}\tag{C}
\]

The upper bound \(f\le m\) is equivalent to the known own-ray bound
\(C_0(a,b)\ge1-m\). To see \(C_0(a,b)\le c(m)\), first suppose
\(m\le h/2\). The diagonal pair \((m,m)\) belongs to the quartic cell,
because its cell polynomial is \(m^2(16m^2-3)\le0\). Thus
\(C_0(a,b)\le C_0(m,m)=c(m)\). If \(m\ge h/2\), antitonicity gives
\(C_0(a,b)\le C_0(h/2,h/2)=h\le c(m)\).

For completeness, both lower bounds are certified by substitution in the
quartic. For \(v=1/2-m\),
\[
\frac{1024F(1-q(m),m)}{m^2}
=64v^6+64v^5+496v^4+480v^3+1276v^2+644v+33.
\]
For \(v=3/8-m\),
\[
\begin{split}
\frac{10240000F(1-b(m),m)}{m^2}={}&262144v^6+720896v^5+3174400v^4\\
&+5826560v^3+11428800v^2+9721776v+3049.
\end{split}
\]
All coefficients are positive. The tested values of \(c\) exceed \(h\),
and \(F_c=4c^3-2c+m>0\) on \([h,1]\). Hence these nonnegative quartic
values imply (B) and (C). At \(m=0\), take the continuous limits.

### 1.2. Concavity and the transition function

Let \(D_0=4c^3-2c+m\). Implicit differentiation gives
\[
\ell'(m)=\frac{c-2m}{D_0},
\]
\[
\ell''(m)=-\frac{2\{8c^2m(c-m)+c^2-cm+m^2\}}{D_0^3}<0.
\]
Thus \(\ell\) is concave and, since \(\ell(0)=0\) and
\(\ell'(0)=1/2\),
\[
\ell(m)\le m/2.
\]
It is increasing on \([0,3/8]\). The function
\[
g(m)=m+\ell(m)
\]
is strictly increasing on \([0,1/2]\), because
\[
g'(m)=\frac{4c^3-c-m}{D_0}>0.
\]
Also,
\[
g(3/8)\ge3/8+b(3/8)=81/160>1/2.\tag{D}
\]
Consequently \(g(z)\le1/2\) implies \(z<3/8\).

For \(0\le b\le a\) and \(a+b\le1\), the exact capacity
formula can be written
\[
f(a,b)=
\begin{cases}
\ell(b),&1-a\ge g(b),\\
1-a\,j(a+b),&1-a\le g(b),
\end{cases}\tag{E}
\]
where
\[
j(s)=\frac2{1+\sqrt{4s^2-3}}.
\]
The expressions agree at the transition; the second expression is used
only in its real selected domain. Formula (E) follows from the exact
quartic/triangular cell formula. Indeed, its cell polynomial at sum \(s\)
is \(F(s,b)\), whose selected zero is \(s=c(b)\).

Each branch of \(f\) is concave separately in either argument while the
larger argument remains the first one. For the triangular branch,
\(j''(s)>0\). If \(D=\sqrt{4s^2-3}\in(0,1]\), then
\[
2j'(s)+\frac s2j''(s)
=\frac{4s(-2D^3-4D^2+9D+3)}{D^3(1+D)^3}>0.
\]
The numerator bracket is at least \(3D+3\). Since \(a\ge(a+b)/2\),
\(\partial_a^2[a\,j(a+b)]>0\); also
\(\partial_b^2[a\,j(a+b)]=a j''(a+b)>0\). Negating these derivatives
proves the asserted branchwise concavity. The quartic branch is constant
in the first argument and concave in the second.

### 1.3. A two-piece rational envelope

Write `delta = 1-a-b`, `m = min(a,b)`, and retain
\[
 b(m)=m/2-2m^2/5,
 \qquad K(m)=\frac{5+4m}{5-4m}.
\]
For every nonsupercritical pair with \(0\le m\le3/8\),
\[
\boxed{
 f(a,b)\ge\max\{b(m),\ m-K(m)\delta\}.
}\tag{RE}
\]
Equivalently,
\[
 C_0(a,b)\le\min\{1-b(m),\ 1-m+K(m)(1-a-b)\}.
\]
This envelope is exact at \(a+b=1\). Its two branches meet at the explicit
slack \(\delta=b(m)\), rather than at an implicitly defined quartic root.
It is not asserted with the same coefficients when \(m>3/8\).

**Chord principle.** If $0<\beta\le m$, $F(0)=m$, $F\ge\beta$, and
$F$ is concave on $[0,\beta]$, then
$$F(\delta)\ge\max\{\beta,m-(m-\beta)\delta/\beta\}.$$
Before $\beta$ this is the chord inequality; afterward the affine term is
at most $\beta$. Only concavity on that first interval is required.

**Proof.** If \(m=0\), the assertion is immediate. Otherwise write
\(M=1-m-\delta\) and use the baseline bound \(f(M,m)\ge\ell(m)\ge b(m)\).
For \(\delta\ge b(m)\), the affine entry is at most \(b(m)\), so nothing
more is needed.

For \(0\le\delta\le b(m)\), we have
\[
 M+m=1-\delta\ge1-b(m)\ge1-\ell(m)=c(m).
\]
Thus the selected triangular branch applies. On this interval,
\[
 F_m(\delta)=f(1-m-\delta,m)
\]
is concave, as established in Section 1.2; here \(M\ge m\) since
\(m\le3/8\) and \(1-2m-b(m)\ge19/160>0\).
No assumption $M\ge1/2$ is needed: the ordered-domain derivative proof
in Section 1.2 applies.
Its endpoint values satisfy
\[
 F_m(0)=m,\qquad F_m(b(m))\ge b(m).
\]
The chord inequality therefore gives
\[
 F_m(\delta)\ge m-\frac{m-b(m)}{b(m)}\delta
 =m-\frac{5+4m}{5-4m}\delta.
\]
This proves (RE).

## 2. Easy parameter regions

### 2.1. The region \(y\ge1/2\)

Put \(a=1-y\le1/2\). Then \(u\le(1-a)/2\), \(u\le z\le1-a\).
Use (A) and the lower bounds (B).

If \(z\ge a\) and \(z\le1-u\), we may use \(r=q(a)\), \(t=q(u)\).
The resulting expression is concave in \(u\); its endpoint at \(u=0\)
is visibly nonnegative, and its endpoint at \(u=(1-a)/2\) is
\[
\frac{(1-a)^3(1+a)}4>0.
\]

If \(z\ge a\) and \(z\ge1-u\), then \(r,t\ge q(a)\), because
\(a\le1-z\le u\le1/2\). After this replacement the expression decreases
with \(u\), and at \(u=(1-a)/2\) it equals
\[
\frac{a(1-a)(a^2-a+2)}4>0.
\]

If \(z\le a\), then \(r,t\ge q(u)\). The resulting expression is
concave in \(a\) on
\[
u\le a\le\min\{1/2,1-2u\}.
\]
Its possible endpoint values are
\[
\begin{array}{c|c|c}
a& P\text{ after replacement}&\text{range}\\\hline
u&\frac u4(14-43u+14u^2-u^3)&0\le u\le1/3\\
1/2&\frac14(1-17u^2+10u^3-u^4)&0\le u\le1/4\\
1-2u&\frac u4(-u^3+2u^2+9u-2)&1/4\le u\le1/3.
\end{array}
\]
The three polynomial brackets are positive. The first decreases to
\(32/27\), the second decreases to \(23/256\), and the third increases
from \(23/64\), respectively. This proves the region.

### 2.2. The region \(y\le1/2\), \(z\ge2u\)

Here \(r\ge q(z)\) and \(t\ge q(u)\). The replaced expression increases
with \(y\), so set \(y=z\). It is then concave in \(u\in[0,z/2]\).
Its value at zero is positive, and its value at \(u=z/2\) is
\[
\frac{z^3(2-z)}4>0.
\]

## 3. Reduction of the remaining region to three transitions

It remains to consider
\[
0<u\le1/4,\quad u\le z\le2u\le y\le1/2.\tag{H}
\]
The first arguments of both capacities are their larger arguments, so
(E) applies throughout.

Fix \(u,z\) and vary \(y\). In the triangular branch, \(r''(y)\le0\),
and direct differentiation gives
\[
\frac{d^2P}{dy^2}
=(1-4u+2y-2r)r''-2(1-r')^2\le0.
\]
In the quartic branch \(r\) is constant and
\(dP/dy=1+4u+2r-2y>0\). Hence it suffices to check
\(y=2u\), the already-proved endpoint \(y=1/2\), or the transition
\(y=g(z)\), whenever it belongs to the interval.

On \(y=2u\),
\[
P=r(1-r)+2t-2u(1-2u).\tag{I}
\]
The function \(r(1-r)\) is concave and increasing for \(0\le r\le1/2\).
By branchwise concavity of both radii, (I) is concave on each interval in
\(z\) separated by \(g(z)=2u\) and \(z=g(u)\). Thus its minimum is at
\(z=u\), \(z=2u\), or one of these transitions. At \(z=u\), \(t=u\),
so (I) is \(r(1-r)+4u^2>0\). At \(z=2u\), \(r=2u\), so it is \(2t>0\).

On \(y=g(z)\), we have \(r=\ell(z)\) and \(z<3/8\), and
\[
P=2\ell(z)+2t-(1-z)(4u-z).
\]
The allowed interval for \(u\) is \([z/2,g(z)/2]\). This expression is
branchwise concave in \(u\), with its only possible switch at \(z=g(u)\).
Its endpoints are the already-checked case \(z=2u\) and the first
transition below. Therefore only these three configurations remain:
\[
\begin{array}{c|l}
\mathrm A& y=2u=g(z),\ r=\ell(z),\\
\mathrm B& y=2u,\ z=g(u),\ t=\ell(u),\\
\mathrm C& y=g(z),\ z=g(u),\ r=\ell(z),\ t=\ell(u).
\end{array}\tag{J}
\]
This is an exhaustive reduction by concavity, not an assumption that
capacities always lie at transitions.

## 4. Exact transition checks

### 4.1. Transition A: one rational bound, no subdivision

Here
\[
 y=2u=z+r,\qquad r=\ell(z),\qquad 0<z<3/8,
\]
and
\[
 P=2t-z(1-z-2r).
\]
Apply (RE) to the second capacity, whose smaller coordinate is \(u\)
and whose slack is \(z-u\):
\[
 t\ge u-K(u)(z-u).
\]
Therefore
\[
 P\ge 2\{u-K(u)(z-u)\}-z(1-z-2r),\qquad u=(z+r)/2.
\]
This expression increases with \(r\). Indeed, at fixed \(z\),
\[
 \frac{d}{du}\{u-K(u)(z-u)\}
 =\frac{10(5-4z)}{(5-4u)^2}>0,
\]
and the remaining contribution to the \(r\)-derivative is \(2z>0\).
Replace \(r\) by \(b(z)\). Exact simplification gives
\[
\boxed{
 P\ge
 \frac{z^2(75-230z+100z^2-16z^3)}{5(25-15z+4z^2)}>0.
}
\]
The cubic in the numerator is decreasing on \([0,3/8]\), with value
\(63/32>0\) at \(3/8\). This treats the whole transition in one calculation.
The former split at \(z=1/4\) and its degree-eight certificate are unnecessary.

### 4.2. Transition B: one rational bound, no subdivision

Write
\[
 v=\ell(u),\qquad z=u+v,\qquad t=v,\qquad0<u\le1/4.
\]
Then
\[
 P=r(1-r)+2v-2u(1-2u).
\]
Since \(z\le3u/2\le3/8\), (RE) applies to the first capacity and gives
\[
 r\ge R(u,v):=u+v-K(u+v)(u-v).
\]
On \(b(u)\le v\le u/2\),
\[
 \frac{\partial R}{\partial v}
 =\frac{10(5-8u)}{(5-4u-4v)^2}>0.
\]
Furthermore,
\[
 R(u,b(u))=\frac{u(25-80u+16u^2)}{(5-2u)(5-4u)}>0,
\]
and \(R(u,v)\le u+v\le3/8\). Thus substituting \(R\) for \(r\), and then
\(b(u)\) for \(v\), can only decrease the expression. We obtain
\[
\boxed{
 P\ge
 \frac{u^2(625+4500u-18400u^2+5440u^3-256u^4)}
 {5(5-2u)^2(5-4u)^2}>0.
}
\]
On \(0\le u\le1/4\), the quartic numerator bracket is at least
\[
 625+4500u-4600u-1=624-100u\ge599.
\]
No split at \(u=1/6\) is needed, and both former degree-six and degree-seven
certificates are removed.

### 4.3. Transition C

Again write \(v=\ell(u)\), \(z=u+v\). Now \(r=\ell(z)\), and
\[
P=2(r+v)-(1-z)(4u-z).
\]
We have \(z\le3u/2\le3/8\). First replace \(r\) by \(b(z)\).
The resulting expression, as a function of \(v\) with \(z=u+v\), has
positive derivative
\[
4+4u-\frac{18}{5}(u+v)>0.
\]
Thus replace \(v\) by \(v_0=b(u)\), and \(z\) by \(z_0=u+v_0\), obtaining
\[
P\ge2\{b(z_0)+v_0\}-(1-z_0)(4u-z_0)
=\frac{u^2}{500}(175+280u-144u^2)>0.
\]

All three transitions are proved. The exhaustive concavity reduction and
the easy regions therefore establish (19) throughout its stated domain.

## 5. Implication (16) and the caliper consequence

Put \(k=y-r\). Since \(0<r\le\min\{1-y,z\}\le y\), we have
\(0\le k<1\). Inequality (19) is
\[
r+t>(1-k)(x-k/2).
\]
Therefore
\[
\begin{split}
r+t+\max\{1/2,1-x(1-k)\}
&\ge r+t+1-x(1-k)\\
&>1-k/2+k^2/2\\
&\ge\sqrt{1-k+k^2}.
\end{split}
\]
The last step follows from
\[
(1-k/2+k^2/2)^2-(1-k+k^2)=k^2(1-k)^2/4\ge0.
\]
This proves (16), strictly.

Combined with the five-point caliper reduction in [2616](2616_bc_d_finite_calipers.md),
this proves that the comparison set \(\{M_0,G_x,G_y,rV_2,tV_4\}\) has minimum equilateral enclosure side
greater than one. The boundary-only five-point forcing, including the possible clipping on $r_4$,
is proved separately in that source. It does not assert that own-ray bounds
control neighboring suppliers at different argument pairs.


## Exact audit and dependency scope

Run `python verify_bc_envelope.py` and `python verify_bc_capacity_calculus.py`
from this directory. They audit identities and rational signs, not the geometric
theorem or the completeness of the analytic reductions. No floating-point
sampling is a proof dependency. The envelope coefficient range is $m\le3/8$;
the global bound $m(1-m)/2$ is retained outside that range.
