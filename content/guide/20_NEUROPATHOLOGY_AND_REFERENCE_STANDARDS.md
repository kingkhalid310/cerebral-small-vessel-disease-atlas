# Neuropathology and Reference Standards: What Counts as Truth?

## Why the reference standard needs its own chapter

Imaging-biomarker papers often describe neuropathology as `ground truth`. That phrase is useful only if the target pathology is well defined, sampled in relevant regions, measured reproducibly, and temporally aligned with imaging. Human neuropathology is the most direct available evidence about vessel-wall disease, but it is still a measurement process with missing tissue, reader variation, ordinal scales, and selection [[R003]] [[R025]] [[R026]].

> Pathology is closer to the disease construct than MRI, but a limited tissue sample is not an error-free whole-brain label.

## 1. The diagnostic target must be explicit

A study can target at least four different things:

- Presence of any pathology.
- Moderate-to-severe pathology.
- Regional severity in a specified block.
- Person-level burden aggregated across several regions.

These targets have different prevalence and clinical meaning. Dichotomizing an ordinal score may simplify analysis while making performance highly dependent on the chosen threshold. A model trained on `moderate/severe versus none/mild` cannot be assumed to estimate the full continuous spectrum.

## 2. Brain arteriolosclerosis assessment

B-ASC ratings typically use ordinal assessment of arteriolar wall thickening or related changes in sampled regions. The comprehensive review demonstrates variation in terms, regions, and methods across cohorts [[R003]]. A high-quality record should include:

1. Regions sampled and number of blocks.
2. Vessel inclusion criteria.
3. Stains and magnification.
4. Features that define severity.
5. Number of vessels examined or sampling rule.
6. Reader number, training, and blinding.
7. Inter-rater and intra-rater statistics.
8. Regional and person-level aggregation.

Digital image analysis can provide continuous measurements and spatial maps, but training labels still inherit expert disagreement. Domain shift across staining, scanners, tissue preparation, and laboratories must be tested [[R016]].

## 3. CAA assessment

CAA assessment considers vascular amyloid in leptomeningeal and cortical vessels and may distinguish capillary involvement. Severity, anatomical distribution, and vasculopathic consequences should be separated. The consensus postmortem protocol was developed to improve sampling and reporting comparability [[R026]].

Important questions include:

- Was amyloid confirmed with immunohistochemistry or another validated stain?
- Were leptomeningeal, cortical, and capillary compartments evaluated?
- Was severity recorded by region?
- Were vessel-wall consequences such as fibrinoid change or inflammation documented?
- Was full autopsy available, or only a biopsy or hematoma specimen?

A small biopsy can confirm amyloid in sampled tissue but cannot reliably characterize whole-brain distribution or exclude disease elsewhere.

## 4. VCING and cognitive attribution

VCING provides a framework for estimating the likelihood that vascular pathology contributed to cognitive impairment [[R025]]. It deliberately concerns contribution rather than a single pure vascular dementia entity. Infarcts, vessel disease, and other pathologies must be evaluated together.

Even a standardized contribution framework does not fully solve mixed pathology. Cognitive reserve, lesion timing, network location, neurodegeneration, and terminal illness influence clinical expression. The goal is calibrated attribution, not forced exclusivity.

## 5. Sampling error

### Regional sampling

Small-vessel pathology can vary across lobes, deep nuclei, hippocampal regions, and white matter. Standard blocks improve comparability but cannot capture every vessel. A whole-brain MRI phenotype may therefore be compared with a sparse target.

### Lesion sampling

The vessel responsible for an MRI lesion may not be present in the sampled section. Conversely, pathology may be severe in a region without a visible conventional MRI lesion.

### Severity sampling

Using the maximum observed grade increases sensitivity to focal disease but depends heavily on which block happened to contain the worst vessel. Averaging can hide focal extremes. Both approaches should be justified.

## 6. Temporal mismatch

MRI may precede death by years. During that interval new infarcts, hemorrhages, WMH, amyloid deposition, arteriolar remodeling, and neurodegeneration can occur. The MRI-to-death interval should be reported as a distribution, included in sensitivity analyses, and considered in biological interpretation.

Very short intervals reduce mismatch but can introduce terminal-state effects or select acutely ill participants. There is no perfect interval; the important step is to define what the comparison can support.

## 7. Reader and laboratory variation

Ordinal ratings can disagree because criteria are underspecified, lesions are borderline, tissue quality differs, or readers apply thresholds differently. Reliability is not a nuisance statistic to place in supplementary material. It sets an upper bound on observable agreement with an imaging model.

Recommended reporting:

- Reader expertise and training set.
- Blinding to imaging, clinical data, and outcome.
- Number and selection of double-rated cases.
- Weighted kappa or intraclass correlation as appropriate.
- Adjudication procedure.
- Laboratory and staining batch.
- Missing and ungradable tissue.

## 8. Verification bias and spectrum bias

Only a selected subset of patients receives biopsy or autopsy. Patients with dramatic hemorrhage, unusual inflammation, research enrollment, long survival, or brain-donation consent may differ from the intended clinical population. Diagnostic accuracy in this selected spectrum can misrepresent performance in community, memory-clinic, or asymptomatic groups.

Boston v2.0 illustrates why development and community validation should be read together [[R006]] [[R051]] [[R052]]. The criterion did not change between studies; the people, presentation, disease spectrum, and reference distribution did.

## 9. Digital pathology as an opportunity and risk

Digitized slides make vessel-level annotation, continuous measurement, spatial analysis, and reproducible model development possible. Deep-learning work demonstrates strong marker detection under defined conditions [[R016]]. But external validity requires:

- Independent laboratories and scanners.
- Different tissue-processing and staining batches.
- Clearly defined human reference annotations.
- Error analysis by vessel size, region, artifact, and disease.
- Transparent model version and preprocessing.
- Calibration and uncertainty, not only area under the curve.
- Public or shareable benchmark data when governance permits.

## 10. Designing an MRI-pathology validation study

| Domain | Minimum requirement | Stronger design |
|---|---|---|
| Target | Prespecified pathology construct and threshold | Continuous and regional targets retained |
| Sampling | Named standard regions | MRI-guided lesion and control-region sampling |
| Timing | MRI-to-death interval reported | Short interval or longitudinal MRI with interval modeling |
| Blinding | Imaging and pathology readers separated | Fully independent pipelines and locked analysis |
| Reliability | A subset double-rated | Multilaboratory reproducibility study |
| Spectrum | Intended population defined | External validation in contrasting populations |
| Co-pathology | Major competing lesions measured | Prespecified causal and predictive models |
| Performance | Discrimination with uncertainty | Calibration, incremental value, and decision analysis |

## 11. What pathology can establish

Pathology can demonstrate the presence, location, and morphology of vessel and tissue lesions in sampled material. It can validate whether an imaging feature is associated with a target lesion and reveal false-positive imaging assumptions. It cannot, from one terminal cross-section alone, prove temporal order, whole-life mechanism, treatment responsiveness, or clinical utility.

## Verification and further study

- **Brain arteriolosclerosis methods and pathology:** [[R003]]
- **CAA postmortem consensus protocol:** [[R026]]
- **VCING contribution framework:** [[R025]]
- **Digital histopathology marker assessment:** [[R016]]
- **False-positive CAA lesion pathology:** [[R015]]
- **Boston v2.0 community validation:** [[R051]]

