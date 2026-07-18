# Exact Rational Certificate for the Mixed Witness Overlaps

Status: Proven

This note replaces the outward-rounded mixed-overlap calculation in Section 7
of [`31034_witness_enclosure_inequality.md`](31034_witness_enclosure_inequality.md).
It proves the same two cap overlaps using exact rational-function algebra and
exact integer Bernstein coefficients. No floating-point or interval arithmetic
is used.

The self-contained verifier is
[`3103X_computation/verify_rational_mixed_overlap.py`](3103X_computation/verify_rational_mixed_overlap.py).
The older outward-rounded verifier is retained only as an independent legacy
audit.

## 1. Domain and notation

Retain the notation of `31032`--`31034`:

$$
p=1-b,
\qquad
q=1-a,
\qquad
s=p+q,
\qquad
m=\min(p,q),
\qquad
M=\max(p,q),
$$

and

$$
\chi=s^4-s^2+mM.
$$

The strict $AB$ domain gives

$$
mM>(1-s)(2-s),
\qquad
m>1-s.
\tag{1}
$$

Since $m\le s/2$, equation (1) implies $s>2/3$. Put

$$
F_m(x)=x^4-x^2+mx-m^2,
\qquad
\kappa=F_m'(s)=4s^3-2s+m.
\tag{2}
$$

Equation (1) gives

$$
\kappa
>
4s^3-3s+1
=
(s+1)(2s-1)^2
>0.
\tag{3}
$$

The exact radial value is

$$
c_*=
\begin{cases}
C_L(m),&\chi\le0,\\[1mm]
\displaystyle\frac{2M}{1+\sqrt{4s^2-3}},&\chi>0,
\end{cases}
\tag{4}
$$

where $C_L(m)$ is the selected root of $F_m$ in $[\sqrt3/2,1]$.

## 2. Branchwise rational upper envelopes

Define

$$
\boxed{
\bar c_L=s-\frac{\chi}{\kappa}
}
\qquad(\chi\le0)
\tag{5}
$$

and

$$
\boxed{
\bar c_T=s-\frac{\chi}{1-m}
}
\qquad(\chi\ge0).
\tag{6}
$$

### Proposition 2.1

On the corresponding radial cells,

$$
\boxed{c_*\le\bar c_L<1},
\qquad
\boxed{c_*\le\bar c_T<1}.
\tag{7}
$$

At $\chi=0$ both bounds equal $s=c_*$.

### Proof on the $C_L(m)$ cell

Here

$$
F_m(s)=\chi\le0,
\qquad
F_m(c_*)=0.
$$

Since $s>2/3$,

$$
F_m''(x)=12x^2-2>0
$$

for $x\ge s$. Thus $F_m$ is increasing and convex from $s$ to the selected
root. Its graph lies above its tangent at $s$, so

$$
0=F_m(c_*)
\ge
F_m(s)+F_m'(s)(c_*-s)
=
\chi+\kappa(c_*-s).
$$

By (3),

$$
c_*\le s-\frac{\chi}{\kappa}=\bar c_L.
\tag{8}
$$

Let $U=1-s$. To prove $\bar c_L<1$, it is enough to prove
$\chi+U\kappa>0$. From (1), $mM>U(1+U)$, and hence

$$
\begin{aligned}
\chi+U\kappa
&=s^4-s^2+mM+U(4s^3-2s+m)\\
&>U\left(m+3s^3-s^2-3s+2\right).
\end{aligned}
\tag{9}
$$

Since $0<U<1/3$,

$$
3s^3-s^2-3s+2
=1-4U+8U^2-3U^3
>1-4U+7U^2>0;
$$

the last quadratic has discriminant $-12$. Thus (9) is positive and
$\bar c_L<1$.

### Proof on the second radial cell

Put

$$
E=\sqrt{4s^2-3},
\qquad
m_0=\frac{s(1-E)}2,
\qquad
M_0=\frac{s(1+E)}2.
$$

Then $m_0+M_0=s$ and $m_0M_0=s^2-s^4$, so

$$
\chi
=mM-m_0M_0
=(m-m_0)(M_0-m).
\tag{10}
$$

Both $m,m_0$ lie in $[0,s/2]$, where $x(s-x)$ is increasing. Hence
$\chi>0$ implies $m>m_0$. Formula (4) gives

$$
s-c_*=\frac{2(m-m_0)}{1+E}.
\tag{11}
$$

Combining (10)--(11),

$$
\frac{\chi}{s-c_*}
=\frac{1+E}{2}(M_0-m)
\le1-m,
$$

because $0\le E\le1$ and $M_0\le1$. Therefore

$$
c_*\le s-\frac{\chi}{1-m}=\bar c_T.
\tag{12}
$$

Also $\chi>0$ gives $\bar c_T<s<1$.

## 3. Rational form after reflection

Reflect so that

$$
z=a-b\ge0,
\qquad
U=a+b-1,
\qquad
s=1-U,
\qquad
m=\frac{s-z}{2}.
\tag{13}
$$

Then

$$
D^2=z^2+6U+3U^2=:K(U,z),
\tag{14}
$$

and

$$
4\chi
=4s^4-3s^2-z^2
=:\Xi(U,z)
=1-10U+21U^2-16U^3+4U^4-z^2.
\tag{15}
$$

Moreover

$$
2\kappa
=8s^3-3s-z
=:G(U,z)
=5-21U+24U^2-8U^3-z.
\tag{16}
$$

Thus

$$
\boxed{
\bar c_L
=1-U-\frac{\Xi(U,z)}{2G(U,z)}
}
\tag{17}
$$

and

$$
\boxed{
\bar c_T
=1-U-\frac{\Xi(U,z)}{2(1+U+z)}.
}
\tag{18}
$$

Both are rational functions of $U,z$; neither contains the quartic root nor
the radial radical $\sqrt{4s^2-3}$.

## 4. Passing to smaller forced disks

Assume, as in the nonautomatic part of `31034`, that $c_*>2/3$. On the active
radial cell let $\bar c$ denote the corresponding value in (17) or (18), and
put

$$
\bar\eta=h(1-\bar c),
\qquad
\bar\tau=h(2\bar c-1),
\qquad
h=\frac{\sqrt3}{2}.
\tag{19}
$$

Proposition 2.1 gives $\bar c\ge c_*$, hence

$$
0<\bar\eta\le\eta=h(1-c_*).
\tag{20}
$$

The Minkowski sum $S$ from `31034` contains

$$
\mathbb D(C,2\eta),
\qquad
\mathbb D(W,\eta),
\qquad
\mathbb D(RA,2\eta),
\qquad W=C+RA.
$$

It therefore also contains the three concentric subdisks obtained by replacing
$\eta$ with $\bar\eta$. It is enough to prove the two mixed cap overlaps for
these smaller disks. The two adjacent overlaps continue to use the original
radius $\eta$ and the analytic proof already given in Section 6 of `31034`.

## 5. Gram reduction of the mixed residuals

Represent a global vector as $(x,hy)$ and put

$$
C'=R^{-1}C,
\qquad
N_A=\lVert A\rVert^2,
\qquad
N_C=\lVert C\rVert^2,
\qquad
u=\langle A,C'\rangle,
$$

$$
\Delta_0=x_Ay_{C'}-y_Ax_{C'}.
\tag{21}
$$

Thus the actual Cartesian determinant satisfies

$$
h^2\Delta_0^2=N_AN_C-\nu^2.
\tag{22}
$$

Write

$$
e=1-\bar c,
\qquad
t=2\bar c-1.
$$

The mixed square residuals for the smaller disks factor as

$$
\boxed{
\bar P_A
=h^2N_AQ_A,
\qquad
Q_A=\Delta_0^2-\lVert tA-eC'\rVert^2,
}
\tag{23}
$$

and

$$
\boxed{
\bar P_C
=h^2N_CQ_C,
\qquad
Q_C=\Delta_0^2-\lVert tC'-eA\rVert^2.
}
\tag{24}
$$

For example, expanding the original $A$ residual and using (22) gives

$$
\begin{aligned}
\frac{\bar P_A}{h^2}
&=(N_A-h^2e^2)\Delta_0^2-(tN_A-e\nu)^2\\
&=N_A\left(\Delta_0^2-t^2N_A-e^2N_C+2te\nu\right),
\end{aligned}
$$

which is (23). The $C$ identity is identical after exchanging the two vectors.
Since $N_A,N_C>0$, it remains to prove

$$
Q_A\ge0,
\qquad
Q_C\ge0.
\tag{25}
$$

The radius estimates in `31034` give
$\lVert A\rVert,\lVert C\rVert>h/2>\eta\ge\bar\eta$, and the ray-order proof
gives the required positive determinant. Consequently (25) implies the two
mixed cap overlaps by the same outer-tangent calculation as in `31034`.

## 6. Exact polynomial reduction

The tangent witnesses $A,C$ are rational functions of $U,z,D$. Substitute
(17) into (23)--(24) on the $L$ cell and (18) on the $T$ cell. The verifier
performs all operations in the exact rational-function field

$$
\mathbb Q(U,z,D).
$$

Each denominator is a positive rational constant times four even powers:

- $(D+3)^4$;
- $G(U,z)^2$ on the $L$ cell or $(1+U+z)^2$ on the $T$ cell;
- the squares of the two cleared Newton-derivative numerators.

Here $D+3>0$, $G=2\kappa>0$ by (3), and $1+U+z>0$. The fixed-line sign lemma
in `31033` proves both Newton derivatives strictly negative throughout the
strict domain. Hence every denominator is strictly positive there.

Reduce the numerator modulo

$$
D^2-K(U,z)=0.
$$

For each branch $B\in\{L,T\}$ and witness $X\in\{A,C\}$, exact polynomial
division gives

$$
\operatorname{num}(Q_{B,X})
=
32(K+3)^2
\left(A_{B,X}(U,z)+D B_{B,X}(U,z)\right),
\tag{26}
$$

where $A_{B,X},B_{B,X}\in\mathbb Z[U,z]$. The exact term counts are

$$
\begin{array}{c|cc}
(B,X)&\#A_{B,X}&\#B_{B,X}\\ \hline
(L,A)&347&298\\
(L,C)&347&298\\
(T,A)&342&294\\
(T,C)&341&294.
\end{array}
\tag{27}
$$

Since $D\ge0$, it suffices to prove all eight integer polynomials in (27)
nonnegative on their respective radial cells.

## 7. Exact integer Bernstein certificate

The reflected strict domain is contained in

$$
0<U<\frac2{\sqrt3}-1<\frac4{25},
\qquad
0\le z<1,
\qquad
K(U,z)<1.
\tag{28}
$$

The verifier starts with the rational rectangle

$$
\mathcal B_0=[0,4/25]\times[0,1].
$$

It converts each target polynomial, together with

$$
g_K(U,z)=1-K(U,z)
$$

and $\Xi(U,z)=4\chi$, from the power basis to the tensor-product Bernstein
basis on $\mathcal B_0$. Every coefficient is then multiplied by a common
positive denominator, so all stored coefficients are integers.

The only subdivision is midpoint de Casteljau subdivision. The implementation
again clears the common power of two, so every descendant coefficient remains
an exact integer. The Bernstein convex-hull property gives the following
rigorous rules for a box:

1. discard it if the largest Bernstein coefficient of $g_K$ is nonpositive;
2. on the $L$ cell, discard it if the smallest coefficient of $\Xi$ is
   positive;
3. on the $T$ cell, discard it if the largest coefficient of $\Xi$ is
   negative;
4. certify it if every Bernstein coefficient of the four relevant target
   polynomials $A_{B,A},B_{B,A},A_{B,C},B_{B,C}$ is nonnegative;
5. otherwise bisect the coordinate with the smaller current dyadic depth.

These rules use only integer additions, multiplications, comparisons, and
binomial coefficients. No approximate root isolation, directed rounding,
floating-point operation, or interval arithmetic occurs.

The deterministic output is

```json
{"arithmetic":"exact_rational_function_and_integer_Bernstein","branches":[{"branch":"L","certified_boxes":43,"maximum_depth_used":19,"processed_boxes":165,"pruned_by_radial_cell":37,"pruned_by_radial_domain":3,"split_boxes":82,"transcript_sha256":"a9f738749a66b74afd19a8ba4fa7f3c8936d5e3428f040ef9bf77d121efc647d","unresolved_boxes":0},{"branch":"T","certified_boxes":43,"maximum_depth_used":19,"processed_boxes":191,"pruned_by_radial_cell":49,"pruned_by_radial_domain":4,"split_boxes":95,"transcript_sha256":"9775745d5147da389f1bf8d1939389cd25e600fbd7b1abcbfcdfd1d691cbd6c1","unresolved_boxes":0}],"certificate":"3103X_exact_rational_mixed_overlaps","core_term_counts":{"L_A":[347,298],"L_C":[347,298],"T_A":[342,294],"T_C":[341,294]},"denominator_factor_counts":{"L_A":4,"L_C":4,"T_A":4,"T_C":4},"result":"PASS","root_rectangle":{"U":[0,"4/25"],"z":[0,1]}}
```

There are no unresolved boxes. Therefore all eight polynomials are
nonnegative on the indicated closed radial cells. Equation (26) proves
$Q_A,Q_C\ge0$ for $z\ge0$. Both inequalities were checked on the same
half-domain; reflection supplies $z\le0$.

Run the certificate from the repository root with

```text
python3 proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/3103X_computation/verify_rational_mixed_overlap.py
```

## 8. Completion

Equations (23)--(25) and the exact certificate prove the two mixed cap
overlaps for the smaller disks. Those disks lie inside the three original
Minkowski disks by (20), so the corresponding original caps overlap as well.
Together with the two analytically proved adjacent overlaps, the five caps
cover the sector from $A$ to $RA$; rotation covers the unit circle. Thus

$$
\Lambda(\widehat K)\ge1,
$$

and the containment from `31034` gives

$$
\boxed{\Lambda(K_{\mathrm{wit}}(a,b))\ge1.}
$$

This completes the witness-enclosure proof without interval arithmetic.
