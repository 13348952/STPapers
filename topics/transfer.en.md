# Heterogeneity, meta-learning, and transfer

[简体中文](transfer.md) | [English](transfer.en.md) · [主题导航 / Topics](README.md) · [Full catalog](../README.en.md)

<a id="topic-transfer"></a>

## 07 · Heterogeneity, meta-learning, and transfer

Node-specific parameters, cross-domain adaptation, and continual learning are distinct tasks.

<a id="paper-pimcst"></a>

- **PIMCST** — Abdul Joseph Fofanah et al. **[PIMCST: Physics-Informed Multi-Phase Consensus and Spatio-Temporal Few-Shot Learning for Traffic Flow Forecasting](https://arxiv.org/abs/2602.01936)**. 2026 · arXiv; formal publication status not verified.

  Builds multi-stage consensus from diffusion, synchronization, and spectral representations, using meta-learning for few-shot cross-city forecasting.

  [Publication evidence](https://arxiv.org/abs/2602.01936) · [Code](https://github.com/afofanah/MCPST) (author/project repository checked)

  Version / usage notes: The title uses PIMCST, while the abstract and repository use MCPST; this naming difference is retained.

<a id="paper-urbanpg"></a>

- **UrbanPG** — Aoyu Liu et al. **[UrbanPG: An Efficient Framework with Personalized Context and General Backbone Interaction for Urban Spatio-Temporal Learning](https://ojs.aaai.org/index.php/AAAI/article/view/38554)**. 2026 · AAAI.

  Separates personalized context from a general backbone to study large-scale forecasting, few-shot transfer, and continual learning.

  [Published version](https://ojs.aaai.org/index.php/AAAI/article/view/38554) · [Publication evidence](https://ojs.aaai.org/index.php/AAAI/article/view/38554) · [Code](https://github.com/Aoyu-Liu/UrbanPG) (author/project repository checked)

  Version / usage notes: GitHub About still mentions AAAI 2025, whereas the README and official conference page specify AAAI 2026; the conference page takes precedence.

<a id="paper-himnet"></a>

- **HimNet** — Zheng Dong et al. **[Heterogeneity-Informed Meta-Parameter Learning for Spatiotemporal Time Series Forecasting](https://arxiv.org/abs/2405.10800)**. 2024 · KDD.

  Learns model parameters that vary across space and time through spatio-temporal embeddings and meta-parameter pools.

  [Publication evidence](https://github.com/XDZhelheim/HimNet) · [Code](https://github.com/XDZhelheim/HimNet) (author/project repository checked)

<a id="paper-megacrn"></a>

- **MegaCRN** — Renhe Jiang et al. **[Spatio-Temporal Meta-Graph Learning for Traffic Forecasting](https://arxiv.org/abs/2211.14701)**. 2023 · AAAI; first arXiv release: 2022.

  Uses meta-node memory and meta-graph learning to capture heterogeneity across traffic nodes and temporal patterns.

  [Publication evidence](https://github.com/deepkashiwa20/MegaCRN) · [Code](https://github.com/deepkashiwa20/MegaCRN) (author/project repository checked)

  Version / usage notes: Uses arXiv:2211.14701, corresponding to AAAI 2023, rather than the withdrawn extended manuscript arXiv:2212.05989.

<a id="paper-st-metanet"></a>

- **ST-MetaNet** — Zheyi Pan et al. **[Urban Traffic Prediction from Spatio-Temporal Data Using Deep Meta Learning](https://doi.org/10.1145/3292500.3330884)**. 2019 · KDD.

  Uses geographical attributes to generate parameters for meta graph attention and meta recurrent networks, modeling heterogeneity among urban traffic nodes and connections.

  [Published version](https://doi.org/10.1145/3292500.3330884) · [Publication evidence](https://api.crossref.org/works/10.1145/3292500.3330884) · [Code](https://github.com/panzheyi/ST-MetaNet) (author/project repository checked)

  Version / usage notes: Meta-learning generates node/edge-dependent parameters from geographical attributes; this does not establish few-shot cross-city adaptation. The MXNet author implementation training entry was inspected but not run.

<a id="paper-omnist"></a>

- **OmniST** — Praveg Vashishtha **[OmniST: Topology-Invariant Spatiotemporal Forecasting with Guaranteed-Coverage Uncertainty at Unseen Sensor Locations](https://arxiv.org/abs/2611.04256)**. 2026 · arXiv; formal publication status not verified.

  Combines coordinate encoding, dynamic neighborhood attention, and per-node recurrent modeling for changing sensor sets, with conformal calibration at unseen locations.

  [Publication evidence](https://arxiv.org/abs/2611.04256) · [Code](https://github.com/Praveg432/OmniST) (author/project repository checked)

  Version / usage notes: Coverage guarantees depend on exchangeability of calibration and test scores; local topology invariance requires conditions including unchanged neighborhoods. Model source and run instructions were inspected; no training was performed.

<a id="paper-evost"></a>

- **EvoST** — Du Yin et al. **[EvoST: Adapting Traffic Forecasters to Evolving Sensor Graphs](https://arxiv.org/abs/2607.25875)**. 2026 · arXiv; formal publication status not verified.

  Keeps shared forecasting weights frozen while refreshing node identities, initializing new sensors, and calibrating online with delayed labels in evolving traffic sensor networks.

  [Publication evidence](https://arxiv.org/abs/2607.25875) · [Code](https://github.com/lixus7/EvoST) (author/project repository checked)

  Version / usage notes: First posted on 2026-07-28 and revised to v5 on 2026-11-07; one version chain is cataloged. Uses subsequent supervised feedback rather than unlabeled zero-shot transfer. Implementation and commands were inspected; original experimental checkpoints are not included, and results were not reproduced.

<a id="paper-atlas"></a>

- **ATLAS** — Ryusei Iwasa et al. **[Latent Prediction-Anchored Multi-View Reconstruction for Cross-Network Spatiotemporal Forecasting](https://drive.google.com/file/d/1nLRm3JRLsAaLG4lI9mw0-hDfVli4nI4p/view?usp=drivesdk)**. 2026 · ACM SIGSPATIAL 2026.

  Pretrains on temporal and spectral reconstruction anchored by latent prediction. During transfer it combines functional and physical graphs to forecast traffic or crowd distribution.

  [Publication evidence](https://sigspatial2026.sigspatial.org/detailed-program.html) · [Code](https://github.com/ryu291/ATLAS) (linked by the paper; returned HTTP 404 during verification)

  Version / usage notes: Verified against the conference program and the author manuscript. The code link in the author manuscript returned HTTP 404.

<a id="paper-icl-traffic"></a>

- **ICL-Traffic** — Parth Ripal Parikh et al. **[ICL-Traffic Forecasting: Lightweight In-Context Learning for Pretrained Spatio-Temporal Foundation Models](https://drive.google.com/file/d/1KT78sWRt6fYkSl5ClilOQt7fayfvxeUc/view?usp=drivesdk)**. 2026 · ACM SIGSPATIAL 2026.

  Retrieves similar training windows and uses an offline-trained attention module to combine their errors into output corrections for a frozen traffic forecaster.

  [Publication evidence](https://sigspatial2026.sigspatial.org/detailed-program.html) · [Code](https://github.com/Parth291102/Traffic-Forecasting-TSFM) (author/project repository checked)

  Version / usage notes: Verified against the conference program and the author manuscript.
