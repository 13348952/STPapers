# Graph convolutions, dynamic graphs, and continuous-time modeling

[简体中文](graph.md) | [English](graph.en.md) · [主题导航 / Topics](README.md) · [Full catalog](../README.en.md)

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
