# Strategy 2 Formalization Plan and Implementation Audit

## 6. Pure optimization specification

The formalization-ready problems now use one explicit function $F(c,x)$ and
its update

$$
T(c,x)=1-F(c,x).
$$

The four ready problems have the following shapes.

### S2-E1: one-gap endpoint

Input:

$$
(r,a,d)\in\mathcal D_1\cup\mathcal D_2.
$$

Objective:

$$
F(c_-,x_-)+F(c_+,x_+)-1<0.
$$

### S2-E2: paired endpoint

Input:

$$
(r,a,d)\in\mathcal D_2.
$$

Objective:

$$
F(c_-,x_-)+F(c_+,x_+)-1<0.
$$

### S2-R1: CE1 return

Input:

$$
(r,a,d)\in\mathcal D_1.
$$

Recurrence:

$$
Y_1=T(1-a,Y_0),\qquad
Y_2=T(1-m,Y_1),\qquad
Y_3=T(1-d,Y_2).
$$

Objective:

$$
w+d-Y_3<0.
$$

### S2-R2: CE2 return

The recurrence and objective are identical; only the domain changes to
$\mathcal D_2$.  The proof must encode an inclusive disjunction saying that
at least one threshold condition holds.

This format is substantially easier to formalize than a composition written
with hats, complement duals, geometric slot names, and center intervals.

## 7. Notation policy

### Body

Use only the following Strategy 2 quantities unless a theorem statement
requires more:

- actual reaches $A_i,B_i,C_i$;
- actual supercritical count $N_+$;
- active-gap rank $\mathrm{gr}$;
- an endpoint record $\mathbf e$;
- a returned lower bound $Z$ and terminal cap $H$.

Do not display $R,W,E,\eta,P,k,\Delta_R,\Delta_L,\alpha,\delta$ in the body.

### Optimization appendix

Use:

- independent variables $(r,a,d)$;
- derived variables $(w,e,\eta,p,k)$;
- one primitive function $F(c,x)$;
- one update $T(c,x)=1-F(c,x)$;
- one objective symbol $\Psi$ per problem.

Do not use $A_i,B_i,C_i$, role names, boundary-edge names, or placement
coordinates.

### Verification appendix

Technical aliases are permitted locally, but each subsection must begin with
a dictionary to the corresponding optimization problem and must end by
restating its objective sign.

