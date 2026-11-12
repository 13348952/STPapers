# 简洁基线、高效与大规模预测

[简体中文](efficient.md) | [English](efficient.en.md) · [主题导航 / Topics](README.md) · [返回主目录](../README.md)

<a id="topic-efficient"></a>

## 05 · 简洁基线、高效与大规模预测

将节点规模、历史长度、预测跨度及计算开销纳入设计。

<a id="paper-fast"></a>

- **FaST** — Yiji Zhao et al. **[FaST: Efficient and Effective Long-Horizon Forecasting for Large-Scale Spatial-Temporal Graphs via Mixture-of-Experts](https://arxiv.org/abs/2601.05174)**. 2026 · KDD.

  以自适应图代理注意力和异质性感知 MoE，面向大规模、长预测跨度的时空图。

  [发表证据](https://github.com/yijizhao/FaST) · [代码](https://github.com/yijizhao/FaST)（作者/项目仓库已核验）

  版本/使用说明：关注长跨度与大图；不把论文摘要的性能表述当成跨设置的统一排名。

<a id="paper-hieramix"></a>

- **HieraMix** — Yongyao Wang et al. **[HieraMix: A Hierarchical MLP-Mixer for Large-Scale Traffic Forecasting](https://ijcai.org/proceedings/2026/729)**. 2026 · IJCAI.

  通过分层时空混合及自适应区域混合，构建面向大规模路网的 MLP 架构。

  [正式版本](https://ijcai.org/proceedings/2026/729) · [发表证据](https://ijcai.org/proceedings/2026/729) · 代码：未核验到作者代码

<a id="paper-lorest"></a>

- **LoReST** — Qi Feng et al. **[Learning Local Heterogeneity and Cross-Region Context for Large-Scale Traffic Forecasting](https://arxiv.org/abs/2609.27637)**. 2026 · arXiv；正式发表状态未核验.

  结合关系感知局部聚合与区域汇聚、交互和回传，建模局部异质性及跨区域上下文。

  [发表证据](https://arxiv.org/abs/2609.27637) · 代码：未核验到作者代码

<a id="paper-minist"></a>

- **MiniST** — Sheng Huang et al. **[MiniST: Unlocking Input Window Length in Traffic Flow Forecasting with Compact Parameters](https://ijcai.org/proceedings/2026/298)**. 2026 · IJCAI.

  将长交通历史投影为紧凑正交基，并结合模板更新模块处理长历史输入。

  [正式版本](https://ijcai.org/proceedings/2026/298) · [发表证据](https://ijcai.org/proceedings/2026/298) · [代码](https://github.com/enheng66/MiniST)（项目仓库可访问，归属链待补强）

  版本/使用说明：仓库示例 seq_len=720；与短历史基线比较时需对齐输入窗口。

<a id="paper-sagt"></a>

- **SAGT** — Amirhossein Ghaffari et al. **[Spectral Adaptive Graph Transformer for Efficient and Scalable Traffic Forecasting](https://arxiv.org/abs/2610.25140)**. 2026 · arXiv；正式发表状态未核验.

  结合学习式低秩有向空间算子、局部图扩散和频率重加权，研究预测开销。

  [发表证据](https://arxiv.org/abs/2610.25140) · [代码](https://github.com/Ahghaffari/sagt)（作者/项目仓库已核验）

<a id="paper-sqlinear"></a>

- **SqLinear** — Yongfeng Su et al. **[SqLinear: Balanced Square Partitioning Makes Linear Interaction Sufficient for Large-Scale Traffic Forecasting](https://arxiv.org/abs/2606.21072)**. 2026 · arXiv；正式发表状态未核验.

  以均衡空间划分配合分层线性交互，研究大规模交通预测的效率。

  [发表证据](https://arxiv.org/abs/2606.21072) · 代码：未核验到作者代码

<a id="paper-graphsparsenet"></a>

- **GraphSparseNet** — Weiyang Kong et al. **[GraphSparseNet: a Novel Method for Large Scale Traffic Flow Prediction](https://arxiv.org/abs/2502.19823)**. 2025 · PVLDB.

  通过特征提取与关系压缩模块，降低大规模路网关系建模成本。

  [发表证据](https://arxiv.org/abs/2502.19823) · 代码：未核验到作者代码

<a id="paper-patchstg"></a>

- **PatchSTG** — Yuchen Fang et al. **[Efficient Large-Scale Traffic Forecasting with Transformers: A Spatial Data Management Perspective](https://arxiv.org/abs/2412.09972)**. 2025 · KDD；arXiv 首发 2024.

  利用 KDTree 构造不规则空间分块，以块内与跨块注意力学习局部和全局关系。

  [发表证据](https://arxiv.org/abs/2412.09972) · [代码](https://github.com/LMissher/PatchSTG)（作者/项目仓库已核验）

<a id="paper-stgformer"></a>

- **STGformer** — Hongjun Wang et al. **[STGformer: Efficient Spatiotemporal Graph Transformer for Traffic Forecasting](https://arxiv.org/abs/2410.00385)**. 2024 · arXiv；正式发表状态未核验.

  提出面向交通预测的高效时空图 Transformer，将图卷积与 Transformer 结合，用单个 STG attention block 捕捉高阶时空交互，并在 LargeST 等设置上评估效率与效果。

  [发表证据](https://arxiv.org/abs/2410.00385) · [代码](https://github.com/Dreamzz5/STGformer)（作者/项目仓库已核验）

  版本/使用说明：论文直接链接作者仓库，已检查 model/train.py 与运行说明，未运行实验。保留 arXiv 2024；与同名的人体姿态、轨迹及稀疏感知论文区分，不将速度报告泛化为跨设置结论。

<a id="paper-bigst"></a>

- **BigST** — Jindong Han et al. **[BigST: Linear Complexity Spatio-Temporal Graph Neural Network for Traffic Forecasting on Large-Scale Road Networks](https://www.vldb.org/pvldb/vol17/p1081-han.pdf)**. 2024 · PVLDB.

  预计算长历史表示，并以线性化全局空间建模扩展到大规模路网。

  [正式版本](https://doi.org/10.14778/3641204.3641217) · [发表证据](https://doi.org/10.14778/3641204.3641217) · [代码](https://github.com/usail-hkust/BigST)（作者/项目仓库已核验）

<a id="paper-stid"></a>

- **STID** — Zezhi Shao et al. **[Spatial-Temporal Identity: A Simple yet Effective Baseline for Multivariate Time Series Forecasting](https://arxiv.org/abs/2208.05233)**. 2022 · CIKM Short.

  把节点与时间身份嵌入接入简洁 MLP，是检验复杂空间模块收益的基础对照。

  [发表证据](https://github.com/GestaltCogTeam/STID) · [代码](https://github.com/GestaltCogTeam/STID)（作者/项目仓库已核验）

<a id="paper-stnorm"></a>

- **STNorm** — Jinliang Deng et al. **[ST-Norm: Spatial and Temporal Normalization for Multi-variate Time Series Forecasting](https://doi.org/10.1145/3447548.3467330)**. 2021 · KDD.

  用空间与时间归一化处理多变量序列中的不同成分，形成简洁预测模块。

  [正式版本](https://doi.org/10.1145/3447548.3467330) · [发表证据](https://doi.org/10.1145/3447548.3467330) · [代码](https://github.com/JLDeng/ST-Norm)（作者/项目仓库已核验）

<a id="paper-ragc"></a>

- **RAGC** — Kaiqi Wu et al. **[Efficient Traffic Forecasting on Large-Scale Road Network by Regularized Adaptive Graph Convolution](https://arxiv.org/abs/2506.07179)**. 2026 · ICDE；arXiv 首发 2025.

  面向大规模交通预测，以高效余弦算子降低图卷积复杂度，并通过随机共享嵌入与残差差分机制正则化自适应图学习。

  [正式版本](https://doi.org/10.1109/ICDE65706.2026.00068) · [发表证据](https://doi.org/10.1109/ICDE65706.2026.00068) · [代码](https://github.com/wkq-wukaiqi/RAGC)（作者/项目仓库已核验）

  版本/使用说明：arXiv v1（2025-06-08）题为 Regularized Adaptive Graph Learning for Large-Scale Traffic Forecasting，简称 RAGL；v3（2026-04-30）采用现标题，按同一工作收录，不重复计数。作者顺序采用正式出版元数据及 v3。已检查作者源码与运行说明，未运行训练或验证性能。

<a id="paper-tas-gnn"></a>

- **TAS-GNN** — JiaJun Yu et al. **[Active Arbitration: Decoupling Spatio-Temporal Duality for Efficient Traffic Forecasting](https://ijcai.org/proceedings/2026/583)**. 2026 · IJCAI 2026.

  以时间上下文调节空间交互，并结合离散小波分解，区分物理传播滞后与语义同步。

  [正式版本](https://doi.org/10.24963/ijcai.2026/583) · [发表证据](https://ijcai.org/proceedings/2026/583) · 代码：未核验到作者代码

  版本/使用说明：论文链接 https://github.com/highhhhh/TAS-GNN ，但所查提交仅有补充材料 PDF，不作为已开放模型代码。
