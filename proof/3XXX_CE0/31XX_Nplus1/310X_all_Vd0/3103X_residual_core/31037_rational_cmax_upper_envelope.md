# Rational Upper Envelope for the Radial Core

Status: Exploratory. The upper-envelope lemma below is proved, but the final
mixed-overlap inequalities have not yet been replaced analytically. This note
is not a dependency of the current proof; the outward-rounded certificate in
[`31034_witness_enclosure_inequality.md`](31034_witness_enclosure_inequality.md)
remains authoritative.

## 1. Objective

The only computer-assisted step in `31034` proves the two mixed cap overlaps
for the exact radial value

$$
c_*=c_{\max}(p,q).
$$

The exact formula for $c_*$ changes radial sheets and introduces either a
selected quartic root or the radical $\sqrt{4s^2-3}$. This note records a
single upper envelope for $c_*$ that is rational in the reflected variables
$(U,z)$. Replacing the forced disk by the smaller disk associated with this
upper envelope may turn the remaining mixed overlaps into exact polynomial
inequalities in $U,z,D$, where

$$
D^2=z^2+6U+3U^2.
$$

The structural radical $D$ already occurs in the tangent witnesses; the point
of the reduction is to remove the separate radial-sheet algebra.

## 2. Domain and notation

Retain the notation of `31032` and `31034`:

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

Since $m\le s/2$, equation (1) implies $s>2/3$.

Put

$$
F_m(x)=x^4-x^2+mx-m^2,
\qquad
\kappa=F_m'(s)=4s^3-2s+m.
\tag{2}
$$

Equation (1) gives the useful strict sign

$$
\kappa
>
4s^3-3s+1
=
(s+1)(2s-1)^2
>0.
\tag{3}
$$

## 3. A single upper envelope on both radial sheets

Define

$$
\boxed{
\widetilde c
=
s-\frac{\chi}{4s^3-2s+m}.
}
\tag{4}
$$

### Proposition 3.1

Throughout the strict $AB$ domain,

$$
\boxed{c_*\le \widetilde c<1.}
\tag{5}
$$

At the radial-sheet boundary $\chi=0$, equality holds:
$c_*=\widetilde c=s$.

### Proof on the $C_L(m)$ sheet

Suppose $\chi\le0$. Since

$$
F_m(s)=s^4-s^2+ms-m^2=\chi,
$$

while $F_m(1)=m(1-m)>0$, the selected root $c_*$ lies in $[s,1]$.
Moreover,

$$
F_m''(x)=12x^2-2>0
$$

for $x\ge s>2/3$. Thus $F_m$ is increasing and strictly convex from $s$
to $c_*$. Its graph lies above the tangent line at $s$, so

$$
0=F_m(c_*)
\ge
F_m(s)+F_m'(s)(c_*-s)
=
\chi+\kappa(c_*-s).
$$

Using (3) gives

$$
c_*
\le
s-\frac{\chi}{\kappa}
=
\widetilde c.
\tag{6}
$$

Thus (4) is the zero of the tangent line to the quartic at $s$, or one
Newton upper step taken from $s$.

### Proof on the other radial sheet

Suppose $\chi>0$ and put

$$
E=\sqrt{4s^2-3},
\qquad
m_0=\frac{s(1-E)}2,
\qquad
M_0=\frac{s(1+E)}2.
$$

Then $m_0+M_0=s$ and

$$
m_0M_0=s^2-s^4.
$$

Consequently

$$
\chi
=mM-m_0M_0
=(m-m_0)(M_0-m).
\tag{7}
$$

Both $m$ and $m_0$ lie in $[0,s/2]$, where $x(s-x)$ is increasing, so
$\chi>0$ implies $m>m_0$. The exact second-sheet formula gives

$$
c_*=\frac{2M}{1+E},
\qquad
s-c_*=\frac{2(m-m_0)}{1+E}.
\tag{8}
$$

Using $E^2=4s^2-3$, equation (2) becomes

$$
\kappa=s(1+E^2)+m.
$$

A direct calculation gives

$$
\begin{aligned}
2\kappa-(1+E)(M_0-m)
&=s(E^2-2E+3)+(E+3)(m-m_0)\\
&>0.
\end{aligned}
\tag{9}
$$

Combining (7)--(9),

$$
\begin{aligned}
\kappa(s-c_*)-\chi
&=(m-m_0)
\left(
\frac{2\kappa}{1+E}-(M_0-m)
\right)\\
&>0.
\end{aligned}
$$

Therefore $c_*<s-\chi/\kappa=\widetilde c$ on this sheet as well.

### The upper envelope stays below one

Let $U=1-s$. To prove $\widetilde c<1$, it is enough by (3) to prove

$$
\chi+U\kappa>0.
$$

Using the strict domain inequality $mM>U(1+U)$ from (1),

$$
\begin{aligned}
\chi+U\kappa
&=s^4-s^2+mM+U(4s^3-2s+m)\\
&>U\left(m+3s^3-s^2-3s+2\right).
\end{aligned}
\tag{10}
$$

Here $0<U<1/3$, and

$$
3s^3-s^2-3s+2
=1-4U+8U^2-3U^3
>1-4U+7U^2
>0.
$$

The last quadratic has discriminant $-12$. Hence (10) is positive and
$\widetilde c<1$. This completes the proof of Proposition 3.1.

## 4. Rational form after reflection

Reflect so that

$$
z=a-b\ge0,
\qquad
U=a+b-1,
\qquad
s=1-U,
\qquad
m=\frac{s-z}{2}.
$$

Then

$$
4\chi=4s^4-3s^2-z^2
$$

and

$$
2\kappa=8s^3-3s-z.
$$

Therefore (4) is the rational function

$$
\boxed{
\widetilde c
=s-
\frac{4s^4-3s^2-z^2}
{2(8s^3-3s-z)}.
}
\tag{11}
$$

Equivalently, define

$$
\Xi(U,z)
=1-10U+21U^2-16U^3+4U^4-z^2
$$

and

$$
G(U,z)
=5-21U+24U^2-8U^3-z.
$$

Then

$$
\boxed{
\widetilde c
=1-U-
\dfrac{\Xi(U,z)}{2G(U,z)}.
}
\tag{12}
$$

The denominator is positive by (3). Formula (12) contains neither the
quartic root $C_L(m)$ nor the radial radical $\sqrt{4s^2-3}$, and it is valid
without splitting according to the sign of $\chi$.

## 5. Reusing the proved adjacent-overlap estimate

Section 6 of `31034` proves that the smaller normalized adjacent line distance
is

$$
d=
\frac{
\mathcal A+U(2m-1)+D(\mathcal A+U)
}{2\rho},
\qquad
\mathcal A=1-m+m^2,
\qquad
\rho=\mathcal A+U(1+m+U),
\tag{13}
$$

and satisfies

$$
d\ge2c_*-1.
$$

Thus

$$
c_*\le c_{\mathrm{adj}}:=\frac{1+d}{2}.
\tag{14}
$$

One safe candidate for the smaller-disk argument is therefore

$$
\boxed{
\overline c
=
\min\{\widetilde c,c_{\mathrm{adj}}\}.
}
\tag{15}
$$

Both entries in (15) are upper bounds for $c_*$, while
$\widetilde c<1$. Hence

$$
c_*\le\overline c<1.
$$

Moreover, $2\overline c-1\le d$, so both adjacent cap overlaps follow
immediately from the already-proved line-distance estimate. This leaves only
the two mixed overlaps. Alternatively, one may try to prove directly that
$\widetilde c\le c_{\mathrm{adj}}$ and avoid the minimum in (15).

Set

$$
\overline\eta=h(1-\overline c),
\qquad
\overline\tau=h(2\overline c-1).
$$

Since $\overline c\ge c_*$,

$$
\overline\eta\le\eta=h(1-c_*),
$$

so the disk $\mathcal D_{\overline\eta}$ is contained in the disk already
forced by `31032`. Proving the cap chain for this smaller disk is therefore a
valid, stronger replacement target.

## 6. Cleaner forms of the mixed certificates

Put

$$
N_A=\lVert A\rVert^2,
\qquad
N_C=\lVert C\rVert^2,
\qquad
u_0=\langle C,RA\rangle,
\qquad
\Delta=\operatorname{cross}(C,RA),
$$

and abbreviate

$$
e=1-\overline c,
\qquad
t=2\overline c-1.
$$

The Gram identity is

$$
\Delta^2=N_AN_C-u_0^2.
\tag{16}
$$

Substituting $\overline\eta=he$ and $\overline\tau=ht$ into the mixed
quantities and using (16) gives the factorizations

$$
\boxed{
P_A
=N_A\left[
\Delta^2-h^2\lVert tRA-eC\rVert^2
\right].
}
\tag{17}
$$

and

$$
\boxed{
P_C
=N_C\left[
\Delta^2-h^2\lVert tC-eRA\rVert^2
\right].
}
\tag{18}
$$

Thus the two remaining signs are reduced to

$$
\Delta^2\ge h^2\lVert tRA-eC\rVert^2,
\qquad
\Delta^2\ge h^2\lVert tC-eRA\rVert^2.
\tag{19}
$$

These forms avoid the nested $\eta,\tau,u_0$ expression and expose the mixed
conditions as two Gram-determinant inequalities.

## 7. Proposed exact-algebra route

The tangent witnesses $A,C$ are rational functions of $a,b,D$, and after
reflection

$$
D^2=z^2+6U+3U^2.
\tag{20}
$$

On the cell $\widetilde c\le c_{\mathrm{adj}}$, substitute (12) into (19).
On the complementary cell, substitute (13)--(15). After multiplying by the
known positive denominators, each target is a polynomial expression in
$U,z,D$. Reducing powers of $D$ with (20) leaves an expression of the form

$$
R_0(U,z)+D R_1(U,z)\ge0.
\tag{21}
$$

The reflected strict domain can be written semialgebraically as

$$
U>0,
\qquad
z\ge0,
\qquad
z^2+6U+3U^2<1.
\tag{22}
$$

The comparison defining the two cells in (15) is also algebraic after clearing
positive denominators. Consequently (21) can in principle be discharged by
exact rational methods: direct factorization, Sturm/resultant arguments, CAD,
or a rational sum-of-squares/Positivstellensatz certificate. No interval
arithmetic is inherent in this reduced target.

A useful first subtarget is

$$
\widetilde c\le c_{\mathrm{adj}},
$$

because proving it would eliminate the additional cell split and allow (12)
to be used globally.

## 8. What remains before replacing the certificate

This note proves only the upper-envelope statement (5). To remove the current
interval dependency, one must still do one of the following:

1. prove $\widetilde c\le c_{\mathrm{adj}}$ and prove both inequalities in
   (19) with $\overline c=\widetilde c$; or
2. retain (15), split along its algebraic comparison, and prove (19) on both
   cells.

All denominator signs used while clearing the tangent-witness formulas must be
recorded explicitly, and the final polynomial positivity argument must cover
the limiting faces of (22). Until those obligations are completed and checked,
Section 7 of `31034` remains a genuine proof dependency.