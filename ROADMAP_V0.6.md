# v0.6 roadmap: the Learning Graph edition

## Product thesis

v0.6 should turn the atlas from a strong linear course plus evidence library into a research-learning environment. A reader should be able to enter at a concept, criterion, observation, paper, claim, controversy, or open question and see how it connects to the rest of the field.

The intended users are new laboratory members, neurology and neuroradiology trainees, cSVD researchers crossing into an unfamiliar subfield, research coordinators, and methodologists. It remains an educational and research resource, not a clinical decision system.

## The core learning loop

Every major chapter should support three modes:

1. **Learn:** prerequisites, learning objectives, first-principles explanation, annotated diagrams, essential vocabulary, and a short core reading set.
2. **Test:** retrieval questions, image-free reasoning cases, misconception checks, and explanations for every answer.
3. **Investigate:** linked claims, conflicting evidence, study and cohort lineage, unresolved questions, falsifiers, and a research-design exercise.

Readers should be able to move progressively from beginner summaries to advanced methodological detail without losing their place.

## Eight major capabilities

### 1. Interactive concept graph

Connect vessel segment, pathology, mechanism, tissue injury, imaging observation, clinical phenotype, diagnostic rule, biomarker, study, claim, and open question. Each relationship must have a plain-language meaning and traceable evidence; the graph must not imply causality merely because two nodes are connected.

### 2. Claim dossiers

Give every maintained claim a page containing the precise proposition, supporting and challenging evidence, population and reference standard, effect estimates when available, limitations, confidence by evidence dimension, boundary conditions, decisive experiment, and revision history.

### 3. Criteria and biomarker deep dives

Build structured learning modules for STRIVE-2, Boston criteria v2.0, CAA-related inflammation criteria, ARIA frameworks, and ARTS. Each module should distinguish purpose, input, output, derivation population, reference standard, validation state, dangerous misuse, and what would be needed for transport.

### 4. Disease and mixed-pathology models

Create deep modules for CAA, non-amyloid arteriolosclerosis, and mixed pathology. Compare convergent and divergent mechanisms without forcing all observations into a single-disease label.

### 5. Paper reading room

Create one readable card per prioritized paper: question, design, sample, exposure/index test, reference standard, result, bias risks, what the paper changed, what it did not establish, connected claims, cohort lineage, and recommended reading order. Link to lawful publisher, DOI, PubMed, or open-access locations rather than redistributing PDFs.

### 6. Educational diagnostic-reasoning lab

Use fictional or fully public aggregate scenarios to practice observation-first reasoning: describe the finding, identify competing explanations, select discriminating evidence, apply criteria within scope, and state residual uncertainty. Do not output patient diagnoses or treatment advice.

### 7. Research workbench

Provide a question builder, PECO/PICO canvas, hypothesis-falsifier template, validation-chain planner, cohort-independence checker, transportability checklist, and study-design comparison. Allow local export to Markdown or CSV, with no server-side storage and no protected data.

### 8. Personal learning layer

Add device-local completion, bookmarks, private notes, confidence ratings, spaced retrieval prompts, and a visual mastery map. Make storage behavior explicit and provide reset/export controls.

## Minimum content target

- 15 complete Learn–Test–Investigate chapter experiences.
- 5 criteria or biomarker deep dives.
- 3 disease or mixed-pathology models.
- 24 claim dossiers and 21 pivotal-study cards upgraded from tables to explanatory pages.
- 40 individually navigable research-question dossiers.
- One interactive concept graph and one research-gap radar.
- At least 30 misconception checks and 15 reasoning exercises.
- A glossary with synonyms, abbreviations, and links to the concepts where each term matters.

These targets deepen the current curated corpus; they do not imply comprehensive coverage of the entire literature.

## Evidence maturity model

For each tool or claim, show separate status for technical performance, repeatability, biological validity, diagnostic accuracy, prognostic association, incremental value, transportability, clinical utility, and treatment responsiveness. Avoid collapsing these into one score.

## Release sequence

### v0.6-alpha: learning skeleton

Define the content schemas, concept ontology, page templates, glossary, prerequisite map, and the Learn–Test–Investigate structure. Convert three representative chapters before scaling.

### v0.6-beta: connected evidence

Complete claim dossiers, study cards, concept links, criteria comparisons, question dossiers, cohort-lineage views, and contradiction displays. Conduct scientific and usability review.

### v0.6: research-learning release

Complete all chapter experiences, assessments, local learning tools, accessibility checks, mobile and performance testing, Word parity, synchronization checks, and a versioned editorial sign-off.

## Quality gates

- A domain expert can trace every important conclusion to evidence and limitations.
- A beginner can explain the observation-versus-etiology distinction after the first module.
- A trainee cannot complete a criteria exercise without seeing its population and reference-standard limits.
- A researcher can find contradictory evidence and cohort reuse without opening raw CSV files.
- Keyboard-only and screen-reader navigation cover the entire learning path.
- Generated document, repository records, and website display the same release manifest.
- No automatic literature ingestion, fabricated citation, patient-specific output, or protected data is introduced.

## Explicit non-goals for v0.6

- No autonomous literature updating.
- No diagnostic or treatment recommendations for individual patients.
- No risk calculator presented as validated without external validation and governance.
- No LLM-generated scientific claims entering the public evidence base without human verification.
- No copyrighted full-text archive.
