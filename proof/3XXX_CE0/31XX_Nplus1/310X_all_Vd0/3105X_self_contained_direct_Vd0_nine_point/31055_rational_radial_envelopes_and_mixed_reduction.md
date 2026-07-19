# Rational Radial Envelopes and Exact Mixed-Overlap Reduction

Status: Proven

This note replaces the exact radial value in the two mixed cap overlaps from
[`31054_four_cap_enclosure_reduction.md`](31054_four_cap_enclosure_reduction.md)
by branchwise rational upper envelopes.  It then factors the mixed Gram
residuals and reduces them exactly to eight integer-polynomial signs.  The
eight signs are proved in
[`31056_global_analytic_mixed_positivity.md`](31056_global_analytic_mixed_positivity.md).

## 1. Domain and exact radial cells

Assume

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1.
\tag{1}
$$

Put

$$
p=1-b,
\qquad
q=1-a,
\qquad
s=p+q,
$$

$$
m=\min\{p,q\},
\qquad
M=\max\{p,q\},
\qquad
\chi=s^4-s^2+mM.
$$

Writing $U=a+b-1=1-s$, the last inequality in (1) is equivalent to

$$
mM>(1-s)(2-s)=U(1+U).
\tag{2}
$$

Since $M<1$, equation (2) implies

$$
m>1-s.
\tag{3}
$$

As $m\le s/2$, equation (3) also gives $s>2/3$.  Define

$$
F_m(x)=x^4-x^2+mx-m^2,
$$

$$
\kappa=F_m'(s)=4s^3-2s+m.
\tag{4}
$$

Equation (3) yields

$$
\kappa
>
4s^3-3s+1
=(s+1)(2s-1)^2
>0.
\tag{5}
$$

The exact radial envelope from
[`2004_admissible_set.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md)
is

$$
c_*=
\begin{cases}
C_L(m),&\chi\le0,\\[1mm]
\displaystyle\frac{2M}{1+\sqrt{4s^2-3}},&\chi>0,
\end{cases}
\tag{6}
$$

where $C_L(m)$ is the selected root of $F_m$ in $[\sqrt3/2,1]$.

## 2. Rational upper envelopes

Define

$$
\boxed{
\bar c_L=s-\frac\chi\kappa
}
\qquad(\chi\le0),
\tag{7}
$$

and

$$
\boxed{
\bar c_T=s-\frac\chi{1-m}
}
\qquad(\chi\ge0).
\tag{8}
$$

### Proposition 2.1

On the corresponding radial cells,

$$
c_*\le\bar c_L<1,
\qquad
c_*\le\bar c_T<1.
\tag{9}
$$

At $\chi=0$, both bounds equal $s=c_*$.

### Proof on the quartic cell

Here $F_m(s)=\chi\le0$ and $F_m(c_*)=0$.  For $x\ge s>2/3$,

$$
F_m''(x)=12x^2-2>0.
$$

Convexity and (5) give

$$
0=F_m(c_*)
\ge
F_m(s)+F_m'(s)(c_*-s),
$$

and therefore

$$
c_*\le s-\frac\chi\kappa=\bar c_L.
\tag{10}
$$

To prove $\bar c_L<1$, it is enough to prove $\chi+U\kappa>0$.  By (2),

$$
\begin{aligned}
\chi+U\kappa
&=s^4-s^2+mM+U(4s^3-2s+m)\\
&>U\left(m+3s^3-s^2-3s+2\right).
\end{aligned}
$$

For $0<U<1/3$,

$$
3s^3-s^2-3s+2
=1-4U+8U^2-3U^3
>1-4U+7U^2>0.
$$

The last quadratic has negative discriminant.  Hence $\chi+U\kappa>0$ and
$\bar c_L<1$.

### Proof on the radical cell

Put

$$
E=\sqrt{4s^2-3},
\qquad
m_0=\frac{s(1-E)}2,
\qquad
M_0=\frac{s(1+E)}2.
$$

Then $m_0+M_0=s$, $m_0M_0=s^2-s^4$, and

$$
\chi
=mM-m_0M_0
=(m-m_0)(M_0-m).
\tag{11}
$$

Both $m$ and $m_0$ lie in $[0,s/2]$, where $x(s-x)$ is increasing.
Therefore $\chi>0$ implies $m>m_0$.  Formula (6) gives

$$
s-c_*=\frac{2(m-m_0)}{1+E}.
\tag{12}
$$

Combining (11)--(12),

$$
\frac\chi{s-c_*}
=
\frac{1+E}{2}(M_0-m)
\le1-m,
$$

because $0\le E\le1$ and $M_0\le1$.  Thus

$$
c_*\le s-\frac\chi{1-m}=\bar c_T.
\tag{13}
$$

Also $\chi>0$ gives $\bar c_T<s<1$.  This proves Proposition 2.1.
$\square$

## 3. Rational form after reflection

Reflect so that

$$
z=a-b\ge0,
\qquad
U=a+b-1.
$$

Then

$$
s=1-U,
\qquad
m=\frac{1-U-z}{2},
$$

$$
D^2=z^2+6U+3U^2=:K(U,z).
\tag{14}
$$

Direct expansion gives

$$
4\chi
=
1-10U+21U^2-16U^3+4U^4-z^2
=:\Xi(U,z),
\tag{15}
$$

and

$$
2\kappa
=
5-21U+24U^2-8U^3-z
=:G(U,z).
\tag{16}
$$

Consequently

$$
\boxed{
\bar c_L
=1-U-\frac{\Xi(U,z)}{2G(U,z)}
},
\tag{17}
$$

$$
\boxed{
\bar c_T
=1-U-\frac{\Xi(U,z)}{2(1+U+z)}
}.
\tag{18}
$$

Neither expression contains the selected quartic root or the radial radical
$\sqrt{4s^2-3}$.

## 4. Smaller forced disks and exact Gram factors

Assume $c_*>2/3$, since the complementary region is automatic in `31054`.
On the active cell, let $\bar c$ denote (17) or (18), and put

$$
\bar\eta=h(1-\bar c),
\qquad
e=1-\bar c,
\qquad
t=2\bar c-1,
\qquad
\bar\tau=ht.
\tag{19}
$$

Proposition 2.1 gives

$$
0<\bar\eta\le\eta=h(1-c_*).
\tag{20}
$$

Thus the Minkowski sum from `31054` contains the three concentric subdisks

$$
\mathbb D(C,2\bar\eta),
\qquad
\mathbb D(W,\bar\eta),
\qquad
\mathbb D(RA,2\bar\eta).
\tag{21}
$$

It is enough to prove both mixed cap overlaps for these smaller disks.

Represent a global vector as $(x,hy)$ and put

$$
C'=R^{-1}C,
\qquad
N_A=\left\lVert A\right\rVert^2,
\qquad
N_C=\left\lVert C\right\rVert^2,
$$

$$
\nu=\langle A,C'\rangle,
\qquad
\Delta_0=x_Ay_{C'}-y_Ax_{C'}.
\tag{22}
$$

The Gram identity is

$$
h^2\Delta_0^2=N_AN_C-\nu^2.
\tag{23}
$$

The two mixed square residuals for the smaller disks are, explicitly,

$$
\bar P_A
=
(N_A-\bar\eta^2)h^2\Delta_0^2
-(\bar\tau N_A-\bar\eta\nu)^2,
$$

$$
\bar P_C
=
(N_C-\bar\eta^2)h^2\Delta_0^2
-(\bar\tau N_C-\bar\eta\nu)^2.
$$

They are exactly the residuals in equation (24) of the preceding reduction
with $\eta$ replaced by $\bar\eta$.  Exact expansion followed by (23) gives

$$
\boxed{
\bar P_A=h^2N_AQ_A,
\qquad
Q_A=\Delta_0^2-\left\lVert tA-eC'\right\rVert^2,
}
\tag{24}
$$

and

$$
\boxed{
\bar P_C=h^2N_CQ_C,
\qquad
Q_C=\Delta_0^2-\left\lVert tC'-eA\right\rVert^2.
}
\tag{25}
$$

For example,

$$
\begin{aligned}
\frac{\bar P_A}{h^2}
&=(N_A-h^2e^2)\Delta_0^2-(tN_A-e\nu)^2\\
&=N_A\left(
\Delta_0^2-t^2N_A-e^2N_C+2te\nu
\right),
\end{aligned}
$$

which is (24).  Equation (25) is the same identity with the two vectors
exchanged.  Since $N_A,N_C>0$, it remains to prove

$$
Q_A\ge0,
\qquad
Q_C\ge0.
\tag{26}
$$

The radius and determinant proof in `31054` applies a fortiori to the
smaller radius $\bar\eta$.  Hence (26) gives the two mixed overlaps in (21).

## 5. Exact eight-polynomial reduction

The Newton witnesses $A,C$ are rational functions of $U,z,D$.  Substitute
(17) into (24)--(25) on the $L$ cell and (18) on the $T$ cell.  Work in the
exact rational-function field

$$
\mathbb Q(U,z,D).
$$

Every denominator is a positive rational constant times the product of

- $(D+3)^4$;
- $G(U,z)^2$ on the $L$ cell, or $(1+U+z)^2$ on the $T$ cell; and
- the squares of the two cleared Newton-derivative numerators.

These factors are strictly positive.  Indeed $D+3>0$,
$G(U,z)=2\kappa>0$ by (5), and $1+U+z>0$.  The fixed-line theorem
[`31052_fixed_line_circle_signs.md`](31052_fixed_line_circle_signs.md)
proves that both Newton derivatives are strictly negative throughout the
strict domain, so their cleared numerators are nonzero.

Reduce each numerator modulo

$$
D^2-K(U,z)=0.
$$

For each radial branch $B\in\{L,T\}$ and outer witness $X\in\{A,C\}$,
exact polynomial division gives

$$
\boxed{
\mathrm{num}(Q_{B,X})
=
32(K+3)^2
\left(
A_{B,X}(U,z)+D B_{B,X}(U,z)
\right),
}
\tag{27}
$$

where $A_{B,X},B_{B,X}\in\mathbb Z[U,z]$.  The exact term counts are

| $(B,X)$ | Terms in $A_{B,X}$ | Terms in $B_{B,X}$ |
|---|---:|---:|
| $(L,A)$ | 347 | 298 |
| $(L,C)$ | 347 | 298 |
| $(T,A)$ | 342 | 294 |
| $(T,C)$ | 341 | 294 |

The package-local symbolic checker
[`verify_mixed_overlap_core_derivation.py`](3105X_computation/verify_mixed_overlap_core_derivation.py)
performs the substitutions, clears the displayed positive denominators,
reduces by $D^2-K$, derives all eight integer polynomials, and compares them
coefficient by coefficient with the canonical transcript.  Thus (27) is an
exact symbolic identity, not a numerical reconstruction.

Since $D\ge0$ and every omitted factor is positive, the two mixed targets
reduce to

$$
\boxed{
A_{B,X}(U,z)\ge0,
\qquad
B_{B,X}(U,z)\ge0
}
\tag{28}
$$

for $B\in\{L,T\}$ and $X\in\{A,C\}$.  Reflection supplies $z\le0$ after
the eight signs for the reflected half-domain have been proved.  This is the
claimed exact eight-polynomial reduction. $\square$
