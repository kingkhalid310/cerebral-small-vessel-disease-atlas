# Mixed Pathology and Cognitive Attribution

## Mixed disease is the default problem, not an exception

Older adults frequently have combinations of arteriolosclerosis, CAA, infarcts, Alzheimer disease neuropathologic change, LATE-NC, hippocampal sclerosis, Lewy body disease, and other lesions. A model that forces every MRI finding or cognitive outcome into one etiology can be easier to describe but biologically misleading [[R003]] [[R004]] [[R034]] [[R050]].

> Coexistence does not tell us whether pathologies are independent, share causes, interact, mediate one another, or merely accumulate in the same ageing brain.

## 1. Five relationships that are often conflated

### Co-occurrence

Two pathologies are present in the same person. This is descriptive and does not establish a causal relationship.

### Shared cause

Age, APOE, vascular risks, systemic inflammation, or other factors influence both pathologies. An observed association may weaken after appropriate control, but control must respect the causal structure.

### Mediation

One pathology or injury pathway lies between an exposure and an outcome. For example, vessel disease might influence cognition partly through infarcts and network disruption. Adjusting for a mediator can remove part of the effect one intends to estimate.

### Interaction

The joint effect differs from the sum or product expected under a chosen scale. Interaction must be defined statistically and biologically; saying diseases `synergize` without a specified contrast is not enough.

### Diagnostic contamination

One pathology produces an imaging or clinical feature conventionally attributed to another, reducing specificity. Lobar microbleed false positives and mixed hemorrhagic patterns are examples [[R015]].

## 2. CAA and Alzheimer disease

CAA and ADNC share amyloid-beta biology but differ in anatomical compartment. Amyloid PET can reflect both vascular and parenchymal fibrillar amyloid, limiting patient-level separation [[R032]] [[R059]]. CAA can contribute to cognition through vascular injury even when ADNC is present; conversely, cognitive decline in a person meeting imaging criteria for CAA should not automatically be assigned to CAA alone.

A useful analysis separates:

- Vascular amyloid burden and distribution.
- Parenchymal plaques and tau stage.
- Hemorrhagic and ischemic vascular lesions.
- White-matter and network injury.
- Cognitive domain and longitudinal trajectory.
- Reserve and demographic context.

## 3. Arteriolosclerosis, LATE-NC, and hippocampal sclerosis

Regional arteriolosclerosis has been associated with hippocampal sclerosis of ageing [[R033]], while modern LATE-NC staging emphasizes age-related TDP-43 pathology and its anatomical progression [[R034]]. Association could reflect local vascular vulnerability, common ageing processes, reverse influence, or selection. Cross-sectional autopsy data are powerful for anatomical relationships but limited for temporal direction.

Medial temporal lobe studies that combine vascular and proteinopathy measures can reveal spatial associations [[R035]] [[R050]]. A decisive design would include regional quantitative pathology, longitudinal cognition, antemortem MRI, short interval to death, and causal models prespecified before looking at results.

## 4. Why `adjusting for everything` is not a solution

Statistical adjustment can reduce confounding, block mediation, introduce collider bias, or amplify measurement error. The correct covariate set depends on the estimand.

### Example estimands

- **Total association:** How much does arteriolosclerosis burden predict cognitive decline, including paths through infarcts and WMH?
- **Direct association:** Is there an association remaining after specified tissue injuries?
- **Mediated pathway:** How much of the association may operate through infarcts or network disruption?
- **Predictive value:** Does adding arteriolosclerosis improve future cognitive prediction regardless of causal interpretation?

These are different questions. One regression table should not be interpreted as answering all four.

## 5. Cognition is a network outcome

cSVD can affect processing speed, executive function, attention, memory, and other domains through distributed disconnection, focal strategic lesions, impaired reserve, and interaction with neurodegeneration. The same total lesion volume can have different effects depending on location, network position, age, education, prior brain health, and co-pathology [[R029]] [[R066]].

VCING and VasCog-2-WSO provide structured approaches to vascular contribution and clinical classification [[R025]] [[R065]]. They should be used as operational frameworks, not as proof that vascular and neurodegenerative causes can always be cleanly separated.

## 6. Better study designs

### Longitudinal multimodal cohorts

Repeated MRI, cognition, vascular physiology, fluid biomarkers, and eventual neuropathology can establish temporal order better than one cross-sectional visit. Missingness and selective autopsy still require explicit handling.

### Regional analyses

Map regional vessel pathology to regional tissue injury and network change rather than reducing each disease to one global score. Spatial proximity can strengthen biological inference while raising multiple-comparison and registration challenges.

### Negative controls

Use outcomes, exposures, or regions that should not be related under the proposed mechanism. A model that predicts everything may be measuring general frailty, age, or data leakage.

### Interaction tests

Prespecify the scale, expected direction, and biological rationale. Report joint categories or marginal effects so the reader can see the data rather than relying only on a product-term p value.

### Competing causal models

Draw at least two plausible directed acyclic graphs before analysis. Identify which measurements would distinguish them and which arrows remain untestable.

## 7. A practical attribution worksheet

For any cognitive or functional outcome, record:

1. **Outcome:** domain, instrument, date, and trajectory.
2. **Vascular lesions:** infarcts, hemorrhages, WMH, microinfarcts, and network measures.
3. **Vessel pathologies:** CAA, arteriolosclerosis, and other vasculopathies.
4. **Neurodegenerative pathologies:** ADNC, LATE-NC, hippocampal sclerosis, Lewy bodies, and others.
5. **Temporal evidence:** what was known before decline and what was measured only at death.
6. **Shared causes:** age, genetics, vascular risks, systemic disease, and reserve.
7. **Candidate pathways:** direct, mediated, interactive, or diagnostic contamination.
8. **Residual uncertainty:** measurements and designs needed to adjudicate.

## 8. Claims that require special caution

- `Arteriolosclerosis independently causes dementia.` Independence depends on measured confounders, target definition, timing, and co-pathology.
- `CAA explains cognitive decline.` CAA may contribute, but attribution requires tissue injury and competing pathology assessment.
- `Mixed disease is worse than either alone.` This may be descriptively true while statistical interaction remains untested.
- `Adjusting for AD proves a vascular effect.` AD measures can be incomplete, mismeasured, or downstream of shared processes.
- `A composite score captures total disease.` Weighting and component overlap can conceal distinct pathways.

## 9. Research questions with high leverage

1. Which regional combinations of CAA and arteriolosclerosis best predict network disruption?
2. Do vascular pathologies accelerate tau or TDP-43 progression, or do shared ageing processes explain the association?
3. How much cognitive decline is mediated through microinfarcts, WMH progression, atrophy, and disconnection?
4. Which imaging measures add information after detailed neurodegenerative biomarkers?
5. Are observed interactions robust across community, memory-clinic, stroke, and autopsy cohorts?

## Verification and further study

- **Brain arteriolosclerosis and co-pathology:** [[R003]]
- **CAA and nonhemorrhagic disease:** [[R004]]
- **LATE-NC staging:** [[R034]]
- **Medial temporal vascular and proteinopathy relationships:** [[R050]]
- **VCING:** [[R025]]
- **VasCog-2-WSO:** [[R065]]
- **WSO vascular contribution to dementia statement:** [[R066]]

