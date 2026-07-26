# Vd1/Vd2 Corner Radial Margins

Status: Proven

This note records the two immediate radial inequalities from the Vd1/Vd2
corner normal form.  They replace repeated substitutions in the adjacent and
nonadjacent CE2 placement proofs.

## Setup

Use the local coordinates of
[`2014`](2014_Vd1_Vd2_corner_normal_form.md).  Let $a,b$ be the two exact
boundary reaches.  For the unique parameter $t>0$, put

$$
d=\sqrt{t^2+t+1}.
$$

The triangle is given by

$$
\begin{aligned}
x-(t+1)y&\le a,\\
ty-(t+1)x&\le tb,\\
tx+y&\le d-a-tb.
\end{aligned}
$$

The own-radial reach is

$$
c_0=\frac{d-a-tb}{t+1}.
$$

If the supported adjacent arm is the one corresponding to the second endpoint
formula in `2014`, its upper endpoint is

$$
u_+=\frac{d-a-tb-1}{t}.
$$

## 1. Own-radial margin

Since

$$
d<t+1,
$$

we have

$$
\begin{aligned}
c_0
&<
1-\frac{a+tb}{t+1}\\
&\le
1-\min\{a,b\}.
\end{aligned}
$$

Thus

$$
\boxed{c_0<1-\min\{a,b\}.}
$$

More generally, if $a\ge A$ and $b\ge H$, then

$$
\boxed{c_0<1-\min\{A,H\}.}
$$

## 2. Supported-arm endpoint margin

Again using $d<t+1$,

$$
\begin{aligned}
u_+
&<
\frac{t+1-a-tb-1}{t}\\
&=
1-b-\frac at.
\end{aligned}
$$

Hence

$$
\boxed{u_+<1-b-\frac at<1-b.}
$$

In particular, if $b\ge H$, then

$$
\boxed{u_+<1-H.}
$$

Reflection supplies the corresponding formulas for the other supported
adjacent arm.
