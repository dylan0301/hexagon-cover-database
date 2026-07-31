from pathlib import Path

ROOT=Path.cwd()

def load(rel): return (ROOT/rel).read_text(encoding='utf-8')
def save(rel,s): (ROOT/rel).write_text(s,encoding='utf-8')
def once(s,a,b,label):
    n=s.count(a)
    if n!=1: raise RuntimeError(f'{label}: expected one occurrence, found {n}')
    return s.replace(a,b,1)
def replace_table_by_label(text,label,new):
    marker=f'\\label{{{label}}}'
    pos=text.find(marker)
    if pos<0: raise RuntimeError('label missing '+label)
    start=text.rfind('\\begin{table}[H]',0,pos)
    end=text.find('\\end{table}',pos)
    if start<0 or end<0: raise RuntimeError('table bounds missing '+label)
    end+=len('\\end{table}')
    return text[:start]+new+text[end:]

# Reuse the signed companion quantity already defined in Appendix D.
rel='arrange/paper_draft/02_reader_framework.tex'
s=load(rel).replace('\\sigma_L','\\Delta_L')
save(rel,s)

rel='arrange/paper_draft/04_strategy2_summary.tex'
s=load(rel)
old=r"""Only under this condition, together with exclusion of nonincident boundary
traces on that edge, may the $i$th slot be lowered to $\mathrm I$.
\end{definition}"""
new=r"""Only under this condition, together with exclusion of nonincident boundary
traces on that edge, may the $i$th slot be replaced by $\mathrm I$ in a
certificate word.  Such a replacement means that the exact handoff inequality
\[
 A_{i+1}\ge\widehat g_{c_i}^{\vee}(A_i)
\]
has been weakened to $A_{i+1}\ge A_i$.  It is a statement about that
individual handoff; no pointwise order between the two formal compositions is
being asserted.  The terminal proposition named in the register supplies the
valid composition/endpoint argument for the whole certificate word.
\end{definition}"""
if 'no pointwise order between the two formal compositions' not in s:
    s=once(s,old,new,'certificate-word semantics')

new_table=r"""\begin{table}[H]
\centering
\scriptsize
\renewcommand{\arraystretch}{1.18}
\begin{tabular}{@{}p{.20\textwidth}p{.69\textwidth}@{}}
\toprule
branch&six explicitly displayed functions and the certified handoff word\\
\midrule
$N_+=0$, all Vd0, $\mathrm{gr}=0$
&The branch exclusions give $J_i^C=\varnothing$ for every $i$.  The exact word
is
$\mathcal G_{00}=[\widehat g_{c_0,J_0^C}^{\vee}\mid
\widehat g_{c_1,J_1^C}^{\vee}\mid\widehat g_{c_2,J_2^C}^{\vee}\mid
\widehat g_{c_3,J_3^C}^{\vee}\mid\widehat g_{c_4,J_4^C}^{\vee}\mid
\widehat g_{c_5,J_5^C}^{\vee}]$.
The certified weaker handoffs are recorded as
$\mathcal C_{00}=[\mathrm I\mid\mathrm I\mid\mathrm I\mid
\mathrm I\mid\mathrm I\mid\mathrm I]$; strict cyclic ascent gives the
contradiction.\\
\addlinespace
$N_+=0$, all Vd0, $\mathrm{gr}=1$
&After cyclic normalization $J_0^C$ is the positive-length center trace; every
possible point contact remains explicit in
$\mathcal G_{01}=[\widehat g_{c_0,J_0^C}^{\vee}\mid
\widehat g_{c_1,J_1^C}^{\vee}\mid\widehat g_{c_2,J_2^C}^{\vee}\mid
\widehat g_{c_3,J_3^C}^{\vee}\mid\widehat g_{c_4,J_4^C}^{\vee}\mid
\widehat g_{c_5,J_5^C}^{\vee}]$.
The certificate word is
$\mathcal C_{01}=[\widehat g_{c_0,J_0^C}^{\vee}\mid
\widehat g_{c_1,J_1^C}^{\vee}\mid\mathrm I\mid\mathrm I\mid\mathrm I\mid
\widehat g_{c_5,J_5^C}^{\vee}]$; the one-gap endpoint sum is $<1$.\\
\addlinespace
CE2, $\mathrm{gr}=2$
&Normalize the two positive-length traces as $J_0^C,J_5^C$ and retain all
point contacts in
$\mathcal G_{02}=[\widehat g_{c_0,J_0^C}^{\vee}\mid
\widehat g_{c_1,J_1^C}^{\vee}\mid\widehat g_{c_2,J_2^C}^{\vee}\mid
\widehat g_{c_3,J_3^C}^{\vee}\mid\widehat g_{c_4,J_4^C}^{\vee}\mid
\widehat g_{c_5,J_5^C}^{\vee}]$.
The certificate word is
$\mathcal C_{02}=[\widehat g_{c_0,J_0^C}^{\vee}\mid
\widehat g_{c_1,J_1^C}^{\vee}\mid\mathrm I\mid\mathrm I\mid\mathrm I\mid
\widehat g_{c_5,J_5^C}^{\vee}]$; the paired endpoint sum is $<1$.\\
\addlinespace
$N_+=0$, one T3-like V triangle
&For support-isolated $T_0$ the exact word is
$\mathcal G_{\rm T3}=[\widehat g_{c_0,J_0^C}^{\vee}\mid
\widehat g_{c_1,J_1^C}^{\vee}\mid\widehat g_{c_2,J_2^C}^{\vee}\mid
\widehat g_{c_3,J_3^C}^{\vee}\mid\widehat g_{c_4,J_4^C}^{\vee}\mid
\widehat g_{c_5,J_5^C}^{\vee}]$.
The certificate word is
$\mathcal C_{\rm T3}=[\widehat g_{c_0,J_0^C}^{\vee}\mid
\widehat g_{c_1,J_1^C}^{\vee}\mid\mathrm I\mid\mathrm I\mid\mathrm I\mid
\widehat g_{c_5,J_5^C}^{\vee}]$; the audited four-label endpoint sum is $<1$.\\
\addlinespace
$N_+=1$, all Vd0, one gap
&With $T_0$ the unique strictly supercritical V triangle, the full exact word is
$\mathcal G_{11}=[g_{c_0,J_0^C}^{\vee}\mid
\widehat g_{c_1,J_1^C}^{\vee}\mid\widehat g_{c_2,J_2^C}^{\vee}\mid
\widehat g_{c_3,J_3^C}^{\vee}\mid\widehat g_{c_4,J_4^C}^{\vee}\mid
\widehat g_{c_5,J_5^C}^{\vee}]$.
The proof retains the exact five-slot hatted subchain on $T_1,\ldots,T_5$ and
closes the $T_0$ slot by $A_0<1-h_{\mathrm{term}}<Z$.\\
\bottomrule
\end{tabular}
\caption{The reader-facing Strategy~2 $g$-composition register.  Every chain
shows all six functions.  An $\mathrm I$ records the weaker handoff
$A_{i+1}\ge A_i$ under Definition~\ref{def:body-six-slot-chain}; it is not an
informal placeholder or an unproved order relation between compositions.}
\label{tab:body-strategy2-chains}
\end{table}"""
s=replace_table_by_label(s,'tab:body-strategy2-chains',new_table)
save(rel,s)

# Replace the appended canonical section with a statement faithful to the
# existing branch chain lemmas, without a new universal monotonicity claim.
rel='proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md'
s=load(rel)
start=s.find('## 10. Full six-V-triangle branch chain')
if start<0: raise RuntimeError('section 10 missing')
new_section=r"""## 10. Full six-V-triangle branch register

For each $i\in\mathbb Z/6\mathbb Z$, parametrize the outgoing edge by

$$
\xi_i(t)=V_i+t(V_{i+1}-V_i),
\qquad 0\le t\le1,
$$

and let

$$
J_i^C=\xi_i^{-1}(T_C\cap e_{i,i+1})
$$

be the empty or closed scalar center interval.  Point contacts are retained as
degenerate intervals.  For a selected radial demand $c_i$, define

$$
\Phi_i^{\rm raw}=g_{c_i,J_i^C}^{\vee},
\qquad
\Phi_i^{\rm ns}=\widehat g_{c_i,J_i^C}^{\vee}.
$$

Use $\Phi_i^{\rm ns}$ when $T_i$ is nonsupercritical and
$\Phi_i^{\rm raw}$ otherwise.  The complete branch word is always displayed in
geometric V-triangle order as

$$
[\Phi_0\mid\Phi_1\mid\Phi_2\mid\Phi_3\mid\Phi_4\mid\Phi_5]
=\Phi_5\circ\Phi_4\circ\Phi_3\circ\Phi_2\circ\Phi_1\circ\Phi_0.
$$

The branch proposition determines how this word is used: cyclic composition,
a cut at a center trace followed by endpoint inequalities, or the exact
five-V-triangle subchain followed by a terminal cap.  Merely writing the word
does not assert an additional universal inequality beyond those branch
propositions.

An identity slot records a weaker *individual handoff*.  It is licensed only
when

$$
J_i^C=\varnothing,
$$

all nonincident boundary traces have been excluded on $e_{i,i+1}$, and $T_i$
is nonsupercritical.  Under precisely these hypotheses the generalized
handoff lemma and nonsupercritical extensivity give

$$
A_{i+1}\ge \widehat g_{c_i}^{\vee}(A_i)\ge A_i.
$$

Thus replacing the $i$th displayed function by $\mathrm I$ means that this
one inequality is weakened to $A_{i+1}\ge A_i$.  It is not, by itself, a
pointwise comparison between the two formal compositions; the corresponding
terminal proof supplies the valid global argument.

For the $N_+=1$ all-Vd0 one-gap branch, the full word has the raw
center-assisted slot $g_{c_0,J_0^C}^{\vee}$ followed by the five hatted slots
$\widehat g_{c_i,J_i^C}^{\vee}$ for $1\le i\le5$.  The one-gap proof retains
that exact five-V-triangle subchain and closes the remaining $T_0$ slot with
its independent terminal diameter cap.  Hence the six-slot reader register is
a faithful expansion of the proved certificate, not a new theorem.
"""
s=s[:start]+new_section+'\n'
save(rel,s)

rel='arrange/paper_draft/source_ledger.md'
s=load(rel)
s=s.replace('Table 2 displays six functions in every $g$-composition chain and states the\n  exact hypotheses under which an identity slot is a valid lower relaxation.',
            'Table 2 displays six functions in every $g$-composition chain, retains\n  point-contact center intervals in every exact slot, and states the exact\n  handoff inequality represented by each identity slot.')
if 'Post-edit audit repairs:' not in s:
    s=s.rstrip()+r"""

Post-edit audit repairs: the reader definition now reuses the appendix symbol
$\Delta_L$ for the signed companion trace; all six-slot words retain degenerate
center intervals; and identity slots are stated as weakened individual
handoff inequalities rather than as an unsupported order on formal
compositions.
"""+'\n'
save(rel,s)

body=load('arrange/paper_draft/02_reader_framework.tex')
tab=load('arrange/paper_draft/04_strategy2_summary.tex')
proof=load('proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md')
assert '\\sigma_L' not in body
assert body.count('\\Delta_L')>=2
assert 'no pointwise order between the two formal compositions' in tab
assert '\\succeq' not in tab
for i in range(6):
    assert f'c_{i},J_{i}^C' in tab
assert 'not, by itself, a pointwise comparison' in proof
assert 'A_0\\ge' not in proof[proof.find('## 10.') :]
print('FOLLOWUP_SAFE_OK')
