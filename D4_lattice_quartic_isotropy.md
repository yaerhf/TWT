# Quartic isotropy of the $D_4$ lattice

### An invariant-theoretic statement about rotational Lorentz violation from a discrete substrate, its sharpness, and its limits

*Draft — standalone note. All numerical claims are reproducible with the script in Appendix A
(numpy only, runtime ≈ 15 s).*

---

## Abstract

Let $G = \operatorname{Aut}(D_4)$ be the automorphism group of the $D_4$ root system in
$\mathbb{R}^4$, of order $1152$ (isomorphic to the Weyl group $W(F_4)$, whose invariant degrees are
$\{2,6,8,12\}$). Because $4$ admits no expression as a sum of parts drawn from $\{2,6,8,12\}$ other
than $2+2$, the space of
$G$-invariant quartic polynomials is **one-dimensional**, spanned by $(k^2)^2$. Consequently, for
*any* **scalar** dispersion kernel $K:\mathbb{R}^4\to\mathbb{R}$
that is invariant under the $D_4$ point group and analytic at $k=0$, the quartic term of its
derivative expansion is exactly $O(4)$-invariant: there is no anisotropic $k^4$ term for any kernel
in that class — a statement about the group, not about one model of it — and hence, given the
premises below and **(P-op)** in particular, no anisotropic dimension-six Lorentz-violating
operator. The leading anisotropy is pushed to $k^6$, i.e. to **dimension eight**. This bound is
*reached*, not merely an upper bound: the degree-6 invariant space is two-dimensional, containing
the explicit anisotropic invariant
$A(k) = 5k^2\sum_i k_i^4 - 4\sum_i k_i^6 - \tfrac54 (k^2)^3$, and the sixth bond moment of the
$D_4$ nearest-neighbour set is correspondingly anisotropic. The statement is specific to $D_4$ and
not a generic consequence of four-dimensionality: the hypercubic lattice $\mathbb{Z}^4$, whose point
group $W(B_4)$ has invariant degrees $\{2,4,6,8\}$, admits a two-dimensional degree-4 invariant
space containing $\sum_i k_i^4$, and its nearest-neighbour dispersion is direction-dependent already
at quartic order (axis-to-diagonal ratio $4$).

Four premises are load-bearing and are stated up front rather than in a footnote. Three of them
condition the theorem itself. **(P-an)**
analyticity in $k$, so that a derivative expansion exists at all; **(P-pg)** invariance under the
*full* point group **including triality** — the reflection subgroup $W(D_4)$ of order $192$ has a
*three*-dimensional degree-4 invariant space, and the second shell splits under it into **three**
orbits of eight: $\{\pm 2e_i\}$ (fourth-moment residual $32$) and the two coordinate-parity classes
of $(\pm1,\pm1,\pm1,\pm1)$ (residual $16$ each). Their combined fourth moment is isotropic **iff all
three carry equal weight**; a coupling that weights triality-related orbits unequally
restores dimension-six anisotropy. And **(P-sc)** the kernel is **scalar** — real-valued, carrying no
internal indices. The theorem does not extend to matrix-valued (equivariant) kernels; the published
dimension-six bounds quoted below are for photons, electrons and protons, none of which is a scalar
field.

The fourth premise conditions not the theorem but its *transfer* to Lorentz-violation
phenomenology, and the lattice mathematics below is untouched by it: **(P-op)** the symmetry
operative on the sector the transfer speaks about is the full point group, and not the proper
subgroup left intact by whatever singles out a rest frame. A medium that distinguishes an axis
$e_4$ — a driven or dissipative steady state, a condensate, a cosmological rest frame — leaves
operative only $\operatorname{Stab}_G(e_4)$, of order $48$, which restricts faithfully onto the
full octahedral group $W(B_3)$ on the transverse 3-space; there the degree-4 invariant space is
**two**-dimensional and an anisotropic *spatial* quartic is permitted. What protects the
nearest-neighbour kernel at that reduced group is then not the reduced symmetry but the constancy
of the coupling on the single full-group bond orbit. See §8.

We also state clearly what the result does **not** do. It constrains the *tensor structure* of the
quartic term and nothing else; the isotropic direction $(k^2)^2$ is available and, for the
nearest-neighbour $D_4$ kernel, occupied with an $O(1)$ coefficient,
$\omega^2 \propto k^2 - \tfrac{1}{12}a^2 (k^2)^2 + O(a^4 k^6)$. But that surviving term is built
from the **four**-dimensional square, and so is not a boost violation either: granting the naive
continuation of §7, a kernel that is a function of $k\cdot k$ alone continues to an exactly
Lorentz-invariant dispersion relation, in which the $-\tfrac{1}{12}$ term is a mass
renormalisation. An isotropic-but-boost-violating quartic would need $\lvert\mathbf k\rvert^4$,
which is not invariant under the point group at all — nor even under the hypercubic one. The
preferred frame that Lorentz-violation phenomenology presupposes must therefore come from
somewhere other than the kernel. **That is this note's flagship caveat: the hard step is the
passage from a Euclidean invariant-theoretic statement to a Lorentzian dispersion relation, and
this note does not perform it.** Lorentz violation is not solved here; what is supplied is one
exact statement about one of the structures a solution would have to use, and the premises under
which that statement may be quoted as physics.

Finally, on attribution: the *physical* content — that the $D_4$/$F_4$ lattice has an isotropic
quartic while the hypercubic lattice does not — is older than this note by four decades. It is the
organising criterion of the **lattice-gas hydrodynamics** literature of 1986–87, where the same
lattice appears as FCHC (the sites of $\mathbb{Z}^4$ with even coordinate sum) and is adopted
precisely because no three-dimensional regular lattice has an isotropic fourth-rank moment. The
*field-theoretic* reading — that this is what removes the dimension-six Lorentz-breaking operator of
the hypercubic regulator — is **Neuberger (1987)**; it was restated for lattice QCD as recently as
December 2025. The
group-level form of the statement, with triality named as the protecting mechanism, is due to Chow
(1999), and the two-sided sharpness (degree-4 isotropy "well known", the anisotropic sixth moment
computed) is established in the lattice-kinetic-theory literature (Chen–Goldhirsch–Orszag 2008).
What this note adds is a generality-and-rigour upgrade of those statements — one-dimensionality of
the invariant quartic space for *every* analytic point-group-symmetric kernel, via the $W(F_4)$
invariant degrees — and one narrow transfer: the dimension-four point-group protection argument is
already standard in Lorentz-violation effective field theory (Mattingly 2005;
Jacobson–Liberati–Mattingly 2006, who credit it to the lattice literature); what does not appear
there is that the same argument *fails* at dimension six for $\mathbb{Z}^4$ and *holds* for $D_4$.
See §9.

---

## 1. Introduction

### 1.1 Emergent Lorentz invariance and the anisotropy problem

A recurring idea across several research programmes is that continuum relativistic physics is not
fundamental but *emergent*: the low-energy excitations of some discrete or condensed substrate
organise themselves into fields obeying an approximately Lorentz-invariant dispersion relation, with
violations suppressed by the substrate scale. The idea is attractive and it is old, but it carries a
standing liability. A lattice is not rotationally invariant. It distinguishes directions — the axis
direction from the body-diagonal direction, say — and unless something removes that distinction, the
emergent dispersion relation inherits it.

In effective-field-theory language the liability is sharp. Write the dispersion relation of a
particle in the effective theory as

$$
E^2 \;=\; p^2 + m^2 + \sum_{n\ge 3} \eta^{(n)}\,\frac{p^n}{M^{\,n-2}} ,
$$

where $M$ is the scale at which the substrate becomes visible and $\eta^{(n)}$ is dimensionless. A
$p^n$ term arises from an operator of mass dimension $n+2$; thus $n=3$ corresponds to a
dimension-five operator, $n=4$ to a dimension-six operator, and $n=6$ to a dimension-eight operator
[Myers–Pospelov 2003; Liberati 2013]. The empirical situation for $n=4$ is that the coefficients are
bounded well below unity. Liberati's review quotes, for the QED sector,

$$
-10^{-7} \lesssim \xi^{(4)} \lesssim 10^{-8}, \qquad
-10^{-7} \lesssim \eta^{(4)} \lesssim 10^{-6}
$$

for photons and electrons respectively (eq. 75 of that review), and, from the ultra-high-energy
cosmic-ray spectrum assuming pure-proton composition,
$-10^{-3} \lesssim \eta^{(4)}_p \lesssim 10^{-6}$ at 99% CL (eq. 76). Its summary Table 2 gives
typical $n=4$ strengths of $O(10^{-8})$ for photons and electrons and $O(10^{-6})$ for protons.

Now put a substrate at a scale $\Lambda$ underneath (throughout this note $\Lambda$ denotes the
inverse lattice spacing $1/a$ — a physical length, not a loop-regulator scheme scale). Its natural contribution to the $p^4$ term is
$c\,p^4/\Lambda^2$ with $c = O(1)$, which in the normalisation above means
$\eta^{(4)} = c\,(M_{\rm Pl}/\Lambda)^2$. If $\Lambda$ is anywhere near the Planck scale, an $O(1)$
substrate coefficient overshoots the bounds by many orders of magnitude. This is why dimension-six
Lorentz violation is the usual killer for lattice-substrate proposals: it is the lowest order at
which a CPT-even substrate effect generically appears, and it is measured.

It is worth separating two distinct things that both live at dimension six, because they are
constrained by different data:

* the **anisotropic** part — a term such as $\sum_i p_i^4$ that depends on the orientation of
  $\mathbf p$ relative to the substrate axes. This is the part that is manifestly a lattice
  artefact; its coefficients are constrained by the directional and sidereal analyses tabulated in
  the SME data tables [Kostelecký–Russell];
* the **isotropic** part — a term $(\mathbf p^2)^2$ that is invariant under spatial rotations but
  still violates boost invariance. This is what the bounds quoted above constrain: the caption of
  Liberati's Table 2 specifies "rotational invariant" LIV operators.

Both descriptions presuppose a **preferred frame** — a split of the four momentum components into
$E$ and $\mathbf p$ — and that is precisely what the theorem below does not have. The theorem lives
on four Euclidean axes with no distinguished direction, and the quartic invariant it forces,
$(k\cdot k)^2$, is built from the *four*-dimensional square. Two consequences follow, and together
they are the honest framing of everything after this section.

*First, the surviving quartic term does not by itself produce a dimension-six Lorentz violation of
either kind.* Grant the naive continuation that §7 gestures at, $k\cdot k \to p_\mu p^\mu$. Then the
pole condition $c_0 + c_2\,p_\mu p^\mu + c_4\,(p_\mu p^\mu)^2 = 0$ is a polynomial in $p_\mu p^\mu$
alone, and its roots sit at *constant* $p_\mu p^\mu$: the dispersion relation is exactly
$E^2 = \mathbf p^2 + m_{\rm phys}^2$, to all orders in the lattice spacing and not merely to the
order computed. The $O(a^2)$ term is a mass renormalisation, contributing $\eta^{(4)} = 0$ rather
than an $O(1)$ coefficient. This is what the Katz–Nogradi sentence quoted in §1.3 says — "at order
$O(a^2)$ the correction is still **Lorentz** invariant" — and §5 sharpens it: every term below
degree six is $O(4)$-invariant, so on this reading the first violation *of any kind* sits at
dimension eight.

*Second, an isotropic-but-boost-violating quartic has no invariant to sit on.* Such a term needs
$\lvert\mathbf k\rvert^4 = (k_1^2+k_2^2+k_3^2)^2$, which is not $G$-invariant — nor even
$W(B_4)$-invariant; any element exchanging $e_4$ with $e_1$ moves it. A substrate whose kernel is
symmetric under the full four-dimensional point group supplies no structure on which a preferred
frame could be built. **The preferred frame must come from somewhere other than the kernel, and
locating it is the hard part.**

**That is the flagship caveat of this note, and it replaces a weaker one: the difficult step is the
passage from a Euclidean invariant-theoretic statement to a Lorentzian dispersion relation, and
this note does not perform it.** What is proved below is a fact about a finite group acting on
$\mathbb{R}^4$. Reading it as a statement about the spatial rotational invariance of a physical
dispersion relation requires a distinguished axis, a continuation, and — because whatever supplies
that axis generically *reduces the operative symmetry group* — the further premise (P-op) of §8.4.
The bounds quoted above are given as motivation for caring about the question, not as quantities
this theorem computes. The point is restated in §7, §8.4 and §8.5.

### 1.2 Statement of the result

The $D_4$ lattice — the set of integer 4-vectors with even coordinate sum, equivalently the
four-dimensional body-centred cubic lattice, equivalently the vertex set of the 16-cell honeycomb —
has an unusually large point group: order $1152$, three times that of the hypercubic lattice. That
extra factor of three is *triality*, the exceptional outer symmetry of $D_4$.

The consequence we exploit is a fact of classical invariant theory. The invariant degrees of $W(F_4)$
are $\{2,6,8,12\}$. There is **no degree-4 basic invariant**. Since the only way to build a
$G$-invariant quartic from basic invariants of degrees $2,6,8,12$ is as the square of the quadratic
one, the space of $G$-invariant quartics is one-dimensional, spanned by $(k^2)^2$. Therefore:

> **Any $D_4$-point-group-symmetric kernel that is analytic at $k=0$ has an exactly isotropic quartic
> term.**

Because the argument is about the group rather than about a particular action, it applies to the
tree-level kernel, to any radiative correction generated by a point-group-preserving regulator, and
to any nearest-neighbour, next-nearest-neighbour or arbitrarily-improved discretisation, provided
only that the couplings respect the full point group. There is no anisotropic quartic invariant for
an anisotropic dimension-six operator to be built from — and hence, *for a sector on which the full
point group is the operative symmetry*, no such operator to fine-tune away. That qualifier is
premise (P-op) of §8.4 and it is not decorative: the same medium that supplies the preferred frame
the phenomenological reading needs will generally leave only a subgroup of $G$ operative, and at
that subgroup the anisotropic spatial quartic is permitted again.

The leading anisotropy then sits at $k^6$: dimension eight. For a substrate at scale $\Lambda$, the
relative size of the leading anisotropic effect is $(E/\Lambda)^4$ rather than $(E/\Lambda)^2$.

### 1.3 Provenance and scope of the novelty claim

The result was isolated in the course of a lattice-substrate emergent-spacetime programme; nothing in
this note depends on that programme, and no part of it is assumed below. The reader needs only
$\mathbb{R}^4$, a root system, and a Taylor expansion.

The novelty claim is deliberately narrow, and is set out in full in §9. In brief: the *physics* is
known, and known earlier than the lattice-field-theory citations alone would suggest — the
fourth-rank isotropy of the $D_4$/FCHC bond set, and the failure of the hypercubic lattice at the
same order, are the organising criterion of the 1986–87 lattice-gas automaton literature (§9(0)).
Neuberger (1987) argued that $F_4$ lattices are singularly well suited to regularising scalar
fields precisely because the dimension-six Lorentz-breaking operator that afflicts the hypercubic
lattice is absent; the free $F_4$ dispersion $g(p) = p^2 - \tfrac{1}{12}(p^2)^2 + O(p^6)$ has been in
the literature since then; and Katz and Nogradi (2025) state for the same lattice that "at order
$O(a^2)$ the correction is still Lorentz invariant, the first order where this does not hold is
$O(a^4)$". The group-level statement and its mechanism are also known: Chow (1999) states that $D_4$
"is the only unexceptional root lattice" that is exactly isotropic at order $a^2$ and names the
accidental threefold Dynkin-diagram symmetry — triality — as what protects it, and
Chen–Goldhirsch–Orszag (2008) treat the degree-4 isotropy as well known and compute the anisotropic
sixth moment. What is offered here is a proof at a still higher level of generality — valid for
every analytic point-group-symmetric kernel, via the invariant degrees of $W(F_4)$ — together with
the explicit premises, and the one transfer that does appear to be absent from the literature: the
dimension-six form of a protection argument that Lorentz-violation EFT already uses at dimension
four.

---

## 2. Setup and conventions

We work in $\mathbb{R}^4$ with the standard Euclidean inner product; $k = (k_1,k_2,k_3,k_4)$ denotes
a wavevector and $k^2 = k\cdot k$. Nothing in the group theory depends on signature; the passage to
a Lorentzian dispersion relation is discussed in §7 and involves an additional assumption that we
flag rather than hide.

**Lattice.** $D_4 = \{x \in \mathbb{Z}^4 : \textstyle\sum_i x_i \in 2\mathbb{Z}\}$. Its minimal
vectors (the $D_4$ *root system*, and simultaneously its nearest-neighbour bond set) are the $24$
vectors obtained from $(\pm1,\pm1,0,0)$ by permutation of coordinates, each of squared length $2$.
The *lattice* kissing number $24$ is maximal among four-dimensional lattices [Conway–Sloane]; that
$24$ is also the **unrestricted** four-dimensional kissing number — no packing of any kind does
better — was a long-standing open problem, settled only by Musin (2008). The convex hull of these
$24$ points is the regular 24-cell.

**Point group.** $G := \operatorname{Aut}(D_4\text{ root system}) = \{A \in O(4) : A\Phi = \Phi\}$
where $\Phi$ is the $24$-element root set. We verify computationally that $|G| = 1152$ (§3).

**Kernel.** By a *dispersion kernel* we mean a function $K : \mathbb{R}^4 \to \mathbb{R}$ that
encodes the quadratic part of the substrate's effective action in momentum space — for a free
lattice field with couplings $J_v$ on bonds $v$, $K(k) = \sum_v J_v\,(1 - \cos(a\,k\cdot v))$, but
the theorem does not require this form.

**Assumption (P-an) — analyticity.** $K$ is analytic in a neighbourhood of $k = 0$, so that
$K(k) = \sum_{d\ge0} P_d(k)$ with $P_d$ homogeneous of degree $d$, converging near the origin.

**Assumption (P-pg) — point-group symmetry.** $K(Ak) = K(k)$ for all $A \in G$, with $G$ the
**full** group of order $1152$, not a subgroup.

**Assumption (P-sc) — scalar kernel.** $K$ is real-valued: $K:\mathbb{R}^4\to\mathbb{R}$, carrying
no internal (polarization, flavour, spinor) indices. A matrix-valued kernel $M_{\mu\nu}(k)$ obeys
*equivariance*, $M(Ak) = A\,M(k)\,A^{\mathsf T}$, not invariance, and lives in a larger
invariant-theory object that the proof below never touches. §8.3 shows the restriction is
load-bearing rather than decorative.

**Assumption (P-op) — the operative symmetry.** *This one is a premise on the physical transfer,
not on the theorem.* The mathematics of §3–§7 is a statement about the group $G$ of order $1152$
and is untouched by (P-op): as invariant theory the theorem needs (P-an) and (P-pg) and nothing
more. What (P-op) conditions is the *quotation* of that conclusion as a statement about the
rotational anisotropy a physical substrate would exhibit. For that reading, the group whose
invariants are counted must be the group operative on the sector the claim is about — and a medium
that distinguishes a rest frame does not leave all of $G$ operative. §8.4 states the premise
precisely, computes what the reduction costs, and gives its would-change-if.

**EFT dictionary.** With a dispersion relation $E^2 = p^2 + m^2 + \sum_n \eta^{(n)} p^n/M^{n-2}$, a
$p^n$ term originates in a mass-dimension-$(n+2)$ operator. We will use the two dictionary entries
$n = 4 \leftrightarrow$ dimension six and $n = 6 \leftrightarrow$ dimension eight throughout.

**Moments.** For a finite set $S \subset \mathbb{R}^4$ with weights $w_v$, the $2m$-th moment tensor
is $M_{i_1\cdots i_{2m}} = \sum_{v\in S} w_v\, v_{i_1}\cdots v_{i_{2m}}$. We call the fourth moment
*isotropic* if $M_{ijkl} = A(\delta_{ij}\delta_{kl} + \delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})$
for some $A$, and measure failure by the **residual**
$\max_{ijkl} |M_{ijkl} - A(\delta\delta+\delta\delta+\delta\delta)_{ijkl}|$ with $A$ fixed by the
mixed component $M_{1122}$. This residual is a raw, unnormalised diagnostic: it is neither
scale-invariant nor divided by the orbit size, so residuals may be compared *within* a table but not
across tables, lattices, or normalisations. Where a scale-free comparison is wanted, the right
quantity is the ratio of the degree-4 harmonic component of the moment to its isotropic part; every
statement below uses the residual only as a zero/nonzero test and as a like-for-like comparison at
fixed total weight.

---

## 3. The $D_4$ lattice and its automorphism group

The $24$ roots form a single orbit already under the reflection subgroup $W(D_4)$ (the even signed
permutations, of order $4!\cdot 2^3 = 192$), and a fortiori under the full group. What distinguishes
the groups is not their action on the roots but their invariant rings:

| group | description | order | invariant degrees | $\dim$ of degree-4 invariants |
|---|---|---:|---|---:|
| $W(D_4)$ | even signed permutations | $192$ | $\{2,4,4,6\}$ | **3** |
| $W(B_4)$ | all signed permutations $=\operatorname{Aut}(\mathbb{Z}^4)$ | $384$ | $\{2,4,6,8\}$ | **2** |
| $G = \operatorname{Aut}(D_4) \cong W(F_4)$ | $W(D_4)\rtimes S_3$ (triality) | $1152$ | $\{2,6,8,12\}$ | **1** |

The chain $W(D_4) \subset W(B_4) \subset G$ has indices $2$ and $3$; the index-$3$ step is where
triality enters. Precisely: $G/W(D_4) \cong S_3$ is the triality group, and $G = \langle W(B_4), T
\rangle$, which suffices because $W(B_4)$ is maximal in $G$ — so a *single* extra element generates
the missing index-3 step even though that element is not itself of order 3. The generator we use is
the orthogonal **involution** ($T^2 = \mathbb{1}$, $\det T = -1$; triality *proper* is the order-3
outer automorphism, and $T$ maps to a transposition in $S_3$, not to a 3-cycle)

$$
T \;=\; \tfrac12\begin{pmatrix} 1&1&1&1\\ 1&1&-1&-1\\ 1&-1&1&-1\\ 1&-1&-1&1\end{pmatrix},
\qquad T^{\mathsf T}T = \mathbb{1},
$$

which maps the axis direction $e_1$ to the body diagonal $(1,1,1,1)/2$ while permuting the roots
(e.g. $T(1,-1,0,0) = (0,0,1,1)$). It is this element that the hypercubic group lacks, and it is
exactly what removes the degree-4 anisotropic invariants.

Two remarks that matter for what follows.

*(i) $G$ is the $F_4$ automorphism group.* $G$ preserves not only the $24$ roots but also the second
shell of $D_4$ — the $24$ vectors $\{\pm 2e_i\} \cup \{(\pm1,\pm1,\pm1,\pm1)\}$ of squared length $4$.
Rescaling the second shell by $1/2$ produces the $24$ short roots of $F_4$; together with the $24$
long roots they form the $48$-root $F_4$ system, and $G$ is its Weyl group. This is why the invariant
degrees are those of $F_4$. (Verified in Appendix A.)

*(ii) The group is computed, not assumed.* In Appendix A the group is constructed as a **stabiliser**
— by enumerating all orthogonal maps carrying a fixed basis of roots to another basis with the same
Gram matrix and retaining those that permute the root set — rather than by taking the closure of a
guessed generating set. This matters, because assuming a generating set is precisely how one could
accidentally build a subgroup and get the wrong invariant dimensions. The two constructions agree.

---

## 4. Bond moments

The nearest-neighbour bond set of $D_4$ (the $24$ roots, unit weights) has moments

$$
\sum_v v_i v_j = 12\,\delta_{ij},
$$

$$
M_{1111} = 12, \qquad M_{1122} = 4, \qquad
M_{ijkl} = 4\,(\delta_{ij}\delta_{kl} + \delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk}) \ \ \text{exactly},
$$

so $M_{1111} = 12 = 3\,M_{1122}$ and the isotropy residual is **zero**. The sixth moment, by
contrast, is anisotropic in the strongest possible sense: no bond has three non-vanishing
coordinates, so

$$
M_{112233} = 0, \qquad \text{while} \qquad M_{111111} = 12 \ne 0,
$$

and an isotropic rank-6 tensor with vanishing $M_{112233}$ vanishes identically. Contracting, the
full sixth moment is

$$
M_6(k) \;=\; \sum_v (k\cdot v)^6 \;=\; 60\,k^2 \sum_i k_i^4 \;-\; 48 \sum_i k_i^6 ,
$$

which is $G$-invariant (checked directly against the triality generator $T$) even though neither
$\sum_i k_i^4$ nor $\sum_i k_i^6$ is invariant separately.

**The free dispersion.** For the nearest-neighbour kernel with lattice spacing $a$,

$$
\frac{1}{6}\sum_{v} \bigl(1 - \cos(a\,k\cdot v)\bigr)
= a^2 k^2 \Bigl[\, 1 \;-\; \frac{a^2}{12}\,k^2 \;+\; \frac{a^4}{360\,k^2}\Bigl(5k^2\!\sum_i k_i^4 - 4\sum_i k_i^6\Bigr) \;-\;\cdots \Bigr].
$$

The quartic coefficient is $-1/12$ **independently of direction** — the numerically extracted value
agrees with $-1/12$ to eight digits along random directions (Appendix A).

**Pinning the normalisation before quoting the literature.** The number $-1/12$ is
convention-dependent and the convention must be stated or the comparison is empty. Here $a$
multiplies $k\cdot v$ with $|v|^2 = 2$, so $a$ is *not* the nearest-neighbour distance: the bonds
have length $a\sqrt2$. Writing the same kernel in terms of the bond length $b = a\sqrt2$ gives
$b^2k^2\bigl[\tfrac12 - \tfrac{b^2}{48}k^2\bigr]$, i.e. a quartic-to-quadratic ratio of $-1/24$, not
$-1/12$. The direction-independence is the convention-free content; the *value* agrees with the
$F_4$ dispersion $g(p) = p^2 - \tfrac{1}{12}(p^2)^2 + O(p^6)$ quoted in the lattice literature only
in the normalisation used here, and the reader should confirm the source's convention before
treating the match as an external check. What is genuinely convention-free, and is what the check
actually tests, is the moment ratio $M_{1111} = 3M_{1122}$.

Note what the same expansion says about the *isotropic* dimension-six term: it is right there, with
coefficient $-1/12$. Nothing in this note removes it. See §8.

---

## 5. The invariant-theory argument

This section contains the whole theorem. It is short, which is the point: the content is a property
of the group, and everything else is bookkeeping.

Let $\mathbb{R}[k]^G_d$ denote the space of $G$-invariant homogeneous polynomials of degree $d$ in
$k_1,\dots,k_4$.

**Lemma 1 (Chevalley–Shephard–Todd).** $G \cong W(F_4)$ is a finite reflection group, so its
invariant ring $\mathbb{R}[k]^G$ is a polynomial algebra on four algebraically independent
homogeneous generators, of degrees $d_1,\dots,d_4$. For $F_4$ these degrees are $\{2,6,8,12\}$
(equivalently, the exponents are $1,5,7,11$ and the Coxeter number is $12$). *The degrees are an
invariant of the group together with its **reflection representation**, not of the abstract group:
the statement applies here because $G$ acts on $\mathbb{R}^4$ in exactly that representation, which
is why Remark (i) below — that $G$ is the Weyl group of the $F_4$ root system, acting on its own
root space — is a step in the argument and not decoration.*

**Lemma 2 (Poincaré series).** Consequently
$\sum_d \dim \mathbb{R}[k]^G_d\, t^d = \prod_{j=1}^4 (1-t^{d_j})^{-1}$, and
$\dim \mathbb{R}[k]^G_d$ equals the number of multisets of parts drawn from $\{2,6,8,12\}$ summing
to $d$.

Reading off the first few coefficients for $\{2,6,8,12\}$:

| $d$ | 2 | 4 | 6 | 8 | 10 | 12 |
|---|---:|---:|---:|---:|---:|---:|
| $\dim\mathbb{R}[k]^G_d$ | 1 | **1** | 2 | 3 | 3 | 5 |

The entry that carries the physics is $d = 4$: the only partition of $4$ into parts from
$\{2,6,8,12\}$ is $2+2$.

**Theorem (quartic isotropy).** *Let $K:\mathbb{R}^4 \to \mathbb{R}$ satisfy (P-an) and (P-pg). Then
the degree-4 term of its Taylor expansion at the origin is a multiple of $(k\cdot k)^2$; that is, it
is exactly rotationally invariant.*

*Proof.* By (P-an), $K = \sum_d P_d$ with $P_d$ homogeneous of degree $d$. Averaging the identity
$K(Ak) = K(k)$ over $A \in G$ and matching homogeneous components shows each $P_d \in
\mathbb{R}[k]^G_d$. By Lemmas 1–2, $\dim \mathbb{R}[k]^G_4 = 1$. Since $(k\cdot k)^2$ is a nonzero
element of that space, $P_4 \in \mathbb{R}\,(k\cdot k)^2$. $\square$

**Corollary (everything below degree six is $O(4)$-invariant).** *Under the same hypotheses,
$P_1 = P_3 = P_5 = 0$ and $P_2 \in \mathbb{R}\,k^2$, so*

$$
K(k) \;=\; c_0 \;+\; c_2\,k^2 \;+\; c_4\,(k^2)^2 \;+\; P_6(k) \;+\; O(k^8),
$$

*with $P_6$ the first term the group permits to depart from full $O(4)$ symmetry.*

*Proof.* $-\mathbb{1} \in W(D_4) \subset G$, so every $G$-invariant polynomial is even and all odd
homogeneous components vanish. The table above gives $\dim\mathbb{R}[k]^G_2 = 1$, whence
$P_2 \in \mathbb{R}\,k^2$, and $\dim\mathbb{R}[k]^G_4 = 1$ is the theorem. $\square$

This costs nothing extra and is worth stating, because it is what the invariant degrees
$\{2,6,8,12\}$ actually say: the first degree at which the group *permits* any departure from
$O(4)$ symmetry is six. In particular the same one-line argument removes every odd power, CPT-odd
$p^3$ terms (dimension five) included, and it does so for the whole class of kernels at once.

**Corollary (no anisotropic dimension-six operator).** A dispersion relation derived from such a
kernel has an $O(k^4)$ term of the form $c\,(k^2)^2$ with $c$ a single constant, and no
direction-dependent $k^4$ contribution, for any choice of **scalar** couplings compatible with the
full point group — premise (P-sc).

Reading that as *"hence no anisotropic dimension-six LIV operator"* is a further step, and it
carries two conditions that are not optional. The first is the passage from the Euclidean $k$ to an
observer's $(E,\mathbf p)$: that step is not performed in this note (§1.1, §7), and within the
four-dimensional invariant theory the statement above is neither about spatial rotations nor about
boosts. The second is premise **(P-op)** of §8.4 — the group whose invariants have just been
counted must be the group operative on the sector the LIV claim concerns. If the medium that
supplies the observer's preferred frame leaves only a subgroup of $G$ intact, the relevant
invariant space is that subgroup's, and it is larger: at the stabiliser of the distinguished axis
the anisotropic *spatial* quartic is permitted, and what protects the nearest-neighbour kernel
there is a property of the coupling rather than of the symmetry. The invariant-theoretic content
above is exact; the phenomenological sentence is conditional on both steps.

Premise (P-sc) is likewise load-bearing rather than decorative, because the point group cannot
close the matrix-valued sector. Here is the two-line reason. Take the pseudo-dipolar bond coupling, the natural $W(F_4)$-symmetric
symmetric-rank-2 kernel, $M_{\mu\nu}(k) = \sum_v v_\mu v_\nu\,\bigl(1-\cos(k\cdot v)\bigr)$; its
four-derivative part is $T_{\mu\nu}(k) = \sum_v v_\mu v_\nu (k\cdot v)^4$ up to a constant. Contract
with $k$:

$$
T_{\mu\nu}(k)\,k^\mu k^\nu \;=\; \sum_v (k\cdot v)^6 \;=\; M_6(k),
$$

which §6 shows is **not** a multiple of $(k^2)^3$. But any isotropic symmetric rank-2 tensor built
from $k$ has the form $\alpha(k^2)\,\delta_{\mu\nu} + \beta(k^2)\,k_\mu k_\nu$, whose contraction
with $k^\mu k^\nu$ is a rotationally invariant degree-6 polynomial, hence a multiple of $(k^2)^3$.
So $T_{\mu\nu}$ is not isotropic. The two-derivative part $\sum_v v_\mu v_\nu (k\cdot v)^2$ *is*
isotropic — it is the (isotropic) fourth moment contracted twice — so the splitting appears exactly
at four derivatives and not before. Numerically (Appendix A) the eigenvalues of $T_{\mu\nu}$
transverse to $k$ are threefold degenerate at $4$ along $e_1$ and at $2$ along
$(1,1,0,0)/\sqrt2$ — different values, so the *magnitude* already depends on direction — and along a
generic direction they are **non-degenerate**: a direction-dependent four-derivative polarization
splitting, present in the simplest $W(F_4)$-symmetric matrix-valued kernel there is.

Three remarks.

**(a) It is a statement about the group, not about a model.** The usual way this fact is established
in the lattice literature is by expanding a specific free action and observing that the $O(a^2)$
correction comes out proportional to $(p^2)^2$. That is a computation about one kernel. The
invariant-theory statement covers all of them at once: improved actions, longer-range couplings,
radiatively generated terms, and terms whose form nobody has written down — provided only that they
respect $G$ and are analytic.

**(b) Equivalent harmonic formulation.** Decomposing degree-4 polynomials as
$\mathcal{H}_4 \oplus k^2\mathcal{H}_2 \oplus (k^2)^2\mathcal{H}_0$ into spaces of harmonics,
$\dim\mathbb{R}[k]^G_4 = \dim \mathcal{H}_4^G + \dim \mathcal{H}_2^G + 1$. Since
$\dim\mathbb{R}[k]^G_2 = 1$ we have $\mathcal{H}_2^G = 0$, so the theorem is exactly the statement
$\mathcal{H}_4^G = 0$: **$G$ admits no invariant harmonic of degree 4**.

**(c) Spherical-design corollary — this is Sobolev's theorem.** If $\mathcal{H}_4^G = 0$ then for
any $Y \in \mathcal{H}_{d}$ with
$d \le 4$ and any $G$-orbit $\mathcal{O}$ on a sphere, $\sum_{v\in\mathcal{O}} Y(v) = 0$ — the sum
defines a $G$-invariant functional on $\mathcal{H}_d$, which must vanish when $\mathcal{H}_d^G = 0$.
Hence **every $G$-orbit on a sphere is a spherical 4-design**, and a 5-design since $-\mathbb{1}\in G$
kills the odd degrees. The derivation is retained above for self-containedness, but the statement is
not new: it is Sobolev's theorem (1962) — for a finite reflection group, an invariant cubature
formula is exact to degree $t$ **iff** it is exact on the invariant polynomials of degree $\le t$ —
specialised to a group whose invariants of degree $\le 4$ all restrict to constants on the sphere.

The converse also holds, and it corrects a claim made in an earlier draft of this note. If every
$G$-orbit on a sphere is a 4-design and $Y \in \mathcal{H}_4^G$ were nonzero, pick $x$ with
$Y(x) \ne 0$; $G$-invariance makes $Y$ constant on the orbit of $x$, so the orbit sum is a nonzero
multiple of $Y(x)$, contradicting the design property. Hence $\mathcal{H}_4^G = 0$ is
**equivalent** to "every $G$-orbit is a 4-design", not strictly stronger than it — and since a
weighted union of designs is a design, the "arbitrary weighted combinations of orbits" argument
establishes nothing extra. What the group statement *is* stronger than is the classical
single-orbit fact that the $24$-cell is a spherical 5-design
[Delsarte–Goethals–Seidel 1977; Cohn–Conway–Elkies–Kumar 2007], which it implies.
A concrete instance of the theorem: the Reynolds average of $k_1^4$ over $G$ is
exactly $\tfrac18 (k^2)^2$, which is precisely the average of $k_1^4$ over the full rotation group
$O(4)$, namely $3|k|^4/(4\cdot 6)$. The finite group of order $1152$ reproduces the continuous
average exactly at fourth order.

---

## 6. Sharpness: dimension eight is reached, not merely bounded

A protection statement of the form "the leading effect is at order $N$" has two halves, and quoting
only the first is a common way to overstate. The first half is the theorem of §5: nothing anisotropic
at $p^4$. The second half is that something anisotropic really does appear at $p^6$ — otherwise
"dimension eight" would be an unchecked upper bound, and the true leading order might be higher
still (or absent).

From the table in §5, $\dim\mathbb{R}[k]^G_6 = 2$. One direction is $(k^2)^3$. The other is
anisotropic. Explicitly, using the sixth-moment contraction of §4 and subtracting its isotropic part
(the spherical averages are $\langle\sum_i k_i^4\rangle = |k|^4/2$ and
$\langle\sum_i k_i^6\rangle = \tfrac{5}{16}|k|^6$),

$$
\boxed{\;A(k) \;=\; 5\,k^2\sum_i k_i^4 \;-\; 4\sum_i k_i^6 \;-\; \tfrac54\,(k^2)^3\;}
$$

is $G$-invariant, nonzero, and orthogonal to the isotropic direction. On unit vectors it takes the
values

$$
A(e_1) = -\tfrac14, \qquad A\!\left(\tfrac{(1,1,0,0)}{\sqrt2}\right) = +\tfrac14 .
$$

Both signs occur, so $A$ genuinely separates directions and the anisotropy at sixth order is real. A
useful consistency check on the group: $A(e_1) = A\bigl((1,1,1,1)/2\bigr)$, because the axis and the
body diagonal are related **by triality** and therefore cannot be distinguished by any $G$-invariant.
The directions that $A$ separates are the short-root and long-root directions of $F_4$, which lie in
genuinely different orbits.

Independently, the sixth *bond* moment of the $D_4$ nearest-neighbour set is anisotropic
($M_{112233}=0$ while $M_{111111}=12$), which exhibits the anisotropic sextic already in the simplest
possible kernel rather than merely asserting that one exists.

Both sides therefore hold: **no anisotropy at dimension six, anisotropy present at dimension eight.**
Dimension eight is the leading order, and the relative suppression of the leading anisotropic effect
is $(E/\Lambda)^4$.

---

## 7. The $\mathbb{Z}^4$ contrast: this is not a fact about four dimensions

The natural sceptical reading of §5 is that any reasonably symmetric four-dimensional lattice would
do as well, and that the result is a soft consequence of having four dimensions and a lot of
symmetry. It is not. The hypercubic lattice fails at exactly the order in question.

For $\mathbb{Z}^4$ the point group is $W(B_4)$, of order $384$, with invariant degrees
$\{2,4,6,8\}$. Because $4$ is itself a degree, $\dim\mathbb{R}[k]^{W(B_4)}_4 = 2$: the invariant
quartics are spanned by $(k^2)^2$ **and** $\sum_i k_i^4$. The second is anisotropic, and there is no
symmetry reason for its coefficient to vanish.

Concretely, the nearest-neighbour bond set $\{\pm e_i\}$ has

$$
N_{1111} = 2, \qquad N_{1122} = 0, \qquad \text{isotropy residual } = 2 \ne 0,
$$

and the corresponding free dispersion is

$$
\sum_i \bigl(2 - 2\cos(a k_i)\bigr) \;=\; a^2\Bigl[k^2 - \frac{a^2}{12}\sum_i k_i^4 + \cdots\Bigr],
$$

whose quartic coefficient along a unit direction $u$ is $-\tfrac{1}{12}\sum_i u_i^4$ — equal to
$-1/12$ along an axis but $-1/48$ along the body diagonal, a **factor of $4$** direction dependence
at the leading correction. In LIV-EFT terms this is precisely an anisotropic dimension-six operator
with an $O(1)$ coefficient.

So the difference between $\mathbb{Z}^4$ and $D_4$ is not a matter of degree but of the presence or
absence of a degree-4 basic invariant, i.e. of triality. The result is an $F_4$ fact, not a
four-dimensionality fact. This is what makes it worth stating: it is substrate-specific and it
discriminates.

*(A caveat on transfer to Lorentzian signature: all of the above concerns a Euclidean point group
acting on a four-dimensional momentum space. Reading the conclusion as a statement about spatial
rotational invariance of a Lorentzian dispersion relation requires a further step — a choice of
distinguished axis and a continuation — which we do not perform here and which is not part of the
theorem. What is proved is the invariant-theoretic statement; the phenomenological reading is offered
as motivation, not as a corollary. This is the flagship caveat of §1.1, and the choice of
distinguished axis carries a second cost as well: it reduces the operative symmetry group, which is
premise (P-op) of §8.4.)*

---

## 8. Premises, and what is not claimed

### 8.1 (P-an) Analyticity

The proof consists of matching homogeneous components of a Taylor series. If the kernel is not
analytic at $k = 0$ — for instance if the substrate has a memory kernel producing $|k|^3$, $k^2\log
k^2$, or fractional-power terms — the argument does not apply. Polynomial invariant theory constrains
polynomials. A non-analytic kernel can be $G$-invariant and still direction-dependent at leading
non-quadratic order.

This is a real restriction, not a formality, and the loophole is not empty — here is an explicit
counterexample, built from material already on the table. Let $A(k)$ be the anisotropic sextic
invariant of §6. Then

$$
K_\epsilon(k) \;=\; k^2 \;+\; \epsilon\,\bigl|A(k)\bigr|^{2/3}
$$

is continuous, $G$-invariant, and its leading correction $|A|^{2/3}$ is homogeneous of degree $4$ —
yet it is **not** a multiple of $(k^2)^2$. It cannot be: $A$ takes both signs on the unit sphere and
therefore vanishes on a nontrivial cone (along the arc from $e_1$ to $(1,1,0,0)/\sqrt2$ it vanishes
at exactly $\pi/8$, where $A = 0$ identically), so $|A|^{2/3}/(k^2)^2$ is not constant. A degree-4
homogeneous function analytic at the origin would have to *be* a quartic polynomial, and the only
$G$-invariant one is $c\,(k^2)^2$; so $|A|^{2/3}$ is non-analytic, exactly as the premise requires,
and $K_\epsilon$ is a $G$-symmetric kernel with a genuinely anisotropic degree-four part. (All four
properties — invariance under all $1152$ elements, degree-4 homogeneity, non-constancy of the ratio
to $(k^2)^2$, and the zero on the sphere — are checked in Appendix A.)

The honest statement is therefore: *given a
derivative expansion, the quartic term is isotropic; whether a derivative expansion exists is a
separate question about the dynamics.*

**A partial rescue for the one case that matters most.** The realistic way analyticity fails in an
interacting theory is that massless loops generate logarithms, and the news there is good. A term
$f(k)\log k^2$ with $f$ homogeneous of degree $4$ still requires $f$ itself to be $G$-invariant —
$\log k^2$ is already invariant, and the analytic and log-multiplied parts cannot mix — so $f$ is
forced to $(k^2)^2$ and the term is $(k^2)^2\log k^2$, isotropic. Logarithmic non-analyticity does
not reopen the anisotropic channel; power-law and fractional non-analyticity, of the
$|A|^{2/3}$ type above, does. This makes the loop-robustness claim at the end of §8.5 tighter than
a bare appeal to "any $G$-preserving regulator" would be.

### 8.2 (P-pg) The full point group, including triality

The theorem requires invariance under all $1152$ elements. If the couplings are only $W(D_4)$-
symmetric (order $192$), the degree-4 invariant space is **three**-dimensional and there is no
protection at all. Even $W(B_4)$ symmetry (order $384$) leaves a two-dimensional degree-4 space, as
§7 shows.

The failure mode is concrete and worth spelling out, because it is how a real model would lose the
result without anybody noticing. Consider the second shell of $D_4$ — the $24$ vectors
$\{\pm2e_i\}\cup(\pm1,\pm1,\pm1,\pm1)$ of squared length $4$. It is a single orbit under $G$; it
splits into **two** orbits under $W(B_4)$ (sizes $8$ and $16$); and it splits into **three** orbits
of eight under $W(D_4)$, because even signed permutations preserve the product of the coordinates
and hence the parity of the number of minus signs:

| $W(D_4)$-orbit | size | $M_{1111}$ | $M_{1122}$ | $M_{1234}$ | 4th-moment residual |
|---|---:|---:|---:|---:|---:|
| $\mathcal{O}_1 = \{\pm 2 e_i\}$ | 8 | 32 | 0 | 0 | **32** |
| $\mathcal{O}_2 = (\pm1)^4$, even # of $-$ | 8 | 8 | 8 | $+8$ | **16** |
| $\mathcal{O}_3 = (\pm1)^4$, odd # of $-$ | 8 | 8 | 8 | $-8$ | **16** |
| $\mathcal{O}_2\cup\mathcal{O}_3$ (the $W(B_4)$ orbit) | 16 | 16 | 16 | 0 | **32** |
| all three, equal weight | 24 | 48 | 16 | 0 | **0** |
| all three, weights $2\!:\!1\!:\!1$ | 24 | 80 | 16 | 0 | **32** |

Each orbit is separately, and substantially, anisotropic. With weights $(w_1,w_2,w_3)$ the two
independent obstructions are

$$
M_{1234} \;=\; 8\,(w_2 - w_3), \qquad
M_{1111} - 3M_{1122} \;=\; 32w_1 - 16w_2 - 16w_3 ,
$$

and these vanish together **iff $w_1 = w_2 = w_3$**: fourth-order isotropy holds exactly at equal
weight on all three orbits, and nowhere else. (Note that the second obstruction is *not*
proportional to $w_1 - w_2$; it is $32\bigl(w_1 - \tfrac{w_2+w_3}{2}\bigr)$, so the axis orbit is
balanced against the *mean* of the two diagonal orbits.)

The three-orbit form is also where the $S_3$ becomes visible. The generator $T$ of §3 swaps
$\mathcal{O}_1 \leftrightarrow \mathcal{O}_2$ and fixes $\mathcal{O}_3$ pointwise-as-a-set — exactly
what a transposition in $S_3 \cong G/W(D_4)$ should do. It also sharpens the failure mode. A model
builder is far more likely to lose triality by weighting *axes against diagonals* ($w_1 \ne w_2 =
w_3$, a completely natural thing to do if one has not noticed the triality structure, since the two
are geometrically distinguishable: one is "along an axis", the other "along a diagonal") than by
splitting the two diagonal orbits, which are distinguished only by a sign parity that $W(B_4)$
merges and that nobody tracks by accident. Either failure **restores dimension-six anisotropy at
full strength**.

So the protection is a property of the symmetry of the *action*, not of the *lattice geometry* alone.
Putting fields on a $D_4$ lattice is necessary but not sufficient; the couplings must respect
triality. This is the result's own "would change if" clause and it should travel with it.

### 8.3 (P-sc) A scalar kernel

The theorem's quantifier is $K:\mathbb{R}^4\to\mathbb{R}$, and that is not a stylistic choice. A
kernel carrying internal indices — a polarization tensor, a spinor structure, a flavour matrix —
transforms by *equivariance*, $M(Ak) = A\,M(k)\,A^{\mathsf T}$, and the relevant object is then the
space of $G$-equivariant matrix-valued quartics, which is larger than $\mathbb{R}[k]^G_4$ and which
the proof of §5 does not touch.

The gap is not hypothetical. §5's corollary exhibits it explicitly: the simplest fully
$W(F_4)$-symmetric matrix-valued bond coupling has $T_{\mu\nu}(k)k^\mu k^\nu = M_6(k)$, which is not
a multiple of $(k^2)^3$, so the four-derivative tensor is not isotropic, and its transverse
eigenvalues split along a generic direction while remaining degenerate along $e_1$ and
$(1,1,0,0)/\sqrt2$. The two-derivative part is isotropic, so the splitting is a genuine
four-derivative effect and not a leading-order artefact.

This matters for how the result may be quoted. The constraints assembled in §1.1 are bounds on
photons, electrons and protons; Neuberger's title is *Spinless fields on $F_4$ lattices*. None of
those objects is a scalar field. A reader who takes the abstract's quantifier to range over "any
dispersion kernel" will read the theorem as covering exactly the sector it does not. The scalar
restriction therefore travels with the result, on the same footing as (P-an) and (P-pg), and
extending the statement to the equivariant case is open work this note does not do.

### 8.4 (P-op) The operative symmetry

The three premises above are premises on the *theorem*. This one is a premise on the *transfer* —
on the step from "the invariant theory of $G$ forbids an anisotropic quartic" to "a substrate built
on this lattice exhibits no anisotropic dimension-six Lorentz violation". **Nothing in §3–§7 depends
on it.** As mathematics the theorem is a statement about the order-$1152$ group acting on
$\mathbb{R}^4$, and it stands exactly as proved whether or not (P-op) holds; the lattice
mathematics is untouched by this subsection.

The transfer, however, needs the group being used to be the group *operative on the sector the
claim is about*, and §1.1 already supplied the reason to doubt that it is. The theorem's own
symmetry is too large to supply a preferred frame: a kernel invariant under all of $G$ has no
structure on which $\lvert\mathbf k\rvert^4$, or any other frame-dependent object, could be built.
So a substrate that exhibits Lorentz violation at all must obtain its frame from somewhere else —
a driven or dissipative steady state, a condensate, a cosmological rest frame. Whatever does that
singles out an axis, and the symmetry the medium leaves intact is then not $G$ but the stabiliser
of that axis.

Write the axis as $e_4$ and set $G_{48} := \operatorname{Stab}_G(e_4)$. Both facts we need are
immediate from material already in this note.

* **$|G_{48}| = 48$.** By §8.2 the second shell $\{\pm2e_i\}\cup(\pm1,\pm1,\pm1,\pm1)$ is a *single*
  $G$-orbit, of size $24$; $2e_4$ lies in it; so the orbit–stabiliser theorem gives
  $|\operatorname{Stab}_G(2e_4)| = 1152/24 = 48$, and $\operatorname{Stab}_G(e_4)$ is the same
  subgroup. The $48$ signed permutations of the coordinates $k_1,k_2,k_3$ (acting trivially on
  $k_4$) lie in $W(B_4)\subset G$ and fix $e_4$, so they exhaust it.
* **$G_{48}$ restricts faithfully onto $W(B_3)$.** Each such element is block-diagonal; an element
  fixing $e_4$ and acting trivially on $e_4^{\perp}$ is the identity, so the restriction to the
  transverse 3-space is injective, and its image is all $48$ signed permutations of three
  coordinates — the **full octahedral group** $W(B_3)$.

$W(B_3)$ has invariant degrees $\{2,4,6\}$. Because $4$ *is* one of them, the space of degree-4
invariants of the **spatial** variables is **two**-dimensional, spanned by $(\mathbf k^2)^2$ **and**
$\sum_{i\le3}k_i^4$. So the anisotropic spatial quartic that $G$ forbids is *permitted* at
$G_{48}$: the reduction to the stabiliser reinstates precisely the invariant that §7 identified as
the hypercubic lattice's failure mode. Note what this means structurally. The two things the full
point group excludes — a boost-violating isotropic quartic and an anisotropic spatial one — become
available *together*, at the same group, by the same reduction. They are not independent, and a
substrate cannot have the first without exposing itself to the second.

**What carries the protection at the reduced group is then a property of the coupling, not of the
reduced symmetry.** The $24$ bonds form a single $G$-orbit carrying equal weight, and that alone
forces $\sum_v (k\cdot v)^4 = 12\,(k^2)^2$ identically in four variables (§4, contracting the
fourth moment). An identity in four variables restricts to every 3-plane, so the *spatial* fourth
moment of the nearest-neighbour set is exactly isotropic — full tensor, residual $0$ — whatever
axis is singled out. The reduction therefore leaves a **permission that this kernel does not
populate**, not a term that it does.

It is worth recording the axis-specific decomposition of that fact, because it is easy to mistake
for the mechanism. (The moments below are elementary consequences of §4's bond set, obtained by
counting; unlike the rest of the note's numbers they are not separately computed in Appendix A,
because they need no computation.) With $e_4$ singled out, the $24$ bonds split $12+12$: those with a nonzero
$e_4$-component have spatial parts $\pm e_i$ ($i\le3$, four of each) and contribute
$M_{1111}=4$, $M_{1122}=0$, spatial residual $+4$; those lying in the hyperplane $k_4 = 0$ have
spatial parts $(\pm1,\pm1,0)$ and contribute $M_{1111}=8$, $M_{1122}=4$, spatial residual $-4$.
The sums are $M_{1111} = 12$ and $M_{1122}=4$ — §4's isotropic pair — and the protection is the
cancellation of the two halves. But that $\pm4$ split is a **sensitivity decomposition along the
chosen axis, not the source of the isotropy**: at an axis that is not a symmetry direction of the
lattice the $12+12$ split does not exist at all, and the isotropy persists regardless, because it
descends from the full-orbit identity above.

**Would change if.** Any coupling whose bond weights are invariant under the reduced group but are
**not constant on the full $G$-orbit** breaks the cancellation and restores a dimension-six
*spatial* anisotropy — which then faces directional and sidereal bounds rather than the isotropic
ones. The concrete instance is the reweighting the reduced group permits and the full group does
not: weight $w$ on the $12$ in-hyperplane bonds and $1$ on the $12$ others gives spatial
$M_{1111} = 4 + 8w$ and $M_{1122} = 4w$, hence $M_{1111} - 3M_{1122} = 4(1-w)$, zero only at
$w = 1$. This is the same *shape* of failure as (P-pg) — unequal weight on what the full group
makes one orbit — but a weaker and more easily met condition triggers it, because $G_{48}$ no
longer forces the orbit to carry constant weight in the first place.

The honest statement is therefore: *the invariant theory forbids the anisotropic quartic at the
full point group; at the group a frame-selecting medium leaves intact it does not, and what stands
in its place is the requirement that the couplings remain constant on the full-group orbit.*
Whether a given substrate's dressed couplings do is a dynamical question, and this note does not
address it.

### 8.5 What the theorem does **not** do

This subsection is the one that must not be skimmed.

**It does not perform the Euclidean-to-Lorentzian step, and that is the hard part.** The argument
constrains the *tensor structure* of $P_4$, not its magnitude; the isotropic direction $(k^2)^2$ is
available and generically occupied, and §4 exhibits it for the nearest-neighbour $D_4$ kernel with
coefficient $-1/12$, an $O(1)$ number. What the theorem cannot say is whether that surviving term
is a Lorentz violation at all, because the answer depends entirely on a step taken outside it. If
the naive continuation of §7 is granted, $(k\cdot k)^2$ becomes $(p_\mu p^\mu)^2$, a Lorentz
scalar; the pole sits at constant $p_\mu p^\mu$; the dispersion relation is exactly
$E^2 = \mathbf p^2 + m_{\rm phys}^2$; and the $-1/12$ term is a mass renormalisation with
$\eta^{(4)} = 0$. If it is *not* granted, then $\eta^{(4)}$ is not a quantity the theorem's setup
can express, and the bounds of §1.1 are not being spoken to either. Either way **this note supplies
no $\eta^{(4)}$**, and a reader who comes away with the impression that a $D_4$ substrate solves —
or, for that matter, incurs — the Lorentz-violation problem has misread it. The frame-selecting
structure that would decide the question is exactly what §8.4 shows must come from outside the
kernel, and locating it is real work that is not done here.

**Its physical reading is conditional on the operative symmetry.** Premise (P-op) of §8.4 is not a
refinement to be quoted away: at the stabiliser of the axis a frame-selecting medium singles out,
the anisotropic spatial quartic is permitted, and the protection is carried by the coupling's
constancy on the full-group orbit rather than by the reduced symmetry. The mathematics is
unaffected; the physical sentence is conditional.

**It fixes no limiting speed.** Two nearby things are worth separating from that. The theorem
*does* remove anisotropic dimension-four rotation breaking — but so does hypercubic symmetry, and
that observation is not new here; it is the standard argument of the Lorentz-violation literature
credited in §9(iii). It also removes CPT-odd $p^3$ terms and every other odd power at a stroke,
since $-\mathbb{1}\in G$ (the first corollary of §5). What it does **not** fix is the *magnitude*
of the isotropic dimension-four coefficient — the limiting speed $c_2$ in the expansion of §5 —
which is a single free number per field, and species-dependent limiting speeds are precisely the
tightly constrained quantity this note leaves entirely open.

**It fixes no magnitude.** No coefficient is predicted, including the dimension-eight anisotropic
coefficient whose *existence* §6 establishes. Its size depends on the dynamics.

**It is a statement about a symmetry, and symmetry statements have a known loophole.** Collins,
Perez, Sudarsky, Urrutia and Vucetich showed that in an interacting theory regulated by a
Lorentz-violating cutoff, violations generically percolate to low-dimension operators with
unsuppressed coefficients. Our argument is partly robust to this and partly not, and the distinction
matters. It *is* robust for the tensor structure: any counterterm generated by a regulator that
preserves $G$ is itself $G$-invariant, so if it is analytic its quartic part is again isotropic — the
anisotropy protection survives loops. It is *not* a response to the percolation problem itself,
which concerns the magnitudes of the low-dimension coefficients — again, exactly what this note
does not address. And a regulator preserving only the *reduced* group of §8.4 preserves less: the
loop-robustness statement inherits (P-op) along with everything else.

**It does not argue that nature uses this lattice.** The result is conditional: *if* a substrate is
$D_4$-symmetric with triality-symmetric analytic couplings, *then* its leading rotational anisotropy
is dimension eight. Whether any such substrate exists is not addressed.

---

## 9. Relation to prior work

Honest attribution requires separating three literatures.

**(0) Lattice-gas hydrodynamics — the earliest home of the criterion, and it is not lattice field
theory.** The requirement that drives everything below — *find a lattice whose point group makes the
fourth-rank tensor built from its bond vectors isotropic* — was already the organising criterion of
the lattice-gas automaton literature of 1986–87, a year before Neuberger. There, the motivation is
not Lorentz violation but the Navier–Stokes limit: a lattice gas reproduces isotropic hydrodynamics
only if its fourth-rank velocity moment is isotropic, no regular three-dimensional lattice achieves
this, and the standard resolution is to go to four dimensions and project. The lattice that does the
job is the face-centred hypercubic (FCHC) lattice, defined in that literature as the sites of
$\mathbb{Z}^4$ with even coordinate sum — which is *verbatim* the $D_4$ of §2, with the same $24$
nearest neighbours. d'Humières, Lallemand and Frisch, *Lattice gas models for 3D hydrodynamics*,
Europhys. Lett. **2**, 291 (1986) is where the FCHC model is introduced; Frisch, d'Humières,
Hasslacher, Lallemand, Pomeau and Rivet, Complex Systems **1**, 649 (1987) is the systematic
treatment, and Hénon, Complex Systems **1**, 475 (1987) works with the FCHC isometry group directly.
Wolfram, *Cellular automaton fluids 1*, J. Stat. Phys. **45**, 471 (1986) treats the
group-theoretic isotropy conditions for cellular-automaton fluids in the same period.

So the note's earlier statement — that the physical content "dates to Neuberger (1987)" — assigns
the origin a year too late and to the wrong literature. **The physical content of §4–§5, that the
$D_4$/FCHC bond set has an isotropic fourth-rank moment where the hypercubic one does not, belongs
to the 1986 lattice-gas literature.** What Neuberger (1987) contributes, and what remains properly
his, is the *field-theoretic* reading: that this is what removes the dimension-six Lorentz-breaking
operator of the hypercubic regulator.

*Verification status of this paragraph, stated because absence-and-priority claims are only as good
as their sourcing.* The EPL 1986 bibliographic record and abstract were read from the publisher
(DOI 10.1209/0295-5075/2/4/006); the abstract confirms the FCHC-based 4D lattice gas projected to
three dimensions but does **not** itself state the rank-four-isotropy motivation, and the full text
was not obtained. The Complex Systems 1987 and Hénon 1987 papers, and Wolfram 1986, were **not read
in the original** — the scans exceeded the retrieval limits available here. The FCHC $=$ $D_4$
identification and the "no regular 3D lattice suffices, so use 4D and project" criterion are taken
from secondary descriptions of those papers, not from the primaries. Accordingly the paragraph
above should be read as a **priority claim with secondary sourcing**: the direction of the
correction is not in doubt, but a referee-grade version of §9 requires these four items read in the
original, and the specific sentence "introduced FCHC *precisely because* it is the simplest lattice
achieving rank-four isotropy" is **not** yet confirmed against a primary and is not asserted here.

**(i) Lattice field theory — where the field-theoretic reading lives.** The physical content is known and
should be credited there. Celmaster (1982) introduced gauge theories on the four-dimensional
body-centred hypercubic lattice specifically because its point group is three times larger than the
hypercubic one, and pursued the programme through the 1980s with several collaborators. Neuberger
(1987) argued that lattices built on the (co)roots of $F_4$ are "singularly well suited" to
regularising scalar fields, and the motivation given in that line of work is exactly ours: on a
hypercubic lattice there is a Lorentz-breaking dimension-six operator with no counterpart in any
extension of the Standard Model, and on the $F_4$ lattice there is not. The free $F_4$ dispersion
$g(p) = p^2 - \tfrac{1}{12}(p^2)^2 + O(p^6)$ appears in that literature; we reproduce its coefficient
in §4 as a check. Bhanot, Bitar, Heller and Neuberger (1990, 1991) and Klomfass (1993) used $F_4$
lattices for the Higgs triviality bound on precisely these grounds. Most recently Katz and Nogradi
(2025) formulated QCD on the 16-cell honeycomb — the same lattice — and state plainly that "at order
$O(a^2)$ the correction is still Lorentz invariant, the first order where this does not hold is
$O(a^4)$", against cubic lattices where "already at order $O(a^2)$ we encounter Lorentz breaking
terms".

The closest prior work is Chow (1999), who enumerates order by order which derivative operators the
lattice symmetry permits, states as a displayed result that "the checkerboard lattice in four
dimensions $D_4$ is exactly isotropic at order $a^2$. It is the only unexceptional root lattice with
this property", and gives the mechanism: "the $D_4$ lattice has an accidental threefold discrete
symmetry (which is also a symmetry of its Dynkin diagram) which mixes $\mathcal{B}_4$ and
$\mathcal{B}_{22}$. The only combination which is invariant under this threefold symmetry is
$\partial^4$." That is the group-level statement of §5 and the triality mechanism of §8.2, in a
different vocabulary. The two-sided sharpness is likewise on record: Chen, Goldhirsch and Orszag
(2008), working with the same lattice as the 4D FCHC velocity set, describe its fourth-order
isotropy as "well known", compute the anisotropic sixth moment explicitly
($M^{(6)}_{iiiiii} = 12 \neq 15$), and construct higher-order-isotropic velocity sets as *weighted*
unions of exactly the second-shell sub-orbits of §8.2 — so the dependence of isotropy on the
relative weighting of triality-related orbits is also worked out there, from the constructive
direction.

**We therefore do not claim the physical result, the group-level formulation, the triality
mechanism, or the two-sided sharpness as new.** What §5 adds over Chow is generality and rigour: his
counting is set up for one-shell nearest-neighbour Laplacians, whereas the invariant-degree argument
covers every analytic point-group-symmetric kernel at once, with the sharpness quantified (§6) and
the premises isolated (§8). The residual novelty claim of this note is the single narrowed item in
(iii) below.

**(ii) Discrete geometry.** That the $24$-cell is a spherical 5-design is classical
[Delsarte–Goethals–Seidel 1977]; it cannot be a 6-design because a 6-design in $S^3$ requires at
least $30$ points, consistent with the anisotropic sixth moment of §4. Cohn, Conway, Elkies and Kumar
(2007) study the $D_4$ root system's optimality properties and, notably, show it is *not* universally
optimal. The design property is a corollary of the group statement (§5c) rather than the other way
round. The invariant-degree facts are standard reflection-group theory (Chevalley–Shephard–Todd;
Coxeter); $F_4$'s degrees $\{2,6,8,12\}$ and exponents $1,5,7,11$ are textbook.

**(iii) Lorentz-violation phenomenology — where the *move* is standard and the *dimension-six form*
of it appears to be absent.** The EFT framework for modified dispersion relations is that of Myers
and Pospelov (2003); the constraint compilations are Mattingly (2005), Kostelecký and Russell (SME
data tables), and Liberati (2013), from which the numbers in §1.1 are taken. The acknowledged
precursor of this note's argument sits inside two of those references: Mattingly (2005) notes that
"hypercubic symmetry on a lattice is enough to forbid dimension four rotation breaking operators for
scalars" (the only hypercubically-invariant tensor $M^{ab}$ is $\delta^{ab}$), and Jacobson,
Liberati and Mattingly (2006) make the same argument — "a discrete subgroup of the Euclidean
rotation group suffices to protect the operators of dimension four and less" — crediting it to the
lattice field theory literature. So *"take the invariant theory of the substrate's point group and
conclude that a class of Lorentz-violating operators is forbidden"* is a known move in this
literature, executed at degree 2 / dimension four. What our searches did not find — including
full-text searches of the HEP literature and the complete citation graphs of Neuberger (1987) and
Chow (1999), all of whose citers are lattice field theory — is the dimension-six continuation:
that the hypercubic protection *fails* at degree 4 (where $\sum_i k_i^4$ survives), and that the
$D_4$/$F_4$ point group *succeeds* there. That single narrowed item is the gap this note is aimed
at. (Absence claims are only as good as their coverage; the search coverage and its stated
weaknesses are on record. The pre-1991 lattice-gas originals — where Chen–Goldhirsch–Orszag locate
the "well known" degree-4 result — are now identified and credited in §9(0) above, but three of the
four are still **not read in the original**; that paragraph states exactly which, and the absence
claim in this paragraph is correspondingly weaker against the lattice-gas literature than against
the lattice-field-theory one.)

**A different protection mechanism, for contrast.** In the analogue-gravity programme, Volovik and
collaborators derive emergent Lorentz invariance in fermionic condensates from a *topological*
invariant in momentum space at a Fermi point: the gaplessness and the emergent relativistic dispersion
are protected by a nonzero momentum-space topological charge, robust against microscopic details.
That mechanism is genuinely different from the one here — topological rather than group-theoretic,
protecting the existence and form of the low-energy cone rather than the tensor structure of a
specific term in the derivative expansion — and it is subject to its own re-entrant violations at low
energy. A referee will reasonably ask how the two relate; the answer is that they are complementary
and neither implies the other.

Other approaches to the same liability include randomised discretisations, where rotational
invariance is restored on average rather than by a point group [Christ, Friedberg and Lee 1982], and
causal-set sprinklings, where discreteness is arranged to break no direction at all
[Bombelli, Henson and Sorkin 2006]. Both trade the exactness of a lattice for statistical isotropy;
the mechanism here keeps the lattice and buys two orders in $E/\Lambda$.

---

## 10. Summary

* $\operatorname{Aut}(D_4) \cong W(F_4)$ has order $1152$ and invariant degrees $\{2,6,8,12\}$.
* Consequently $\dim\mathbb{R}[k]^G_4 = 1$: the only invariant quartic is $(k^2)^2$. Any analytic,
  point-group-symmetric, **scalar** dispersion kernel therefore has an exactly isotropic quartic
  term. More: since $-\mathbb{1}\in G$ and $\dim\mathbb{R}[k]^G_2 = 1$, the expansion reads
  $K = c_0 + c_2k^2 + c_4(k^2)^2 + P_6(k) + O(k^8)$ — **everything below degree six is
  $O(4)$-invariant**, odd terms included.
* $\dim\mathbb{R}[k]^G_6 = 2$, with an explicit anisotropic invariant $A(k)$ taking both signs on the
  unit sphere, and the sixth bond moment is anisotropic. Dimension eight is therefore *reached*.
* $\mathbb{Z}^4$ fails: $\dim\mathbb{R}[k]^{W(B_4)}_4 = 2$, $\sum_i k_i^4$ survives, and the
  nearest-neighbour dispersion is direction-dependent at quartic order by a factor of $4$. The result
  is an $F_4$ fact, not a four-dimensionality fact.
* Four premises are load-bearing. Three condition the theorem: **(P-an)** analyticity — and the
  loophole is non-empty,
  $k^2 + \epsilon|A(k)|^{2/3}$ being a $G$-invariant kernel with an anisotropic degree-four part,
  though logarithmic non-analyticity is harmless since $f\log k^2$ still forces $f = (k^2)^2$;
  **(P-pg)** the full point group including triality — the second shell carries **three** $W(D_4)$
  orbits of eight (residuals $32,16,16$) and isotropy holds *iff all three weights are equal*, so
  unequal weighting of triality-related orbits restores dimension-six anisotropy at full strength;
  and **(P-sc)** a **scalar** kernel — the theorem does not reach matrix-valued (equivariant)
  kernels, and the simplest $W(F_4)$-symmetric one already splits polarizations
  direction-dependently at four derivatives, while the bounds of §1.1 are for photons, electrons and
  protons, none of them scalars.
* The fourth conditions the *transfer* to Lorentz-violation phenomenology and leaves the lattice
  mathematics untouched: **(P-op)** the operative symmetry is the full point group and not the
  subgroup a frame-selecting medium leaves intact. That subgroup is $\operatorname{Stab}_G(e_4)$,
  of order $48$, restricting faithfully onto the full octahedral group $W(B_3)$ — invariant degrees
  $\{2,4,6\}$ — where the degree-4 *spatial* invariant space is **two**-dimensional and
  $\sum_{i\le3}k_i^4$ is permitted. What protects the nearest-neighbour kernel there is the
  coupling's constancy on the single full-group bond orbit (which forces spatial isotropy on every
  3-plane), not the reduced symmetry; the $\pm4$ split of the $12+12$ bonds about $e_4$ is the
  axis-specific sensitivity decomposition of that protection, not its mechanism. Any weighting that
  is not constant on the orbit restores dimension-six *spatial* anisotropy.
* **The Euclidean-to-Lorentzian step is not performed here, and it is the hard part.** The theorem
  constrains a tensor structure, not a magnitude; the surviving $(k^2)^2$ term is built from the
  four-dimensional square and, under the naive continuation, is a mass renormalisation rather than
  a boost violation, while an isotropic-but-boost-violating quartic has no point-group invariant to
  sit on at all. The preferred frame must come from outside the kernel. Lorentz violation is not
  solved here.

---

## Appendix A — Reproduction script

Standalone; requires only `numpy`. Runtime ≈ 15 s. It rebuilds the point group as a *stabiliser*
(not from a guessed generating set) and computes invariant-space dimensions by Reynolds averaging plus
numerical rank (not by Molien's formula), so that the two independent routes to the invariant degrees
can be compared against each other and against the Poincaré series.

```python
#!/usr/bin/env python3
"""
Reproduction script for "Quartic isotropy of the D4 lattice".
Standalone: requires only numpy.  Runtime: a few seconds.

Checks, in order:
  (1) the 24 nearest-neighbour bonds of D4 and their 2nd/4th/6th moments;
  (2) Aut(D4 root system) built as a *stabilizer* (not from guessed generators), |G| = 1152;
  (3) dim of the degree-d G-invariant polynomials, by Reynolds averaging + numerical rank;
  (4) the free nearest-neighbour dispersion, showing the quartic term is isotropic;
  (5) the Z^4 (hypercubic) contrast;
  (6) premise P-pg: the THREE shell-2 W(D4) orbits cancel only at equal weight on all three;
  (7) Remark (i): G acts on the second shell, and the rescaled union is the 48-root F4 system;
  (8) premise P-sc: the matrix-valued (pseudo-dipolar) kernel is NOT isotropic at 4 derivatives;
  (9) premise P-an: |A(k)|^{2/3} is a non-analytic G-invariant anisotropic quartic.
"""
import itertools
import numpy as np

ok = lambda b: "OK " if b else "FAIL"
fails = []
def check(name, cond, detail=""):
    fails.append(name) if not cond else None
    print(f"  [{ok(cond)}] {name}{('  ' + detail) if detail else ''}")

# ---------------------------------------------------------------- (1) bonds and moments
def d4_bonds():
    out = []
    for i, j in itertools.combinations(range(4), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0, 0, 0, 0]; v[i] = si; v[j] = sj
                out.append(tuple(v))
    return sorted(set(out))

def z4_bonds():
    return sorted({tuple(s if k == i else 0 for k in range(4))
                   for i in range(4) for s in (1, -1)})

def mom(vs, idx, w=None):
    w = [1] * len(vs) if w is None else w
    t = 0
    for wi, v in zip(w, vs):
        p = 1
        for a in idx:
            p *= v[a]
        t += wi * p
    return t

d = lambda p, q: 1 if p == q else 0
def resid4(vs, w=None):
    A = mom(vs, (0, 0, 1, 1), w)
    return max(abs(mom(vs, ix, w) - A * (d(ix[0],ix[1])*d(ix[2],ix[3])
                                       + d(ix[0],ix[2])*d(ix[1],ix[3])
                                       + d(ix[0],ix[3])*d(ix[1],ix[2])))
               for ix in itertools.product(range(4), repeat=4)), A

R, Z = d4_bonds(), z4_bonds()
print("\n(1) bond sets and moments")
check("D4 has 24 nearest-neighbour bonds, all of squared length 2",
      len(R) == 24 and {sum(x*x for x in v) for v in R} == {2}, f"|bonds|={len(R)}")
check("D4 second moment = 12 delta_ij",
      all(mom(R,(a,b)) == 12*d(a,b) for a in range(4) for b in range(4)))
r4, A4 = resid4(R)
check("D4 fourth moment exactly isotropic: M_1111 = 12 = 3 M_1122, residual 0",
      r4 == 0 and mom(R,(0,0,0,0)) == 12 == 3*A4,
      f"M_1111={mom(R,(0,0,0,0))}, M_1122={A4}, residual={r4}")
m6_111111, m6_112233 = mom(R,(0,)*6), mom(R,(0,0,1,1,2,2))
check("D4 sixth moment NOT isotropic (M_112233 = 0 but M_111111 = 12 != 0)",
      m6_112233 == 0 and m6_111111 == 12,
      f"M_111111={m6_111111}, M_112233={m6_112233}, residual={abs(m6_111111 - 15*m6_112233)}")

# ---------------------------------------------------------------- (2) the point group
def aut_root_system(roots):
    """All A in O(4) with A(roots) = roots. Determined by the image of a basis of roots;
    enumerated with Gram-matrix pruning. No generating set is assumed."""
    Rs = set(roots); arr = np.array(sorted(Rs), dtype=float)
    basis = []
    for v in sorted(Rs):
        if np.linalg.matrix_rank(np.array(basis + [v], dtype=float)) == len(basis) + 1:
            basis.append(v)
        if len(basis) == 4:
            break
    B = np.array(basis, dtype=float).T
    Binv, gram = np.linalg.inv(B), B.T @ B
    rl = sorted(Rs)
    out = {}
    def rec(k, chosen):
        if k == 4:
            A = np.array(chosen, dtype=float).T @ Binv
            img = arr @ A.T
            if np.allclose(img, np.rint(img)) and all(tuple(int(x) for x in q) in Rs
                                                      for q in np.rint(img)):
                # normalise -0.0 -> 0.0 BEFORE hashing: raw float bytes distinguish the two
                # signed zeros, which would double-count an element and inflate |G|.  It does
                # not bite for this group, but the whole point of this routine is that the
                # group is computed rather than assumed, so the hash must not be fragile.
                A = np.round(A, 9)
                A = np.where(np.abs(A) < 1e-12, 0.0, A)
                out[A.tobytes()] = A
            return
        for w in rl:                      # prune on partial Gram matrix
            if all(abs(sum(a*b for a, b in zip(w, chosen[m])) - gram[k][m]) < 1e-9
                   for m in range(k)) and abs(sum(x*x for x in w) - gram[k][k]) < 1e-9:
                rec(k + 1, chosen + [w])
    rec(0, [])
    return list(out.values())

print("\n(2) the point group")
G  = aut_root_system(R)
GZ = aut_root_system(Z)
check("|Aut(D4 root system)| = 1152 = |W(F4)|", len(G) == 1152, f"got {len(G)}")
check("every element is orthogonal", all(np.allclose(A.T @ A, np.eye(4)) for A in G))
check("|Aut(Z^4 bond set)| = |W(B4)| = 384", len(GZ) == 384, f"got {len(GZ)}")

def signed_perms(even_only):
    out = []
    for p in itertools.permutations(range(4)):
        for s in itertools.product((1, -1), repeat=4):
            if even_only and np.prod(s) != 1:
                continue
            A = np.zeros((4, 4))
            for i, pi in enumerate(p):
                A[i, pi] = s[i]
            out.append(A)
    return out
WD4, WB4 = signed_perms(True), signed_perms(False)
check("W(D4) (even signed permutations) has order 192", len(WD4) == 192)
check("W(B4) sits inside Aut(D4) with index 3", len(G) // len(WB4) == 3)

# ---------------------------------------------------------------- (3) invariant dimensions
def inv_dim(Gp, deg, npts=400, seed=7):
    """dim of the space of degree-`deg` Gp-invariant polynomials in 4 variables.
    Reynolds-average every monomial, evaluate on generic points, take the rank."""
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(npts, 4))
    Y = np.einsum('gij,tj->gti', np.array(Gp), X)
    rows = []
    for e in (e for e in itertools.product(range(deg+1), repeat=4) if sum(e) == deg):
        val = np.ones((len(Gp), npts))
        for k, ek in enumerate(e):
            if ek:
                val = val * Y[:, :, k] ** ek
        rows.append(val.mean(axis=0))
    s = np.linalg.svd(np.array(rows), compute_uv=False)
    return int((s > max(len(rows), npts) * s[0] * 1e-9).sum())

def poincare(degs, dmax):
    c = [0]*(dmax+1); c[0] = 1
    for g in degs:
        for n in range(g, dmax+1):
            c[n] += c[n-g]
    return c

print("\n(3) dimensions of the invariant polynomial spaces (Reynolds + rank)")
for nm, Gp, degs in (("Aut(D4) = W(F4)", G,   [2, 6, 8, 12]),
                     ("W(D4)",           WD4, [2, 4, 4, 6]),
                     ("W(B4)= Aut(Z^4)", WB4, [2, 4, 6, 8])):
    got  = [inv_dim(Gp, n) for n in (2, 4, 6, 8)]
    want = [poincare(degs, 8)[n] for n in (2, 4, 6, 8)]
    check(f"{nm:16s} deg 2,4,6,8 dims = {got}  (Poincare series of degrees {degs}: {want})",
          got == want)
check("THE THEOREM: degree-4 invariant space of the order-1152 group is 1-dimensional",
      inv_dim(G, 4) == 1)
check("SHARPNESS: degree-6 invariant space is 2-dimensional (an anisotropic sextic exists)",
      inv_dim(G, 6) == 2)
check("CONTRAST: degree-4 invariant space of W(B4) is 2-dimensional (sum k_i^4 survives)",
      inv_dim(WB4, 4) == 2)
check("PREMISE P-pg: degree-4 invariant space of W(D4) alone is 3-dimensional",
      inv_dim(WD4, 4) == 3)

# ---------------------------------------------------------------- (4)(5) dispersion
print("\n(4)/(5) free nearest-neighbour dispersion, D4 vs Z^4")
Rm, Zm = np.array(R, float), np.array(Z, float)
# 2*sin(x/2)^2 instead of 1-cos(x): algebraically identical, but 1-cos loses ~3 significant
# digits to cancellation at the x ~ 1e-2 sample points used below, which is the same order as
# the tolerance in quartic_coeff.  This is free and removes the margin question entirely.
_1mcos = lambda x: 2.0 * np.sin(x / 2.0) ** 2
gD4 = lambda k: np.sum(_1mcos(Rm @ k)) / 6.0
gZ4 = lambda k: np.sum(_1mcos(Zm @ k))
def quartic_coeff(g, u):
    ts = np.array([1e-2, 2e-2, 3e-2])
    A  = np.vstack([ts**2, ts**4, ts**6]).T
    return np.linalg.lstsq(A, np.array([g(t*u) for t in ts]), rcond=None)[0][1]
rng = np.random.default_rng(11)
dirs = [u/np.linalg.norm(u) for u in rng.normal(size=(6, 4))]
cD = [quartic_coeff(gD4, u) for u in dirs]
check("D4: quartic coefficient is direction-INDEPENDENT and equals -1/12",
      all(abs(c + 1/12) < 1e-6 for c in cD),
      f"min={min(cD):.8f} max={max(cD):.8f}, -1/12={-1/12:.8f}")
cZ = [quartic_coeff(gZ4, u) for u in dirs]
predZ = [-(1/12)*np.sum(u**4) for u in dirs]
check("Z^4: quartic coefficient is direction-DEPENDENT, = -(1/12) sum u_i^4",
      all(abs(a-b) < 1e-6 for a, b in zip(cZ, predZ)),
      f"axis {-(1/12):.6f} vs diagonal {-(1/12)/4:.6f}  (ratio 4)")
rz, Az = resid4(Z)
check("Z^4 fourth bond moment anisotropic: N_1111 = 2, N_1122 = 0, residual 2",
      rz == 2 and mom(Z,(0,0,0,0)) == 2 and Az == 0)
# the explicit sextic
M6 = lambda k: float(np.sum((Rm @ k) ** 6))
M6f = lambda k: -48*np.sum(k**6) + 60*(k@k)*np.sum(k**4)
kk = [rng.normal(size=4) for _ in range(5)]
check("explicit sixth moment M6(k) = 60 k^2 sum k_i^4 - 48 sum k_i^6",
      all(np.isclose(M6(k), M6f(k)) for k in kk))
T = 0.5*np.array([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]], float)
check("M6 is invariant under the triality generator T, while sum k_i^4 is not",
      all(np.isclose(M6(k), M6(T@k)) for k in kk)
      and not all(np.isclose(np.sum(k**4), np.sum((T@k)**4)) for k in kk))
aniso = lambda k: M6f(k)/12.0 - 1.25*(k@k)**3      # J(k) - (5/4)(k^2)^3, J = 5k^2 S4 - 4 S6
check("the anisotropic sextic A(k) = 5k^2 sum k_i^4 - 4 sum k_i^6 - (5/4)(k^2)^3 is nonzero"
      " and G-invariant under ALL 1152 elements",
      any(abs(aniso(k)) > 1e-9 for k in kk) and all(np.isclose(aniso(k), aniso(A@k))
                                                     for k in kk for A in G))
# NB: the axis e1 and the body diagonal (1,1,1,1)/2 are related BY TRIALITY, so A must agree on
# them.  Inequivalent unit directions are the short-root direction e1 and the long-root direction
# (1,1,0,0)/sqrt(2).
sh, lg, dg = np.array([1.,0,0,0]), np.array([1.,1,0,0])/np.sqrt(2), np.ones(4)/2.0
check("A(k) is constant on a triality orbit: A(e1) = A((1,1,1,1)/2)",
      np.isclose(aniso(sh), aniso(dg)), f"A={aniso(sh):.6f}")
check("A(k) separates the short-root from the long-root direction (so it really is anisotropic)",
      not np.isclose(aniso(sh), aniso(lg)),
      f"A(e1)={aniso(sh):.6f}  vs  A((1,1,0,0)/sqrt2)={aniso(lg):.6f}")

# ---------------------------------------------------------------- (6) premise P-pg
print("\n(6) premise P-pg: the shell-2 orbits (THREE under W(D4), two under W(B4))")
shell2 = ([tuple(s if k == i else 0 for k in range(4)) for i in range(4) for s in (2, -2)]
          + [t for t in itertools.product((1, -1), repeat=4)])

def orbits(Gp, pts):
    pts = [tuple(p) for p in pts]; rem, orbs = set(pts), []
    while rem:
        v = next(iter(rem))
        o = {tuple(int(round(x)) for x in (A @ np.array(v, float))) for A in Gp}
        assert o <= set(pts), "an orbit left the shell — the group does not act on it"
        orbs.append(sorted(o)); rem -= o
    return orbs

oD, oB4, oG = orbits(WD4, shell2), orbits(WB4, shell2), orbits(G, shell2)
check("shell 2 is ONE orbit under G, TWO under W(B4) (8+16), THREE of 8 under W(D4)",
      sorted(len(o) for o in oG) == [24] and sorted(len(o) for o in oB4) == [8, 16]
      and sorted(len(o) for o in oD) == [8, 8, 8],
      f"G:{sorted(len(o) for o in oG)}  B4:{sorted(len(o) for o in oB4)}  "
      f"D4:{sorted(len(o) for o in oD)}")
# label the three W(D4) orbits: axis / even-parity diagonal / odd-parity diagonal
def lab(o):
    v = o[0]
    if max(abs(x) for x in v) == 2: return "axis"
    return "diag+" if np.prod(v) > 0 else "diag-"
byname = {lab(o): o for o in oD}
rows = {n: (mom(o, (0,)*4), mom(o, (0, 0, 1, 1)), mom(o, (0, 1, 2, 3)), resid4(o)[0])
        for n, o in byname.items()}
check("W(D4) orbit moments: axis (32,0,0,res 32); diag+ (8,8,+8,res 16); diag- (8,8,-8,res 16)",
      rows["axis"] == (32, 0, 0, 32) and rows["diag+"] == (8, 8, 8, 16)
      and rows["diag-"] == (8, 8, -8, 16), f"{rows}")
check("the two DIAGONAL orbits are separately anisotropic but W(B4) merges them into residual 32",
      resid4(byname["diag+"] + byname["diag-"])[0] == 32)
rEq, AEq = resid4(byname["axis"] + byname["diag+"] + byname["diag-"])
check("they cancel EXACTLY at equal weight on all three", rEq == 0,
      f"combined residual={rEq}, A={AEq}")
w21 = [2]*8 + [1]*8 + [1]*8
allv = byname["axis"] + byname["diag+"] + byname["diag-"]
rUn = resid4(allv, w=w21)[0]
check("weights 2:1:1 (axis vs diagonals) RESTORE quartic anisotropy: M_1111=80, M_1122=16, res 32",
      rUn == 32 and mom(allv, (0,)*4, w21) == 80 and mom(allv, (0, 0, 1, 1), w21) == 16,
      f"residual={rUn}")
# the two obstructions, and the iff
def obstr(w1, w2, w3):
    w = [w1]*8 + [w2]*8 + [w3]*8
    return (mom(allv, (0, 1, 2, 3), w), mom(allv, (0,)*4, w) - 3*mom(allv, (0, 0, 1, 1), w))
check("M_1234 = 8(w2-w3) and M_1111-3M_1122 = 32w1-16w2-16w3 (NOT 32(w1-w2))",
      all(obstr(a, b, c) == (8*(b-c), 32*a-16*b-16*c)
          for a, b, c in itertools.product(range(-2, 3), repeat=3)))
check("=> fourth-order isotropy holds IFF all three weights are equal",
      all((obstr(a, b, c) == (0, 0)) == (a == b == c)
          for a, b, c in itertools.product(range(-2, 3), repeat=3)))
# triality: T swaps the axis orbit with one diagonal orbit and fixes the other
def which(v):
    for n, o in byname.items():
        if tuple(int(round(x)) for x in v) in [tuple(y) for y in o]: return n
    return "?"
Tact = {n: {which(T @ np.array(v, float)) for v in o} for n, o in byname.items()}
check("T acts on the three orbits as a TRANSPOSITION (swaps axis<->diag+, fixes diag-)",
      Tact == {"axis": {"diag+"}, "diag+": {"axis"}, "diag-": {"diag-"}}, f"{Tact}")

# ---------------------------------------------------------------- (7) Remark (i): the F4 system
print("\n(7) Remark (i): G acts on shell 2, and shell1 + shell2/2 is the 48-root F4 system")
S2 = np.array(shell2, float)
inset = lambda v, S: bool(np.any(np.all(np.abs(S - v) < 1e-9, axis=1)))
check("G genuinely acts on the second shell (all 1152 x 24 images land back in it)",
      all(inset(A @ v, S2) for A in G for v in S2))
F4 = np.array(sorted({tuple(np.round(x, 9) + 0.0) for x in
                      list(Rm) + list(S2 / 2.0)}), float)
check("|F4 root set| = 48, with squared lengths {1, 2} (24 short + 24 long)",
      len(F4) == 48 and sorted({round(float(v @ v), 6) for v in F4}) == [1.0, 2.0],
      f"|F4|={len(F4)}")
check("G preserves the 48-root set", all(inset(A @ v, F4) for A in G for v in F4))
check("it IS a root system: closed under its own reflections, and <b,a^v> in Z",
      all(inset(b - 2*(a @ b)/(a @ a)*a, F4) for a in F4 for b in F4)
      and all(abs(2*(a @ b)/(a @ a) - round(2*(a @ b)/(a @ a))) < 1e-9
              for a in F4 for b in F4))
check("|Aut(F4 root system)| = 1152 = |G| (rebuilt independently as a stabiliser)",
      len(aut_root_system([tuple(int(round(x)) for x in v) for v in 2*F4])) == 1152)

# ---------------------------------------------------------------- (8) premise P-sc
print("\n(8) premise P-sc: the theorem does NOT cover matrix-valued kernels")
Tmn = lambda k, p: np.einsum('va,vb,v->ab', Rm, Rm, (Rm @ k) ** p)
kk2 = [rng.normal(size=4) for _ in range(5)]
check("T_ab(k) k^a k^b = M6(k) for the four-derivative pseudo-dipolar tensor",
      all(np.isclose(k @ Tmn(k, 4) @ k, M6(k)) for k in kk2))
check("M6(k) is NOT a multiple of (k^2)^3, so T_ab is NOT an isotropic tensor",
      len({round(M6(k)/(k @ k)**3, 6) for k in kk2}) > 1)
def iso_resid(p, k):
    Tt = Tmn(k, p)
    a, b = np.linalg.lstsq(np.vstack([np.eye(4).ravel()*(k @ k),
                                      np.outer(k, k).ravel()]).T, Tt.ravel(), rcond=None)[0]
    return np.max(np.abs(Tt - (a*(k @ k)*np.eye(4) + b*np.outer(k, k))))/np.max(np.abs(Tt))
check("the TWO-derivative part IS isotropic (residual ~ 0) — the splitting is genuinely quartic",
      max(iso_resid(2, k) for k in kk2) < 1e-12,
      f"2-deriv {max(iso_resid(2,k) for k in kk2):.2e}  "
      f"vs 4-deriv {max(iso_resid(4,k) for k in kk2):.3f}")
def transverse(k):
    k = k/np.linalg.norm(k)
    _, V = np.linalg.eigh(np.eye(4) - np.outer(k, k))
    return np.linalg.eigvalsh(V[:, 1:].T @ Tmn(k, 4) @ V[:, 1:])
ug = rng.normal(size=4); ug /= np.linalg.norm(ug)
check("transverse eigenvalues of the 4-derivative tensor SPLIT along a generic direction",
      np.ptp(transverse(ug)) > 1e-6 and np.ptp(transverse(sh)) < 1e-9,
      f"generic {np.round(transverse(ug),3)}  e1 {np.round(transverse(sh),3)}  "
      f"(1,1,0,0)/r2 {np.round(transverse(lg),3)}")

# ---------------------------------------------------------------- (9) premise P-an
print("\n(9) premise P-an: an explicit non-analytic G-invariant anisotropic quartic")
cex = lambda k: abs(aniso(np.asarray(k, float))) ** (2.0/3.0)
check("|A(k)|^{2/3} is G-invariant under all 1152 elements",
      all(np.isclose(cex(A @ k), cex(k)) for k in kk2 for A in G))
check("|A(k)|^{2/3} is homogeneous of degree 4",
      all(np.isclose(cex(2.7*k), 2.7**4 * cex(k)) for k in kk2))
check("|A(k)|^{2/3} is NOT a multiple of (k^2)^2 (so the quartic part is anisotropic)",
      len({round(cex(k)/(k @ k)**2, 9) for k in kk2}) > 1)
arc = lambda t: np.array([np.cos(t), np.sin(t), 0.0, 0.0])
check("A vanishes on a nontrivial cone (A(arc(pi/8)) = 0), so |A|^{2/3} is non-analytic there",
      abs(aniso(arc(np.pi/8))) < 1e-12 and aniso(arc(0.0))*aniso(arc(np.pi/4)) < 0,
      f"A(e1)={aniso(arc(0.0)):.3f}, A(pi/8)={aniso(arc(np.pi/8)):.1e}, "
      f"A(pi/4)={aniso(arc(np.pi/4)):.3f}")

print("\n" + ("ALL CHECKS PASSED" if not fails else f"FAILURES: {fails}"))
```

### Expected output

```
(1) bond sets and moments
  [OK ] D4 has 24 nearest-neighbour bonds, all of squared length 2  |bonds|=24
  [OK ] D4 second moment = 12 delta_ij
  [OK ] D4 fourth moment exactly isotropic: M_1111 = 12 = 3 M_1122, residual 0  M_1111=12, M_1122=4, residual=0
  [OK ] D4 sixth moment NOT isotropic (M_112233 = 0 but M_111111 = 12 != 0)  M_111111=12, M_112233=0, residual=12

(2) the point group
  [OK ] |Aut(D4 root system)| = 1152 = |W(F4)|  got 1152
  [OK ] every element is orthogonal
  [OK ] |Aut(Z^4 bond set)| = |W(B4)| = 384  got 384
  [OK ] W(D4) (even signed permutations) has order 192
  [OK ] W(B4) sits inside Aut(D4) with index 3

(3) dimensions of the invariant polynomial spaces (Reynolds + rank)
  [OK ] Aut(D4) = W(F4)  deg 2,4,6,8 dims = [1, 1, 2, 3]  (Poincare series of degrees [2, 6, 8, 12]: [1, 1, 2, 3])
  [OK ] W(D4)            deg 2,4,6,8 dims = [1, 3, 4, 7]  (Poincare series of degrees [2, 4, 4, 6]: [1, 3, 4, 7])
  [OK ] W(B4)= Aut(Z^4)  deg 2,4,6,8 dims = [1, 2, 3, 5]  (Poincare series of degrees [2, 4, 6, 8]: [1, 2, 3, 5])
  [OK ] THE THEOREM: degree-4 invariant space of the order-1152 group is 1-dimensional
  [OK ] SHARPNESS: degree-6 invariant space is 2-dimensional (an anisotropic sextic exists)
  [OK ] CONTRAST: degree-4 invariant space of W(B4) is 2-dimensional (sum k_i^4 survives)
  [OK ] PREMISE P-pg: degree-4 invariant space of W(D4) alone is 3-dimensional

(4)/(5) free nearest-neighbour dispersion, D4 vs Z^4
  [OK ] D4: quartic coefficient is direction-INDEPENDENT and equals -1/12  min=-0.08333333 max=-0.08333333, -1/12=-0.08333333
  [OK ] Z^4: quartic coefficient is direction-DEPENDENT, = -(1/12) sum u_i^4  axis -0.083333 vs diagonal -0.020833  (ratio 4)
  [OK ] Z^4 fourth bond moment anisotropic: N_1111 = 2, N_1122 = 0, residual 2
  [OK ] explicit sixth moment M6(k) = 60 k^2 sum k_i^4 - 48 sum k_i^6
  [OK ] M6 is invariant under the triality generator T, while sum k_i^4 is not
  [OK ] the anisotropic sextic A(k) = 5k^2 sum k_i^4 - 4 sum k_i^6 - (5/4)(k^2)^3 is nonzero and G-invariant under ALL 1152 elements
  [OK ] A(k) is constant on a triality orbit: A(e1) = A((1,1,1,1)/2)  A=-0.250000
  [OK ] A(k) separates the short-root from the long-root direction (so it really is anisotropic)  A(e1)=-0.250000  vs  A((1,1,0,0)/sqrt2)=0.250000

(6) premise P-pg: the shell-2 orbits (THREE under W(D4), two under W(B4))
  [OK ] shell 2 is ONE orbit under G, TWO under W(B4) (8+16), THREE of 8 under W(D4)  G:[24]  B4:[8, 16]  D4:[8, 8, 8]
  [OK ] W(D4) orbit moments: axis (32,0,0,res 32); diag+ (8,8,+8,res 16); diag- (8,8,-8,res 16)  {'diag-': (8, 8, -8, 16), 'diag+': (8, 8, 8, 16), 'axis': (32, 0, 0, 32)}
  [OK ] the two DIAGONAL orbits are separately anisotropic but W(B4) merges them into residual 32
  [OK ] they cancel EXACTLY at equal weight on all three  combined residual=0, A=16
  [OK ] weights 2:1:1 (axis vs diagonals) RESTORE quartic anisotropy: M_1111=80, M_1122=16, res 32  residual=32
  [OK ] M_1234 = 8(w2-w3) and M_1111-3M_1122 = 32w1-16w2-16w3 (NOT 32(w1-w2))
  [OK ] => fourth-order isotropy holds IFF all three weights are equal
  [OK ] T acts on the three orbits as a TRANSPOSITION (swaps axis<->diag+, fixes diag-)  {'diag-': {'diag-'}, 'diag+': {'axis'}, 'axis': {'diag+'}}

(7) Remark (i): G acts on shell 2, and shell1 + shell2/2 is the 48-root F4 system
  [OK ] G genuinely acts on the second shell (all 1152 x 24 images land back in it)
  [OK ] |F4 root set| = 48, with squared lengths {1, 2} (24 short + 24 long)  |F4|=48
  [OK ] G preserves the 48-root set
  [OK ] it IS a root system: closed under its own reflections, and <b,a^v> in Z
  [OK ] |Aut(F4 root system)| = 1152 = |G| (rebuilt independently as a stabiliser)

(8) premise P-sc: the theorem does NOT cover matrix-valued kernels
  [OK ] T_ab(k) k^a k^b = M6(k) for the four-derivative pseudo-dipolar tensor
  [OK ] M6(k) is NOT a multiple of (k^2)^3, so T_ab is NOT an isotropic tensor
  [OK ] the TWO-derivative part IS isotropic (residual ~ 0) — the splitting is genuinely quartic  2-deriv 4.28e-16  vs 4-deriv 0.099
  [OK ] transverse eigenvalues of the 4-derivative tensor SPLIT along a generic direction  generic [1.844 2.375 4.044]  e1 [4. 4. 4.]  (1,1,0,0)/r2 [2. 2. 2.]

(9) premise P-an: an explicit non-analytic G-invariant anisotropic quartic
  [OK ] |A(k)|^{2/3} is G-invariant under all 1152 elements
  [OK ] |A(k)|^{2/3} is homogeneous of degree 4
  [OK ] |A(k)|^{2/3} is NOT a multiple of (k^2)^2 (so the quartic part is anisotropic)
  [OK ] A vanishes on a nontrivial cone (A(arc(pi/8)) = 0), so |A|^{2/3} is non-analytic there  A(e1)=-0.250, A(pi/8)=0.0e+00, A(pi/4)=0.250

ALL CHECKS PASSED
```

---

## Appendix B — Numerical summary

| quantity | value | status |
|---|---|---|
| $D_4$ nearest-neighbour bonds | $24$, all $\lvert v\rvert^2 = 2$ | computed |
| second moment | $12\,\delta_{ij}$ | computed |
| fourth moment | $M_{1111}=12$, $M_{1122}=4$, residual $0$ | computed |
| sixth moment | $M_{111111}=12$, $M_{112233}=0$ (anisotropic) | computed |
| $\lvert\operatorname{Aut}(D_4)\rvert$ | $1152 = \lvert W(F_4)\rvert$ | computed as a stabiliser |
| $W(F_4)$ invariant degrees | $\{2,6,8,12\}$ | standard; confirmed via Poincaré series vs. Reynolds rank |
| $\dim$ deg-4 invariants, $G$ | $\mathbf{1}$ | computed (Reynolds + rank) |
| $\dim$ deg-6 invariants, $G$ | $2$ | computed |
| $\dim$ deg-4 invariants, $W(B_4)$ | $2$ | computed |
| $\dim$ deg-4 invariants, $W(D_4)$ | $3$ | computed |
| $D_4$ free dispersion quartic coefficient | $-1/12$, direction-independent | computed; matches published $F_4$ value |
| $\mathbb{Z}^4$ bond moments | $N_{1111}=2$, $N_{1122}=0$, residual $2$ | computed |
| $\mathbb{Z}^4$ quartic anisotropy | axis:diagonal $=4$ | computed |
| shell-2 orbit structure | $1$ orbit under $G$; $2$ under $W(B_4)$ ($8+16$); **$3$ of $8$** under $W(D_4)$ | computed |
| shell-2 $W(D_4)$-orbit residuals | axis $32$; the two diagonal parity orbits $16$ each; $0$ combined at equal weight; $32$ at weights $2\!:\!1\!:\!1$ | computed |
| shell-2 isotropy condition | $M_{1234}=8(w_2-w_3)$, $M_{1111}-3M_{1122}=32w_1-16w_2-16w_3$; isotropic iff $w_1=w_2=w_3$ | computed |
| $F_4$ root system (Remark (i)) | shell 1 $\cup$ (shell 2)/2 $=$ $48$ roots, lengths$^2$ $\{1,2\}$, reflection-closed, integral; $\lvert\operatorname{Aut}\rvert=1152$ | computed |
| (P-sc) matrix-valued kernel | $T_{\mu\nu}k^\mu k^\nu = M_6(k) \not\propto (k^2)^3$; 2-derivative part isotropic to $4\times10^{-16}$, 4-derivative part not; transverse eigenvalues split generically | computed |
| (P-an) counterexample | $\lvert A(k)\rvert^{2/3}$: $G$-invariant, degree-4 homogeneous, $\not\propto (k^2)^2$, vanishes at $\pi/8$ on the $e_1\!\to\!(1,1,0,0)/\sqrt2$ arc | computed |
| photon $\xi^{(4)}$ bound | $-10^{-7} \lesssim \xi^{(4)} \lesssim 10^{-8}$ | quoted, Liberati (2013) eq. 75 |
| electron $\eta^{(4)}$ bound | $-10^{-7} \lesssim \eta^{(4)} \lesssim 10^{-6}$ | quoted, Liberati (2013) eq. 75 |
| proton $\eta^{(4)}_p$ bound | $-10^{-3} \lesssim \eta^{(4)}_p \lesssim 10^{-6}$ (99% CL) | quoted, Liberati (2013) eq. 76 |

---

## References

All entries below were checked against arXiv, Crossref or the publisher record. Items marked
*(unverified)* were not confirmed against a primary source and should be checked before submission.

**Lattice-gas hydrodynamics — the FCHC ($=D_4$) lattice and the rank-four isotropy criterion**

0a. D. d'Humières, P. Lallemand and U. Frisch, *Lattice gas models for 3D hydrodynamics*,
    Europhys. Lett. **2** (4), 291 (1986). DOI: 10.1209/0295-5075/2/4/006. *(Publisher record and
    abstract read directly; the abstract confirms the 4D face-centred-hypercubic lattice gas and its
    3D projection but does **not** state the rank-four-isotropy motivation. Full text not obtained —
    the motivation clause is therefore **not** asserted in §9(0).)*

0b. U. Frisch, D. d'Humières, B. Hasslacher, P. Lallemand, Y. Pomeau and J.-P. Rivet, *Lattice gas
    hydrodynamics in two and three dimensions*, Complex Systems **1**, 649–707 (1987). *(NOT READ IN
    THE ORIGINAL — the archival scan exceeded the retrieval limits available here. Cited on
    secondary description only.)*

0c. M. Hénon, *Isometric collision rules for the four-dimensional FCHC lattice gas*, Complex Systems
    **1**, 475–494 (1987). *(NOT READ IN THE ORIGINAL; same reason. This is the standard source for
    the FCHC isometry group, and for the definition of FCHC as the sites of $\mathbb{Z}^4$ with even
    coordinate sum — i.e. for the FCHC $=D_4$ identification used in §9(0).)*

0d. S. Wolfram, *Cellular automaton fluids 1: Basic theory*, J. Stat. Phys. **45**, 471–526 (1986).
    *(NOT READ IN THE ORIGINAL. Cited for the group-theoretic treatment of lattice isotropy
    conditions in the same period.)*

**Lattice field theory on non-hypercubic lattices**

1. W. Celmaster, *Gauge theories on the body-centered hypercubic lattice*, Phys. Rev. D **26**, 2955
   (1982). DOI: 10.1103/PhysRevD.26.2955.
2. W. Celmaster and F. Krausz, Phys. Rev. D **28**, 1527 (1983). *(bibliographic data taken from the
   reference list of ref. 6; not independently verified)*
3. W. Celmaster and K. J. M. Moriarty, *SU(2) quark potential on a body-centered-hypercubic lattice*,
   Phys. Rev. D **33**, 3718 (1986).
4. H. Neuberger, *Spinless fields on $F_4$ lattices*, Phys. Lett. B **199**, 536–540 (1987).
   DOI: 10.1016/0370-2693(87)91623-6.
5. G. Bhanot, K. Bitar, U. M. Heller and H. Neuberger, Nucl. Phys. B **343**, 467–506 (1990); Nucl.
   Phys. B **353**, 551–564 (1991) [erratum Nucl. Phys. B **375**, 503 (1992)]. *(bibliographic data
   taken from the reference list of ref. 6; not independently verified)*
6. S. D. Katz and D. Nogradi, *QCD on the 16-cell honeycomb*, arXiv:2512.10604 [hep-lat] (2025).
7. M. Klomfass, *Semi-analytical solution of the $\varphi^4$ theory on an $F_4$ lattice*,
   Nucl. Phys. B **412**, 621–656 (1994); arXiv:hep-lat/9307013.
8. C.-K. Chow, *Discretization errors and rotational symmetry: The Laplacian operator on
   nonhypercubical lattices*, Nucl. Phys. B **547**, 281–302 (1999);
   DOI: 10.1016/S0550-3213(99)00109-1; arXiv:hep-lat/9810051. *(quotations in §9(i) read directly
   from the author's LaTeX source.)*
9. H. Chen, I. Goldhirsch and S. A. Orszag, *Discrete rotational symmetry, moment isotropy, and
   higher order lattice Boltzmann models*, J. Sci. Comput. **34**, 87–112 (2008);
   DOI: 10.1007/s10915-007-9159-3; arXiv:0709.1464.

**Lorentz-violation effective field theory and constraints**

10. R. C. Myers and M. Pospelov, *Ultraviolet modifications of dispersion relations in effective field
    theory*, Phys. Rev. Lett. **90**, 211601 (2003); arXiv:hep-ph/0301124.
11. D. Mattingly, *Modern tests of Lorentz invariance*, Living Rev. Rel. **8**, 5 (2005);
    arXiv:gr-qc/0502097.
12. T. Jacobson, S. Liberati and D. Mattingly, *Lorentz violation at high energy: concepts, phenomena
    and astrophysical constraints*, Annals Phys. **321**, 150–196 (2006); arXiv:astro-ph/0505267.
13. V. A. Kostelecký and N. Russell, *Data tables for Lorentz and CPT violation*, Rev. Mod. Phys.
    **83**, 11 (2011); arXiv:0801.0287.
14. S. Liberati, *Tests of Lorentz invariance: a 2013 update*, Class. Quantum Grav. **30**, 133001
    (2013); arXiv:1304.5795. DOI: 10.1088/0264-9381/30/13/133001. *(numerical bounds in §1.1 read
    directly from eqs. 75–76 and Table 2 of the arXiv v3 text.)*
15. J. Collins, A. Perez, D. Sudarsky, L. Urrutia and H. Vucetich, *Lorentz invariance and quantum
    gravity: an additional fine-tuning problem?*, Phys. Rev. Lett. **93**, 191301 (2004);
    arXiv:gr-qc/0403053.
16. F. W. Stecker, *Gamma-ray and cosmic-ray tests of Lorentz invariance violation and quantum
    gravity models and their implications*, AIP Conf. Proc. **1223**, 192–206 (2010);
    arXiv:0912.0500.

**Alternative protection mechanisms**

17. G. E. Volovik, *The Universe in a Helium Droplet*, Oxford University Press (2003)
    *(book; publisher record not independently verified)*; *Momentum-Space Topology of Standard
    Model*, J. Low Temp. Phys. **119**, 241–247 (2000), arXiv:hep-ph/9907456; and *Reentrant
    violation of special relativity in the low-energy corner*, JETP Lett. **73**, 162–165 (2001),
    arXiv:hep-ph/0101286.
18. N. H. Christ, R. Friedberg and T. D. Lee, *Random lattice field theory: general formulation*,
    Nucl. Phys. B **202**, 89–125 (1982).
19. L. Bombelli, J. Henson and R. D. Sorkin, *Discreteness without symmetry breaking: a theorem*,
    Mod. Phys. Lett. A **24**, 2579–2587 (2009); arXiv:gr-qc/0605006.

**Lattices, reflection groups, invariant theory, spherical designs**

20. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, Grundlehren der
    mathematischen Wissenschaften **290**, 3rd ed., Springer (1999).
21. J. E. Humphreys, *Reflection Groups and Coxeter Groups*, Cambridge University Press (1990) — for
    the Chevalley–Shephard–Todd theorem and the table of invariant degrees. *(standard reference;
    the $F_4$ degrees $\{2,6,8,12\}$ were additionally confirmed numerically, see Appendix A.)*
22. P. Delsarte, J. M. Goethals and J. J. Seidel, *Spherical codes and designs*, Geom. Dedicata **6**,
    363–388 (1977). *(unverified against the primary source; the 5-design property of the $D_4$ root
    system is however re-derived here as a corollary in §5c.)*
23. H. Cohn, J. H. Conway, N. D. Elkies and A. Kumar, *The $D_4$ root system is not universally
    optimal*, Experimental Mathematics **16**, 313–320 (2007); arXiv:math/0607447.
24. S. L. Sobolev, *Cubature formulas on the sphere invariant under transformations of finite
    rotation groups*, Dokl. Akad. Nauk SSSR **146** (2), 310–313 (1962); English translation Soviet
    Math. Dokl. **3**, 1307–1310 (1962). *(Bibliographic record verified against the Mathnet.ru
    archive record. The theorem as used in §5(c) — for a finite reflection group, an invariant
    cubature formula is exact to degree $t$ iff it is exact on the invariant polynomials of degree
    $\le t$ — is taken from secondary statements of Sobolev's theorem; the original was **not read
    in the original**.)*
25. O. R. Musin, *The kissing number in four dimensions*, Annals of Mathematics **168** (1), 1–32
    (2008); arXiv:math/0309430. *(Abstract and publication record read directly; establishes
    $k(4) = 24$ for unrestricted packings, described there as a long-standing open problem. This is
    the correct citation for the §2 kissing-number statement; Conway–Sloane covers the **lattice**
    kissing number only.)*

---

## Appendix C — Revision record

Repairs applied on **2026-08-25** in response to an independent cold review of this note. Each was
recomputed independently before application. The review, and the adjudication recording the
computations together with the items that were **refuted** — and the one bundle held **proposed**
pending a decision, since applied as R16–R17 — are
internal records, not shipped with this note
(`knowledge/audit/standalone_reviews_2026-08-25/review_d4_01_24_08_2026.md` and
`.../ADJUDICATION_D4_2026-08-25.md`).

| # | Where | Repair | Stamp |
|---|---|---|---|
| R1 | Abstract | The reason for one-dimensionality restated non-circularly: $4$ has no expression as a sum of parts from $\{2,6,8,12\}$ other than $2+2$ | 2026-08-25 |
| R2 | Abstract, §2, §5, §8.3 (new), §10 | **(P-sc)** promoted from a clause inside a corollary to a stated premise; the abstract's quantifier now says *scalar*; the two-line contraction argument and a numerical check added | 2026-08-25 |
| R3 | Abstract, §8.2, Appendix A(6), Appendix B | **Factual correction.** The second shell splits into **three** $W(D_4)$ orbits of eight, not two — residuals $32,16,16$, not "$32$ apiece"; the two-orbit reading is the $W(B_4)$ one. Table rebuilt, the two weight obstructions given explicitly, the isotropy condition sharpened to *iff all three weights are equal*, the triality transposition made visible, and the $2\!:\!1\!:\!1$ row's em-dashes filled in ($80$, $16$) | 2026-08-25 |
| R4 | §2 | Kissing number: $24$ as the **unrestricted** four-dimensional maximum is Musin (2008), not Conway–Sloane, which covers the lattice case | 2026-08-25 |
| R5 | §2 | The isotropy residual flagged as a raw, unnormalised diagnostic, not comparable across tables or lattices | 2026-08-25 |
| R6 | §3 | $T$ is an **involution**; triality proper is the order-3 outer automorphism. Restated as $G=\langle W(B_4),T\rangle$ with the maximality of $W(B_4)$ as the reason, and $T \mapsto$ a transposition in $S_3$ | 2026-08-25 |
| R7 | §4 | The $-1/12$ **normalisation pinned**: $a$ multiplies $k\cdot v$ with $\lvert v\rvert^2=2$, so the bond length is $a\sqrt2$ and the same kernel in bond-length units gives $-1/24$. The convention-free content is the moment ratio, not the number | 2026-08-25 |
| R8 | §5, Lemma 1 | Invariant degrees depend on the **reflection representation**, not the abstract group; Remark (i) is a step in the argument | 2026-08-25 |
| R9 | §5(c) | Attributed to **Sobolev (1962)**. "Strictly stronger" **withdrawn**: $\mathcal{H}_4^G=0$ is *equivalent* to the 4-design property (converse proved inline), and weighted unions of designs are designs, so the old justification established nothing. It is stronger than the classical *single-orbit* 24-cell fact | 2026-08-25 |
| R10 | §8.1 | The (P-an) loophole made **non-empty** by an explicit counterexample, $K = k^2 + \epsilon\lvert A(k)\rvert^{2/3}$, with its non-analyticity located ($A$ vanishes at $\pi/8$ on the $e_1 \to (1,1,0,0)/\sqrt2$ arc). Added the log-robustness sharpening: $f\log k^2$ forces $f=(k^2)^2$ | 2026-08-25 |
| R11 | §9(0) (new), §1.3, Abstract | **Attribution corrected.** The fourth-rank isotropy of the $D_4$/FCHC bond set, and the hypercubic failure at the same order, belong to the **1986–87 lattice-gas** literature, not to Neuberger (1987), whose contribution is the field-theoretic reading. The verification status of every new citation is stated in the paragraph itself: one primary read, three **not read in the original**, and the "*precisely because* of rank-four isotropy" motivation explicitly **not asserted** | 2026-08-25 |
| R12 | §9(iii) | The pre-1991 coverage caveat re-pointed at §9(0) and correspondingly weakened for the lattice-gas literature | 2026-08-25 |
| R13 | Appendix A | Code robustness: $-0.0$ normalised before hashing group elements; $1-\cos x$ replaced by $2\sin^2(x/2)$ (recovers ~3 significant digits at the $10^{-2}$ sample points, against a $10^{-6}$ tolerance); the $G$-invariance check on $A(k)$ run over **all 1152** elements rather than the first 50 | 2026-08-25 |
| R14 | Appendix A(7) | Remark (i)'s promise discharged: explicit checks that $G$ acts on the second shell, that shell 1 $\cup$ (shell 2)$/2$ is a genuine $48$-root system (reflection-closed, integral), and that its automorphism group, rebuilt independently, has order $1152$ | 2026-08-25 |
| R15 | Appendix A(8),(9) | New numerical checks for (P-sc) and (P-an), as described in R2 and R10 | 2026-08-25 |
| R16 | Abstract, §1.1, §1.2, §5, §7, §8.5, §10 | **The flagship caveat replaced.** The review's central objection is adjudicated and upheld: after the continuation of §7, $(k\cdot k)^2$ is a Lorentz scalar, the pole sits at constant $p_\mu p^\mu$, and the surviving isotropic quartic is a **mass renormalisation** with $\eta^{(4)} = 0$, not a boost violation; conversely an isotropic-but-boost-violating quartic would need $\lvert\mathbf k\rvert^4$, which is invariant under neither $G$ nor $W(B_4)$, so the preferred frame cannot come from the kernel. The former caveat ("it closes one of two channels, and the surviving channel is the more strongly constrained one") is **withdrawn** and replaced by the honest one: *the hard step is the Euclidean-to-Lorentzian passage, which this note does not perform.* Carried through every place the old caveat was stated — abstract, §1.1, §8.5 and §10 — since a caveat restated in four places is replaced in four places. Also **free strengthening**: $P_1 = P_3 = P_5 = 0$ and $P_2 \in \mathbb{R}k^2$ (so everything below degree six is $O(4)$-invariant) added as a corollary in §5; and §8.5's "it says nothing about dimension four or five" corrected — the framework *does* kill anisotropic dimension four (a standard result, credited in §9(iii)) and every odd power; what it does not fix is the **magnitude** of the isotropic dimension-four coefficient, the limiting speed | 2026-08-25 |
| R17 | Abstract, §2, §5, §8.4 (new), §10 | **(P-op) added as a fourth load-bearing premise**, on the *transfer* rather than on the theorem — the lattice mathematics of §3–§7 is untouched by it and says so. The theorem is proved at the full point group, but a medium that supplies the preferred frame the phenomenological reading needs leaves operative only $\operatorname{Stab}_G(e_4)$, of order $48$ (orbit–stabiliser on the single $24$-element second shell), restricting faithfully onto the full octahedral group $W(B_3)$, whose degree-4 *spatial* invariant space is **two**-dimensional — so $\sum_{i\le3}k_i^4$ is permitted there. The protection that remains is carried by the coupling's **constancy on the single full-group bond orbit** (which forces $\sum_v (k\cdot v)^4 = 12(k^2)^2$ in four variables, descending to every 3-plane), **not** by the reduced symmetry; the $\pm4$ residual split of the $12+12$ bonds about $e_4$ is the axis-specific sensitivity decomposition of that protection, not its mechanism. Would-change-if: any weighting invariant at the reduced group but not constant on the orbit ($M_{1111}-3M_{1122} = 4(1-w)$) restores dimension-six *spatial* anisotropy. The physics transfer in §5's corollary is conditioned on the premise explicitly, and the premise count is updated from three to four throughout | 2026-08-25 |
| — | §8.4 → §8.5 | "What the theorem does not do" is renumbered **§8.5** to make room for §8.4 (P-op); its cross-reference in §8.1 is updated. Its content is revised under R16 | 2026-08-25 |
