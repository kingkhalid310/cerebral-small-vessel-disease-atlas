# Cerebral Small Vessel Disease Evidence Atlas

[![Release](https://img.shields.io/badge/release-v0.5-173f35)](CHANGELOG.md)
[![Evidence records](https://img.shields.io/badge/evidence_records-61-426a5a)](data/source_registry.csv)
[![Research questions](https://img.shields.io/badge/research_questions-40-b07d35)](data/research_questions.csv)
[![Clinical use](https://img.shields.io/badge/clinical_use-educational_only-8c3d32)](DISCLAIMER.md)

An evidence-traceable, question-driven knowledge base for cerebral small vessel disease, with focused coverage of cerebral amyloid angiopathy (CAA), brain arteriolosclerosis, mixed pathology, diagnostic criteria, imaging markers, biomarkers, mechanisms, and unresolved research problems.

**Release:** v0.5
**Status:** curated scoping knowledge base; not a systematic review or clinical decision-support system
**Website:** [csvd.medics-global.com](https://csvd.medics-global.com/)

## Why this repository exists

The cSVD literature is difficult to learn because the same imaging finding can reflect several disease processes, criteria often transport poorly outside their derivation setting, and multiple papers may reuse the same cohort. This repository makes those boundaries visible.

It is designed to answer five questions:

1. What does the field currently claim?
2. What evidence supports, qualifies, or challenges each claim?
3. Which observations are measurements, biomarkers, diagnostic evidence, or only candidate phenotypes?
4. Which major uncertainties could be resolved by a decisive study?
5. Where might a new researcher make a useful contribution?

## Start here

| If you want to... | Open... |
|---|---|
| Learn the field in sequence | [Web-native 11-chapter course](https://csvd.medics-global.com/learn.html) or [`content/guide/`](content/guide/) |
| See the central unresolved problems | [`data/research_questions.csv`](data/research_questions.csv) |
| Inspect claim-level evidence | [`data/claims.csv`](data/claims.csv) and [`data/claim_evidence.csv`](data/claim_evidence.csv) |
| Compare diagnostic approaches | [`data/diagnostic_profiles.csv`](data/diagnostic_profiles.csv) |
| Test a hypothesis against falsifiers | [`data/hypotheses.csv`](data/hypotheses.csv) |
| Check cohort reuse before calling evidence independent | [`data/cohorts.csv`](data/cohorts.csv) and [`data/study_cohorts.csv`](data/study_cohorts.csv) |
| Explore the website locally | Run `python3 scripts/serve.py`, then open the printed address |
| Validate an edited release | Run `python3 scripts/validate.py` |

## Repository map

```text
.
├── content/                 Human-readable records and learning modules
│   ├── guide/               Progressive field curriculum
│   ├── questions/           One page per maintained research question
│   ├── claims/              One page per evidence-traceable claim
│   ├── studies/             Structured pivotal-study cards
│   ├── tools/               Criteria, scales, and biomarker profiles
│   ├── hypotheses/          Predictions, challenges, falsifiers, experiments
│   ├── cohorts/             Cohort lineage and reuse records
│   ├── diagnostic-profiles/ Validation-chain assessments
│   └── cases/               Educational differential-reasoning cases
├── data/                    Maintainable CSV and JSON source of truth
├── docs/                    Zero-build searchable website for GitHub Pages
├── governance/              Methods, ontology, confidence, and review rules
├── schemas/                 Machine-checkable expectations
├── scripts/                 Standard-library build, validation, and preview tools
├── downloads/               Reading-edition document
└── domain/                  Custom-domain activation guide
```

## Evidence model

The atlas separates observations from conclusions:

```text
source → study → evidence edge → claim → research question
                  │             │
                  ├─ supports   ├─ confidence
                  ├─ qualifies  ├─ boundary conditions
                  ├─ challenges └─ decisive test
                  └─ method
```

An imaging pattern may generate a candidate phenotype without constituting validated diagnostic criteria. Association, repeatability, biological validity, diagnostic accuracy, incremental value, transportability, clinical utility, and treatment responsiveness are tracked as different evidentiary achievements.

## Editing workflow

1. Edit the CSV registries or Markdown records.
2. Run `python3 scripts/build_site_data.py` to regenerate the searchable catalog.
3. Run `python3 scripts/build_chapters.py` to regenerate the web-native course.
4. Run `python3 scripts/validate.py`.
5. Preview with `python3 scripts/serve.py`.
6. Commit only after reading the generated validation summary.

This workflow does **not** automate literature surveillance. Source discovery, screening, appraisal, and interpretation remain deliberate human editorial tasks.

## Public and clinical boundary

- No protected identifiers, patient-level data, unpublished cohort output, credentials, or redistributed copyrighted PDFs.
- The site is for research and education, not patient-specific diagnosis or treatment.
- Boston criteria, STRIVE terminology, ARTS, and other tools must be used within their stated population and validation limits.
- Report-derived features remain candidate phenotype signals until image-level and pathology-linked validation.

See [DISCLAIMER.md](DISCLAIMER.md), [governance/METHODS.md](governance/METHODS.md), and [governance/CONFIDENCE_RUBRIC.md](governance/CONFIDENCE_RUBRIC.md).

## Citation and reuse

Citation metadata are provided in [`CITATION.cff`](CITATION.cff). No reuse license has yet been granted; see [`LICENSE.md`](LICENSE.md). A content/code dual license should be selected before a public launch.

## Version history

v0.5 turns the repository edition into a learning product: web-native chapters, guided pathways, a diagnostic-methods workbench, and human-readable evidence pages. v0.4 remains available through the repository history and release tag.
