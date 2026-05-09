# Center Type 1 Optimization

Status: Empirical / certificate target

For Type 1, the all-midpoint state is

\[
\left(\frac12,\dots,\frac12\right).
\]

The objective is

\[
L(\mathbf d)=\sum_{\theta\in\{0,60,120,180,240,300\}}
\left(d_\theta-\frac12\right)^2.
\]

In parameters,

\[
\begin{aligned}
L(u,s,v,w)={}&\left(u-\frac12\right)^2+\left(s-\frac12\right)^2+\left(v-\frac12\right)^2+\left(w-\frac12\right)^2\\
&+\left(\frac{uv}{u+w}-\frac12\right)^2+\left(\frac{uw}{u+w}-\frac12\right)^2.
\end{aligned}
\]

subject to

\[
(s(u+w)+u(v+w))^2=u^2+uw+w^2.
\]

Empirical numerical optimization gives

\[
\min L(\mathbf d)\approx0.13918.
\]

An approximate optimizer is

\[
\mathbf d^*\approx(0.534,0.334,0.531,0.274,0.503,0.259).
\]

This is not yet a rigorous global certificate.
