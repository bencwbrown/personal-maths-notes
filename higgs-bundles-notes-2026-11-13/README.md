# A first introduction to Higgs bundles

Prepared on 13 November 2026 as a companion to the introductory stack notes.

**[Read the notes — PDF, 36 pages](higgs-bundles-introduction.pdf)**, or use the **[standalone LaTeX source](higgs-bundles-introduction.tex)**.

The notes assume familiarity with Hartshorne, Chapters I–II, and **no prior study of moduli spaces of vector bundles**. They introduce vector bundles on curves, degree, subbundles, slope stability, families, and S-equivalence before asking the reader to work with Higgs moduli. The particular curve-cohomology and deformation results needed later are stated explicitly as tools used without proof.

The route through the material is:

1. Canonical bundles and the needed curve formulas.
2. Vector bundles, determinant degree, saturation, and slope stability.
3. Families and moduli, starting with line bundles and matrix conjugacy.
4. Extensions, Jordan–Hölder factors, and S-equivalence.
5. Higgs fields, invariant subbundles, and Higgs stability.
6. Rank-one, elliptic Jordan, theta-characteristic, and twisted projective-line examples.
7. The Hitchin map and spectral curves, with an explicit companion-matrix calculation.
8. The cotangent open, scaling, nilpotent limits, and the connection to semiprojective geometry.
9. A short optional outlook on connections and nonabelian Hodge theory.
10. Twelve exercises with worked solutions.

The running rank-two pair uses a square root `S² = K_C` and the matrix with rows `(0,q)` and `(1,0)`. It is stable even though its underlying bundle is unstable. The same pair supplies a concrete spectral equation and a scaling limit with a nonzero nilpotent Higgs field. These calculations explain several distinctions that matter in Higgs geometry and in possible cutting applications.

The appendices are:

- **Appendix A**, starting on page 18: tools used without proof and a route through books in the Literature folder.
- **Appendix B, pages 20–25**: an alphabetical glossary of **64 terms and definitions**, section references, and a notation table.
- **Appendix C, pages 26–36, “Examples Glossary”**: **two simple examples for each entry, 128 examples in total**. Each examples heading links to its definition, and every definition links forward to its examples.

Sources include five textbooks read in place in the Literature folder, three saved Zotero PDFs, and primary author/publisher references. Exact source locations, qualifications, and validation are recorded in **[sources-and-validation.md](sources-and-validation.md)**.

To rebuild from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build higgs-bundles-introduction.tex
```

The source contains the glossary, examples, and bibliography directly; it needs no separate JSON files, manuscript macros, bibliography database, or external figures. The freshly compiled PDF appears in `build/`; the PDF alongside this README is the checked delivery copy.

Existing repository files, including the stack notes, were left unchanged. The Literature folder was used only for reading. The preservation record checks all 136 pre-existing non-Git repository files by SHA-256, inventories all 1,543 Literature files by path/size/modification time, and additionally verifies SHA-256 for the five consulted textbook PDFs. See **[preservation-check.json](preservation-check.json)** and **[glossary-and-build-validation.json](glossary-and-build-validation.json)**.
