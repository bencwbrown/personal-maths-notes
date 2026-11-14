# Introductory notes on quiver varieties

Start with [the compiled PDF](quiver-varieties-introduction.pdf). The editable, standalone source is [quiver-varieties-introduction.tex](quiver-varieties-introduction.tex).

These 37-page notes assume the algebraic geometry of Hartshorne, Chapters I–II, together with elementary linear algebra. They introduce representation theory, invariant quotients, stability, cotangent geometry and moment maps as needed. Prior study of moduli spaces, geometric invariant theory or symplectic geometry is not assumed.

The main route is:

1. Quivers, representations, subrepresentations, changes of basis and orbit closures.
2. Affine invariant quotients, character semi-invariants, relative Proj and King stability.
3. Framing, doubled arrows, the moment-map equations and cyclic stability.
4. Nakajima quiver varieties, their dimension and the descended symplectic form.
5. Explicit models: the Kronecker projective space, cotangent Grassmannians, the two charts of the cotangent bundle of the projective line, the quadratic cone, the Jordan quiver and the two-point Hilbert scheme.
6. Stability variation, moment-level deformations and scaling actions, followed by connections with stacks, Higgs bundles and semiprojective algebraic cutting.

Section 19 gives fourteen exercises with worked solutions. Appendix A (pages 17–18) records conventions, the tools used without proof and a source-specific reading route. Appendix B (pages 19–25) contains 64 glossary definitions and a notation table. Appendix C, **Examples Glossary** (pages 26–37), supplies two examples for each definition: 128 examples in total. Every definition links to its examples, and each example entry links back to the exact definition.

The principal textbooks consulted directly in the read-only Literature folder were Alexander Kirillov Jr., *Quiver Representations and Quiver Varieties*, and Hiraku Nakajima, *Lectures on Hilbert Schemes of Points on Surfaces*. Local Zotero articles by Ginzburg, Nakajima and King supplement them. Appendix A explains the sign translations between sources. Full source locations and checks are recorded in [sources-and-validation.md](sources-and-validation.md).

Build from this directory with a standard TeX Live installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build quiver-varieties-introduction.tex
```

The source includes its bibliography and both glossaries; no external bibliography, drafting JSON or Literature file is required to compile it. The newly compiled PDF is written to `build/`; the PDF at the top level is the checked delivery copy.

Compilation, PDF integrity and all internal PDF link destinations were checked. The explicit models and exercise solutions received a separate mathematical review. These checks do not constitute an independent proof audit of every general theorem cited from the literature.

All files created for this task are inside this new notes directory. The 163 pre-existing workspace files have unchanged SHA-256 hashes. The Literature inventory of 1,555 files has unchanged paths, sizes and modification times; the two textbook PDFs consulted also have unchanged SHA-256 hashes. See [preservation-check.json](preservation-check.json) for the scope and results. No prior manuscript, stack notes, Higgs notes or Literature files were edited.

Supporting records:

- [Glossary and PDF link validation](glossary-and-build-validation.json)
- [PDFKit validation](build/pdfkit-validation.json)
- [Delivery checksums](artifact-checksums.sha256)

The `build/` directory also contains TeX output, preview images, drafting records and the scripts used for validation. They are not required for reading or rebuilding the notes.
