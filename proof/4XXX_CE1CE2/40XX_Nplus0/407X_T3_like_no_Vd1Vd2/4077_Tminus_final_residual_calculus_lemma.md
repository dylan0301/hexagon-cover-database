# Calculus Lemma for the Final Left-$T_-$ Residual

Status: Proven

This file proves the one-variable calculus lemma used in
[`4075_Tminus_low_lower_branch_obligations.md`](4075_Tminus_low_lower_branch_obligations.md) to rule out the final overlap residual with right branch $T_+^{hi}$.

## 1. Statement

Let

$$
0<\kappa<{1\over2}
$$

and define

$$
y_*={\kappa(1-2\kappa)\over(1-\kappa)(2-\kappa)}.
$$

Let

$$
\lambda={\kappa(2-\kappa)\over1-\kappa^2}.
$$

Then for every

$$
0\le y<y_*,
$$

one has

$$
\boxed{\ell(y)<\kappa+{\lambda\over1-\lambda}y.}
$$

Here

$$
\ell(y)={ (1-y)(1-\sqrt{4(1-y)^2-3})\over2}.
$$

## 2. Proof

First,

$$
y_*<{1\over8}.
$$

Indeed,

$$
y_*<{1\over8}
$$

is equivalent to

$$
8\kappa(1-2\kappa)<(1-\kappa)(2-\kappa),
$$

or

$$
0<2-11\kappa+17\kappa^2.
$$

The quadratic on the right has discriminant

$$
121-136<0
$$

and positive leading coefficient, so it is positive for all real $\kappa$.

Now define the affine function

$$
L(y)=\kappa+{\lambda\over1-\lambda}y.
$$

Using

$$
{\lambda\over1-\lambda}={\kappa(2-\kappa)\over1-2\kappa},
$$

we have

$$
L(y)=\kappa+{\kappa(2-\kappa)\over1-2\kappa}y.
$$

We prove

$$
\ell(y)<L(y)\qquad(0\le y\le y_*).
$$

On $0\le y\le y_*<1/8$, the Low function is convex.  Indeed,

$$
\ell''(y)=
{2(y-1)(8(y-1)^2-9)\over(4(y-1)^2-3)^{3/2}}.
$$

For $0\le y\le1/8$, both $y-1<0$ and $8(y-1)^2-9<0$, so $\ell''(y)>0$.  Therefore

$$
L(y)-\ell(y)
$$

is concave on $[0,y_*]$.  It suffices to check positivity at the endpoints.

At $y=0$,

$$
\ell(0)=0,\qquad L(0)=\kappa>0.
$$

At $y=y_*$, compute

$$
L(y_*)={\kappa\over1-\kappa}.
$$

It remains to show

$$
\ell(y_*)<{\kappa\over1-\kappa}.
$$

Let

$$
c_*=1-y_*.
$$

The Low value $\ell(y_*)$ is the smaller positive root of

$$
P(b):=b^2-c_*b+c_*^2(1-c_*^2)=0.
$$

Substitute

$$
b_0={\kappa\over1-\kappa}.
$$

A direct simplification gives

$$
P(b_0)=
-{\kappa^2(1-2\kappa)^2 Q(\kappa)
\over(2-\kappa)^4(1-\kappa)^4},
$$

where

$$
Q(\kappa)=17\kappa^4-62\kappa^3+94\kappa^2-68\kappa+20.
$$

We prove $Q>0$ on $(0,1/2)$.  Its second derivative is

$$
Q''(\kappa)=204\kappa^2-372\kappa+188.
$$

The discriminant of $Q''$ is

$$
372^2-4\cdot204\cdot188<0,
$$

and the leading coefficient is positive, so $Q''>0$.  Hence $Q'$ is increasing.  Since

$$
Q'\left({1\over2}\right)<0,
$$

we have $Q'<0$ on $(0,1/2)$.  Thus $Q$ is decreasing on $(0,1/2)$, and

$$
Q(\kappa)>Q\left({1\over2}\right)={45\over16}>0.
$$

Therefore

$$
P(b_0)<0.
$$

Since $P(0)=c_*^2(1-c_*^2)>0$, the point $b_0$ lies to the right of the smaller root of $P$.  Hence

$$
\ell(y_*)<b_0={\kappa\over1-\kappa}=L(y_*).
$$

Thus $L-\ell$ is positive at both endpoints of $[0,y_*]$.  Since $L-\ell$ is concave, it is positive throughout the interval.  Therefore

$$
\ell(y)<L(y)
$$

for every $0\le y\le y_*$.  This proves the lemma.
