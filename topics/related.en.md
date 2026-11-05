# Related tasks and time-series background

[简体中文](related.md) | [English](related.en.md) · [主题导航 / Topics](README.md) · [Full catalog](../README.en.md)

<a id="topic-related"></a>

## 13 · Related tasks and time-series background

Time-series baselines, imputation, and spatial extrapolation; task definitions and physical-space assumptions are distinguished.

<a id="paper-itransformer"></a>

- **iTransformer** — Yong Liu et al. **[iTransformer: Inverted Transformers Are Effective for Time Series Forecasting](https://arxiv.org/abs/2310.06625)**. 2024 · ICLR; first arXiv release: 2023.

  Treats variables rather than time steps as tokens, serving as a general baseline for cross-variable modeling.

  [Publication evidence](https://github.com/thuml/iTransformer) · [Code](https://github.com/thuml/iTransformer) (author/project repository checked)

<a id="paper-dlinear"></a>

- **DLinear** — Ailing Zeng et al. **[Are Transformers Effective for Time Series Forecasting?](https://arxiv.org/abs/2205.13504)**. 2023 · AAAI; first arXiv release: 2022.

  Revisits long-sequence forecasting using decomposition and linear layers, providing a simple temporal baseline for complex models.

  [Publication evidence](https://github.com/cure-lab/LTSF-Linear) · [Code](https://github.com/cure-lab/LTSF-Linear) (author/project repository checked)

<a id="paper-patchtst"></a>

- **PatchTST** — Yuqi Nie et al. **[A Time Series is Worth 64 Words: Long-term Forecasting with Transformers](https://arxiv.org/abs/2211.14730)**. 2023 · ICLR; first arXiv release: 2022.

  Splits time series into patches and uses a channel-independent Transformer as a general temporal baseline.

  [Publication evidence](https://github.com/yuqinie98/PatchTST) · [Code](https://github.com/yuqinie98/PatchTST) (author/project repository checked)

<a id="paper-timesnet"></a>

- **TimesNet** — Haixu Wu et al. **[TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis](https://arxiv.org/abs/2210.02186)**. 2023 · ICLR; first arXiv release: 2022.

  Maps periodic variations into two-dimensional structures to jointly model within-period and across-period changes.

  [Publication evidence](https://github.com/thuml/TimesNet) · [Code](https://github.com/thuml/TimesNet) (author/project repository checked)

<a id="paper-stgnp"></a>

- **STGNP** — Junfeng Hu et al. **[Graph Neural Processes for Spatio-Temporal Extrapolation](https://arxiv.org/abs/2305.18719)**. 2023 · KDD.

  This paper generalizes neural processes to spatio-temporal graph extrapolation, where the goal is to infer target locations from surrounding context nodes. It combines causal temporal encoding, cross-set graph reasoning, and Bayesian aggregation to model uncertainty.

  [Published version](https://doi.org/10.1145/3580305.3599372) · [Publication evidence](https://api.crossref.org/works/10.1145/3580305.3599372) · [Code](https://github.com/hjf1997/STGNP) (author/project repository checked)

  Version / usage notes: Related task: inferring target locations from surrounding observations is distinct from forecasting future time intervals. The author repository hierarchical model and usage instructions were inspected; no experiments were run.

<a id="paper-graphdf"></a>

- **GraphDF** — Hongjie Chen et al. **[Graph Deep Factors for Probabilistic Time-series Forecasting](https://arxiv.org/abs/2010.07373)**. 2023 · ACM TKDD; first arXiv release: 2020.

  Combines relational global and local probabilistic models for dependent time series; the journal version also studies online incremental learning.

  [Published version](https://doi.org/10.1145/3543511) · [Publication evidence](https://api.crossref.org/works/10.1145/3543511) · Code: author code not verified

  Version / usage notes: Related background: probabilistic forecasting of graph-related time series without assuming geographical structure. The 2023 TKDD article extends the 2020 preprint with online incremental learning; both versions are represented by one entry. Author code was not verified.

<a id="paper-csdi"></a>

- **CSDI** — Yusuke Tashiro et al. **[CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation](https://arxiv.org/abs/2107.03502)**. 2021 · NeurIPS.

  Primarily studies conditional diffusion for time-series imputation; included as missing-data background rather than a direct spatio-temporal forecasting model.

  [Publication evidence](https://github.com/ermongroup/CSDI) · [Code](https://github.com/ermongroup/CSDI) (author/project repository checked)

  Version / usage notes: The primary task is imputation; it is not counted as a direct spatio-temporal forecasting method.

<a id="paper-timegrad"></a>

- **TimeGrad** — Kashif Rasul et al. **[Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting](https://arxiv.org/abs/2101.12072)**. 2021 · ICML.

  Uses autoregressive denoising diffusion for multivariate probabilistic forecasting, providing a probabilistic modeling reference.

  [Publication evidence](https://arxiv.org/abs/2101.12072) · Code: author code not verified
