# Introductory deformation and intersection theory

Start with [the 40-page PDF](deformation-intersection-introduction.pdf). The editable, standalone source is [deformation-intersection-introduction.tex](deformation-intersection-introduction.tex).

These notes assume Hartshorne, Chapters I–II, and elementary commutative algebra. Flatness, first-order deformations, normal cones, Chow groups, Chern classes and Gysin maps are introduced where needed. General theorems are identified as tools used without proof; their construction is not treated as prior knowledge.

The main route is:

1. Scheme-theoretic intersection, local length, tangency and flat families.
2. Dual numbers, embedded versus abstract first-order deformations, a hypersurface deformation calculation and an elementary lifting obstruction.
3. Conormal sheaves, regular embeddings, normal bundles and normal cones.
4. Ordinary and extended Rees algebras, saturation and deformation to the normal cone.
5. Blow-ups and the distinction between the open deformation and the full blow-up family.
6. Cycles, rational equivalence, Chern classes, specialization, ordinary and refined Gysin maps, excess intersection and self-intersection.
7. Connections with the ideal and weight filtrations appearing in semiprojective algebraic cutting.

Repeated toy models include two colliding points, the smoothing of a node, a doubled Cartier centre, the tangent cone of a node and a cusp, tangent plane curves, the blow-up of the plane, and exceptional self-intersection. Particular care is taken with nilpotent multiplicities, projective-bundle conventions, exceptional-divisor signs, and the distinction between a local multiplicity and a Chow class after pushforward to a nonproper space.

Section 22 contains **sixteen exercises with worked solutions**. The appendices provide:

- **Appendix A, pages 21–22:** conventions, tools used without proof, bibliography and a reading route through the available textbooks.
- **Appendix B, pages 23–29:** 64 glossary definitions and a notation table.
- **Appendix C, pages 30–40, “Examples Glossary”:** two examples for every glossary entry, giving 128 examples. Each definition links to its examples, and each example entry links back to its exact definition.

Readers primarily interested in deformation to the normal cone can begin with Section 3 on flatness, then Sections 7–14 on ideals, cones, Rees algebras and the two deformation spaces. Sections 15–20 explain how this leads to intersection theory. The infinitesimal introduction in Sections 4–6 is useful but is not a prerequisite for the Rees computations.

The principal local references are Fulton’s *Introduction to Intersection Theory in Algebraic Geometry* and *Intersection Theory*, Vakil’s 2004 class notes, and Sernesi’s *Deformations of Algebraic Schemes*. Local Zotero copies of Vakil and Hartshorne’s 2004 deformation lectures supply additional reference material. See [sources-and-validation.md](sources-and-validation.md) for precise locations and source checks.

Build with a standard TeX Live installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build deformation-intersection-introduction.tex
```

The bibliography and both glossaries are included in the source. No external bibliography, drafting JSON, Literature file or Zotero attachment is required to compile it. The new build PDF appears in `build/`; the PDF at the top level is the checked delivery copy.

The TeX log is clean. PDF structure and all 303 internal link annotations were checked, including the paired destinations of the 64 glossary entries. The explicit calculations and all sixteen exercise solutions received a mathematical review, and representative pages were rendered for visual inspection. These checks do not claim an independent proof audit of every general theorem cited from the references.

All outputs are confined to this new dated directory. The 198 pre-existing non-Git workspace files retain their SHA-256 hashes. The Literature inventory of 1,555 files retains its paths, sizes and modification times; the four textbook PDFs consulted also retain their SHA-256 hashes. No Literature files, earlier notes or manuscript files were edited.

Supporting records:

- [Source and validation record](sources-and-validation.md)
- [Glossary and PDF link validation](glossary-and-build-validation.json)
- [PDFKit check](build/pdfkit-validation.json)
- [Preservation check](preservation-check.json)
- [Delivery checksums](artifact-checksums.sha256)

The `build/` directory retains TeX output, drafting records, preview images and validation scripts. These are supporting materials rather than build dependencies of the standalone source.
