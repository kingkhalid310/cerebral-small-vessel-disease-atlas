# Contributing

Thank you for helping improve the Cerebral Small Vessel Disease Evidence Atlas.

## Suitable contributions

- Correct a factual, citation, transcription, or broken-link error.
- Suggest a pivotal source with a stable identifier.
- Improve an evidence boundary or competing explanation.
- Propose a new research question, falsifier, or decisive study design.
- Improve accessibility, navigation, validation, or documentation.

## Not suitable

- Patient-specific advice or clinical records.
- Protected health information or unpublished identifiable data.
- Full-text copyrighted articles without redistribution permission.
- Promotional claims or diagnostic conclusions unsupported by an appropriate reference standard.

## Evidence contribution checklist

1. Give a DOI, PMID, PMCID, guideline URL, or other stable identifier.
2. State whether the record was assessed from full text, abstract, or citation only.
3. Separate the authors' result from your interpretation.
4. Name the population, index measure, comparator, reference standard, and outcome.
5. State the claim the source supports, qualifies, or challenges.
6. Identify major bias, transportability, and competing-pathology concerns.
7. Do not silently convert an association into diagnostic or causal evidence.

## Local checks

```bash
python3 scripts/build_site_data.py
python3 scripts/validate.py
python3 scripts/serve.py
```

Pull requests should explain what changed, why it changed, how it was checked, and whether the interpretation or only presentation changed.
