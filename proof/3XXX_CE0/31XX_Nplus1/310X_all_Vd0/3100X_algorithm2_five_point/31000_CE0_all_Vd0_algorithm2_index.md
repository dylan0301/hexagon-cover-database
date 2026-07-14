# CE0 All-Vd0 Algorithm-2 Five-Point Proof Tree

Status: Strategy

This is a paper-style proof-tree scaffold for the existing `3100X`
algorithm-2 five-point route inside the `310X` all-Vd0 package. It is not
itself a proof of the branch. Each statement below keeps the status of the
numbered note that supports it.

## Main Branch Target

**Route `3100X` (Status: Strategy).** Assume a hypothetical seven-triangle
cover lies in the branch

$$
T_C\text{ is CE0},\qquad N_+=1,
$$

and all six vertex roles are Vd0. The goal of this route is to prove that this
branch cannot occur.

By cyclic symmetry, take the unique supercritical row to be the $V_4$ row:

$$
a_4+b_4>1.
$$

The intended obstruction is a five-point set

$$
K_5=\left\{P_3,P_5,D_0,D_1,D_2\right\}.
$$

The branch is closed if every remaining admissible configuration forces

$$
\Lambda(K_5)>1,
$$

equivalently, no closed unit equilateral triangle contains the five obstruction
points.

## Setup And Notation

The far-from-tight coordinates are

$$
p=1-b_4,\qquad q=1-a_4.
$$

In the lower symmetric half, the proof tree takes

$$
p\le q.
$$

The displayed ordered-half formulas below should be used with the convention
from
[`2004_admissible_set.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md):
$m=\min(p,q)$ and $M=\max(p,q)$. Thus in the half written here $m=p$ and
$M=q$; in the reflected half $p>q$, use $m=q$ and $M=p$.

The close-to-tight coordinates near the lower vertex-limit corner are

$$
a_4=(1+k)x,\qquad b_4=1-x,
$$

with remaining free parameters $s,\tau$ satisfying

$$
0\le s\le\tau\le1.
$$

The live branch splits into two complementary subtrees:

| Number | Recorded status | Mathematical role |
|---|---|---|
| `310X` | Strategy | Full CE0, $N_+=1$, all-Vd0 branch target. |
| `3100X` | Strategy | Existing algorithm-2 five-point route. |
| `31002` | Reference | Status ledger and open assembly obligations. |
| `3100aX` | Strategy | Far-from-tight algorithm-2 subtree. |
| `3100a1` | Reference | Far-from-tight status and remaining certificate obligations. |
| `3100a2` | Strategy | Five-point construction and algorithm-2 diagonal choices. |
| `3100a5` | Proven | Strict $\rho<1$ line realization for $P_3,P_5$. |
| `3100a6` | Strategy | Exact two-variable reduction and radial formulas; transition use needs selector-aware rechecking. |
| `3100a8` | Proven | Convex cyclic order and five support-edge reduction. |
| `3100a9` | Empirical | Transition-strip computation and certificate outline. |
| `3100b2` | Practically proven | Close-to-tight diagonal remainder estimates. |
| `3100b3` | Lemma target | Final close-to-tight two-variable inequality. |
| `3100b5` | Proven | Algorithm-1 tangent gap. |

## Reductions

**Reduction Target `31002` (Recorded status: Reference).** The full all-Vd0
branch still needs a proof reducing the original row data to

$$
a_3+b_3=1,\qquad a_5+b_5=1.
$$

This equality reduction is an open assembly obligation. It is not proved by
the current `3100X` files.

**Construction `3100a2` (Status: Strategy).** After the cyclic normalization,
take $a_4,b_4$ as outer parameters and $a_1,b_1$ as the remaining free
variables. Under the equality assumptions

$$
a_3+b_3=1,\qquad a_5+b_5=1,
$$

the construction selects two fixed $V_4$ obstruction points $P_3,P_5$ and
three diagonal obstruction points $D_0,D_1,D_2$.

Algorithm 2 chooses $D_0,D_1,D_2$ by forcing two of the three nonsupercritical
rows among $V_0,V_1,V_2$ to lie on equality lines:

| Point | Equality pattern |
|---|---|
| $D_0$ | $a_1+b_1=1$ and $a_2+b_2=1$ |
| $D_1$ | $a_0+b_0=1$ and $a_2+b_2=1$ |
| $D_2$ | $a_0+b_0=1$ and $a_1+b_1=1$ |

The intended containment statement for these diagonal points in the relaxed
obstruction region remains part of the strategy; it is not yet a proved
lemma.

## Far-From-Tight Subtree

The far-from-tight subtree uses algorithm 2 away from the two vertex-limit
corners. The current cutoff is

$$
p\ge0.1,\qquad q\ge0.1.
$$

**Lemma `3100a5` (Status: Proven).** Assume the strict $V_4$ branch

$$
a+b>1,\qquad \rho=a^2+ab+b^2<1.
$$

Let $\Gamma_{AB}$ be the candidate strict non-axis chain, decomposed into the
four pieces

$$
\Gamma_A^{\mathrm{circ}},\quad
\Gamma_A^{\mathrm{lin}},\quad
\Gamma_B^{\mathrm{lin}},\quad
\Gamma_B^{\mathrm{circ}}.
$$

Then the radius-$1$ circle centered at the $C_2$ point meets
$\Gamma_{AB}$ exactly once, and this intersection lies on
$\Gamma_A^{\mathrm{lin}}$. By symmetry, the radius-$1$ circle centered at the
$C_5$ point meets $\Gamma_{AB}$ exactly once, and this intersection lies on
$\Gamma_B^{\mathrm{lin}}$.

This is an exact statement about the candidate chain.  Its use as the actual
$AB$-union frontier is conditional on lemma target `20091`.

The limiting boundary $\rho=1$ is not covered by `3100a5`.

**Reduction `3100a6` (Status: Strategy).** Under the equality assumptions

$$
a_3+b_3=1,\qquad a_5+b_5=1,
$$

algorithm 2 depends only on

$$
(p,q)=(1-b_4,1-a_4).
$$

All three diagonal choices use the same local pair $(p,q)$ and the same
diagonal coordinate

$$
c_*=c_{\max}(p,q),
$$

so

$$
D_j=(1-c_*)V_j,\qquad j=0,1,2.
$$

For $p\le q$, the selected diagonal branch is split by

$$
T(p,q)=(p+q)^4-(p+q)^2+pq.
$$

On the mixed branch,

$$
T(p,q)\ge0,\qquad
c_*=\frac{2q}{1+\sqrt{4(p+q)^2-3}}.
$$

On the quartic branch,

$$
T(p,q)\le0,\qquad
c_*^4-c_*^2+pc_*-p^2=0,\qquad c_*\ge p+q.
$$

At $T=0$, the two branches meet at $c_*=p+q$. The diagonal radius

$$
r=1-c_*
$$

is nondecreasing in both $p$ and $q$ on the recorded away region.

**Lemma `3100a8` (Status: Proven).** Once the strict line realization of `3100a5`
holds, write

$$
P_3=(u,v)\in\Gamma_A^{\mathrm{lin}},\qquad
P_5=(s,t)\in\Gamma_B^{\mathrm{lin}}.
$$

Then

$$
s\ge u,\qquad v\ge t.
$$

Consequently, for any $r\ge0$, the five points

$$
D_0=rV_0,\qquad D_1=rV_1,\qquad D_2=rV_2,\qquad P_3,\qquad P_5
$$

have cyclic convex order

$$
D_0,D_1,D_2,P_3,P_5,
$$

away from degeneracies. Therefore the algorithm-2 support check reduces to the
five hull-edge cases

$$
D_0D_1,\quad D_1D_2,\quad D_2P_3,\quad P_3P_5,\quad P_5D_0.
$$

**Computation `3100a9` (Status: Empirical).** On the transition strip

$$
0.1\le p\le0.15,\qquad p\le q,
$$

the recorded computation gives a certificate outline for the five support-edge
checks after `3100a8`. The dangerous edge is $P_3P_5$, with recorded numerical
lower value

$$
1.0031590223\ldots
$$

at the transition point. The non-dangerous edges are handled by interval and
denominator-free lower-bound checks recorded in `3100a9`.

This is not a proof-level certificate. To upgrade this computation, the branch
needs recorded interval subdivision data or verifier code, including the
selected-root checks for the line-circle intersections.

**Far-From-Tight Assembly Target `3100a1` (Recorded status: Reference).** The
far-from-tight subtree will be complete after all of the following are proved:

| Obligation | Current status |
|---|---|
| Upgrade the `3100a9` transition-strip outline to a proof-level certificate. | Open |
| Prove the farther region $p\ge0.15$ and the reflected half. | Open |
| Treat the limiting boundary $\rho=1$. | Open |
| Prove the algorithm-2 diagonal points are valid obstruction points for the exact relaxed region. | Open |

## Close-To-Tight Subtree

The close-to-tight subtree uses algorithm 1 near the vertex-limit corners,
where algorithm 2 is known not to suffice uniformly.

**Lemma `3100b5` (Status: Proven).** In the lower vertex-limit scaling

$$
a_4=(1+k)x,\qquad b_4=1-x,\qquad x\downarrow0,
$$

with

$$
0\le k\le1,\qquad 0\le s\le\tau\le1,
$$

define

$$
d_0=\max\left(\frac12,\ 1-k+k\tau\right),
$$

$$
d_1=\max\left(\frac{1+k-k\tau}{2},\ 1+k-2k\tau+ks\right),
$$

and

$$
d_2=\max\left(\frac{1+k-ks}{2},\ 1+k-2ks\right).
$$

The limiting support coefficient

$$
C_1(k,s,\tau)=\max(d_0,d_1)+d_2-\frac{3-k}{2}
$$

satisfies

$$
C_1(k,s,\tau)\ge\frac14.
$$

This proves only the first-order tangent gap. It does not prove the finite-$x$
close-to-tight branch.

**Reduction `3100b1` (Status: Lemma target).** The finite-$x$ close-to-tight
target is

$$
f_{\mathrm{algo1}}(x,k,s,\tau)\ge1+xC_1(k,s,\tau)
$$

on the valid near-limit domain. The dominant-branch residual is reduced to

$$
R_+\ge P_{\mathrm{res}}+E_{01}+E_2.
$$

**Working Lemma `3100b2` (Status: Practically proven).** The recorded diagonal
remainder estimates are

$$
E_{01}\ge-2x^2,\qquad E_2\ge-kx^2.
$$

The $E_{01}$ proof tree splits into:

| Case | Current status |
|---|---|
| $d_0$-selected case | Working estimate recorded |
| $d_1$-selected actual mixed branch | Working estimate recorded |
| $d_1$-selected actual quartic branch with $A\le2H$ | Working estimate recorded |
| $d_1$-selected actual quartic branch with $A>2H$ | Working estimate recorded |

The $E_2$ proof tree splits into:

| Case | Current status |
|---|---|
| Actual mixed branch | Working estimate recorded |
| Actual quartic branch with $H\ge K/3$ | Working estimate recorded |
| Actual quartic branch with $H<K/3$ | Working estimate recorded |

The status is not `Proven` because the full Bernstein coefficient data or an
independently checkable exact certificate is not recorded.

**Target `3100b3` (Status: Lemma target).** After `3100b2`, the remaining
two-variable target is

$$
P_{\mathrm{res}}(x,k)\ge(2+k)x^2.
$$

Equivalently, with

$$
a=1-x,\qquad b=(1+k)x,
$$

it is

$$
P(a,b)\ge a^2-ab+\frac32b.
$$

The domain is

$$
0<x\le0.1,\qquad 0\le k\le k_{\max}(x),
$$

where

$$
k_{\max}(x)=\frac{-(1+x)+\sqrt{1+6x-3x^2}}{2x}.
$$

The current proof options recorded in `3100b3` are monotonicity of the scaled
margin in $x$, or a root-bound reduction for the selected line parameters.
Neither option is complete.

**Close-To-Tight Assembly Target `3100bX` (Status: Strategy).** The
close-to-tight subtree closes if `3100b3` is proved and the working estimates in
`3100b2` are upgraded or otherwise made rigorous enough for the final assembly.

## Full Branch Assembly

To make the `3100X` algorithm-2 route prove the `310X` target, the final
argument must combine the following pieces:

| Piece | Required conclusion | Current status |
|---|---|---|
| Equality reduction | Reduce the full all-Vd0 branch to $a_3+b_3=a_5+b_5=1$. | Open |
| Five-point construction | Define valid obstruction points for every remaining admissible configuration. | Strategy |
| Far-from-tight subtree | Prove $\Lambda(K_5)>1$ away from the vertex-limit corners. | Open |
| Close-to-tight subtree | Prove $\Lambda(K_5)>1$ near the vertex-limit corners. | Open |
| Branch gluing | Show the far and close regions cover the full normalized parameter domain. | Open |

Only after all rows in this assembly table are closed can this route close the
`310X` branch.

## Warnings And Failed Routes

| Number | Recorded status | Warning |
|---|---|---|
| `31004` | Failed | The May 21 four-point obstruction is not a live proof route for this branch. |
| `9631` | Failed | The May 25 CE0 supremum-endpoint route is archived and is not a live dependency. |

Numerical evidence, plotting evidence, and certificate outlines remain
empirical unless the numbered proof notes record a proof-level certificate.
