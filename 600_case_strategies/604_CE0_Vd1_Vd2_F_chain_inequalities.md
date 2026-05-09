# CE0 + Vd1/Vd2 \(F\)-Chain Inequalities

Status: Proven analytic inequality

Define

\[
F(t)=\frac{t-1+\sqrt{1+6t-3t^2}}{2},
\qquad 0\le t\le1.
\]

For \(x\in[0,1)\) and allowed \(\theta\), define

\[
a(x,\theta)=
\frac{\frac{\sqrt3}{2}-\sin(\pi/3+\theta)}{\sin(\theta-\pi/3)}-x,
\]

and

\[
b(x,\theta)=
\frac{x\sin\theta-\sin(\theta-\pi/3)}{\sin(\theta+\pi/3)}.
\]

At \(\theta=\pi/3\), use continuous extension.

Let

\[
u=\tan\frac{\theta-\pi/3}{2}.
\]

Then

\[
\boxed{a(x,u)=\frac12-x+\frac{\sqrt3}{2}u,}
\]

and

\[
\boxed{b(x,u)=
\frac{x\sqrt3(1-u^2)+2u(x-2)}{\sqrt3(1-u^2)-2u}.}
\]

## Claim 1: small \(x\)

For

\[
x\in[0,1/2),
\]

and all allowed \(\theta\),

\[
\boxed{b(x,\theta)+F^{\circ3}(a(x,\theta))<1.}
\]

The proof uses affine upper bounds \(P_1,P_2,P_3\) for \(F\), giving

\[
F^{\circ3}(t)<t+\frac12
\qquad (0\le t\le1/2).
\]

One then proves

\[
b(x,u)+a(x,u)\le\frac12.
\]

Combining the two inequalities gives Claim 1.

## Claim 2: large \(x\)

For

\[
x\in[1/2,1),
\]

on the natural domain where

\[
a(x,\theta)\in[0,1],
\]

we have

\[
\boxed{b(x,\theta)+F^{\circ4}(a(x,\theta))<1.}
\]

The original full-interval statement is not well-defined when \(x>1/2\), since

\[
a(x,\pi/3)=\frac12-x<0.
\]

The corrected domain is the subinterval where \(a\in[0,1]\).

The proof uses affine upper bounds \(Q_1,Q_2,Q_3,Q_4\) for \(F\), giving

\[
F^{\circ4}(t)\le \frac{21}{10}t+\frac{39}{100}.
\]

For \(t=a(x,u)\), one proves

\[
0\le t\le \frac15,
\]

and

\[
b(x,u)\le B(t),
\]

where

\[
B(t)=\frac{4t^2+12t-3}{2(2t-1)(2t+3)}.
\]

Finally,

\[
1-\left(B(t)+\frac{21}{10}t+\frac{39}{100}\right)
=
\frac{840t^3+796t^2-274t+33}{100(1-2t)(2t+3)}>0
\]

for \(0\le t\le1/5\). This proves Claim 2.
