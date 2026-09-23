# Wider-range slack envelope (independent retained result)

Status: Proven

This source preserves the former local-calculus proof of the envelope on
$m\le3/8$. It is not used by the active coupled BC proof in
[2615](2615_slack_sensitive_radial_envelope.md), which needs only $m\le1/4$
and uses a stronger bound there. The two ranges are not identified.
Here $f(a,b)=1-c_{\max}(a,b)$, $a,b\ge0$, $a+b\le1$; the exact selected
own-ray formula is [2004](../20XX_V_triangle_geometry/2004_admissible_set.md),
and antitonicity and $f\le\min(a,b)$ are supplied by
[2008b](../20XX_V_triangle_geometry/2008b_direct_neighbor_domination.md).
The retained `verify_bc_envelope.py` and `verify_bc_capacity_calculus.py`
audit this older local algebra, not the new active quarter-range proof.

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
