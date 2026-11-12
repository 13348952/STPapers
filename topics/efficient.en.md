# Simple baselines, efficiency, and large-scale forecasting

[简体中文](efficient.md) | [English](efficient.en.md) · [主题导航 / Topics](README.md) · [Full catalog](../README.en.md)

<a id="topic-efficient"></a>

## 05 · Simple baselines, efficiency, and large-scale forecasting

Designs that account for node count, history length, forecasting horizon, and computational cost.

<a id="paper-fast"></a>

- **FaST** — Yiji Zhao et al. **[FaST: Efficient and Effective Long-Horizon Forecasting for Large-Scale Spatial-Temporal Graphs via Mixture-of-Experts](https://arxiv.org/abs/2601.05174)**. 2026 · KDD.

  Uses adaptive graph proxy attention and a heterogeneity-aware mixture of experts for large spatio-temporal graphs and long forecasting horizons.

  [Publication evidence](https://github.com/yijizhao/FaST) · [Code](https://github.com/yijizhao/FaST) (author/project repository checked)

  Version / usage notes: Focuses on long horizons and large graphs; performance claims in the abstract are not treated as a ranking across different experimental settings.

<a id="paper-hieramix"></a>

- **HieraMix** — Yongyao Wang et al. **[HieraMix: A Hierarchical MLP-Mixer for Large-Scale Traffic Forecasting](https://ijcai.org/proceedings/2026/729)**. 2026 · IJCAI.

  Builds an MLP architecture for large road networks through hierarchical spatio-temporal mixing and adaptive regional mixing.

  [Published version](https://ijcai.org/proceedings/2026/729) · [Publication evidence](https://ijcai.org/proceedings/2026/729) · Code: author code not verified

<a id="paper-lorest"></a>

- **LoReST** — Qi Feng et al. **[Learning Local Heterogeneity and Cross-Region Context for Large-Scale Traffic Forecasting](https://arxiv.org/abs/2609.27637)**. 2026 · arXiv; formal publication status not verified.

  Combines relation-aware local aggregation with regional pooling, interaction, and redistribution to model local heterogeneity and cross-region context.

  [Publication evidence](https://arxiv.org/abs/2609.27637) · Code: author code not verified

<a id="paper-minist"></a>

- **MiniST** — Sheng Huang et al. **[MiniST: Unlocking Input Window Length in Traffic Flow Forecasting with Compact Parameters](https://ijcai.org/proceedings/2026/298)**. 2026 · IJCAI.

  Projects long traffic histories onto a compact orthogonal basis and combines this with a template update module to handle long historical inputs.

  [Published version](https://ijcai.org/proceedings/2026/298) · [Publication evidence](https://ijcai.org/proceedings/2026/298) · [Code](https://github.com/enheng66/MiniST) (project repository accessible; author attribution needs stronger evidence)

  Version / usage notes: The repository example uses seq_len=720; align input windows when comparing with short-history baselines.

<a id="paper-sagt"></a>

- **SAGT** — Amirhossein Ghaffari et al. **[Spectral Adaptive Graph Transformer for Efficient and Scalable Traffic Forecasting](https://arxiv.org/abs/2610.25140)**. 2026 · arXiv; formal publication status not verified.

  Studies forecasting cost using a learned low-rank directed spatial operator, local graph diffusion, and frequency reweighting.

  [Publication evidence](https://arxiv.org/abs/2610.25140) · [Code](https://github.com/Ahghaffari/sagt) (author/project repository checked)

<a id="paper-sqlinear"></a>

- **SqLinear** — Yongfeng Su et al. **[SqLinear: Balanced Square Partitioning Makes Linear Interaction Sufficient for Large-Scale Traffic Forecasting](https://arxiv.org/abs/2606.21072)**. 2026 · arXiv; formal publication status not verified.

  Studies efficient large-scale traffic forecasting through balanced spatial partitioning and hierarchical linear interactions.

  [Publication evidence](https://arxiv.org/abs/2606.21072) · Code: author code not verified

<a id="paper-graphsparsenet"></a>

- **GraphSparseNet** — Weiyang Kong et al. **[GraphSparseNet: a Novel Method for Large Scale Traffic Flow Prediction](https://arxiv.org/abs/2502.19823)**. 2025 · PVLDB.

  Reduces the cost of relationship modeling in large road networks through feature extraction and relation compression modules.

  [Publication evidence](https://arxiv.org/abs/2502.19823) · Code: author code not verified

<a id="paper-patchstg"></a>

- **PatchSTG** — Yuchen Fang et al. **[Efficient Large-Scale Traffic Forecasting with Transformers: A Spatial Data Management Perspective](https://arxiv.org/abs/2412.09972)**. 2025 · KDD; first arXiv release: 2024.

  Uses a KDTree to construct irregular spatial patches, learning local and global relationships through within-patch and cross-patch attention.

  [Publication evidence](https://arxiv.org/abs/2412.09972) · [Code](https://github.com/LMissher/PatchSTG) (author/project repository checked)

<a id="paper-stgformer"></a>

- **STGformer** — Hongjun Wang et al. **[STGformer: Efficient Spatiotemporal Graph Transformer for Traffic Forecasting](https://arxiv.org/abs/2410.00385)**. 2024 · arXiv; formal publication status not verified.

  This paper proposes an efficient spatiotemporal graph Transformer for traffic forecasting, combining graph convolution and Transformer modeling, with a single STG attention block to capture high-order spatiotemporal interactions and evaluating efficiency and performance on settings including LargeST.

  [Publication evidence](https://arxiv.org/abs/2410.00385) · [Code](https://github.com/Dreamzz5/STGformer) (author/project repository checked)

  Version / usage notes: The paper directly links the author repository; model/train.py and usage instructions were inspected without running experiments. Retains arXiv 2024 status. Distinct from similarly named pose, trajectory, and sparse-sensing papers; reported speedups are setting-specific.

<a id="paper-bigst"></a>

- **BigST** — Jindong Han et al. **[BigST: Linear Complexity Spatio-Temporal Graph Neural Network for Traffic Forecasting on Large-Scale Road Networks](https://www.vldb.org/pvldb/vol17/p1081-han.pdf)**. 2024 · PVLDB.

  Precomputes long-history representations and uses linearized global spatial modeling to scale to large road networks.

  [Published version](https://doi.org/10.14778/3641204.3641217) · [Publication evidence](https://doi.org/10.14778/3641204.3641217) · [Code](https://github.com/usail-hkust/BigST) (author/project repository checked)

<a id="paper-stid"></a>

- **STID** — Zezhi Shao et al. **[Spatial-Temporal Identity: A Simple yet Effective Baseline for Multivariate Time Series Forecasting](https://arxiv.org/abs/2208.05233)**. 2022 · CIKM Short.

  Adds node and temporal identity embeddings to a simple MLP, providing a baseline for assessing the benefits of complex spatial modules.

  [Publication evidence](https://github.com/GestaltCogTeam/STID) · [Code](https://github.com/GestaltCogTeam/STID) (author/project repository checked)

<a id="paper-stnorm"></a>

- **STNorm** — Jinliang Deng et al. **[ST-Norm: Spatial and Temporal Normalization for Multi-variate Time Series Forecasting](https://doi.org/10.1145/3447548.3467330)**. 2021 · KDD.

  Uses spatial and temporal normalization to handle different components of multivariate sequences in a simple forecasting module.

  [Published version](https://doi.org/10.1145/3447548.3467330) · [Publication evidence](https://doi.org/10.1145/3447548.3467330) · [Code](https://github.com/JLDeng/ST-Norm) (author/project repository checked)

<a id="paper-ragc"></a>

- **RAGC** — Kaiqi Wu et al. **[Efficient Traffic Forecasting on Large-Scale Road Network by Regularized Adaptive Graph Convolution](https://arxiv.org/abs/2506.07179)**. 2026 · ICDE; first arXiv release: 2025.

  Targets large-scale traffic forecasting with an efficient cosine operator for graph convolution and regularizes adaptive graph learning through stochastic shared embeddings and a residual-difference mechanism.

  [Published version](https://doi.org/10.1109/ICDE65706.2026.00068) · [Publication evidence](https://doi.org/10.1109/ICDE65706.2026.00068) · [Code](https://github.com/wkq-wukaiqi/RAGC) (author/project repository checked)

  Version / usage notes: arXiv v1 (2025-06-08) was titled Regularized Adaptive Graph Learning for Large-Scale Traffic Forecasting (RAGL); v3 (2026-04-30) uses the current title. These versions are counted as one work. Author order follows the publisher metadata and v3. Author source files and usage instructions were inspected; training and performance were not reproduced.

<a id="paper-tas-gnn"></a>

- **TAS-GNN** — JiaJun Yu et al. **[Active Arbitration: Decoupling Spatio-Temporal Duality for Efficient Traffic Forecasting](https://ijcai.org/proceedings/2026/583)**. 2026 · IJCAI 2026.

  Uses temporal context to arbitrate spatial interactions and wavelet decomposition to separate physical lags from semantic synchrony.

  [Published version](https://doi.org/10.24963/ijcai.2026/583) · [Publication evidence](https://ijcai.org/proceedings/2026/583) · Code: author code not verified

  Version / usage notes: The paper links https://github.com/highhhhh/TAS-GNN, but the inspected commit contains only a supplementary PDF, not released model code.
