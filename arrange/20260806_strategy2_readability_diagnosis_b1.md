# Strategy 2 Readability Diagnosis: Remaining Findings and Architecture

### 3.5 The six-slot chain table repeats formal expressions rather than
explaining proof ownership

The old register wrote all six maps for each branch and then explained which
slots were replaced by identities.  This is technically explicit but
expositorily inefficient.  The important information is:

- where the chain begins;
- which internal edges are genuinely center-free;
- which terminal inequality closes it;
- which appendix problem proves that inequality.

The revised register records those four facts and does not duplicate the full
composition word.

### 3.6 Strict inequalities need a formalization-safe convention

Several feasible domains are open.  A strict pointwise inequality

$$
\Psi(z)<0\qquad(z\in D)
$$

does not imply

$$
\sup_{z\in D}\Psi(z)<0.
$$

The supremum may be zero and attained only on the excluded boundary.  A
formalization that replaces every strict target by a uniformly negative
optimum would therefore risk proving a stronger and possibly false statement.

The correct branchwise certificate is:

$$
\max_{\overline{D_\lambda}}\Psi_\lambda\le0
$$

for every algebraic branch $\lambda$, together with

$$
D_\lambda\cap\{\Psi_\lambda=0\}=\varnothing.
$$

This convention has been added to the optimization appendix.

### 3.7 Three special-role domains are not yet formalization-ready

The one-gap endpoint, paired endpoint, CE1 return, and CE2 return calculations
can already be written as pure three-variable problems.

The T3-like, adjacent-rescuer, and Vd terminal proofs are mathematically
proved, but their current feasible domains still contain one or more of:

- a translated-role normal form;
- a support-choice condition;
- a placement-defined supremum;
- a geometrically defined residual interval.

Calling such a domain “admissible” does not remove the geometry.  A proof
assistant needs the domain as a finite union of explicit real-variable
inequalities.  The revision therefore marks these interfaces as partial
rather than pretending that they are already pure optimization problems.

This is an interface defect, not a downgrade of the underlying theorem.
