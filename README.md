# Cerebral Small Vessel Disease Evidence Atlas

[![Release](https://img.shields.io/badge/release-v0.6-173f35)](CHANGELOG.md)
[![Evidence records](https://img.shields.io/badge/evidence_records-67-426a5a)](data/source_registry.csv)
[![Research questions](https://img.shields.io/badge/research_questions-40-b07d35)](data/research_questions.csv)
[![Clinical use](https://img.shields.io/badge/clinical_use-educational_only-8c3d32)](DISCLAIMER.md)

An evidence-traceable, question-driven knowledge base for cerebral small vessel disease, with focused coverage of cerebral amyloid angiopathy (CAA), brain arteriolosclerosis, mixed pathology, diagnostic criteria, imaging markers, biomarkers, mechanisms, and unresolved research problems.

**Release:** v0.6 depth and coverage edition
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
| Learn the field in sequence | [Web-native 24-chapter course](https://csvd.medics-global.com/learn.html), [Word reading edition](downloads/Cerebral_Small_Vessel_Disease_Evidence_Guide_v0.6.docx), or [`content/guide/`](content/guide/) |
| Audit breadth and unfinished areas | [Topic coverage map](https://csvd.medics-global.com/coverage.html) or [`data/topics.csv`](data/topics.csv) |
| See the central unresolved problems | [`data/research_questions.csv`](data/research_questions.csv) |
| Inspect claim-level evidence | [`data/claims.csv`](data/claims.csv) and [`data/claim_evidence.csv`](data/claim_evidence.csv) |
| Compare diagnostic approaches | [`data/diagnostic_profiles.csv`](data/diagnostic_profiles.csv) |
| Test a hypothesis against falsifiers | [`data/hypotheses.csv`](data/hypotheses.csv) |
| Check cohort reuse before calling evidence independent | [`data/cohorts.csv`](data/cohorts.csv) and [`data/study_cohorts.csv`](data/study_cohorts.csv) |
| Explore the website locally | Run `python3 scripts/serve.py`, then open the printed address |
| Synchronize and validate all three views | Run `python3 scripts/sync_release.py` |

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

## One-source publishing workflow

The repository is the canonical editorial source. The website and Word guide are generated reading views; do not edit those outputs by hand.

1. Edit `content/guide/`, `data/`, or `governance/`.
2. Update `release/release.json` when the public version changes.
3. Run `python3 scripts/sync_release.py` to rebuild the catalog, course, figures, and Word guide; validate them; and write a hash manifest.
4. Run `python3 scripts/sync_release.py --check` before publishing to detect drift.
5. Preview with `python3 scripts/serve.py`, review the changes, then commit and deploy.

See [SYNCING.md](SYNCING.md) for ownership rules, review gates, and the release checklist.

The Word builder requires Pillow and python-docx. Install [`requirements-docs.txt`](requirements-docs.txt) in a local virtual environment when those packages are not already available.

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

v0.6 adds nine deep chapters, 72 transparent topic-coverage records, and point-of-claim source links while preserving synchronized publication across the repository, website, and Word guide. It remains a curated scoping knowledge base—not a systematic review, comprehensive textbook, or clinical decision system. See [ROADMAP_V0.6.md](ROADMAP_V0.6.md) for delivered scope and remaining work.
