# T015: WMH segmentation algorithms

- **Category:** automated image analysis
- **Intended context:** Quantify WMH volume and spatial distribution
- **Target construct:** MRI-defined WMH
- **Required inputs:** FLAIR plus optional T1; algorithm-specific preprocessing
- **Output:** Masks, volume, spatial features

## Evidence and use

- **Development/authority:** Multiple research groups and challenges
- **Validation status:** Benchmark performance exists; external transport varies
- **Reference standard:** Expert masks and challenge datasets
- **Key strength:** Scalable continuous measurement
- **Failure mode:** Domain shift, lesion mimics, scanner effects, opaque QC
- **Clinical status:** Research; clinical use depends on product
- **Version/access:** Record model, weights, threshold, and QC
- **References:** R045
- **Reviewed:** 2026-08-18