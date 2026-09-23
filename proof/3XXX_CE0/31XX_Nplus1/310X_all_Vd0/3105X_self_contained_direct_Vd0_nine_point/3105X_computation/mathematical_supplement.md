# Explicit Case F certificate: complete mathematical supplement

Status: Proven (exact computer-assisted algebra; upstream geometry cited separately)

This is the consolidated supplement for `verify_explicit_stage.py` and the active
source `../3105b_explicit_comparison_enclosure.md`. All formulas refer to the
fixed-start Newton comparison points, except the explicitly distinguished original
frontier points. The actual forced disk is unchanged. The older sparse Bernstein
certificate is preserved separately and is not an input to this route.

The sections below collect the detailed identities used by the final standalone
verifier. Internal equation numbers in imported derivations are local to their
section. Earlier discovery-only inventories and superseded SOS certificates are
not part of this supplement. The four mixed signs in the first section are
proved by its explicit quadratic models, not assumed SOS inputs. The increment
and shared-boundary coefficient budgets remain finite exact computations.

The manuscript includes the full geometric forcing, the fixed-start inclusion,
and the uniform-radius proof. This supplement prints the longer algebraic
identities and coefficient bounds cited by its explicit comparison lemmas.


## Supplement 1: Definitions and explicit-comparison certificate

### 2. Unchanged setup and definitions

Assume the strict F geometric domain

\[
0<a,b<1,\qquad a+b>1,\qquad \rho=a^2+ab+b^2<1.
\]

Reflect so that a>=b, and put

\[
a=1-m,\qquad b=m+U,\qquad D^2=K=4\rho-3.
\]

The geometric domain is contained in

\[
\mathcal R=[0,1/2]\times[0,1/6].
\]

All five new polynomial comparisons hold on this full rectangle, including points that need not correspond to a physical configuration. The radius parameter e is independent when partial derivatives are taken. The polynomial Pi is quadratic in e, so Pi_Uee and Pi_ee do not depend on e.

The previous radius lemma supplies

\[
b_0=\frac{m(1-m)}2\le r<m,\qquad
 e_0=\max\{r,m-\kappa U\},\qquad
 \kappa=\frac{m-r}{r},\qquad e_0\le e_*=1-c_*.
\]

Thus b0<=r<=e0<=m. Endpoints involving m=0 are understood by continuity; kappa is only used for positive m.

The previous explicit polynomial proof supplies

\[
\mathcal B_{ee}<-5600,\qquad \mathcal B(m,U,m)>210
\]

on the same rectangle. These calculations are rerun by the supplied verifier.

For exact reconstruction, define

\[
A_1=\frac{b+2a-bD}{2},\quad B_1=\frac{b-a+(a+b)D}{2},\quad
D_1=\frac{2b+a-aD}{2},\quad G_1=\frac{-b+a+(a+b)D}{2},
\]

\[
n_b=12b^2-12b+7,\quad n_a=12a^2-12a+7,
\]

\[
E_b=8\rho-12UA_1,\quad E_a=8\rho-12UD_1,
\]

\[
J_b=(1-2b)E_b+(A_1+2B_1)n_b,\quad L_b=E_b-A_1n_b,
\]

\[
J_a=(1-2a)E_a+(D_1+2G_1)n_a,\quad L_a=E_a-D_1n_a.
\]

Set

\[
\mathscr N=(J_bL_a+J_aL_b)^2
-((1-2e)J_bE_a-eJ_aE_b)^2
-3((1-2e)L_bE_a+eL_aE_b)^2.
\]

Reduction modulo D^2-K and exact division define Acal and Bcal by

\[
\operatorname{rem}_{D^2-K}\mathscr N=2\rho^2(\mathcal A+D\mathcal B),
\qquad
\Pi=(1+3K)\mathcal A+K(3+K)\mathcal B.
\]

The geometric tangent residual is

\[
Q_X=\frac{\rho^2}{2E_a^2E_b^2}(\mathcal A+D\mathcal B),
\]

with positive denominators on the physical domain. The verifier regenerates these expressions rather than trusting a coefficient transcript.

### 3. One common bounded-basis remainder lemma

Normalize

\[
s=4m-1,\qquad t=12U-1,\qquad -1\le s,t\le1.
\]

For a polynomial F(s,t), expand it exactly in the tensor Chebyshev basis:

\[
F(s,t)=\sum_{i,j}c_{ij}T_i(s)T_j(t).
\]

The identity T_n(cos theta)=cos(n theta) implies |T_n(z)|<=1 on [-1,1]. An algebraic verification uses

\[
T_n(z)^2+(1-z^2)U_{n-1}(z)^2=1,
\]

where the second-kind polynomial U_{n-1} is unrelated to the geometric variable U.

If G has coefficients g_ij in the same basis, then

\[
\boxed{|F-G|\le\sum_{i,j}|c_{ij}-g_{ij}|.}
\]

No numerical transform is used. The exact conversion uses

\[
z^n=2^{1-n}\sum_{0\le j<n/2}\binom njT_{n-2j}(z)
+\mathbf 1_{2\mid n}\,2^{-n}\binom n{n/2}
\]

for n>=1, and T0=1. The verifier also reconstructs F from the coefficients and checks equality as a rational polynomial.

The classical identity used here is NIST DLMF, §18.5(i), equation 18.5.1. No novelty is claimed for Chebyshev polynomials or the bounded-basis remainder estimate.

### 4. A single lower endpoint for Bcal on the entire rectangle

Let

\[
F_B(s,t)=\mathcal B\left(\frac{1+s}{4},\frac{1+t}{12},
 b_0\!\left(\frac{1+s}{4}\right)\right).
\]

Use the explicit cubic

\[
\begin{aligned}
10g(s,t)={}&-292s^3+556s^2t+1504s^2+364st^2-317st-1795s\\
&-28t^3+272t^2-389t+804.
\end{aligned}
\]

The exact coefficient error is

\[
\boxed{\|F_B-g\|_\infty\le
\frac{1351198806043}{163074539520}<\frac{17}{2}.}
\]

This comparison processes 75 canonical coefficients. It is the only new coefficient check for the radical-coefficient endpoints.

#### 4.1 Left half: s<=0

On the entire square,

\[
g_{ss}=\frac{1504-876s+556t}{5}\ge\frac{72}{5}>0.
\]

Moreover,

\[
g_s(0,t)=\frac{364t^2-317t-1795}{10}
\le-\frac{557}{5}<0.
\]

Therefore g_s(s,t)<0 when s<=0, so g(s,t)>=g(0,t). Since

\[
g(0,t)=\frac{804-389t+272t^2-28t^3}{10}
\ge\frac{387}{10}>\frac{25}{2},
\]

the lower bound is immediate on this half.

#### 4.2 Right half: four 2-by-2 matrices prove strong convexity

On 0<=s<=1, -1<=t<=1, the matrix

\[
10(\nabla^2g-8I)
\]

is affine in s,t. Its vertex values are:

| (s,t) | Matrix | Determinant |
|---|---|---:|
| (0,-1) | [[1816,-1045],[-1045,632]] | 55687 |
| (0,1) | [[4040,411],[411,296]] | 1026919 |
| (1,-1) | [[64,67],[67,1360]] | 82551 |
| (1,1) | [[2288,1523],[1523,1024]] | 23383 |

Each leading diagonal entry and determinant is positive, hence each matrix is positive definite. Bilinear interpolation gives the matrix at every point as a convex combination of those four matrices. Thus Hessian(g)>=8I throughout this half rectangle.

At z0=(2/3,1/3), exact evaluation gives

\[
g(z_0)=\frac{383}{30},\qquad
\nabla g(z_0)=\left(\frac{13}{45},-\frac{35}{18}\right).
\]

Strong convexity and completion of a square imply

\[
\begin{aligned}
g(z)&\ge g(z_0)+\nabla g(z_0)\cdot(z-z_0)+4\|z-z_0\|^2\\
&\ge g(z_0)-\frac{\|\nabla g(z_0)\|^2}{16}
=\frac{1623259}{129600}>\frac{25}{2}.
\end{aligned}
\]

Combining the two halves and the coefficient error,

\[
\boxed{\mathcal B(m,U,b_0)>\frac{25}{2}-\frac{17}{2}=4.}
\]

The statement has one lower-endpoint formula over the full rectangle. The proof of its cubic model uses two half rectangles; there is no claim that all case distinctions have disappeared.

#### 4.3 Consequence for the actual comparison radius

Bcal is concave in e, while

\[
\mathcal B(m,U,b_0)>4,\qquad \mathcal B(m,U,m)>210.
\]

Hence

\[
\boxed{\mathcal B(m,U,e)>4\quad(b_0\le e\le m).}
\]

In particular this applies to e0, because b0<=r<=e0<=m. Degenerate endpoint intervals are handled by their common endpoint, without division by m-b0.

**This does not replace the tangent comparison radius e0 or the actual disk radius by b0.** It uses b0 only to prove the sign of the radical coefficient. The earlier unsuccessful coarse-disk shortcut is not being reintroduced.

### 5. Four mixed-derivative checks with a common quadratic identity

For H1,H2,H3,H4 defined in Section 1, set

\[
F_i(s,t)=\frac1{1000}H_i\left(\frac{1+s}{4},\frac{1+t}{12}\right).
\]

Use the following quadratics:

\[
G_i=a s^2+b st+c s+d t^2+j t+k.
\]

| i | a | b | c | d | j | k | Error bound E_i |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 130 | 80 | -124 | 52 | 100 | 454 | 70 |
| 2 | 466 | 414 | 124 | 238 | 771 | 1379 | 300 |
| 3 | 286 | 228 | -202 | 154 | 348 | 1090 | 176 |
| 4 | 18 | 4 | -14 | 6 | 17 | 44 | 8 |

Exact Chebyshev conversion gives |Fi-Gi|<Ei. The exact errors, each computed from 77 coefficients, are:

| i | Exact coefficient error |
|---|---|
| 1 | 39790480544309 / 573308928000 |
| 2 | 85972921822907 / 286654464000 |
| 3 | 1400802677851 / 7962624000 |
| 4 | 338140798291 / 42998169600 |

#### A single completed-square identity proves positivity

For any row define

\[
\gamma=d-\frac{b^2}{4a},\qquad
\delta=j-\frac{bc}{2a}-2\gamma,\qquad
L=k-j+d-\frac{(c-b)^2}{4a}.
\]

Then

\[
\boxed{
G_i=a\left(s+\frac{bt+c}{2a}\right)^2
+\gamma(t+1)^2+\delta(t+1)+L.
}
\]

All a,gamma,delta are positive, and t+1>=0. The exact values are:

| i | gamma | delta | L |
|---|---|---|---|
| 1 | 516/13 | 764/13 | 21188/65 |
| 2 | 68059/466 | 98750/233 | 373211/466 |
| 3 | 15524/143 | 30230/143 | 210031/286 |
| 4 | 52/9 | 7 | 57/2 |

Thus Fi>Li-Ei, proving the round bounds

\[
\boxed{H_1>250000,\quad H_2>500000,\quad H_3>550000,\quad H_4>20000.}
\]

These quadratics are explicit constrained-SOS identities. The claim is not that SOS reasoning disappears: the large separately stored searched witnesses are replaced by one elementary identity and four fixed coefficient error checks.

### 6. Simplified derivative consequences and absence of circularity

Because H1=-Pi_Uee>0,

\[
\Pi_{Ue}(m,U,e)\ge\Pi_{Ue}(m,U,1/3)>20000
\qquad(0\le e\le1/3).
\]

The preceding verified increment argument supplies, with x=1-2m,

\[
\Pi_U(m,U,b_0)\ge A(x)+25000U,
\qquad A(x)=-2985+503x+\frac{12515}{2}x^2.
\]

Integrating the uniform mixed-derivative bound gives

\[
\begin{aligned}
\Pi_U(m,U,1/3)
&>A(x)+20000\left(\frac13-\frac{1-x^2}{8}\right)\\
&=\frac{3545}{3}+503x+\frac{52545}{6}x^2>1180.
\end{aligned}
\]

This replaces the former reuse of a separately stored four-square certificate, its x-dependent lower bound J(x), and the extra quartic completed-square comparison. The independent stronger local bound Pi_U>10700 for m>=1/3, used for the endpoint estimate, is retained.

No circular step is introduced. The four new derivative comparisons are checked directly from Pi. The increment polynomial is checked independently. Neither computation assumes the resulting positivity of Pi_U.

For

\[
S_k(e)=\Pi_{UU}-2k\Pi_{Ue}+k^2\Pi_{ee},
\]

the identity

\[
\partial_eS_\kappa(e)=(1-3e)H_2+3eH_3+2(\kappa-1)H_1>0
\]

holds for the actual kappa>=1 and 0<=e<=1/3. Thus the new signs feed into exactly the existing affine-path argument. The earlier weighted-conjugate proof of Pi_ee<0 is used only on its established D<1 physical and integration domains; it is not silently extended to every point of the large rectangle.

### 7. Completion of the unchanged tangent argument

The previous cubic-curvature proof remains and gives, for ell=(1+5m)/2,

\[
-S_\ell(1/3)>21500.
\]

The positive-square identity kappa0-ell=2(m-1/2)^2 and the new Pi_Ue>0 give the same slope and radius comparisons. Therefore the affine branch remains strictly concave and is controlled by its positive endpoints. The constant-radius branch remains increasing by the earlier restricted derivative result and Pi_Ue>0. The shared-boundary Taylor argument remains unchanged.

Consequently Pi(m,U,e0)>0. The new Bcal positivity gives

\[
\mathcal A+D\mathcal B
\ge\frac{\Pi}{1+3K}>0
\]

using the preserved identity

\[
D(1+3D^2)-D^2(3+D^2)=D(1-D)^3\ge0.
\]

The preserved Gram factorization, endpoint-norm ordering, and paired-radius transfer supply the two actual-radius tangent inequalities. Together with the unchanged actual-disk line contacts, this retains the same Case F enclosure conclusion. All upstream geometric assumptions are the ones stated in the supplied reports; this step verifies their algebraic terminal calculations, not a new independent proof of every geometric lemma.


## Supplement 2: Weighted-conjugate curvature and its domain

### 3. Analytic replacement I: the hidden positive weights

#### Proposition 3.1. Weighted-conjugate identity

For `D^2=K`,

\[
\boxed{
\Pi(m,U,e)=
\frac{(1+D)^3\mathscr N(D,e)+(1-D)^3\mathscr N(-D,e)}{4\rho^2}.
}
\tag{3.1}
\]

**Proof.** The two conjugate remainders are

\[
\mathscr N(\pm D,e)=2\rho^2(\mathcal A\pm D\mathcal B).
\]

Use

\[
(1+D)^3+(1-D)^3=2(1+3D^2),
\]
\[
(1+D)^3-(1-D)^3=2D(3+D^2).
\]

Substitution gives (3.1).

#### Corollary 3.2. Radius concavity without a coefficient certificate

On the strict physical domain,

\[
\boxed{\Pi_{ee}<0.}
\tag{3.2}
\]

**Proof.** Let

\[
V(D)=\bigl(2J_bE_a+J_aE_b,\;\sqrt3(2L_bE_a-L_aE_b)\bigr).
\]

The minus sign in its second component is important: it comes from differentiating the plus sign in the second square of (2.2). Direct differentiation gives

\[
\mathscr N_{ee}(D,e)=-2\|V(D)\|^2.
\]

Therefore (3.1) yields

\[
\boxed{
-\Pi_{ee}=
\frac{(1+D)^3\|V(D)\|^2+(1-D)^3\|V(-D)\|^2}{2\rho^2}.
}
\tag{3.3}
\]

Both weights are nonnegative for `0<=D<=1`. On the strict domain, the first component of `V(D)` is

\[
E_aE_b(2j_b+j_a)>0.
\]

Thus the right-hand side is strictly positive. No sign computation on the expanded polynomial is needed.

#### Scope: the domain cannot be silently enlarged

Identity (3.3) is **not** an automatic sign proof for `D>1`, because `(1-D)^3` would then be negative. The older certificate checked a larger rectangle, part of which has `D>1`. The replacement uses (3.3) only where its nonnegative weights are justified.

That is enough for the complete proof. The affine-branch argument moves through `0<U<=r(m)`. To check these points remain physical, put `c=C_L(m)`. Its quartic equation gives

\[
K(m,1-c)=4c^4-12c+9.
\]

For `h<=c<1`,

\[
K(m,1-c)-1=4(c-1)(c^3+c^2+c-2)<0.
\]

Indeed the second factor is increasing and is positive at `c=h`, where it equals `(7h-5)/4`. Since `K` increases with `U` and `r<=1-c`,

\[
K(m,U)<1\qquad(0<U\le r).
\]

The original constant-branch application is already in the physical domain. The new boundary derivative checks in Section 5 are independent exact checks on their stated rectangle. No use of (3.3) outside its valid domain is required.

#### A reusable interpretation

The earlier approximation

\[
\sqrt K\ge\frac{K(3+K)}{1+3K}
\]

is tied to the same positive weights. More generally, for an odd integer `n`, put

\[
E_n(K)=\sum_{j\ \mathrm{even}}\binom nj K^{j/2},\qquad
O_n(K)=\sum_{j\ \mathrm{odd}}\binom nj K^{(j+1)/2}.
\]

For `0<=D<=1`,

\[
D E_n(D^2)-O_n(D^2)=D(1-D)^n\ge0.
\]

Thus `O_n/E_n` is a rational lower bound for `sqrt K`. In addition,

\[
E_n\mathcal A+O_n\mathcal B
=\tfrac12\bigl[(1+D)^n(\mathcal A+D\mathcal B)
 +(1-D)^n(\mathcal A-D\mathcal B)\bigr].
\]

Whenever the two conjugate expressions are concave in another parameter, this combination is concave too. The case `n=3` is exactly the present proof. Larger odd powers are not needed here, and are not proposed as an automatic simplification.

### 4. Analytic replacement II: endpoint-norm ordering

The previous exact algebra gives

\[
\|X\|^2-\|Y\|^2
=\frac{8Uz\rho^2}{E_a^2E_b^2}\,H(D,U).
\tag{4.1}
\]

The verifier reconstructs this identity from the point numerators. What previously needed 153 positive-basis entries was the sign of `H`.

#### Proposition 4.1

On

\[
0\le D\le1,\qquad 0\le U\le D^2/6,
\]

one has

\[
\boxed{H(D,U)\ge\frac{1261}{162}>0.}
\tag{4.2}
\]

The physical domain is contained in this region because `D^2=z^2+6U+3U^2`.

#### Step 1: `H` is convex in `U`

The explicit coefficients of `H` are given in Appendix A. Retaining its positive high-order terms or discarding them as appropriate gives

\[
\begin{aligned}
H_{UU}\ge{}&5688+4068D+3681D^2+1752D^3\\
&-5535D^4-2754D^5-1674D^6-360D^7-780D^8.
\end{aligned}
\tag{4.3}
\]

Here the negative terms involving `U` were bounded using `U<=D^2/6`. The unused coefficient `17928-2592D^2-432D` is positive for `D<=1`.

For `0<=D<=1`, the right-hand side of (4.3) is at least

\[
5688+(4068+3681+1752-11103)D^4
=5688-1602D^4\ge4086.
\]

Thus

\[
\boxed{H_{UU}\ge4086>0.}
\tag{4.4}
\]

#### Step 2: `H` decreases up to the upper boundary

At `U=D^2/6`, exact substitution gives

\[
\begin{aligned}
-H_U={}&720-360D+42D^2+504D^3-456D^4\\
&+32D^5+\tfrac{39}{2}D^6-51D^7
 +\tfrac{33}{2}D^8-D^9\\
&+\tfrac{11}{3}D^{10}+\tfrac13D^{11}
 +\tfrac1{18}D^{12}-\tfrac2{27}D^{14}.
\end{aligned}
\tag{4.5}
\]

Every negative high power can be absorbed by preceding positive terms. For example,

\[
504D^3-456D^4\ge48D^3,
\]
\[
32D^5+\tfrac{39}{2}D^6-51D^7\ge\tfrac12D^7,
\]
\[
\tfrac{33}{2}D^8-D^9\ge\tfrac{31}{2}D^8,
\]
\[
\tfrac{11}{3}D^{10}-\tfrac2{27}D^{14}\ge\tfrac{97}{27}D^{10}.
\]

Also `720-360D>=360`. Hence `-H_U(D,D^2/6)>=360`. By convexity,

\[
H_U(D,U)\le H_U(D,D^2/6)\le-360,
\]

and therefore

\[
H(D,U)\ge H(D,D^2/6).
\tag{4.6}
\]

#### Step 3: the boundary has a short power-grouping proof

Set `x=1-D`, so `0<=x<=1`. Then

\[
\begin{aligned}
648H(D,D^2/6)={}&5044+97166x-35625x^2\\
&+40360x^3+4565x^4-17736x^5-11711x^6\\
&+25172x^7-23022x^8\\
&+11588x^9-2018x^{10}-1248x^{11}\\
&+1148x^{12}-470x^{13}+114x^{14}-16x^{15}+x^{16}.
\end{aligned}
\tag{4.7}
\]

The six displayed groups following the constant are nonnegative. The corresponding positive remainders are bounded below by

\[
61541x,\quad10913x^3,\quad2150x^7,
\quad8322x^9,\quad678x^{12},\quad98x^{14}.
\]

For the second group, discard the positive `4565x^4` and use
`40360-17736-11711=10913`. Thus the boundary is at least `5044/648=1261/162`, proving (4.2).

This establishes (4.1) with the correct nonnegative sign whenever `z>=0`. Equality of the endpoint norms occurs on `z=0`; on the strict reflected asymmetric region the difference is positive. The old 153-entry positivity expansion is unnecessary.


## Supplement 3: Ordering polynomial in full

### Appendix A. Explicit polynomial for the ordering lemma

Write `H(D,U)=sum_{i=0}^8 h_i(D)U^i`, where

\[
\begin{aligned}
h_0={}&(D^2+3)(27D^5+9D^4+36D^3-2D^2-40D+48),\\
h_1={}&\tfrac32(27D^6-306D^5-189D^4-788D^3-660D^2+240D-480),\\
h_2={}&-\tfrac32(54D^6+198D^5+459D^4-1124D^3-1731D^2-1356D-1896),\\
h_3={}&54(21D^4+60D^3+89D^2-30D-28),\\
h_4={}&54(15D^4+16D^3-84D^2-120D-231),\\
h_5={}&-648D(13D+6),\\
h_6={}&-216(12D^2+2D-83),\\
h_7={}&12960,\qquad h_8=2592.
\end{aligned}
\]

The verifier derives this polynomial from (4.1), then checks the displayed formulas as identities. Its positive sign follows from Section 4, not from a 153-entry positivity table.


## Supplement 4: Polynomial radius comparison q <= r

#### 5.2 A quadratic comparison for `r`

One has

\[
\boxed{b_0(m)\le q(m)\le r(m)\quad(1/5\le m\le1/2).}
\tag{5.4}
\]

For the first inequality, `q-b_0` is concave, with endpoint values

\[
(q-b_0)(1/5)=369/100000,\qquad
(q-b_0)(1/2)=489/100000.
\]

For the second, put

\[
P_6=m^6-3m^5+9m^4-13m^3+16m^2-8m+4=L_r/8>0.
\]

Exact expansion gives

\[
r-q=\frac{p_8(m)}{100000P_6(m)},
\]

where

\[
\begin{aligned}
p_8(m)={}&52500m^8-198400m^7+623911m^6-1136733m^5\\
&+1605099m^4-1322643m^3+596576m^2-143288m+14844.
\end{aligned}
\tag{5.5}
\]

There is a short direct positivity proof for this degree-8 polynomial. For `m<=9/25`, substitute `x=9/25-m`; all nine power coefficients are positive (they are displayed in Appendix B). For `9/25<=m<=1/2`, put `x=m-43/100`, so `|x|<=7/100`. Writing `p_8=sum a_k x^k`, exact expansion gives

\[
a_0>7,\quad |a_1|<355,\quad a_2>35000,
\]

with bounds on `|a_3|,...,|a_8|` respectively

\[
135000,\ 466000,\ 64000,\ 299000,\ 18000,\ 52501.
\]

Their weighted tail is less than `11800x^2`. Consequently

\[
p_8>7-355|x|+23200x^2
\ge7-\frac{355^2}{92800}>5.
\tag{5.6}
\]

This proves (5.4), without checking the degree-105 polynomial.


## Supplement 5: Positive expansion for q <= r

### Appendix B. The positive expansion in the quadratic-radius comparison

For `x=9/25-m`, the coefficients of `p_8(9/25-x)` in increasing powers of `x` are exactly

\[
\frac{41724222906}{244140625},\quad
\frac{7752554236}{1953125},\quad
\frac{8237996528}{390625},\quad
\frac{18407109}{15625},\quad
\frac{63701151}{125},\quad
\frac{4797051}{25},\quad
314455,\quad47200,\quad52500.
\]

All are visibly positive. This is a nine-term, fully displayed elementary identity, not the former hidden degree-105 certificate.


## Supplement 6: Small-m shared boundary

#### 6.1 The small-`m` polynomial `F_b`

Expand at `m=1/5-x`, `0<=x<=1/5`, as `F_b=sum c_k x^k`. The expansion gives

- `c_0>103`, `c_4>61000`;
- `c_1,c_2,c_3` and `c_8,...,c_18` are nonnegative;
- `|c_5|<46000`, `|c_6|<189000`, `|c_7|<5000`;
- `|c_k|<6000000` for `19<=k<=27`.

The possible negative tail, after factoring `x^4`, is at most

\[
46000/5+189000/25+5000/125
+6000000\frac{(1/5)^{15}}{1-1/5}<17000.
\]

Hence `F_b>103+(61000-17000)x^4>103`.


## Supplement 7: Radical-coefficient concavity and upper endpoint

### 4. An analytic proof that the radical coefficient is concave in e

Let `B_2(m,U)` be the coefficient of `e^2` in `Bcal`. Put `x=1-2m` and define

\[
H(x,U)=-\frac1{16}B_2((1-x)/2,U).
\]

The exact expansion is

\[
H(x,U)=\sum_{j=0}^7 c_j(x)U^j,
\]

where

\[
\begin{aligned}
c_0={}&10(x^2+3)(2x^2+3)(3x^2+4),\\
c_1={}&\frac12(81x^7+189x^6-369x^5-21x^4-2596x^3-1644x^2-2880x-1440),\\
c_2={}&-\frac34(711x^6+702x^5+705x^4-500x^3-3242x^2-3728x-2664),\\
c_3={}&2268x^5+1161x^4+2454x^3+135x^2-3332x-120,\\
c_4={}&-3861x^4-1512x^3-2628x^2-3648x-874,\\
c_5={}&12(144x^3+45x^2+123x+385),\\
c_6={}&24(9x-2)(9x+10),\\
c_7={}&-1728(x+1).
\end{aligned}
\tag{4.1}
\]

For `0<=x<=1`,

\[
c_1<0,\quad c_2>0,\quad c_3\ge-(3332x+120),\quad
c_4<0,\quad c_5>0,\quad c_6\ge-480.
\]

For example, `81x^7+189x^6 <=270x^5<369x^5` proves the first sign, while

\[
711x^6+702x^5+705x^4\le2118x^2<3242x^2
\]

proves the second. No univariate root isolation is required.

Using `U<=1/6` only for the nonpositive contributions gives

\[
\begin{aligned}
H\ge L(x):={}&\frac{27}4x^7+\frac{303}4x^6-\frac{123}4x^5
+\frac{16573}{48}x^4-\frac{435}2x^3\\
&+\frac{17675}{36}x^2-\frac{20918}{81}x+\frac{464137}{1944}.
\end{aligned}
\tag{4.2}
\]

Absorb the negative fifth-degree term into the fourth-degree term, and the negative cubic into the quadratic. Then

\[
L(x)\ge
\frac{9845}{36}x^2-\frac{20918}{81}x+\frac{464137}{1944}
\ge270x^2-260x+238.
\]

Finally,

\[
270x^2-260x+238
=270\left(x-\frac{13}{27}\right)^2+\frac{4736}{27}>175.
\]

It follows that

\[
\boxed{-B_2>2800,\qquad \mathcal B_{ee}=2B_2<-5600.}
\tag{4.3}
\]

The complete argument consists of the displayed coefficient identity and elementary inequalities between powers on `[0,1]`. The former `minus_B_e2` SOS certificate is removed.

### 5. An analytic endpoint bound Bcal(m,U,m)>210

Set

\[
x=1-2m,\qquad t=6U,\qquad 0\le x,t\le1.
\]

Define

\[
\begin{aligned}
R_0={}&190+1342x+526x^2+3118x^3-114x^4+1630x^5\\
&-198x^6+138x^7-27x^8-27x^9,\\
R_1={}&198970-23352x+80802x^2+985572x^3-262845x^4\\
&+810405x^5-12393x^6+110079x^7+34992x^8-13122x^9,
\end{aligned}
\]

\[
f_0=385+\frac{1-x}{2}R_0,
\qquad f_1=\frac{75368}{243}+\frac{1-x}{972}R_1,
\]

and

\[
c(x)=\frac{70713x^8+94770x^6-177066x^5-121869x^4-436590x^3+87306x^2+57614x+220506}{972}.
\tag{5.1}
\]

There is an exact identity

\[
\begin{aligned}
\mathcal B(m,U,m)
={}&(1-t)f_0+t f_1-c(x)t(1-t)\\
&+\sum_{j=3}^7\bigl(P_j(x)t^j+N_j(x)t^2(1-t^{j-2})\bigr).
\end{aligned}
\tag{5.2}
\]

Every `P_j,N_j` has positive coefficients:

| j | P_j(x) | N_j(x) |
|---:|---|---|
| 3 | `(2784x^4+2768x^3+2049x^2)/54` | `(2430x^7+351x^6+1932x^5+3320x+136)/54` |
| 4 | `(3807x^6+108x^5+279x^4+1392x^3+118x^2)/324` | `(4360x+2362)/324` |
| 5 | `(27x^3+291x+65)/162` | `(117x^5+18x^4+470x^2)/162` |
| 6 | `(38x^2+106x+37)/486` | `(90x^4+27x^3)/486` |
| 7 | `(12x^3+6x^2+1)/486` | `5x/486` |

Thus the sum in (5.2) is nonnegative.

All negative terms of `R_0` are absorbed by lower powers:

\[
3118x^3-114x^4\ge3004x^3,
\]
\[
1630x^5-198x^6\ge1432x^5,
\]
\[
138x^7-27x^8-27x^9\ge84x^7.
\]

So `R_0>0` and `f_0>=385`. Similarly,

\[
198970-23352x\ge175618,
\]
\[
985572x^3-262845x^4\ge722727x^3,
\]
\[
810405x^5-12393x^6\ge798012x^5,
\]
\[
34992x^8-13122x^9\ge21870x^8.
\]

Hence `R_1>0` and `f_1>=75368/243>310`.

For the coefficient `c(x)`, note that

\[
70713x^8+94770x^6\le165483x^5<177066x^5.
\]

Dropping the other negative contributions gives

\[
c(x)\le\frac{87306+57614+220506}{972}<400.
\]

Since `t(1-t)<=1/4`, (5.2) yields

\[
\boxed{\mathcal B(m,U,m)>310-400/4=210.}
\tag{5.3}
\]

This removes `B_at_m`. Together with Section 4 and the two retained lower-endpoint signs for `Bcal`, it supplies the same concavity interpolation used in the full F argument.


## Supplement 8: Zero affine endpoint

#### 6.1 Endpoint U=0, e=m

For `0<=m<=1/3`, put `x=1-3m`. Direct substitution gives

\[
\Pi(m,0,m)=\frac8{19683}(2m-1)^2T_0(x),
\tag{6.1}
\]

where

\[
\begin{aligned}
T_0={}&5950089+6245545x+3511089x^2+508925x^3\\
&-3979797x^4-2670105x^5-2294523x^6-675504x^7\\
&-279300x^8-6864x^9+2864x^{10}+4992x^{11}+832x^{12}.
\end{aligned}
\]

All negative terms have degree at least four. On `[0,1]`, absorb them using the positive terms of degrees one, two, and three:

\[
6245545+3511089+508925
-(3979797+2670105+2294523+675504+279300+6864)=359466>0.
\]

Therefore

\[
T_0(x)\ge5950089+359466x^4>0.
\]

Since `(2m-1)^2>0` in this interval, the endpoint is strictly positive. The former univariate SOS-plus-remainder check is unnecessary.


## Supplement 9: One-interval shared-boundary Taylor proof

### 7. One boundary estimate covers the whole main interval

Coordinatewise monotonicity from Section 3 gives

\[
\Pi(m,r,r)\ge
\begin{cases}
\Pi(m,b_0,b_0),&0\le m\le1/5,\\
\Pi(m,q,q),&1/5\le m\le1/2.
\end{cases}
\]

The earlier elementary estimate `Pi(m,b_0,b_0)>103` for `m<=1/5` is retained, as is the degree-eight proof `q<=r`.

For the main interval define

\[
F(m)=\Pi(m,q(m),q(m)),\qquad x=m-\frac{41}{100}.
\]

Then `-21/100<=x<=9/100`. Write

\[
F(m)=\sum_{k=0}^{27}a_kx^k.
\]

The following coefficient bounds are checked exactly from the unchanged polynomial formulas:

\[
a_0>\frac{16}{25},\quad |a_1|<10,\quad a_2>5500,
\]
\[
-17500<a_3<-17400,\qquad a_4>-73000,
\]
\[
|a_5|<32000,\quad |a_6|<183000,\quad |a_7|<655000,
\]
\[
|a_k|<6000000\ (8\le k\le12),\qquad
|a_k|<34000000\ (13\le k\le27).
\tag{7.1}
\]

These are retained finite coefficient computations, not analytic consequences assumed without checking.

Write `a_3=-17500+delta`, with `0<delta<100`. Since `x>=-21/100`,

\[
a_3x\ge-17500x-21.
\]

The quadratic

\[
G(x)=5500-17500x-73000x^2-21
\]

is concave. Its minimum on the interval is at an endpoint, and

\[
G(-21/100)=\frac{59347}{10},\qquad
G(9/100)=\frac{33127}{10}.
\]

For `R=21/100`, the terms of degree at least five contribute in absolute value at most `x^2 T`, where

\[
\begin{aligned}
T={}&32000R^3+183000R^4+655000R^5\\
&+6000000\sum_{j=6}^{10}R^j+
34000000\frac{R^{11}}{1-R}<1600.
\end{aligned}
\tag{7.2}
\]

It follows that

\[
F(m)>\frac{16}{25}-10|x|+1700x^2.
\]

Complete the square in `|x|`:

\[
\boxed{
F(m)>\frac{16}{25}-\frac{100}{4\cdot1700}
=\frac{1063}{1700}>\frac35.
}
\tag{7.3}
\]

Unlike the earlier proof, this covers all of `[1/5,1/2]`; there is no separate division at `m=31/100`.

The improvement is obtained by retaining the sign of the cubic term on the asymmetric interval. Bounding that term by `-|a_3||x|` would lose the useful positive contribution on the longer left side.

Combining the small-`m` and main-interval estimates proves

\[
\boxed{\Pi(m,r,r)>1063/1700.}
\]

This is a lower bound for the specified normalization of `Pi`, not a numerical lower bound of the same size for the geometric tangent residual.


## Supplement 10: Increment polynomial and intercept

### 3. Work with an increment polynomial, not a second derivative

Define
\[
Q(m,U)=\Pi_U(m,U,b_0(m)),\qquad Q_0(m)=Q(m,0).
\]
Since the polynomial `Q(m,U)-Q(m,0)` is divisible by `U`, there is a polynomial
\[
\boxed{R(m,U)=\frac{Q(m,U)-Q(m,0)}{U}.}
\tag{3.1}
\]
At `U=0`, use that polynomial's value, equivalently `Q_U(m,0)`. Thus there is no singularity and no division-by-zero assumption.

The main quantitative lemma is
\[
\boxed{R(m,U)>25000\quad\text{on }\mathcal R.}
\tag{3.2}
\]
Notice what (3.2) does and does not say. It proves that `Q` lies above the line `Q0+25000U`. It is an increment bound; it does not claim `Q_U>=25000`, and the proof does not need that stronger derivative claim.

#### 3.1 First fixed chart

For `0<=m<=1/4`, set
\[
m=\frac{1+s}{8},\qquad U=\frac{1+t}{12},\qquad -1\le s,t\le1.
\]
Exact coefficient arithmetic gives
\[
\boxed{
R>43400+4600s^2+(4700t-5400)s-720t^2-10700t.
}
\tag{3.3}
\]
Complete the square in `s`. The right-hand side is at least
\[
43400-720t^2-10700t-\frac{(4700t-5400)^2}{18400}.
\]
This is concave in `t`, so its minimum on `[-1,1]` is at an endpoint. The two endpoint values are
\[
\frac{1469855}{46},\qquad \frac{2200455}{46}.
\]
Consequently
\[
R>\frac{1469855}{46}>31900
\quad(0\le m\le1/4).
\tag{3.4}
\]

#### 3.2 Second fixed chart

For `1/4<=m<=1/2`, set
\[
m=\frac{3+s}{8},\qquad U=\frac{1+t}{12},\qquad -1\le s,t\le1.
\]
The second exact coefficient bound is
\[
\boxed{
R>40580+11510s^2+(13385t+19015)s+2171t^2+5125t.
}
\tag{3.5}
\]
Completing the square in `s` leaves
\[
40580+2171t^2+5125t-\frac{(13385t+19015)^2}{46040}.
\]
Its `t^2` coefficient is negative. Its endpoint values are
\[
\frac{28861276}{1151},\qquad \frac{85030207}{2302}.
\]
Therefore
\[
R>\frac{28861276}{1151}>25000
\quad(1/4\le m\le1/2).
\tag{3.6}
\]
Together, (3.4) and (3.6) prove (3.2).

#### 3.3 What exactly is checked in (3.3) and (3.5)

Write the transformed increment polynomial minus the stated nonconstant quadratic as
\[
b+\sum_{i+j>0}c_{ij}s^it^j.
\]
Retain every positive even-even monomial as a nonnegative term. For every other monomial use
\[
c_{ij}s^it^j\ge-|c_{ij}|\qquad(|s|,|t|\le1).
\]
Let `L` be the sum of the absolute values of those other coefficients. Then the exact lower constant is `b-L`.

The program obtains:

| Chart | Exact constant `b` | Exact `b-L` | Lower constant used |
|---|---|---|---:|
| `m=(1+s)/8` | `230987404376132099/4696546738176` | `51047093775242087/1174136684544` | 43400 |
| `m=(3+s)/8` | `45508099326242071/782757789696` | `95304134251780469/2348273369088` | 40580 |

The first chart has 18 positive even terms and 86 signed terms; the second has 23 positive even terms and 81 signed terms. Both are total-degree-14 polynomials, with 105 terms including the constant.

These are two fixed, predetermined rational coefficient comparisons. There is no adaptive subdivision, optimization, interval-arithmetic tolerance, or numerical sampling in their verification. They remain finite computational checks; the table is not offered as a claim that 208 nonconstant coefficients can simply be ignored.

The same remainder can be written as a constrained-SOS identity using
\[
1\pm AB=\frac12(A\pm B)^2+\frac12(1-A^2)+\frac12(1-B^2)
\]
and the finite geometric-series identities for `1-A^2`. The new verifier does not need another stored SOS witness file for these fixed quadratics.

### 4. An explicit lower bound for the U=0 intercept

In the coordinate `x=1-2m`, put
\[
A(x)=-2985+503x+\frac{12515}{2}x^2.
\]
There is the exact identity
\[
8\bigl(Q_0((1-x)/2)-A(x)\bigr)=M(x),
\tag{4.1}
\]
where
\[
\begin{aligned}
M(x)={}&83782x^4+64114x^6+18944x^8+2828x^{10}\\
&+114234x^2(1-x)+189651x^4(1-x)\\
&+122145x^6(1-x)+45336x^8(1-x)\\
&+13312x^{10}(1-x)+732x^{10}(1-x^2)\\
&+3201x^{12}(1-x)+189x^{12}(1-x^2)
+81x^{12}(1-x^3).
\end{aligned}
\tag{4.2}
\]
Every term is nonnegative for `0<=x<=1`. Thus
\[
\boxed{Q_0(m)\ge A(1-2m).}
\tag{4.3}
\]
This is an explicit power-grouping identity, not a coefficient-budget estimate.

By (3.1), (3.2), and (4.3),
\[
Q(m,U)\ge A(x)+25000U.
\]
For `U>=b0=(1-x^2)/8`, this becomes
\[
\boxed{
\Pi_U(m,U,b_0)\ge
140+503x+\frac{6265}{2}x^2+25000(U-b_0)>0.
}
\tag{4.4}
\]
The right-hand side is at least 140. This replaces `Pu_at_b0_restricted`, the old 12-square, degree-15 target with 120 nonconstant remainder coefficients.

Since the retained `Pi_Ue>0` lets the derivative increase when `e` is increased from `b0` to `r`, the constant-radius proof continues unchanged:
\[
\Pi_U(m,U,r)\ge\Pi_U(m,U,b_0)>0\qquad(U\ge r\ge b_0).
\]
The coordinatewise monotonicity used at the shared boundary also remains valid.


## Supplement 11: Sharp local derivative and endpoint

### 7. Stronger direct proof on the endpoint-transfer domain

For the endpoint argument only, one can do better without the mixed-derivative certificate. Assume `1/3<=m<=1/2`, so `x=1-2m` lies in `[0,1/3]`. Expand
\[
\Pi_U((1-x)/2,U,1/3)=\sum_{j=0}^{10}a_j(x)U^j.
\]
Whenever a coefficient in `a_j` is negative and has odd degree `i`, use
\[
x^i\le\frac{x^{i-1}}3
\]
for that negative term. The generated lower polynomials for `j>=1` are printed in Appendix B.

For `a0`, keep its linear term and apply this operation only to negative odd terms of degree at least three. It gives
\[
\begin{aligned}
a_0(x)\ge{}&10880-\frac{13376}{3}x+\frac{1193024}{27}x^2\\
&+\frac{563908}{9}x^4+\frac{1294762}{27}x^6
+\frac{189044}{9}x^8+5838x^{10}+828x^{12}.
\end{aligned}
\]
Complete the square in the first three terms and drop the remaining positive terms:
\[
\boxed{a_0(x)\ge\frac{200717392}{18641}>10700.}
\tag{7.1}
\]

The remaining coefficient bounds are
\[
\begin{array}{c|rrrrrrrrrr}
j&1&2&3&4&5&6&7&8&9&10\\\hline
 a_j\text{ lower bound}&34000&0&-500000&0&0&-3000000&-2000000&0&0&0.
\end{array}
\tag{7.2}
\]
For `0<=U<=1/6`,
\[
\begin{aligned}
\sum_{j=1}^{10}a_jU^j
&\ge U(34000-500000U^2-3000000U^5-2000000U^6)\\
&\ge\frac{14348500}{729}U\ge0.
\end{aligned}
\]
Thus
\[
\boxed{\Pi_U(m,U,1/3)>10700\quad(1/3\le m\le1/2).}
\tag{7.3}
\]

#### 7.1 Simpler and stronger endpoint transfer

An exact even-polynomial identity is
\[
\Pi((1-x)/2,0,1/3)
=\frac{3159x^{14}+26163x^{12}+126501x^{10}+376529x^8
+664736x^6+603680x^4+160512x^2-6912}{72}.
\]
In particular,
\[
\Pi(m,0,1/3)\ge-96+\frac{6688}{3}x^2.
\]
If `U>=(m-1/3)/3=(1-3x)/18`, then (7.3) implies
\[
\Pi(m,U,1/3)\ge
-96+\frac{6688}{3}x^2+\frac{10700}{18}(1-3x).
\]
The last quadratic is decreasing on `[0,1/3]`: its derivative at the right endpoint is `-2674/9`, and its derivative is increasing. Its minimum is therefore its value at `x=1/3`:
\[
\boxed{
\Pi(m,U,1/3)\ge\frac{4096}{27}>151.
}
\tag{7.4}
\]
The actual affine endpoint `U3=(m-1/3)/kappa` belongs to this region because `kappa<=3`. This replaces the prior degree-14 endpoint coefficient-pairing check, not just its derivative transfer. The `m<=1/3` endpoint argument is unchanged.

The local proof is an additional explicit coefficient-dominance calculation. Its arithmetic is accounted for separately from both the seven retained SOS checks and the two increment remainder checks. The global proof in Section 6 is useful for replacing the original full-rectangle target; the stronger local proof is useful for simplifying its application.


## Supplement 12: All local-derivative coefficient bounds

### Appendix B. Explicit coefficient bounds for the sharper local derivative

The following are the lower polynomials obtained from the `U^j` coefficients by replacing each negative odd power with its valid lower value at `x<=1/3`. This replacement is applied coefficientwise, not asserted from sampling. Positive terms may then be dropped; any remaining negative monomials are bounded using `x<=1/3`.

#### U power 1

```text
7722*x**12 + 56472*x**10 + 219742*x**8 + 1364684*x**6/3 + 1568068*x**4/3 + 2519776*x**2/9 + 309440/9
```

Exact scalar lower bound: `309440/9`. Bound used in the proof: `34000`.

#### U power 2

```text
183006*x**10 + 907458*x**8 + 2195288*x**6 + 24628312*x**4/9 + 10558240*x**2/9 + 905984/9
```

Exact scalar lower bound: `905984/9`. Bound used in the proof: `0`.

#### U power 3

```text
139536*x**10 + 1877856*x**8 + 6285120*x**6 + 8455920*x**4 + 43808480*x**2/9 - 1265792/3
```

Exact scalar lower bound: `-1265792/3`. Bound used in the proof: `-500000`.

#### U power 4

```text
1913760*x**8 + 9460000*x**6 + 17877520*x**4 + 276999680*x**2/27 + 1647280/3
```

Exact scalar lower bound: `1647280/3`. Bound used in the proof: `0`.

#### U power 5

```text
313632*x**8 + 8218080*x**6 + 21176448*x**4 + 15938112*x**2 + 1829168/3
```

Exact scalar lower bound: `1829168/3`. Bound used in the proof: `0`.

#### U power 6

```text
2501856*x**6 + 14645792*x**4 + 47871712*x**2/3 - 67528160/27
```

Exact scalar lower bound: `-67528160/27`. Bound used in the proof: `-3000000`.

#### U power 7

```text
-214272*x**6 + 4065024*x**4 + 8294400*x**2 - 2996224/3
```

Exact scalar lower bound: `-26973952/27`. Bound used in the proof: `-2000000`.

#### U power 8

```text
311040*x**5 - 1244160*x**4 + 3456*x**3 + 2802816*x**2 + 2072576
```

Exact scalar lower bound: `2057216`. Bound used in the proof: `0`.

#### U power 9

```text
-138240*x**4 + 1382400*x**3 - 537600*x**2 + 3708160/3
```

Exact scalar lower bound: `3523840/3`. Bound used in the proof: `0`.

#### U power 10

```text
112640 - 608256*x**2
```

Exact scalar lower bound: `45056`. Bound used in the proof: `0`.


## Supplement 13: Affine curvature with the current slope

### 2. Setup and the simpler slope

Write

\[
a=1-m,\qquad b=m+U,\qquad
\rho=a^2+ab+b^2,\qquad D^2=K=4\rho-3.
\]

The physical F domain is contained in \(\mathcal R\). In the affine-radius branch, \(m\) is fixed and

\[
e(U)=m-\kappa U,
\qquad
\kappa\ge\kappa_0(m):=1+\frac m2+2m^2.
\]

The previous radius comparison gives this bound and the restriction \(0\le e\le1/3\) on the part requiring the tangent argument.

The new slope is the tangent line to \(\kappa_0\) at \(m=1/2\). Its validity needs only

\[
\boxed{
\kappa_0(m)-\ell(m)=2\left(m-\frac12\right)^2\ge0.
}
\tag{2.1}
\]

Thus \(\kappa\ge\ell\ge1/2>0\). This replaces the less simple constants in \(\ell_{\rm old}\); the point construction and radius itself are unchanged.

Define, with all derivatives evaluated at the same \((m,U,e)\),

\[
S_k(e)=\Pi_{UU}-2k\Pi_{Ue}+k^2\Pi_{ee}.
\tag{2.2}
\]

For fixed \(m\), the second derivative of \(f(U)=\Pi(m,U,m-\kappa U)\) is \(S_\kappa(e(U))\).

### 3. A canonical bounded basis for the remainder

Normalize

\[
s=4m-1,\qquad t=12U-1,
\qquad -1\le s,t\le1,
\]

and set

\[
F(s,t)=\frac1{100}H\left(\frac{1+s}{4},\frac{1+t}{12}\right).
\]

Let \(T_n\) be the Chebyshev polynomials defined by

\[
T_0(z)=1,\quad T_1(z)=z,\quad
T_{n+1}(z)=2zT_n(z)-T_{n-1}(z).
\]

They obey \(|T_n(z)|\le1\) for \(-1\le z\le1\). For example, the recurrence gives \(T_n(\cos\theta)=\cos(n\theta)\). An algebraic certificate for the same bound is

\[
T_n(z)^2+(1-z^2)U_{n-1}(z)^2=1\quad(n\ge1),
\tag{3.1}
\]

where \(U_j\) denotes the second-kind Chebyshev polynomial, not the geometric parameter \(U\). The verifier checks these polynomial identities for every needed degree.

Expand uniquely

\[
F(s,t)=\sum_{i,j}c_{ij}T_i(s)T_j(t).
\]

The conversion is exact. For \(n\ge1\),

\[
z^n=2^{1-n}\sum_{0\le j<n/2}\binom njT_{n-2j}(z)
 +\mathbf 1_{2\mid n}\,2^{-n}\binom n{n/2}.
\tag{3.2}
\]

Apply this formula to both variables in each monomial. The new verifier uses rational arithmetic and verifies that the reconstructed tensor-Chebyshev sum equals the original polynomial. There is no sampled or approximate transform.

#### Cubic comparison

Use the following ten-coefficient approximation:

\[
\begin{aligned}
g(s,t)={}&679-23T_1(s)+197T_1(t)-92T_2(s)
 +226T_1(s)T_1(t)-17T_2(t)\\
&+19T_3(s)-80T_2(s)T_1(t)
 +52T_1(s)T_2(t)-2T_3(t).
\end{aligned}
\tag{3.3}
\]

In ordinary powers this is

\[
\boxed{
\begin{aligned}
g(s,t)={}&76s^3-160s^2t-184s^2+104st^2+226st-132s\\
&-8t^3-34t^2+283t+788.
\end{aligned}
}
\tag{3.4}
\]

Let \(\widehat c_{ij}\) be the ten coefficients in (3.3). Exact coefficient arithmetic gives:

| Group | Sum being bounded | Strict upper bound |
|---|---|---:|
| Total degree at most 3 | \(\sum_{i+j\le3}|c_{ij}-\widehat c_{ij}|\) | \(31/10\) |
| Total degree 4 | \(\sum_{i+j=4}|c_{ij}|\) | \(38\) |
| Total degree 5 | \(\sum_{i+j=5}|c_{ij}|\) | \(17/2\) |
| Total degree 6 | \(\sum_{i+j=6}|c_{ij}|\) | \(15/4\) |
| Total degree 7 | \(\sum_{i+j=7}|c_{ij}|\) | \(1/2\) |
| Total degrees 8 through 14 | \(\sum_{i+j\ge8}|c_{ij}|\) | \(17/100\) |

The sum of the displayed bounds is

\[
\frac{31}{10}+38+\frac{17}{2}+\frac{15}{4}+\frac12+\frac{17}{100}
=\frac{2701}{50}<55.
\]

Because every \(T_i(s)T_j(t)\) has absolute value at most one,

\[
\boxed{|F(s,t)-g(s,t)|<\frac{2701}{50}<55.}
\tag{3.5}
\]

For reproducibility, the exact total coefficient error is

\[
\frac{4741325476795649}{88060251340800},
\]

approximately 53.84183447815. The decimal is not used by the verifier.

There are 113 nonzero coefficients: ten in the degree-at-most-three comparison and 103 of higher degree. `verification.json` records all of them, the six exact sums, and their bounds. These coefficient inequalities are the computational input of the new lemma. The table does not purport to establish them without expansion.

### 4. The cubic is positive by one square and nonnegative products

Put

\[
X=1-s,\qquad Y=1+t,
\qquad 0\le X,Y\le2.
\]

Substitution in (3.4) gives

\[
g=277+74X+X^2(204-76X)+YB(X,Y),
\tag{4.1}
\]

where

\[
B(X,Y)=185+302X-160X^2+94Y-104XY-8Y^2.
\]

This auxiliary quadratic has the exact decomposition

\[
\begin{aligned}
B={}&\frac{185}{4}(2-X)(2-Y)+\frac{149}{4}X(2-Y)
 +\frac{341}{4}(2-X)Y-\frac{111}{4}XY\\
&+160X(2-X)+8Y(2-Y).
\end{aligned}
\tag{4.2}
\]

Every term except the explicitly negative \(XY\) term is nonnegative. Hence

\[
B\ge-\frac{111}{4}XY,
\qquad
YB\ge-111X
\]

because \(Y^2\le4\). Also \(204-76X\ge52\). Consequently

\[
\begin{aligned}
g&\ge277-37X+52X^2\\
 &=270+52\left(X-\frac{37}{104}\right)^2+\frac{87}{208}\\
 &\ge270+\frac{87}{208}>270.
\end{aligned}
\tag{4.3}
\]

For readers preferring one identity instead of successive inequalities, the same proof is

\[
\begin{aligned}
g-270={}&52\left(X-\frac{37}{104}\right)^2+\frac{87}{208}
 +76X^2(2-X)+\frac{111}{4}X(4-Y^2)\\
&+Y\left\{
\frac{185}{4}(2-X)(2-Y)+\frac{149}{4}X(2-Y)
+\frac{341}{4}(2-X)Y\\
&\hspace{22mm}+160X(2-X)+8Y(2-Y)
\right\}.
\end{aligned}
\tag{4.4}
\]

All summands are nonnegative on the stated box. This is a direct constrained-positive-product identity; no searched Gram matrix or numerical optimizer is involved in checking it.

Combining (3.5) and (4.3),

\[
\frac{H}{100}=F>270-55=215.
\]

This proves the uniform bound (1.1).

### 5. The original affine-path conclusion follows with a quantitative margin

Three retained derivative signs are

\[
H_1=-\Pi_{Uee}>0,
\quad H_2=\Pi_{UUe}(m,U,0)-2\Pi_{Uee}>0,
\quad H_3=\Pi_{UUe}(m,U,1/3)-2\Pi_{Uee}>0.
\]

They are unchanged from the supplied seven-sign stage. Since \(\Pi\) is quadratic in \(e\),

\[
\partial_e S_\kappa(e)
=(1-3e)H_2+3eH_3+2(\kappa-1)H_1>0
\]

for the actual \(\kappa\ge1\) and \(0\le e\le1/3\). Thus

\[
S_\kappa(e)\le S_\kappa(1/3).
\]

The unchanged four-square mixed-derivative certificate gives \(\Pi_{Ue}>0\). The analytic weighted-conjugate identity gives \(\Pi_{ee}<0\) on the physical and auxiliary integration paths needed here. Therefore

\[
\partial_k S_k(e)=-2\Pi_{Ue}+2k\Pi_{ee}<0
\qquad(k\ge0).
\]

By (2.1), \(\kappa\ge\ell>0\), so

\[
\boxed{
S_\kappa(e)\le S_\kappa(1/3)
\le S_\ell(1/3)<-21500.
}
\tag{5.1}
\]

The order of the comparisons matters: the radius comparison uses the actual \(\kappa\ge1\); only afterward is the slope lowered to \(\ell\), which can be less than one.

The new polynomial estimate (1.1) holds on the full rectangle. The inequality \(\Pi_{ee}<0\) used for slope transfer is not silently extended to nonphysical points with \(D>1\). Its preceding proof establishes \(D<1\) on the affine integration path \(0<U\le r(m)\); that restriction is preserved.

Thus, for a nondegenerate affine interval \([\alpha,\beta]\),

\[
f(U)=\Pi(m,U,m-\kappa U)
\]

satisfies the stronger chord bound

\[
\boxed{
f(U)\ge
\frac{\beta-U}{\beta-\alpha}f(\alpha)
+\frac{U-\alpha}{\beta-\alpha}f(\beta)
+10750(U-\alpha)(\beta-U).
}
\tag{5.2}
\]

Indeed subtract the last quadratic and use concavity. Existing endpoint positivity proves the desired positivity throughout; the extra term is not needed to finish the theorem, but it quantifies the new curvature margin. A degenerate interval is handled by its endpoint value.
