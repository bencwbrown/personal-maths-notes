# Local Zotero and primary-source ledger

Read-only research for deformation/intersection notes, 14 November 2026. The already-enabled local Zotero API was initially blocked by the sandbox; a read-only escalation succeeded. No preferences, Zotero records, attachments or Literature files were written. All extracts, previews and scripts were written under `/private/tmp/deformation-zotero-20261114`.

## Sources actually read

1. Ravi Vakil, *Intersection Theory Class 14*, 8 November 2004.
   - Zotero item `U9Z8JKTN`, attachment `VYVNNVDF`.
   - Local PDF `/Users/Benjamin/Zotero/storage/VYVNNVDF/Vakil - INTERSECTION THEORY CLASS 14.pdf`.
   - Complete indexed coverage: 6/6 pages. Printed page = PDF page.
   - §3 and §3.1 pp3–5: deformation to normal cone via blowing up `Y×P1` along `X×0`, special fibre `Bl_XY ∪ P(C_XY⊕1)`, intersection `P(C_XY)`; remove `Bl_XY` to obtain open deformation.
   - §4 pp5–6: specialization `σ:A_k(Y)→A_k(C_XY)`; cycle formula `[V]↦[C_{V∩X}V]` with scheme-theoretic intersection.
   - §4.1 p6: regular-embedding Gysin by specialization followed by inverse vector-bundle pullback, self-intersection.
   - §4.2 p6: diagonal construction of intersection products on smooth varieties, with no properness assumption on the variety.
   - Inspected actual local page images pp4,5,6. Source warning: p4 says the effective exceptional divisor has class `O_Proj(1)`. Correct convention is `O(-E)=O_Proj(1)`, hence `O(E)|_E=O_E(-1)`. Do not copy the sign typo. Text also contains a typographical misdescription of the boundary of `P(C⊕1)`.
   - Verified author-hosted primary URL: https://math.stanford.edu/~vakil/245/245class14.pdf .

2. Ravi Vakil, *Intersection Theory Class* compilation.
   - Zotero item `B79FDMWA`, attachment `HWGBH2VT`.
   - Local PDF `/Users/Benjamin/Zotero/storage/HWGBH2VT/Vakil - INTERSECTION THEORY CLASS.pdf`.
   - Indexed coverage 100/113 pages; only statements within those pages were used.
   - Class14 is PDF pages68–73, equivalent to the complete standalone above.
   - Class17, §1.1, printed pp2–3 = compilation PDF86–87: refined Gysin, compatibility and cone inclusion after arbitrary base change.
   - Class17, §1.2, printed p4 = compilation PDF88: excess normal bundle and excess intersection, self-intersection as special case. Inspected actual PDF88 image.
   - Class17 is dated 17 November 2004. Verified primary URL https://math.stanford.edu/~vakil/245/245class17.pdf .
   - Source typo: excess bundle rank is `e=d−d′`; printed p4 calls it `d=d−d′` in one line, while formula correctly uses `c_e`.

3. Robin Hartshorne, *Lectures on Deformation Theory*, Math274, Berkeley, 2004 lecture notes.
   - Zotero item `YTYGKD7U`, attachment `LNMLVE7Q`.
   - Local PDF `/Users/Benjamin/Zotero/storage/LNMLVE7Q/math274root.pdf`.
   - Indexed coverage 100/169 pages. Do not identify this attachment with the later 2010 published textbook; its numbering is the 2004 notes.
   - Main printed page n = PDF page n+6.
   - §2, printed p5/PDF11, Corollary2.2: a dual-numbers module M is flat iff multiplication by ε induces an injection M/εM→M.
   - Proposition2.3, printed pp6–7/PDF12–13: embedded affine first-order deformations correspond to Hom_B(I,B/I), with ideal-construction proof. Normal-sheaf definition pp7–8.
   - Theorem2.4, printed p8/PDF14: global embedded first-order deformations correspond to H0(Y,N_Y/X). Inspected actual local PDF11–14 images (Theorem2.4 confirmed directly).
   - Theorem1.1, printed pp1–3/PDF7–9: Hilbert tangent/obstruction discussion under smooth projective hypotheses; use if needed as optional preview only, since cohomology is beyond the requested background.
   - Theorem5.5, printed p29/PDF35: smooth abstract first-order deformations classified by H1(T), again optional and explicitly beyond assumed prerequisites.
   - Verified author-hosted primary URL https://math.berkeley.edu/~robin/math274root.pdf .
   - The preface explicitly calls these rough lecture notes with inconsistent numbering between sections, so retain exact local edition/date and verify context.

4. Luca Battistella, Francesca Carocci, Cristina Manolache, *Virtual Classes for the Working Mathematician*, SIGMA16 (2020),026,38pages.
   - Zotero item `7X8MMT7K`, attachment `BZMIUV9U`.
   - Local PDF `/Users/Benjamin/Zotero/storage/BZMIUV9U/Mathematikon, Germany et al. - 2020 - Virtual Classes for the Working Mathematician.pdf`.
   - Complete index39/39 pages, including one repository-cover page. Printed article page n = PDF n+1.
   - §3 printed pp3–6/PDF4–7: definition and examples of normal cones; §3.2 cone inclusion under arbitrary base change.
   - §3.3 printed p6/PDF7: deformation to normal cone, flat family and open/blowup distinction.
   - §3.4 printed p6 onwards: Segre class with projective completion and first Chern powers.
   - Used as a supplementary check/read-on source; do not use virtual obstruction theory as prerequisite for the elementary notes. Bibliographic creator metadata has malformed affiliation entries: use the actual three authors listed above.
   - DOI https://doi.org/10.3842/SIGMA.2020.026 .

## Primary Stacks Project references verified online

- https://stacks.math.columbia.edu/tag/062Z : conormal algebra, Sym(I/I²)→gr_I, normal cone, base-change surjection and flat-base-change isomorphism. Current section31.20; stable tag preferred to mutable section number.
- https://stacks.math.columbia.edu/tag/0638 : regular immersions. Noetherian equivalences; regular immersion implies locally free conormal sheaf and Sym→gr isomorphism; flat base change preserves regularity. Current section31.22.
- https://stacks.math.columbia.edu/tag/0FEZ : Gysin maps for local complete intersection morphisms, factorization independence and compatibility. Current section42.59.

Stacks terminology caveat: its conventions allow 'vector bundle' for Spec Sym of a sheaf not necessarily finite locally free. For these introductory notes, reserve honest vector-bundle terminology for finite locally free sheaves and explain the general normal cone without suggesting all fibres are vector spaces.

## Sources discovered but not used as authorities

- Attachment `P7D4GLK2`, `/Users/Benjamin/Zotero/storage/P7D4GLK2/Intersection_Theory.pdf`, is a 54-page student transcription of Barbara Fantechi's Chennai lectures, January2014. Its preface warns it is unrevised and may contain mistakes. Metadata/search inspection and opening text were used to identify it; main claims should instead cite Fulton/Vakil/Stacks.
- User-authored or user-stored DNC attachments titled *Affine DNC (Fulton's Notation)* (`6QJNRW2E`), *DNC Projective Deformation Algebraic Cut* (`NSGB64QE`) and *... (Complete)* (`R9HGPZX4`) were found in metadata but not used as authoritative source or instructions.
- No Zotero book record titled *Intersection Theory* by Fulton was found in the metadata search; use the separate Literature source if available.

## Suggested reading route

Hartshorne2004 §2 first (flatness over dual numbers and embedded deformations), then the new notes' cone/Rees computations, then Vakil Class14 §3 for the geometric blowup picture and §4 for specialization. Read Vakil Class17 §§1.1–1.2 after learning Chow groups and Chern classes. Fulton remains the reference for the complete theory; the virtual-class survey is later optional reading.
