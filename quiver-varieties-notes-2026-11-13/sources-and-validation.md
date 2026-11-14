# Sources and validation for the quiver-variety notes

## Audience and mathematical scope

The notes are written for a reader familiar with Chapters I–II of Hartshorne. Matrices, affine schemes, projective space, bundles, tangent spaces and relative Proj provide the entry points. Representation theory, GIT stability, Lie algebras, differential forms and moment maps are introduced where used. General invariant theory and reduction theorems are identified as tools, rather than presented as consequences of Hartshorne I–II alone. The optional real-equation discussion does not assume a course in hyperkähler geometry.

The treatment concentrates on framed Nakajima varieties and elementary models. It does not attempt a general account of Kac–Moody theory, wall crossing, derived geometry, gauge theory or the construction of every representation moduli space.

## Textbooks read directly from Literature

The Literature collection was read without modification. Page numbers below are printed page numbers; for these two PDFs the corresponding PDF page number is the printed number plus 13.

**Alexander Kirillov Jr., *Quiver Representations and Quiver Varieties*, Graduate Studies in Mathematics 174, AMS, 2016.**

Local source: `/Users/Benjamin/Literature/Algebraic & Complex Geometry/Alexander Kirillov Jr_/Quiver Representations and Quiver Varieties (195)/Quiver Representations and Quiver Varietie - Alexander Kirillov Jr_.pdf`.

- Chapter 1, pages 3–15: quivers, representations, paths and subrepresentations.
- Chapter 2, pages 23–29: representation spaces, orbits, degenerations and semisimplification.
- Section 9.3, pages 163–168: semi-invariants, relative Proj and the projective morphism to the affine quotient; especially equation (9.8), page 165.
- Section 10.1, pages 191–195: King stability, particularly Definition 10.4 and Theorem 10.5 on page 193.
- Sections 10.3–10.5, pages 200–209: framing, moment maps and stability. Lemma 10.26 on page 205 uses a framing term with the opposite sign to the one in these notes. Equation (10.37) on page 209 describes the cyclic chamber with the source's stability convention.
- Theorem 10.35, page 209: smooth symplectic geometry and dimension in the generic stable situation. Projectivity and resolution hypotheses are treated separately on pages 206 and 210.
- Pages 213–216: cotangent flag varieties and Grassmannians, especially Theorem 10.43 and Example 10.45.
- Section 10.9, pages 219–222: a scaling construction with an acyclic original orientation. Those hypotheses are not silently transferred to the Jordan quiver.
- Sections 11.1–11.2, pages 225–229: the Hilbert-scheme example, including Example 11.4 and Theorem 11.5.

**Hiraku Nakajima, *Lectures on Hilbert Schemes of Points on Surfaces*, University Lecture Series 18, AMS, 1999.**

Local source: `/Users/Benjamin/Literature/Algebraic & Complex Geometry/Hiraku Nakajima/Lectures on Hilbert Schemes of Points on Surfaces (20)/Lectures on Hilbert Schemes of Points on S - Hiraku Nakajima.pdf`.

- Section 1.2, pages 7–11: cyclic commuting matrices and the Hilbert scheme; Theorem 1.9 on page 7.
- Theorem 1.13, page 11: punctual fibres, useful for avoiding an incorrect Lagrangian claim for the Jordan example.
- Theorem 2.1, page 17: the framed matrix equation and cyclic stability.
- Proposition 2.8 and Lemma 2.9, page 24: rank-one framing forces the return framing map to vanish and the Jordan operators to commute.
- Chapter 3, pages 29–45: further study of GIT and hyperkähler constructions.

## Local Zotero sources

Zotero item and attachment keys below record exactly which local records were consulted. Indexed full text was read, with selected theorem statements checked against page images. No Zotero records or attachments were modified.

| Source | Zotero item / attachment | Relevant coverage |
| --- | --- | --- |
| V. Ginzburg, *Lectures on Nakajima's Quiver Varieties* (2009), [arXiv:0905.0686](https://arxiv.org/abs/0905.0686) | `H75YRCWA` / `8V7ZBZA7` | Sections 2.2–2.3 on quotients and stability; Propositions 5.1.5 and 5.6.5, Corollary 5.1.9 and Theorem 5.2.2 on cyclic stability, smoothness and Hilbert schemes. All 43 local PDF pages were indexed. In this local HAL copy, printed page numbers are three less than PDF page numbers. |
| H. Nakajima, *Introduction to quiver varieties—for ring and representation theorists* (2016), [arXiv:1611.10000](https://arxiv.org/abs/1611.10000) | `VJJ9E9TS` / `XQ8EPJIQ` | Section 2.1 on moment equations; Definition 6, Proposition 8 and Theorem 9 on stable smooth quotients; Example 10 on Grassmannians and failure of surjectivity. All 19 local pages were indexed. |
| A. D. King, *Moduli of representations of finite dimensional algebras*, Q. J. Math. 45 (1994), 515–530, [DOI](https://doi.org/10.1093/qmath/45.4.515) | `T35R7A7N` / `IKS9JNK5` | Definition 1.1, Proposition 3.1 and Theorem 4.1. All 16 local pages were indexed; journal page equals PDF page plus 514. |
| W. Crawley-Boevey, *Lectures on Representations of Quivers*, [author's lecture notes](https://www.math.uni-bielefeld.de/~wcrawley/quivlecs.pdf) | `QXHYP74V` / `YFBJLCTT` | Supplementary reading route: path algebras, bricks and representation varieties. All 38 local pages were indexed. |

The Zotero Kirillov attachment (`HFSJIPFK` / `X2NWN3JH`) contains 310 PDF pages but only its first 100 pages were indexed. Later chapters were therefore read directly from the Literature PDF, rather than inferred from incomplete indexed text.

## Conventions checked across sources

- Semi-invariants use point-action covariance: `f(gx) = chi(g)^n f(x)`. For unframed King stability, `chi_theta = product det(g_k)^(theta_k)` and every subrepresentation has nonnegative theta-weight. Ginzburg's character parameter has the opposite sign. The notes state their convention before using it.
- The moment equation has incoming `B_a B_a*`, outgoing `-B_a* B_a`, and framing `+ij`. Kirillov's opposite framing sign is translated by replacing `j` with `-j`.
- The framing spaces are fixed; only the internal general linear groups are quotiented. The cyclic character in these conventions is the product of the internal determinants.
- Common scalar automorphisms in unframed King-stable representations are distinguished from the trivial stabilisers of framed cyclic data.
- The map from a projective GIT quotient to the full affine quotient is not assumed surjective or a resolution. The isolated-vertex case with internal and framing dimensions both two gives an explicit counterexample to surjectivity.
- Full dilation scales every arrow and framing map and makes the symplectic form have weight two. At zero moment level it gives the semiprojective action used here. Cotangent dilation is a separate action of weight one; the one-dimensional Jordan example shows that its fixed locus can be nonproper.
- The general Jordan identification with a Hilbert scheme uses the cited rank-one-framing theorem. The notes prove the smallest cases and the two-point chart directly. They do not transfer acyclic-quiver Lagrangian-fibre statements to the punctual Jordan fibre.
- The optional norm-balancing calculation establishes an orbit-set correspondence. Identifying induced complex structures is explicitly assigned to the reduction theorem.

## Review and validation

The main construction and explicit models were reviewed independently of their drafting. The review checked the semi-invariant sign, cyclic-stability argument, moment-map sign, dimension formula, cotangent transition functions, quadratic cone, nonsurjective example, Jordan matrix equations, two-point Hilbert chart, scaling actions and all fourteen worked exercise solutions. The two halves of the glossary were cross-reviewed, including the dimensions and framing hypotheses in every example.

The final document has 37 pages, 64 glossary definitions, 64 corresponding example entries and 128 examples. There are fourteen exercises with worked solutions. Appendix A starts on page 17, Appendix B on page 19 and Appendix C on page 26.

The source was compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build`. The final TeX log contains no warnings, undefined references or citations, or overfull/underfull boxes. `qpdf --check` passed. The PDF's named destinations were read from its object structure, all internal link destinations were resolved, and all 128 glossary/example destinations were checked against their expected pages and incoming links. PDFKit provided a separate link-resolution and text-extraction check. Representative pages were rendered for visual inspection.

Machine-readable results are in [glossary-and-build-validation.json](glossary-and-build-validation.json), [build/pdfkit-validation.json](build/pdfkit-validation.json) and [preservation-check.json](preservation-check.json). The checking scripts are retained in `build/`. Mathematical review, compilation checks and preservation checks have distinct scopes; none is a claim of an independent proof of every theorem quoted from the references.

## Preservation and delivery

All outputs were created in the new `quiver-varieties-notes-2026-11-13` directory. The SHA-256 hashes of all 163 pre-existing non-Git workspace files were rechecked, including the earlier stacks and Higgs notes. The full Literature inventory of 1,555 files was checked by path, size and modification time. The two textbook PDFs actually consulted were additionally content-hashed before and after reading and again at delivery. The entire Literature collection was not content-hashed. No protected input file was edited.

The source is standalone, with an internal bibliography and both glossaries. The delivery PDF matches the checked build PDF. [artifact-checksums.sha256](artifact-checksums.sha256) records checksums of the principal deliverables and validation records.
