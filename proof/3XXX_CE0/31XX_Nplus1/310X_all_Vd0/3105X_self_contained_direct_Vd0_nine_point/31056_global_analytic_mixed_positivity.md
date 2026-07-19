# Global Analytic Positivity of the Mixed-Overlap Polynomials

Status: Proven

The exact elimination in
[`31055_rational_radial_envelopes_and_mixed_reduction.md`](31055_rational_radial_envelopes_and_mixed_reduction.md)
produces integer polynomials

$$
A_{B,X}(U,z),
\qquad
B_{B,X}(U,z),
\qquad
B\in\{L,T\},
\quad
X\in\{A,C\},
$$

such that the reduced mixed numerator is a positive factor times

$$
A_{B,X}(U,z)+D B_{B,X}(U,z),
\qquad
D^2=z^2+6U+3U^2.
\tag{1}
$$

This note proves all eight polynomial signs by three fixed analytic charts
and twenty global positive-basis identities.  It uses no interval arithmetic,
adaptive subdivision, pruning, or branch-and-bound.

## 1. Exact closed cells

Put

$$
\mathcal G(U)=1-6U-3U^2,
$$

$$
H(U)=1-10U+21U^2-16U^3+4U^4,
$$

$$
U_H=1-\frac{\sqrt3}{2},
\qquad
U_{\max}=\frac2{\sqrt3}-1.
$$

In the reflected variables of `31055`, the strict witness domain satisfies

$$
0<U<U_{\max},
\qquad
z\ge0,
\qquad
z^2<\mathcal G(U).
\tag{2}
$$

Indeed

$$
a^2+ab+b^2
=
\frac{3(1+U)^2+z^2}{4}<1
$$

is exactly the last inequality in (2), while its minimum at fixed $U$ gives
$U<U_{\max}$.  The radial selector is

$$
4\chi=H(U)-z^2.
\tag{3}
$$

The factorization

$$
H(U)=(U-1)^2(4U^2-8U+1)
$$

shows that $H\ge0$ on $[0,U_H]$ and $H\le0$ on
$[U_H,U_{\max}]$.  Moreover

$$
\mathcal G(U)-H(U)
=
4U(1-6U+4U^2-U^3)
\ge0
\qquad(0\le U\le U_H).
$$

The cubic in parentheses is decreasing on this interval and at $U_H$ equals

$$
-\frac54+\frac{7\sqrt3}{8}>0.
$$

Therefore the two radial branches are exactly covered by the three closed
cells

$$
\begin{array}{ll}
T:&0\le U\le U_H,
\quad 0\le z^2\le H(U),\\[1mm]
L_0:&0\le U\le U_H,
\quad H(U)\le z^2\le\mathcal G(U),\\[1mm]
L_1:&U_H\le U\le U_{\max},
\quad 0\le z^2\le\mathcal G(U).
\end{array}
\tag{4}
$$

Passing from the strict domain to these closed cells is valid by polynomial
continuity.

## 2. Global Bernstein lemma

If $P(r,s)$ has bidegree $(m,n)$, write its tensor Bernstein expansion on
$[0,1]^2$ as

$$
P(r,s)
=
\sum_{i=0}^m\sum_{j=0}^n
b_{ij}
\binom mi r^i(1-r)^{m-i}
\binom nj s^j(1-s)^{n-j}.
\tag{5}
$$

Every basis function in (5) is nonnegative on the square.  Hence
$b_{ij}\ge0$ for every $i,j$ implies $P\ge0$ on the whole square.  This is
one global polynomial identity, not a subdivision procedure.

All coefficients below lie in $\mathbb Q(\sqrt3)$.  For
$r_0,r_1\in\mathbb Q$, the sign of $r_0+r_1\sqrt3$ is determined exactly by
rational sign tests and, when the summands have opposite signs, by comparing
$r_0^2$ with $3r_1^2$.

## 3. The $T$ chart

Use

$$
U=\frac{(x-1)(3-x)}{4x},
\qquad
z=y\frac{9-x^4}{8x^2},
$$

$$
1\le x\le\sqrt3,
\qquad
0\le y\le1.
\tag{6}
$$

Here

$$
H\left(\frac{(x-1)(3-x)}{4x}\right)
=
\left(\frac{9-x^4}{8x^2}\right)^2,
$$

and $U$ increases from $0$ to $U_H$.  Thus (6) covers the complete $T$
cell in (4).

For a core polynomial

$$
F(U,z)=\sum c_{ij}U^iz^j,
$$

put

$$
M_F=\max_{c_{ij}\ne0}(i+2j),
\qquad
N_F=\max_{c_{ij}\ne0}(2i+3j).
$$

Then

$$
\widehat F_T(x,y)
=
2^{N_F}x^{M_F}
F\left(
\frac{(x-1)(3-x)}{4x},
y\frac{9-x^4}{8x^2}
\right)
\tag{7}
$$

is an integer polynomial and has the same sign as $F$ on (6).  Substitute

$$
x=1+(\sqrt3-1)r,
\qquad
0\le r\le1.
$$

The single global Bernstein expansion of each transformed target on the
$(r,y)$ square has the following exact data.

| Polynomial | Bidegree | Coefficients | Zero coefficients |
|---|---:|---:|---:|
| $A_{T,A}$ | $(88,22)$ | 2047 | 2 |
| $B_{T,A}$ | $(80,20)$ | 1701 | 0 |
| $A_{T,C}$ | $(88,22)$ | 2047 | 2 |
| $B_{T,C}$ | $(80,20)$ | 1701 | 0 |

Every nonzero coefficient is strictly positive.  The two zero coefficients
in each $A$ row are boundary coefficients.  Therefore all four $T$-cell
polynomials are nonnegative.

## 4. The two $L$ charts

For any of the four $L$-branch polynomials $F(U,z)$, separate its even and
odd powers of $z$:

$$
F(U,z)=E_F(U,w)+zO_F(U,w),
\qquad
w=z^2.
\tag{8}
$$

Define

$$
R_F(U,w)=E_F(U,w)^2-wO_F(U,w)^2.
\tag{9}
$$

If $E_F\ge0$ and $R_F\ge0$, then

$$
E_F\ge\sqrt w\left\lvert O_F\right\rvert,
$$

and therefore, because $z=\sqrt w\ge0$,

$$
F
=E_F+zO_F
\ge
E_F-\sqrt w\left\lvert O_F\right\rvert
\ge0.
\tag{10}
$$

Thus it is enough to prove $E_F,R_F\ge0$ on two fixed squares.

### 4.1 The $L_0$ chart

Set

$$
U=U_Hr,
$$

$$
w=H(U)+s\left(\mathcal G(U)-H(U)\right),
\qquad
0\le r,s\le1.
\tag{11}
$$

This maps the square exactly onto

$$
0\le U\le U_H,
\qquad
H(U)\le w\le\mathcal G(U).
$$

### 4.2 The $L_1$ chart

Set

$$
U=U_H+(U_{\max}-U_H)r,
$$

$$
w=s\mathcal G(U),
\qquad
0\le r,s\le1.
\tag{12}
$$

This maps the square exactly onto

$$
U_H\le U\le U_{\max},
\qquad
0\le w\le\mathcal G(U).
$$

Convert $E_F$ and $R_F$ once to tensor Bernstein form on each square.  The
exact bidegrees and coefficient counts are as follows; each entry is
“bidegree; number of coefficients.”

| $F$ | $L_0:E_F$ | $L_0:R_F$ | $L_1:E_F$ | $L_1:R_F$ |
|---|---:|---:|---:|---:|
| $A_{L,A}$ | $(46,11);564$ | $(92,22);2139$ | $(26,11);324$ | $(52,22);1219$ |
| $B_{L,A}$ | $(42,10);473$ | $(84,20);1785$ | $(24,10);275$ | $(48,20);1029$ |
| $A_{L,C}$ | $(46,11);564$ | $(92,22);2139$ | $(26,11);324$ | $(52,22);1219$ |
| $B_{L,C}$ | $(42,10);473$ | $(84,20);1785$ | $(24,10);275$ | $(48,20);1029$ |

Every coefficient in these sixteen expansions is strictly positive.  Hence
$E_F,R_F\ge0$ on both cells, and (10) proves all four $L$-branch polynomial
signs.

Together with the four $T$ expansions, these are exactly twenty global
Bernstein identities.

## 5. Conclusion

Sections 3--4 prove

$$
A_{B,X}(U,z)\ge0,
\qquad
B_{B,X}(U,z)\ge0
$$

for every $B\in\{L,T\}$ and $X\in\{A,C\}$ on the complete reflected
domain.  Since $D\ge0$, equation (1) is nonnegative.  The positive
denominators and exact factorization in `31055` therefore give

$$
Q_A\ge0,
\qquad
Q_C\ge0.
$$

Reflection supplies the other half-domain.  Thus both mixed smaller-disk cap
overlaps hold. $\square$

## 6. Exact reproduction

The package-local symbolic derivation audit is

```text
python3 proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/verify_mixed_overlap_core_derivation.py
```

This audit requires SymPy.  It independently derives the eight polynomials
from the witness formulas and compares them coefficient by coefficient with
the canonical transcript.  Its deterministic JSON output includes

```text
certificate: 3105X_mixed_overlap_core_derivation
core_polynomial_sha256:
dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485
result: PASS
```

The exact global positive-basis verifier is

```text
python3 proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/verify_global_core_positivity.py
```

It loads
[`mixed_overlap_core_polynomials.py`](3105X_computation/mixed_overlap_core_polynomials.py)
and its six package-local numbered data modules, authenticates the decoded
polynomial transcript, and verifies all twenty identities using only the
Python standard library with exact integers, rational numbers, and
$\mathbb Q(\sqrt3)$ sign comparisons.  Its
deterministic output includes

```text
adaptive_subdivision: false
branch_and_bound: false
core_polynomial_sha256:
dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485
result: PASS
```

The fixed three-chart proof contains no interval boxes, recursive splitting,
pruning, adaptive depth, or search tree.
