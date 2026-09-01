# Simplified Finite-Enclosure Proofs: Implementation Report

Branch target: `simplify-finite-enclosure-proofs`

Base: current `main`

## 1. Scope

This update incorporates the proof simplifications obtained from the
enclosing-triangle and numerical audits.  It changes the active proof package
and canonical manuscript.  The changes are mathematical, not merely
editorial:

1. the one-gap all-Vd0 witness is reduced from ten points to seven;
2. the CE2 two-gap root-separation proof is replaced by a short concavity
   argument;
3. the adjacent-Vd radial coefficient improves from `1/4` to `1/3` on the
   actual half-edge domain;
4. the repeated T3-like and Vd1 center-hiding arguments are factored into one
   rescuer-tail theorem;
5. a disk--finite-set caliper theorem records the exact contact structure
   behind disk-plus-points enclosures.

The zero-gap nine-point theorem, the complementary-gap theorem, the
nonadjacent Vd point, the Vd2 perimeter terminal, and the corrected two-chart
replacement are retained.

## 2. Transverse seven-point enclosure

### Old witness

The former one-gap all-Vd0 proof retained

\[
K_{410}
=
\{O,M_0,X(\ell),X(r),P_0,\ldots,P_5\},
\qquad
P_i=(1-C_i)V_i.
\]

A hypothetical C triangle containing all ten points was used to reconstruct
all six radial arms.

### New witness

The active witness is

\[
\boxed{
K_{\rm tr}
=
\{O,M_0,X(\ell),X(r),P_2,P_3,P_4\}.
}
\]

The dependency audit of the direct CE1 proof shows that only the radial data
at \(T_4,T_3,T_2\) are used.  The CE2 proof uses only \(P_4,P_2\).  Hence
\(P_0,P_1,P_5\) are unnecessary.

### Upper squeeze

Give a candidate open unit triangle containing \(K_{\rm tr}\) the signed
variables and put

\[
X=R-\delta,
\qquad
Q=\frac{\eta+\alpha+\delta}{2R}.
\]

Since both actual gap endpoints lie in its open trace,

\[
B_0=\ell>2Q,
\qquad
A_1=1-r>X.
\]

The two boundary endpoints of the actual supercritical role \(T_0\) have
distance at most one:

\[
A_0^2+A_0B_0+B_0^2\le1.
\]

Thus

\[
A_0
\le
\frac{-B_0+\sqrt{4-3B_0^2}}2
<
-Q+\sqrt{1-3Q^2}
<
1-Q.
\]

This argument uses the actual gap endpoint and no radial point at \(r_0\).

### Boundary chain

Every other boundary edge is V-gap-free and
\(T_1,\ldots,T_5\) are nonsupercritical.  Therefore

\[
A_1<A_2<A_3<A_4<A_5<A_0,
\]

and the upper squeeze gives

\[
B_2>Q,
\qquad
B_4>Q.
\]

Containment of the transverse points gives

\[
C_2>1-\delta,
\]

\[
C_3>
1-\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\},
\]

\[
C_4>1-\alpha.
\]

### CE2 return

The signed CE2 calculation gives

\[
X>\epsilon(\alpha),
\qquad
\min\{\epsilon(\alpha),\epsilon(\delta)\}<Q.
\]

If \(\epsilon(\alpha)<Q\), the direct threshold at \(T_4\) gives
\(B_4<Q\).  Otherwise the threshold at \(T_2\) gives \(B_2<Q\).
Both contradict the boundary-chain lower bounds.

### CE1 return

In CE1,

\[
C_4>1-\alpha,
\qquad
C_3>1-\frac{\alpha}{R},
\qquad
C_2>1-\delta.
\]

These are exactly the three radial hypotheses used by the existing CE1
reverse certificate.  Its two selected-chord steps and final threshold imply

\[
A_0>1-Q,
\]

contradicting the endpoint upper squeeze.

Therefore

\[
\boxed{\Lambda(K_{\rm tr})\ge1.}
\]

Since \(K_{\rm tr}\subset K_{410}\), the old enclosure conclusion follows
immediately.

## 3. Short CE2 two-gap proof

Put

\[
p=W-\alpha,
\qquad
q=R-\delta,
\qquad
e=\min\{\alpha,\delta\},
\qquad
M=\max\{R,W\}.
\]

The two strict CE2 inequalities imply

\[
P>(1+M)e.
\]

Since \(E^2=1-M+M^2\),

\[
(1+M)^2-(3M-1)^2E^2
=
3M(1-M)(3M^2-2M+3)>0.
\]

Thus

\[
\eta=P/E>(3M-1)e.
\]

Using \(RW=\eta+P\) in the two CE2 inequalities yields

\[
p,q>3e.
\]

Since \(p+q\le1-2e\),

\[
\boxed{3e<p,q<1-5e.}
\]

Also

\[
e<\frac{P}{1+M}
\le\frac{2\sqrt3-3}{6}<\frac1{12}.
\]

Set \(c=1-e\) and

\[
f_c(t)=c^4-c^2+ct-t^2.
\]

The function is concave, and

\[
f_c(3e)=e(1-7e-4e^2+e^3)>0,
\]

\[
f_c(1-5e)=e(2-15e-4e^2+e^3)>0.
\]

Therefore \(f_c(p),f_c(q)>0\).  Together with
\(p+c,q+c>1\) and \(c>p+q\), the exact four local support-contact lengths are
all greater than one.  Hence

\[
\boxed{c_{\max}(p,q)<1-e.}
\]

This removes the former roots \(t_\pm\), the auxiliary point
\((1+\sqrt3)e\), and the cubic \(B(e)\).

The theorem closes every two-gap all-Vd0 or T3-like row, for
\(N_+\in\{0,1\}\), and the rank-two output of the Vd1 replacement.

## 4. Half-edge one-third radial envelope

On the adjacent-Vd domain,

\[
M\ge\frac12,
\qquad
0<m\le M,
\qquad
M+m<1.
\]

The new bound is

\[
\boxed{
c_{\max}(M,m)<1-\frac m3.
}
\]

For \(m\le3/8\), the selected \(L\)-polynomial at
\(c_0=1-m/3\) is

\[
F_L(c_0)
=
\frac m{81}(m^3-12m^2-63m+27)>0.
\]

At the \(L/T\) transition the roots agree.  On the \(T\) sheet,

\[
c_T(s)=
\frac{2(s-m)}{1+\sqrt{4s^2-3}}
\]

decreases with \(s\), because

\[
c_T'(s)
=
\frac{2(\sqrt{4s^2-3}+4ms-3)}
{\sqrt{4s^2-3}(1+\sqrt{4s^2-3})^2}
<0.
\]

For \(m\ge3/8\), the selector is uniformly positive and only the \(T\) sheet
occurs; its maximum is at \(M=1/2\) and is at most \(4/5\).

In the adjacent Vd placement,

\[
M=\frac12+\rho_R,
\qquad
m=\rho_L,
\]

so

\[
C_2
<
1-\frac{\rho_L}{3}
<
1-\delta
\]

using the already proved stronger residual estimate
\(4\delta<\rho_L\).  This replaces the former quarter coefficient.

## 5. Common rescuer-tail budget

Both the one-gap T3-like proof and the Vd1 neighboring-midpoint proof have the
same global mechanism.

Suppose the special role has boundary endpoint \(a\), supported interval
\([c,u]\subset r_1\), and center-forced O-side endpoint

\[
\varepsilon V_1,
\qquad
\varepsilon=1-u.
\]

Let \(M=M_c^{\rm sup}\).  Assume

\[
a+\varepsilon\le1,
\qquad
a\le1-M,
\qquad
\frac{a}{a+\varepsilon}\le1-M.
\]

If the companion center trace does not hide \(a\), the remaining far tail is
at least \(1-a\ge M\).  If it does hide \(a\), then

\[
k/W\le a,
\qquad
\delta/R\ge\varepsilon,
\]

so

\[
Wa\ge k>\alpha+R\varepsilon
\]

and

\[
R+\alpha
<
\frac{a}{a+\varepsilon}
\le1-M.
\]

The far tail is again at least \(M\).  The adjacent supercritical role has
outgoing reach below \(M\), and the four ordinary edge-cover inequalities
sum to more than four, contrary to nonsupercriticality.

The T3-like and Vd1 proofs now contain only their distinct local verification
of the two displayed inequalities; the center-hiding and path sum are stated
once.

## 6. Disk--finite-set calipers

For a centered disk and finitely many points, a minimizing orientation is
either:

- disk-only;
- a point--point support tie;
- a point--disk tangent tie.

On every open support-source cell containing an active point, the support sum
has the form

\[
q\eta+\langle v,n(\theta)\rangle
\]

with positive last term, and therefore has negative second derivative.
A minimum lies on a tie boundary.

This theorem supplies an exact finite contact interpretation for disk-plus-two
and disk-plus-three-point configurations.  It is retained as a general
finite-enclosure tool, although the active \(K_{\rm tr}\) proof is stronger
and simpler than a disk compression.

## 7. Files changed

### Proof authority

- `proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2609_simplified_finite_enclosure_lemmas.md`
- `proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2600_minimum_enclosing_triangle_tools.md`
- `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4103_transverse_seven_point_enclosure.md`
- `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4101_new_all_Vd0_finite_enclosure.md`
- `proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md`
- `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md`

### Canonical paper

- `arrange/paper_draft/06_finite_enclosure_full.tex`
- `arrange/paper_draft/06i_simplified_finite_enclosure_interfaces.tex`
- `arrange/paper_draft/06c_exceptional_direct_terminals.tex`
- `arrange/paper_draft/figures/finite_enclosure/fe00_case_roadmap.tex`
- `arrange/paper_draft/figures/finite_enclosure/fe05_k410_actual_reach.tex`

The canonical PDF and the interactive dependency graph are rebuilt after the
source commit.
