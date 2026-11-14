# Sources and validation

Date: 13 November 2026.

This record accompanies the new introductory notes. It distinguishes consulted sources, explicit calculations, theorem citations, mathematical review, and mechanical validation.

## Local Zotero sources

| Source | Zotero item / attachment | Material consulted | Coverage and qualification |
|---|---|---|---|
| Kai Behrend, *Introduction to algebraic stacks*, 127-page lecture-note version; library record dated 2014 | `VATE6STI` / `X4I5FF7W` | §§3.3–3.6, especially pp. 110–125: algebraic/DM stacks, coarse spaces, equivariant bundles, root stacks | Zotero indexes only 100 of 127 pages. The later sections were read directly from the saved PDF using macOS PDFKit. For the checked later sections, PDF page numbers and printed page numbers coincide. |
| Sebastian Casalaina-Martin and Jonathan Wise, *An introduction to moduli stacks, with a view towards Higgs bundles on algebraic curves*, arXiv:1708.08124, saved 147-page version | `M7ZYQQVN` / `EFK3ZA2P` | §§2–4 and 6; Definition 3.31, p. 26, for the stack axioms; Example 4.6, pp. 29–30, for the diagonal as an isomorphism sheaf | Indexed coverage is 100 of 147 pages. The cited introductory sections are within that coverage. The later Higgs-bundle discussion was not needed. |
| Jarod Alper, *Good moduli spaces for Artin stacks*, Ann. Inst. Fourier 63 (2013), 2349–2402 | `N52IIMPU` / `C5YGYDI5` | Good moduli spaces and Theorem 10.3, journal p. 2386, for vector-bundle descent | All 55 PDF pages are indexed. The notes restrict the descent application to separated finite-type DM stacks in characteristic zero. |

The Behrend PDF was read at its original local attachment path:

`/Users/Benjamin/Zotero/storage/X4I5FF7W/Behrend - 2014 - Introduction to algebraic stacks.pdf`

These PDFs were read in place. No references were imported, no Zotero records were edited, and no source PDFs were copied into the deliverable.

The notes explicitly distinguish the reduced residual gerbe over a root point from the nonreduced scheme-theoretic fibre of the coarse map. They use the modern geometric-classifying definition of a coarse moduli space, and distinguish this from a good GIT/moduli-space quotient.

## Primary online references

- The [Stacks Project, Tag 026N](https://stacks.math.columbia.edu/tag/026N), for the definitions of algebraic and Deligne–Mumford stacks.
- The [Stacks Project, Tag 04UV](https://stacks.math.columbia.edu/tag/04UV), for quotient stacks described using torsors and equivariant maps.
- The [Stacks Project, Tag 04TK](https://stacks.math.columbia.edu/tag/04TK), for algebraic stacks from smooth groupoids.
- The [Stacks Project, Tag 06N3](https://stacks.math.columbia.edu/tag/06N3), for the equivalence between an unramified diagonal and an étale atlas.
- The [Stacks Project, Tag 04UX](https://stacks.math.columbia.edu/tag/04UX), for coarse-space existence references. This is a guide to the primary literature, rather than a proof of the theorem.
- [Alper's original paper](https://maths-people.anu.edu.au/~alperj/papers/gms.pdf), also available as the [published article](https://aif.centre-mersenne.org/articles/10.5802/aif.2833/), for good moduli spaces and descent.
- [Vistoli, *Notes on Grothendieck topologies, fibered categories and descent theory*](https://arxiv.org/abs/math/0412512), included as further systematic reading on descent. Exact theorem locators in the introductory notes use the consulted Casalaina-Martin–Wise source instead.
- [Cadman, *Using stacks to impose tangency conditions on curves*](https://arxiv.org/abs/math/0312349), included for the original divisor-root construction and further reading. The explicit construction and local chart were also checked in the saved Behrend notes.

## Repository context

The notes were informed by these existing files, which were read without modification:

- `claude-notes/conventions.tex`: current names, section-weight convention, level twist, and signs.
- `claude-notes/comparison-theorem.tex`: regular versus critical levels, finite boundary stabilisers, stack polarisation versus quotient sheaf, and the common boundary.
- `SemiprojectiveAlgebraicCutting-integrated.tex`: earlier conventions and the distinction between stack and coarse normal geometry.

The new notes use the convention of 12 November 2026. They do not revise or certify the manuscript's comparison theorem, quantisation theorem, or general degeneration arguments.

## Mathematical review

The draft received separate read-only reviews of foundational definitions and references, equivariant sheaves and root-stack calculations, and consistency with the repository's cutting conventions. Corrections incorporated into the new source include stating the character obstruction modulo the group order, specifying the ambient stack in the normal-line exercise, explaining the dual-frame torsor in the weighted-family convention, and limiting finiteness statements when using the Stacks Project's broad definition of DM stacks.

The calculations reviewed include:

- The cyclic affine-line quotient and the quadratic-cone invariant ring.
- Equivariant sections and the difference between pushforward and descent.
- The weighted-line charts and coarse map.
- The floor formula for divisor-line pushforward, including negative powers.
- The root divisor, its thickened coarse fibre, and normal/conormal characters.
- The two cutting semistable loci and their Veronese rings.
- The common boundary, opposite normal characters, equal polarisation characters, and periodic boundary-section counts.
- All ten exercise solutions.

The notes give elementary proofs of the explicit examples and label the general algebraicity, DM-characterisation, coarse-existence/local-structure, and descent results as cited theorems. This review is not a formal proof verification or a comprehensive audit of the research manuscript.

## Mechanical validation

The final standalone source was compiled with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build dm-stacks-introduction.tex
```

The final log contains no LaTeX warnings, unresolved citations or cross-references, multiply defined labels, overfull boxes, or underfull boxes. The result has **25 pages**. The PDF also passed:

```sh
qpdf --check build/dm-stacks-introduction.pdf
```

PDF parsing and structural checks do not establish mathematical correctness; the mathematical review and explicit arguments are separate evidence.

The PDF was opened with macOS PDFKit, which found 25 pages and extracted its text without replacement characters. Rendered pages covering the title and contents, the atlas diagram, line-bundle descent, the two cutting examples, and the bibliography were visually inspected.

A SHA-256 baseline was taken for all **93 pre-existing non-Git repository files** before any notes were created. The final comparison found **zero changed files and zero missing files**. The per-file baseline and results are recorded in `preservation-check.json`. The new PDF, LaTeX source, README, this record, validation data, and build outputs all live under the newly created notes directory.
