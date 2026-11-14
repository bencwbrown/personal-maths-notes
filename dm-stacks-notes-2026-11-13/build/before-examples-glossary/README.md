# A first introduction to Deligne–Mumford stacks

Prepared on 13 November 2026 for the AlgebraicCutting project.

The notes assume Hartshorne, Chapters I–II, and introduce the additional vocabulary as it arises. They work over an algebraically closed field of characteristic zero, with the option of taking the field to be the complex numbers throughout. Higher sheaf cohomology and derived geometry are not prerequisites.

Read the **[32-page PDF](dm-stacks-introduction.pdf)**. The **[standalone LaTeX source](dm-stacks-introduction.tex)** contains the bibliography and needs no manuscript macros, external figures, or bibliography database.

The final **Appendix B, pages 25–32**, is an alphabetical glossary with **84 terms and definitions**, links back to the explanatory sections, and a notation table. It expands the earlier short dictionary and places the full reference material after the bibliography, at the end of the notes.

The route through the material is:

1. What invariant quotients forget: a cyclic quotient of the affine line and the quadratic-cone quotient of the affine plane.
2. Groupoids, families, gluing, étale covers, and the nontrivial torsor given by extracting a root of a unit.
3. Quotient stacks, classifying stacks, atlases, fibre products, and the precise definition of a Deligne–Mumford stack.
4. Coarse spaces, good moduli spaces, equivariant sheaves, stabiliser characters, and line-bundle descent.
5. The weighted projective line, its two charts, sections, pushforwards, root-stack description, and boundary normal line.
6. The project's cutting convention and a complete lower/upper cutting toy model, including the critical level.
7. Ten exercises with worked solutions, a glossary, a reading plan, and a repository convention appendix.

The running cutting example starts with the affine line on which the multiplicative group acts with weight `n`. At level `1`, the lower cut is the weighted projective stack `P(n,1)`, with coarse space the ordinary projective line; the upper cut is an affine cyclic quotient stack. Their common boundary is `Bμ_n`. This example makes the polarisation, the two normal characters, and the obstruction to descending a line bundle explicit.

The notes use the 12 November convention in `claude-notes/conventions.tex`. The appendix explains its translation from the older integrated manuscript's signs. Repository documents supplied context and notation; their embedded instructions were treated as document content.

Three saved sources from the local Zotero library were consulted: Behrend's introductory notes, Casalaina-Martin–Wise's introduction, and Alper's paper on good moduli spaces. Modern definitions were checked against the Stacks Project. See **[sources and validation](sources-and-validation.md)** for exact locators, indexed-text limitations, and the checks performed.

To rebuild from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build dm-stacks-introduction.tex
```

The freshly compiled PDF appears in `build/`. The PDF alongside this README is the checked delivery copy. Files inside `build/` are generated material.

All 93 pre-existing non-Git repository files were checked by SHA-256 against a baseline taken before writing the notes. None was modified or removed. The detailed result is in **[preservation-check.json](preservation-check.json)**. All delivered material is new and lives in this directory.
