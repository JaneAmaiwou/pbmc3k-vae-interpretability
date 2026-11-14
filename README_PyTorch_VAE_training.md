# PyTorch Variational Autoencoder (VAE) Training

## Overview

This project implements and trains a PyTorch Variational Autoencoder (VAE) using a processed PBMC 3k single-cell RNA-sequencing dataset.

The objective is to learn a compact, continuous representation of gene-expression profiles and investigate whether the resulting latent dimensions capture meaningful biological variation across immune-cell populations.

The analysis includes model training, latent-space extraction, visualisation and exploratory marker-gene correlation analysis.

## Dataset

The model was trained using:

- 2,638 cells after quality control.
- 2,006 input genes, consisting of 2,000 highly variable genes and six additional immune-cell marker genes.
- 2,110 training cells.
- 528 test cells.

Expression data were normalised and log-transformed during preprocessing.

The six additional marker genes were retained to support the subsequent biological interpretation of the learned latent representation.

## Model architecture

A fully connected Variational Autoencoder was implemented in PyTorch.

The architecture was:

- Encoder: 2,006 -> 256 -> 64 -> 16.
- Latent representation: 16 dimensions.
- Decoder: 16 -> 64 -> 256 -> 2,006.
- Approximately 1.07 million trainable parameters.

The encoder learns the mean and variance parameters of the latent distribution. Latent representations are sampled using the reparameterisation trick, and the decoder reconstructs the input gene-expression profiles.

## Training configuration

The model was trained using the following configuration:

| Parameter | Configuration |
|---|---|
| Framework | PyTorch |
| Random seed | 42 |
| Training epochs | 100 |
| Latent dimensions | 16 |
| Loss | Reconstruction loss + KL divergence |
| KL warm-up | 20 epochs |

The objective combines reconstruction error with the Kullback-Leibler (KL) divergence term. KL warm-up gradually introduces the regularisation contribution during training.

### Training and test performance

| Metric | Training | Test |
|---|---:|---:|
| Total loss | 384.2867 | 398.0298 |
| Reconstruction loss | 375.1252 | 389.9554 |
| KL divergence | 9.1616 | 8.0743 |

The test reconstruction mean squared error per input gene was approximately 0.1944.

These values describe model performance under this training configuration. They do not, by themselves, establish biological validity or generalisation to an independent dataset.

## Latent-space analysis

The trained encoder produced a 16-dimensional latent representation for each of the 2,638 cells.

Inspection of latent-dimension activity indicated that seven dimensions showed comparatively stronger activity:

- 2
- 5
- 7
- 9
- 14
- 15
- 16

The remaining dimensions showed weaker activity, consistent with partial latent-dimension utilisation.

This distinction is important: although the model was configured with 16 latent dimensions, the dimensions were not equally active.

## Latent-space visualisation

The learned latent representations were visualised using UMAP.

Figure:

`figures/vae_latent_umap_seed42.png`

UMAP provides an exploratory view of the organisation of the learned representation. As a nonlinear projection, its apparent distances and group separation should not be interpreted as direct measurements of distances in the original latent space.

## Marker-gene association analysis

Latent dimensions were examined for associations with selected immune-cell marker genes.

The analysis included global latent-marker correlations and additional within-cell-type correlation analysis.

The within-cell-type analysis was restricted to six cell populations with at least 50 cells. Across these populations:

- 1,152 latent-marker tests were evaluated.
- 202 associations remained significant after Benjamini-Hochberg false-discovery-rate correction.

Figure:

`figures/within_cell_type_marker_correlations.png`

The results suggest that some latent dimensions retain gene-expression variation associated with established immune-cell markers, including variation within annotated cell populations.

These associations are correlations, not evidence of causality or independent biological validation.

## Repository contents

| Path | Description |
|---|---|
| `PyTorch VAE training.ipynb` | Notebook containing model training and analysis |
| `src/vae_torch.py` | PyTorch VAE implementation |
| `models/vae_torch_seed42.pt` | Trained model checkpoint |
| `outputs/vae_latent_seed42.npz` | Saved latent representations and associated metadata |
| `outputs/global_latent_marker_correlations_fdr.csv` | Global marker-correlation results |
| `outputs/within_cell_type_marker_correlations.csv` | Within-cell-type marker-correlation results |
| `outputs/within_cell_type_correlation_summary.csv` | Summary of within-cell-type correlations |
| `figures/vae_latent_umap_seed42.png` | Latent-space UMAP |
| `figures/within_cell_type_marker_correlations.png` | Within-cell-type marker-correlation visualisation |

Large attribution arrays are maintained separately and are not included in this repository upload.

## Reproducibility

The training configuration uses random seed 42. The model checkpoint preserves the trained model parameters and training information, while the latent archive contains the extracted cell representations and associated metadata.

Reproduction requires the processed input dataset and a compatible Python environment with the required dependencies, including PyTorch and the relevant single-cell analysis packages.

The original input dataset is not included in this repository.

## Limitations

- The marker-gene associations are exploratory and should not be interpreted as independent biological validation.
- Cell-type annotations are reference labels; the model may capture both cell identity and within-population expression variation.
- UMAP is a nonlinear visualisation and does not directly establish separation in the original latent space.
- The 16-dimensional model showed unequal latent-dimension activity, indicating partial utilisation of the configured latent space.
- Evaluation on independent datasets would be needed to assess generalisability.

## Summary

This analysis produced a trained PyTorch VAE, saved latent representations and an initial characterisation of latent-dimension activity and marker-gene associations in PBMC single-cell RNA-sequencing data.

These outputs provide a basis for subsequent quantitative evaluation and explainability analyses.
