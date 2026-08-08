# Pure Finite-Cell T3 Endpoint Theorem

Status: Proven

This source upgrades the `407X` calculation from a theorem stated on a
geometric support-isolated configuration to a universal theorem on the
explicit real-variable domain used by Strategy 2 formalization.

## Pure domain

Let

$$
\xi=(r,a,d,\tau,\beta,A_1,A_5,C_1,C_5)
$$

belong to the finite union $\Omega_{\rm T3}$.  Thus the signed center belongs
to the full CE1 or CE2 cell, the T3 source satisfies

$$
0<\tau<1,\qquad
z=\sqrt{1-\tau+\tau^2},\qquad
0<\beta<\frac{\tau z}{1+z},
$$

and one right residual cell, one left residual cell, one radial hit/miss cell,
and—on the hard region—one ordered pair of the four exact capped-map contact
labels have been selected.  Equality at every branch boundary is assigned to
one named cell.

## Algebraic realization of the `407X` variables

Define

$$
D_T=\frac1z,\qquad R_T=\frac\tau z,
\qquad \alpha_T=\beta,
\qquad p_T=z-\beta.
$$

Then

$$
R_T^2-D_TR_T+D_T^2=1,
\qquad
\alpha_T+p_T=\frac1{D_T},
$$

and, with $q_T=1-p_T$,

$$
q_T=1-z+\beta,
$$

$$
\frac{D_Tq_T}{R_T}
 =\frac{1-z+\beta}{\tau}=c_\star,
$$

$$
q_T+\frac{1-R_T}{D_T}
 =1+\beta-\tau=u_\star.
$$

Because $0<\tau<1$, one has $0<R_T<1<D_T$.  The source inequalities imply
$\alpha_T,p_T\ge0$ and $q_T<1/2$.  Thus every algebraic source hypothesis
used in the `407X` four-label calculation follows directly from the pure-cell
definition.

The residual predicates $\mathcal R_i$ and $\mathcal L_{\varepsilon,j}$
are exactly the cases of the center interval-component formula.  The predicates
$\mathcal K_h$ are exactly the radial hit/miss cases.  Finally, the ordered
contact predicates select the same explicit formulas of the capped-output
function as the four labels in
[`4073`](4073_boundary_loss_framework.md)--[`407d`](407d_rigor_final_assembly.md).

## Objective sign

If $A_1+A_5>1$, the primitive cap $F(c,x)\le1-x$ gives

$$
F(C_5,A_5)+F(C_1,A_1)<1.
$$

On the hard region $A_1+A_5\le1$, the eight rows of the exact `407X` audit
cover all sixteen ordered label pairs.  After the substitutions above, every
quantity used by those rows is an explicit function of the pure variables and
every hypothesis is one of the defining cell inequalities.  Therefore the
same finite algebraic proof gives

$$
\boxed{
F(C_5,A_5)+F(C_1,A_1)-1<0
}
$$

for every $\xi\in\Omega_{\rm T3}$.

This is a universal real-domain theorem.  It does not assume that $\xi$ was
first produced by a geometric placement.  The later geometry bridge only
shows that an actual support-isolated branch supplies such a point.
