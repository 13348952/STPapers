# Precipitation, weather, and Earth-system forecasting

[简体中文](weather.md) | [English](weather.en.md) · [主题导航 / Topics](README.md) · [Full catalog](../README.en.md)

<a id="topic-weather"></a>

## 11 · Precipitation, weather, and Earth-system forecasting

Nowcasting, medium-range weather forecasting, and Earth-system foundation models.

<a id="paper-aurora"></a>

- **Aurora** — Cristian Bodnar et al. **[A foundation model for the Earth system](https://arxiv.org/abs/2405.13063)**. 2025 · Nature; first arXiv release: 2024.

  Pretrains on diverse Earth-system data and adapts to tasks including weather, air quality, and ocean waves.

  [Published version](https://doi.org/10.1038/s41586-025-09005-y) · [Publication evidence](https://doi.org/10.1038/s41586-025-09005-y) · [Code](https://github.com/microsoft/aurora) (author/project repository checked)

<a id="paper-fengwu"></a>

- **FengWu** — Kang Chen et al. **[FengWu: Pushing the Skillful Global Medium-range Weather Forecast beyond 10 Days Lead](https://arxiv.org/abs/2304.02948)**. 2025 · Communications Earth & Environment; first arXiv release: 2023.

  Uses a multimodal, multitask architecture, cross-modal fusion, and a replay buffer for medium-range weather modeling.

  [Publication evidence](https://github.com/OpenEarthLab/FengWu) · [Code](https://github.com/OpenEarthLab/FengWu) (author/project repository checked)

<a id="paper-gencast"></a>

- **GenCast** — Ilan Price et al. **[Probabilistic weather forecasting with machine learning](https://arxiv.org/abs/2312.15796)**. 2025 · Nature; first arXiv release: 2023.

  Uses diffusion to generate ensemble forecasts that capture joint uncertainty in future global weather states.

  [Published version](https://doi.org/10.1038/s41586-024-08252-9) · [Publication evidence](https://doi.org/10.1038/s41586-024-08252-9) · [Code](https://github.com/google-deepmind/graphcast) (author/project repository checked)

  Version / usage notes: Uses the Nature volume year, 2025; published online on 2024-12-04, with the preprint first released in 2023.

<a id="paper-climax"></a>

- **ClimaX** — Tung Nguyen et al. **[ClimaX: A foundation model for weather and climate](https://arxiv.org/abs/2301.10343)**. 2023 · ICML.

  Pretrains on heterogeneous climate data and adapts to different weather variables and forecasting tasks.

  [Publication evidence](https://github.com/microsoft/ClimaX) · [Code](https://github.com/microsoft/ClimaX) (author/project repository checked)

<a id="paper-graphcast"></a>

- **GraphCast** — Remi Lam et al. **[Learning skillful medium-range global weather forecasting](https://arxiv.org/abs/2212.12794)**. 2023 · Science; first arXiv release: 2022.

  Uses a graph neural network to learn the evolution of global weather fields and produce medium-range multivariate forecasts.

  [Published version](https://doi.org/10.1126/science.adi2336) · [Publication evidence](https://doi.org/10.1126/science.adi2336) · [Code](https://github.com/google-deepmind/graphcast) (author/project repository checked)

<a id="paper-nowcastnet"></a>

- **NowcastNet** — Yuchen Zhang et al. **[Skilful nowcasting of extreme precipitation with NowcastNet](https://www.nature.com/articles/s41586-023-06184-4)**. 2023 · Nature.

  Combines physical evolution constraints with generative modeling for extreme precipitation nowcasting.

  [Published version](https://www.nature.com/articles/s41586-023-06184-4) · [Publication evidence](https://www.nature.com/articles/s41586-023-06184-4) · Code: author code not verified

<a id="paper-pangu-weather"></a>

- **Pangu-Weather** — Kaifeng Bi et al. **[Accurate medium-range global weather forecasting with 3D neural networks](https://arxiv.org/abs/2211.02556)**. 2023 · Nature; first arXiv release: 2022.

  Uses a three-dimensional Earth-specific Transformer and hierarchical temporal aggregation for global weather forecasting.

  [Published version](https://doi.org/10.1038/s41586-023-06185-3) · [Publication evidence](https://doi.org/10.1038/s41586-023-06185-3) · [Code](https://github.com/198808xc/Pangu-Weather) (author/project repository checked)

<a id="paper-earthformer"></a>

- **Earthformer** — Zhihan Gao et al. **[Earthformer: Exploring Space-Time Transformers for Earth System Forecasting](https://arxiv.org/abs/2207.05833)**. 2022 · NeurIPS.

  Exchanges information through local Cuboid Attention and global vectors for precipitation and Earth-system forecasting.

  [Publication evidence](https://github.com/amazon-science/earth-forecasting-transformer) · [Code](https://github.com/amazon-science/earth-forecasting-transformer) (author/project repository checked)

<a id="paper-fourcastnet"></a>

- **FourCastNet** — Jaideep Pathak et al. **[FourCastNet: A Global Data-driven High-resolution Weather Model using Adaptive Fourier Neural Operators](https://arxiv.org/abs/2202.11214)**. 2022 · arXiv; formal publication status not verified.

  Uses an adaptive Fourier neural operator for high-resolution global weather forecasting.

  [Publication evidence](https://arxiv.org/abs/2202.11214) · [Code](https://github.com/NVlabs/FourCastNet) (author/project repository checked)

<a id="paper-dgmr"></a>

- **DGMR** — Suman Ravuri et al. **[Skilful precipitation nowcasting using deep generative models of radar](https://arxiv.org/abs/2104.00954)**. 2021 · Nature.

  Uses a deep generative model to produce probabilistic precipitation nowcasts with spatio-temporal consistency.

  [Published version](https://doi.org/10.1038/s41586-021-03854-z) · [Publication evidence](https://doi.org/10.1038/s41586-021-03854-z) · Code: author code not verified

<a id="paper-fitzroy"></a>

- **FitzRoy** — Ozan Sener et al. **[Skillful and realistic precipitation forecasting with reinforced diffusion](https://arxiv.org/abs/2610.38775)**. 2026 · arXiv; formal publication status not verified.

  Refines conditional discrete diffusion with reinforcement learning to forecast future precipitation fields.

  [Publication evidence](https://arxiv.org/abs/2610.38775) · Code: author code not verified

  Version / usage notes: The full model uses ERA5, MRMS, and NBM forecast guidance; distinguish it from the standalone variant without NBM. Author code was not verified; links to other models are not this implementation.

<a id="paper-sonny-ens"></a>

- **Sonny-ENS** — Minjong Cheon **[Sonny-ENS: demystifying machine-learning ensemble weather forecasting](https://arxiv.org/abs/2611.01614)**. 2026 · arXiv; formal publication status not verified.

  Trains multiple weather networks with CRPS and constructs ensemble forecasts using Monte Carlo dropout.

  [Publication evidence](https://arxiv.org/abs/2611.01614) · Code: author code not verified

  Version / usage notes: The paper promises code and weights upon publication; a public release was not verified, so the promise is not treated as an available implementation.

<a id="paper-lcg-sfno"></a>

- **LCG-SFNO** — Yaojun Li et al. **[Low-Rank Clebsch--Gordan Coupling for Equivariant Spherical Forecasting](https://arxiv.org/abs/2611.03411)**. 2026 · arXiv; formal publication status not verified.

  Uses low-rank Clebsch–Gordan coupling for nonlinear spectral interactions in equivariant spherical dynamics and weather forecasting.

  [Publication evidence](https://arxiv.org/abs/2611.03411) · Code: author code not verified

  Version / usage notes: Author code was not verified; reported equivariance and computational efficiency have not been independently reproduced by this catalog.

<a id="paper-ai-ensemble-blend"></a>

- **AI-Ensemble-Blend** — Harris Sop Nkuiate et al. **[Value of Adding AI Weather Model Ensembles to a Multi-model Probabilistic Blend](https://arxiv.org/abs/2610.42130)**. 2026 · arXiv; formal publication status not verified.

  Studies adding AI weather ensembles to multimodel probabilistic blends, examining calibration, ensemble diversity, and forecast quality.

  [Publication evidence](https://arxiv.org/abs/2610.42130) · Code: author code not verified

  Version / usage notes: AI-Ensemble-Blend is an editorial index label. The study combines existing forecasts, so comparisons must align constituent models and inputs; author code was not verified.

<a id="paper-taiji"></a>

- **TaiJi** — Jiale Wang et al. **[TaiJi: State-Conditional Adaptive Combination of Machine-Learning and Physics-Based Global Weather Forecasts](https://arxiv.org/abs/2609.31972)**. 2026 · arXiv; formal publication status not verified.

  Predicts spatially and lead-time varying combination weights and residuals from recent atmospheric states to blend machine-learning and physics-based forecasts.

  [Publication evidence](https://arxiv.org/abs/2609.31972) · Code: author code not verified

  Version / usage notes: First posted on 2026-09-25 and revised to v3 on 2026-11-02; newly added to this catalog following a revision, not a first release this week. Primary metadata and abstract were checked; HTML was unavailable and author code was not verified.

<a id="paper-swaither-precip"></a>

- **SwAIther-Precip** — Dan Assouline et al. **[SwAIther-Precip: Lead-Time-Aware Bias Correction Enables Kilometer-Scale Downscaling of Global AI Precipitation Forecasts over Switzerland](https://arxiv.org/abs/2605.16163)**. 2026 · arXiv; formal publication status not verified.

  Applies lead-time-conditioned U-Net bias correction to coarse precipitation forecasts, followed by diffusion super-resolution for probabilistic precipitation over Switzerland.

  [Publication evidence](https://arxiv.org/abs/2605.16163) · [Code](https://github.com/danassou/swaither-precip) (author/project repository checked)

  Version / usage notes: First posted on 2026-05-15 and revised to v3 on 2026-10-29; added following that revision. Author source and training instructions were inspected; the paper-specific historical AIFS forecast dataset is not public, and other data access conditions require separate checks. No training was performed.

<a id="paper-six-hourly-pqpf"></a>

- **Six-hourly-PQPF** — Thomas M Hamill **[Six-hourly Probabilistic Precipitation Forecasts Created From Hourly Probabilities](https://arxiv.org/abs/2611.03326)**. 2026 · arXiv; formal publication status not verified.

  Aggregates hourly probabilistic forecasts into six-hour precipitation distributions using a lightweight GRU and MLP.

  [Publication evidence](https://arxiv.org/abs/2611.03326) · Code: author code not verified

  Version / usage notes: First posted on 2026-11-02; backfills a previously pending candidate. This is probabilistic forecast postprocessing, not a baseline using only historical radar observations.

<a id="paper-prola"></a>

- **PROLA** — Minseo Yoon et al. **[PROLA: Principal-Orthogonal Low-rank Adaptation for Predictive Spatiotemporal Weather Downscaling](https://arxiv.org/abs/2611.11318)**. 2026 · NeurIPS 2026.

  Splits a low-rank adaptation budget between pretrained principal directions and their orthogonal complement for future weather prediction with spatial and temporal refinement.

  [Publication evidence](https://nips.cc/virtual/2026/poster/155892) · [Code](https://github.com/yms020615/PROLA) (author/project repository checked)

  Version / usage notes: Acceptance is confirmed by the official NeurIPS 2026 poster page; proceedings volume/pages were not verified. Adapter source, training entry point, and instructions were inspected; no training was performed.

<a id="paper-rescene-esm"></a>

- **Rescene-ESM** — Minjong Cheon et al. **[Rescene-ESM: an Earth system model built around a frozen AI weather model](https://arxiv.org/abs/2611.11066)**. 2026 · arXiv; formal publication status not verified.

  Couples a frozen AI atmosphere to ocean, sea-ice, land, river, carbon, and energy components for long-term Earth-system simulation and scenario projections.

  [Publication evidence](https://arxiv.org/abs/2611.11066) · Code: author code not verified

  Version / usage notes: The paper promises code, fitted coefficients, and run records on publication; a public implementation was not verified. Long-term climate scenarios and short-range weather errors are different evaluation tasks.

<a id="paper-ai-nwp-fp16"></a>

- **AI-NWP-FP16** — Stefan Siegert **[Half-precision inference of AI weather prediction models: negligible loss of skill at a fraction of the cost](https://arxiv.org/abs/2611.09573)**. 2026 · arXiv; formal publication status not verified.

  Evaluates half-precision inference across AI weather models while keeping physical states, normalization, and denormalization in FP32.

  [Publication evidence](https://arxiv.org/abs/2611.09573) · [Code](https://github.com/sieste/ai-nwp-fp16) (author/project repository checked)

  Version / usage notes: The ID is an editorial label. Precision conversion, forecast entry point, and experiment instructions were inspected; accuracy and energy findings are model-, hardware-, and evaluation-date-dependent and were not independently reproduced.

<a id="paper-dayu-tc"></a>

- **DaYu-TC** — Runzepu Hou et al. **[DaYu-TC: a global-regional nested AI system for tropical cyclone forecasting](https://arxiv.org/abs/2611.15266)**. 2026 · arXiv; formal publication status not verified.

  Combines global and regional models with extreme-aware objectives, coupling large-scale forecasts to local evolution for tropical cyclone forecasting.

  [Publication evidence](https://arxiv.org/abs/2611.15266) · [Code](https://github.com/hourzp/DaYu-TC) (author inference entry point checked; binary model, no public training code)

  Version / usage notes: Paper attribution and the public inference entry point were checked, but the neural implementation is compiled binary and training code is not public. The authors mark full-resolution accelerator validation as pending; this catalog did not download weights or run the model.

<a id="paper-satellite-swr-nowcasting"></a>

- **Satellite-SWR-Nowcasting** — Tianyu Xie et al. **[Direct Multispectral Satellite Nowcasting of Gridded Surface Solar Radiation](https://arxiv.org/abs/2611.12999)**. 2026 · arXiv; formal publication status not verified.

  Directly predicts gridded surface shortwave radiation over the next four hours from Himawari-9 multispectral histories and solar geometry.

  [Publication evidence](https://arxiv.org/abs/2611.12999) · Code: author code not verified

  Version / usage notes: The ID is an editorial label. First posted on 2026-11-08 and revised to v2 on 2026-11-11; counted once. Author code was not verified; distinguish external satellite observations from historical-radiation-only inputs.
