# Third Phase: VAE Evaluation and Explainable AI

## 1. Overview

The Third Phase of the PBMC VAE Explainability Project focuses on evaluating the learned latent representations of a Variational Autoencoder (VAE) and interpreting gene-level contributions using Explainable Artificial Intelligence (XAI).

Following the preparation of the PBMC single-cell RNA-seq dataset and training of the PyTorch VAE, this phase investigates what the model has learned and how reliably its latent representations can be interpreted.

Two complementary explainability approaches were used:

- SHAP (SHapley Additive exPlanations)
- Integrated Gradients (IG)

The analyses include latent-space evaluation, gene-level attribution, marker-gene association analysis, baseline sensitivity, attribution completeness, SHAP additivity and expression-matched statistical testing.

The overall objective is to investigate the interpretability and reliability of VAE-derived representations in single-cell transcriptomic data.

## 2. Dataset and Model Context

The analysis uses the processed PBMC single-cell RNA-seq dataset established in the earlier project phases.

| Dataset characteristic | Configuration |
|---|---:|
| Dataset | PBMC 3k |
| Cells | 2,638 |
| Selected genes | 2,006 |
| Training cells | 2,110 |
| Test cells | 528 |
| Model | Variational Autoencoder |
| Framework | PyTorch |
| Latent dimensions | 16 |
| Random seed | 42 |

The trained VAE produces a 16-dimensional latent representation for each cell.

Seven latent dimensions were selected for the principal explainability analyses:

- latent_2
- latent_5
- latent_7
- latent_9
- latent_14
- latent_15
- latent_16

These dimensions were identified as the most active dimensions during the preceding model evaluation.

The original model architecture and training configuration are documented in the preceding PyTorch VAE training phase.

## 3. Third Phase Objectives

The principal objectives were:

1. Evaluate VAE latent-space performance against PCA.
2. Investigate latent dimension activity and clustering characteristics.
3. Examine global latent-dimension and marker-gene associations.
4. Investigate within-cell-type marker-gene correlations.
5. Apply SHAP to identify influential genes in the learned latent representations.
6. Apply Integrated Gradients using zero and mean-expression baselines.
7. Compare gene attribution rankings across explainability methods.
8. Investigate attribution completeness and SHAP additivity.
9. Evaluate the sensitivity of Integrated Gradients to baseline selection.
10. Investigate enrichment of known cell-type marker genes using expression-matched null testing.

## 4. Computational Methodology

### 4.1 PCA and VAE Latent-Space Evaluation

PCA and VAE latent representations were compared using silhouette scores to investigate their ability to separate annotated cell populations.

The evaluation included:

- PCA using 16 components.
- VAE using all 16 latent dimensions.
- VAE using the seven selected active dimensions.
- PCA using seven components.

The comparison was conducted to establish whether the nonlinear VAE representation provided improved cell-type separation relative to the conventional PCA representation.

### 4.2 Global and Within-Cell-Type Marker Associations

Associations between latent dimensions and established marker genes were investigated using correlation analysis.

The analysis included:

- Global latent-marker correlations.
- Multiple-testing correction using false discovery rate procedures.
- Within-cell-type marker correlations.
- Cell-type-specific correlation heatmaps.

The within-cell-type analysis covered six cell populations, 16 latent dimensions and 12 marker genes, producing 1,152 association records.

These analyses provide complementary perspectives on marker relationships across the overall dataset and within individual cell populations.

### 4.3 SHAP Explainability

SHAP was applied to investigate the contribution of individual genes to the VAE latent representations.

The final SHAP analysis used the 528 test cells and 2,006 genes across the 16 latent dimensions.

Two independent SHAP runs were performed using different random seeds:

- Seed 0
- Seed 1

The resulting attribution values were used to calculate gene-level importance rankings.

The analysis included:

- Mean absolute SHAP values.
- Mean signed SHAP values.
- Attribution variability.
- Gene rankings for individual latent dimensions.
- Top-20 gene comparisons.
- Ranking stability between independent runs.

The final SHAP attribution arrays are stored separately for the two seeds.

### 4.4 Integrated Gradients Explainability

Integrated Gradients was used to estimate gene-level contributions to individual latent dimensions.

Two baseline configurations were investigated.

**Zero-expression baseline**

A zero-valued baseline was used to calculate gene-level attributions relative to the zero-expression reference.

**Mean-expression baseline**

The mean gene-expression profile calculated from the training cells was used as the reference baseline.

The comparison was designed to investigate whether gene attribution rankings were sensitive to baseline selection.

The analyses were restricted to the seven active latent dimensions for the principal comparisons.

### 4.5 SHAP and Integrated Gradients Comparison

The two explainability methods were compared using:

- Spearman rank correlation.
- Top-20 gene overlap.
- Shared gene identification.
- Marker-gene ranking comparisons.

The comparisons were used to investigate agreement between the gene rankings generated by different attribution approaches.

The mean-baseline IG versus SHAP comparison covered all 2,006 genes in each of the seven active dimensions.

### 4.6 Attribution Completeness and SHAP Additivity

Attribution reliability was investigated using completeness and additivity checks.

For Integrated Gradients, completeness errors were evaluated for both zero and mean-expression baselines.

For SHAP, additivity errors were examined across the two independent seeds.

The final SHAP validation included 32 records across the original 16 latent dimensions and both seeds. The seven active dimensions contributed 14 records to the principal analysis.

A 5% mean-error-to-output-standard-deviation criterion was retained for the SHAP additivity assessment.

The criterion was not relaxed to obtain a more favourable result.

### 4.7 Baseline Sensitivity Analysis

The two Integrated Gradients baseline configurations were compared using:

- Full gene-ranking Spearman correlations.
- Top-20 gene overlap.
- Marker-gene rank comparisons.

This analysis investigated whether the interpretation of individual latent dimensions changed depending on the reference baseline.

### 4.8 Expression-Matched Marker Enrichment

Known PBMC cell-type marker genes were used to investigate the representation of established marker genes within the attribution rankings.

The marker panel included:

| Cell population | Marker genes |
|---|---|
| B cells | CD79A, MS4A1 |
| NK cells | NKG7, GNLY |
| Monocytes | LYZ, CST3 |
| T cells | CD3D, CD3E, CD3G, IL7R, CD8A, CCR7 |

Expression-matched null testing was used to compare observed marker-gene hits against expectations from genes with similar expression characteristics.

The analysis investigated:

- SHAP and IG rankings.
- The complete 12-marker panel.
- The six markers represented in the selected HVG dataset.
- Top-10, top-20 and top-50 gene rankings.
- Pair-count and distinct-marker-count outcomes.

Empirical p-values were adjusted using the Benjamini-Hochberg false discovery rate procedure across 24 comparisons.

The significance threshold was set at 0.05.

## 5. Results

### 5.1 PCA versus VAE Evaluation

The silhouette comparison produced the following results:

| Representation | Silhouette score |
|---|---:|
| PCA, 16 components | 0.3122 |
| VAE, 16 dimensions | 0.2462 |
| VAE, seven active dimensions | 0.2626 |
| PCA, seven components | 0.3464 |

PCA achieved higher silhouette scores than the VAE representations in this experiment.

The findings indicate that the trained VAE did not outperform PCA in separating the annotated cell populations according to this evaluation metric.

This result was retained rather than presenting the VAE as superior to the conventional method.

### 5.2 SHAP and Integrated Gradients Agreement

The mean-baseline IG versus SHAP comparison produced:

- Spearman rank correlations ranging approximately from 0.943 to 0.951.
- Top-20 overlap ranging from 14 to 18 shared genes across the seven active dimensions.

These findings indicate substantial agreement between the two attribution methods, although their gene rankings were not identical.

### 5.3 Integrated Gradients Baseline Sensitivity

The zero-baseline versus mean-baseline comparison produced:

- Spearman rank correlations of approximately 0.972–0.978.
- Top-20 overlap ranging from 5 to 14 genes across the active dimensions.

Although the overall rankings were highly correlated, the top-ranked genes showed greater sensitivity to baseline selection.

This demonstrates the importance of considering baseline configuration when interpreting Integrated Gradients results.

### 5.4 SHAP Stability

Two independent SHAP runs were compared.

The top-20 gene overlap was:

- 20 out of 20 genes for six active dimensions.
- 19 out of 20 genes for one active dimension.

Full-ranking Spearman correlations were approximately 0.9998–0.9999.

These results indicate high ranking stability across the two SHAP runs.

### 5.5 Attribution Reliability

Integrated Gradients completeness checks were conducted for both baseline configurations.

SHAP additivity was assessed across the two seeds.

Using the predefined 5% mean-error-to-output-standard-deviation criterion, five of the seven active latent dimensions passed the final SHAP additivity assessment.

Latent_14 and latent_16 did not satisfy the criterion.

These results highlight that attribution reliability was not uniform across all latent dimensions.

### 5.6 Marker-Gene Enrichment

Expression-matched marker enrichment testing produced 24 comparisons.

Following Benjamini-Hochberg correction:

- 14 comparisons were statistically significant.
- 10 comparisons were not statistically significant.

SHAP showed more consistent marker enrichment across the tested conditions, while IG also showed significant enrichment in selected comparisons.

These findings indicate that known marker genes were enriched in selected attribution rankings relative to expression-matched expectations.

The results are computational and exploratory and do not constitute independent experimental validation.

## 6. Figures and Visual Outputs

A total of 21 Third Phase figures were generated and saved in the `figures/` directory.

The figures cover the following analyses:

| Analysis | Figures |
|---|---:|
| SHAP top-20 gene rankings | 1 |
| Zero-baseline IG top-20 rankings | 1 |
| Mean-baseline IG top-20 rankings | 1 |
| SHAP versus IG comparisons and shared-gene plots | 9 |
| IG baseline sensitivity | 2 |
| Attribution completeness and SHAP additivity | 3 |
| Expression-matched marker enrichment | 2 |
| Marker-ranking comparison | 2 |
| **Total** | **21** |

All Third Phase figures use filenames beginning with `third_phase_`.

### Main figure files

- `third_phase_shap_top20.png`
- `third_phase_ig_zero_top20.png`
- `third_phase_ig_mean_top20.png`
- `third_phase_shap_ig_top20_overlap.png`
- `third_phase_shap_ig_spearman.png`
- `third_phase_ig_baseline_spearman.png`
- `third_phase_ig_baseline_top20_overlap.png`
- `third_phase_ig_completeness_comparison.png`
- `third_phase_shap_additivity_by_seed.png`
- `third_phase_shap_additivity_threshold.png`
- `third_phase_marker_enrichment_observed_vs_null.png`
- `third_phase_marker_enrichment_fdr.png`
- `third_phase_marker_rank_ig_vs_shap_spread.png`

The seven shared-gene figures are saved separately for each active latent dimension.

## 7. Output Files and Directory Organisation

The principal Third Phase outputs are organised into the following directories.

### Figures

`figures/`

Contains the 21 generated Third Phase figures.

### SHAP outputs

`outputs/shap/`

Important files include:

- `shap_attributions_test528_seed0.npy`
- `shap_attributions_test528_seed1.npy`
- `shap_gene_ranking.csv`
- `shap_final_seed_stability_test528.csv`
- `shap_final_additivity_test528.csv`
- `shap_ig_marker_sensitivity_test528_corrected.csv`
- `shap_ig_marker_sensitivity_test528_FDR_corrected.csv`

### Integrated Gradients outputs

`outputs/attributions/`

Important files include:

- `ig_zero.npy`
- `ig_zero_meta.npz`
- `ig_zero_ranking.csv`
- `ig_zero_completeness.csv`
- `ig_mean.npy`
- `ig_mean_meta.npz`
- `ig_mean_ranking.csv`
- `ig_mean_completeness.csv`
- `ig_mean_vs_shap_spearman.csv`
- `ig_mean_vs_shap_top20_overlap.csv`
- `ig_baseline_spearman_comparison.csv`
- `ig_baseline_top20_overlap.csv`

The original full-cell Integrated Gradients attribution output is also retained under:

`outputs/integrated_gradients/`

Large attribution arrays are excluded from Git tracking according to the project's existing `.gitignore` configuration.

## 8. Reproducibility and Computational Environment

The Third Phase analyses were performed using Python in JupyterLab on macOS.

The project environment included:

| Component | Version |
|---|---|
| Python | 3.12 |
| NumPy | 1.26.4 |
| Pandas | 2.2.3 |
| Scanpy | 1.11.5 |
| AnnData | 0.11.4 |
| PyTorch | 2.2.2 |
| SHAP | 0.48.0 |

The analysis uses previously generated model representations, attribution arrays and processed dataset outputs.

The random seed for the original VAE model was 42. The two final SHAP runs used separate seeds, 0 and 1.

Reproduction requires the processed input dataset, the trained VAE checkpoint, the relevant analysis scripts and a compatible Python environment.

The original input dataset and large attribution arrays are not necessarily included in the Git repository. Their availability should be confirmed separately when reproducing the complete workflow.

## 9. Scientific Interpretation

The Third Phase demonstrates a workflow for investigating the interpretability of deep-learning-derived representations in single-cell transcriptomic data.

Several findings are particularly relevant:

1. The VAE generated latent representations that could be investigated using gene-level attribution methods.
2. SHAP and Integrated Gradients identified substantially overlapping gene rankings.
3. Integrated Gradients rankings showed sensitivity to baseline selection, particularly among the highest-ranked genes.
4. SHAP rankings were highly stable across the two independent runs.
5. Attribution completeness and additivity checks identified limitations in some latent dimensions.
6. Expression-matched marker testing identified statistically significant enrichment in selected comparisons.
7. PCA achieved stronger silhouette-based cell-type separation than the VAE in this experiment.

Together, these results illustrate why model performance, explanation consistency, attribution reliability and marker-gene enrichment should be evaluated separately.

## 10. Limitations

The following limitations should be considered when interpreting the results:

- The VAE did not outperform PCA according to the silhouette scores obtained in this experiment.
- The seven selected active dimensions do not necessarily represent every relevant aspect of the data.
- SHAP and Integrated Gradients measure model attribution and do not establish causal gene relationships.
- Integrated Gradients rankings depend partly on baseline selection.
- SHAP additivity did not satisfy the predefined acceptance criterion in two active dimensions.
- Marker enrichment is exploratory and does not constitute independent experimental validation.
- The PBMC dataset is a single-cell reference dataset and does not establish clinical validity or direct applicability to patient-specific precision medicine.
- The analysis uses selected highly variable genes and a marker panel; findings may differ when other gene-selection strategies are used.

## 11. Conclusion

The Third Phase extends the PBMC VAE project from model development into systematic evaluation and explainable AI.

By combining SHAP, Integrated Gradients, ranking comparisons, baseline sensitivity analysis, attribution reliability checks and expression-matched marker enrichment, the project investigates both what the VAE learned and how reliably its latent representations can be interpreted.

The work demonstrates practical experience in:

- Deep learning with PyTorch.
- Variational autoencoder evaluation.
- Single-cell RNA-seq analysis.
- Explainable artificial intelligence.
- SHAP and Integrated Gradients.
- Statistical testing and multiple-testing correction.
- Gene-level attribution analysis.
- Reproducible computational research.

The central contribution is a structured evaluation of explainability methods applied to VAE latent representations, including both their strengths and their limitations.

The results provide a foundation for further investigation of interpretable deep learning methods in single-cell transcriptomics and translational bioinformatics.
