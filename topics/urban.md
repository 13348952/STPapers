# 城市网格流量与需求预测

[简体中文](urban.md) | [English](urban.en.md) · [主题导航 / Topics](README.md) · [返回主目录](../README.md)

<a id="topic-urban"></a>

## 02 · 城市网格流量与需求预测

区域流入/流出和乘客需求，空间可表现为网格或区域图。

<a id="paper-deepstn"></a>

- **DeepSTN** — Ziqian Lin et al. **[DeepSTN+: Context-Aware Spatial-Temporal Neural Network for Crowd Flow Prediction in Metropolis](https://ojs.aaai.org/index.php/AAAI/article/download/3892/3770)**. 2019 · AAAI.

  结合长距离空间依赖、区域功能与时间上下文，预测城市人群流入/流出量。

  [发表证据](https://github.com/vonfeng/DeepSTN) · [代码](https://github.com/vonfeng/DeepSTN)（作者/项目仓库已核验）

<a id="paper-stg2seq"></a>

- **STG2Seq** — Lei Bai et al. **[STG2Seq: Spatial-temporal Graph to Sequence Model for Multi-step Passenger Demand Forecasting](https://arxiv.org/abs/1905.10069)**. 2019 · IJCAI.

  用长短期编码器、图卷积和注意力进行多步乘客需求预测。

  [发表证据](https://github.com/LeiBAI/STG2Seq) · [代码](https://github.com/LeiBAI/STG2Seq)（作者/项目仓库已核验）

<a id="paper-stdn"></a>

- **STDN** — Huaxiu Yao et al. **[Revisiting Spatial-Temporal Similarity: A Deep Learning Framework for Traffic Prediction](https://arxiv.org/abs/1803.01254)**. 2019 · AAAI；arXiv 首发 2018.

  这篇论文提出 STDN，通过流门控机制学习动态空间相似性，并用周期偏移注意力处理非严格周期的时间动态。它直接回应了交通预测里“空间关系静态、时间规律严格周期化”的常见假设。

  [正式版本](https://doi.org/10.1609/aaai.v33i01.33015668) · [发表证据](https://api.crossref.org/works/10.1609/aaai.v33i01.33015668) · [代码](https://github.com/tangxianfeng/STDN)（作者/项目仓库已核验）

  版本/使用说明：arXiv 首发于 2018 年，正式 AAAI 版本为 2019 年；已检查作者仓库 main.py 与运行说明，未训练复现。

<a id="paper-st-mgcn"></a>

- **ST-MGCN** — Xu Geng et al. **[Spatiotemporal Multi-Graph Convolution Network for Ride-Hailing Demand Forecasting](https://doi.org/10.1609/aaai.v33i01.33013656)**. 2019 · AAAI.

  这篇论文提出 ST-MGCN，用多张图建模区域间非欧式相关性，并结合上下文门控循环网络建模时间依赖。它适用于网约车/出行需求的区域级预测，而不仅是相邻栅格或传感器的局部建模。

  [正式版本](https://doi.org/10.1609/aaai.v33i01.33013656) · [发表证据](https://api.crossref.org/works/10.1609/aaai.v33i01.33013656) · 代码：未核验到作者代码

  版本/使用说明：出版者登记的 Crossref 元数据与摘要已核对；出版者页面本次访问受限，未核验到作者代码。

<a id="paper-dmvst-net"></a>

- **DMVST-Net** — Huaxiu Yao et al. **[Deep Multi-View Spatial-Temporal Network for Taxi Demand Prediction](https://arxiv.org/abs/1802.08714)**. 2018 · AAAI.

  这篇论文提出 DMVST-Net，用时间视图、局部空间视图和语义视图联合建模出租车需求的时空相关性。它针对区域级需求预测中仅用 CNN 或 LSTM 难以同时刻画空间与时间依赖的问题。

  [正式版本](https://doi.org/10.1609/aaai.v32i1.11836) · [发表证据](https://api.crossref.org/works/10.1609/aaai.v32i1.11836) · [代码](https://github.com/huaxiuyao/DMVST-Net)（作者/项目仓库已核验）

  版本/使用说明：作者仓库明确仅提供模型部分，原始数据未公开；已读 model.py，不能视为完整复现包。

<a id="paper-st-resnet"></a>

- **ST-ResNet** — Junbo Zhang et al. **[Deep Spatio-Temporal Residual Networks for Citywide Crowd Flows Prediction](https://arxiv.org/abs/1610.00081)**. 2017 · AAAI；arXiv 首发 2016.

  对城市网格流入/流出量，分别建模近期、周期、趋势并融合外部因素。

  [发表证据](https://arxiv.org/abs/1610.00081) · 代码：未核验到作者代码
