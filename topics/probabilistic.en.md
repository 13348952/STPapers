# Probabilistic spatio-temporal graph forecasting

[简体中文](probabilistic.md) | [English](probabilistic.en.md) · [主题导航 / Topics](README.md) · [Full catalog](../README.en.md)

<a id="topic-probabilistic"></a>

## 09 · Probabilistic spatio-temporal graph forecasting

Predicting future distributions or samples rather than only point estimates.

<a id="paper-specstg"></a>

- **SpecSTG** — Lequan Lin et al. **[SpecSTG: A Fast Spectral Diffusion Framework for Probabilistic Spatio-Temporal Traffic Forecasting](https://arxiv.org/abs/2401.08119)**. 2025 · ICLR 2025 DeLTa Workshop; first arXiv release: 2024.

  Generates future sequences in the spectral domain, incorporating spatial dependencies and spectral graph convolutions.

  [Published version](https://openreview.net/pdf/8bc5f3850ffa6d0159499622645a1bc63f21165c.pdf) · [Publication evidence](https://openreview.net/pdf/8bc5f3850ffa6d0159499622645a1bc63f21165c.pdf) · [Code](https://github.com/lequanlin/SpecSTG) (author/project repository checked)

  Version / usage notes: First posted on arXiv in 2024 and published at the ICLR DeLTa Workshop in 2025. The workshop paper links the author repository. Model sources, the training entry point and README were inspected.

<a id="paper-diffstg"></a>

- **DiffSTG** — Haomin Wen et al. **[DiffSTG: Probabilistic Spatio-Temporal Graph Forecasting with Denoising Diffusion Models](https://arxiv.org/abs/2301.13629)**. 2023 · ACM SIGSPATIAL.

  Extends denoising diffusion models to spatio-temporal graphs for non-autoregressive probabilistic forecasting.

  [Published version](https://doi.org/10.1145/3589132.3625614) · [Publication evidence](https://arxiv.org/html/2301.13629v3) · [Code](https://github.com/wenhaomin/DiffSTG) (author/project repository checked)

  Version / usage notes: The author homepage lists the paper and links the author GitHub account; its repository README identifies the paper and includes train.py and training instructions. Public sources were inspected; training was not run.

<a id="paper-stgp-spde"></a>

- **STGP-SPDE** — Alexander V. Nikitin et al. **[Non-separable Spatio-temporal Graph Kernels via SPDEs](https://arxiv.org/abs/2111.08524)**. 2022 · AISTATS; first arXiv release: 2021.

  Derives non-separable spatio-temporal graph kernels through the link between SPDEs and Gaussian processes, modeling diffusion and wave-like dynamics.

  [Published version](https://proceedings.mlr.press/v151/nikitin22a.html) · [Publication evidence](https://proceedings.mlr.press/v151/nikitin22a.html) · [Code](https://github.com/AaltoPML/spatiotemporal-graph-kernels) (author/project repository checked)

  Version / usage notes: Published at AISTATS 2022, following an initial arXiv release in 2021. The repository includes both interpolation and extrapolation settings, which must be distinguished in comparisons. Temporal kernel code was inspected; experiments were not run.

<a id="paper-coreflow"></a>

- **CoReFlow** — Pengnan Chi et al. **[CoReFlow: Consistency-Relaxed Flow Maps for Probabilistic Traffic Forecasting](https://arxiv.org/abs/2611.05715)**. 2026 · arXiv; formal publication status not verified.

  Learns consistency-relaxed flow maps for probabilistic traffic forecasting, using endpoint training and conditional-mean constraints for one-step generation.

  [Publication evidence](https://arxiv.org/abs/2611.05715) · Code: author code not verified

  Version / usage notes: The paper states that code is in supplementary material; that implementation was not retrieved and inspected, and no public author repository was verified. Distinct from the similarly named low-rank matrix generation work.

<a id="paper-double-diffusion"></a>

- **Double-Diffusion** — Hanlin Dong et al. **[Double-Diffusion: Balancing Speed, Accuracy, and Uncertainty in Probabilistic Forecasting for Urban Sensor Networks](https://arxiv.org/abs/2506.23053)**. 2026 · ACM SIGSPATIAL 2026; first arXiv release: 2025.

  Uses graph heat diffusion to form a low-pass prior and a shortened denoising chain to sample future traffic and air-quality states.

  [Publication evidence](https://sigspatial2026.sigspatial.org/detailed-program.html) · [Code](https://github.com/cruiseresearchgroup/Double-Diffusion) (author/project repository checked)

  Version / usage notes: Verified against the conference program and the author manuscript. First posted on arXiv on 2025-06-29.
