# 近期论文（2025—2026）

[返回主目录](README.md)

年份依据与代码标记见主目录。以下复用同一结构化数据，不额外增加论文数。

## 2026（65 篇）

- **Vision-ST-Fusion-survey** — Anna Wang et al. **[Towards Vision-Spatiotemporal Fusion in Traffic Forecasting: A Survey on Cross-Modal Alignment](https://ijcai.org/proceedings/2026/891)**. 2026 · IJCAI 2026 (Survey Track).

  从特征、语义和任务级对齐组织视觉与交通时空信号融合方法，讨论跨视角与几何映射挑战。

  [正式版本](https://doi.org/10.24963/ijcai.2026/891) · [发表证据](https://ijcai.org/proceedings/2026/891) · 代码：未核验到作者代码

  版本/使用说明：范围同时涉及交通状态、轨迹、事件与需求；作为跨模态预测综述收录，不将轨迹规划方法列为核心预测基线。资源仓库未核验。

- **Extreme-Weather-Review** — Gabriele Messori et al. **[Comparing Data-Driven and Numerical Weather Prediction Forecasts of Extreme Weather: A Review](https://arxiv.org/abs/2611.23863)**. 2026 · arXiv；正式发表状态未核验.

  按事件类型、提前量和评价方法梳理数据驱动与数值天气预报的极端事件对比，分别讨论事件位置、强度和破纪录情形。

  [发表证据](https://arxiv.org/abs/2611.23863) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-11-18 首发。

- **CARE-EMS** — Md Ali Akber et al. **[CARE-EMS: Towards Reliable Emergency Response Planning through Context-Aware Spatio-Temporal Graph Learning for EMS Demand Forecasting](https://drive.google.com/file/d/19E6d63P6vV4yslVE4D8BE1xbGilNCAAI/view?usp=drivesdk)**. 2026 · ACM SIGSPATIAL 2026.

  将纽约各区逐时急救呼叫、社区属性和路网关系输入时空图模型，预测下一小时的呼叫需求。

  [发表证据](https://sigspatial2026.sigspatial.org/detailed-program.html) · [代码](https://github.com/samiikkk/CARE-EMS)（作者仓库可访问，已核验部分源码）

  版本/使用说明：会议官网议程与作者稿已核对。 仓库含按小时聚合数据和模型模块，README 提供仪表板入口，完整预测流程的运行说明待核验。

- **Actionable-Congestion** — Dizhi Huang et al. **[Congestion Forecasting (Actionably) Revisited: Limitations of Deep Learning and Potential of LLM-as-Data-Scientist](https://drive.google.com/file/d/1cr_PHTQxSpx20HtTE_nPAQyyUUJNR8KF/view?usp=drivesdk)**. 2026 · ACM SIGSPATIAL 2026.

  面向提前数周发布的假日拥堵预报，把历史事件表示为时空三角形，按日历选择相似年份，在日本两条高速公路上评估覆盖区域。

  [发表证据](https://sigspatial2026.sigspatial.org/detailed-program.html) · 代码：未核验到作者代码

  版本/使用说明：会议官网议程与作者稿已核对。

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

- **SIMBAD** — Daniel Y. Lee et al. **[SIMBAD: Spatio-Temporal Traffic Forecasting Robust to Aperiodicity](https://arxiv.org/abs/2611.09015)**. 2026 · NeurIPS 2026.

  利用历史周期与近期观测的相似性调节时间信息和节点间作用，增强非周期交通模式下的预测。

  [发表证据](https://nips.cc/virtual/2026/poster/150645) · [代码](https://github.com/theghks3/SIMBAD)（作者/项目仓库已核验）

  版本/使用说明：2026-11-06 首发。NeurIPS 2026 官方海报页已确认录用；未确认正式论文集卷页。代码核验沿用 2026-11-12 的源文件及运行说明检查，本次未重跑或复现。

- **UniST-Pred** — Yue Wang et al. **[UniST-Pred: A Robust Unified Framework for Spatio-Temporal Traffic Forecasting in Transportation Networks Under Disruptions](https://ijcai.org/proceedings/2026/834)**. 2026 · IJCAI 2026 (AI and Social Good).

  先解耦时间建模与空间表征，再自适应融合；在真实交通与 MATSim 网络中断场景中评估。

  [正式版本](https://doi.org/10.24963/ijcai.2026/834) · [发表证据](https://ijcai.org/proceedings/2026/834) · [代码](https://anonymous.4open.science/r/UniST-Pred-EF27)（论文提供匿名代码，访问未核验）

  版本/使用说明：与目录中的 UniST 为不同工作。论文提供匿名代码及数据链接，本次未核验匿名站点内容。

- **CANDOR** — Ziqi Wang et al. **[Decompose Dynamics Before Learning Dependencies in Spatiotemporal Systems](https://arxiv.org/abs/2609.36637)**. 2026 · arXiv；正式发表状态未核验.

  先将局部动态拆分为背景、积累释放和稀疏冲击，再融合延迟感知的有向传播与不受拓扑约束的依赖学习，用于交通和水质预测。

  [发表证据](https://arxiv.org/abs/2609.36637) · 代码：未核验到作者代码

  版本/使用说明：首发 2026-09-29，v2 修订 2026-11-07；属于修订触发的目录补录。分支命名不构成因果机制识别证据；未核验到作者代码。

- **DSGN-TMT** — Zuojun Wu et al. **[Dynamic spatiotemporal graph network with a temporal masked transformer for traffic flow forecasting](https://doi.org/10.1038/s41598-026-80267-w)**. 2026 · Scientific Reports.

  按周期时间索引学习空间与时间邻接矩阵，在历史时间片之间做图卷积，并由 Transformer 编码完整历史以预测交通流。

  [正式版本](https://doi.org/10.1038/s41598-026-80267-w) · [发表证据](https://www.nature.com/articles/s41598-026-80267-w_reference.pdf) · 代码：未核验到作者代码

  版本/使用说明：2026-11-09 在线发表。 11 月 5 日录用。论文报告的训练和推理均输入完整历史，训练目标为预测损失。

- **CA-DTNet** — Shishir Singh Chauhan et al. **[CA-DTNet: a trace-driven communication-aware digital twin network for robust high-resolution traffic forecasting under heterogeneous V2X conditions](https://doi.org/10.1038/s41598-026-76830-0)**. 2026 · Scientific Reports.

  将 pNEUMA 交通状态与通信记录按确定协议回放，用可靠性门控处理过时或缺失的观测，预测未来 5、10、30 秒的速度、车辆数和流量分位数。

  [正式版本](https://doi.org/10.1038/s41598-026-76830-0) · [发表证据](https://www.nature.com/articles/s41598-026-76830-0) · 代码：未核验到作者代码

  版本/使用说明：2026-11-11 在线发表。 实验将交通与通信记录配对回放。

- **ST-GT** — Da Wang et al. **[A spatio-temporal graph transformer for multi-horizon urban traffic speed forecasting](https://doi.org/10.1007/s44163-026-02649-3)**. 2026 · Discover Artificial Intelligence.

  在 METR-LA 上结合按距离聚合的传感器图与时间自注意力，一次输出未来十二个五分钟步长的交通速度。

  [正式版本](https://doi.org/10.1007/s44163-026-02649-3) · [发表证据](https://link.springer.com/article/10.1007/s44163-026-02649-3) · 代码：未核验到作者代码

  版本/使用说明：2026-11-07 在线发表。 作者说明实验使用单种子、固定图和轻量对照，并讨论插值可能造成的信息泄漏。

- **FAST-SSM** — Xinjin Li et al. **[FAST: A Synergistic Framework of Attention and State-space Models for Spatiotemporal Traffic Prediction](https://arxiv.org/abs/2604.13453)**. 2026 · ICME.

  结合时间注意力与 Mamba 空间模块；与 KDD 2026 的 FaST 是不同论文。

  [发表证据](https://arxiv.org/abs/2604.13453) · 代码：未核验到作者代码

- **SpecLST** — Kenan Kang et al. **[SpecLST: Spectral-Enhanced Long-Short Term Spatio-Temporal Multimodal Modeling for Traffic Forecasting](https://arxiv.org/abs/2610.36393)**. 2026 · arXiv；正式发表状态未核验.

  以频域长历史表示融合天气、事故等上下文，并采用稀疏 MoE；属于多模态设置。

  [发表证据](https://arxiv.org/abs/2610.36393) · 代码：未核验到作者代码

- **ASTPKEFormer** — Wenfeng Zhou et al. **[ASTPKEFormer: Adaptive Spatiotemporal Prior Knowledge Embedding-Induced Transformers for Traffic Data Forecasting](https://ijcai.org/proceedings/2026/368)**. 2026 · IJCAI 2026.

  结合多尺度时间通道对齐、时间与图结构先验嵌入及交叉融合，建模交通时空依赖。

  [正式版本](https://doi.org/10.24963/ijcai.2026/368) · [发表证据](https://ijcai.org/proceedings/2026/368) · 代码：未核验到作者代码

- **SSCA-LSTM** — Vishwanath Bidare Ranganath et al. **[A Spatial Skip-Connected Attention-based LSTM for urban traffic forecasting using air quality data](https://doi.org/10.1007/s10791-026-10812-8)**. 2026 · Discover Computing.

  将交通与空气质量观测输入带跳连和空间加权的层级 LSTM，直接预测多个提前量的车辆数。

  [正式版本](https://doi.org/10.1007/s10791-026-10812-8) · [发表证据](https://link.springer.com/article/10.1007/s10791-026-10812-8) · 代码：未核验到作者代码

  版本/使用说明：2026-11-21 在线发表。 论文指向 CityPulse 数据来源。

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

- **TAS-GNN** — JiaJun Yu et al. **[Active Arbitration: Decoupling Spatio-Temporal Duality for Efficient Traffic Forecasting](https://ijcai.org/proceedings/2026/583)**. 2026 · IJCAI 2026.

  以时间上下文调节空间交互，并结合离散小波分解，区分物理传播滞后与语义同步。

  [正式版本](https://doi.org/10.24963/ijcai.2026/583) · [发表证据](https://ijcai.org/proceedings/2026/583) · 代码：未核验到作者代码

  版本/使用说明：论文链接 https://github.com/highhhhh/TAS-GNN ，但所查提交仅有补充材料 PDF，不作为已开放模型代码。

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

- **EvoST** — Du Yin et al. **[EvoST: Adapting Traffic Forecasters to Evolving Sensor Graphs](https://arxiv.org/abs/2607.25875)**. 2026 · arXiv；正式发表状态未核验.

  保持共享预测权重冻结，用延迟到达的标签刷新节点身份、初始化新传感器并在线校准，以适应持续演化的交通传感器网络。

  [发表证据](https://arxiv.org/abs/2607.25875) · [代码](https://github.com/lixus7/EvoST)（作者/项目仓库已核验）

  版本/使用说明：首发 2026-07-28，v5 修订 2026-11-07；补录一个版本链。该设置使用后续监督反馈，不是无标签零样本迁移。已检查实现与命令；原始实验检查点未随仓库发布，未复现。

- **ATLAS** — Ryusei Iwasa et al. **[Latent Prediction-Anchored Multi-View Reconstruction for Cross-Network Spatiotemporal Forecasting](https://drive.google.com/file/d/1nLRm3JRLsAaLG4lI9mw0-hDfVli4nI4p/view?usp=drivesdk)**. 2026 · ACM SIGSPATIAL 2026.

  在源网络重建时间序列及两种频谱视图，以潜空间预测约束预训练；迁移时融合功能图与物理图，预测新网络的交通或人群分布。

  [发表证据](https://sigspatial2026.sigspatial.org/detailed-program.html) · [代码](https://github.com/ryu291/ATLAS)（论文提供链接，本次返回 404）

  版本/使用说明：会议官网议程与作者稿已核对。 作者稿给出的代码链接本次返回 404。

- **ICL-Traffic** — Parth Ripal Parikh et al. **[ICL-Traffic Forecasting: Lightweight In-Context Learning for Pretrained Spatio-Temporal Foundation Models](https://drive.google.com/file/d/1KT78sWRt6fYkSl5ClilOQt7fayfvxeUc/view?usp=drivesdk)**. 2026 · ACM SIGSPATIAL 2026.

  冻结交通预测主干，从训练窗口检索近邻样本，以离线训练的注意力模块聚合近邻预测误差，修正目标城市的输出。

  [发表证据](https://sigspatial2026.sigspatial.org/detailed-program.html) · [代码](https://github.com/Parth291102/Traffic-Forecasting-TSFM)（作者/项目仓库已核验）

  版本/使用说明：会议官网议程与作者稿已核对。

- **FactoST-v2** — Siru Zhong et al. **[Learning to Factorize and Adapt: A Versatile Approach Toward Universal Spatio-Temporal Foundation Models](https://arxiv.org/abs/2601.12083)**. 2026 · arXiv；正式发表状态未核验.

  分离通用时间预训练与领域空间适配，扩展至可变长度和概率分位数预测。

  [发表证据](https://arxiv.org/abs/2601.12083) · [代码](https://github.com/CityMind-Lab/FactoST)（论文提供链接，本次返回 404）

  版本/使用说明：2026 扩展稿，不等同于其 NeurIPS 2025 会议版本；论文给出的仓库本次返回 404。

- **E2Forecast** — Jingtao Li et al. **[Forecasting Earth Surface Change in Embedding Space](https://arxiv.org/abs/2611.02211)**. 2026 · arXiv；正式发表状态未核验.

  从不规则卫星观测序列预测未来地表嵌入，结合高斯分支与整流流分支，并接受未来查询日期。

  [发表证据](https://arxiv.org/abs/2611.02211) · [代码](https://github.com/ucam-eo/e2forecast)（作者/项目仓库已核验）

  版本/使用说明：预测目标是地表嵌入，不是原始像素。作者仓库含模型、训练和评估说明；部分 GSA 嵌入与带日期 SSL4EO 数据仍待发布，未训练复现。

- **TopoST** — Kaiyun Wei et al. **[TopoST: Topology-Conditioned Node Specialization for Urban Spatio-Temporal Foundation Models](https://arxiv.org/abs/2611.15440)**. 2026 · arXiv；正式发表状态未核验.

  通过共享的拓扑到参数映射生成节点特定的时空参数，研究跨城市和跨任务的零样本预测。

  [发表证据](https://arxiv.org/abs/2611.15440) · [代码](https://github.com/weikaiyun/TopoST)（作者/项目仓库已核验）

  版本/使用说明：已检查拓扑编码、参数生成源码与训练说明；零样本与数据隔离结论仍需按源/目标划分独立复核，未训练复现。

- **Multi-STG** — Zhu Xiao et al. **[Beyond Sunny Skies: Using Large Language Models to Predict Urban Traffic in Adverse Weather](https://arxiv.org/abs/2611.12635)**. 2026 · arXiv；正式发表状态未核验.

  将天气、POI 和节假日描述转换为语言模型语义先验，通过多模态注意力与门控残差校准辅助恶劣天气下的城市交通预测。

  [发表证据](https://arxiv.org/abs/2611.12635) · 代码：未核验到作者代码

  版本/使用说明：未核验到作者代码。外部上下文和私家车数据设置需与基线对齐；语义表征不等于已识别天气对交通的因果机制。

- **SceneAdapter** — Han Fu et al. **[SceneAdapter: Boosting Time Series Foundation Models for Atypical-Scenario Traffic Flow Forecasting](https://drive.google.com/file/d/1FgPjiEYpwuluwosaF36xHqi78DOEMMJq/view?usp=drivesdk)**. 2026 · ACM SIGSPATIAL 2026.

  冻结时序基础模型，分别编码静态属性、历史协变量和未来已知事件，在节假日、活动及封路场景下修正交通流预测。

  [发表证据](https://sigspatial2026.sigspatial.org/detailed-program.html) · 代码：未核验到作者代码

  版本/使用说明：会议官网议程与作者稿已核对。

- **CoReFlow** — Pengnan Chi et al. **[CoReFlow: Consistency-Relaxed Flow Maps for Probabilistic Traffic Forecasting](https://arxiv.org/abs/2611.05715)**. 2026 · arXiv；正式发表状态未核验.

  通过一致性松弛的流映射学习概率交通预测，以端点训练和条件均值约束支持单步生成。

  [发表证据](https://arxiv.org/abs/2611.05715) · 代码：未核验到作者代码

  版本/使用说明：论文称代码位于补充材料；本次未取得并核验该材料中的实现，未确认公开作者仓库。勿与同名的低秩矩阵生成工作混淆。

- **Double-Diffusion** — Hanlin Dong et al. **[Double-Diffusion: Balancing Speed, Accuracy, and Uncertainty in Probabilistic Forecasting for Urban Sensor Networks](https://arxiv.org/abs/2506.23053)**. 2026 · ACM SIGSPATIAL 2026；arXiv 首发 2025.

  以传感器图的热扩散产生低通先验，再由截短的去噪扩散链采样交通与空气质量的未来分布。

  [发表证据](https://sigspatial2026.sigspatial.org/detailed-program.html) · [代码](https://github.com/cruiseresearchgroup/Double-Diffusion)（作者/项目仓库已核验）

  版本/使用说明：会议官网议程与作者稿已核对。 arXiv 首发 2025-06-29。

- **DSSD** — Woojun Lee et al. **[Dynamical State-Space Diffusion for Spatiotemporal Prediction](https://arxiv.org/abs/2611.06652)**. 2026 · arXiv；正式发表状态未核验.

  用稳定状态空间模型构建时间相关的扩散噪声，并通过平稳协方差的 Cholesky 因子组织未来帧预测。

  [发表证据](https://arxiv.org/abs/2611.06652) · 代码：未核验到作者代码

  版本/使用说明：科学空间场与视频预测的通用方法背景；所学时间算子描述噪声相关性，不据此认定物理因果动力学。未核验到作者代码。

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

- **Six-hourly-PQPF** — Thomas M Hamill **[Six-hourly Probabilistic Precipitation Forecasts Created From Hourly Probabilities](https://arxiv.org/abs/2611.03326)**. 2026 · arXiv；正式发表状态未核验.

  将逐小时概率预报通过轻量 GRU 和 MLP 聚合为六小时累积降水分布，处理连续时段间的相关性。

  [发表证据](https://arxiv.org/abs/2611.03326) · 代码：未核验到作者代码

  版本/使用说明：2026-11-02 首发；补录此前待核验候选。属于概率预报后处理，不是仅输入历史雷达观测的外推基线。

- **PROLA** — Minseo Yoon et al. **[PROLA: Principal-Orthogonal Low-rank Adaptation for Predictive Spatiotemporal Weather Downscaling](https://arxiv.org/abs/2611.11318)**. 2026 · NeurIPS 2026.

  将低秩更新预算分配到预训练权重的主方向及正交补空间，并用于同时预测未来和细化时空分辨率的天气降尺度。

  [发表证据](https://nips.cc/virtual/2026/poster/155892) · [代码](https://github.com/yms020615/PROLA)（作者/项目仓库已核验）

  版本/使用说明：NeurIPS 2026 官方海报页已确认录用；未确认正式论文集卷页。已检查适配器、训练入口和运行说明，未训练复现。

- **Rescene-ESM** — Minjong Cheon et al. **[Rescene-ESM: an Earth system model built around a frozen AI weather model](https://arxiv.org/abs/2611.11066)**. 2026 · arXiv；正式发表状态未核验.

  将冻结的 AI 大气网络与海洋、海冰、陆面、河流及碳能量过程耦合，研究长期地球系统模拟和情景预测。

  [发表证据](https://arxiv.org/abs/2611.11066) · 代码：未核验到作者代码

  版本/使用说明：论文正文称代码、拟合系数和运行记录将在发表时开放；尚未核验公开实现。长期气候情景与短期天气误差不是相同评价任务。

- **AI-NWP-FP16** — Stefan Siegert **[Half-precision inference of AI weather prediction models: negligible loss of skill at a fraction of the cost](https://arxiv.org/abs/2611.09573)**. 2026 · arXiv；正式发表状态未核验.

  比较多个 AI 天气模型的半精度推理，将神经网络计算与保持 FP32 的物理状态、归一化和反归一化区分。

  [发表证据](https://arxiv.org/abs/2611.09573) · [代码](https://github.com/sieste/ai-nwp-fp16)（作者/项目仓库已核验）

  版本/使用说明：目录 ID 为编辑简称。已检查精度转换源码、预测入口和复现实验说明；精度与节能结论受模型、硬件及评估日期限制，未独立运行验证。

- **DaYu-TC** — Runzepu Hou et al. **[DaYu-TC: a global-regional nested AI system for tropical cyclone forecasting](https://arxiv.org/abs/2611.15266)**. 2026 · arXiv；正式发表状态未核验.

  通过全球与区域嵌套模型及极端感知目标，将大尺度预报与局地演变结合以预测热带气旋。

  [发表证据](https://arxiv.org/abs/2611.15266) · [代码](https://github.com/hourzp/DaYu-TC)（作者推理入口已核验（模型为二进制，训练代码未公开））

  版本/使用说明：已核验论文关联和公开推理入口，但模型实现为编译二进制，训练代码未公开；作者注明全分辨率加速器验证仍待完成。本目录未下载权重或运行模型。

- **Satellite-SWR-Nowcasting** — Tianyu Xie et al. **[Direct Multispectral Satellite Nowcasting of Gridded Surface Solar Radiation](https://arxiv.org/abs/2611.12999)**. 2026 · arXiv；正式发表状态未核验.

  从向日葵九号多光谱历史影像和太阳几何信息，直接生成未来四小时的网格地表短波辐射预测。

  [发表证据](https://arxiv.org/abs/2611.12999) · 代码：未核验到作者代码

  版本/使用说明：目录 ID 为编辑简称；首发 2026-11-08，v2 修订 2026-11-11，只计一个条目。未核验到作者代码；外部观测输入需与历史辐射基线区分。

- **CorrectCast** — Henan Wang et al. **[CorrectCast: Selective Multimodal Context for Scale-Aware Residual Correction in Precipitation Nowcasting](https://arxiv.org/abs/2611.22178)**. 2026 · arXiv；正式发表状态未核验.

  冻结基础降水临近预报模型，结合历史降水估计与可降水量，分尺度修正已生成预报的残差。

  [发表证据](https://arxiv.org/abs/2611.22178) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-11-17 首发。

- **ForeSay** — Xudong Ling et al. **[ForeSay: Tell the Future in Words, Branch the Details in Noise for Precipitation Nowcasting](https://arxiv.org/abs/2611.20815)**. 2026 · arXiv；正式发表状态未核验.

  从历史雷达图生成风暴演变的文字条件，让集合成员共享早期流采样步骤，后期再分支生成局地降水细节。

  [发表证据](https://arxiv.org/abs/2611.20815) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-11-16 首发。

- **ProtoCast** — Zhixuan Li et al. **[Interpretable Prototype-Conditioned Adaptation for Weather Forecasting](https://arxiv.org/abs/2611.25848)**. 2026 · arXiv；正式发表状态未核验.

  按变量组和位置匹配天气演变原型，用稀疏加权的低秩算子修正局部特征，再融合变量组信息。

  [发表证据](https://arxiv.org/abs/2611.25848) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-11-19 首发。 [作者项目页](https://zhixuanli.github.io/projects/li2026protocast/)展示了预报样例，Code 按钮未启用。

- **WeatherCraft** — Jinhan Li et al. **[Reinforcement-Aligned Probabilistic Weather Forecasting with Discrete Tokens](https://arxiv.org/abs/2611.25570)**. 2026 · arXiv；正式发表状态未核验.

  将大气状态编码为多尺度离散 token，用 Transformer 生成集合预报，并用 GRPO 按下游预报目标调整模型。

  [发表证据](https://arxiv.org/abs/2611.25570) · [代码](https://github.com/Jinhan-Li/WeatherCraft)（作者/项目仓库已核验）

  版本/使用说明：arXiv 2026-11-19 首发。

- **WeatherDreamer** — Kate Duffy et al. **[WeatherDreamer: Learning a World Model from Multimodal Earth Observations](https://arxiv.org/abs/2611.18393)**. 2026 · arXiv；正式发表状态未核验.

  从 18 类地球观测学习潜在大气状态，每小时推进并用新观测更新，生成后续站点及仪器观测的集合预报。

  [发表证据](https://arxiv.org/abs/2611.18393) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-11-13 首发。

- **Xaurora** — Eliot Walt et al. **[Xaurora: Generative Weather Forecasting with Denoising Stochastic Interpolants from a Foundation Model Prior](https://arxiv.org/abs/2610.06509)**. 2026 · arXiv；正式发表状态未核验.

  从确定性的 Aurora 小模型出发，用去噪随机插值和轨迹回放训练随机动力学，生成中期天气集合预报。

  [发表证据](https://arxiv.org/abs/2610.06509) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-10-05 首发。 v2 于 2026-11-19 修订，本次补录。 与目录中 Aurora 的关系为下游概率扩展，另见[早期会议摘要](https://doi.org/10.5194/ems2026-650)。

- **Tyche** — Fan Xu et al. **[Tyche: One Step Flow for Efficient Probabilistic Weather Forecasting](https://arxiv.org/abs/2605.06916)**. 2026 · arXiv；正式发表状态未核验.

  用单次条件流映射将噪声转换为未来天气场，并在自回归滚动阶段用 CRPS 校准集合。

  [发表证据](https://arxiv.org/abs/2605.06916) · [代码](https://github.com/Markus-xu/Tyche)（论文提供链接，本次返回 404）

  版本/使用说明：arXiv 2026-05-07 首发。 v2 于 2026-11-06 修订，本次补录。 [论文正文](https://arxiv.org/html/2605.06916v2)给出的仓库本次公开访问返回 404。

- **UQ-Aardvark** — Rodrigo Almeida et al. **[Uncertainty-Aware End-to-End AI Weather Forecasting: Disentangling Observation and Model Contributions](https://arxiv.org/abs/2608.30795)**. 2026 · arXiv；正式发表状态未核验.

  在 Aardvark 的观测编码器引入输入相关噪声，在动力学模块使用 Monte Carlo dropout，通过嵌套集合估计两部分对预报离散度的贡献。

  [发表证据](https://arxiv.org/abs/2608.30795) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-08-31 首发。 v2 于 2026-11-09 修订，本次补录。 正文链接到数据和评估工具，模型实现尚待核验。

- **EvoXXLTraffic** — Du Yin et al. **[From XXLTraffic to EvoXXLTraffic: Scaling Traffic Forecasting to Sensor-Evolving Networks](https://arxiv.org/abs/2605.29768)**. 2026 · arXiv；正式发表状态未核验.

  提供逐年变化的传感器目录、持续站点标识和交通矩阵，区分全传感器预测与新节点的监督适配。

  [发表证据](https://arxiv.org/abs/2605.29768) · [代码](https://github.com/cruiseresearchgroup/TSAS26-EvoXXLTraffic)（作者/项目仓库已核验）

  版本/使用说明：首发 2026-05-28，v3 修订 2026-11-12；为 XXLTraffic 家族扩展基准，非新预测模型。采用回溯地理图和特定实现适配；新节点接受当年训练，不属于零样本。已检查源码与运行说明，未下载数据或复现。

- **Conformal-WX** — Mariya **[Distribution-Free Uncertainty Quantification for Weather Forecasting: Conformal Prediction Under Spatiotemporal Dependence](https://arxiv.org/abs/2611.24329)**. 2026 · arXiv；正式发表状态未核验.

  在 ERA5 网格气温预测上比较八种区间估计程序，同时衡量逐格覆盖率、每日空间覆盖波动和连续漏报。

  [发表证据](https://arxiv.org/abs/2611.24329) · [代码](https://github.com/Mariyaaleem/conformal-wx)（作者/项目仓库已核验）

  版本/使用说明：arXiv 2026-11-18 首发。 逐格边际覆盖与同一天各格点联合覆盖分别评估。研究范围为一种变量、两种预报器。

- **SeasonRainBench** — Qiuyan Sun et al. **[SeasonRainBench: Global Seasonal Precipitation](https://arxiv.org/abs/2611.22281)**. 2026 · arXiv；正式发表状态未核验.

  用全球逐月降水、气候模拟和业务集合预报构建提前 1 至 5 个月的预测基准，并评估异常强度和雨带位置。

  [发表证据](https://arxiv.org/abs/2611.22281) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-11-17 首发。

- **OTTER-NYC** — Seongwon Jin et al. **[OTTER-NYC: A Minute-Scale Multimodal Dataset for Urban Flood Event Dynamics and Forecasting](https://doi.org/10.1038/s41597-026-08642-w)**. 2026 · Scientific Data.

  将纽约积水传感器的分钟级深度与降水、地形和排水设施对齐，支持站点积水预测及事件质量控制。

  [正式版本](https://doi.org/10.1038/s41597-026-08642-w) · [发表证据](https://www.nature.com/articles/s41597-026-08642-w_reference.pdf) · [代码](https://github.com/jinwork00/OTTER-NYC)（作者/项目仓库已核验）

  版本/使用说明：2026-11-17 在线发表。 已核验作者公开的数据处理与质控流水线，预测训练实现需另行核验。

- **Traffic-IMC** — Seungbin Yim et al. **[Traffic-IMC: An Urban Road-Network Traffic Forecasting Benchmark](https://drive.google.com/file/d/1O5jDSMjIpcYjVg7dfM3LMj0ABRkyP2V5/view?usp=drivesdk)**. 2026 · ACM SIGSPATIAL 2026.

  仁川 2,013 个路段传感器的逐时流量基准同时提供有向可达图、原始有效性掩码和插补输入。评分排除原本无效的目标。

  [发表证据](https://sigspatial2026.sigspatial.org/detailed-program.html) · [代码](https://github.com/ysb06/traffic-imc)（作者/项目仓库已核验）

  版本/使用说明：会议官网议程与作者稿已核对。

- **HeatCast** — Jesus Guerrero et al. **[HeatCast: A Benchmark for Neighborhood-Scale LST Forecasting across 124 U.S. Cities](https://arxiv.org/abs/2608.07640)**. 2026 · ACM SIGSPATIAL 2026.

  用 124 个美国城市的 Landsat 月度影像进行 30 米地表温度的次月预测，按固定时间切分并按局地气候区评价。

  [发表证据](https://sigspatial2026.sigspatial.org/detailed-program.html) · 代码：未核验到作者代码

  版本/使用说明：会议官网议程与作者稿已核对。 arXiv 首发 2026-08-07。 作者链接的数据集可访问，尚未独立核验训练实现。


## 2025（10 篇）

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

- **SpecSTG** — Lequan Lin et al. **[SpecSTG: A Fast Spectral Diffusion Framework for Probabilistic Spatio-Temporal Traffic Forecasting](https://arxiv.org/abs/2401.08119)**. 2025 · ICLR 2025 DeLTa Workshop；arXiv 首发 2024.

  在频谱域生成未来序列，并结合空间依赖与频谱图卷积。

  [正式版本](https://openreview.net/pdf/8bc5f3850ffa6d0159499622645a1bc63f21165c.pdf) · [发表证据](https://openreview.net/pdf/8bc5f3850ffa6d0159499622645a1bc63f21165c.pdf) · [代码](https://github.com/lequanlin/SpecSTG)（作者/项目仓库已核验）

  版本/使用说明：2024 年 arXiv 首发，2025 年作为 ICLR DeLTa 工作坊论文发表。工作坊稿直接链接作者仓库，已检查模型、训练入口和 README。

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
