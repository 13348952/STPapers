# Foundation models, language models, and cross-modal transfer

[简体中文](foundation.md) | [English](foundation.en.md) · [主题导航 / Topics](README.md) · [Full catalog](../README.en.md)

<a id="topic-foundation"></a>

## 08 · Foundation models, language models, and cross-modal transfer

Unified pretraining and few-shot or zero-shot adaptation.

<a id="paper-factost-v2"></a>

- **FactoST-v2** — Siru Zhong et al. **[Learning to Factorize and Adapt: A Versatile Approach Toward Universal Spatio-Temporal Foundation Models](https://arxiv.org/abs/2601.12083)**. 2026 · arXiv; formal publication status not verified.

  Separates general temporal pretraining from domain-specific spatial adaptation, extending to variable-length and probabilistic quantile forecasting.

  [Publication evidence](https://arxiv.org/abs/2601.12083) · [Code](https://github.com/CityMind-Lab/FactoST) (linked by the paper; returned HTTP 404 during verification)

  Version / usage notes: This 2026 extension is distinct from the NeurIPS 2025 conference version; the repository linked in the paper returned HTTP 404 during verification.

<a id="paper-st-vfm"></a>

- **ST-VFM** — Changlu Chen et al. **[Reprogramming Vision Foundation Models for Spatio-Temporal Forecasting](https://arxiv.org/abs/2507.11558)**. 2025 · arXiv; formal publication status not verified.

  Adapts a frozen vision foundation model to spatio-temporal forecasting through temporal adaptation and coordinated dual-branch prompts.

  [Publication evidence](https://arxiv.org/abs/2507.11558) · Code: author code not verified

<a id="paper-stllm"></a>

- **STLLM** — Chenxi Liu et al. **[Spatial-Temporal Large Language Model for Traffic Prediction](https://arxiv.org/abs/2401.10134)**. 2024 · IEEE MDM.

  Feeds spatio-temporal embeddings into a large language model and adapts it to traffic forecasting with partially frozen attention.

  [Publication evidence](https://github.com/ChenxiLiu-HNU/ST-LLM) · [Code](https://github.com/ChenxiLiu-HNU/ST-LLM) (author/project repository checked)

<a id="paper-unist"></a>

- **UniST** — Yuan Yuan et al. **[UniST: A Prompt-Empowered Universal Model for Urban Spatio-Temporal Prediction](https://arxiv.org/abs/2402.11838)**. 2024 · KDD.

  Explores a unified urban spatio-temporal forecasting model through multi-scenario pretraining and knowledge-guided prompting.

  [Publication evidence](https://github.com/tsinghua-fib-lab/UniST) · [Code](https://github.com/tsinghua-fib-lab/UniST) (author/project repository checked)

<a id="paper-urbangpt"></a>

- **UrbanGPT** — Zhonghang Li et al. **[UrbanGPT: Spatio-Temporal Large Language Models](https://arxiv.org/abs/2403.00813)**. 2024 · KDD.

  Combines a spatio-temporal dependency encoder with instruction tuning to explore zero-shot generalization across urban tasks.

  [Publication evidence](https://github.com/HKUDS/UrbanGPT) · [Code](https://github.com/HKUDS/UrbanGPT) (author/project repository checked)

<a id="paper-e2forecast"></a>

- **E2Forecast** — Jingtao Li et al. **[Forecasting Earth Surface Change in Embedding Space](https://arxiv.org/abs/2611.02211)**. 2026 · arXiv; formal publication status not verified.

  Forecasts future Earth-surface embeddings from irregular satellite histories using Gaussian and rectified-flow branches conditioned on a future query date.

  [Publication evidence](https://arxiv.org/abs/2611.02211) · [Code](https://github.com/ucam-eo/e2forecast) (author/project repository checked)

  Version / usage notes: Targets Earth-surface embeddings rather than raw pixels. The author repository contains model source and training/evaluation instructions; some GSA embeddings and dated SSL4EO data remain unreleased. No training was performed.

<a id="paper-topost"></a>

- **TopoST** — Kaiyun Wei et al. **[TopoST: Topology-Conditioned Node Specialization for Urban Spatio-Temporal Foundation Models](https://arxiv.org/abs/2611.15440)**. 2026 · arXiv; formal publication status not verified.

  Generates node-specific temporal and spatial parameters through a shared topology-to-parameter mapping for zero-shot forecasting across cities and tasks.

  [Publication evidence](https://arxiv.org/abs/2611.15440) · [Code](https://github.com/weikaiyun/TopoST) (author/project repository checked)

  Version / usage notes: Topology encoding, parameter-generation source, and training instructions were inspected. Zero-shot and data-separation claims require independent source/target protocol checks; no training was performed.

<a id="paper-multi-stg"></a>

- **Multi-STG** — Zhu Xiao et al. **[Beyond Sunny Skies: Using Large Language Models to Predict Urban Traffic in Adverse Weather](https://arxiv.org/abs/2611.12635)**. 2026 · arXiv; formal publication status not verified.

  Combines language-model semantic priors from weather, POIs, and holidays with multimodal attention and gated residual calibration for urban traffic forecasting in adverse weather.

  [Publication evidence](https://arxiv.org/abs/2611.12635) · Code: author code not verified

  Version / usage notes: Author code was not verified. External context and private-car data settings must be aligned across baselines; semantic representations do not establish causal weather effects on traffic.

<a id="paper-sceneadapter"></a>

- **SceneAdapter** — Han Fu et al. **[SceneAdapter: Boosting Time Series Foundation Models for Atypical-Scenario Traffic Flow Forecasting](https://drive.google.com/file/d/1FgPjiEYpwuluwosaF36xHqi78DOEMMJq/view?usp=drivesdk)**. 2026 · ACM SIGSPATIAL 2026.

  Adapts a frozen time-series foundation model with static, past-observed and future-known covariates to forecast traffic during holidays, events and road closures.

  [Publication evidence](https://sigspatial2026.sigspatial.org/detailed-program.html) · Code: author code not verified

  Version / usage notes: Verified against the conference program and the author manuscript.
