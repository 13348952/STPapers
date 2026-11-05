# Urban grid flow and demand forecasting

[简体中文](urban.md) | [English](urban.en.md) · [主题导航 / Topics](README.md) · [Full catalog](../README.en.md)

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
