# Exact Maximal $B_c(a)$ Map

Status: Proven

This note defines the maximal outgoing-coordinate map by the exact admissible
set from [`2004_admissible_set.md`](2004_admissible_set.md). It also records an
exact counterexample to the former candidate-root maximum.

## Exact map

For $a,c\in[0,1]$, define

$$
B_c(a)=
\max\left\{b\in[0,1]:(a,b,c)\in\mathcal A\right\}.
$$

The fiber is nonempty because

$$
(a,0,c)\in\mathcal A
$$

for all $a,c\in[0,1]$: the unit triangle

$$
\mathrm{conv}\left\{0,e_A,e_R\right\}
$$

contains the three demanded points. Compactness of $\mathcal A$ gives the
maximum. Down-closedness gives the exact fiber identity

$$
\left\{b:(a,b,c)\in\mathcal A\right\}=[0,B_c(a)].
$$

Equivalently, if $K=P(a,b,c)$ and $L_K$ is the finite support expression in
`2004`, then

$$
\boxed{
B_c(a)=
\max\left\{
b\in[0,1]:
\min_{\phi\in\Theta_K}L_K(\phi)\le1
\right\}.
}
$$

This is an exact formula: $\Theta_K$ is a finite set of explicitly determined
breakpoint directions.

The defect map is

$$
g_c(a)=1-B_c(a).
$$

## Monotonicity and symmetry

If

$$
a_1\le a_2,
\qquad
c_1\le c_2,
$$

then inclusion of demand fibers gives

$$
B_{c_1}(a_1)\ge B_{c_2}(a_2).
$$

Thus $B_c(a)$ is nonincreasing in both demands and $g_c(a)$ is
nondecreasing.

Reflection in the radial line gives

$$
b\le B_c(a)
\quad\Longleftrightarrow\quad
a\le B_c(b).
$$

These statements use lower-bound demands. They do not by themselves classify
the actual realizing row as nonsupercritical or supercritical.

## Actual-coordinate classified maps

For a unit vertex triangle $T$ containing the normalized vertex, let

$$
A(T),
\qquad
B(T),
\qquad
C(T)
$$

be its actual maximal reaches on the incoming boundary edge, outgoing
boundary edge, and own radial arm.

For a row class $\mathcal R$, define the proof-safe classified envelope

$$
B_c^{\mathcal R}(a)=
\sup\left\{
B(T):
T\in\mathcal R,
A(T)\ge a,
C(T)\ge c
\right\},
$$

when the set is nonempty. The two maps needed by an all-Vd0, $N_+=1$
propagation are obtained from

$$
\mathcal R_0=
\left\{
T:T\text{ is Vd0 and }A(T)+B(T)\le1
\right\},
$$

and

$$
\mathcal R_+=
\left\{
T:T\text{ is Vd0 and }A(T)+B(T)>1
\right\}.
$$

Set

$$
g_c^{\mathcal R}(a)=1-B_c^{\mathcal R}(a).
$$

The same feasible-set inclusion proves that every classified $B$-map is
nonincreasing and every classified $g$-map is nondecreasing. Also

$$
B_c^{\mathcal R}(a)\le B_c(a)
$$

for either class. Therefore the unclassified map is a valid rowwise
relaxation, but it does not encode the condition $N_+=1$. A proof using the
classified branch must enumerate the supercritical index and use
$\mathcal R_+$ there and $\mathcal R_0$ at the other five rows.

The shortcut

$$
\max\left\{b:(a,b,c)\in\mathcal A, a+b\le1\right\}
$$

is not a definition of the nonsupercritical map: $a,b$ are demands, while the
classification concerns the actual reaches $A(T),B(T)$.

## Exact failure of the former candidate maximum

The previous version took the maximum of formal algebraic roots. The following
exact witness shows that rule was false.

Set

$$
a=\frac5{12},
\qquad
c=\frac{59}{60},
\qquad
b_0=\frac9{20}.
$$

For the four-point set $P(a,b_0,c)$, write

$$
A=a e_A,
\qquad
B=b_0e_B,
\qquad
C=c e_R.
$$

Take the outer-normal angle modulo
$120$ degrees in the interval from $-30$ degrees to $90$ degrees. Put

$$
\phi_1=arctan\left(-\frac5{59\sqrt3}\right),
\qquad
\phi_2=arctan\left(\frac9{59\sqrt3}\right).
$$

Direct comparison of the four projections gives the support-maximizer triples

$$
[B,C,0],
\quad
[C,C,0],
\quad
[C,A,0],
\quad
[C,A,B]
$$

on the four consecutive intervals cut by

$$
-30\text{ degrees},
\quad
\phi_1,
\quad
\phi_2,
\quad
30\text{ degrees},
\quad
90\text{ degrees}.
$$

On each interval the support sum $S$ is positive and satisfies

$$
S''=-S<0,
$$

so its minimum is at an endpoint. At the four multiples of $30$ degrees the
relevant values are

$$
\frac{\sqrt3}{2}(b_0+c)
\quad\text{or}\quad
\frac{\sqrt3}{2}(a+c),
$$

both strictly greater than $\sqrt3/2$. At $\phi_1$, the inequality
$S>\sqrt3/2$ is equivalent to

$$
c^4-c^2+b_0c-b_0^2
=
\frac{2696161}{12960000}>0.
$$

At $\phi_2$, it is equivalent to

$$
c^4-c^2+ac-a^2
=
\frac{2645761}{12960000}>0.
$$

Therefore the exact support criterion gives

$$
(a,b_0,c)\notin\mathcal A.
$$

Down-closedness then gives

$$
B_c(a)<\frac9{20}.
$$

By contrast, the former $D_+^-$ candidate was

$$
b_*=
\frac{38645-12\sqrt{10028761}}{1428}
>\frac9{20}.
$$

It satisfied every domain test listed there. For completeness,

$$
b_*<\frac7{12},
$$

and, with

$$
q(b)=(a+b)^4-(a+b)^2+ab,
$$

one has

$$
q\left(\frac9{20}\right)=\frac{451}{810000}>0,
\qquad
q'\left(\frac9{20}\right)=\frac{17377}{13500}>0,
$$

while $q''>0$ thereafter. Hence $q(b_*)>0$. The inequalities
$b_*>9/20$ and $b_*<7/12$ follow by squaring positive quantities:

$$
225(10028761)<47503^2,
\qquad
10028761>3151^2.
$$

Thus the old candidate rule asserted

$$
B_c(a)\ge b_*>\frac9{20},
$$

contradicting the exact support certificate. Those candidate sheets are not
part of the corrected map.
