# STPapers · Spatio-Temporal Forecasting Papers

[简体中文](README.md) | **English**

A curated paper list for **spatio-temporal forecasting / spatiotemporal prediction**, with datasets and author-code links. Covers traffic prediction, traffic flow forecasting, urban demand prediction, spatio-temporal graph neural networks, and weather forecasting.

**时空序列预测 / 时空预测 / 时空数据预测论文目录** — a bilingual Chinese–English catalog with weekly updates.

Inspired by the topic organization and contribution model of [RSPapers](https://github.com/hongleizhang/RSPapers), this repository collects papers, datasets, and code resources for spatio-temporal forecasting. Method summaries are editorial descriptions written for this catalog; paper titles retain their original English wording.

**Search cutoff: 2026-11-04 (Asia/Shanghai). 108 unique entries across 13 topics, covering 2015–2026; 24 papers are assigned to 2026 under the verified year convention, and 74 papers link to inspected author/project repositories.** Repository coverage is counted per paper; one toolkit can serve multiple papers.

Catalog updated: 2026-11-12. Targeted backfills do not advance the complete-search cutoff; see the [update log](updates/README.md) for actual coverage.

This is a representative collection centered on traffic and urban graph forecasting, with coverage of grid sequences, precipitation, and weather. It is neither an exhaustive review nor a performance leaderboard. 26 entries use verified preprint records; some may have formally published versions that were not confirmed in this search.

## Quick links

- [Browse by year](BY_YEAR.md) · [Recent papers (2025–2026)](RECENT.md) · [2025–2026 index](RECENT_2025_2026.md)
- [Datasets and tools](DATASETS.md) · [Search and verification notes](SEARCH_NOTES.md) · [Contributing](CONTRIBUTING.md)
- [CSV table](papers.csv) · [JSON catalog](papers.json) · [Draft BibTeX references](references.bib)
- [Changelog](CHANGELOG.md) · [Structural validation results](verification.json)
- [Weekly update log](updates/README.md) · [Monitoring workflow](MONITORING.md) · [Contributors](CONTRIBUTORS.md)
- [Standalone topic pages](topics/README.md) · [Tutorial-style reading guide](TUTORIALS.en.md)

The English README, topic pages, and reading guide cover the same catalog as their Chinese counterparts. Other supporting guides and secondary indexes are currently in Chinese; paper titles and source links are shared across both versions.

## Scope and labels

**Core scope:** tasks that forecast future time intervals and have explicit spatial locations, regions, graph structures, or two- or three-dimensional spatial fields. Relationships learned among variables may represent statistical dependencies; they do not automatically establish geographic relationships or causal propagation.

**Related background is listed separately:** general time-series baselines, imputation methods, and spatial extrapolation. CSDI primarily addresses imputation; STGNP infers target locations from surrounding observations. Video prediction architectures are included as background for grid forecasting. Trajectory planning, recommender systems, and static graph classification are outside the core catalog.

Years follow a verified formal publication when available, otherwise the first arXiv release. Differences between online publication and volume years are noted. Each paper has one primary category and is counted once, even if it spans multiple topics.

“Author/project repository checked” means that a paper-linked README or repository page was inspected. **No training runs or numerical reproduction were performed, and this label does not establish that complete training code and data are open.** Paper-only code links, access failures, and limited attribution evidence have separate labels. “Not verified” does not mean “does not exist.”

## Suggested reading paths

These are editorial suggestions, not rankings of model performance.

| Goal | Suggested order | Questions to examine |
| --- | --- | --- |
| Foundations of traffic graph forecasting | DCRNN → STGCN → Graph WaveNet → AGCRN → D²STGNN | How do fixed graphs, learned graphs, node heterogeneity, and dynamic dependencies differ? |
| Transformers and simple baselines | STID → GMAN → PDFormer → STAEformer | Do gains come from interaction operators, identity/time encodings, or training settings? |
| Large-scale traffic forecasting | LargeST → BigST → PatchSTG → GraphSparseNet → MiniST / HieraMix / FaST | How do node count, history length, and forecasting horizon each affect cost? |
| Self-supervised learning and transfer | STEP → STGCL → ST-SSL → STD-MAE → UniST / UrbanPG | How are pretraining information, domain overlap, and adaptation cost controlled? |
| Probabilistic forecasting | TimeGrad (background) → DiffSTG → SpecSTG → GenCast | How should point error, distribution calibration, and joint spatial consistency be evaluated together? |
| Grids and weather | ConvLSTM → PredRNN → SimVP → Earthformer → GraphCast / Aurora | What roles do local structure, long-range communication, physical constraints, and pretraining play? |

## Topics

| No. | Topic | Entries |
| --- | --- | ---: |
| 01 | [Surveys and introductions](#topic-survey) | 4 |
| 02 | [Urban grid flow and demand forecasting](#topic-urban) | 6 |
| 03 | [Graph convolutions, dynamic graphs, and continuous-time modeling](#topic-graph) | 17 |
| 04 | [Attention, Transformers, and state-space models](#topic-attention) | 7 |
| 05 | [Simple baselines, efficiency, and large-scale forecasting](#topic-efficient) | 13 |
| 06 | [Self-supervised learning and pretraining](#topic-pretrain) | 5 |
| 07 | [Heterogeneity, meta-learning, and transfer](#topic-transfer) | 6 |
| 08 | [Foundation models, language models, and cross-modal transfer](#topic-foundation) | 6 |
| 09 | [Probabilistic spatio-temporal graph forecasting](#topic-probabilistic) | 4 |
| 10 | [General grid and spatio-temporal frame prediction](#topic-grid) | 8 |
| 11 | [Precipitation, weather, and Earth-system forecasting](#topic-weather) | 16 |
| 12 | [Datasets, benchmarks, and tools](#topic-benchmark) | 8 |
| 13 | [Related tasks and time-series background](#topic-related) | 8 |

<a id="topic-survey"></a>

## 01 · Surveys and introductions

Maps of tasks, methods, and resources.

<a id="paper-stfm-survey"></a>

- **STFM-survey** — Yuxuan Liang et al. **[Foundation Models for Spatio-Temporal Data Science: A Tutorial and Survey](https://arxiv.org/abs/2503.13502)**. 2025 · arXiv; formal publication status not verified.

  Surveys spatio-temporal foundation models and their roles in sensing, management, and mining, providing broader background.

  [Publication evidence](https://arxiv.org/abs/2503.13502) · Code: author code not verified

<a id="paper-urban-stgnn-survey"></a>

- **Urban-STGNN-survey** — Guangyin Jin et al. **[Spatio-Temporal Graph Neural Networks for Predictive Learning in Urban Computing: A Survey](https://arxiv.org/abs/2303.14483)**. 2024 · IEEE TKDE; first arXiv release: 2023.

  Reviews spatio-temporal graph construction, model design, and predictive applications in urban computing.

  [Published version](https://doi.org/10.1109/TKDE.2023.3333824) · [Publication evidence](https://doi.org/10.1109/TKDE.2023.3333824) · Code: author code not verified

<a id="paper-traffic-survey"></a>

- **Traffic-survey** — Weiwei Jiang et al. **[Graph Neural Network for Traffic Forecasting: A Survey](https://arxiv.org/abs/2101.11174)**. 2022 · Expert Systems with Applications; first arXiv release: 2021.

  Reviews graph neural networks for traffic forecasting through graph construction, models, tasks, and open resources.

  [Publication evidence](https://arxiv.org/abs/2101.11174) · Code: author code not verified

<a id="paper-sttp-survey"></a>

- **STTP-survey** — Kyungeun Lee et al. **[Short-term Traffic Prediction with Deep Neural Networks: A Survey](https://arxiv.org/abs/2009.00712)**. 2020 · arXiv; formal publication status not verified.

  Organizes short-term traffic forecasting research by input representation, network architecture, applications, and data resources.

  [Publication evidence](https://arxiv.org/abs/2009.00712) · Code: author code not verified

  Version / usage notes: The verified arXiv version is listed here; this does not imply that no formally published version exists.


<a id="topic-urban"></a>

## 02 · Urban grid flow and demand forecasting

Regional inflows, outflows, and passenger demand, represented as grids or regional graphs.

<a id="paper-deepstn"></a>

- **DeepSTN** — Ziqian Lin et al. **[DeepSTN+: Context-Aware Spatial-Temporal Neural Network for Crowd Flow Prediction in Metropolis](https://ojs.aaai.org/index.php/AAAI/article/download/3892/3770)**. 2019 · AAAI.

  Combines long-range spatial dependencies, regional functions, and temporal context to forecast urban crowd inflows and outflows.

  [Publication evidence](https://github.com/vonfeng/DeepSTN) · [Code](https://github.com/vonfeng/DeepSTN) (author/project repository checked)

<a id="paper-stg2seq"></a>

- **STG2Seq** — Lei Bai et al. **[STG2Seq: Spatial-temporal Graph to Sequence Model for Multi-step Passenger Demand Forecasting](https://arxiv.org/abs/1905.10069)**. 2019 · IJCAI.

  Uses long- and short-term encoders, graph convolutions, and attention for multi-step passenger demand forecasting.

  [Publication evidence](https://github.com/LeiBAI/STG2Seq) · [Code](https://github.com/LeiBAI/STG2Seq) (author/project repository checked)

<a id="paper-stdn"></a>

- **STDN** — Huaxiu Yao et al. **[Revisiting Spatial-Temporal Similarity: A Deep Learning Framework for Traffic Prediction](https://arxiv.org/abs/1803.01254)**. 2019 · AAAI; first arXiv release: 2018.

  This paper proposes STDN, using a flow gating mechanism for dynamic spatial similarity and a shifted attention mechanism for non-strictly periodic temporal patterns. It directly addresses the common assumptions that spatial dependence is static and temporal patterns are perfectly periodic.

  [Published version](https://doi.org/10.1609/aaai.v33i01.33015668) · [Publication evidence](https://api.crossref.org/works/10.1609/aaai.v33i01.33015668) · [Code](https://github.com/tangxianfeng/STDN) (author/project repository checked)

  Version / usage notes: First released on arXiv in 2018 and published at AAAI in 2019. The author repository main.py and usage instructions were inspected; no training was run.

<a id="paper-st-mgcn"></a>

- **ST-MGCN** — Xu Geng et al. **[Spatiotemporal Multi-Graph Convolution Network for Ride-Hailing Demand Forecasting](https://doi.org/10.1609/aaai.v33i01.33013656)**. 2019 · AAAI.

  This paper proposes ST-MGCN, which models non-Euclidean inter-region dependencies with multiple graphs and uses a contextual gated recurrent network for temporal dynamics. It is designed for region-level ride-hailing demand forecasting rather than only local adjacency-based modeling.

  [Published version](https://doi.org/10.1609/aaai.v33i01.33013656) · [Publication evidence](https://api.crossref.org/works/10.1609/aaai.v33i01.33013656) · Code: author code not verified

  Version / usage notes: Publisher-deposited Crossref metadata and abstract were checked. Direct publisher-page access was restricted during this check; author code was not verified.

<a id="paper-dmvst-net"></a>

- **DMVST-Net** — Huaxiu Yao et al. **[Deep Multi-View Spatial-Temporal Network for Taxi Demand Prediction](https://arxiv.org/abs/1802.08714)**. 2018 · AAAI.

  This paper proposes DMVST-Net, which combines temporal, local spatial, and semantic views to model taxi demand dynamics. It targets the limitation of using only CNN or LSTM to capture both spatial and temporal dependencies in citywide demand prediction.

  [Published version](https://doi.org/10.1609/aaai.v32i1.11836) · [Publication evidence](https://api.crossref.org/works/10.1609/aaai.v32i1.11836) · [Code](https://github.com/huaxiuyao/DMVST-Net) (author/project repository checked)

  Version / usage notes: The author repository explicitly provides only the model component and does not release the raw data. model.py was inspected; this is not a complete reproduction package.

<a id="paper-st-resnet"></a>

- **ST-ResNet** — Junbo Zhang et al. **[Deep Spatio-Temporal Residual Networks for Citywide Crowd Flows Prediction](https://arxiv.org/abs/1610.00081)**. 2017 · AAAI; first arXiv release: 2016.

  Models recent, periodic, and trend components of urban grid inflows and outflows, integrating external factors.

  [Publication evidence](https://arxiv.org/abs/1610.00081) · Code: author code not verified


<a id="topic-graph"></a>

## 03 · Graph convolutions, dynamic graphs, and continuous-time modeling

Spatial dependencies and temporal dynamics of road or sensor nodes.

<a id="paper-strp"></a>

- **STRP** — Shuhao Li et al. **[From Coarse to Fine: Managing Temporal Granularity in Spatio-Temporal Data for Fine-Grained Traffic Prediction](https://arxiv.org/abs/2606.09392)**. 2026 · arXiv; formal publication status not verified.

  This paper studies traffic forecasting across temporal granularities: predicting fine-grained future traffic from coarsely sampled history, using Tree Convolution for spatial modeling and Inverse Dilated Convolution for progressive temporal extrapolation, while distinguishing window-based and duration-based settings.

  [Publication evidence](https://arxiv.org/abs/2606.09392) · Code: author code not verified

  Version / usage notes: Input and output temporal granularity differs from conventional same-resolution forecasting. Listed as an arXiv preprint; a formal publication and author code were not verified.

<a id="paper-igstgnn"></a>

- **IGSTGNN** — Lixiang Fan et al. **[Incident-Guided Spatiotemporal Traffic Forecasting](https://arxiv.org/abs/2602.02528)**. 2026 · KDD.

  This paper proposes Incident-Guided Spatiotemporal Traffic Forecasting, combining incident-context spatial fusion (ICSF) and temporal incident impact decay (TIID) to model traffic history together with external incident information, and it includes a traffic/incident-aligned dataset.

  [Published version](https://doi.org/10.1145/3770854.3780215) · [Publication evidence](https://github.com/fanlixiang/IGSTGNN) · [Code](https://github.com/fanlixiang/IGSTGNN) (author/project repository checked)

  Version / usage notes: KDD 2026 attribution follows the author repository citation; the publisher page was not accessible during this check. Align the availability time and scope of incident inputs in comparisons. The training entry point was inspected; no experiments were run.

<a id="paper-dgcrn"></a>

- **DGCRN** — Fuxian Li et al. **[Dynamic Graph Convolutional Recurrent Network for Traffic Prediction: Benchmark and Solution](https://arxiv.org/abs/2104.14917)**. 2023 · ACM TKDD; first arXiv release: 2021.

  Generates graph structures from dynamic node information and provides a unified evaluation framework and implementation for traffic forecasting.

  [Publication evidence](https://github.com/tsinghua-fib-lab/Traffic-Benchmark) · [Code](https://github.com/tsinghua-fib-lab/Traffic-Benchmark) (author/project repository checked)

<a id="paper-d2stgnn"></a>

- **D2STGNN** — Zezhi Shao et al. **[Decoupled Dynamic Spatial-Temporal Graph Neural Network for Traffic Forecasting](https://arxiv.org/abs/2206.09112)**. 2022 · PVLDB.

  Separates traffic signals into diffusion and inherent components, modeling them with dynamic graph learning.

  [Publication evidence](https://github.com/GestaltCogTeam/D2STGNN) · [Code](https://github.com/GestaltCogTeam/D2STGNN) (author/project repository checked)

<a id="paper-dstagnn"></a>

- **DSTAGNN** — Shiyong Lan et al. **[DSTAGNN: Dynamic Spatial-Temporal Aware Graph Neural Network for Traffic Flow Forecasting](https://proceedings.mlr.press/v162/lan22a.html)**. 2022 · ICML.

  Combines dynamic spatio-temporal relationship modeling with graph networks for traffic forecasting.

  [Published version](https://proceedings.mlr.press/v162/lan22a.html) · [Publication evidence](https://proceedings.mlr.press/v162/lan22a.html) · [Code](https://github.com/SYLan2019/DSTAGNN) (author/project repository checked)

<a id="paper-stgncde"></a>

- **STGNCDE** — Jeongwhan Choi et al. **[Graph Neural Controlled Differential Equations for Traffic Forecasting](https://arxiv.org/abs/2112.03558)**. 2022 · AAAI; first arXiv release: 2021.

  Combines spatial and temporal neural controlled differential equations for continuous-time modeling.

  [Publication evidence](https://github.com/jeongwhanchoi/STG-NCDE) · [Code](https://github.com/jeongwhanchoi/STG-NCDE) (author/project repository checked)

<a id="paper-gts"></a>

- **GTS** — Chao Shang et al. **[Discrete Graph Structure Learning for Forecasting Multiple Time Series](https://arxiv.org/abs/2101.06861)**. 2021 · ICLR.

  Learns a discrete graph distribution with differentiable sampling, jointly optimized with a forecasting model for multiple time series.

  [Publication evidence](https://github.com/chaoshangcs/GTS) · [Code](https://github.com/chaoshangcs/GTS) (author/project repository checked)

<a id="paper-stfgnn"></a>

- **STFGNN** — Mengzhang Li et al. **[Spatial-Temporal Fusion Graph Neural Networks for Traffic Flow Forecasting](https://arxiv.org/abs/2012.09641)**. 2021 · AAAI; first arXiv release: 2020.

  Fuses spatial graphs with data-driven temporal relationship graphs and combines them with gated convolutions.

  [Publication evidence](https://github.com/MengzhangLI/STFGNN) · [Code](https://github.com/MengzhangLI/STFGNN) (author/project repository checked)

  Version / usage notes: The authors' README corrects results for some datasets; check the latest paper and repository before comparing numbers.

<a id="paper-stgode"></a>

- **STGODE** — Zheng Fang et al. **[Spatial-Temporal Graph ODE Networks for Traffic Flow Forecasting](https://arxiv.org/abs/2106.12931)**. 2021 · KDD.

  Models spatio-temporal dynamics using tensor-based ordinary differential equations, considering both spatial and semantic relationships.

  [Publication evidence](https://github.com/square-coder/STGODE) · [Code](https://github.com/square-coder/STGODE) (author/project repository checked)

<a id="paper-agcrn"></a>

- **AGCRN** — Lei Bai et al. **[Adaptive Graph Convolutional Recurrent Network for Traffic Forecasting](https://arxiv.org/abs/2007.02842)**. 2020 · NeurIPS.

  Combines node-adaptive parameter learning with adaptive graph generation to capture distinct forecasting patterns across nodes.

  [Publication evidence](https://github.com/LeiBAI/AGCRN) · [Code](https://github.com/LeiBAI/AGCRN) (author/project repository checked)

<a id="paper-mtgnn"></a>

- **MTGNN** — Zonghan Wu et al. **[Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks](https://arxiv.org/abs/2005.11650)**. 2020 · KDD.

  Jointly learns a directed graph among variables, mix-hop propagation, and temporal convolutions for general multivariate series and traffic tasks.

  [Publication evidence](https://github.com/nnzhan/MTGNN) · [Code](https://github.com/nnzhan/MTGNN) (author/project repository checked)

  Version / usage notes: A general multivariate model included in the main catalog because it explicitly covers traffic tasks and graph learning.

<a id="paper-stsgcn"></a>

- **STSGCN** — Chao Song et al. **[Spatial-Temporal Synchronous Graph Convolutional Networks: A New Framework for Spatial-Temporal Network Data Forecasting](https://ojs.aaai.org/index.php/AAAI/article/view/5438)**. 2020 · AAAI.

  Connects nodes across adjacent time steps into local spatio-temporal graphs to jointly model local relationships and heterogeneity.

  [Published version](https://ojs.aaai.org/index.php/AAAI/article/view/5438) · [Publication evidence](https://ojs.aaai.org/index.php/AAAI/article/download/5438/5294) · [Code](https://github.com/Davidham3/STSGCN) (author/project repository checked)

<a id="paper-astgcn"></a>

- **ASTGCN** — Shengnan Guo et al. **[Attention Based Spatial-Temporal Graph Convolutional Networks for Traffic Flow Forecasting](https://ojs.aaai.org/index.php/AAAI/article/view/3881)**. 2019 · AAAI.

  Forecasts traffic flow using spatio-temporal attention, graph convolutions, and recent, daily, and weekly branches.

  [Published version](https://ojs.aaai.org/index.php/AAAI/article/view/3881) · [Publication evidence](https://ojs.aaai.org/index.php/AAAI/article/view/3881) · [Code](https://github.com/guoshnBJTU/ASTGCN-2019-pytorch) (author/project repository checked)

  Version / usage notes: The linked author-maintained PyTorch repository states that it implements only the recent branch; do not assume it is the full three-branch ASTGCN.

<a id="paper-graph-wavenet"></a>

- **Graph-WaveNet** — Zonghan Wu et al. **[Graph WaveNet for Deep Spatial-Temporal Graph Modeling](https://arxiv.org/abs/1906.00121)**. 2019 · IJCAI.

  Learns adaptive adjacency through node embeddings and models historical sequences with dilated temporal convolutions.

  [Publication evidence](https://github.com/nnzhan/Graph-WaveNet) · [Code](https://github.com/nnzhan/Graph-WaveNet) (author/project repository checked)

<a id="paper-dcrnn"></a>

- **DCRNN** — Yaguang Li et al. **[Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting](https://arxiv.org/abs/1707.01926)**. 2018 · ICLR; first arXiv release: 2017.

  Combines directed graph diffusion convolutions with a recurrent encoder-decoder, offering a starting point for road-network forecasting.

  [Publication evidence](https://github.com/liyaguang/DCRNN) · [Code](https://github.com/liyaguang/DCRNN) (author/project repository checked)

<a id="paper-stgcn"></a>

- **STGCN** — Bing Yu et al. **[Spatio-Temporal Graph Convolutional Networks: A Deep Learning Framework for Traffic Forecasting](https://arxiv.org/abs/1709.04875)**. 2018 · IJCAI; first arXiv release: 2017.

  Builds a fully convolutional spatio-temporal forecasting network from graph and temporal convolutions.

  [Publication evidence](https://github.com/VeritasYin/STGCN_IJCAI-18) · [Code](https://github.com/VeritasYin/STGCN_IJCAI-18) (author/project repository checked)

<a id="paper-atpo"></a>

- **ATPO** — Hongxin Yu et al. **[Uncertainty-Aware Coordinated Multi-Ramp Metering Based on an Action-Conditioned Traffic Prediction Operator Under Sparse Observations](https://arxiv.org/abs/2611.01270)**. 2026 · arXiv; formal publication status not verified.

  Predicts future density and speed distributions from sparse traffic observations, missingness masks, and candidate control actions for uncertainty-aware coordinated ramp metering.

  [Publication evidence](https://arxiv.org/abs/2611.01270) · Code: author code not verified

  Version / usage notes: Action-conditioned prediction uses different inputs from passive traffic forecasting. Evaluation uses a simulated corridor and does not establish field deployment; author code was not verified.


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


<a id="topic-pretrain"></a>

## 06 · Self-supervised learning and pretraining

Contrastive learning, masked modeling, and their use in downstream forecasting.

<a id="paper-hgaurban"></a>

- **HGAurban** — Qianru Zhang et al. **[HGAurban: Heterogeneous Graph Autoencoding for Urban Spatial-Temporal Learning](https://arxiv.org/abs/2410.10915)**. 2025 · CIKM; first arXiv release: 2024.

  Learns regional representations with a heterogeneous graph masked autoencoder for urban spatio-temporal tasks, including tasks beyond forecasting.

  [Publication evidence](https://arxiv.org/abs/2410.10915) · Code: author code not verified

  Version / usage notes: The current arXiv title is HGAurban. Earlier search records used Graph Masked Autoencoder; these are merged under the same identifier.

<a id="paper-stdmae"></a>

- **STDMAE** — Haotian Gao et al. **[Spatial-Temporal-Decoupled Masked Pre-training for Spatiotemporal Forecasting](https://arxiv.org/abs/2312.00516)**. 2024 · IJCAI; first arXiv release: 2023.

  Performs masked reconstruction separately along spatial and temporal dimensions, using pretrained representations for downstream forecasting.

  [Publication evidence](https://github.com/Jimmy-7664/STD-MAE) · [Code](https://github.com/Jimmy-7664/STD-MAE) (author/project repository checked)

<a id="paper-stssl"></a>

- **STSSL** — Jiahao Ji et al. **[Spatio-Temporal Self-Supervised Learning for Traffic Flow Prediction](https://arxiv.org/abs/2212.04475)**. 2023 · AAAI; first arXiv release: 2022.

  Learns heterogeneous traffic patterns through adaptive graph augmentation and spatial and temporal self-supervised tasks.

  [Publication evidence](https://github.com/Echo-Ji/ST-SSL) · [Code](https://github.com/Echo-Ji/ST-SSL) (author/project repository checked)

<a id="paper-step"></a>

- **STEP** — Zezhi Shao et al. **[Pre-training Enhanced Spatial-temporal Graph Neural Network for Multivariate Time Series Forecasting](https://arxiv.org/abs/2206.09113)**. 2022 · KDD.

  Pretrains on long historical sequences to provide temporal context and structural information for downstream graph forecasting models.

  [Publication evidence](https://github.com/GestaltCogTeam/STEP) · [Code](https://github.com/GestaltCogTeam/STEP) (author/project repository checked)

<a id="paper-stgcl"></a>

- **STGCL** — Xu Liu et al. **[When Do Contrastive Learning Signals Help Spatio-Temporal Graph Forecasting?](https://arxiv.org/abs/2108.11873)**. 2022 · ACM SIGSPATIAL; first arXiv release: 2021.

  Systematically compares ways to integrate spatio-temporal graph contrastive learning, augmentation strategies, and negative-sample selection.

  [Publication evidence](https://github.com/liuxu77/STGCL) · [Code](https://github.com/liuxu77/STGCL) (author/project repository checked)


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


<a id="topic-probabilistic"></a>

## 09 · Probabilistic spatio-temporal graph forecasting

Predicting future distributions or samples rather than only point estimates.

<a id="paper-specstg"></a>

- **SpecSTG** — Lequan Lin et al. **[SpecSTG: A Fast Spectral Diffusion Framework for Probabilistic Spatio-Temporal Traffic Forecasting](https://arxiv.org/abs/2401.08119)**. 2024 · arXiv; formal publication status not verified.

  Generates future sequences in the spectral domain, incorporating spatial dependencies and spectral graph convolutions.

  [Publication evidence](https://arxiv.org/abs/2401.08119) · [Code](https://anonymous.4open.science/r/SpecSTG) (anonymous code linked by the paper; access not verified)

  Version / usage notes: The verified arXiv version is listed here; this does not imply that no formally published version exists.

<a id="paper-diffstg"></a>

- **DiffSTG** — Haomin Wen et al. **[DiffSTG: Probabilistic Spatio-Temporal Graph Forecasting with Denoising Diffusion Models](https://arxiv.org/abs/2301.13629)**. 2023 · ACM SIGSPATIAL.

  Extends denoising diffusion models to spatio-temporal graphs for non-autoregressive probabilistic forecasting.

  [Publication evidence](https://arxiv.org/abs/2301.13629) · Code: author code not verified

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


<a id="topic-grid"></a>

## 10 · General grid and spatio-temporal frame prediction

Architectural foundations for weather and urban grid forecasting, including video prediction background.

<a id="paper-tau"></a>

- **TAU** — Cheng Tan et al. **[Temporal Attention Unit: Towards Efficient Spatiotemporal Predictive Learning](https://arxiv.org/abs/2206.12126)**. 2023 · CVPR; first arXiv release: 2022.

  Splits temporal attention into within-frame and across-frame components to improve parallel spatio-temporal frame prediction.

  [Publication evidence](https://github.com/chengtan9907/OpenSTL) · [Code](https://github.com/chengtan9907/OpenSTL) (implementation in the authors' toolkit checked)

<a id="paper-simvp"></a>

- **SimVP** — Zhangyang Gao et al. **[SimVP: Simpler yet Better Video Prediction](https://arxiv.org/abs/2206.05099)**. 2022 · CVPR.

  Provides a simple video and grid forecasting baseline using a convolutional encoder, a temporal processing module, and a decoder.

  [Publication evidence](https://github.com/gaozhangyang/SimVP-Simpler-yet-Better-Video-Prediction) · [Code](https://github.com/gaozhangyang/SimVP-Simpler-yet-Better-Video-Prediction) (author/project repository checked)

<a id="paper-phydnet"></a>

- **PhyDNet** — Vincent Le Guen et al. **[Disentangling Physical Dynamics from Unknown Factors for Unsupervised Video Prediction](https://arxiv.org/abs/2003.01460)**. 2020 · CVPR.

  Separates interpretable physical dynamics from unknown residual factors for future-frame prediction.

  [Publication evidence](https://github.com/vincent-leguen/PhyDNet) · [Code](https://github.com/vincent-leguen/PhyDNet) (author/project repository checked)

<a id="paper-mim"></a>

- **MIM** — Yunbo Wang et al. **[Memory In Memory: A Predictive Neural Network for Learning Higher-Order Non-Stationarity from Spatiotemporal Dynamics](https://arxiv.org/abs/1811.07490)**. 2019 · CVPR; first arXiv release: 2018.

  Uses memory modules to handle higher-order nonstationary changes in spatio-temporal sequences.

  [Publication evidence](https://github.com/Yunbo426/MIM) · [Code](https://github.com/Yunbo426/MIM) (author/project repository checked)

<a id="paper-predrnnpp"></a>

- **PredRNNpp** — Yunbo Wang et al. **[PredRNN++: Towards A Resolution of the Deep-in-Time Dilemma in Spatiotemporal Predictive Learning](https://arxiv.org/abs/1804.06300)**. 2018 · ICML.

  Uses causal LSTMs and gradient pathways to ease optimization in deep recurrent prediction.

  [Publication evidence](https://github.com/Yunbo426/predrnn-pp) · [Code](https://github.com/Yunbo426/predrnn-pp) (author/project repository checked)

<a id="paper-predrnn"></a>

- **PredRNN** — Yunbo Wang et al. **[PredRNN: Recurrent Neural Networks for Predictive Learning using Spatiotemporal LSTMs](https://papers.nips.cc/paper/6689-predrnn-recurrent-neural-networks-for-predictive-learning-using-spatiotemporal-lstms)**. 2017 · NeurIPS.

  Models future frames using spatio-temporal LSTMs and dual memory states, providing general spatio-temporal prediction background.

  [Published version](https://papers.nips.cc/paper/6689-predrnn-recurrent-neural-networks-for-predictive-learning-using-spatiotemporal-lstms) · [Publication evidence](https://papers.nips.cc/paper/6689-predrnn-recurrent-neural-networks-for-predictive-learning-using-spatiotemporal-lstms) · [Code](https://github.com/thuml/predrnn-pytorch) (author/project repository checked)

<a id="paper-trajgru"></a>

- **TrajGRU** — Xingjian Shi et al. **[Deep Learning for Precipitation Nowcasting: A Benchmark and A New Model](https://arxiv.org/abs/1706.03458)**. 2017 · NeurIPS.

  Learns location-dependent recurrent connections for precipitation nowcasting and provides a corresponding benchmark.

  [Publication evidence](https://arxiv.org/abs/1706.03458) · Code: author code not verified

<a id="paper-convlstm"></a>

- **ConvLSTM** — Xingjian Shi et al. **[Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting](https://arxiv.org/abs/1506.04214)**. 2015 · NeurIPS.

  Introduces convolutions into LSTM state transitions, providing a foundational architecture for grid sequences and precipitation nowcasting.

  [Published version](https://papers.nips.cc/paper_files/paper/2015/hash/07563a3fe3bbe7e3ba84431ad9d055af-Abstract.html) · [Publication evidence](https://papers.nips.cc/paper_files/paper/2015/hash/07563a3fe3bbe7e3ba84431ad9d055af-Abstract.html) · Code: author code not verified


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


<a id="topic-benchmark"></a>

## 12 · Datasets, benchmarks, and tools

Task definitions, data processing, metrics, and resources for reproduction.

<a id="paper-traffident"></a>

- **TraffiDent** — Xiaochuan Gou et al. **[TraffiDent: A Dataset for Understanding the Interplay Between Traffic Dynamics and Incidents](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html)**. 2025 · NeurIPS Datasets and Benchmarks.

  Aligns traffic states, incidents, and road attributes to support post-incident traffic forecasting and related analysis.

  [Published version](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html) · [Publication evidence](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html) · Code: author code not verified

<a id="paper-basicts"></a>

- **BasicTS** — Zezhi Shao et al. **[Exploring Progress in Multivariate Time Series Forecasting: Comprehensive Benchmarking and Heterogeneity Analysis](https://arxiv.org/abs/2310.06119)**. 2024 · IEEE TKDE; first arXiv release: 2023.

  Uses a unified evaluation pipeline and spatio-temporal heterogeneity analysis to examine why multivariate forecasting results are difficult to compare directly.

  [Publication evidence](https://github.com/GestaltCogTeam/BasicTS) · [Code](https://github.com/GestaltCogTeam/BasicTS) (author/project repository checked)

<a id="paper-weatherbench2"></a>

- **WeatherBench2** — Stephan Rasp et al. **[WeatherBench 2: A Benchmark for the Next Generation of Data‐Driven Global Weather Models](https://arxiv.org/abs/2308.15560)**. 2024 · Journal of Advances in Modeling Earth Systems; first arXiv release: 2023.

  Updates the medium-range weather evaluation framework with benchmark data, physical and data-driven baselines, and evaluation protocols.

  [Published version](https://doi.org/10.1029/2023MS004019) · [Publication evidence](https://doi.org/10.1029/2023MS004019) · [Code](https://github.com/google-research/weatherbench2) (author/project repository checked)

<a id="paper-largest"></a>

- **LargeST** — Xu Liu et al. **[LargeST: A Benchmark Dataset for Large-Scale Traffic Forecasting](https://arxiv.org/abs/2306.08259)**. 2023 · NeurIPS Datasets and Benchmarks.

  Provides large-scale, multi-year traffic sensor data and metadata for studying forecasting accuracy and computational cost.

  [Publication evidence](https://github.com/liuxu77/LargeST) · [Code](https://github.com/liuxu77/LargeST) (author/project repository checked)

<a id="paper-libcity"></a>

- **LibCity** — Jiawei Jiang et al. **[LibCity: A Unified Library Towards Efficient and Comprehensive Urban Spatial-Temporal Prediction](https://arxiv.org/abs/2304.14343)**. 2023 · arXiv; formal publication status not verified.

  Organizes urban forecasting models, data formats, and evaluation pipelines into a unified library; this entry covers the extended manuscript.

  [Publication evidence](https://arxiv.org/abs/2304.14343) · [Code](https://github.com/LibCity/Bigscity-LibCity) (author/project repository checked)

  Version / usage notes: This entry covers the 2023 extended preprint; publication details of the earlier tool paper are not applied to the extension.

<a id="paper-openstl"></a>

- **OpenSTL** — Cheng Tan et al. **[OpenSTL: A Comprehensive Benchmark of Spatio-Temporal Predictive Learning](https://arxiv.org/abs/2306.11249)**. 2023 · NeurIPS Datasets and Benchmarks.

  Unifies multiple spatio-temporal frame prediction models and evaluation tasks across video, traffic grids, and weather.

  [Publication evidence](https://github.com/chengtan9907/OpenSTL) · [Code](https://github.com/chengtan9907/OpenSTL) (author/project repository checked)

<a id="paper-sevir"></a>

- **SEVIR** — Mark Veillette et al. **[SEVIR : A Storm Event Imagery Dataset for Deep Learning Applications in Radar and Satellite Meteorology](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html)**. 2020 · NeurIPS.

  Provides spatio-temporally aligned radar and satellite imagery of storm events for precipitation forecasting and cross-sensor tasks.

  [Published version](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html) · [Publication evidence](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html) · [Code](https://github.com/MIT-AI-Accelerator/neurips-2020-sevir) (author/project repository checked)

<a id="paper-weatherbench"></a>

- **WeatherBench** — Stephan Rasp et al. **[WeatherBench: A Benchmark Data Set for Data‐Driven Weather Forecasting](https://arxiv.org/abs/2002.00469)**. 2020 · Journal of Advances in Modeling Earth Systems.

  Provides data, baselines, and common metrics for data-driven weather forecasting.

  [Published version](https://doi.org/10.1029/2020MS002203) · [Publication evidence](https://doi.org/10.1029/2020MS002203) · [Code](https://github.com/pangeo-data/WeatherBench) (author/project repository checked)


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

## Conditions to align before comparing papers

Data versions, temporal splits, sampling intervals, input windows, forecasting steps, missing/zero-value masks, normalization, external modalities, pretraining data, validation-based selection, and compute budgets all affect comparisons. Select configurations using the validation set, then evaluate the selected model on the test set; do not use test results to select configurations.

LargeST's SD/GBA/GLA/CA, classic PeMS subsets, METR-LA/PEMS-BAY, and meteorological ERA5/SEVIR involve different tasks and metrics and should not be combined into a single ranking. Publication year and code availability alone do not establish that a model is stronger.

## Maintenance

`papers.json` is the single source of paper data, including `summary_zh` / `summary_en` and `notes` / `notes_en`. After editing it, run `python scripts/build_catalog.py` from the repository root to regenerate both READMEs, year indexes, CSV, and BibTeX, then run `python scripts/verify_catalog.py` and `git diff --check` for independent validation and whitespace checks. Contribution guidelines are in [CONTRIBUTING.md](CONTRIBUTING.md).

Weekly searches verify new papers and official code links, deduplicate entries, and update the catalog. Additions, revisions, and items awaiting verification are recorded in the [update log](updates/README.md). The search cutoff is stored in `catalog_meta.json` and advances only after a completed search. New or revised entries must maintain both language versions; missing English summaries, notes, or code-status translations cause generation to fail.

## Contributors

- [13348952](https://github.com/13348952): project founder and maintainer.
- **Codex (OpenAI)**: AI-assisted literature search, source and code-link verification, categorization, summaries, catalog generation, and ongoing maintenance. See [contribution details](CONTRIBUTORS.md).

This repository collects bibliographic information, links, and original short descriptions. Papers, datasets, code, and models remain subject to their authors' and publishers' respective licenses. Its organization is inspired by RSPapers; its contents were searched and organized around spatio-temporal forecasting.
