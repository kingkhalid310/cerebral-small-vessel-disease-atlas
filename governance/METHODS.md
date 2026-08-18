# Methods for the Living Evidence Map

## Purpose

This project is both a curriculum and a research evidence map. It is designed to help a learner understand the field while making the boundary between established knowledge, context-dependent diagnostic performance, and unresolved hypothesis inspectable.

## Current review status

Version 0.3 is a **question-driven curated scoping evidence system**. It is not represented as exhaustive, systematic, or ready for guideline development. It begins with the supplied Valentina and Johanna paper collections, the prior bibliography, and targeted updates for diagnostic transportability, physiology, inflammation, ARIA, genetics, biomarkers, and appraisal methods.

The maintained unit is now an answerable question with an explicit population, index test or exposure, comparator, reference standard, outcome, evidence status, current answer boundary, missing piece, and decisive next design.

## Search and screening

- Every search is recorded in `data/search_log.csv` with date, platform, exact query, scope, and limitations.
- Every candidate source receives a record in `data/screening_decisions.csv`.
- Duplicates are retained as local-file records but linked to one scholarly source.
- Reviews and consensus papers are included for orientation and citation chasing; they do not replace extraction of pivotal primary studies.
- Searches intended for publication should be rerun in bibliographic databases with librarian review and reported using PRISMA-ScR or PRISMA 2020 as appropriate.

## Unit of evidence

The preferred chain is:

`source -> study/cohort -> analysis/result -> claim relationship -> appraisal -> synthesis judgment`

A publication can contain more than one cohort or analysis. A result can support one claim while challenging another. The database therefore does not treat a paper as globally "positive" or "negative."

## Cohort independence

Publication count is not treated as replication count. Parent cohorts, nested subsets, consortium sites, participant overlap, recruitment context, and repeated secondary analyses are tracked in `cohorts.csv` and `study_cohorts.csv` before consistency is judged.

## Contradiction and falsification

Every central hypothesis must expose the strongest evidence for, strongest evidence against, plausible alternative explanations, a result that would materially weaken it, and the most decisive feasible experiment. Missing counterevidence is treated as incomplete review rather than agreement.

## Claim relationships

- `supports`: directly increases confidence in the claim.
- `challenges`: directly lowers confidence or demonstrates a counterexample.
- `qualifies`: supports only within a narrower population, context, or interpretation.
- `context`: informs the claim without directly testing it.
- `null`: reports no association relevant to the claim.
- `method`: defines how the construct is measured or classified.

## Appraisal

Diagnostic-accuracy studies are mapped to QUADAS-3 concepts: participant selection, index test, target condition/reference standard, flow and analysis, plus applicability. Prediction models are mapped to PROBAST concepts: participants, predictors, outcome, and analysis. Reviews, pathology studies, longitudinal cohorts, and experiments use design-specific prompts.

All current ratings are provisional single-reviewer judgments based on available text. Publishable reviews require independent duplicate assessment and adjudication.

## Confidence synthesis

Claim confidence is not determined by study design alone. Five dimensions are considered:

1. directness to the exact claim and intended population;
2. risk of bias and measurement validity;
3. consistency across independent data;
4. precision and information size;
5. transportability across populations, scanners, raters, and settings.

The operational rubric is in `CONFIDENCE_RUBRIC.md`.

## Updating

For a meaningful update:

1. add the source and resolve identifiers;
2. record screening status;
3. extract the study and result fields;
4. add all relevant claim relationships, including null or contradictory findings;
5. appraise bias and applicability;
6. reconsider—not automatically change—the claim confidence;
7. record the decision and date in the claim record and changelog;
8. regenerate and validate the reading edition.

## Interpretation guardrails

- STRIVE terms describe imaging phenomena; they do not assign pathology.
- Boston criteria estimate the likelihood of sporadic CAA in defined clinical contexts; they are not universal screening rules.
- A technically reproducible biomarker is not necessarily etiologically specific, clinically useful, or treatment-responsive.
- Pathology sampling is itself an imperfect reference because CAA and arteriolosclerosis are spatially heterogeneous.
- Mixed pathology is expected in older adults and should be modeled rather than treated only as exclusion.
- Absence of a marker from a radiology report is not equivalent to absence on the images.
