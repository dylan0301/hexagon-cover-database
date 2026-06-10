# The $g_c$ Map

Status: Definition

For fixed $c\in[0,1]$, define

$$
B_c(a)=\max\{b\in[0,1]:(a,b,c)\in\mathcal A\}.
$$

This is a set-defined maximum over the full admissible set. It is not
defined by choosing an arbitrary root of a boundary equation. A root
obtained from a boundary equation is only a candidate value of $b$; it
contributes to $B_c(a)$ only if $(a,b,c)$ satisfies the relevant cell
inequalities defining $\mathcal A$.

Then

$$
g_c(a)=1-B_c(a).
$$

Here $a$ is a defect arriving from the previous edge, $B_c(a)$ is the maximal next-edge coverage, and $g_c(a)$ is the defect passed forward.
