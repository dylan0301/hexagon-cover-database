# CE1/CE2, $N_+=1$, Exactly One T3-Like: Boundary Obstruction

Status: Proven

This file completes the branch after the midpoint reduction in
[`4131`](4131_midpoint_forcing_reduction.md).  The former branch-specific
center-hiding and terminal boundary sum are replaced by the common
adjacent-rescuer theorem in
[`2018`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md).
The only remaining task is a short local inequality for the T3-like normal
form.

## 1. Reduced branch

After reflection if necessary, `4131` gives

$$
T_0\text{ T3-like},
\qquad
M_1\in T_0,
$$

$$
T_1\text{ uniquely supercritical},
$$

and

$$
T_2,T_3,T_4,T_5
$$

are nonsupercritical Vd0 rows.  It is enough to verify the two local
rescuer inequalities required by `2018`.

## 2. T3-like local normal form

Use the normalized $V_0$ coordinates

$$
X=V_0+x(V_5-V_0)+y(V_1-V_0).
$$

By the T3-like translation theorem, replace $T_0$ by the same-orientation
translate that contains its old trace on $H$ and has $V_0$ on a side.  In the
branch with positive support on $r_1$ and none on $r_5$, the standard normal
form gives parameters

$$
1\le D\le\frac2{\sqrt3},
\qquad
E=\sqrt{4-3D^2},
\qquad
R_{\rm loc}=\frac{D+E}{2},
$$

and a boundary reach $a$ on $e_{5,0}$ satisfying

$$
\frac{E}{2D}
\le a\le
\frac{4-3D+E}{4D}.
$$

The relevant traces are

$$
T_0\cap e_{5,0}=[0,a],
$$

and

$$
T_0\cap r_1=[c,u],
$$

where the radial coordinate is measured from $V_1$ toward $O$ and

$$
\boxed{
c=\frac{D(1+a)-1}{R_{\rm loc}},
\qquad
u=1-\frac{R_{\rm loc}}D+a.
}
$$

The midpoint condition is exactly

$$
c\le\frac12\le u.
$$

Put

$$
\boxed{x=\frac{aD}{R_{\rm loc}}.}
$$

We prove

$$
\boxed{x\le A_{\rm sc}(c),}
$$

where

$$
B_{\rm sc}(c)=\frac{c+\sqrt{c^2-8c+4}}2,
\qquad
A_{\rm sc}(c)=1-B_{\rm sc}(c).
$$

## 3. Rationalized proof of the local inequality

Put

$$
\theta=\frac{D-1}{R_{\rm loc}}.
$$

Since $D=1+\theta R_{\rm loc}$ and

$$
R_{\rm loc}^2-DR_{\rm loc}+D^2=1,
$$

one obtains

$$
\boxed{
R_{\rm loc}=\frac{1-2\theta}{1-\theta+\theta^2},
\qquad
D=\frac{1-\theta^2}{1-\theta+\theta^2},
\qquad
E=\frac{1-4\theta+\theta^2}{1-\theta+\theta^2}.
}
$$

The condition $E\ge0$ and the geometric range give

$$
0\le\theta\le2-\sqrt3<\frac13.
$$

The radial input simplifies to

$$
\boxed{c=x+\theta.}
$$

The two midpoint inequalities for $a$ become

$$
\boxed{
\frac{1-4\theta+\theta^2}{2(1-2\theta)}
\le x\le
\frac12-\theta.
}
$$

In particular, $0\le x,c\le1/2$.

For $0\le z\le1/2$, put

$$
\Phi(z)=\frac{z(2-z)}{1+z}.
$$

The defining equation of the strict-supercritical envelope is

$$
\Phi(A_{\rm sc}(c))=c,
$$

and

$$
\Phi'(z)=\frac{2-2z-z^2}{(1+z)^2}>0
$$

on $[0,1/2]$.  Hence it is enough to prove

$$
\Phi(x)\le c=x+\theta.
$$

After multiplication by $1+x>0$, this is equivalent to

$$
Q_\theta(x):=2x^2+(\theta-1)x+\theta\ge0.
$$

The vertex of this convex quadratic is

$$
x_*=\frac{1-\theta}{4}.
$$

### Case 1: $0\le\theta\le1/5$

Let

$$
x_L=\frac{1-4\theta+\theta^2}{2(1-2\theta)}.
$$

Then

$$
x_L-x_*
=
\frac{1-5\theta}{4(1-2\theta)}
\ge0.
$$

Thus $Q_\theta$ is increasing on the full feasible interval and

$$
Q_\theta(x)\ge Q_\theta(x_L).
$$

Direct simplification gives

$$
Q_\theta(x_L)
=
\frac{\theta(1-5\theta+11\theta^2-\theta^3)}
{2(1-2\theta)^2}
\ge0,
$$

because $1-5\theta\ge0$ and
$11\theta^2-\theta^3=\theta^2(11-\theta)\ge0$.

### Case 2: $1/5\le\theta\le2-\sqrt3$

Now $x_L\le x_*$.  The upper endpoint

$$
x_U=\frac12-\theta
$$

satisfies

$$
x_U-x_*=\frac{1-3\theta}{4}>0.
$$

Therefore $x_*$ belongs to the feasible interval and

$$
Q_\theta(x)
\ge
Q_\theta(x_*)
=
\frac{10\theta-1-\theta^2}{8}>0.
$$

The last function is increasing on the present interval and is already
positive at $\theta=1/5$.

Both cases prove $\Phi(x)\le c$, and the monotonicity of $\Phi$ gives

$$
\boxed{x\le A_{\rm sc}(c).}
$$

## 4. Verification of the common rescuer hypotheses

Since $D\ge R_{\rm loc}$,

$$
a\le x\le A_{\rm sc}(c).
$$

Moreover,

$$
1-u=\frac{R_{\rm loc}}D-a,
$$

so

$$
\boxed{
\frac{a}{a+1-u}
=
\frac{aD}{R_{\rm loc}}
=x
\le A_{\rm sc}(c).
}
$$

These are exactly the two local hypotheses of the common adjacent-rescuer
obstruction `2018`.

It remains only to verify its radial-isolation premise.  The interval
$T_0\cap r_1=[c,u]$ contains $M_1$, so $u\ge1/2$.  The supercritical row
$T_1$ cannot contain $M_1$.  Since it contains $V_1$ and is convex, it cannot
cover any point of $r_1$ on the $O$-side of $M_1$.  The four remaining rows
are Vd0 and have no positive-length adjacent support on $r_1$.  Hence the
center role must cover the $O$-side gap of length $1-u$ before the T3-like
interval begins.

All hypotheses of `2018` are now satisfied.  That theorem gives a far-side
boundary demand at least $B_{\rm sc}(c)$, while the strict supercritical
envelope gives the outgoing reach of $T_1$ strictly below
$B_{\rm sc}(c)$.  Its boundary-path budget then contradicts the four
nonsupercritical row caps of $T_2,T_3,T_4,T_5$.

Therefore the CE1/CE2, $N_+=1$, exactly-one-T3-like branch is impossible.

$$
\Box
$$
