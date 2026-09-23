# Elementary radial envelope and coupled BC capacity inequality

Status: Proven

The exact local admissible-set theorem and its connected-component selector
are inputs from [2004](../20XX_V_triangle_geometry/2004_admissible_set.md).
Common-pair domination and antitonicity are proved in
[2008b](../20XX_V_triangle_geometry/2008b_direct_neighbor_domination.md).
The geometric five-point threshold and original-cover forcing remain
separate in [2616](2616_bc_d_finite_calipers.md). The accompanying
`verify_quarter_envelope_revision.py` audits identities, signs, and source
contracts; its rational samples are diagnostics, not a universal proof.
The wider-range envelope remains separately proved in
[2615a](2615a_wide_range_slack_envelope.md), not as an active dependency.

Throughout,

\[
h=\sqrt3/2,\qquad f(a,b)=1-c_{\max}(a,b),\qquad a,b\ge0,\quad a+b\le1.
\]

Write \(m=\min(a,b)\), \(\delta=1-a-b\). The inherited common-pair
bound gives \(0\le f(a,b)\le m\). Increasing either prescribed anchor
increases the deficit. No neighboring-ray exclusion is replaced by this local
calculation.

## 1. Local deficit bounds

Let \(c(m)\in[h,1]\) be the unique root of

\[
F(c,m)=c^4-c^2+mc-m^2=0,\qquad \ell(m)=1-c(m).
\]

Uniqueness follows from \(F_c>0\) on \([h,1]\), while
\(F(h,m)=-(m-h/2)^2\le0\) and \(F(1,m)=m(1-m)\ge0\).
The existing diagonal-capacity argument gives \(f(a,b)\ge\ell(m)\):
for \(m\le h/2\), the diagonal pair lies in the quartic cell and
\(c_{\max}(a,b)\le c_{\max}(m,m)=c(m)\); for \(m\ge h/2\),
antitonicity gives \(c_{\max}(a,b)\le c_{\max}(h/2,h/2)=h\le c(m)\).

### 1.1. The shared quadratic lower bound

For \(0\le m\le1/2\), put \(q(m)=m(1-m)/2\). Then

\[
\boxed{q(m)\le\ell(m)\le f(a,b)\le m.}
\]

Indeed, the root equation and an elementary factorization give

\[
\ell c^2(1+c)=m(c-m),
\]
\[
2(c-m)-(1-m)c^2(1+c)
=(1-c)\bigl((1-m)c(c+2)-2m\bigr)\ge0.
\]

The bracket is positive because \(c\ge h>3/4\), \(m\le1/2\), and

\[
(1-m)c(c+2)-2m\ge\tfrac12\cdot\tfrac34\cdot\tfrac{11}4-1=\tfrac1{32}.
\]

Division by \(c^2(1+c)>0\) proves the claim; \(m=0\) is immediate.

### 1.2. A stronger small-range baseline

For \(0\le m\le1/4\), define

\[
\beta(m)=\frac{2m}{4+3m},\qquad \kappa(m)=1+\frac32m.
\]

Then \(\beta(m)\le\ell(m)\). To prove this, put

\[
B(m)=81m^4+405m^3+656m^2+272m-128.
\]

Direct substitution gives

\[
F(1-\beta(m),m)=-\frac{m^2B(m)}{(4+3m)^4}.
\]

The polynomial \(B\) is increasing on \([0,1/4]\), and
\(B(1/4)=-3163/256<0\). Moreover,
\(1-\beta(m)\ge17/19>h\). Since \(F_c>0\), the substitution
implies \(1-\beta(m)\ge c(m)\).

For comparison with the former bounds,

\[
\beta(m)-q(m)=\frac{m^2(3m+1)}{2(3m+4)}\ge0,
\]
\[
\beta(m)-\left(\frac m2-\frac25m^2\right)
=\frac{m^2(12m+1)}{10(3m+4)}\ge0.
\]

These comparisons are used only on the stated common domain. In particular,
this does not extend the new baseline beyond \(m=1/4\).

## 2. The affine-slope slack envelope

For \(m\le1/4\), one has

\[
\boxed{
f(a,b)\ge\max\left\{\beta(m),\ m-\kappa(m)\delta\right\}.
}
\tag{E}
\]

The two expressions meet at \(\delta=\beta(m)\), since
\(m-\kappa(m)\beta(m)=\beta(m)\). For \(\delta\ge\beta(m)\),
the baseline already proves (E). The case \(m=0\) is immediate.

Suppose now \(m>0\) and \(0<\delta\le\beta(m)\). Put
\(M=1-m-\delta\). The coordinates remain ordered, and
\(1-\delta\ge1-\beta(m)\ge c(m)\). Thus the inherited selected
triangular capacity branch applies. It is the smaller root of

\[
H(C)=\bigl((1-\delta)^2-1\bigr)C^2+MC-M^2.
\]

Test \(\overline C=1-m+\kappa(m)\delta\). Exact expansion yields

\[
H(\overline C)=\frac\delta4N_m(\delta),
\]
where
\[
\begin{split}
N_m(\delta)={}&(3m+2)^2\delta^3-10m(3m+2)\delta^2\\
&+(28m^2-22m-20)\delta+14m(1-m).
\end{split}
\]

This cubic decreases on the entire testing interval. In fact,
\(m\le1/4\) and \(\delta\le\beta(m)\le m/2\le1/8\), so

\[
\begin{split}
N'_m(\delta)
&=3(3m+2)^2\delta^2-20m(3m+2)\delta+28m^2-22m-20\\
&\le3(11/4)^2(1/8)^2+7/4-20=-18325/1024<0.
\end{split}
\]

At its right endpoint,

\[
N_m(\beta(m))=-\frac{2mB(m)}{(4+3m)^3}>0.
\]

Consequently \(H(\overline C)>0\). The quadratic is concave in \(C\),
and the capacity is its selected smaller root, so
\(c_{\max}(M,m)<\overline C\). This proves the affine lower bound in
(E). At \(\delta=0\), the exact capacity is \(1-m\), giving equality.

This proof uses neither implicit differentiation of \(c(m)\) nor a radical
second derivative. The selected smaller-root input is essential: the sign of
an unrestricted polynomial alone is not a geometric capacity definition.

## 3. The coupled inequality: statement and radius monotonicity

Suppose

\[
0<x\le y<1,\qquad x/2\le z\le y,
\]
and retain the exact capacity radii
\[
r=f(1-y,z),\qquad t=f(1-z,x/2).
\]
Then
\[
\boxed{2(r+t)>(1-y+r)(2x-y+r).}
\tag{BC}
\]

Put \(u=x/2\) and
\[
P(y,r,t)=2(r+t)-(1-y+r)(4u-y+r).
\]
The domain is \(0<u\), \(2u\le y<1\), \(u\le z\le y\), and
\(0<r,t\le1/2\). At fixed \(u,y\),
\[
P_r=1-4u+2y-2r\ge1-2r\ge0,\qquad P_t=2.
\]
Thus lower bounds on the radii can be substituted. The proof below concerns
comparison values inside this inequality. The active witness radii do not
change, and no assertion that the corresponding point sets are nested is used.

## 4. Easy regions using only the shared bound

### 4.1. The region \(y\ge1/2\)

Put \(a=1-y\), so \(0<a\le1/2\), \(u\le(1-a)/2\), and
\(u\le z\le1-a\).

If \(z\ge a\) and \(z\le1-u\), substitute \(q(a),q(u)\).
The expression is concave in \(u\); at \(u=0\) it is
\(2q(a)+(a+q(a))(1-a-q(a))>0\), and at \(u=(1-a)/2\) it is
\((1-a)^3(1+a)/4>0\).

If \(z\ge a\) and \(z\ge1-u\), both radii are at least \(q(a)\):
indeed \(a\le1-z\le u\le1/2\), and \(q\) is increasing on this
interval. After substitution the expression decreases with \(u\), and its
value at \(u=(1-a)/2\) is \(a(1-a)(a^2-a+2)/4>0\).

If \(z\le a\), both radii are at least \(q(u)\). The resulting
expression is concave in \(a\) on
\(u\le a\le\min(1/2,1-2u)\). Its endpoints are

| Endpoint | Value | Parameter interval |
|---|---|---|
| \(a=u\) | \(u(14-43u+14u^2-u^3)/4\) | \(0<u\le1/3\) |
| \(a=1/2\) | \((1-17u^2+10u^3-u^4)/4\) | \(0<u\le1/4\) |
| \(a=1-2u\) | \(u(-u^3+2u^2+9u-2)/4\) | \(1/4\le u\le1/3\) |

The three polynomial brackets respectively decrease to \(32/27\), decrease
to \(23/256\), and increase from \(23/64\). All are positive.

### 4.2. The region \(y\le1/2,\ z\ge2u\)

Substitute \(q(z),q(u)\). The resulting expression increases with \(y\),
so set \(y=z\). It is concave in \(u\in[0,z/2]\). Its value at zero
is positive, and at \(u=z/2\) it is \(z^3(2-z)/4>0\).

### 4.3. The improved cutoff: \(y\le1/2,\ 1/4\le z\le2u\)

Substitute \(q(z),q(u)\) and reduce \(y\) to \(2u\). Then
\[
P\ge q(z)(1-q(z))-u+3u^2.
\]
Because \(q(z)(1-q(z))\) increases on \([1/4,1/2]\), and
\(-u+3u^2=3(u-1/6)^2-1/12\),
\[
\boxed{P\ge\frac3{32}\frac{29}{32}-\frac1{12}=\frac5{3072}>0.}
\]

This is the step that permits a small-range envelope on \(m\le1/4\).
The former cutoff \(1/3\) is unnecessary.

## 5. The remaining region has elementary switches

It remains to consider
\[
0<u\le1/4,\qquad u\le z\le\min(2u,1/4),\qquad 2u\le y\le1/2.
\]
The smaller coordinates of the two capacity pairs are \(z\) and \(u\).
Use (E) to replace the radii by
\[
R_0=\max\{\beta(z),\ z-\kappa(z)(y-z)\},\qquad
T_0=\max\{\beta(u),\ u-\kappa(u)(z-u)\}.
\]
Put \(g(v)=v+\beta(v)\). This is an explicit rational function, with
\(g'>0\). The only switches are \(y=g(z)\) and \(z=g(u)\).

### 5.1. Reduction in \(y\)

On the affine branch of \(R_0\),
\[
\frac{d^2}{dy^2}P(y,R_0,T_0)=-2(1+\kappa(z))^2<0.
\]
On the baseline branch,
\[
\frac d{dy}P(y,\beta(z),T_0)=1+4u+2\beta(z)-2y>0.
\]
Since \(g(z)\le g(1/4)=27/76<1/2\), it suffices to check
\(y=2u\) and the switch \(y=g(z)\) whenever it belongs to the domain.

### 5.2. Reduction on \(y=2u\)

Here
\[
P=R_0(1-R_0)+2T_0-2u(1-2u).
\]
Split the \(z\)-interval at \(g(z)=2u\) and \(z=g(u)\).
On each piece, \(T_0\) is affine or constant. The function
\(\beta(z)(1-\beta(z))\) is concave because \(\beta\) is concave
and \(v(1-v)\) is increasing and concave on \([0,1/2]\).

On the other branch,
\[
R=z-\kappa(z)(2u-z)=2z+\frac32z^2-2u-3uz,
\]
so \(R'=2+3z-3u\ge2\), \(R''=3\). Wherever this branch is active,
\(0<R\le z\le1/4\), and
\[
(R(1-R))''=3(1-2R)-2(R')^2\le-5<0.
\]
Thus \(P\) is concave on every piece. At \(z=u\), its value is
\(\beta(u)(1-\beta(u))+4u^2>0\). At \(z=2u\), its value is
\(2T_0>0\). The artificial endpoint \(z=1/4\) is covered by Section 4.3,
since the comparison radii are at least the corresponding \(q\)-bounds.
Only the two switches remain.

### 5.3. Reduction on \(y=g(z)\)

Here
\[
P=2\beta(z)+2T_0-(1-z)(4u-z),\qquad z/2\le u\le g(z)/2.
\]
On the baseline branch \(T_0=\beta(u)\), its derivative in \(u\) is
\[
\frac{16}{(4+3u)^2}-4(1-z)\le-2<0.
\]
On the other branch \(T_0=u-\kappa(u)(z-u)\), the derivative is simply
\[
\boxed{6u+z>0.}
\]
The minimum is therefore at an endpoint or at \(z=g(u)\). The endpoints
are the already checked \(z=2u\) case and the first transition below.
The ordering of the two switches need not be assumed; coincident switches
are included.

## 6. Three short transition checks

### A. \(y=2u=g(z)\)

Use the affine entry as a lower bound for \(T_0\), regardless of which
entry is active. Direct substitution gives
\[
P\ge\frac{z^2(9z^2+36z+44)}{4(3z+4)^2}>0.
\]

### B. \(y=2u,\ z=g(u)\)

Here \(T_0=\beta(u)\). The affine entry of \(R_0\) is \(R_B\), and
\[
R_B-u(1-2u)=\frac{u^2(9u^2+6u+4)}{2(3u+4)^2}>0.
\]
Since \(v(1-v)\) increases on \([0,1/2]\),
\[
P\ge\frac{u^2(1+19u-4u^2-12u^3)}{3u+4}>0.
\]
Indeed, \(4u^2+12u^3\le7/16\) for \(u\le1/4\). No sixth-degree
transition polynomial is needed.

### C. \(y=g(z),\ z=g(u)\)

Both radii are at their baseline switches. Substitution yields
\[
P=\frac{3u^2(81u^4+441u^3+768u^2+460u+48)}
{(3u+2)(3u+4)^2(3u+8)}>0.
\]
All numerator coefficients and denominator factors are positive.

Sections 4--6 cover the entire parameter domain and prove (BC).

## 7. Return to the unchanged geometric threshold

With \(k=y-r\), (BC) gives
\[
r+t>(1-k)(x-k/2).
\]
Therefore
\[
r+t+\max\{1/2,1-x(1-k)\}>1-k/2+k^2/2
\ge\sqrt{1-k+k^2},
\]
where the last squared difference is \(k^2(1-k)^2/4\).
Apply the existing capacity-free five-point threshold.

The exact original-cover radii remain
\[
r=f(1-y,z),\quad t=f(1-z,x/2),\quad \widehat t=\min(t,A_3).
\]
The clipping exit, singleton gaps, actual-versus-selected distinction, and
neighboring-supplier exclusions are unchanged. The old envelope on
\(m\le3/8\) remains a valid separate result; this active proof no longer
requires it and does not claim the new envelope has that wider domain.
