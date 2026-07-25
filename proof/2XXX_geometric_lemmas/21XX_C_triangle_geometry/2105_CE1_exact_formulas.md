# CE1 Exact Formulas as a Signed-Normal-Form Adapter

Status: Proven

This note records the CE1 specialization of the common signed center normal
form in
[`2109`](2109_signed_CE1_CE2_center_normal_form.md).  No separate CE1 line,
interval, or radial-exit calculation is required.

## 1. Variables

Put

$$
0<\lambda<1,
\qquad
W=1-\lambda,
$$

$$
\rho=\sqrt{1-\lambda+\lambda^2},
\qquad
\eta=1-\rho,
\qquad
P=\rho(1-\rho).
$$

Let

$$
\alpha=C_0,
\qquad
\delta=C_2,
\qquad
k=\eta+\alpha+\delta.
$$

In the affine coordinates

$$
X=V_0+b(V_1-V_0)+a(V_5-V_0),
$$

the triangle is

$$
T_C=\left\{F_0\ge0,F_1\ge0,F_2\ge0\right\},
$$

where

$$
\begin{aligned}
F_0&=\lambda+\alpha-a+Wb,\\
F_1&=\lambda b+Wa-k,\\
F_2&=W+\delta-b+\lambda a.
\end{aligned}
$$

These are the side slacks of a unit equilateral triangle because they are the
common edge-cut normal form proved in `2109`.

## 2. Exact CE1 domain

Define

$$
\Delta_R=P-\alpha-W\delta,
\qquad
\Delta_L=P-\lambda\alpha-\delta.
$$

The normalized positive center trace is on $e_{0,1}$.  The closed exact-$M_0$
CE1 domain is

$$
\boxed{
\begin{gathered}
0<\lambda<1,
\qquad
\alpha\ge0,
\qquad
\delta\ge0,\\
\Delta_R>0,
\qquad
\Delta_L\le0.
\end{gathered}
}
$$

For the closure of an original open center role, the center slacks are strict:

$$
\boxed{\alpha>0,
\qquad
\delta>0.}
$$

The trace is

$$
\boxed{
T_C\cap e_{0,1}=[s,t],
\qquad
s=\frac{k}{\lambda},
\qquad
t=W+\delta.
}
$$

Its length is

$$
t-s=\frac{\Delta_R}{\lambda}>0.
$$

The companion trace on $e_{5,0}$ has signed length

$$
\frac{\Delta_L}{W}.
$$

Thus $\Delta_L\le0$ is exactly the assertion that the companion edge has no
positive-length overlap.  Equality permits one point contact, as required by
the CE1 definition.

The historical center slacks are recovered exactly:

$$
C_0=\rho+\lambda s-t-\lambda=\alpha,
$$

$$
C_1=1-\lambda s=\rho-\alpha-\delta,
$$

$$
C_2=t+\lambda-1=\delta.
$$

The inequalities formerly listed separately in this file follow from the
signed domain.  For example,

$$
\delta<\frac{P}{W}
=\frac{\rho\lambda}{1+\rho}
<\frac\lambda2,
$$

and

$$
\alpha<P
<\min\left\{\frac\lambda2,\frac W2\right\}.
$$

The midpoint tests in
[`2100`](2100_CE1_CE2_exactly_one_midpoint_lemma.md) therefore give

$$
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\}.
$$

Conversely, the common edge-cut calculation in `2109` shows that every
normalized exact-$M_0$ CE1 triangle yields precisely these signed inequalities.
Hence the displayed domain is exact.

## 3. Radial exits and demands

The common exit theorem `2109` gives

$$
\boxed{
\begin{aligned}
d_0^C&=\rho-\alpha-\delta,\\
d_1^C&=\frac{\delta}{\lambda},\\
d_2^C&=\delta,\\
d_3^C&=\min\left\{\frac{\alpha}{\lambda},\frac{\delta}{W}\right\},\\
d_4^C&=\alpha,\\
d_5^C&=\frac{\alpha}{W}.
\end{aligned}
}
$$

In the CE1 sign range,

$$
\Delta_L\le0<\Delta_R
$$

implies

$$
\lambda\delta>W\alpha.
$$

Therefore

$$
\boxed{d_3^C=\frac{\alpha}{\lambda}.}
$$

The complementary vertex-role demands are

$$
\boxed{c_i=1-d_i^C.}
$$

For closures of original open center roles,

$$
d_0^C>\frac12,
\qquad
d_i^C<\frac12\quad(i\ne0),
$$

and hence

$$
c_0<\frac12,
\qquad
c_i>\frac12\quad(i\ne0).
$$

If an actual vertex role reaches distance $\widehat c_i$ from $V_i$, radial
coverage gives $\widehat c_i\ge c_i$.  Replacing the actual reach by this lower
demand enlarges the local feasible set, so it is a valid proof relaxation.
