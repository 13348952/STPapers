# STPapers · 时空序列预测论文目录

**简体中文** | [English](README.en.md)

A curated reading list for spatio-temporal forecasting.

参考 [RSPapers](https://github.com/hongleizhang/RSPapers) 的主题分类和贡献方式，整理时空序列预测论文、数据集与代码入口。中文方法定位为本目录概括，论文保留英文原题。

**本次检索截止：2026-11-04（Asia/Shanghai）。共 86 个独立条目、13 个主题，覆盖 2015—2026；其中 11 篇按核验口径归入 2026，62 篇关联已检查的作者/项目仓库。** 仓库数按论文计，同一个工具库可能对应多篇论文。

这是代表性精选目录，重点为交通/城市图预测，同时覆盖网格序列、降水和天气。并非全领域穷尽综述，也不是性能排行榜。13 条采用已核验的预印本记录，其中一部分可能已有本次未确认的正式版本。

## 快速入口

- [按年份浏览](BY_YEAR.md) · [近期论文（2025—2026）](RECENT.md) · [2025—2026 索引](RECENT_2025_2026.md)
- [数据集与工具](DATASETS.md) · [检索和核验说明](SEARCH_NOTES.md) · [贡献规范](CONTRIBUTING.md)
- [CSV 表格](papers.csv) · [JSON 原始目录](papers.json) · [BibTeX 引用草稿](references.bib)
- [版本记录](CHANGELOG.md) · [结构检查结果](verification.json)
- [每周更新记录](updates/README.md) · [更新流程](MONITORING.md) · [贡献者](CONTRIBUTORS.md)

## 收录范围与标记

**核心对象**：有明确空间位置、区域、图结构或二维/三维空间场，同时预测未来时间段的任务。图学习中的“变量关系”可以是统计依赖，不自动等同于地理关系或因果传播。

**相关背景单列**：纯时间序列基线、插补方法和广义城市表示学习。CSDI 的主任务是插补；视频预测架构作为网格预测背景收录。没有将轨迹规划、推荐系统、静态图分类等并入核心目录。

年份优先采用已核验的正式版本年份；未确认正式版本则使用 arXiv 首发年。期刊在线年与卷期年不同时保留说明。正文使用一个主分类，同一论文不会因跨主题而重复计数。

“作者/项目仓库已核验”表示已检查论文关联的 README 或仓库页面，**未执行训练、未验证复现数值，也不等于完整训练代码和数据均已开放**。仅有论文代码链接、访问失败及归属证据有限的情况分别标记；“未核验到”不表示不存在。

## 建议阅读路线

这些顺序是本目录的编辑建议，不代表模型性能排序。

| 目标 | 建议顺序 | 重点问题 |
| --- | --- | --- |
| 建立交通图预测基础 | DCRNN → STGCN → Graph WaveNet → AGCRN → D²STGNN | 固定图、学习图、节点异质性与动态依赖如何区分？ |
| 理解 Transformer 与简洁基线 | STID → GMAN → PDFormer → STAEformer | 提升来自交互算子，还是身份/时间编码和训练设置？ |
| 大规模交通预测 | LargeST → BigST → PatchSTG → GraphSparseNet → MiniST / HieraMix / FaST | 节点数、历史长度、预测跨度分别如何影响成本？ |
| 自监督与迁移 | STEP → STGCL → ST-SSL → STD-MAE → UniST / UrbanPG | 预训练信息、领域重叠和适配成本如何控制？ |
| 概率预测 | TimeGrad（背景）→ DiffSTG → SpecSTG → GenCast | 点误差、分布校准与联合空间一致性如何同时评估？ |
| 网格/天气 | ConvLSTM → PredRNN → SimVP → Earthformer → GraphCast / Aurora | 局部结构、长程通信、物理约束与预训练各有什么作用？ |

## 主题导航

| 编号 | 主题 | 条目数 |
| --- | --- | ---: |
| 01 | [综述与入门](#topic-survey) | 4 |
| 02 | [城市网格流量与需求预测](#topic-urban) | 3 |
| 03 | [图卷积、动态图与连续时间建模](#topic-graph) | 14 |
| 04 | [注意力、Transformer 与状态空间模型](#topic-attention) | 6 |
| 05 | [简洁基线、高效与大规模预测](#topic-efficient) | 11 |
| 06 | [自监督与预训练](#topic-pretrain) | 5 |
| 07 | [异质性、元学习与迁移](#topic-transfer) | 4 |
| 08 | [基础模型、语言模型与跨模态迁移](#topic-foundation) | 5 |
| 09 | [概率时空图预测](#topic-probabilistic) | 2 |
| 10 | [通用网格与时空帧预测](#topic-grid) | 8 |
| 11 | [降水、天气与地球系统预测](#topic-weather) | 10 |
| 12 | [数据集、基准与工具](#topic-benchmark) | 8 |
| 13 | [相关时间序列基线与插补背景](#topic-related) | 6 |

<a id="topic-survey"></a>

## 01 · 综述与入门

用于建立任务、方法和资源地图。

<a id="paper-stfm-survey"></a>

- **STFM-survey** — Yuxuan Liang et al. **[Foundation Models for Spatio-Temporal Data Science: A Tutorial and Survey](https://arxiv.org/abs/2503.13502)**. 2025 · arXiv；正式发表状态未核验.

  梳理时空基础模型及其在感知、管理、挖掘中的作用，作为广义背景。

  [发表证据](https://arxiv.org/abs/2503.13502) · 代码：未核验到作者代码

<a id="paper-urban-stgnn-survey"></a>

- **Urban-STGNN-survey** — Guangyin Jin et al. **[Spatio-Temporal Graph Neural Networks for Predictive Learning in Urban Computing: A Survey](https://arxiv.org/abs/2303.14483)**. 2024 · IEEE TKDE；arXiv 首发 2023.

  面向城市计算，梳理时空图构建、模型设计与不同预测应用。

  [正式版本](https://doi.org/10.1109/TKDE.2023.3333824) · [发表证据](https://doi.org/10.1109/TKDE.2023.3333824) · 代码：未核验到作者代码

<a id="paper-traffic-survey"></a>

- **Traffic-survey** — Weiwei Jiang et al. **[Graph Neural Network for Traffic Forecasting: A Survey](https://arxiv.org/abs/2101.11174)**. 2022 · Expert Systems with Applications；arXiv 首发 2021.

  从图构建、模型、任务及开放资源梳理交通预测中的图神经网络。

  [发表证据](https://arxiv.org/abs/2101.11174) · 代码：未核验到作者代码

<a id="paper-sttp-survey"></a>

- **STTP-survey** — Kyungeun Lee et al. **[Short-term Traffic Prediction with Deep Neural Networks: A Survey](https://arxiv.org/abs/2009.00712)**. 2020 · arXiv；正式发表状态未核验.

  从输入表示、网络结构、应用与数据资源组织短期交通预测研究。

  [发表证据](https://arxiv.org/abs/2009.00712) · 代码：未核验到作者代码

  版本/使用说明： 当前列出已核验的 arXiv 版本；不据此断言没有正式发表版本。


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

<a id="paper-st-resnet"></a>

- **ST-ResNet** — Junbo Zhang et al. **[Deep Spatio-Temporal Residual Networks for Citywide Crowd Flows Prediction](https://arxiv.org/abs/1610.00081)**. 2017 · AAAI；arXiv 首发 2016.

  对城市网格流入/流出量，分别建模近期、周期、趋势并融合外部因素。

  [发表证据](https://arxiv.org/abs/1610.00081) · 代码：未核验到作者代码


<a id="topic-graph"></a>

## 03 · 图卷积、动态图与连续时间建模

以道路或传感器节点为对象，研究空间依赖和时间动态。

<a id="paper-dgcrn"></a>

- **DGCRN** — Fuxian Li et al. **[Dynamic Graph Convolutional Recurrent Network for Traffic Prediction: Benchmark and Solution](https://arxiv.org/abs/2104.14917)**. 2023 · ACM TKDD；arXiv 首发 2021.

  由节点动态信息生成图结构，同时提供交通预测的统一评测与实现。

  [发表证据](https://github.com/tsinghua-fib-lab/Traffic-Benchmark) · [代码](https://github.com/tsinghua-fib-lab/Traffic-Benchmark)（作者/项目仓库已核验）

<a id="paper-d2stgnn"></a>

- **D2STGNN** — Zezhi Shao et al. **[Decoupled Dynamic Spatial-Temporal Graph Neural Network for Traffic Forecasting](https://arxiv.org/abs/2206.09112)**. 2022 · PVLDB.

  将交通信号拆为扩散与固有成分，结合动态图学习分别建模。

  [发表证据](https://github.com/GestaltCogTeam/D2STGNN) · [代码](https://github.com/GestaltCogTeam/D2STGNN)（作者/项目仓库已核验）

<a id="paper-dstagnn"></a>

- **DSTAGNN** — Shiyong Lan et al. **[DSTAGNN: Dynamic Spatial-Temporal Aware Graph Neural Network for Traffic Flow Forecasting](https://proceedings.mlr.press/v162/lan22a.html)**. 2022 · ICML.

  结合动态时空关系建模与图网络进行交通预测。

  [正式版本](https://proceedings.mlr.press/v162/lan22a.html) · [发表证据](https://proceedings.mlr.press/v162/lan22a.html) · [代码](https://github.com/SYLan2019/DSTAGNN)（作者/项目仓库已核验）

<a id="paper-stgncde"></a>

- **STGNCDE** — Jeongwhan Choi et al. **[Graph Neural Controlled Differential Equations for Traffic Forecasting](https://arxiv.org/abs/2112.03558)**. 2022 · AAAI；arXiv 首发 2021.

  联合空间和时间神经控制微分方程，提供连续时间建模视角。

  [发表证据](https://github.com/jeongwhanchoi/STG-NCDE) · [代码](https://github.com/jeongwhanchoi/STG-NCDE)（作者/项目仓库已核验）

<a id="paper-gts"></a>

- **GTS** — Chao Shang et al. **[Discrete Graph Structure Learning for Forecasting Multiple Time Series](https://arxiv.org/abs/2101.06861)**. 2021 · ICLR.

  学习可微采样的离散图分布，并与多序列预测模型共同优化。

  [发表证据](https://github.com/chaoshangcs/GTS) · [代码](https://github.com/chaoshangcs/GTS)（作者/项目仓库已核验）

<a id="paper-stfgnn"></a>

- **STFGNN** — Mengzhang Li et al. **[Spatial-Temporal Fusion Graph Neural Networks for Traffic Flow Forecasting](https://arxiv.org/abs/2012.09641)**. 2021 · AAAI；arXiv 首发 2020.

  融合空间图与数据驱动的时间关系图，并结合门控卷积。

  [发表证据](https://github.com/MengzhangLI/STFGNN) · [代码](https://github.com/MengzhangLI/STFGNN)（作者/项目仓库已核验）

  版本/使用说明：作者 README 对部分数据集结果作了更正说明；比较数字前应检查最新论文与仓库。

<a id="paper-stgode"></a>

- **STGODE** — Zheng Fang et al. **[Spatial-Temporal Graph ODE Networks for Traffic Flow Forecasting](https://arxiv.org/abs/2106.12931)**. 2021 · KDD.

  以张量形式的常微分方程建模时空动态，同时考虑空间与语义关系。

  [发表证据](https://github.com/square-coder/STGODE) · [代码](https://github.com/square-coder/STGODE)（作者/项目仓库已核验）

<a id="paper-agcrn"></a>

- **AGCRN** — Lei Bai et al. **[Adaptive Graph Convolutional Recurrent Network for Traffic Forecasting](https://arxiv.org/abs/2007.02842)**. 2020 · NeurIPS.

  结合节点自适应参数学习和自适应图生成，刻画不同节点的预测模式。

  [发表证据](https://github.com/LeiBAI/AGCRN) · [代码](https://github.com/LeiBAI/AGCRN)（作者/项目仓库已核验）

<a id="paper-mtgnn"></a>

- **MTGNN** — Zonghan Wu et al. **[Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks](https://arxiv.org/abs/2005.11650)**. 2020 · KDD.

  联合学习变量间有向图、mix-hop 传播与时间卷积；兼顾通用多变量序列与交通任务。

  [发表证据](https://github.com/nnzhan/MTGNN) · [代码](https://github.com/nnzhan/MTGNN)（作者/项目仓库已核验）

  版本/使用说明：通用多变量模型，因明确包含交通任务与图学习而收录主目录。

<a id="paper-stsgcn"></a>

- **STSGCN** — Chao Song et al. **[Spatial-Temporal Synchronous Graph Convolutional Networks: A New Framework for Spatial-Temporal Network Data Forecasting](https://ojs.aaai.org/index.php/AAAI/article/view/5438)**. 2020 · AAAI.

  把相邻时间片的节点连成局部时空图，联合建模局部时空关系与异质性。

  [正式版本](https://ojs.aaai.org/index.php/AAAI/article/view/5438) · [发表证据](https://ojs.aaai.org/index.php/AAAI/article/download/5438/5294) · [代码](https://github.com/Davidham3/STSGCN)（作者/项目仓库已核验）

<a id="paper-astgcn"></a>

- **ASTGCN** — Shengnan Guo et al. **[Attention Based Spatial-Temporal Graph Convolutional Networks for Traffic Flow Forecasting](https://ojs.aaai.org/index.php/AAAI/article/view/3881)**. 2019 · AAAI.

  通过时空注意力、图卷积与近期/日/周分支进行交通流预测。

  [正式版本](https://ojs.aaai.org/index.php/AAAI/article/view/3881) · [发表证据](https://ojs.aaai.org/index.php/AAAI/article/view/3881) · [代码](https://github.com/guoshnBJTU/ASTGCN-2019-pytorch)（作者/项目仓库已核验）

  版本/使用说明：关联的作者 PyTorch 仓库说明仅实现近期分支；不能默认等于完整三分支 ASTGCN。

<a id="paper-graph-wavenet"></a>

- **Graph-WaveNet** — Zonghan Wu et al. **[Graph WaveNet for Deep Spatial-Temporal Graph Modeling](https://arxiv.org/abs/1906.00121)**. 2019 · IJCAI.

  通过节点嵌入学习自适应邻接关系，并用膨胀时间卷积建模历史序列。

  [发表证据](https://github.com/nnzhan/Graph-WaveNet) · [代码](https://github.com/nnzhan/Graph-WaveNet)（作者/项目仓库已核验）

<a id="paper-dcrnn"></a>

- **DCRNN** — Yaguang Li et al. **[Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting](https://arxiv.org/abs/1707.01926)**. 2018 · ICLR；arXiv 首发 2017.

  将有向图扩散卷积与循环编码器—解码器结合，是理解路网预测的重要起点。

  [发表证据](https://github.com/liyaguang/DCRNN) · [代码](https://github.com/liyaguang/DCRNN)（作者/项目仓库已核验）

<a id="paper-stgcn"></a>

- **STGCN** — Bing Yu et al. **[Spatio-Temporal Graph Convolutional Networks: A Deep Learning Framework for Traffic Forecasting](https://arxiv.org/abs/1709.04875)**. 2018 · IJCAI；arXiv 首发 2017.

  用图卷积与时间卷积构成全卷积时空预测网络。

  [发表证据](https://github.com/VeritasYin/STGCN_IJCAI-18) · [代码](https://github.com/VeritasYin/STGCN_IJCAI-18)（作者/项目仓库已核验）


<a id="topic-attention"></a>

## 04 · 注意力、Transformer 与状态空间模型

关注时空注意力、嵌入、传播延迟以及与状态空间模型的结合。

<a id="paper-fast-ssm"></a>

- **FAST-SSM** — Xinjin Li et al. **[FAST: A Synergistic Framework of Attention and State-space Models for Spatiotemporal Traffic Prediction](https://arxiv.org/abs/2604.13453)**. 2026 · ICME.

  结合时间注意力与 Mamba 空间模块；与 KDD 2026 的 FaST 是不同论文。

  [发表证据](https://arxiv.org/abs/2604.13453) · 代码：未核验到作者代码

<a id="paper-speclst"></a>

- **SpecLST** — Kenan Kang et al. **[SpecLST: Spectral-Enhanced Long-Short Term Spatio-Temporal Multimodal Modeling for Traffic Forecasting](https://arxiv.org/abs/2610.36393)**. 2026 · arXiv；正式发表状态未核验.

  以频域长历史表示融合天气、事故等上下文，并采用稀疏 MoE；属于多模态设置。

  [发表证据](https://arxiv.org/abs/2610.36393) · 代码：未核验到作者代码

<a id="paper-pdformer"></a>

- **PDFormer** — Jiawei Jiang et al. **[PDFormer: Propagation Delay-Aware Dynamic Long-Range Transformer for Traffic Flow Prediction](https://arxiv.org/abs/2301.07945)**. 2023 · AAAI.

  结合短程/长程图掩码与传播延迟感知变换，建模动态空间关系。

  [发表证据](https://github.com/BUAABIGSCity/PDFormer) · [代码](https://github.com/BUAABIGSCity/PDFormer)（作者/项目仓库已核验）

<a id="paper-staeformer"></a>

- **STAEformer** — Hangchen Liu et al. **[STAEformer: Spatio-Temporal Adaptive Embedding Makes Vanilla Transformer SOTA for Traffic Forecasting](https://arxiv.org/abs/2308.10425)**. 2023 · CIKM Short.

  研究时空自适应嵌入如何增强普通 Transformer 的交通预测能力。

  [发表证据](https://github.com/XDZhelheim/STAEformer) · [代码](https://github.com/XDZhelheim/STAEformer)（作者/项目仓库已核验）

<a id="paper-gman"></a>

- **GMAN** — Chuanpan Zheng et al. **[GMAN: A Graph Multi-Attention Network for Traffic Prediction](https://arxiv.org/abs/1911.08415)**. 2020 · AAAI；arXiv 首发 2019.

  使用时空多重注意力及历史到未来的变换注意力，直接生成多步交通预测。

  [发表证据](https://github.com/zhengchuanpan/GMAN) · [代码](https://github.com/zhengchuanpan/GMAN)（作者/项目仓库已核验）

<a id="paper-sttn"></a>

- **STTN** — Mingxing Xu et al. **[Spatial-Temporal Transformer Networks for Traffic Flow Forecasting](https://arxiv.org/abs/2001.02908)**. 2020 · arXiv；正式发表状态未核验.

  采用空间与时间 Transformer，建模动态有向空间关系及长程时间依赖。

  [发表证据](https://arxiv.org/abs/2001.02908) · 代码：未核验到作者代码

  版本/使用说明： 当前列出已核验的 arXiv 版本；不据此断言没有正式发表版本。


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


<a id="topic-pretrain"></a>

## 06 · 自监督与预训练

对比学习、掩码建模及其下游预测使用方式。

<a id="paper-hgaurban"></a>

- **HGAurban** — Qianru Zhang et al. **[HGAurban: Heterogeneous Graph Autoencoding for Urban Spatial-Temporal Learning](https://arxiv.org/abs/2410.10915)**. 2025 · CIKM；arXiv 首发 2024.

  以异质图掩码自编码学习区域表示，服务城市时空任务；包含预测以外的任务。

  [发表证据](https://arxiv.org/abs/2410.10915) · 代码：未核验到作者代码

  版本/使用说明：arXiv 当前题名为 HGAurban；早期检索记录出现 Graph Masked Autoencoder，按同一标识符合并。

<a id="paper-stdmae"></a>

- **STDMAE** — Haotian Gao et al. **[Spatial-Temporal-Decoupled Masked Pre-training for Spatiotemporal Forecasting](https://arxiv.org/abs/2312.00516)**. 2024 · IJCAI；arXiv 首发 2023.

  分别沿空间与时间维度进行掩码重建，把预训练表示用于下游预测。

  [发表证据](https://github.com/Jimmy-7664/STD-MAE) · [代码](https://github.com/Jimmy-7664/STD-MAE)（作者/项目仓库已核验）

<a id="paper-stssl"></a>

- **STSSL** — Jiahao Ji et al. **[Spatio-Temporal Self-Supervised Learning for Traffic Flow Prediction](https://arxiv.org/abs/2212.04475)**. 2023 · AAAI；arXiv 首发 2022.

  利用自适应图增强与空间/时间自监督任务，学习异质交通模式。

  [发表证据](https://github.com/Echo-Ji/ST-SSL) · [代码](https://github.com/Echo-Ji/ST-SSL)（作者/项目仓库已核验）

<a id="paper-step"></a>

- **STEP** — Zezhi Shao et al. **[Pre-training Enhanced Spatial-temporal Graph Neural Network for Multivariate Time Series Forecasting](https://arxiv.org/abs/2206.09113)**. 2022 · KDD.

  通过长历史序列预训练，为下游图预测模型提供时间上下文与结构信息。

  [发表证据](https://github.com/GestaltCogTeam/STEP) · [代码](https://github.com/GestaltCogTeam/STEP)（作者/项目仓库已核验）

<a id="paper-stgcl"></a>

- **STGCL** — Xu Liu et al. **[When Do Contrastive Learning Signals Help Spatio-Temporal Graph Forecasting?](https://arxiv.org/abs/2108.11873)**. 2022 · ACM SIGSPATIAL；arXiv 首发 2021.

  系统比较时空图对比学习的接入方式、增强策略与负样本选择。

  [发表证据](https://github.com/liuxu77/STGCL) · [代码](https://github.com/liuxu77/STGCL)（作者/项目仓库已核验）


<a id="topic-transfer"></a>

## 07 · 异质性、元学习与迁移

区分节点特定参数、跨域适配和持续学习，三者并非同一任务。

<a id="paper-pimcst"></a>

- **PIMCST** — Abdul Joseph Fofanah et al. **[PIMCST: Physics-Informed Multi-Phase Consensus and Spatio-Temporal Few-Shot Learning for Traffic Flow Forecasting](https://arxiv.org/abs/2602.01936)**. 2026 · arXiv；正式发表状态未核验.

  以扩散、同步和谱表示构建多阶段共识，并用元学习适配少样本跨城市预测。

  [发表证据](https://arxiv.org/abs/2602.01936) · [代码](https://github.com/afofanah/MCPST)（作者/项目仓库已核验）

  版本/使用说明：标题使用 PIMCST，而摘要/仓库使用 MCPST；保留该命名差异。

<a id="paper-urbanpg"></a>

- **UrbanPG** — Aoyu Liu et al. **[UrbanPG: An Efficient Framework with Personalized Context and General Backbone Interaction for Urban Spatio-Temporal Learning](https://ojs.aaai.org/index.php/AAAI/article/view/38554)**. 2026 · AAAI.

  分离个性化上下文与通用骨干，研究大规模预测、少样本迁移和持续学习。

  [正式版本](https://ojs.aaai.org/index.php/AAAI/article/view/38554) · [发表证据](https://ojs.aaai.org/index.php/AAAI/article/view/38554) · [代码](https://github.com/Aoyu-Liu/UrbanPG)（作者/项目仓库已核验）

  版本/使用说明：GitHub About 仍出现 AAAI 2025 字样，README 与正式会议页为 AAAI 2026；以会议页为准。

<a id="paper-himnet"></a>

- **HimNet** — Zheng Dong et al. **[Heterogeneity-Informed Meta-Parameter Learning for Spatiotemporal Time Series Forecasting](https://arxiv.org/abs/2405.10800)**. 2024 · KDD.

  通过时空嵌入与元参数池学习具有时空差异的模型参数。

  [发表证据](https://github.com/XDZhelheim/HimNet) · [代码](https://github.com/XDZhelheim/HimNet)（作者/项目仓库已核验）

<a id="paper-megacrn"></a>

- **MegaCRN** — Renhe Jiang et al. **[Spatio-Temporal Meta-Graph Learning for Traffic Forecasting](https://arxiv.org/abs/2211.14701)**. 2023 · AAAI；arXiv 首发 2022.

  借助元节点记忆与元图学习，刻画交通节点和时间模式的异质性。

  [发表证据](https://github.com/deepkashiwa20/MegaCRN) · [代码](https://github.com/deepkashiwa20/MegaCRN)（作者/项目仓库已核验）

  版本/使用说明：采用 AAAI 2023 对应的 arXiv:2211.14701；不使用已撤回的扩展稿 arXiv:2212.05989。


<a id="topic-foundation"></a>

## 08 · 基础模型、语言模型与跨模态迁移

关注统一预训练与少样本/零样本适配。

<a id="paper-factost-v2"></a>

- **FactoST-v2** — Siru Zhong et al. **[Learning to Factorize and Adapt: A Versatile Approach Toward Universal Spatio-Temporal Foundation Models](https://arxiv.org/abs/2601.12083)**. 2026 · arXiv；正式发表状态未核验.

  分离通用时间预训练与领域空间适配，扩展至可变长度和概率分位数预测。

  [发表证据](https://arxiv.org/abs/2601.12083) · [代码](https://github.com/CityMind-Lab/FactoST)（论文提供链接，本次返回 404）

  版本/使用说明：2026 扩展稿，不等同于其 NeurIPS 2025 会议版本；论文给出的仓库本次返回 404。

<a id="paper-st-vfm"></a>

- **ST-VFM** — Changlu Chen et al. **[Reprogramming Vision Foundation Models for Spatio-Temporal Forecasting](https://arxiv.org/abs/2507.11558)**. 2025 · arXiv；正式发表状态未核验.

  通过时序适配与双分支提示协调，将冻结视觉基础模型用于时空预测。

  [发表证据](https://arxiv.org/abs/2507.11558) · 代码：未核验到作者代码

<a id="paper-stllm"></a>

- **STLLM** — Chenxi Liu et al. **[Spatial-Temporal Large Language Model for Traffic Prediction](https://arxiv.org/abs/2401.10134)**. 2024 · IEEE MDM.

  把时空嵌入接入大语言模型，并通过部分冻结注意力适配交通预测。

  [发表证据](https://github.com/ChenxiLiu-HNU/ST-LLM) · [代码](https://github.com/ChenxiLiu-HNU/ST-LLM)（作者/项目仓库已核验）

<a id="paper-unist"></a>

- **UniST** — Yuan Yuan et al. **[UniST: A Prompt-Empowered Universal Model for Urban Spatio-Temporal Prediction](https://arxiv.org/abs/2402.11838)**. 2024 · KDD.

  通过多场景预训练与知识引导提示，探索统一城市时空预测模型。

  [发表证据](https://github.com/tsinghua-fib-lab/UniST) · [代码](https://github.com/tsinghua-fib-lab/UniST)（作者/项目仓库已核验）

<a id="paper-urbangpt"></a>

- **UrbanGPT** — Zhonghang Li et al. **[UrbanGPT: Spatio-Temporal Large Language Models](https://arxiv.org/abs/2403.00813)**. 2024 · KDD.

  结合时空依赖编码器和指令微调，探索城市任务的零样本泛化。

  [发表证据](https://github.com/HKUDS/UrbanGPT) · [代码](https://github.com/HKUDS/UrbanGPT)（作者/项目仓库已核验）


<a id="topic-probabilistic"></a>

## 09 · 概率时空图预测

预测未来分布或样本，而不只输出一个点估计。

<a id="paper-specstg"></a>

- **SpecSTG** — Lequan Lin et al. **[SpecSTG: A Fast Spectral Diffusion Framework for Probabilistic Spatio-Temporal Traffic Forecasting](https://arxiv.org/abs/2401.08119)**. 2024 · arXiv；正式发表状态未核验.

  在频谱域生成未来序列，并结合空间依赖与频谱图卷积。

  [发表证据](https://arxiv.org/abs/2401.08119) · [代码](https://anonymous.4open.science/r/SpecSTG)（论文提供匿名代码，访问未核验）

  版本/使用说明： 当前列出已核验的 arXiv 版本；不据此断言没有正式发表版本。

<a id="paper-diffstg"></a>

- **DiffSTG** — Haomin Wen et al. **[DiffSTG: Probabilistic Spatio-Temporal Graph Forecasting with Denoising Diffusion Models](https://arxiv.org/abs/2301.13629)**. 2023 · ACM SIGSPATIAL.

  将去噪扩散模型推广到时空图，进行非自回归概率预测。

  [发表证据](https://arxiv.org/abs/2301.13629) · 代码：未核验到作者代码


<a id="topic-grid"></a>

## 10 · 通用网格与时空帧预测

作为天气/城市网格预测的架构基础；包含视频预测背景。

<a id="paper-tau"></a>

- **TAU** — Cheng Tan et al. **[Temporal Attention Unit: Towards Efficient Spatiotemporal Predictive Learning](https://arxiv.org/abs/2206.12126)**. 2023 · CVPR；arXiv 首发 2022.

  将时间注意力拆分为帧内和帧间部分，改善并行时空帧预测。

  [发表证据](https://github.com/chengtan9907/OpenSTL) · [代码](https://github.com/chengtan9907/OpenSTL)（作者团队工具库实现已核验）

<a id="paper-simvp"></a>

- **SimVP** — Zhangyang Gao et al. **[SimVP: Simpler yet Better Video Prediction](https://arxiv.org/abs/2206.05099)**. 2022 · CVPR.

  以卷积编码器、时间处理模块和解码器构成简洁视频/网格预测基线。

  [发表证据](https://github.com/gaozhangyang/SimVP-Simpler-yet-Better-Video-Prediction) · [代码](https://github.com/gaozhangyang/SimVP-Simpler-yet-Better-Video-Prediction)（作者/项目仓库已核验）

<a id="paper-phydnet"></a>

- **PhyDNet** — Vincent Le Guen et al. **[Disentangling Physical Dynamics from Unknown Factors for Unsupervised Video Prediction](https://arxiv.org/abs/2003.01460)**. 2020 · CVPR.

  将可解释的物理动态与未知残差因素分离，用于未来帧预测。

  [发表证据](https://github.com/vincent-leguen/PhyDNet) · [代码](https://github.com/vincent-leguen/PhyDNet)（作者/项目仓库已核验）

<a id="paper-mim"></a>

- **MIM** — Yunbo Wang et al. **[Memory In Memory: A Predictive Neural Network for Learning Higher-Order Non-Stationarity from Spatiotemporal Dynamics](https://arxiv.org/abs/1811.07490)**. 2019 · CVPR；arXiv 首发 2018.

  通过记忆模块处理时空序列中的高阶非平稳变化。

  [发表证据](https://github.com/Yunbo426/MIM) · [代码](https://github.com/Yunbo426/MIM)（作者/项目仓库已核验）

<a id="paper-predrnnpp"></a>

- **PredRNNpp** — Yunbo Wang et al. **[PredRNN++: Towards A Resolution of the Deep-in-Time Dilemma in Spatiotemporal Predictive Learning](https://arxiv.org/abs/1804.06300)**. 2018 · ICML.

  以因果 LSTM 与梯度通路缓解深层递归预测中的优化困难。

  [发表证据](https://github.com/Yunbo426/predrnn-pp) · [代码](https://github.com/Yunbo426/predrnn-pp)（作者/项目仓库已核验）

<a id="paper-predrnn"></a>

- **PredRNN** — Yunbo Wang et al. **[PredRNN: Recurrent Neural Networks for Predictive Learning using Spatiotemporal LSTMs](https://papers.nips.cc/paper/6689-predrnn-recurrent-neural-networks-for-predictive-learning-using-spatiotemporal-lstms)**. 2017 · NeurIPS.

  使用时空 LSTM 及双重记忆状态建模未来帧，属于通用时空预测背景。

  [正式版本](https://papers.nips.cc/paper/6689-predrnn-recurrent-neural-networks-for-predictive-learning-using-spatiotemporal-lstms) · [发表证据](https://papers.nips.cc/paper/6689-predrnn-recurrent-neural-networks-for-predictive-learning-using-spatiotemporal-lstms) · [代码](https://github.com/thuml/predrnn-pytorch)（作者/项目仓库已核验）

<a id="paper-trajgru"></a>

- **TrajGRU** — Xingjian Shi et al. **[Deep Learning for Precipitation Nowcasting: A Benchmark and A New Model](https://arxiv.org/abs/1706.03458)**. 2017 · NeurIPS.

  在降水临近预报中学习位置相关的递归连接，并提供相应基准。

  [发表证据](https://arxiv.org/abs/1706.03458) · 代码：未核验到作者代码

<a id="paper-convlstm"></a>

- **ConvLSTM** — Xingjian Shi et al. **[Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting](https://arxiv.org/abs/1506.04214)**. 2015 · NeurIPS.

  将卷积放入 LSTM 状态转换，为网格序列与降水临近预报提供基础架构。

  [正式版本](https://papers.nips.cc/paper_files/paper/2015/hash/07563a3fe3bbe7e3ba84431ad9d055af-Abstract.html) · [发表证据](https://papers.nips.cc/paper_files/paper/2015/hash/07563a3fe3bbe7e3ba84431ad9d055af-Abstract.html) · 代码：未核验到作者代码


<a id="topic-weather"></a>

## 11 · 降水、天气与地球系统预测

覆盖临近预报、中期天气及地球系统基础模型。

<a id="paper-aurora"></a>

- **Aurora** — Cristian Bodnar et al. **[A foundation model for the Earth system](https://arxiv.org/abs/2405.13063)**. 2025 · Nature；arXiv 首发 2024.

  在多源地球系统数据上预训练，并适配天气、空气质量、海浪等任务。

  [正式版本](https://doi.org/10.1038/s41586-025-09005-y) · [发表证据](https://doi.org/10.1038/s41586-025-09005-y) · [代码](https://github.com/microsoft/aurora)（作者/项目仓库已核验）

<a id="paper-fengwu"></a>

- **FengWu** — Kang Chen et al. **[FengWu: Pushing the Skillful Global Medium-range Weather Forecast beyond 10 Days Lead](https://arxiv.org/abs/2304.02948)**. 2025 · Communications Earth & Environment；arXiv 首发 2023.

  以多模态、多任务结构、跨模态融合和回放缓冲提升中期天气建模。

  [发表证据](https://github.com/OpenEarthLab/FengWu) · [代码](https://github.com/OpenEarthLab/FengWu)（作者/项目仓库已核验）

<a id="paper-gencast"></a>

- **GenCast** — Ilan Price et al. **[Probabilistic weather forecasting with machine learning](https://arxiv.org/abs/2312.15796)**. 2025 · Nature；arXiv 首发 2023.

  使用扩散生成集合预报，刻画未来全球天气状态的联合不确定性。

  [正式版本](https://doi.org/10.1038/s41586-024-08252-9) · [发表证据](https://doi.org/10.1038/s41586-024-08252-9) · [代码](https://github.com/google-deepmind/graphcast)（作者/项目仓库已核验）

  版本/使用说明：采用 Nature 2025 卷期年；2024-12-04 在线发表，预印本首发于 2023。

<a id="paper-climax"></a>

- **ClimaX** — Tung Nguyen et al. **[ClimaX: A foundation model for weather and climate](https://arxiv.org/abs/2301.10343)**. 2023 · ICML.

  使用异构气候数据预训练，再适配不同天气变量与预测任务。

  [发表证据](https://github.com/microsoft/ClimaX) · [代码](https://github.com/microsoft/ClimaX)（作者/项目仓库已核验）

<a id="paper-graphcast"></a>

- **GraphCast** — Remi Lam et al. **[Learning skillful medium-range global weather forecasting](https://arxiv.org/abs/2212.12794)**. 2023 · Science；arXiv 首发 2022.

  以图神经网络学习全球天气场演化，输出中期多变量天气预测。

  [正式版本](https://doi.org/10.1126/science.adi2336) · [发表证据](https://doi.org/10.1126/science.adi2336) · [代码](https://github.com/google-deepmind/graphcast)（作者/项目仓库已核验）

<a id="paper-nowcastnet"></a>

- **NowcastNet** — Yuchen Zhang et al. **[Skilful nowcasting of extreme precipitation with NowcastNet](https://www.nature.com/articles/s41586-023-06184-4)**. 2023 · Nature.

  将物理演化约束与生成建模结合，用于极端降水临近预报。

  [正式版本](https://www.nature.com/articles/s41586-023-06184-4) · [发表证据](https://www.nature.com/articles/s41586-023-06184-4) · 代码：未核验到作者代码

<a id="paper-pangu-weather"></a>

- **Pangu-Weather** — Kaifeng Bi et al. **[Accurate medium-range global weather forecasting with 3D neural networks](https://arxiv.org/abs/2211.02556)**. 2023 · Nature；arXiv 首发 2022.

  以三维地球专用 Transformer 与分层时间聚合处理全球天气预测。

  [正式版本](https://doi.org/10.1038/s41586-023-06185-3) · [发表证据](https://doi.org/10.1038/s41586-023-06185-3) · [代码](https://github.com/198808xc/Pangu-Weather)（作者/项目仓库已核验）

<a id="paper-earthformer"></a>

- **Earthformer** — Zhihan Gao et al. **[Earthformer: Exploring Space-Time Transformers for Earth System Forecasting](https://arxiv.org/abs/2207.05833)**. 2022 · NeurIPS.

  通过局部 Cuboid Attention 与全局向量交换信息，用于降水及地球系统预测。

  [发表证据](https://github.com/amazon-science/earth-forecasting-transformer) · [代码](https://github.com/amazon-science/earth-forecasting-transformer)（作者/项目仓库已核验）

<a id="paper-fourcastnet"></a>

- **FourCastNet** — Jaideep Pathak et al. **[FourCastNet: A Global Data-driven High-resolution Weather Model using Adaptive Fourier Neural Operators](https://arxiv.org/abs/2202.11214)**. 2022 · arXiv；正式发表状态未核验.

  利用自适应傅里叶神经算子进行高分辨率全球天气预测。

  [发表证据](https://arxiv.org/abs/2202.11214) · [代码](https://github.com/NVlabs/FourCastNet)（作者/项目仓库已核验）

<a id="paper-dgmr"></a>

- **DGMR** — Suman Ravuri et al. **[Skilful precipitation nowcasting using deep generative models of radar](https://arxiv.org/abs/2104.00954)**. 2021 · Nature.

  使用深度生成模型输出具有时空一致性的概率降水临近预报。

  [正式版本](https://doi.org/10.1038/s41586-021-03854-z) · [发表证据](https://doi.org/10.1038/s41586-021-03854-z) · 代码：未核验到作者代码


<a id="topic-benchmark"></a>

## 12 · 数据集、基准与工具

优先了解任务定义、数据处理、指标和复现入口。

<a id="paper-traffident"></a>

- **TraffiDent** — Xiaochuan Gou et al. **[TraffiDent: A Dataset for Understanding the Interplay Between Traffic Dynamics and Incidents](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html)**. 2025 · NeurIPS Datasets and Benchmarks.

  对齐交通状态、事故及道路属性，支持事故后的交通预测和相关分析。

  [正式版本](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html) · [发表证据](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html) · 代码：未核验到作者代码

<a id="paper-basicts"></a>

- **BasicTS** — Zezhi Shao et al. **[Exploring Progress in Multivariate Time Series Forecasting: Comprehensive Benchmarking and Heterogeneity Analysis](https://arxiv.org/abs/2310.06119)**. 2024 · IEEE TKDE；arXiv 首发 2023.

  通过统一评测流程与时空异质性分析，研究多变量预测结果为何难以直接比较。

  [发表证据](https://github.com/GestaltCogTeam/BasicTS) · [代码](https://github.com/GestaltCogTeam/BasicTS)（作者/项目仓库已核验）

<a id="paper-weatherbench2"></a>

- **WeatherBench2** — Stephan Rasp et al. **[WeatherBench 2: A Benchmark for the Next Generation of Data‐Driven Global Weather Models](https://arxiv.org/abs/2308.15560)**. 2024 · Journal of Advances in Modeling Earth Systems；arXiv 首发 2023.

  更新中期天气评测框架，提供基准数据、物理/数据驱动对照与评测规范。

  [正式版本](https://doi.org/10.1029/2023MS004019) · [发表证据](https://doi.org/10.1029/2023MS004019) · [代码](https://github.com/google-research/weatherbench2)（作者/项目仓库已核验）

<a id="paper-largest"></a>

- **LargeST** — Xu Liu et al. **[LargeST: A Benchmark Dataset for Large-Scale Traffic Forecasting](https://arxiv.org/abs/2306.08259)**. 2023 · NeurIPS Datasets and Benchmarks.

  提供大规模、多年交通传感器数据及元数据，便于研究预测准确率与计算开销。

  [发表证据](https://github.com/liuxu77/LargeST) · [代码](https://github.com/liuxu77/LargeST)（作者/项目仓库已核验）

<a id="paper-libcity"></a>

- **LibCity** — Jiawei Jiang et al. **[LibCity: A Unified Library Towards Efficient and Comprehensive Urban Spatial-Temporal Prediction](https://arxiv.org/abs/2304.14343)**. 2023 · arXiv；正式发表状态未核验.

  将城市预测模型、数据格式和评测流程组织到统一工具库；本条收录扩展稿。

  [发表证据](https://arxiv.org/abs/2304.14343) · [代码](https://github.com/LibCity/Bigscity-LibCity)（作者/项目仓库已核验）

  版本/使用说明：此条对应 2023 扩展预印本；不将早期工具论文的发表信息套用到扩展稿。

<a id="paper-openstl"></a>

- **OpenSTL** — Cheng Tan et al. **[OpenSTL: A Comprehensive Benchmark of Spatio-Temporal Predictive Learning](https://arxiv.org/abs/2306.11249)**. 2023 · NeurIPS Datasets and Benchmarks.

  统一多类时空帧预测模型与评测任务，覆盖视频、交通网格和天气。

  [发表证据](https://github.com/chengtan9907/OpenSTL) · [代码](https://github.com/chengtan9907/OpenSTL)（作者/项目仓库已核验）

<a id="paper-sevir"></a>

- **SEVIR** — Mark Veillette et al. **[SEVIR : A Storm Event Imagery Dataset for Deep Learning Applications in Radar and Satellite Meteorology](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html)**. 2020 · NeurIPS.

  提供时空对齐的雷达与卫星风暴事件影像，支撑降水预测及跨传感器任务。

  [正式版本](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html) · [发表证据](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html) · [代码](https://github.com/MIT-AI-Accelerator/neurips-2020-sevir)（作者/项目仓库已核验）

<a id="paper-weatherbench"></a>

- **WeatherBench** — Stephan Rasp et al. **[WeatherBench: A Benchmark Data Set for Data‐Driven Weather Forecasting](https://arxiv.org/abs/2002.00469)**. 2020 · Journal of Advances in Modeling Earth Systems.

  建立数据驱动天气预测的数据、基线与统一指标入口。

  [正式版本](https://doi.org/10.1029/2020MS002203) · [发表证据](https://doi.org/10.1029/2020MS002203) · [代码](https://github.com/pangeo-data/WeatherBench)（作者/项目仓库已核验）


<a id="topic-related"></a>

## 13 · 相关时间序列基线与插补背景

这些方法不天然具备物理空间结构，单独列出避免混淆。

<a id="paper-itransformer"></a>

- **iTransformer** — Yong Liu et al. **[iTransformer: Inverted Transformers Are Effective for Time Series Forecasting](https://arxiv.org/abs/2310.06625)**. 2024 · ICLR；arXiv 首发 2023.

  将变量而非时间点作为 token，作为跨变量建模的通用对照。

  [发表证据](https://github.com/thuml/iTransformer) · [代码](https://github.com/thuml/iTransformer)（作者/项目仓库已核验）

<a id="paper-dlinear"></a>

- **DLinear** — Ailing Zeng et al. **[Are Transformers Effective for Time Series Forecasting?](https://arxiv.org/abs/2205.13504)**. 2023 · AAAI；arXiv 首发 2022.

  以分解加线性层审视长序列预测，是复杂模型需要比较的简洁时间基线。

  [发表证据](https://github.com/cure-lab/LTSF-Linear) · [代码](https://github.com/cure-lab/LTSF-Linear)（作者/项目仓库已核验）

<a id="paper-patchtst"></a>

- **PatchTST** — Yuqi Nie et al. **[A Time Series is Worth 64 Words: Long-term Forecasting with Transformers](https://arxiv.org/abs/2211.14730)**. 2023 · ICLR；arXiv 首发 2022.

  将时间序列切成 patch 并使用通道独立 Transformer，作为通用时间基线。

  [发表证据](https://github.com/yuqinie98/PatchTST) · [代码](https://github.com/yuqinie98/PatchTST)（作者/项目仓库已核验）

<a id="paper-timesnet"></a>

- **TimesNet** — Haixu Wu et al. **[TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis](https://arxiv.org/abs/2210.02186)**. 2023 · ICLR；arXiv 首发 2022.

  将序列的周期变化映射为二维结构，联合建模周期内与周期间变化。

  [发表证据](https://github.com/thuml/TimesNet) · [代码](https://github.com/thuml/TimesNet)（作者/项目仓库已核验）

<a id="paper-csdi"></a>

- **CSDI** — Yusuke Tashiro et al. **[CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation](https://arxiv.org/abs/2107.03502)**. 2021 · NeurIPS.

  主要研究条件扩散时间序列插补，可作缺失数据背景；不作为直接时空预测模型。

  [发表证据](https://github.com/ermongroup/CSDI) · [代码](https://github.com/ermongroup/CSDI)（作者/项目仓库已核验）

  版本/使用说明：主任务为插补；不计入直接时空预测方法。

<a id="paper-timegrad"></a>

- **TimeGrad** — Kashif Rasul et al. **[Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting](https://arxiv.org/abs/2101.12072)**. 2021 · ICML.

  用自回归去噪扩散进行多变量概率预测；用于概率建模对照。

  [发表证据](https://arxiv.org/abs/2101.12072) · 代码：未核验到作者代码


## 比较论文时先对齐的条件

数据版本、时间划分、采样间隔、输入窗口、预测步数、缺失/零值掩码、归一化、外部模态、预训练数据、验证选择和计算预算会直接影响比较。使用验证集选择配置后，再对选定模型做测试集评估；不以测试集结果选择配置。

LargeST 的 SD/GBA/GLA/CA、经典 PeMS 子集、METR-LA/PEMS-BAY、气象 ERA5/SEVIR 的任务与指标不可直接混排。也不要用论文发表年份或代码存在与否推断模型更强。

## 维护

以 `papers.json` 为单一数据源，同时维护 `summary_zh` / `summary_en` 和 `notes` / `notes_en`。修改后在本目录运行 `python scripts/build_catalog.py`，同步生成中英文 README、年度索引、CSV 与 BibTeX，并检查统计。贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

每周检索新论文、核验论文与官方代码链接，去重后更新目录，并在 [更新记录](updates/README.md) 中保存每次新增、修订和待核验项。检索截止日期由 `catalog_meta.json` 记录，只有完成检索后才推进。

## 贡献者

- [13348952](https://github.com/13348952)：项目发起与维护。
- **Codex（OpenAI）**：AI 辅助文献检索、来源与代码链接核验、分类摘要、目录生成和持续维护。详见 [贡献说明](CONTRIBUTORS.md)。

本目录只整理文献信息、链接及原创简短说明；论文、数据、代码和模型分别遵循原作者及发布方许可。组织形式参考 RSPapers，内容按时空预测任务重新检索和组织。
