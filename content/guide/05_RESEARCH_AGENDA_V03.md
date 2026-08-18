# Research Agenda: From Knowledge Gaps to Testable Projects

## 1. The highest-value missing link

The field has strong descriptions at three levels - autopsy vessel pathology, MRI lesion burden, and late clinical outcomes - but far fewer datasets connecting all three with temporal and spatial precision. The highest-value program is therefore:

> **Longitudinal, multimodal, regionally registered human phenotyping with eventual pathology, designed to distinguish CAA, arteriolosclerosis, and mixed disease before late irreversible lesions dominate.**

## 2. Ten priority research questions

1. Which physiology or molecular markers identify prehemorrhagic CAA with adequate specificity against AD and B-ASC?
2. Can B-ASC be divided into reproducible molecular/morphologic subtypes with different risk factors and outcomes?
3. Does barrier leakage spatially and temporally precede specific WMH, microinfarcts, or microbleeds?
4. Which PVS features reflect impaired clearance rather than atrophy or nonspecific aging?
5. Can cortical-ribbon versus juxtacortical CMB localization reduce false-positive CAA classification?
6. How do CAA and B-ASC interact when both are present: additive, synergistic, or regionally competitive?
7. Which cSVD markers explain cognitive decline independently of AD, LATE-NC, and brain reserve?
8. Are ARTS, PSMD, free water, and CVR responsive to intervention and predictive of meaningful benefit?
9. Which immune programs produce safe vascular Aβ clearance versus ARIA/CAA-ri-like injury?
10. How do biomarker performance and thresholds differ across ancestry, sex, age, scanner, and care setting?

## 3. Near-term projects using existing cohorts

### Project A: lesion-location refinement for lobar microbleeds

**Question:** Does exact depth relative to the cortical ribbon distinguish CAA-linked from arteriolosclerosis-linked lobar CMBs?

**Design:** rate CMB centroid and distance to gray-white junction on high-resolution SWI/QSM; compare with Boston category, ARTS, deep SVD markers, and pathology where available.

**Critical controls:** veins/calcification, sequence parameters, cortical atrophy, lesion size, susceptibility blooming, mixed pathology.

**Deliverable:** open operational localization rule plus lesion-level and patient-level accuracy.

### Project B: pathology-aware WMH phenotyping

**Question:** Which WMH morphology and microstructure distinguish CAA, B-ASC, and mixed disease?

**Design:** combine spatial WMH maps, multispot features, PSMD/free water, perfusion/CVR, ARTS, and neuropathology severity using nested cross-validation and held-out sites.

**Avoid:** training on Boston labels and then claiming pathology specificity without tissue validation.

### Project C: B-ASC regional heterogeneity

**Question:** Is occipital white-matter arteriolosclerosis representative of frontal, temporal, hippocampal, basal-ganglia, and brainstem disease?

**Design:** multiregion morphometry and cell/matrix markers; estimate within-brain heterogeneity and the number of regions needed for stable classification.

**Deliverable:** sampling recommendation and uncertainty interval for a whole-brain B-ASC estimate.

### Project D: mixed-pathology cognitive models

**Question:** How much longitudinal cognitive variance is uniquely and jointly explained by CAA, B-ASC, ADNC, LATE-NC, infarcts, and network integrity?

**Design:** hierarchical models with domain-specific slopes, age/time-to-death, education/reserve, scanner, and selection weights. Predefine interactions and avoid stepwise significance fishing.

### Project E: ARTS transportability audit

**Question:** Does ARTS preserve calibration and prognostic value across age, ancestry, sex, vascular-risk burden, scanner vendor, field strength, and AD co-pathology?

**Design:** locked-container external validation with calibration plots, decision curves, subgroup uncertainty, failure audit, and comparisons against age/sex, WMH alone, and PSMD.

## 4. Medium-term prospective studies

### A preclinical CAA observatory

Recruit hereditary CAA carriers and sporadic high-risk participants without symptomatic hemorrhage. Repeat:

- SWI/QSM and high-resolution structural MRI;
- DTI/free water/PSMD;
- CVR, perfusion, pulsatility, and permeability;
- amyloid/tau PET when justified;
- plasma and CSF Aβ species, inflammatory and vascular markers;
- sleep, blood pressure, gait, and sensitive cognition;
- retinal/OCTA markers.

The analysis should test a preregistered temporal graph based on the four-stage CAA framework. Record treatment and anti-amyloid exposure.

### A living MRI-autopsy bridge

Enroll participants with consent for brain donation. Maintain acquisition consistency, obtain last-life MRI where feasible, scan intact fixed hemispheres, identify lesions ex vivo, sample them with 3D registration, and serially reconstruct culprit vessels. Include lesion-negative control regions and non-CAA controls.

## 5. Experimental studies that would translate

- Manipulate arterial pulsatility separately from mean pressure in models with human-like vascular amyloid.
- Test whether restoring smooth-muscle contractility improves Aβ clearance without increasing rupture.
- Perturb barrier pathways at defined CAA stages and measure both clearance and hemorrhage.
- Compare immune-cell states during successful Aβ removal versus destructive remodeling.
- Use human induced pluripotent stem cell vascular units with APOE and APP genotypes, while acknowledging the absence of aged 3D anatomy.
- Validate model findings in spatial human pathology before calling them therapeutic targets.

## 6. Measurement priorities

### Harmonization

- minimum MRI sequences and metadata;
- STRIVE-compliant definitions;
- lesion-rating training sets with mimics;
- common neuropathology blocks and vessel-size definitions;
- shared stain and digital-pathology QC;
- prospective recording of missingness and image failure.

### Continuous measures with interpretable anchors

Retain lesion counts, volumes, spatial maps, and quantitative tissue measures rather than only ordinal categories. Use categories for clinical interpretability, not as the only stored data.

### Negative controls

- control brain regions not predicted by the mechanism;
- imaging markers with similar technical behavior but different biology;
- outcomes outside the proposed pathway;
- non-CAA amyloid and non-amyloid cSVD comparator groups.

## 7. Causal-inference discipline

Before a mediation or causal model, draw the proposed graph. Include:

- age and survival to imaging/autopsy;
- hypertension, diabetes, kidney disease, smoking, and medications;
- APOE/ancestry and socioeconomic exposures;
- ADNC, LATE-NC, Lewy body disease, and macrovascular disease;
- scanner/sequence and segmentation quality;
- clinical referral and brain-donation selection;
- time between imaging, symptoms, death, and tissue sampling.

Do not adjust automatically for downstream lesions or colliders. Report total and direct-effect estimands separately when appropriate.

## 8. Data and software architecture for the future repository

### Public layer

- Markdown concept pages and evidence maps;
- citation metadata and lawful links;
- deidentified aggregate examples or openly licensed images;
- protocol checklists and tool records;
- versioned code and synthetic test data.

### Restricted layer

- protected clinical data and identifiers;
- original copyrighted PDFs without redistribution rights;
- raw images and pathology slides under data-use agreements;
- crosswalks and linkage keys.

Never make the public website depend on access to the restricted layer. Generate public aggregate outputs through a documented release process.

## 9. Proposed website information architecture

The future site should have four linked entry routes: **Foundations** (anatomy, physiology, and STRIVE imaging markers); **Diseases** (CAA, arteriolosclerosis, and other cSVDs); **Research reasoning** (criteria, phenotypes, debates, hypotheses, methods, and tools); and an **Evidence library** (papers, claims, cohorts, datasets, and protocols).

Each hypothesis page should display supporting, constraining, and null evidence side by side. Each criterion page should show intended population, required inputs, reference standard, performance, exclusions, and common misuses.

## 10. Definition of success

This knowledge base succeeds if a reader can:

- explain why imaging phenotype and vessel pathology are different layers;
- apply and critique Boston/Edinburgh/STRIVE concepts correctly;
- state what ARTS measures and what remains unvalidated;
- describe competing clearance, barrier, inflammatory, and vascular-function hypotheses;
- identify mixed pathology and spectrum bias in a paper;
- turn a broad claim into a discriminating, spatially and temporally explicit study.

