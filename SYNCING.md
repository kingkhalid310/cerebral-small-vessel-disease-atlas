# Keeping the document, repository, and website synchronized

## The publication contract

The three components are not three separately maintained products.

| Component | Role | Editing rule |
|---|---|---|
| GitHub repository | Canonical evidence and editorial source | Edit here |
| Word reading edition | Long-form, portable reading view | Generate; never hand-edit |
| Website | Navigable learning and evidence-exploration view | Generate chapter and catalog content; hand-edit only stable interface templates |

Canonical narrative lives in `content/guide/`. Structured sources, studies, claims, evidence edges, questions, tools, hypotheses, cohorts, profiles, and cases live in `data/`. Methods and interpretation rules live in `governance/`.

## Standard release procedure

1. Edit canonical Markdown, CSV, or governance files.
2. Update `release/release.json` if the version, date, chapter count, output name, or public URL changes.
3. Run `python3 scripts/sync_release.py`.
4. Inspect `release/sync_manifest.json` and the validation result.
5. Review the website locally with `python3 scripts/serve.py`.
6. Render and visually inspect the Word document when its content or builder changes.
7. Run `python3 scripts/sync_release.py --check` immediately before committing.
8. Commit the canonical changes and generated views together; tag the release; deploy `docs/`.

## What the synchronizer guarantees

- It rebuilds the searchable catalog, course chapters, figures, and Word reading edition.
- It runs relationship, completeness, link, public-boundary, figure, and output checks.
- It records SHA-256 hashes of canonical inputs and published outputs.
- Check mode fails if any tracked input or output differs from the last successful synchronized build.

It does not judge whether a scientific interpretation is correct, perform a systematic search, detect every retraction, or replace editorial review.

## Scientific review gates

Before release, confirm that:

- every material claim has supporting, qualifying, or challenging evidence;
- observation, candidate phenotype, biomarker, and diagnosis remain distinct;
- population, reference standard, and transportability limits are explicit;
- cohort reuse is not misrepresented as independent replication;
- uncertainty and contradictory evidence are visible;
- no protected data or redistributed copyrighted full text entered the public tree;
- the Word guide and website remain educational, not patient-specific decision support.

## Drift recovery

If `--check` fails, do not repair generated files manually. Review the changed canonical source, rerun the full synchronizer, inspect the resulting diff, and publish the rebuilt outputs together.
