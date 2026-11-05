# Attention, Transformers, and state-space models

[简体中文](attention.md) | [English](attention.en.md) · [主题导航 / Topics](README.md) · [Full catalog](../README.en.md)

<a id="topic-attention"></a>

## 04 · Attention, Transformers, and state-space models

Spatio-temporal attention, embeddings, propagation delays, and combinations with state-space models.

<a id="paper-fast-ssm"></a>

- **FAST-SSM** — Xinjin Li et al. **[FAST: A Synergistic Framework of Attention and State-space Models for Spatiotemporal Traffic Prediction](https://arxiv.org/abs/2604.13453)**. 2026 · ICME.

  Combines temporal attention with a Mamba spatial module; it is a different paper from FaST at KDD 2026.

  [Publication evidence](https://arxiv.org/abs/2604.13453) · Code: author code not verified

<a id="paper-speclst"></a>

- **SpecLST** — Kenan Kang et al. **[SpecLST: Spectral-Enhanced Long-Short Term Spatio-Temporal Multimodal Modeling for Traffic Forecasting](https://arxiv.org/abs/2610.36393)**. 2026 · arXiv; formal publication status not verified.

  Combines frequency-domain representations of long histories with weather and incident context, using a sparse mixture of experts in a multimodal setting.

  [Publication evidence](https://arxiv.org/abs/2610.36393) · Code: author code not verified

<a id="paper-stg-mamba"></a>

- **STG-Mamba** — Lincan Li et al. **[STG-Mamba: Spatial-Temporal Graph Learning via Selective State Space Model](https://arxiv.org/abs/2403.12418)**. 2024 · arXiv; formal publication status not verified.

  Combines selective state-space modeling of graph dynamics with Kalman-filter-inspired fusion across temporal granularities.

  [Publication evidence](https://arxiv.org/abs/2403.12418) · [Code](https://github.com/LincanLi-X/STG-Mamba) (author/project repository checked)

  Version / usage notes: Retains the arXiv 2024 record; formal publication status was not verified. The paper-linked old repository redirects to LincanLi-X. main.py was inspected; no training was run.

<a id="paper-pdformer"></a>

- **PDFormer** — Jiawei Jiang et al. **[PDFormer: Propagation Delay-Aware Dynamic Long-Range Transformer for Traffic Flow Prediction](https://arxiv.org/abs/2301.07945)**. 2023 · AAAI.

  Models dynamic spatial relationships using short- and long-range graph masks and propagation-delay-aware transformations.

  [Publication evidence](https://github.com/BUAABIGSCity/PDFormer) · [Code](https://github.com/BUAABIGSCity/PDFormer) (author/project repository checked)

<a id="paper-staeformer"></a>

- **STAEformer** — Hangchen Liu et al. **[STAEformer: Spatio-Temporal Adaptive Embedding Makes Vanilla Transformer SOTA for Traffic Forecasting](https://arxiv.org/abs/2308.10425)**. 2023 · CIKM Short.

  Studies how spatio-temporal adaptive embeddings improve a standard Transformer for traffic forecasting.

  [Publication evidence](https://github.com/XDZhelheim/STAEformer) · [Code](https://github.com/XDZhelheim/STAEformer) (author/project repository checked)

<a id="paper-gman"></a>

- **GMAN** — Chuanpan Zheng et al. **[GMAN: A Graph Multi-Attention Network for Traffic Prediction](https://arxiv.org/abs/1911.08415)**. 2020 · AAAI; first arXiv release: 2019.

  Directly produces multi-step traffic forecasts using multiple spatio-temporal attention mechanisms and transformation attention from history to the future.

  [Publication evidence](https://github.com/zhengchuanpan/GMAN) · [Code](https://github.com/zhengchuanpan/GMAN) (author/project repository checked)

<a id="paper-sttn"></a>

- **STTN** — Mingxing Xu et al. **[Spatial-Temporal Transformer Networks for Traffic Flow Forecasting](https://arxiv.org/abs/2001.02908)**. 2020 · arXiv; formal publication status not verified.

  Uses spatial and temporal Transformers to model dynamic directed spatial relationships and long-range temporal dependencies.

  [Publication evidence](https://arxiv.org/abs/2001.02908) · Code: author code not verified

  Version / usage notes: The verified arXiv version is listed here; this does not imply that no formally published version exists.
