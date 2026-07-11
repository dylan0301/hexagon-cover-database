# Algorithm-2 Two-Variable Model And Transition Polynomial

Status: Strategy

This file records the exact two-variable reduction used by algorithm 2 under the CE0, $N_+=1$, all-Vd0 branch assumptions and the additional equalities

$$
a_3+b_3=1,\qquad a_5+b_5=1.
$$

It does not prove those equalities from the full all-Vd0 hypotheses.

The two-variable equality reduction below is exact. The former claim that the
displayed mixed/quartic formulas form the selected complete radial envelope
was inherited from the withdrawn `2004` branch catalog. Until those formulas
are derived from the exact finite support criterion, the transition and
monotonicity part of this note remains Strategy.

## Two-Variable Reduction

Assume the unique supercritical row is the $V_4$ row. Under

$$
a_3+b_3=1,\qquad a_5+b_5=1,
$$

we have

$$
t_3=t_2,\qquad t_5=t_4.
$$

Fix $a_4,b_4$. Since

$$
a_4=1-t_3,\qquad b_4=t_4,
$$

we get

$$
t_2=t_3=1-a_4,\qquad t_4=t_5=b_4.
$$

The remaining free variables can be represented by $a_1,b_1$. Their feasible triangle is

$$
1-b_4\le a_1,\qquad 1-a_4\le b_1,\qquad a_1+b_1\le1.
$$

The three vertices are

$$
(1-b_4,1-a_4),\qquad (1-b_4,b_4),\qquad (a_4,1-a_4).
$$

They correspond to the three equality patterns among the rows $V_0,V_1,V_2$. In all three patterns, the local diagonal pair used by algorithm 2 is the same pair

$$
(1-b_4,1-a_4).
$$

Therefore algorithm 2 uses one common diagonal coordinate

$$
c_*=c_{\max}(1-b_4,1-a_4),
$$

and places

$$
D_j^{(2)}=(1-c_*)V_j,\qquad j=0,1,2.
$$

Thus the algorithm-2 point set depends only on two variables.

## $p,q$ Coordinates

Set

$$
p=1-b_4,\qquad q=1-a_4.
$$

Then

$$
b_4=1-p,\qquad a_4=1-q.
$$

In the lower half of the symmetric domain we take

$$
p\le q.
$$

The strict $V_4$ branch condition becomes

$$
(1-p)^2+(1-p)(1-q)+(1-q)^2<1,
$$

and the supercritical condition $a_4+b_4>1$ becomes

$$
p+q<1.
$$

The away-from-limit cutoff used in the current strategy is

$$
p\ge0.1,\qquad q\ge0.1.
$$

## Transition Polynomial

Let

$$
S=p+q.
$$

The algorithm-2 diagonal value is

$$
c_*=c_{\max}(p,q).
$$

For $p\le q$, the selected diagonal branch is:

$$
T\ge0:\quad c_*=\frac{2q}{1+\sqrt{4S^2-3}},
$$

and

$$
T\le0:\quad c_*^4-c_*^2+pc_*-p^2=0,\qquad c_*\ge S,
$$

where the transition polynomial is

$$
T(p,q)=S^4-S^2+pq.
$$

At the transition, both branches meet at

$$
c_*=S.
$$

Substituting $c=S$ into either branch equation gives exactly

$$
S^4-S^2+pq=0.
$$

Thus $T=0$ is the exact mixed/quartic branch transition.

## Basic Properties Of $T$

On the valid away region, the valid branch inequality implies

$$
S\ge2-\frac{2\sqrt3}{3}.
$$

Now

$$
T_p=4S^3-2S+q,\qquad T_q=4S^3-2S+p.
$$

Since $p,q\ge0.1$ and $S\ge2-2\sqrt3/3$, we have

$$
T_p>0,\qquad T_q>0.
$$

Hence each vertical line has at most one transition point. Also,

$$
T_{pp}=T_{qq}=12S^2-2>0.
$$

Thus $T$ is coordinate-wise convex. Its Hessian eigenvalues are

$$
24S^2-3,\qquad -1,
$$

so $T$ is not globally convex.

## Monotonicity Of The Diagonal Radius

Let

$$
r=1-c_*.
$$

Then $r$ is nondecreasing in both $p$ and $q$.

On the mixed branch, put

$$
E=\sqrt{4S^2-3}.
$$

Then

$$
c_*=\frac{2q}{1+E}.
$$

Hence

$$
\partial_p c_*=-\frac{8qS}{E(1+E)^2}<0.
$$

For the $q$ derivative,

$$
\partial_qc_*=\frac{2(E(1+E)-4qS)}{E(1+E)^2}.
$$

Since $p\le q$, one has $q\ge S/2$. It is enough to show

$$
E(1+E)\le2S^2.
$$

This follows from

$$
(3-2S^2)^2-E^2=4(1-S^2)(3-S^2)\ge0.
$$

Therefore $\partial_qc_*\le0$.

On the quartic branch,

$$
c_*^4-c_*^2+pc_*-p^2=0.
$$

Implicit differentiation gives

$$
\partial_pc_*=-\frac{c_*-2p}{4c_*^3-2c_*+p}.
$$

Since

$$
c_*\ge p+q\ge2p
$$

and

$$
4c_*^3-2c_*+p>0,
$$

we get $\partial_pc_*\le0$. The quartic branch is independent of $q$. Thus $\partial_qc_*=0$ there.

Consequently

$$
\boxed{r=1-c_*\text{ is nondecreasing in }p\text{ and }q.}
$$

## Limit Failure Of Algorithm 2

Near the lower vertex-limit corner, write

$$
a_4=(1+k)x,\qquad b_4=1-x.
$$

For algorithm 2,

$$
f_{\mathrm{algo2}}=1+xC_2(k)+O(x^2),
$$

where

$$
C_2(k)=\frac{1-3k}{2}\quad\text{for }0<k\le\frac12,
$$

and

$$
C_2(k)=\frac{k-1}{2}\quad\text{for }\frac12\le k<1.
$$

Hence $C_2(k)<0$ for $1/3<k<1$. Algorithm 2 cannot be used in every neighborhood of the two vertex-limit corners.
