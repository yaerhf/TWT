# Quartic isotropy of the $D_4$ lattice

### An invariant-theoretic statement about rotational Lorentz violation from a discrete substrate, its sharpness, and its limits

*Draft — standalone note. All numerical claims are reproducible with the script in Appendix A
(numpy only, runtime ≈ 15 s).*

---

## Abstract

Let $G = \operatorname{Aut}(D_4)$ be the automorphism group of the $D_4$ root system in
$\mathbb{R}^4$, of order $1152$ (isomorphic to the Weyl group $W(F_4)$, whose invariant degrees are
$\{2,6,8,12\}$). Because $G$ has no invariant of degree $4$ other than $(k^2)^2$, the space of
$G$-invariant quartic polynomials is **one-dimensional**. Consequently, for *any* dispersion kernel
that is invariant under the $D_4$ point group and analytic at $k=0$, the quartic term of its
derivative expansion is exactly rotationally invariant: there is no anisotropic $p^4$ term, and
hence no anisotropic dimension-six Lorentz-violating operator, whatever the underlying dynamics.
The leading rotational anisotropy is pushed to $p^6$, i.e. to **dimension eight**. This bound is
*reached*, not merely an upper bound: the degree-6 invariant space is two-dimensional, containing
the explicit anisotropic invariant
$A(k) = 5k^2\sum_i k_i^4 - 4\sum_i k_i^6 - \tfrac54 (k^2)^3$, and the sixth bond moment of the
$D_4$ nearest-neighbour set is correspondingly anisotropic. The statement is specific to $D_4$ and
not a generic consequence of four-dimensionality: the hypercubic lattice $\mathbb{Z}^4$, whose point
group $W(B_4)$ has invariant degrees $\{2,4,6,8\}$, admits a two-dimensional degree-4 invariant
space containing $\sum_i k_i^4$, and its nearest-neighbour dispersion is direction-dependent already
at quartic order (axis-to-diagonal ratio $4$).

Two premises are load-bearing and are stated up front rather than in a footnote: **(P-an)**
analyticity in $k$, so that a derivative expansion exists at all; and **(P-pg)** invariance under the
*full* point group **including triality** — the reflection subgroup $W(D_4)$ of order $192$ has a
*three*-dimensional degree-4 invariant space, and the two second-shell sub-orbits $\{\pm 2e_i\}$ and
$(\pm1,\pm1,\pm1,\pm1)$ are each separately anisotropic (fourth-moment residual $32$ apiece),
cancelling *only* at equal weight. A coupling that weights triality-related orbits unequally
restores dimension-six anisotropy.

We also state clearly what the result does **not** do. It closes the **anisotropic** channel only.
The rotationally *invariant* dimension-six term is untouched: for the nearest-neighbour $D_4$ kernel
it is present and computable, $\omega^2 \propto k^2 - \tfrac{1}{12}a^2 (k^2)^2 + O(a^4 k^6)$, with an
$O(1)$ coefficient. Lorentz violation is not solved by this theorem; one of its two channels is
closed, and the surviving channel is the one that carries the strongest published constraints.

Finally, on attribution: the *physical* content — that the $D_4$/$F_4$ lattice has an isotropic
quartic while the hypercubic lattice does not — is **known in the lattice field theory literature**
and dates to Neuberger (1987); it was restated for lattice QCD as recently as December 2025. What
this note adds is the kernel-independent invariant-theoretic proof (a statement about the group, not
about one action), the two-sided sharpness argument, the explicit triality premise, and the transfer
of the statement into the effective-field-theory language used in quantum-gravity phenomenology,
where it does not appear to have been noted. See §9.

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

It is worth separating two distinct things that both live at dimension six, because the theorem
below touches only one of them:

* the **anisotropic** part — a term such as $\sum_i p_i^4$ that depends on the orientation of $p$
  relative to the substrate axes. This is the part that is manifestly a lattice artefact;
* the **isotropic** part — a term $(p^2)^2$ that is rotationally invariant but still violates boost
  invariance. This is what the bounds quoted above actually constrain: the caption of Liberati's
  Table 2 specifies "rotational invariant" LIV operators. (Anisotropic coefficients are constrained
  separately and are tabulated in the SME data tables [Kostelecký–Russell].)

**The theorem in this note closes the first and says nothing whatever about the second.** That
scoping is the single most important honesty point in what follows and it is restated in §8.

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
only that the couplings respect the full point group. There is no anisotropic dimension-six operator
to fine-tune away, because there is no anisotropic quartic invariant for it to be built from.

The leading anisotropy then sits at $p^6$: dimension eight. For a substrate at scale $\Lambda$, the
relative size of the leading anisotropic effect is $(E/\Lambda)^4$ rather than $(E/\Lambda)^2$.

### 1.3 Provenance and scope of the novelty claim

The result was isolated in the course of a lattice-substrate emergent-spacetime programme; nothing in
this note depends on that programme, and no part of it is assumed below. The reader needs only
$\mathbb{R}^4$, a root system, and a Taylor expansion.

The novelty claim is deliberately narrow, and is set out in full in §9. In brief: the *physics* is
known. Neuberger (1987) argued that $F_4$ lattices are singularly well suited to regularising scalar
fields precisely because the dimension-six Lorentz-breaking operator that afflicts the hypercubic
lattice is absent; the free $F_4$ dispersion $g(p) = p^2 - \tfrac{1}{12}(p^2)^2 + O(p^6)$ has been in
the literature since then; and Katz and Nogradi (2025) state for the same lattice that "at order
$O(a^2)$ the correction is still Lorentz invariant, the first order where this does not hold is
$O(a^4)$". What is offered here is a *proof of the right generality* — a statement about the
invariant ring of the point group rather than a computation for one action — together with the
sharpness argument, the explicit premises, and the translation into LIV-EFT terms.

---

## 2. Setup and conventions

We work in $\mathbb{R}^4$ with the standard Euclidean inner product; $k = (k_1,k_2,k_3,k_4)$ denotes
a wavevector and $k^2 = k\cdot k$. Nothing in the group theory depends on signature; the passage to
a Lorentzian dispersion relation is discussed in §7 and involves an additional assumption that we
flag rather than hide.

**Lattice.** $D_4 = \{x \in \mathbb{Z}^4 : \textstyle\sum_i x_i \in 2\mathbb{Z}\}$. Its minimal
vectors (the $D_4$ *root system*, and simultaneously its nearest-neighbour bond set) are the $24$
vectors obtained from $(\pm1,\pm1,0,0)$ by permutation of coordinates, each of squared length $2$.
The kissing number $24$ is the maximum in four dimensions [Conway–Sloane]. The convex hull of these
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

**EFT dictionary.** With a dispersion relation $E^2 = p^2 + m^2 + \sum_n \eta^{(n)} p^n/M^{n-2}$, a
$p^n$ term originates in a mass-dimension-$(n+2)$ operator. We will use the two dictionary entries
$n = 4 \leftrightarrow$ dimension six and $n = 6 \leftrightarrow$ dimension eight throughout.

**Moments.** For a finite set $S \subset \mathbb{R}^4$ with weights $w_v$, the $2m$-th moment tensor
is $M_{i_1\cdots i_{2m}} = \sum_{v\in S} w_v\, v_{i_1}\cdots v_{i_{2m}}$. We call the fourth moment
*isotropic* if $M_{ijkl} = A(\delta_{ij}\delta_{kl} + \delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})$
for some $A$, and measure failure by the **residual**
$\max_{ijkl} |M_{ijkl} - A(\delta\delta+\delta\delta+\delta\delta)_{ijkl}|$ with $A$ fixed by the
mixed component $M_{1122}$.

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

The chain $W(D_4) \subset W(B_4) \subset G$ has indices $2$ and $3$; the index-$3$ step is triality,
generated by the orthogonal involution

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
agrees with $-1/12$ to eight digits along random directions (Appendix A). This reproduces exactly the
coefficient quoted in the lattice literature for the $F_4$ lattice, $g(p) = p^2 - \tfrac{1}{12}(p^2)^2
+ O(p^6)$, which is a useful external check on the moments.

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
(equivalently, the exponents are $1,5,7,11$ and the Coxeter number is $12$).

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

**Corollary (no anisotropic dimension-six operator).** A dispersion relation derived from such a
kernel has an $O(p^4)$ term of the form $c\,(p^2)^2$ with $c$ a single constant. There is no
direction-dependent $p^4$ contribution, hence no anisotropic dimension-six LIV operator, for any
choice of couplings compatible with the full point group.

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

**(c) Spherical-design corollary.** If $\mathcal{H}_4^G = 0$ then for any $Y \in \mathcal{H}_{d}$ with
$d \le 4$ and any $G$-orbit $\mathcal{O}$ on a sphere, $\sum_{v\in\mathcal{O}} Y(v) = 0$ — the sum
defines a $G$-invariant functional on $\mathcal{H}_d$, which must vanish when $\mathcal{H}_d^G = 0$.
Hence **every $G$-orbit on a sphere is a spherical 4-design**, and a 5-design since $-\mathbb{1}\in G$
kills the odd degrees. The $24$-cell realising a spherical 5-design is a classical fact
[Delsarte–Goethals–Seidel 1977; Cohn–Conway–Elkies–Kumar 2007]; the group statement above implies it,
and is strictly stronger, since it constrains arbitrary weighted combinations of orbits and not just
single orbits. A concrete instance of the theorem: the Reynolds average of $k_1^4$ over $G$ is
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
as motivation, not as a corollary.)*

---

## 8. Premises, and what is not claimed

### 8.1 (P-an) Analyticity

The proof consists of matching homogeneous components of a Taylor series. If the kernel is not
analytic at $k = 0$ — for instance if the substrate has a memory kernel producing $|k|^3$, $k^2\log
k^2$, or fractional-power terms — the argument does not apply. Polynomial invariant theory constrains
polynomials. A non-analytic kernel can be $G$-invariant and still direction-dependent at leading
non-quadratic order.

This is a real restriction, not a formality. Substrates with dissipation or long-range memory are
exactly the ones for which non-analytic kernels are expected. The honest statement is: *given a
derivative expansion, the quartic term is isotropic; whether a derivative expansion exists is a
separate question about the dynamics.*

### 8.2 (P-pg) The full point group, including triality

The theorem requires invariance under all $1152$ elements. If the couplings are only $W(D_4)$-
symmetric (order $192$), the degree-4 invariant space is **three**-dimensional and there is no
protection at all. Even $W(B_4)$ symmetry (order $384$) leaves a two-dimensional degree-4 space, as
§7 shows.

The failure mode is concrete and worth spelling out, because it is how a real model would lose the
result without anybody noticing. Consider the second shell of $D_4$, which splits under $W(D_4)$
into two sub-orbits:

| sub-orbit | size | $M_{1111}$ | $M_{1122}$ | 4th-moment residual |
|---|---:|---:|---:|---:|
| $\{\pm 2 e_i\}$ | 8 | 32 | 0 | **32** |
| $(\pm1,\pm1,\pm1,\pm1)$ | 16 | 16 | 16 | **32** |
| combined, equal weight | 24 | 48 | 16 | **0** |
| combined, weights $2\!:\!1$ | 24 | — | — | **32** |

Each sub-orbit is separately, and substantially, anisotropic. They cancel *exactly* — and only — at
equal weight, because triality exchanges them. A model that assigns different couplings to
second-neighbour bonds of the two types (a completely natural thing to do if one has not noticed the
triality structure, since they are geometrically distinguishable: one is "along an axis", the other
"along a diagonal") **restores dimension-six anisotropy at full strength**.

So the protection is a property of the symmetry of the *action*, not of the *lattice geometry* alone.
Putting fields on a $D_4$ lattice is necessary but not sufficient; the couplings must respect
triality. This is the result's own "would change if" clause and it should travel with it.

### 8.3 What the theorem does **not** do

This subsection is the one that must not be skimmed.

**It closes anisotropy only.** The rotationally invariant dimension-six term is entirely untouched.
The argument constrains the *tensor structure* of $P_4$, not its magnitude, and the isotropic
direction $(k^2)^2$ is available and generically occupied. §4 exhibits it explicitly for the
nearest-neighbour $D_4$ kernel with coefficient $-1/12$ — an $O(1)$ number. In LIV-EFT terms, a $D_4$
substrate at scale $\Lambda$ still generically produces $\eta^{(4)} \sim (M_{\rm Pl}/\Lambda)^2$,
which is exactly the quantity bounded at the $10^{-6}$–$10^{-8}$ level by the constraints quoted in
§1.1. **The theorem does not help with that at all.** A reader who comes away with the impression
that a $D_4$ substrate solves the Lorentz-violation problem has misread this note; what it removes is
one of the two channels, and the surviving channel is the more strongly constrained one.

**It says nothing about dimension four or five.** Species-dependent limiting speeds (dimension four)
and CPT-odd $p^3$ terms (dimension five) are separate questions with their own, much tighter,
constraints. Nothing here addresses them.

**It fixes no magnitude.** No coefficient is predicted, including the dimension-eight anisotropic
coefficient whose *existence* §6 establishes. Its size depends on the dynamics.

**It is a statement about a symmetry, and symmetry statements have a known loophole.** Collins,
Perez, Sudarsky, Urrutia and Vucetich showed that in an interacting theory regulated by a
Lorentz-violating cutoff, violations generically percolate to low-dimension operators with
unsuppressed coefficients. Our argument is partly robust to this and partly not, and the distinction
matters. It *is* robust for the tensor structure: any counterterm generated by a regulator that
preserves $G$ is itself $G$-invariant, so if it is analytic its quartic part is again isotropic — the
anisotropy protection survives loops. It is *not* a response to the percolation problem itself, which
concerns the magnitude of the isotropic coefficients — again, the channel we do not close.

**It does not argue that nature uses this lattice.** The result is conditional: *if* a substrate is
$D_4$-symmetric with triality-symmetric analytic couplings, *then* its leading rotational anisotropy
is dimension eight. Whether any such substrate exists is not addressed.

---

## 9. Relation to prior work

Honest attribution requires separating three literatures.

**(i) Lattice field theory — where this result already lives.** The physical content is known and
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

**We therefore do not claim the physical result as new.** What §5 adds is a proof at the right level
of generality — a one-line consequence of $F_4$ having no degree-4 basic invariant, valid for every
analytic point-group-symmetric kernel rather than for a particular free action — together with the
sharpness argument of §6, the explicit triality premise of §8.2, and the scoping of §8.3. To our
knowledge the invariant-theoretic formulation, the two-sided sharpness, and the triality-weighting
caveat have not been assembled in one place.

**(ii) Discrete geometry.** That the $24$-cell is a spherical 5-design is classical
[Delsarte–Goethals–Seidel 1977]; it cannot be a 6-design because a 6-design in $S^3$ requires at
least $30$ points, consistent with the anisotropic sixth moment of §4. Cohn, Conway, Elkies and Kumar
(2007) study the $D_4$ root system's optimality properties and, notably, show it is *not* universally
optimal. The design property is a corollary of the group statement (§5c) rather than the other way
round. The invariant-degree facts are standard reflection-group theory (Chevalley–Shephard–Todd;
Coxeter); $F_4$'s degrees $\{2,6,8,12\}$ and exponents $1,5,7,11$ are textbook.

**(iii) Lorentz-violation phenomenology — where, as far as we can tell, the result has not been
carried.** The EFT framework for modified dispersion relations is that of Myers and Pospelov (2003);
the constraint compilations are Mattingly (2005), Kostelecký and Russell (SME data tables), and
Liberati (2013), from which the numbers in §1.1 are taken. Searches of this literature turned up no
use of the $D_4$/$F_4$ point-group argument. That is the gap this note is aimed at: the lattice-QCD
community has long known that the $F_4$ lattice is kinder to rotational invariance, and the
quantum-gravity-phenomenology community has long known that anisotropic dimension-six operators are
tightly bounded, and the two facts appear not to have been put side by side.

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
  point-group-symmetric dispersion kernel therefore has an exactly isotropic quartic term, and there
  is no anisotropic dimension-six Lorentz-violating operator.
* $\dim\mathbb{R}[k]^G_6 = 2$, with an explicit anisotropic invariant $A(k)$ taking both signs on the
  unit sphere, and the sixth bond moment is anisotropic. Dimension eight is therefore *reached*.
* $\mathbb{Z}^4$ fails: $\dim\mathbb{R}[k]^{W(B_4)}_4 = 2$, $\sum_i k_i^4$ survives, and the
  nearest-neighbour dispersion is direction-dependent at quartic order by a factor of $4$. The result
  is an $F_4$ fact, not a four-dimensionality fact.
* Two premises are load-bearing: analyticity, and the full point group including triality. Unequal
  weighting of triality-related orbits restores dimension-six anisotropy at full strength.
* **The theorem closes the anisotropic channel only.** The isotropic dimension-six term survives with
  an $O(1)$ coefficient ($-1/12$ for the nearest-neighbour kernel) and is the more strongly
  constrained one. Lorentz violation is not solved.

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
  (6) premise P-pg: the two shell-2 sub-orbits cancel only at equal weight.
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
                out[np.round(A, 9).tobytes()] = np.round(A, 9)
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
gD4 = lambda k: np.sum(1 - np.cos(Rm @ k)) / 6.0
gZ4 = lambda k: np.sum(1 - np.cos(Zm @ k))
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
      " and G-invariant",
      any(abs(aniso(k)) > 1e-9 for k in kk) and all(np.isclose(aniso(k), aniso(A@k))
                                                     for k in kk for A in G[:50]))
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
print("\n(6) premise P-pg: the shell-2 sub-orbits")
oA = [tuple(s if k == i else 0 for k in range(4)) for i in range(4) for s in (2, -2)]
oB = [t for t in itertools.product((1, -1), repeat=4)]
rA, _ = resid4(oA); rB, _ = resid4(oB)
check("each shell-2 sub-orbit is separately anisotropic with residual 32",
      rA == 32 and rB == 32, f"{{+-2e_i}}: {rA},  (+-1,+-1,+-1,+-1): {rB}")
rEq, AEq = resid4(oA + oB)
check("they cancel EXACTLY at equal weight", rEq == 0, f"combined residual={rEq}, A={AEq}")
rUn, _ = resid4(oA + oB, w=[2]*len(oA) + [1]*len(oB))
check("unequal weighting (2:1) RESTORES quartic anisotropy", rUn != 0, f"residual={rUn}")

print("\n" + ("ALL CHECKS PASSED" if not fails else f"FAILURES: {fails}"))
```

### Expected output

```
(1) bond sets and moments
  [OK ] D4 has 24 nearest-neighbour bonds, all of squared length 2  |bonds|=24
  [OK ] D4 second moment = 12 delta_ij
  [OK ] D4 fourth moment exactly isotropic: M_1111 = 12 = 3 M_1122, residual 0
        M_1111=12, M_1122=4, residual=0
  [OK ] D4 sixth moment NOT isotropic (M_112233 = 0 but M_111111 = 12 != 0)
        M_111111=12, M_112233=0, residual=12

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
  [OK ] D4: quartic coefficient is direction-INDEPENDENT and equals -1/12
        min=-0.08333334 max=-0.08333333, -1/12=-0.08333333
  [OK ] Z^4: quartic coefficient is direction-DEPENDENT, = -(1/12) sum u_i^4
        axis -0.083333 vs diagonal -0.020833  (ratio 4)
  [OK ] Z^4 fourth bond moment anisotropic: N_1111 = 2, N_1122 = 0, residual 2
  [OK ] explicit sixth moment M6(k) = 60 k^2 sum k_i^4 - 48 sum k_i^6
  [OK ] M6 is invariant under the triality generator T, while sum k_i^4 is not
  [OK ] the anisotropic sextic A(k) = ... is nonzero and G-invariant
  [OK ] A(k) is constant on a triality orbit: A(e1) = A((1,1,1,1)/2)  A=-0.250000
  [OK ] A(k) separates the short-root from the long-root direction
        A(e1)=-0.250000  vs  A((1,1,0,0)/sqrt2)=0.250000

(6) premise P-pg: the shell-2 sub-orbits
  [OK ] each shell-2 sub-orbit is separately anisotropic with residual 32
        {+-2e_i}: 32,  (+-1,+-1,+-1,+-1): 32
  [OK ] they cancel EXACTLY at equal weight  combined residual=0, A=16
  [OK ] unequal weighting (2:1) RESTORES quartic anisotropy  residual=32

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
| shell-2 sub-orbit residuals | $32$ each; $0$ combined at equal weight | computed |
| photon $\xi^{(4)}$ bound | $-10^{-7} \lesssim \xi^{(4)} \lesssim 10^{-8}$ | quoted, Liberati (2013) eq. 75 |
| electron $\eta^{(4)}$ bound | $-10^{-7} \lesssim \eta^{(4)} \lesssim 10^{-6}$ | quoted, Liberati (2013) eq. 75 |
| proton $\eta^{(4)}_p$ bound | $-10^{-3} \lesssim \eta^{(4)}_p \lesssim 10^{-6}$ (99% CL) | quoted, Liberati (2013) eq. 76 |

---

## References

All entries below were checked against arXiv, Crossref or the publisher record. Items marked
*(unverified)* were not confirmed against a primary source and should be checked before submission.

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

**Lorentz-violation effective field theory and constraints**

8. R. C. Myers and M. Pospelov, *Ultraviolet modifications of dispersion relations in effective field
   theory*, Phys. Rev. Lett. **90**, 211601 (2003); arXiv:hep-ph/0301124.
9. D. Mattingly, *Modern tests of Lorentz invariance*, Living Rev. Rel. **8**, 5 (2005);
   arXiv:gr-qc/0502097.
10. V. A. Kostelecký and N. Russell, *Data tables for Lorentz and CPT violation*, Rev. Mod. Phys.
    **83**, 11 (2011); arXiv:0801.0287.
11. S. Liberati, *Tests of Lorentz invariance: a 2013 update*, Class. Quantum Grav. **30**, 133001
    (2013); arXiv:1304.5795. DOI: 10.1088/0264-9381/30/13/133001. *(numerical bounds in §1.1 read
    directly from eqs. 75–76 and Table 2 of the arXiv v3 text.)*
12. J. Collins, A. Perez, D. Sudarsky, L. Urrutia and H. Vucetich, *Lorentz invariance and quantum
    gravity: an additional fine-tuning problem?*, Phys. Rev. Lett. **93**, 191301 (2004);
    arXiv:gr-qc/0403053.
13. F. W. Stecker, *Gamma-ray and cosmic-ray tests of Lorentz invariance violation and quantum
    gravity models and their implications*, AIP Conf. Proc. **1223**, 192–206 (2010);
    arXiv:0912.0500.

**Alternative protection mechanisms**

14. G. E. Volovik, *The Universe in a Helium Droplet*, Oxford University Press (2003)
    *(book; publisher record not independently verified)*; *Momentum-Space Topology of Standard
    Model*, J. Low Temp. Phys. **119**, 241–247 (2000), arXiv:hep-ph/9907456; and *Reentrant
    violation of special relativity in the low-energy corner*, JETP Lett. **73**, 162–165 (2001),
    arXiv:hep-ph/0101286.
15. N. H. Christ, R. Friedberg and T. D. Lee, *Random lattice field theory: general formulation*,
    Nucl. Phys. B **202**, 89–125 (1982).
16. L. Bombelli, J. Henson and R. D. Sorkin, *Discreteness without symmetry breaking: a theorem*,
    Mod. Phys. Lett. A **24**, 2579–2587 (2009); arXiv:gr-qc/0605006.

**Lattices, reflection groups, invariant theory, spherical designs**

17. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, Grundlehren der
    mathematischen Wissenschaften **290**, 3rd ed., Springer (1999).
18. J. E. Humphreys, *Reflection Groups and Coxeter Groups*, Cambridge University Press (1990) — for
    the Chevalley–Shephard–Todd theorem and the table of invariant degrees. *(standard reference;
    the $F_4$ degrees $\{2,6,8,12\}$ were additionally confirmed numerically, see Appendix A.)*
19. P. Delsarte, J. M. Goethals and J. J. Seidel, *Spherical codes and designs*, Geom. Dedicata **6**,
    363–388 (1977). *(unverified against the primary source; the 5-design property of the $D_4$ root
    system is however re-derived here as a corollary in §5c.)*
20. H. Cohn, J. H. Conway, N. D. Elkies and A. Kumar, *The $D_4$ root system is not universally
    optimal*, Experimental Mathematics **16**, 313–320 (2007); arXiv:math/0607447.
