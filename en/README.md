# claude-wind-engineering-skills (English)

Claude skills for wind engineering: wind loads on buildings from CFD (LES) and comparison with wind tunnel tests.

## Sources

| Short name | Document | Coverage in the skills |
|---|---|---|
| CWE | ASCE, *Prestandard for Use of Computational Wind Engineering in Building Design* | All of Chapters 1–10 |
| ASCE 49 | ASCE/SEI 49-21, *Wind Tunnel Testing for Buildings and Other Structures* | Chapters 1–8 and commentary (C1–C8) |

The skills are summaries of these documents; no text is copied and they do not replace the documents. Every criterion is given with its clause number and PDF page number; for binding work, consult the original.

**Disclaimer.** This repository is not affiliated with ASCE and does not contain the text of the documents. The summaries were prepared with AI assistance and may contain errors; for design decisions the original documents govern. The summaries and scripts are released under the MIT license; copyright in the ASCE documents belongs to ASCE.

## Structure

```
skills/
  process/      scope of the CWE Prestandard, two-step process, target wind definition
  simulation/   empty domain verification, computational domain, mesh, boundary conditions
  loads/        pressure coefficients, peak values, design loads
  quality/      quality assurance, report content, peer review
  wind-tunnel/  ASCE 49: approach flow, model and surroundings, measurement and loads
  helpers/      calculation script (blockage, cutoff frequency, empty domain check, peak)
  experience/   mistakes made on one project (not a summary of a standard)
```

Each skill folder contains:

- `SKILL.md`: when to use, step-by-step path, mandatory requirements, checklist, common mistakes.
- `reference.md`: clause-by-clause table (clause, type, summary, numerical criterion, PDF page) and a list of what could not be found in the text.

Type column: **MANDATORY** ("shall" in the document), **RECOMMENDED** ("should"), **COMMENTARY**.

For the list of skills see [SKILLS_INVENTORY.md](SKILLS_INVENTORY.md).

## Installation

To use the skills in Claude Code, copy the skill folders under `skills` into your personal or project skills folder (without the category folders, each skill under its own name):

```
~/.claude/skills/<skill-name>/SKILL.md          (all projects)
<project>/.claude/skills/<skill-name>/SKILL.md  (that project only)
```

The calculation script needs Python 3 and `numpy`.

## Known gaps

- **Equations.** Most equations came out garbled when text was extracted from the PDFs. Those whose structure could be read with confidence are written as plain text; the others are marked as unreadable in the `reference.md` files. No coefficient was invented. To be checked by eye against the originals: CWE Equations 3-1, 3-4, 3-8…3-13, 3-16…3-19, 5-1…5-3, 6-3…6-6, 7-1…7-6.
- **Figures.** The content of the figures could not be read (CWE Figure 2-1 flowchart, 4-1 incident location sketch; ASCE 49 Figures 1-1, C2-1…C2-3, C6-1).
- **Lower limit of the mesh refinement ratio r** (CWE §6.6.4) reads the same as the ideal value in the extracted text; a symbol may have been lost.
- **CWE Table 8-1**: the rows for Chapters 3–5 were taken from the table headings; the thresholds are in the skill for the relevant chapter.
- After writing, the skills were not checked line by line against each other; only the format (front matter, name, files present) was checked for all, and one skill was reviewed for content.
- The English version is a translation of the Turkish version and was not separately checked against the original documents.

## Two points the documents do not state outright

- **CWE, incident location:** with explicitly modeled surroundings, the incident location is the location of the most upwind building of the study region, not the location of the study building (§1.8, PO 5-3, AC 6-7).
- **ASCE 49, where the profile is measured:** the standard does not say where in plan the approach flow profile is measured in the tunnel, or whether the proximity model is in place during the measurement. This has to be obtained from each wind tunnel report.
