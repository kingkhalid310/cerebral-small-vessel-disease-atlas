# Biomarkers and Tools

## 1. A biomarker is defined by its context of use

A number is not "validated" in the abstract. It can be validated for one or more specific jobs:

- **susceptibility/risk:** identify people more likely to develop disease or an outcome;
- **diagnostic:** identify current disease or subtype;
- **prognostic:** predict course among people with disease;
- **monitoring:** track change over time;
- **predictive:** identify differential response or harm from an intervention;
- **pharmacodynamic/response:** show that a biological process changed after treatment;
- **trial enrichment/stratification:** select or balance participants.

Technical repeatability, association with cognition, pathology prediction, and treatment responsiveness are different validation layers.

## 2. ARTS: the arteriolosclerosis biomarker

### What it is

ARTS is a fully automated, containerized MRI-based classifier designed to output a score related to the likelihood of brain arteriolosclerosis. It combines:

- 3D T1-weighted MRI;
- T2-weighted FLAIR for WMH-related features;
- diffusion tensor imaging, including regional fractional-anisotropy information;
- age at MRI and sex.

The public package accepts DICOM (preferred by its documentation) or NIfTI and was distributed for Singularity-based execution on Linux/macOS and high-performance computing. Check the current package requirements before using Apptainer as a drop-in replacement.

### Development logic

ARTS was trained using ex vivo MRI and neuropathology, then translated to in vivo imaging. Its central scientific value is the attempt to learn a pathology-linked arteriolosclerosis signature rather than treating total WMH as if it were specific.

### Evidence to date

- The initial publication reported prediction of arteriolosclerosis, scan-rescan reproducibility, and association with two-year cognitive decline in nondemented older adults.
- MarkVCID instrumental validation reported extremely high inter-rater reliability, high test-retest repeatability, and strong inter-scanner reproducibility in the validation design.
- Clinical/biological validation linked higher baseline ARTS scores with worse baseline performance and faster decline in processing-speed/executive measures in independent cohorts.
- A later diverse cohort of 1,226 older adults linked higher ARTS with incident MCI, dementia, stroke, and several vascular risk factors, with heterogeneity across racial/ethnic groups.

### What ARTS does not yet justify

- It should not be called a definitive clinical diagnosis of arteriolosclerosis.
- Its output is not a direct image of the vessel wall.
- Validation in very old cohorts does not automatically generalize to midlife, rare genetic cSVD, unusual scanner/protocol distributions, or different disease spectra.
- Age and sex are inputs; fairness and transportability must be evaluated, not assumed.
- Association with outcomes does not prove that changing the ARTS score changes outcomes.
- The composite model can capture correlates of arteriolosclerosis, comorbid pathology, aging, or tissue consequences unless competing pathologies are explicitly tested.

### Access and reproducibility record

- Tool page: [NITRC ARTS biomarker](https://www.nitrc.org/projects/arts/)
- MarkVCID protocol/resources: [MarkVCID2 protocols](https://markvcid.partners.org/markvcid2-protocols-resources)
- Initial paper: [ARTS: a novel in-vivo classifier](https://pmc.ncbi.nlm.nih.gov/articles/PMC8329541/)
- Validation report: [ARTS instrumental and clinical validation](https://pmc.ncbi.nlm.nih.gov/articles/PMC11712721/)

For any ARTS analysis, preserve software version, container hash, input series identifiers, acquisition parameters, DICOM-to-NIfTI conversion provenance, all quality-control failures, demographic inputs, exclusions, and raw output before transformation.

## 3. MarkVCID biomarker kits

MarkVCID is an NIH-funded multisite program intended to move promising VCID biomarkers toward trial readiness using common protocols and staged instrumental, biological, and clinical validation.

Current major MRI/fluid kits include:

| Kit | Input | Output concept | Current intended use | Main cautions |
|---|---|---|---|---|
| ARTS | T1, FLAIR, DTI, age, sex | Arteriolosclerosis likelihood score | Susceptibility/risk and trial stratification | Transportability, age range, pathology overlap |
| PSMD | Preprocessed diffusion MRI | 95th minus 5th percentile width of skeletonized mean diffusivity | Diffuse white-matter injury/risk | Sensitive to diffusion QC, processing, CSF contamination; not etiologic |
| Free water | Diffusion MRI | Extracellular free-water fraction | Tissue injury/risk | Model and acquisition dependence; inflammation/atrophy can influence |
| Cerebrovascular reactivity | Controlled CO2/BOLD MRI | Vascular response to stimulus | Vascular dysfunction/target engagement candidate | Gas delivery, physiology, motion, site harmonization |
| WMH volume | T1 + FLAIR | Automated lesion volume | Vascular burden/enrichment | Algorithm/scanner/domain shift; low specificity |
| Plasma NfL | Plasma assay | Axonal injury marker | Risk stratification | General injury marker, not cSVD-specific |
| OCTA vessel skeleton density | Retinal OCT angiography | Retinal microvascular density | Candidate accessible microvascular marker | Device/segmentation dependence; brain specificity uncertain |

Resources: [MarkVCID consortium](https://markvcid.partners.org/), [MarkVCID1 results](https://markvcid.partners.org/markvcid1-results), and [MarkVCID2 protocols](https://markvcid.partners.org/markvcid2-protocols-resources).

## 4. CAA biomarkers

### Hemorrhagic MRI markers

Strictly lobar CMBs, cSS/cSAH, and lobar ICH are the most established clinical imaging signals. cSS extent is also prognostic for recurrent lobar ICH in CAA cohorts. Sequence sensitivity is a major confounder: SWI detects more lesions than many GRE protocols, and field strength/echo time affect counts.

### Non-hemorrhagic MRI markers

- severe centrum semiovale PVS;
- posterior or multispot WMH patterns;
- cortical microinfarcts;
- diffusion damage and PSMD;
- reduced structural-network efficiency;
- altered cerebrovascular reactivity;
- cortical thinning and atrophy;
- BBB permeability and vascular-function measures.

These markers may occur earlier or correlate more closely with cognition than microbleed count. Most lack the etiologic specificity to stand alone.

### Amyloid PET

Amyloid PET can be sensitive to cerebral amyloid but cannot readily separate vascular from parenchymal amyloid. A negative scan may be useful in selected diagnostic contexts; a positive scan is less specific because Alzheimer-type plaques are common. Tracer, reference region, partial-volume correction, disease stage, and coexisting AD must be modeled.

### CSF

Across studies, CAA is often associated with lower CSF Aβ40 and Aβ42, while tau patterns help distinguish or identify coexisting AD. Meta-analyses and newer cohorts support signal, but assay platforms, diagnostic reference standards, and overlap limit stand-alone use. CSF biomarkers are not part of Boston v2.0.

### Blood

Plasma proteomic, vascular-injury, inflammatory, Aβ, and APOE-related signatures are active research areas. Recent exploratory studies report candidate protein panels associated with lobar CMBs or neuropathologic CAA. These require independent, prospective, spectrum-appropriate replication and comparison against AD, arteriolosclerosis, renal function, age, and systemic vascular disease.

### Genetic information

- APOE ε4 is associated with CAA presence/amyloid deposition and capillary CAA.
- APOE ε2 is associated with severe vasculopathic/hemorrhagic manifestations in several cohorts.
- APP mutations cause hereditary CAA syndromes such as Dutch-type CAA; other genes/proteins cause rarer amyloid angiopathies.

Genetic association is not deterministic diagnosis in sporadic disease. Ancestry, allele frequency, selection, and treatment context matter.

## 5. Visual rating tools

| Tool | Measures | Recommended archive item |
|---|---|---|
| MARS | CMB certainty, count, and anatomy | Rating form, training cases, rater ID, sequence parameters |
| BOMBS | CMB presence/distribution with mimic guidance | Scale version, adjudication log |
| CHARTS | Anatomic features of cerebral hemorrhage on CT | Completed form and reader reliability |
| Fazekas | Periventricular and deep WMH severity | Both component scores, not only total |
| Scheltens | Regional WMH burden | Region-level values and total |
| Potter/Wardlaw PVS scales | PVS burden by region | Basal ganglia and centrum semiovale separately |
| cSS focal/disseminated and multifocality scales | Extent/distribution of superficial siderosis | Sulci/foci map, not only binary presence |

Rating forms and atlases should be versioned. Training examples should include mimics and uncertainty, not only textbook-positive cases.

## 6. Open and common computational tools

### WMH segmentation

- **LST-LGA/LPA:** SPM-based lesion growth/prediction algorithms; widely used, originally developed in multiple-sclerosis contexts and often adapted to aging WMH.
- **BIANCA:** FSL supervised classifier for white-matter hyperintensities; requires representative training labels and careful thresholding.
- **SAMSEG:** sequence-adaptive Bayesian segmentation in FreeSurfer; supports lesion segmentation in multimodal data.
- **WMH Segmentation Challenge containers:** standardized benchmark methods; benchmark rank does not guarantee transportability to a new cohort.
- **nnU-Net/custom U-Net pipelines:** powerful when trained and externally validated; susceptible to scanner and population domain shift.

For all automated WMH tools, perform blinded manual QC, record failure categories, assess small-lesion false positives, and compare performance across scanner, site, race/ethnicity, age, lesion burden, and co-pathology.

### Diffusion and microstructure

- **PSMD toolbox:** [miac-research/psmd](https://github.com/miac-research/psmd), using FSL/TBSS-based skeletonization and histogram analysis.
- **FSL diffusion tools:** TOPUP, EDDY, DTIFIT, and TBSS; acquisition-specific QC is essential.
- **Free-water models:** implementation and fitting choices vary; keep code/version and parameter maps.

### Microbleed detection

Automated CMB detectors are improving but face severe class imbalance and mimics from vessels, calcification, and susceptibility artifact. Evaluate lesion-level sensitivity and false positives per scan, not only voxel Dice or patient-level AUC. External validation on different SWI/GRE protocols is essential.

### Structural/network analysis

- **FreeSurfer:** cortical thickness, volume, and surface reconstruction.
- **FSL/ANTs:** registration, segmentation, and image processing.
- **MRtrix3:** tractography and structural connectomics.
- **QSIPrep/fMRIPrep-like reproducible pipelines:** useful for standardized preprocessing, but cSVD lesions can break assumptions and require lesion-aware QC.

### Digital pathology

The Perosa/Scherlek workflow trained separate deep-learning models for parenchymal Aβ plaques, vascular Aβ, iron/calcium, astrocytes, microglia, and fibrin extravasation. The key methodological lesson is to retain marker-specific outputs and expert QC rather than collapsing all staining into one pathology score.

Useful platforms include QuPath and slide-specific deep-learning frameworks. Cross-laboratory stain normalization, scanner differences, annotation policy, tissue folds, vessel-size definitions, and spatial registration to MRI are first-order problems.

## 7. Literature and evidence-archive tools

| Need | Tool class | Examples | Quality control |
|---|---|---|---|
| Citation library | Reference manager | Zotero, EndNote | Save DOI/PMID, tags, notes, lawful link, duplicate merge history |
| Biomedical search | Curated index | PubMed/MEDLINE, Embase | Store exact query, date, filters, and result count |
| Forward/backward citation search | Citation graph | OpenAlex, Web of Science, Scopus, Semantic Scholar | Verify metadata against DOI/publisher |
| Screening | Review platform | Rayyan, Covidence, ASReview | Export decisions and exclusion reasons |
| Living alerts | Automated search | PubMed/MyNCBI, Crossref/OpenAlex scripts | Deduplicate and manually triage |
| Reproducible extraction | Structured records | CSV/JSON + templates in this repository | Two-person review for high-stakes claims |

Discovery tools such as Connected Papers, ResearchRabbit, and Litmaps are useful for finding neighborhoods of papers but should not define completeness. Search strategy and eligibility rules should be documented independently.

## 8. Minimum tool-record schema

Every tool record should contain:

- name, version, owner, and stable URL;
- license and redistribution terms;
- intended context of use;
- required inputs and accepted formats;
- preprocessing and quality-control requirements;
- output definition and scale direction;
- training/development population;
- technical, biological, clinical, and external validation evidence;
- known failure modes and excluded populations;
- compute/runtime/container requirements;
- last verified date and maintainer status;
- primary citation and independent evaluations.

Use `templates/TOOL_RECORD_TEMPLATE.md` to add new entries.

## 9. A practical validation ladder

1. **Analytical validity:** does the measurement accurately quantify its intended signal on controlled data?
2. **Repeatability:** does it agree across raters and repeat scans?
3. **Reproducibility:** does it agree across scanners, sites, and implementations?
4. **Biological validity:** does it associate with tissue or a credible mechanistic reference?
5. **Clinical validity:** does it identify or predict a meaningful clinical state/outcome?
6. **Incremental validity:** does it add information beyond age, risk factors, and standard imaging?
7. **Transportability and fairness:** does it work in new sites, protocols, ancestries, ages, and comorbidity patterns?
8. **Responsiveness:** does it change over time or after an intervention in an interpretable way?
9. **Clinical utility:** does using it improve decisions or outcomes?

Most cSVD biomarkers have not completed the full ladder. That is not failure; it is the research map.
