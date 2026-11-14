# Sources and validation

Date: 13 November 2026.

This record accompanies a new introductory document. It separates the assumed background, consulted sources, explicit calculations, cited deeper results, mathematical review, and mechanical checks. The research manuscript and the earlier stack notes were not revised.

## Reader level and scope

The assumed background is Hartshorne I–II, with no previous course on moduli of vector bundles. Riemann–Roch, curve Serre duality, the cohomological classification of extensions, Picard varieties, the projective-line splitting theorem, moduli existence, spectral correspondence, and properness are identified as tools used without proof. Nonabelian Hodge theory is an optional outlook, with degree-zero and polystability hypotheses retained.

The notes work with ordinary `GL(r)` Higgs bundles on smooth projective complex curves, with explicit statements when a different twisting line is used. General smoothness/dimension and semiprojective claims are restricted to the indicated genus and coprimality setting. The semistable GIT quotient classifies S-equivalence classes; the stable locus has the geometric-classifying coarse interpretation.

## Textbooks read in the Literature folder

These files were read in place. All extraction and compiler caches were written outside the Literature folder.

**J. Le Potier, *Lectures on Vector Bundles* (1997).**

Local file: `/Users/Benjamin/Literature/Algebraic & Complex Geometry/J. le Potier/Lectures on Vector Bundles (80)/Lectures on Vector Bundles - J. le Potier.pdf`.

The saved PDF has 261 pages. In the checked main text, PDF page = printed page + 10. Consulted: Part I, Chapter 1, printed pp. 7–16; Chapter 2, pp. 17–36; Theorem 2.5.1, printed p. 28 / PDF p. 38, for Serre duality; §5.3, Definition 5.3.1, printed p. 73 / PDF p. 83, for semistability. Chapters 7–8, starting at printed pp. 105 and 121, supply the later moduli route. This is the principal curve-specific textbook companion.

**D. Huybrechts and M. Lehn, *The Geometry of Moduli Spaces of Sheaves*, second edition (2010).**

Local file: `/Users/Benjamin/Literature/Algebraic & Complex Geometry/Daniel Huybrechts/The Geometry of Moduli Spaces of Sheaves (67)/The Geometry of Moduli Spaces of Sheaves - Daniel Huybrechts.pdf`.

The PDF has 343 pages; main-text PDF page = printed page + 18. Checked: Definition 1.1.5, printed p. 4 / PDF p. 22, saturation; Example 1.1.16, p. 9 / PDF p. 27, torsion-free sheaves on a smooth curve; Example 1.2.10, p. 13 / PDF p. 31, a stable nonsplit extension; Definitions 1.2.11–12, p. 14 / PDF p. 32, degree and slope; Definition 1.5.3, p. 24 / PDF p. 42, S-equivalence; Theorem 4.3.4, p. 102 / PDF p. 120, projective semistable moduli. This is used for precise statements, rather than as an assumed prerequisite.

**P. E. Newstead, *Introduction to Moduli Problems and Orbit Spaces* (1978; saved reprint 2012).**

Local file: `/Users/Benjamin/Literature/Algebraic & Complex Geometry/Peter E. Newstead/Introduction to Moduli Problems and Orbit Spaces (74)/Introduction to Moduli Problems and Orbit - Peter E. Newstead.pdf`.

The PDF has 164 pages, with reprint pagination and older marginal pagination. Main printed p. 13 = PDF p. 23. Checked route: Chapter 1, printed pp. 13–22, families and moduli; Chapter 2, pp. 23–34, endomorphisms as a moduli model; Chapter 5, starting p. 99, bundles over curves, with locally universal families at p. 106 and quotient/fine-moduli discussions at pp. 113 and 117. It motivates the early family-and-matrix approach.

**R. Hartshorne, *Algebraic Geometry*.**

Local file: `/Users/Benjamin/Literature/Algebraic & Complex Geometry/Robin Hartshorne/Algebraic Geometry (34)/Algebraic Geometry - Robin Hartshorne.pdf`.

The searchable saved PDF has 513 pages. Checked main-text page offset is approximately +16. III §7, especially Corollary 7.12 and its remarks, printed p. 246 / PDF p. 262, supports the curve-duality/genus toolkit. IV §1, Theorem 1.3, printed p. 295 / PDF p. 311, is the Riemann–Roch reference. These chapters are later-study references; their needed statements are supplied in the notes.

**S. Donaldson, *Riemann Surfaces* (2011).**

Local file: `/Users/Benjamin/Literature/Algebraic & Complex Geometry/Simon Donaldson/Riemann Surfaces (6)/Riemann Surfaces - Simon Donaldson.pdf`.

The PDF has 301 pages; main-text PDF page = printed page + 15. Checked: §8.2, printed pp. 115–117, Riemann–Roch; §12.1.2, pp. 182 onward, local-product/transition descriptions of bundles; §12.2, pp. 196 onward, Jacobians and Abel–Jacobi. It is an optional analytic companion. The source review did not identify a precise theta-characteristic existence locator here, so it is not presented as the sole source for that fact.

Miranda's *Algebraic Curves and Riemann Surfaces* is available, but the saved copy has essentially no usable text layer. It was not relied on for precise locators.

## Local Zotero sources

| Source | Item / attachment | Verified coverage and use |
|---|---|---|
| Casalaina-Martin–Wise, *An introduction to moduli stacks, with a view towards Higgs bundles on algebraic curves* (2017) | `M7ZYQQVN` / `EFK3ZA2P` | Saved 147-page PDF, first 100 pages indexed. §§7.5–8.2, printed pp. 49–61, are within that coverage: twisted pairs, the S-equivalence quotient, characteristic coefficients, spectral finite algebras, and the torsion-free spectral-sheaf qualification. |
| Hausel–Rodríguez-Villegas, *Cohomology of large semiprojective hyperkähler varieties*, Astérisque 370 (2015), 113–156 | `VTWH4FT2` / `M8ZHT74R` | All 46 PDF pages indexed. Definition 1.1.1, printed p. 115 = PDF p. 5, defines the action-based semiprojectivity condition. Higgs example, printed p. 116 = PDF p. 6, gives the coprime smooth case, proper Hitchin map, and semiprojective scaling. Publication year is 2015; the saved filename's 2018 date is not used as publication metadata. |
| Rayan–Schaposnik, *Higgs bundles without geometry*, Snapshots of Modern Mathematics from Oberwolfach 8/2020 | `F8N5CQ9V` / `IP33UQRD` | All 10 pages indexed. Used for the matrix/eigenvalue motivation. The notes independently distinguish conjugacy from characteristic invariants and restrict line-bundle spectral statements to smooth integral covers. |

The corresponding saved PDFs are:

- `/Users/Benjamin/Zotero/storage/EFK3ZA2P/Casalaina-Martin and Wise - 2017 - An introduction to moduli stacks, with a view towards Higgs bundles on algebraic curves.pdf`
- `/Users/Benjamin/Zotero/storage/M8ZHT74R/Hausel and Villegas - 2018 - Cohomology of large semiprojective hyperkähler varieties.pdf`
- `/Users/Benjamin/Zotero/storage/IP33UQRD/Rayan and Schaposnik - 2020 - Higgs bundles without geometry.pdf`

No Zotero records were imported or modified.

## Primary online references and citation scope

- [Schaposnik, *An introduction to spectral data for Higgs bundles*](https://arxiv.org/abs/1408.0333): checked introductory definitions and stability on printed pp. 2–4 / PDF pp. 3–5; dimension and cotangent-open discussion on printed p. 4; spectral degree formula in Exercise 4, printed p. 6 / PDF p. 7. The notes give the explicit local spectral calculation and explain the hypotheses.
- [Schaposnik, *Advanced topics in gauge theory: mathematics and physics of Higgs bundles*](https://arxiv.org/abs/1907.09800): §2.1 supports the basic examples and theta-characteristic construction. Used in the independent toy-model review.
- [Wentworth, *Higgs bundles and local systems on Riemann surfaces*](https://www.math.umd.edu/~raw/papers/barcelona.pdf), version 29 March 2015: Theorem 2.15, p. 13, properness; Theorem 2.17, p. 14, the metric correspondence; Theorem 3.17, p. 33, the topological correspondence. Its principal fixed-determinant/traceless conventions are distinguished from the unrestricted `GL(r)` convention of these notes.
- [Nitsure, *Moduli space of semistable pairs on a curve*](https://doi.org/10.1112/plms/s3-62.2.275): bibliography checked; the construction and Theorem 5.10, p. 290, were consulted through Casalaina-Martin–Wise §7.7. The original full paper was not retrieved here, and the notes say that the construction is cited through that account.
- [Simpson, *Higgs bundles and local systems*](https://www.numdam.org/item/PMIHES_1992__75__5_0/): original general reference for the optional degree-zero correspondence; bibliographic metadata checked. A full reading of this paper is not claimed.

## Mathematical review

The core and both glossary/example groups received separate read-only mathematical reviews. The examples were calculated explicitly, rather than copied from a source. Checks included:

- Saturation and the subbundle convention.
- The degree-one nonsplit extension and the coprimality argument.
- Geometric isomorphism classes versus S-equivalence and polystable representatives.
- The Higgs transition rule and its absence of a derivative term.
- Ordinary versus twisted projective-line examples, and semistable versus stable examples.
- Theta-field entry types, all-parameter stability, and the nonzero scaling limit.
- The companion matrix, spectral genus, and spectral degree shift.
- The cotangent-open description and its difference from the cotangent bundle of the curve.
- Properness and action-based semiprojectivity without identifying the Hitchin map with the affinisation map.
- Degree zero, polystability, semisimplicity, and the type of identification in the optional nonabelian Hodge statement.
- All 12 exercise solutions and all 64 paired glossary entries.

Incorporated clarifications include the sign `a1 = -trace`, explicit rigidification in the fine-moduli example, the genus restriction in the simple-branch rank-two spectral discussion, and the distinction between proper scheme-theoretic fibres and their underlying reduced varieties. The definition of unstable is “not semistable”; in particular, the ordinary projective-line discussion does not incorrectly exclude its strictly semistable examples.

This review is not formal proof verification or a certification of the research manuscript. General moduli and analytic theorems are cited results used without proof, separate from the elementary computations.

## Mechanical checks and preservation

The source compiles using `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build higgs-bundles-introduction.tex`. The final PDF has **36 pages**, with no LaTeX warnings, unresolved references or citations, duplicate labels, overfull boxes, or underfull boxes. It passes `qpdf --check`.

Appendix B starts on page 20, Appendix C on page 26. All **64 definitions** and **64 examples entries** are present, with **128 numbered examples**. All **128 named PDF destinations** for those entries are verified against their LaTeX labels and destination pages, with incoming links in both directions. The detailed result is in `glossary-and-build-validation.json`.

The PDF was also opened with macOS PDFKit. Its text was extractable without replacement characters. All 282 internal link annotations resolved, and the other 8 link annotations were external URLs. Selected rendered pages covering the title/contents, Higgs definition and diagram, theta stability example, spectral construction, scaling limit, glossary, and Examples Glossary were inspected during build review.

The earlier repository files were hashed before writing. `preservation-check.json` records **136 pre-existing non-Git repository files checked by SHA-256**, including the stack notes. The Literature folder was inventoried by path, size, and modification time for all **1,543 files**. The **five consulted textbook PDFs** were additionally hashed before/after source consultation and checked again for delivery. This distinguishes full content verification of the consulted PDFs from metadata comparison of the whole 23 GB collection. The Literature folder and its files were not edited.

All authored files and generated build outputs are in the new `higgs-bundles-notes-2026-11-13` directory. No textbooks or saved article PDFs are copied into the deliverable.
