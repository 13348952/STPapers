# 按年份浏览

[返回主目录](README.md)

年份依据与代码标记见主目录。以下复用同一结构化数据，不额外增加论文数。

## 2026（24 篇）

- **STRP** — Shuhao Li et al. **[From Coarse to Fine: Managing Temporal Granularity in Spatio-Temporal Data for Fine-Grained Traffic Prediction](https://arxiv.org/abs/2606.09392)**. 2026 · arXiv；正式发表状态未核验.

  研究不同时间粒度之间的交通预测：从粗采样历史预测细粒度未来，采用 Tree Convolution 做空间建模，并用 Inverse Dilated Convolution 做逐步时间外推，同时区分 window-based 与 duration-based 设定。

  [发表证据](https://arxiv.org/abs/2606.09392) · 代码：未核验到作者代码

  版本/使用说明：输入与输出时间粒度不同于常规同分辨率预测；保留 arXiv 预印本记录，未核验到正式发表版本或作者代码。

- **IGSTGNN** — Lixiang Fan et al. **[Incident-Guided Spatiotemporal Traffic Forecasting](https://arxiv.org/abs/2602.02528)**. 2026 · KDD.

  结合事故上下文的空间融合（ICSF）与时间事故影响衰减（TIID）来建模交通历史与外部事故信息，并附带交通/事故对齐数据集。

  [正式版本](https://doi.org/10.1145/3770854.3780215) · [发表证据](https://github.com/fanlixiang/IGSTGNN) · [代码](https://github.com/fanlixiang/IGSTGNN)（作者/项目仓库已核验）

  版本/使用说明：KDD 2026 信息依据作者仓库引用，出版者页面本次未成功访问。使用事故上下文，比较时需对齐事故信息的可用时点和输入范围；已检查训练入口，未运行实验。

- **ATPO** — Hongxin Yu et al. **[Uncertainty-Aware Coordinated Multi-Ramp Metering Based on an Action-Conditioned Traffic Prediction Operator Under Sparse Observations](https://arxiv.org/abs/2611.01270)**. 2026 · arXiv；正式发表状态未核验.

  从稀疏交通观测、缺失掩码与候选控制动作预测未来密度和速度分布，并用于不确定性感知的多匝道协调控制。

  [发表证据](https://arxiv.org/abs/2611.01270) · 代码：未核验到作者代码

  版本/使用说明：动作条件预测与被动交通预测的输入不同；论文采用仿真走廊评估，不能解释为现场部署验证。未核验到作者代码。

- **FAST-SSM** — Xinjin Li et al. **[FAST: A Synergistic Framework of Attention and State-space Models for Spatiotemporal Traffic Prediction](https://arxiv.org/abs/2604.13453)**. 2026 · ICME.

  结合时间注意力与 Mamba 空间模块；与 KDD 2026 的 FaST 是不同论文。

  [发表证据](https://arxiv.org/abs/2604.13453) · 代码：未核验到作者代码

- **SpecLST** — Kenan Kang et al. **[SpecLST: Spectral-Enhanced Long-Short Term Spatio-Temporal Multimodal Modeling for Traffic Forecasting](https://arxiv.org/abs/2610.36393)**. 2026 · arXiv；正式发表状态未核验.

  以频域长历史表示融合天气、事故等上下文，并采用稀疏 MoE；属于多模态设置。

  [发表证据](https://arxiv.org/abs/2610.36393) · 代码：未核验到作者代码

- **FaST** — Yiji Zhao et al. **[FaST: Efficient and Effective Long-Horizon Forecasting for Large-Scale Spatial-Temporal Graphs via Mixture-of-Experts](https://arxiv.org/abs/2601.05174)**. 2026 · KDD.

  以自适应图代理注意力和异质性感知 MoE，面向大规模、长预测跨度的时空图。

  [发表证据](https://github.com/yijizhao/FaST) · [代码](https://github.com/yijizhao/FaST)（作者/项目仓库已核验）

  版本/使用说明：关注长跨度与大图；不把论文摘要的性能表述当成跨设置的统一排名。

- **HieraMix** — Yongyao Wang et al. **[HieraMix: A Hierarchical MLP-Mixer for Large-Scale Traffic Forecasting](https://ijcai.org/proceedings/2026/729)**. 2026 · IJCAI.

  通过分层时空混合及自适应区域混合，构建面向大规模路网的 MLP 架构。

  [正式版本](https://ijcai.org/proceedings/2026/729) · [发表证据](https://ijcai.org/proceedings/2026/729) · 代码：未核验到作者代码

- **LoReST** — Qi Feng et al. **[Learning Local Heterogeneity and Cross-Region Context for Large-Scale Traffic Forecasting](https://arxiv.org/abs/2609.27637)**. 2026 · arXiv；正式发表状态未核验.

  结合关系感知局部聚合与区域汇聚、交互和回传，建模局部异质性及跨区域上下文。

  [发表证据](https://arxiv.org/abs/2609.27637) · 代码：未核验到作者代码

- **MiniST** — Sheng Huang et al. **[MiniST: Unlocking Input Window Length in Traffic Flow Forecasting with Compact Parameters](https://ijcai.org/proceedings/2026/298)**. 2026 · IJCAI.

  将长交通历史投影为紧凑正交基，并结合模板更新模块处理长历史输入。

  [正式版本](https://ijcai.org/proceedings/2026/298) · [发表证据](https://ijcai.org/proceedings/2026/298) · [代码](https://github.com/enheng66/MiniST)（项目仓库可访问，归属链待补强）

  版本/使用说明：仓库示例 seq_len=720；与短历史基线比较时需对齐输入窗口。

- **SAGT** — Amirhossein Ghaffari et al. **[Spectral Adaptive Graph Transformer for Efficient and Scalable Traffic Forecasting](https://arxiv.org/abs/2610.25140)**. 2026 · arXiv；正式发表状态未核验.

  结合学习式低秩有向空间算子、局部图扩散和频率重加权，研究预测开销。

  [发表证据](https://arxiv.org/abs/2610.25140) · [代码](https://github.com/Ahghaffari/sagt)（作者/项目仓库已核验）

- **SqLinear** — Yongfeng Su et al. **[SqLinear: Balanced Square Partitioning Makes Linear Interaction Sufficient for Large-Scale Traffic Forecasting](https://arxiv.org/abs/2606.21072)**. 2026 · arXiv；正式发表状态未核验.

  以均衡空间划分配合分层线性交互，研究大规模交通预测的效率。

  [发表证据](https://arxiv.org/abs/2606.21072) · 代码：未核验到作者代码

- **RAGC** — Kaiqi Wu et al. **[Efficient Traffic Forecasting on Large-Scale Road Network by Regularized Adaptive Graph Convolution](https://arxiv.org/abs/2506.07179)**. 2026 · ICDE；arXiv 首发 2025.

  面向大规模交通预测，以高效余弦算子降低图卷积复杂度，并通过随机共享嵌入与残差差分机制正则化自适应图学习。

  [正式版本](https://doi.org/10.1109/ICDE65706.2026.00068) · [发表证据](https://doi.org/10.1109/ICDE65706.2026.00068) · [代码](https://github.com/wkq-wukaiqi/RAGC)（作者/项目仓库已核验）

  版本/使用说明：arXiv v1（2025-06-08）题为 Regularized Adaptive Graph Learning for Large-Scale Traffic Forecasting，简称 RAGL；v3（2026-04-30）采用现标题，按同一工作收录，不重复计数。作者顺序采用正式出版元数据及 v3。已检查作者源码与运行说明，未运行训练或验证性能。

- **PIMCST** — Abdul Joseph Fofanah et al. **[PIMCST: Physics-Informed Multi-Phase Consensus and Spatio-Temporal Few-Shot Learning for Traffic Flow Forecasting](https://arxiv.org/abs/2602.01936)**. 2026 · arXiv；正式发表状态未核验.

  以扩散、同步和谱表示构建多阶段共识，并用元学习适配少样本跨城市预测。

  [发表证据](https://arxiv.org/abs/2602.01936) · [代码](https://github.com/afofanah/MCPST)（作者/项目仓库已核验）

  版本/使用说明：标题使用 PIMCST，而摘要/仓库使用 MCPST；保留该命名差异。

- **UrbanPG** — Aoyu Liu et al. **[UrbanPG: An Efficient Framework with Personalized Context and General Backbone Interaction for Urban Spatio-Temporal Learning](https://ojs.aaai.org/index.php/AAAI/article/view/38554)**. 2026 · AAAI.

  分离个性化上下文与通用骨干，研究大规模预测、少样本迁移和持续学习。

  [正式版本](https://ojs.aaai.org/index.php/AAAI/article/view/38554) · [发表证据](https://ojs.aaai.org/index.php/AAAI/article/view/38554) · [代码](https://github.com/Aoyu-Liu/UrbanPG)（作者/项目仓库已核验）

  版本/使用说明：GitHub About 仍出现 AAAI 2025 字样，README 与正式会议页为 AAAI 2026；以会议页为准。

- **OmniST** — Praveg Vashishtha **[OmniST: Topology-Invariant Spatiotemporal Forecasting with Guaranteed-Coverage Uncertainty at Unseen Sensor Locations](https://arxiv.org/abs/2611.04256)**. 2026 · arXiv；正式发表状态未核验.

  以坐标编码、动态近邻注意力和逐节点循环网络处理变化的传感器集合，并结合共形校准预测未见位置及其不确定性。

  [发表证据](https://arxiv.org/abs/2611.04256) · [代码](https://github.com/Praveg432/OmniST)（作者/项目仓库已核验）

  版本/使用说明：覆盖保证依赖校准与测试分数的交换性；局部拓扑不变性有近邻集合不变等条件。已检查模型源码和运行入口，未训练复现。

- **FactoST-v2** — Siru Zhong et al. **[Learning to Factorize and Adapt: A Versatile Approach Toward Universal Spatio-Temporal Foundation Models](https://arxiv.org/abs/2601.12083)**. 2026 · arXiv；正式发表状态未核验.

  分离通用时间预训练与领域空间适配，扩展至可变长度和概率分位数预测。

  [发表证据](https://arxiv.org/abs/2601.12083) · [代码](https://github.com/CityMind-Lab/FactoST)（论文提供链接，本次返回 404）

  版本/使用说明：2026 扩展稿，不等同于其 NeurIPS 2025 会议版本；论文给出的仓库本次返回 404。

- **E2Forecast** — Jingtao Li et al. **[Forecasting Earth Surface Change in Embedding Space](https://arxiv.org/abs/2611.02211)**. 2026 · arXiv；正式发表状态未核验.

  从不规则卫星观测序列预测未来地表嵌入，结合高斯分支与整流流分支，并接受未来查询日期。

  [发表证据](https://arxiv.org/abs/2611.02211) · [代码](https://github.com/ucam-eo/e2forecast)（作者/项目仓库已核验）

  版本/使用说明：预测目标是地表嵌入，不是原始像素。作者仓库含模型、训练和评估说明；部分 GSA 嵌入与带日期 SSL4EO 数据仍待发布，未训练复现。

- **CoReFlow** — Pengnan Chi et al. **[CoReFlow: Consistency-Relaxed Flow Maps for Probabilistic Traffic Forecasting](https://arxiv.org/abs/2611.05715)**. 2026 · arXiv；正式发表状态未核验.

  通过一致性松弛的流映射学习概率交通预测，以端点训练和条件均值约束支持单步生成。

  [发表证据](https://arxiv.org/abs/2611.05715) · 代码：未核验到作者代码

  版本/使用说明：论文称代码位于补充材料；本次未取得并核验该材料中的实现，未确认公开作者仓库。勿与同名的低秩矩阵生成工作混淆。

- **FitzRoy** — Ozan Sener et al. **[Skillful and realistic precipitation forecasting with reinforced diffusion](https://arxiv.org/abs/2610.38775)**. 2026 · arXiv；正式发表状态未核验.

  以强化学习细化条件离散扩散模型，预测未来降水空间场。

  [发表证据](https://arxiv.org/abs/2610.38775) · 代码：未核验到作者代码

  版本/使用说明：完整模型使用 ERA5、MRMS 与 NBM 预报引导；须与不使用 NBM 的独立变体区分。未核验到作者代码，论文中的其他模型仓库链接不代表本方法代码。

- **Sonny-ENS** — Minjong Cheon **[Sonny-ENS: demystifying machine-learning ensemble weather forecasting](https://arxiv.org/abs/2611.01614)**. 2026 · arXiv；正式发表状态未核验.

  以 CRPS 训练多个天气网络，并通过 Monte Carlo dropout 构造集合预报。

  [发表证据](https://arxiv.org/abs/2611.01614) · 代码：未核验到作者代码

  版本/使用说明：论文称代码和权重将在发表时开放；本次未确认公开发布，不能将未来开放承诺视为已有可用实现。

- **LCG-SFNO** — Yaojun Li et al. **[Low-Rank Clebsch--Gordan Coupling for Equivariant Spherical Forecasting](https://arxiv.org/abs/2611.03411)**. 2026 · arXiv；正式发表状态未核验.

  通过低秩 Clebsch–Gordan 耦合构造球面谱非线性交互，研究等变球面动力学与天气预测。

  [发表证据](https://arxiv.org/abs/2611.03411) · 代码：未核验到作者代码

  版本/使用说明：未核验到作者代码；论文报告的等变性和计算效率未经本目录独立数值复现。

- **AI-Ensemble-Blend** — Harris Sop Nkuiate et al. **[Value of Adding AI Weather Model Ensembles to a Multi-model Probabilistic Blend](https://arxiv.org/abs/2610.42130)**. 2026 · arXiv；正式发表状态未核验.

  研究将 AI 天气集合加入多模型概率融合，并分析校准、成员多样性与概率预报质量。

  [发表证据](https://arxiv.org/abs/2610.42130) · 代码：未核验到作者代码

  版本/使用说明：AI-Ensemble-Blend 是本目录索引简称。该工作组合已有预报，比较时需对齐组成模型与输入；未核验到作者代码。

- **TaiJi** — Jiale Wang et al. **[TaiJi: State-Conditional Adaptive Combination of Machine-Learning and Physics-Based Global Weather Forecasts](https://arxiv.org/abs/2609.31972)**. 2026 · arXiv；正式发表状态未核验.

  由近期大气状态生成随网格位置和预测步长变化的组合权重与残差，融合机器学习及物理天气预报。

  [发表证据](https://arxiv.org/abs/2609.31972) · 代码：未核验到作者代码

  版本/使用说明：arXiv 首发 2026-09-25，v3 修订 2026-11-02；因窗口内修订首次补入本目录，不是本周首发。已核验主源元数据与摘要，HTML 不可用，未核验到作者代码。

- **SwAIther-Precip** — Dan Assouline et al. **[SwAIther-Precip: Lead-Time-Aware Bias Correction Enables Kilometer-Scale Downscaling of Global AI Precipitation Forecasts over Switzerland](https://arxiv.org/abs/2605.16163)**. 2026 · arXiv；正式发表状态未核验.

  先以预测步长条件化的 U-Net 校正粗网格降水偏差，再通过扩散超分辨率生成瑞士地区概率降水场。

  [发表证据](https://arxiv.org/abs/2605.16163) · [代码](https://github.com/danassou/swaither-precip)（作者/项目仓库已核验）

  版本/使用说明：首发 2026-05-15，v3 修订 2026-10-29；本次为修订触发的目录补录。已检查作者源码与训练说明；论文专用 AIFS 历史预测数据未公开，其他数据获取条件需单独核对，未训练复现。


## 2025（9 篇）

- **STFM-survey** — Yuxuan Liang et al. **[Foundation Models for Spatio-Temporal Data Science: A Tutorial and Survey](https://arxiv.org/abs/2503.13502)**. 2025 · arXiv；正式发表状态未核验.

  梳理时空基础模型及其在感知、管理、挖掘中的作用，作为广义背景。

  [发表证据](https://arxiv.org/abs/2503.13502) · 代码：未核验到作者代码

- **GraphSparseNet** — Weiyang Kong et al. **[GraphSparseNet: a Novel Method for Large Scale Traffic Flow Prediction](https://arxiv.org/abs/2502.19823)**. 2025 · PVLDB.

  通过特征提取与关系压缩模块，降低大规模路网关系建模成本。

  [发表证据](https://arxiv.org/abs/2502.19823) · 代码：未核验到作者代码

- **PatchSTG** — Yuchen Fang et al. **[Efficient Large-Scale Traffic Forecasting with Transformers: A Spatial Data Management Perspective](https://arxiv.org/abs/2412.09972)**. 2025 · KDD；arXiv 首发 2024.

  利用 KDTree 构造不规则空间分块，以块内与跨块注意力学习局部和全局关系。

  [发表证据](https://arxiv.org/abs/2412.09972) · [代码](https://github.com/LMissher/PatchSTG)（作者/项目仓库已核验）

- **HGAurban** — Qianru Zhang et al. **[HGAurban: Heterogeneous Graph Autoencoding for Urban Spatial-Temporal Learning](https://arxiv.org/abs/2410.10915)**. 2025 · CIKM；arXiv 首发 2024.

  以异质图掩码自编码学习区域表示，服务城市时空任务；包含预测以外的任务。

  [发表证据](https://arxiv.org/abs/2410.10915) · 代码：未核验到作者代码

  版本/使用说明：arXiv 当前题名为 HGAurban；早期检索记录出现 Graph Masked Autoencoder，按同一标识符合并。

- **ST-VFM** — Changlu Chen et al. **[Reprogramming Vision Foundation Models for Spatio-Temporal Forecasting](https://arxiv.org/abs/2507.11558)**. 2025 · arXiv；正式发表状态未核验.

  通过时序适配与双分支提示协调，将冻结视觉基础模型用于时空预测。

  [发表证据](https://arxiv.org/abs/2507.11558) · 代码：未核验到作者代码

- **Aurora** — Cristian Bodnar et al. **[A foundation model for the Earth system](https://arxiv.org/abs/2405.13063)**. 2025 · Nature；arXiv 首发 2024.

  在多源地球系统数据上预训练，并适配天气、空气质量、海浪等任务。

  [正式版本](https://doi.org/10.1038/s41586-025-09005-y) · [发表证据](https://doi.org/10.1038/s41586-025-09005-y) · [代码](https://github.com/microsoft/aurora)（作者/项目仓库已核验）

- **FengWu** — Kang Chen et al. **[FengWu: Pushing the Skillful Global Medium-range Weather Forecast beyond 10 Days Lead](https://arxiv.org/abs/2304.02948)**. 2025 · Communications Earth & Environment；arXiv 首发 2023.

  以多模态、多任务结构、跨模态融合和回放缓冲提升中期天气建模。

  [发表证据](https://github.com/OpenEarthLab/FengWu) · [代码](https://github.com/OpenEarthLab/FengWu)（作者/项目仓库已核验）

- **GenCast** — Ilan Price et al. **[Probabilistic weather forecasting with machine learning](https://arxiv.org/abs/2312.15796)**. 2025 · Nature；arXiv 首发 2023.

  使用扩散生成集合预报，刻画未来全球天气状态的联合不确定性。

  [正式版本](https://doi.org/10.1038/s41586-024-08252-9) · [发表证据](https://doi.org/10.1038/s41586-024-08252-9) · [代码](https://github.com/google-deepmind/graphcast)（作者/项目仓库已核验）

  版本/使用说明：采用 Nature 2025 卷期年；2024-12-04 在线发表，预印本首发于 2023。

- **TraffiDent** — Xiaochuan Gou et al. **[TraffiDent: A Dataset for Understanding the Interplay Between Traffic Dynamics and Incidents](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html)**. 2025 · NeurIPS Datasets and Benchmarks.

  对齐交通状态、事故及道路属性，支持事故后的交通预测和相关分析。

  [正式版本](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html) · [发表证据](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html) · 代码：未核验到作者代码


## 2024（13 篇）

- **Urban-STGNN-survey** — Guangyin Jin et al. **[Spatio-Temporal Graph Neural Networks for Predictive Learning in Urban Computing: A Survey](https://arxiv.org/abs/2303.14483)**. 2024 · IEEE TKDE；arXiv 首发 2023.

  面向城市计算，梳理时空图构建、模型设计与不同预测应用。

  [正式版本](https://doi.org/10.1109/TKDE.2023.3333824) · [发表证据](https://doi.org/10.1109/TKDE.2023.3333824) · 代码：未核验到作者代码

- **STG-Mamba** — Lincan Li et al. **[STG-Mamba: Spatial-Temporal Graph Learning via Selective State Space Model](https://arxiv.org/abs/2403.12418)**. 2024 · arXiv；正式发表状态未核验.

  本文提出 STG-Mamba，将选择性状态空间模型引入时空图学习，用 ST-S3M 建模跨时间的动态状态演化，并结合 KFGN 做多时间粒度的图表示融合。

  [发表证据](https://arxiv.org/abs/2403.12418) · [代码](https://github.com/LincanLi-X/STG-Mamba)（作者/项目仓库已核验）

  版本/使用说明：保留 arXiv 2024 记录，正式发表状态未核验。论文链接的旧仓库地址重定向至 LincanLi-X；已检查 main.py，未训练复现。

- **STGformer** — Hongjun Wang et al. **[STGformer: Efficient Spatiotemporal Graph Transformer for Traffic Forecasting](https://arxiv.org/abs/2410.00385)**. 2024 · arXiv；正式发表状态未核验.

  提出面向交通预测的高效时空图 Transformer，将图卷积与 Transformer 结合，用单个 STG attention block 捕捉高阶时空交互，并在 LargeST 等设置上评估效率与效果。

  [发表证据](https://arxiv.org/abs/2410.00385) · [代码](https://github.com/Dreamzz5/STGformer)（作者/项目仓库已核验）

  版本/使用说明：论文直接链接作者仓库，已检查 model/train.py 与运行说明，未运行实验。保留 arXiv 2024；与同名的人体姿态、轨迹及稀疏感知论文区分，不将速度报告泛化为跨设置结论。

- **BigST** — Jindong Han et al. **[BigST: Linear Complexity Spatio-Temporal Graph Neural Network for Traffic Forecasting on Large-Scale Road Networks](https://www.vldb.org/pvldb/vol17/p1081-han.pdf)**. 2024 · PVLDB.

  预计算长历史表示，并以线性化全局空间建模扩展到大规模路网。

  [正式版本](https://doi.org/10.14778/3641204.3641217) · [发表证据](https://doi.org/10.14778/3641204.3641217) · [代码](https://github.com/usail-hkust/BigST)（作者/项目仓库已核验）

- **STDMAE** — Haotian Gao et al. **[Spatial-Temporal-Decoupled Masked Pre-training for Spatiotemporal Forecasting](https://arxiv.org/abs/2312.00516)**. 2024 · IJCAI；arXiv 首发 2023.

  分别沿空间与时间维度进行掩码重建，把预训练表示用于下游预测。

  [发表证据](https://github.com/Jimmy-7664/STD-MAE) · [代码](https://github.com/Jimmy-7664/STD-MAE)（作者/项目仓库已核验）

- **HimNet** — Zheng Dong et al. **[Heterogeneity-Informed Meta-Parameter Learning for Spatiotemporal Time Series Forecasting](https://arxiv.org/abs/2405.10800)**. 2024 · KDD.

  通过时空嵌入与元参数池学习具有时空差异的模型参数。

  [发表证据](https://github.com/XDZhelheim/HimNet) · [代码](https://github.com/XDZhelheim/HimNet)（作者/项目仓库已核验）

- **STLLM** — Chenxi Liu et al. **[Spatial-Temporal Large Language Model for Traffic Prediction](https://arxiv.org/abs/2401.10134)**. 2024 · IEEE MDM.

  把时空嵌入接入大语言模型，并通过部分冻结注意力适配交通预测。

  [发表证据](https://github.com/ChenxiLiu-HNU/ST-LLM) · [代码](https://github.com/ChenxiLiu-HNU/ST-LLM)（作者/项目仓库已核验）

- **UniST** — Yuan Yuan et al. **[UniST: A Prompt-Empowered Universal Model for Urban Spatio-Temporal Prediction](https://arxiv.org/abs/2402.11838)**. 2024 · KDD.

  通过多场景预训练与知识引导提示，探索统一城市时空预测模型。

  [发表证据](https://github.com/tsinghua-fib-lab/UniST) · [代码](https://github.com/tsinghua-fib-lab/UniST)（作者/项目仓库已核验）

- **UrbanGPT** — Zhonghang Li et al. **[UrbanGPT: Spatio-Temporal Large Language Models](https://arxiv.org/abs/2403.00813)**. 2024 · KDD.

  结合时空依赖编码器和指令微调，探索城市任务的零样本泛化。

  [发表证据](https://github.com/HKUDS/UrbanGPT) · [代码](https://github.com/HKUDS/UrbanGPT)（作者/项目仓库已核验）

- **SpecSTG** — Lequan Lin et al. **[SpecSTG: A Fast Spectral Diffusion Framework for Probabilistic Spatio-Temporal Traffic Forecasting](https://arxiv.org/abs/2401.08119)**. 2024 · arXiv；正式发表状态未核验.

  在频谱域生成未来序列，并结合空间依赖与频谱图卷积。

  [发表证据](https://arxiv.org/abs/2401.08119) · [代码](https://anonymous.4open.science/r/SpecSTG)（论文提供匿名代码，访问未核验）

  版本/使用说明： 当前列出已核验的 arXiv 版本；不据此断言没有正式发表版本。

- **BasicTS** — Zezhi Shao et al. **[Exploring Progress in Multivariate Time Series Forecasting: Comprehensive Benchmarking and Heterogeneity Analysis](https://arxiv.org/abs/2310.06119)**. 2024 · IEEE TKDE；arXiv 首发 2023.

  通过统一评测流程与时空异质性分析，研究多变量预测结果为何难以直接比较。

  [发表证据](https://github.com/GestaltCogTeam/BasicTS) · [代码](https://github.com/GestaltCogTeam/BasicTS)（作者/项目仓库已核验）

- **WeatherBench2** — Stephan Rasp et al. **[WeatherBench 2: A Benchmark for the Next Generation of Data‐Driven Global Weather Models](https://arxiv.org/abs/2308.15560)**. 2024 · Journal of Advances in Modeling Earth Systems；arXiv 首发 2023.

  更新中期天气评测框架，提供基准数据、物理/数据驱动对照与评测规范。

  [正式版本](https://doi.org/10.1029/2023MS004019) · [发表证据](https://doi.org/10.1029/2023MS004019) · [代码](https://github.com/google-research/weatherbench2)（作者/项目仓库已核验）

- **iTransformer** — Yong Liu et al. **[iTransformer: Inverted Transformers Are Effective for Time Series Forecasting](https://arxiv.org/abs/2310.06625)**. 2024 · ICLR；arXiv 首发 2023.

  将变量而非时间点作为 token，作为跨变量建模的通用对照。

  [发表证据](https://github.com/thuml/iTransformer) · [代码](https://github.com/thuml/iTransformer)（作者/项目仓库已核验）


## 2023（19 篇）

- **DGCRN** — Fuxian Li et al. **[Dynamic Graph Convolutional Recurrent Network for Traffic Prediction: Benchmark and Solution](https://arxiv.org/abs/2104.14917)**. 2023 · ACM TKDD；arXiv 首发 2021.

  由节点动态信息生成图结构，同时提供交通预测的统一评测与实现。

  [发表证据](https://github.com/tsinghua-fib-lab/Traffic-Benchmark) · [代码](https://github.com/tsinghua-fib-lab/Traffic-Benchmark)（作者/项目仓库已核验）

- **PDFormer** — Jiawei Jiang et al. **[PDFormer: Propagation Delay-Aware Dynamic Long-Range Transformer for Traffic Flow Prediction](https://arxiv.org/abs/2301.07945)**. 2023 · AAAI.

  结合短程/长程图掩码与传播延迟感知变换，建模动态空间关系。

  [发表证据](https://github.com/BUAABIGSCity/PDFormer) · [代码](https://github.com/BUAABIGSCity/PDFormer)（作者/项目仓库已核验）

- **STAEformer** — Hangchen Liu et al. **[STAEformer: Spatio-Temporal Adaptive Embedding Makes Vanilla Transformer SOTA for Traffic Forecasting](https://arxiv.org/abs/2308.10425)**. 2023 · CIKM Short.

  研究时空自适应嵌入如何增强普通 Transformer 的交通预测能力。

  [发表证据](https://github.com/XDZhelheim/STAEformer) · [代码](https://github.com/XDZhelheim/STAEformer)（作者/项目仓库已核验）

- **STSSL** — Jiahao Ji et al. **[Spatio-Temporal Self-Supervised Learning for Traffic Flow Prediction](https://arxiv.org/abs/2212.04475)**. 2023 · AAAI；arXiv 首发 2022.

  利用自适应图增强与空间/时间自监督任务，学习异质交通模式。

  [发表证据](https://github.com/Echo-Ji/ST-SSL) · [代码](https://github.com/Echo-Ji/ST-SSL)（作者/项目仓库已核验）

- **MegaCRN** — Renhe Jiang et al. **[Spatio-Temporal Meta-Graph Learning for Traffic Forecasting](https://arxiv.org/abs/2211.14701)**. 2023 · AAAI；arXiv 首发 2022.

  借助元节点记忆与元图学习，刻画交通节点和时间模式的异质性。

  [发表证据](https://github.com/deepkashiwa20/MegaCRN) · [代码](https://github.com/deepkashiwa20/MegaCRN)（作者/项目仓库已核验）

  版本/使用说明：采用 AAAI 2023 对应的 arXiv:2211.14701；不使用已撤回的扩展稿 arXiv:2212.05989。

- **DiffSTG** — Haomin Wen et al. **[DiffSTG: Probabilistic Spatio-Temporal Graph Forecasting with Denoising Diffusion Models](https://arxiv.org/abs/2301.13629)**. 2023 · ACM SIGSPATIAL.

  将去噪扩散模型推广到时空图，进行非自回归概率预测。

  [发表证据](https://arxiv.org/abs/2301.13629) · 代码：未核验到作者代码

- **TAU** — Cheng Tan et al. **[Temporal Attention Unit: Towards Efficient Spatiotemporal Predictive Learning](https://arxiv.org/abs/2206.12126)**. 2023 · CVPR；arXiv 首发 2022.

  将时间注意力拆分为帧内和帧间部分，改善并行时空帧预测。

  [发表证据](https://github.com/chengtan9907/OpenSTL) · [代码](https://github.com/chengtan9907/OpenSTL)（作者团队工具库实现已核验）

- **ClimaX** — Tung Nguyen et al. **[ClimaX: A foundation model for weather and climate](https://arxiv.org/abs/2301.10343)**. 2023 · ICML.

  使用异构气候数据预训练，再适配不同天气变量与预测任务。

  [发表证据](https://github.com/microsoft/ClimaX) · [代码](https://github.com/microsoft/ClimaX)（作者/项目仓库已核验）

- **GraphCast** — Remi Lam et al. **[Learning skillful medium-range global weather forecasting](https://arxiv.org/abs/2212.12794)**. 2023 · Science；arXiv 首发 2022.

  以图神经网络学习全球天气场演化，输出中期多变量天气预测。

  [正式版本](https://doi.org/10.1126/science.adi2336) · [发表证据](https://doi.org/10.1126/science.adi2336) · [代码](https://github.com/google-deepmind/graphcast)（作者/项目仓库已核验）

- **NowcastNet** — Yuchen Zhang et al. **[Skilful nowcasting of extreme precipitation with NowcastNet](https://www.nature.com/articles/s41586-023-06184-4)**. 2023 · Nature.

  将物理演化约束与生成建模结合，用于极端降水临近预报。

  [正式版本](https://www.nature.com/articles/s41586-023-06184-4) · [发表证据](https://www.nature.com/articles/s41586-023-06184-4) · 代码：未核验到作者代码

- **Pangu-Weather** — Kaifeng Bi et al. **[Accurate medium-range global weather forecasting with 3D neural networks](https://arxiv.org/abs/2211.02556)**. 2023 · Nature；arXiv 首发 2022.

  以三维地球专用 Transformer 与分层时间聚合处理全球天气预测。

  [正式版本](https://doi.org/10.1038/s41586-023-06185-3) · [发表证据](https://doi.org/10.1038/s41586-023-06185-3) · [代码](https://github.com/198808xc/Pangu-Weather)（作者/项目仓库已核验）

- **LargeST** — Xu Liu et al. **[LargeST: A Benchmark Dataset for Large-Scale Traffic Forecasting](https://arxiv.org/abs/2306.08259)**. 2023 · NeurIPS Datasets and Benchmarks.

  提供大规模、多年交通传感器数据及元数据，便于研究预测准确率与计算开销。

  [发表证据](https://github.com/liuxu77/LargeST) · [代码](https://github.com/liuxu77/LargeST)（作者/项目仓库已核验）

- **LibCity** — Jiawei Jiang et al. **[LibCity: A Unified Library Towards Efficient and Comprehensive Urban Spatial-Temporal Prediction](https://arxiv.org/abs/2304.14343)**. 2023 · arXiv；正式发表状态未核验.

  将城市预测模型、数据格式和评测流程组织到统一工具库；本条收录扩展稿。

  [发表证据](https://arxiv.org/abs/2304.14343) · [代码](https://github.com/LibCity/Bigscity-LibCity)（作者/项目仓库已核验）

  版本/使用说明：此条对应 2023 扩展预印本；不将早期工具论文的发表信息套用到扩展稿。

- **OpenSTL** — Cheng Tan et al. **[OpenSTL: A Comprehensive Benchmark of Spatio-Temporal Predictive Learning](https://arxiv.org/abs/2306.11249)**. 2023 · NeurIPS Datasets and Benchmarks.

  统一多类时空帧预测模型与评测任务，覆盖视频、交通网格和天气。

  [发表证据](https://github.com/chengtan9907/OpenSTL) · [代码](https://github.com/chengtan9907/OpenSTL)（作者/项目仓库已核验）

- **DLinear** — Ailing Zeng et al. **[Are Transformers Effective for Time Series Forecasting?](https://arxiv.org/abs/2205.13504)**. 2023 · AAAI；arXiv 首发 2022.

  以分解加线性层审视长序列预测，是复杂模型需要比较的简洁时间基线。

  [发表证据](https://github.com/cure-lab/LTSF-Linear) · [代码](https://github.com/cure-lab/LTSF-Linear)（作者/项目仓库已核验）

- **PatchTST** — Yuqi Nie et al. **[A Time Series is Worth 64 Words: Long-term Forecasting with Transformers](https://arxiv.org/abs/2211.14730)**. 2023 · ICLR；arXiv 首发 2022.

  将时间序列切成 patch 并使用通道独立 Transformer，作为通用时间基线。

  [发表证据](https://github.com/yuqinie98/PatchTST) · [代码](https://github.com/yuqinie98/PatchTST)（作者/项目仓库已核验）

- **TimesNet** — Haixu Wu et al. **[TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis](https://arxiv.org/abs/2210.02186)**. 2023 · ICLR；arXiv 首发 2022.

  将序列的周期变化映射为二维结构，联合建模周期内与周期间变化。

  [发表证据](https://github.com/thuml/TimesNet) · [代码](https://github.com/thuml/TimesNet)（作者/项目仓库已核验）

- **STGNP** — Junfeng Hu et al. **[Graph Neural Processes for Spatio-Temporal Extrapolation](https://arxiv.org/abs/2305.18719)**. 2023 · KDD.

  这项工作把 Neural Processes 扩展到图上的时空外推任务，显式建模不确定性，并通过 Graph Bayesian Aggregation 融合上下文节点信息。

  [正式版本](https://doi.org/10.1145/3580305.3599372) · [发表证据](https://api.crossref.org/works/10.1145/3580305.3599372) · [代码](https://github.com/hjf1997/STGNP)（作者/项目仓库已核验）

  版本/使用说明：相关任务：依据周围观测推断目标位置，不能等同于未来时间预测。已检查作者仓库层级模型实现和运行说明，未运行实验。

- **GraphDF** — Hongjie Chen et al. **[Graph Deep Factors for Probabilistic Time-series Forecasting](https://arxiv.org/abs/2010.07373)**. 2023 · ACM TKDD；arXiv 首发 2020.

  结合图关系驱动的全局与局部概率模型，描述相关时间序列；正式期刊版本还研究在线增量学习。

  [正式版本](https://doi.org/10.1145/3543511) · [发表证据](https://api.crossref.org/works/10.1145/3543511) · 代码：未核验到作者代码

  版本/使用说明：相关背景：图相关的概率时间序列预测，不预设地理空间。2023 年 TKDD 正式版本扩展了 2020 年预印本并加入在线增量学习；以一个条目记录版本关系，未核验作者代码。


## 2022（11 篇）

- **Traffic-survey** — Weiwei Jiang et al. **[Graph Neural Network for Traffic Forecasting: A Survey](https://arxiv.org/abs/2101.11174)**. 2022 · Expert Systems with Applications；arXiv 首发 2021.

  从图构建、模型、任务及开放资源梳理交通预测中的图神经网络。

  [发表证据](https://arxiv.org/abs/2101.11174) · 代码：未核验到作者代码

- **D2STGNN** — Zezhi Shao et al. **[Decoupled Dynamic Spatial-Temporal Graph Neural Network for Traffic Forecasting](https://arxiv.org/abs/2206.09112)**. 2022 · PVLDB.

  将交通信号拆为扩散与固有成分，结合动态图学习分别建模。

  [发表证据](https://github.com/GestaltCogTeam/D2STGNN) · [代码](https://github.com/GestaltCogTeam/D2STGNN)（作者/项目仓库已核验）

- **DSTAGNN** — Shiyong Lan et al. **[DSTAGNN: Dynamic Spatial-Temporal Aware Graph Neural Network for Traffic Flow Forecasting](https://proceedings.mlr.press/v162/lan22a.html)**. 2022 · ICML.

  结合动态时空关系建模与图网络进行交通预测。

  [正式版本](https://proceedings.mlr.press/v162/lan22a.html) · [发表证据](https://proceedings.mlr.press/v162/lan22a.html) · [代码](https://github.com/SYLan2019/DSTAGNN)（作者/项目仓库已核验）

- **STGNCDE** — Jeongwhan Choi et al. **[Graph Neural Controlled Differential Equations for Traffic Forecasting](https://arxiv.org/abs/2112.03558)**. 2022 · AAAI；arXiv 首发 2021.

  联合空间和时间神经控制微分方程，提供连续时间建模视角。

  [发表证据](https://github.com/jeongwhanchoi/STG-NCDE) · [代码](https://github.com/jeongwhanchoi/STG-NCDE)（作者/项目仓库已核验）

- **STID** — Zezhi Shao et al. **[Spatial-Temporal Identity: A Simple yet Effective Baseline for Multivariate Time Series Forecasting](https://arxiv.org/abs/2208.05233)**. 2022 · CIKM Short.

  把节点与时间身份嵌入接入简洁 MLP，是检验复杂空间模块收益的基础对照。

  [发表证据](https://github.com/GestaltCogTeam/STID) · [代码](https://github.com/GestaltCogTeam/STID)（作者/项目仓库已核验）

- **STEP** — Zezhi Shao et al. **[Pre-training Enhanced Spatial-temporal Graph Neural Network for Multivariate Time Series Forecasting](https://arxiv.org/abs/2206.09113)**. 2022 · KDD.

  通过长历史序列预训练，为下游图预测模型提供时间上下文与结构信息。

  [发表证据](https://github.com/GestaltCogTeam/STEP) · [代码](https://github.com/GestaltCogTeam/STEP)（作者/项目仓库已核验）

- **STGCL** — Xu Liu et al. **[When Do Contrastive Learning Signals Help Spatio-Temporal Graph Forecasting?](https://arxiv.org/abs/2108.11873)**. 2022 · ACM SIGSPATIAL；arXiv 首发 2021.

  系统比较时空图对比学习的接入方式、增强策略与负样本选择。

  [发表证据](https://github.com/liuxu77/STGCL) · [代码](https://github.com/liuxu77/STGCL)（作者/项目仓库已核验）

- **STGP-SPDE** — Alexander V. Nikitin et al. **[Non-separable Spatio-temporal Graph Kernels via SPDEs](https://arxiv.org/abs/2111.08524)**. 2022 · AISTATS；arXiv 首发 2021.

  本文利用 SPDE 与图上的高斯过程联系，推导出非可分的时空图核，用于描述扩散、振荡等跨时空耦合现象。

  [正式版本](https://proceedings.mlr.press/v151/nikitin22a.html) · [发表证据](https://proceedings.mlr.press/v151/nikitin22a.html) · [代码](https://github.com/AaltoPML/spatiotemporal-graph-kernels)（作者/项目仓库已核验）

  版本/使用说明：正式版本为 AISTATS 2022，arXiv 首发 2021。仓库同时包含插值和外推设置，比较时需区分；已检查时空核实现，未运行实验。

- **SimVP** — Zhangyang Gao et al. **[SimVP: Simpler yet Better Video Prediction](https://arxiv.org/abs/2206.05099)**. 2022 · CVPR.

  以卷积编码器、时间处理模块和解码器构成简洁视频/网格预测基线。

  [发表证据](https://github.com/gaozhangyang/SimVP-Simpler-yet-Better-Video-Prediction) · [代码](https://github.com/gaozhangyang/SimVP-Simpler-yet-Better-Video-Prediction)（作者/项目仓库已核验）

- **Earthformer** — Zhihan Gao et al. **[Earthformer: Exploring Space-Time Transformers for Earth System Forecasting](https://arxiv.org/abs/2207.05833)**. 2022 · NeurIPS.

  通过局部 Cuboid Attention 与全局向量交换信息，用于降水及地球系统预测。

  [发表证据](https://github.com/amazon-science/earth-forecasting-transformer) · [代码](https://github.com/amazon-science/earth-forecasting-transformer)（作者/项目仓库已核验）

- **FourCastNet** — Jaideep Pathak et al. **[FourCastNet: A Global Data-driven High-resolution Weather Model using Adaptive Fourier Neural Operators](https://arxiv.org/abs/2202.11214)**. 2022 · arXiv；正式发表状态未核验.

  利用自适应傅里叶神经算子进行高分辨率全球天气预测。

  [发表证据](https://arxiv.org/abs/2202.11214) · [代码](https://github.com/NVlabs/FourCastNet)（作者/项目仓库已核验）


## 2021（7 篇）

- **GTS** — Chao Shang et al. **[Discrete Graph Structure Learning for Forecasting Multiple Time Series](https://arxiv.org/abs/2101.06861)**. 2021 · ICLR.

  学习可微采样的离散图分布，并与多序列预测模型共同优化。

  [发表证据](https://github.com/chaoshangcs/GTS) · [代码](https://github.com/chaoshangcs/GTS)（作者/项目仓库已核验）

- **STFGNN** — Mengzhang Li et al. **[Spatial-Temporal Fusion Graph Neural Networks for Traffic Flow Forecasting](https://arxiv.org/abs/2012.09641)**. 2021 · AAAI；arXiv 首发 2020.

  融合空间图与数据驱动的时间关系图，并结合门控卷积。

  [发表证据](https://github.com/MengzhangLI/STFGNN) · [代码](https://github.com/MengzhangLI/STFGNN)（作者/项目仓库已核验）

  版本/使用说明：作者 README 对部分数据集结果作了更正说明；比较数字前应检查最新论文与仓库。

- **STGODE** — Zheng Fang et al. **[Spatial-Temporal Graph ODE Networks for Traffic Flow Forecasting](https://arxiv.org/abs/2106.12931)**. 2021 · KDD.

  以张量形式的常微分方程建模时空动态，同时考虑空间与语义关系。

  [发表证据](https://github.com/square-coder/STGODE) · [代码](https://github.com/square-coder/STGODE)（作者/项目仓库已核验）

- **STNorm** — Jinliang Deng et al. **[ST-Norm: Spatial and Temporal Normalization for Multi-variate Time Series Forecasting](https://doi.org/10.1145/3447548.3467330)**. 2021 · KDD.

  用空间与时间归一化处理多变量序列中的不同成分，形成简洁预测模块。

  [正式版本](https://doi.org/10.1145/3447548.3467330) · [发表证据](https://doi.org/10.1145/3447548.3467330) · [代码](https://github.com/JLDeng/ST-Norm)（作者/项目仓库已核验）

- **DGMR** — Suman Ravuri et al. **[Skilful precipitation nowcasting using deep generative models of radar](https://arxiv.org/abs/2104.00954)**. 2021 · Nature.

  使用深度生成模型输出具有时空一致性的概率降水临近预报。

  [正式版本](https://doi.org/10.1038/s41586-021-03854-z) · [发表证据](https://doi.org/10.1038/s41586-021-03854-z) · 代码：未核验到作者代码

- **CSDI** — Yusuke Tashiro et al. **[CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation](https://arxiv.org/abs/2107.03502)**. 2021 · NeurIPS.

  主要研究条件扩散时间序列插补，可作缺失数据背景；不作为直接时空预测模型。

  [发表证据](https://github.com/ermongroup/CSDI) · [代码](https://github.com/ermongroup/CSDI)（作者/项目仓库已核验）

  版本/使用说明：主任务为插补；不计入直接时空预测方法。

- **TimeGrad** — Kashif Rasul et al. **[Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting](https://arxiv.org/abs/2101.12072)**. 2021 · ICML.

  用自回归去噪扩散进行多变量概率预测；用于概率建模对照。

  [发表证据](https://arxiv.org/abs/2101.12072) · 代码：未核验到作者代码


## 2020（9 篇）

- **STTP-survey** — Kyungeun Lee et al. **[Short-term Traffic Prediction with Deep Neural Networks: A Survey](https://arxiv.org/abs/2009.00712)**. 2020 · arXiv；正式发表状态未核验.

  从输入表示、网络结构、应用与数据资源组织短期交通预测研究。

  [发表证据](https://arxiv.org/abs/2009.00712) · 代码：未核验到作者代码

  版本/使用说明： 当前列出已核验的 arXiv 版本；不据此断言没有正式发表版本。

- **AGCRN** — Lei Bai et al. **[Adaptive Graph Convolutional Recurrent Network for Traffic Forecasting](https://arxiv.org/abs/2007.02842)**. 2020 · NeurIPS.

  结合节点自适应参数学习和自适应图生成，刻画不同节点的预测模式。

  [发表证据](https://github.com/LeiBAI/AGCRN) · [代码](https://github.com/LeiBAI/AGCRN)（作者/项目仓库已核验）

- **MTGNN** — Zonghan Wu et al. **[Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks](https://arxiv.org/abs/2005.11650)**. 2020 · KDD.

  联合学习变量间有向图、mix-hop 传播与时间卷积；兼顾通用多变量序列与交通任务。

  [发表证据](https://github.com/nnzhan/MTGNN) · [代码](https://github.com/nnzhan/MTGNN)（作者/项目仓库已核验）

  版本/使用说明：通用多变量模型，因明确包含交通任务与图学习而收录主目录。

- **STSGCN** — Chao Song et al. **[Spatial-Temporal Synchronous Graph Convolutional Networks: A New Framework for Spatial-Temporal Network Data Forecasting](https://ojs.aaai.org/index.php/AAAI/article/view/5438)**. 2020 · AAAI.

  把相邻时间片的节点连成局部时空图，联合建模局部时空关系与异质性。

  [正式版本](https://ojs.aaai.org/index.php/AAAI/article/view/5438) · [发表证据](https://ojs.aaai.org/index.php/AAAI/article/download/5438/5294) · [代码](https://github.com/Davidham3/STSGCN)（作者/项目仓库已核验）

- **GMAN** — Chuanpan Zheng et al. **[GMAN: A Graph Multi-Attention Network for Traffic Prediction](https://arxiv.org/abs/1911.08415)**. 2020 · AAAI；arXiv 首发 2019.

  使用时空多重注意力及历史到未来的变换注意力，直接生成多步交通预测。

  [发表证据](https://github.com/zhengchuanpan/GMAN) · [代码](https://github.com/zhengchuanpan/GMAN)（作者/项目仓库已核验）

- **STTN** — Mingxing Xu et al. **[Spatial-Temporal Transformer Networks for Traffic Flow Forecasting](https://arxiv.org/abs/2001.02908)**. 2020 · arXiv；正式发表状态未核验.

  采用空间与时间 Transformer，建模动态有向空间关系及长程时间依赖。

  [发表证据](https://arxiv.org/abs/2001.02908) · 代码：未核验到作者代码

  版本/使用说明： 当前列出已核验的 arXiv 版本；不据此断言没有正式发表版本。

- **PhyDNet** — Vincent Le Guen et al. **[Disentangling Physical Dynamics from Unknown Factors for Unsupervised Video Prediction](https://arxiv.org/abs/2003.01460)**. 2020 · CVPR.

  将可解释的物理动态与未知残差因素分离，用于未来帧预测。

  [发表证据](https://github.com/vincent-leguen/PhyDNet) · [代码](https://github.com/vincent-leguen/PhyDNet)（作者/项目仓库已核验）

- **SEVIR** — Mark Veillette et al. **[SEVIR : A Storm Event Imagery Dataset for Deep Learning Applications in Radar and Satellite Meteorology](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html)**. 2020 · NeurIPS.

  提供时空对齐的雷达与卫星风暴事件影像，支撑降水预测及跨传感器任务。

  [正式版本](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html) · [发表证据](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html) · [代码](https://github.com/MIT-AI-Accelerator/neurips-2020-sevir)（作者/项目仓库已核验）

- **WeatherBench** — Stephan Rasp et al. **[WeatherBench: A Benchmark Data Set for Data‐Driven Weather Forecasting](https://arxiv.org/abs/2002.00469)**. 2020 · Journal of Advances in Modeling Earth Systems.

  建立数据驱动天气预测的数据、基线与统一指标入口。

  [正式版本](https://doi.org/10.1029/2020MS002203) · [发表证据](https://doi.org/10.1029/2020MS002203) · [代码](https://github.com/pangeo-data/WeatherBench)（作者/项目仓库已核验）


## 2019（8 篇）

- **DeepSTN** — Ziqian Lin et al. **[DeepSTN+: Context-Aware Spatial-Temporal Neural Network for Crowd Flow Prediction in Metropolis](https://ojs.aaai.org/index.php/AAAI/article/download/3892/3770)**. 2019 · AAAI.

  结合长距离空间依赖、区域功能与时间上下文，预测城市人群流入/流出量。

  [发表证据](https://github.com/vonfeng/DeepSTN) · [代码](https://github.com/vonfeng/DeepSTN)（作者/项目仓库已核验）

- **STG2Seq** — Lei Bai et al. **[STG2Seq: Spatial-temporal Graph to Sequence Model for Multi-step Passenger Demand Forecasting](https://arxiv.org/abs/1905.10069)**. 2019 · IJCAI.

  用长短期编码器、图卷积和注意力进行多步乘客需求预测。

  [发表证据](https://github.com/LeiBAI/STG2Seq) · [代码](https://github.com/LeiBAI/STG2Seq)（作者/项目仓库已核验）

- **STDN** — Huaxiu Yao et al. **[Revisiting Spatial-Temporal Similarity: A Deep Learning Framework for Traffic Prediction](https://arxiv.org/abs/1803.01254)**. 2019 · AAAI；arXiv 首发 2018.

  这篇论文提出 STDN，通过流门控机制学习动态空间相似性，并用周期偏移注意力处理非严格周期的时间动态。它直接回应了交通预测里“空间关系静态、时间规律严格周期化”的常见假设。

  [正式版本](https://doi.org/10.1609/aaai.v33i01.33015668) · [发表证据](https://api.crossref.org/works/10.1609/aaai.v33i01.33015668) · [代码](https://github.com/tangxianfeng/STDN)（作者/项目仓库已核验）

  版本/使用说明：arXiv 首发于 2018 年，正式 AAAI 版本为 2019 年；已检查作者仓库 main.py 与运行说明，未训练复现。

- **ST-MGCN** — Xu Geng et al. **[Spatiotemporal Multi-Graph Convolution Network for Ride-Hailing Demand Forecasting](https://doi.org/10.1609/aaai.v33i01.33013656)**. 2019 · AAAI.

  这篇论文提出 ST-MGCN，用多张图建模区域间非欧式相关性，并结合上下文门控循环网络建模时间依赖。它适用于网约车/出行需求的区域级预测，而不仅是相邻栅格或传感器的局部建模。

  [正式版本](https://doi.org/10.1609/aaai.v33i01.33013656) · [发表证据](https://api.crossref.org/works/10.1609/aaai.v33i01.33013656) · 代码：未核验到作者代码

  版本/使用说明：出版者登记的 Crossref 元数据与摘要已核对；出版者页面本次访问受限，未核验到作者代码。

- **ASTGCN** — Shengnan Guo et al. **[Attention Based Spatial-Temporal Graph Convolutional Networks for Traffic Flow Forecasting](https://ojs.aaai.org/index.php/AAAI/article/view/3881)**. 2019 · AAAI.

  通过时空注意力、图卷积与近期/日/周分支进行交通流预测。

  [正式版本](https://ojs.aaai.org/index.php/AAAI/article/view/3881) · [发表证据](https://ojs.aaai.org/index.php/AAAI/article/view/3881) · [代码](https://github.com/guoshnBJTU/ASTGCN-2019-pytorch)（作者/项目仓库已核验）

  版本/使用说明：关联的作者 PyTorch 仓库说明仅实现近期分支；不能默认等于完整三分支 ASTGCN。

- **Graph-WaveNet** — Zonghan Wu et al. **[Graph WaveNet for Deep Spatial-Temporal Graph Modeling](https://arxiv.org/abs/1906.00121)**. 2019 · IJCAI.

  通过节点嵌入学习自适应邻接关系，并用膨胀时间卷积建模历史序列。

  [发表证据](https://github.com/nnzhan/Graph-WaveNet) · [代码](https://github.com/nnzhan/Graph-WaveNet)（作者/项目仓库已核验）

- **ST-MetaNet** — Zheyi Pan et al. **[Urban Traffic Prediction from Spatio-Temporal Data Using Deep Meta Learning](https://doi.org/10.1145/3292500.3330884)**. 2019 · KDD.

  利用地理属性生成元图注意力和元循环网络的参数，刻画城市交通节点与连接的异质性。

  [正式版本](https://doi.org/10.1145/3292500.3330884) · [发表证据](https://api.crossref.org/works/10.1145/3292500.3330884) · [代码](https://github.com/panzheyi/ST-MetaNet)（作者/项目仓库已核验）

  版本/使用说明：元学习根据地理属性生成节点/边相关参数；不据此推断少样本跨城市适配。已检查 MXNet 作者实现的训练入口，未运行。

- **MIM** — Yunbo Wang et al. **[Memory In Memory: A Predictive Neural Network for Learning Higher-Order Non-Stationarity from Spatiotemporal Dynamics](https://arxiv.org/abs/1811.07490)**. 2019 · CVPR；arXiv 首发 2018.

  通过记忆模块处理时空序列中的高阶非平稳变化。

  [发表证据](https://github.com/Yunbo426/MIM) · [代码](https://github.com/Yunbo426/MIM)（作者/项目仓库已核验）


## 2018（4 篇）

- **DMVST-Net** — Huaxiu Yao et al. **[Deep Multi-View Spatial-Temporal Network for Taxi Demand Prediction](https://arxiv.org/abs/1802.08714)**. 2018 · AAAI.

  这篇论文提出 DMVST-Net，用时间视图、局部空间视图和语义视图联合建模出租车需求的时空相关性。它针对区域级需求预测中仅用 CNN 或 LSTM 难以同时刻画空间与时间依赖的问题。

  [正式版本](https://doi.org/10.1609/aaai.v32i1.11836) · [发表证据](https://api.crossref.org/works/10.1609/aaai.v32i1.11836) · [代码](https://github.com/huaxiuyao/DMVST-Net)（作者/项目仓库已核验）

  版本/使用说明：作者仓库明确仅提供模型部分，原始数据未公开；已读 model.py，不能视为完整复现包。

- **DCRNN** — Yaguang Li et al. **[Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting](https://arxiv.org/abs/1707.01926)**. 2018 · ICLR；arXiv 首发 2017.

  将有向图扩散卷积与循环编码器—解码器结合，是理解路网预测的重要起点。

  [发表证据](https://github.com/liyaguang/DCRNN) · [代码](https://github.com/liyaguang/DCRNN)（作者/项目仓库已核验）

- **STGCN** — Bing Yu et al. **[Spatio-Temporal Graph Convolutional Networks: A Deep Learning Framework for Traffic Forecasting](https://arxiv.org/abs/1709.04875)**. 2018 · IJCAI；arXiv 首发 2017.

  用图卷积与时间卷积构成全卷积时空预测网络。

  [发表证据](https://github.com/VeritasYin/STGCN_IJCAI-18) · [代码](https://github.com/VeritasYin/STGCN_IJCAI-18)（作者/项目仓库已核验）

- **PredRNNpp** — Yunbo Wang et al. **[PredRNN++: Towards A Resolution of the Deep-in-Time Dilemma in Spatiotemporal Predictive Learning](https://arxiv.org/abs/1804.06300)**. 2018 · ICML.

  以因果 LSTM 与梯度通路缓解深层递归预测中的优化困难。

  [发表证据](https://github.com/Yunbo426/predrnn-pp) · [代码](https://github.com/Yunbo426/predrnn-pp)（作者/项目仓库已核验）


## 2017（3 篇）

- **ST-ResNet** — Junbo Zhang et al. **[Deep Spatio-Temporal Residual Networks for Citywide Crowd Flows Prediction](https://arxiv.org/abs/1610.00081)**. 2017 · AAAI；arXiv 首发 2016.

  对城市网格流入/流出量，分别建模近期、周期、趋势并融合外部因素。

  [发表证据](https://arxiv.org/abs/1610.00081) · 代码：未核验到作者代码

- **PredRNN** — Yunbo Wang et al. **[PredRNN: Recurrent Neural Networks for Predictive Learning using Spatiotemporal LSTMs](https://papers.nips.cc/paper/6689-predrnn-recurrent-neural-networks-for-predictive-learning-using-spatiotemporal-lstms)**. 2017 · NeurIPS.

  使用时空 LSTM 及双重记忆状态建模未来帧，属于通用时空预测背景。

  [正式版本](https://papers.nips.cc/paper/6689-predrnn-recurrent-neural-networks-for-predictive-learning-using-spatiotemporal-lstms) · [发表证据](https://papers.nips.cc/paper/6689-predrnn-recurrent-neural-networks-for-predictive-learning-using-spatiotemporal-lstms) · [代码](https://github.com/thuml/predrnn-pytorch)（作者/项目仓库已核验）

- **TrajGRU** — Xingjian Shi et al. **[Deep Learning for Precipitation Nowcasting: A Benchmark and A New Model](https://arxiv.org/abs/1706.03458)**. 2017 · NeurIPS.

  在降水临近预报中学习位置相关的递归连接，并提供相应基准。

  [发表证据](https://arxiv.org/abs/1706.03458) · 代码：未核验到作者代码


## 2015（1 篇）

- **ConvLSTM** — Xingjian Shi et al. **[Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting](https://arxiv.org/abs/1506.04214)**. 2015 · NeurIPS.

  将卷积放入 LSTM 状态转换，为网格序列与降水临近预报提供基础架构。

  [正式版本](https://papers.nips.cc/paper_files/paper/2015/hash/07563a3fe3bbe7e3ba84431ad9d055af-Abstract.html) · [发表证据](https://papers.nips.cc/paper_files/paper/2015/hash/07563a3fe3bbe7e3ba84431ad9d055af-Abstract.html) · 代码：未核验到作者代码
