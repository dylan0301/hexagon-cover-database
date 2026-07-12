# CE2 Vd1 Axis-Replacement Radial Bridge

Status: Proven

This note proves the radial statement needed to turn the boundary replacement
in `4147` into a full reduction to `4013`.

## Statement

Use the normalized Vd1--supercritical adjacent pair of `4147`. Let $T_i$ be
the supercritical row, let $b_i$ be its outgoing boundary reach, and let

$$
c_i^{\mathrm{req}}=1-d_i
$$

be the exact complementary demand left by the CE2 center triangle on the
rescued radial arm. Then

$$
\boxed{
c_i^{\mathrm{req}}
<
\max\{1-a,1-b_i\}.
}
$$

Consequently there is a parameter

$$
p\in(a,1-b_i)
$$

with

$$
c_i^{\mathrm{req}}<\max\{p,1-p\}.
$$

## The Vd1 exit bound

In the corner-side coordinates of `4147`, the Vd1 intersection with the
neighboring radial arm, measured from $V_i$ toward $O$, is

$$
(\lambda,\mu),
$$

where

$$
\lambda=\frac{t(1-b)}{t+1},
\qquad
\mu=\frac{d-a-tb-1}{t},
\qquad
d=\sqrt{t^2+t+1}.
$$

The exact Vd1 hypotheses give

$$
t\ge1,
\qquad
b\ge\frac{t-1}{2t},
\qquad
a+tb\le d-1-\frac t2.
$$

Therefore

$$
\begin{aligned}
t(\mu+a-1)
&=d-(t+1)-tb+(t-1)a\\
&\le
d-(t+1)-tb
+(t-1)\left(d-1-\frac t2-tb\right)\\
&=t\left(d-2-\frac{t-1}{2}-tb\right)\\
&\le t(d-t-1)<0.
\end{aligned}
$$

The last inequality uses $d<t+1$. Hence

$$
\boxed{\mu<1-a.}
$$

## The center handoff

Let $c_i$ be the old supercritical row's actual own-radial reach. In this
reduced branch every other vertex role has zero adjacent support. Thus the
only original open roles that cover a positive interval of the rescued arm
are $T_i$, the Vd1 row, and $T_C$.

The open cover therefore forces

$$
c_i^{\mathrm{req}}<\max\{c_i,\mu\}.
$$

Equality is insufficient: it would leave the common exit or entry point
outside all three open roles.

The max-$B$ argument in `4147` gives

$$
c_i\le1-b_i.
$$

Combining the last three inequalities yields

$$
c_i^{\mathrm{req}}
<
\max\{1-b_i,1-a\},
$$

as claimed.

## Interior endpoint selection

The open-role inequalities in `4147` also give

$$
a+b_i<1.
$$

If the strict maximum above is supplied by $1-a$, choose $p>a$ sufficiently
close to $a$. If it is supplied by $1-b_i$, choose $p<1-b_i$ sufficiently
close to $1-b_i$. In either case $p$ can be chosen in the open interval
$(a,1-b_i)$ while preserving the strict radial inequality.

This is exactly the bridge required by the perturbed axis replacements in
`4147`. Thus the adjacent Vd1--supercritical route has no terminal dependency
between `4147` and `4013`.

$$
\Box
$$
