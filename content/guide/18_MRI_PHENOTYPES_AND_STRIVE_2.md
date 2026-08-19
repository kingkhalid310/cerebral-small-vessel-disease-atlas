# MRI Phenotypes and STRIVE-2: Description Before Etiology

## What STRIVE-2 is for

STRIVE-2 is a consensus terminology and reporting framework for neuroimaging manifestations of cSVD. It updates STRIVE-1, incorporates advances since 2013, and highlights emerging quantitative and advanced imaging approaches [[R001]] [[R002]]. Its job is to make observations comparable. It does not diagnose CAA, arteriolosclerosis, or another etiology.

> A STRIVE label answers, "What does this look like on this acquisition?" Etiologic criteria answer, "How much does this pattern raise the probability of a disease in this population?" Those questions must remain separate.

## 1. Acquisition is part of the phenotype

Lesion visibility depends on field strength, sequence type, spatial resolution, slice thickness, echo time, susceptibility weighting, motion, artifacts, and post-processing. Counts obtained with T2*-GRE and SWI are not automatically interchangeable. DWI detects recent ischemia over a limited temporal window. FLAIR suppresses CSF to increase conspicuity of many white-matter lesions, but partial volume and artifacts remain.

Every reusable imaging record should specify at least:

- Scanner field strength and vendor when relevant.
- Sequence name and major parameters.
- Spatial resolution and slice thickness.
- Susceptibility sequence type.
- Availability and quality of T1, T2, FLAIR, DWI/ADC, and T2*-GRE or SWI.
- Rating or segmentation method and version.
- Reader training, blinding, and reliability.
- Missing or non-diagnostic sequences.

## 2. Recent small subcortical infarct

A recent small subcortical infarct is a neuroimaging lesion in the territory of a perforating arteriole, with imaging features or symptoms consistent with recent infarction. DWI is particularly important acutely. Size alone cannot establish mechanism; branch atheromatous disease, embolism, parent-artery disease, and other causes can produce small subcortical lesions.

Clinical lacunar syndromes and imaging-defined lesions overlap imperfectly. The ESO guideline emphasizes diagnostic uncertainty, clinical-imaging mismatch, acute treatment, progressive lacunar stroke, and secondary prevention [[R063]]. The imaging label should not silently become `lacunar mechanism`.

## 3. Lacune of presumed vascular origin

A lacune is a small, fluid-filled cavity in a typical subcortical location, interpreted as the healed result of a prior small subcortical infarct or hemorrhage. It usually has CSF-like signal with a surrounding FLAIR rim that may be incomplete. Enlarged perivascular spaces, old hemorrhage, cysts, and other cavities can mimic lacunes [[R001]].

For deep interpretation, record exact structure, maximum dimensions, shape, FLAIR rim, adjacency to vessels, and coexisting lesions. The phrase `presumed vascular origin` preserves uncertainty: imaging rarely reveals the exact vessel-wall pathology that caused the cavity.

## 4. White-matter hyperintensity of presumed vascular origin

WMH are hyperintense on T2-weighted and FLAIR images and not cavitated like CSF. They are common with ageing and vascular risks but heterogeneous in histology and cause. Periventricular and deep distributions, confluent versus punctate morphology, lesion progression, and spatial pattern may carry information.

Important mimics include demyelination, inflammation, genetic leukodystrophy, treatment-related change, edema, infection, and secondary degeneration. In a deep knowledge resource, `WMH` must never be used as shorthand for `ischemia`, `hypertension`, or `arteriolosclerosis` without additional evidence.

Visual scales are practical but threshold continuous biology. Automated segmentation provides volume and spatial maps but introduces algorithm, training-label, scanner, and QC dependencies [[R044]] [[R045]]. A model can produce a precise volume that is systematically wrong.

## 5. Perivascular spaces

PVS follow the course of penetrating vessels and are generally CSF-like on relevant sequences. They are commonly rated in basal ganglia and centrum semiovale. Visibility varies with acquisition and anatomy; small lacunes can mimic enlarged spaces; and cutoffs such as 2 or 3 mm are operational rather than biological boundaries [[R001]].

Distribution may alter etiologic probability, but severe PVS remain nonspecific. Pathology-linked regional evidence in CAA is important [[R012]], yet visible space burden is not a direct measurement of solute clearance.

## 6. Cerebral microbleeds

CMBs are small susceptibility signal voids caused by prior blood products, detected on T2*-weighted GRE or SWI. Mimics include vessels, calcification, iron deposition, bone-air interfaces, cavernous malformations, and artifacts. MARS and BOMBS improve structured rating and anatomical recording [[R023]] [[R024]].

Distribution is clinically and etiologically informative:

- Strictly lobar lesions raise the probability of CAA in an appropriate context.
- Deep or infratentorial lesions raise the probability of deep perforator arteriopathy.
- Mixed distributions may represent mixed pathology, severe one-process disease, or another cause.

These are probability statements. Lesion-level pathology demonstrates that a conventionally CAA-compatible pattern can contain false positives [[R015]].

## 7. Cortical superficial siderosis and convexity subarachnoid hemorrhage

cSS is linear susceptibility along cortical surfaces caused by chronic blood products. Acute convexity subarachnoid hemorrhage may be visible on CT, FLAIR, or susceptibility imaging depending on timing. Focal versus disseminated extent should be documented. cSS is strongly associated with CAA and recurrence risk, but prior trauma, surgery, vascular malformation, and other causes must be considered [[R030]] [[R047]].

## 8. Cerebral microinfarcts

Microinfarcts are primarily pathological lesions, many below conventional MRI resolution. A subset of cortical lesions can be detected with optimized high-resolution MRI, while DWI may reveal acute microscopic ischemic lesions. In-vivo visibility is selective, so absence on routine MRI does not indicate absence of pathology [[R001]] [[R004]].

## 9. Atrophy and secondary brain change

Atrophy is common and clinically relevant but weakly specific. It can reflect neurodegeneration, vascular injury, Wallerian degeneration, loss of tissue after infarction, ageing, or combinations. Total intracranial volume, segmentation method, region, and longitudinal interval must be reported when quantitative measures are used.

## 10. Diffusion and microstructural measures

Diffusion tensor measures, free water, PSMD, and related approaches can detect diffuse tissue abnormality outside visible WMH. Technical and biological validation in MarkVCID supports selected measures as research biomarkers [[R021]] [[R022]]. Interpretation still depends on preprocessing, motion, scanner, white-matter geometry, lesion masks, and the target construct.

Use the validation ladder:

1. Can the measure be computed reliably?
2. Is it repeatable across scans and sites?
3. Does it relate to the intended tissue process?
4. Does it predict a meaningful outcome?
5. Does it add information beyond conventional measures?
6. Is it responsive to an intervention?
7. Does changing it track clinical benefit?

## 11. Perfusion, CVR, permeability, and advanced susceptibility

Advanced MRI can measure vascular function before or beyond visible structural injury. ASL and contrast perfusion characterize delivery; BOLD or perfusion CVR characterizes vascular response; dynamic contrast methods estimate permeability; quantitative susceptibility can characterize iron and blood products. These approaches are promising but remain sensitive to physiology, protocol, modeling, and analysis [[R001]] [[R054]].

The phrase `early biomarker` should be reserved for a measure shown temporally before established injury in an appropriate longitudinal or hereditary model, not simply a sophisticated measure acquired in people with disease.

## 12. Total-burden scores

Total SVD and CAA-SVD scores summarize multiple visible markers [[R027]] [[R028]]. They are practical and often prognostic. Equal-weight scores impose assumptions: components may differ in reliability, prevalence, mechanism, and outcome association. A higher score describes greater composite burden; it does not identify etiology or prove that each one-point change is equivalent.

## 13. A reporting template

### Observation

State sequence quality, lesion type, number or extent, laterality, exact location, and uncertainty.

### Phenotype

Summarize the pattern using STRIVE-2 terminology and defined rating instruments.

### Differential

List compatible etiologies and important mimics; explain which features shift probability.

### Criteria

Apply a named diagnostic rule only if the population, qualifying presentation, sequences, and exclusions are satisfied.

### Residual uncertainty

State what additional imaging, longitudinal observation, pathology, genetics, or clinical information would discriminate among explanations.

## 14. Common interpretation errors

- Calling every WMH `ischemic`.
- Calling a deep microbleed `hypertensive` without differential reasoning.
- Calling a lobar microbleed `CAA` without considering mimics and context.
- Counting lesions across GRE and SWI as though sensitivity were identical.
- Treating PVS as direct clearance measurements.
- Treating a burden score as an etiologic classifier.
- Treating automated segmentation output as ground truth without QC.
- Inferring absence of microinfarcts from routine MRI.

## Verification and further study

- **STRIVE-2:** [[R001]]
- **STRIVE-1:** [[R002]]
- **Microbleed interpretation:** [[R046]]
- **MARS:** [[R023]]
- **BOMBS:** [[R024]]
- **Automatic WMH segmentation benchmark:** [[R045]]
- **Lacunar stroke guideline:** [[R063]]

