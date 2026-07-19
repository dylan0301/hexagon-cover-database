# Global Analytic Positivity of the Mixed-Overlap Core Polynomials

Status: Proven

This note removes the adaptive Bernstein subdivision from
[`31037_rational_cmax_upper_envelope.md`](31037_rational_cmax_upper_envelope.md).
That note derives the exact core reduction

$$
\operatorname{num}(Q_{B,X})
=32(K+3)^2\left(A_{B,X}(U,z)+D B_{B,X}(U,z)\right),
\qquad D^2=z^2+6U+3U^2,
$$

with positive denominators. The present note proves the eight polynomial
signs by three fixed analytic charts and global positive-basis expansions.
There is no interval arithmetic, adaptive subdivision, pruning, or
branch-and-bound.

The exact verifier and its exported polynomial data are:

- [`3103X_computation/verify_global_core_positivity.py`](3103X_computation/verify_global_core_positivity.py);
- [`3103X_computation/mixed_overlap_core_polynomials.json`](3103X_computation/mixed_overlap_core_polynomials.json);
- [`3103X_computation/export_mixed_overlap_core_polynomials.py`](3103X_computation/export_mixed_overlap_core_polynomials.py).

## Claim

For each radial cell $B\in\{L,T\}$ and each outer witness
$X\in\{A,C\}$, the exact elimination in the mixed-overlap argument produces
integer polynomials

$$
A_{B,X}(U,z),\qquad B_{B,X}(U,z)
$$

such that the reduced numerator is a positive factor times

$$
A_{B,X}(U,z)+D B_{B,X}(U,z),
\qquad D^2=z^2+6U+3U^2.
$$

On the reflected domain $z\ge0$, all eight polynomials are nonnegative.
The proof below uses no branch-and-bound, no adaptive subdivision, and no
interval arithmetic. It consists of three fixed analytic charts and one
global tensor-product Bernstein expansion for each transformed target.

## 1. Exact domain

Put

$$
G(U)=1-6U-3U^2,
\qquad
H(U)=1-10U+21U^2-16U^3+4U^4.
$$

The strict residual-core domain satisfies

$$
0\le U\le U_{\max}:=\frac2{\sqrt3}-1,
\qquad 0\le z,
\qquad z^2\le G(U).
$$

Moreover the radial selector is

$$
4\chi=H(U)-z^2.
$$

Let

$$
U_H=1-\frac{\sqrt3}{2}.
$$

The factorization

$$
H(U)=(U-1)^2(4U^2-8U+1)
$$

shows that $H\ge0$ on $[0,U_H]$ and $H\le0$ on
$[U_H,U_{\max}]$. Also

$$
G(U)-H(U)=4U\bigl(1-6U+4U^2-U^3\bigr)\ge0
\quad(0\le U\le U_H).
$$

Indeed the cubic in parentheses is decreasing there, and at $U_H$ it is

$$
-\frac54+\frac{7\sqrt3}{8}>0.
$$

Consequently the two radial cells are exactly covered by

$$
\begin{array}{ll}
T:&0\le U\le U_H,\quad 0\le z^2\le H(U),\\[1mm]
L_0:&0\le U\le U_H,\quad H(U)\le z^2\le G(U),\\[1mm]
L_1:&U_H\le U\le U_{\max},\quad 0\le z^2\le G(U).
\end{array}
$$

Passing to these closed cells is harmless by continuity.

## 2. Global Bernstein lemma

If $P(r,s)$ has bidegree $(m,n)$, write its tensor Bernstein expansion
on $[0,1]^2$ as

$$
P(r,s)=
\sum_{i=0}^m\sum_{j=0}^n b_{ij}
\binom mi r^i(1-r)^{m-i}
\binom nj s^j(1-s)^{n-j}.
$$

Every basis function is nonnegative on the square. Therefore
$b_{ij}\ge0$ for all $i,j$ implies $P\ge0$ on the whole square.
This is one global algebraic identity, not a subdivision argument.

All coefficients below lie in $\mathbb Q(\sqrt3)$. Their signs are checked
exactly: for $a,b\in\mathbb Q$, the sign of $a+b\sqrt3$ is determined by
rational sign tests and, when necessary, comparison of $a^2$ with $3b^2$.

## 3. The $T$ cell

Use the rationalizing chart

$$
U=\frac{(x-1)(3-x)}{4x},
\qquad
z=y\frac{9-x^4}{8x^2},
\qquad
1\le x\le\sqrt3,
\quad 0\le y\le1.
$$

Here

$$
H\!\left(\frac{(x-1)(3-x)}{4x}\right)
=\left(\frac{9-x^4}{8x^2}\right)^2,
$$

and $U$ increases from $0$ to $U_H$, so this chart covers the entire
$T$ cell exactly.

For a core polynomial

$$
F(U,z)=\sum c_{ij}U^i z^j,
$$

put

$$
M_F=\max_{c_{ij}\ne0}(i+2j),
\qquad
N_F=\max_{c_{ij}\ne0}(2i+3j).
$$

Then

$$
\widehat F_T(x,y)=2^{N_F}x^{M_F}
F\!\left(\frac{(x-1)(3-x)}{4x},
 y\frac{9-x^4}{8x^2}\right)
$$

is an integer polynomial and has the same sign as $F$. Set
$x=1+(\sqrt3-1)r$. The single global Bernstein expansions on
$(r,y)\in[0,1]^2$ have the following exact sign data.

| polynomial | bidegree | Bernstein coefficients | zeros |
|---|---:|---:|---:|
| $A_{T,A}$ | $(88,22)$ | 2047 | 2 |
| $B_{T,A}$ | $(80,20)$ | 1701 | 0 |
| $A_{T,C}$ | $(88,22)$ | 2047 | 2 |
| $B_{T,C}$ | $(80,20)$ | 1701 | 0 |

Every nonzero coefficient is strictly positive. Hence all four $T$-cell
polynomials are nonnegative. The two zero coefficients in each $A$ row are
boundary coefficients and cause no difficulty.

## 4. The $L$ cell

For any one of the four $L$-cell polynomials $F(U,z)$, separate its even
and odd powers of $z$:

$$
F(U,z)=E_F(U,w)+zO_F(U,w),
\qquad w=z^2.
$$

Define

$$
R_F(U,w)=E_F(U,w)^2-wO_F(U,w)^2.
$$

The following elementary implication is the key analytic reduction:

$$
E_F\ge0,\quad R_F\ge0
\quad\Longrightarrow\quad
F\ge0.
$$

Indeed $R_F\ge0$ and $E_F\ge0$ give
$E_F\ge\sqrt w\,|O_F|$, while $z=\sqrt w\ge0$, so

$$
F=E_F+zO_F\ge E_F-\sqrt w\,|O_F|\ge0.
$$

It remains to prove $E_F,R_F\ge0$ on two fixed rectangles.

### 4.1 The cell $L_0$

Set

$$
U=U_H r,
\qquad
w=H(U)+s\bigl(G(U)-H(U)\bigr),
\qquad 0\le r,s\le1.
$$

This maps the square exactly onto
$0\le U\le U_H$, $H(U)\le w\le G(U)$.

### 4.2 The cell $L_1$

Set

$$
U=U_H+(U_{\max}-U_H)r,
\qquad
w=sG(U),
\qquad 0\le r,s\le1.
$$

This maps the square exactly onto
$U_H\le U\le U_{\max}$, $0\le w\le G(U)$.

On each square, convert $E_F$ and $R_F$ once to tensor Bernstein form.
Every coefficient is strictly positive. The exact degrees and counts are:

| $F$ | $L_0:E_F$ | $L_0:R_F$ | $L_1:E_F$ | $L_1:R_F$ |
|---|---:|---:|---:|---:|
| $A_{L,A}$ | $(46,11);564$ | $(92,22);2139$ | $(26,11);324$ | $(52,22);1219$ |
| $B_{L,A}$ | $(42,10);473$ | $(84,20);1785$ | $(24,10);275$ | $(48,20);1029$ |
| $A_{L,C}$ | $(46,11);564$ | $(92,22);2139$ | $(26,11);324$ | $(52,22);1219$ |
| $B_{L,C}$ | $(42,10);473$ | $(84,20);1785$ | $(24,10);275$ | $(48,20);1029$ |

Each entry records “bidegree; number of coefficients.” There are no zero or
negative coefficients in any of these sixteen expansions. Thus
$E_F,R_F\ge0$, and the even/odd lemma proves all four $L$-cell polynomial
signs.

## 5. Conclusion

We have proved

$$
A_{B,X}(U,z)\ge0,
\qquad B_{B,X}(U,z)\ge0
$$

for $B\in\{L,T\}$, $X\in\{A,C\}$, on the complete reflected domain.
Since $D\ge0$,

$$
A_{B,X}+DB_{B,X}\ge0.
$$

The positive denominator and common-factor calculation from the exact
elimination therefore gives both mixed residual inequalities. Reflection
supplies $z\le0$.

The certificate is nonbranching in the literal sense: it uses three fixed
charts, twenty global Bernstein expansions, and no box splitting, pruning,
adaptive depth, or search tree.

## 6. Reproduction

From the repository root run

```text
python3 proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/3103X_computation/verify_global_core_positivity.py
```

The verifier reads `mixed_overlap_core_polynomials.json` from the same
directory. To regenerate that file from the exact elimination routine, run

```text
python3 proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/3103X_computation/export_mixed_overlap_core_polynomials.py
```

and compare the output byte-for-byte with the committed JSON file. The program
uses only exact integers, rational numbers, and $\mathbb Q(\sqrt3)$ sign
comparisons. Its deterministic result is `PASS`, with

```text
adaptive_subdivision: false
branch_and_bound: false
core_polynomial_sha256:
dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485
```
