# General grid and spatio-temporal frame prediction

[简体中文](grid.md) | [English](grid.en.md) · [主题导航 / Topics](README.md) · [Full catalog](../README.en.md)

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
