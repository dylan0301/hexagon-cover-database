# High-Sheet Symbol Convention

Status: Definition

This note fixes one typographical ambiguity in
[`407a_left_Thigh_branch_completion.md`](407a_left_Thigh_branch_completion.md)
and
[`407c_rigor_completion_details.md`](407c_rigor_completion_details.md).
It changes no hypothesis, formula, inequality, branch condition, or proof
status.

In the left-high-sheet calculations, the symbol

$$
\boxed{\nu=\gamma_5}
$$

is the center radial-exit variable. Thus every displayed occurrence of
$\nu$ in the high-sheet formulas means the same quantity as the isolated
center formula

$$
\gamma_5=\frac{X}{1-\lambda}.
$$

In particular, with

$$
r=1-\lambda,
\qquad
y=\frac{Y}{\lambda},
\qquad
\rho=\sqrt{r^2-r+1},
$$

the formulas used in `407a` and Section 2 of `407c` are

$$
S=\nu+\frac{1-r}{1+\rho}+\frac{1-r}{r}y,
$$

$$
T=r\nu+1-r,
$$

and

$$
1-\nu=\frac{\sqrt{\beta^2-\beta+1}}{r+\beta}.
$$

The initial line in those files that writes $u=\gamma_5$ is a typographical
alias for the boxed convention above. It must not be confused with the local
variable $u$ used independently in Lemma 1.4 of `407c`.

All downstream estimates in `407a`, `407c`, and `407d` use the boxed
high-sheet convention.
