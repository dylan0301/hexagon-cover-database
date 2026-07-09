# Completion of the Left-Low Family in $407X$

Status: Proven with local details in [`407c_rigor_completion_details.md`](407c_rigor_completion_details.md)

This file closes the remaining hard-region branches with first coordinate

$$
B_5=B(A_5,C_5)=L
$$

in the boundary-loss framework of
[`4073_boundary_loss_framework.md`](4073_boundary_loss_framework.md).  Together with `4074` and `4075`, it proves

$$
B_5=L\quad\Longrightarrow\quad B_5+B_1<1
$$

for every realized right branch in the support-isolated $407X$ domain.

The detailed polynomial, convexity, and center-transfer computations used below are recorded in
[`407c_rigor_completion_details.md`](407c_rigor_completion_details.md), Sections 1.1--1.4.

Throughout use the notation of `4073`.  Let

$$
z=\ell(\gamma_5)
$$

when the left branch is Low.

## 1. Low branch separation

### Lemma 1.1

Let $0\le\eta\le1-\sqrt3/2$ and let $z=\ell(\eta)$.  If the Low candidate is realized for input $a=1-\beta$, then

$$
\boxed{\beta\ge z+\eta.}
$$

### Proof

The Low equation is

$$
z^2-(1-\eta)z+(1-\eta)^2\left(1-(1-\eta)^2\right)=0.
$$

Equivalently $P(\eta,z)=0$, where

$$
P(x,z)=x^4-4x^3+5x^2-(2+z)x+z-z^2.
$$

The Low cell condition contains

$$
(a+z)^4-(a+z)^2+az\le0.
$$

With $a=1-\beta$ and $h=\beta-z$, this is $P(h,z)\le0$.  The domain condition $a+z\le1$ gives $h\ge0$; see `407c`, Lemma 1.1.  On $0\le x\le1-\sqrt3/2<1/7$,

$$
{\partial P\over\partial x}=4x^3-12x^2+10x-(2+z)<0.
$$

Thus $P$ is strictly decreasing on the Low range.  If $h<\eta$, then $P(h,z)>P(\eta,z)=0$, contradiction.  Hence $h\ge\eta`, proving $\beta\ge z+\eta$.

