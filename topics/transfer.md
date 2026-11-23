# 异质性、元学习与迁移

[简体中文](transfer.md) | [English](transfer.en.md) · [主题导航 / Topics](README.md) · [返回主目录](../README.md)

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

<a id="paper-st-metanet"></a>

- **ST-MetaNet** — Zheyi Pan et al. **[Urban Traffic Prediction from Spatio-Temporal Data Using Deep Meta Learning](https://doi.org/10.1145/3292500.3330884)**. 2019 · KDD.

  利用地理属性生成元图注意力和元循环网络的参数，刻画城市交通节点与连接的异质性。

  [正式版本](https://doi.org/10.1145/3292500.3330884) · [发表证据](https://api.crossref.org/works/10.1145/3292500.3330884) · [代码](https://github.com/panzheyi/ST-MetaNet)（作者/项目仓库已核验）

  版本/使用说明：元学习根据地理属性生成节点/边相关参数；不据此推断少样本跨城市适配。已检查 MXNet 作者实现的训练入口，未运行。

<a id="paper-omnist"></a>

- **OmniST** — Praveg Vashishtha **[OmniST: Topology-Invariant Spatiotemporal Forecasting with Guaranteed-Coverage Uncertainty at Unseen Sensor Locations](https://arxiv.org/abs/2611.04256)**. 2026 · arXiv；正式发表状态未核验.

  以坐标编码、动态近邻注意力和逐节点循环网络处理变化的传感器集合，并结合共形校准预测未见位置及其不确定性。

  [发表证据](https://arxiv.org/abs/2611.04256) · [代码](https://github.com/Praveg432/OmniST)（作者/项目仓库已核验）

  版本/使用说明：覆盖保证依赖校准与测试分数的交换性；局部拓扑不变性有近邻集合不变等条件。已检查模型源码和运行入口，未训练复现。

<a id="paper-evost"></a>

- **EvoST** — Du Yin et al. **[EvoST: Adapting Traffic Forecasters to Evolving Sensor Graphs](https://arxiv.org/abs/2607.25875)**. 2026 · arXiv；正式发表状态未核验.

  保持共享预测权重冻结，用延迟到达的标签刷新节点身份、初始化新传感器并在线校准，以适应持续演化的交通传感器网络。

  [发表证据](https://arxiv.org/abs/2607.25875) · [代码](https://github.com/lixus7/EvoST)（作者/项目仓库已核验）

  版本/使用说明：首发 2026-07-28，v5 修订 2026-11-07；补录一个版本链。该设置使用后续监督反馈，不是无标签零样本迁移。已检查实现与命令；原始实验检查点未随仓库发布，未复现。

<a id="paper-atlas"></a>

- **ATLAS** — Ryusei Iwasa et al. **[Latent Prediction-Anchored Multi-View Reconstruction for Cross-Network Spatiotemporal Forecasting](https://drive.google.com/file/d/1nLRm3JRLsAaLG4lI9mw0-hDfVli4nI4p/view?usp=drivesdk)**. 2026 · ACM SIGSPATIAL 2026.

  在源网络重建时间序列及两种频谱视图，以潜空间预测约束预训练；迁移时融合功能图与物理图，预测新网络的交通或人群分布。

  [发表证据](https://sigspatial2026.sigspatial.org/detailed-program.html) · [代码](https://github.com/ryu291/ATLAS)（论文提供链接，本次返回 404）

  版本/使用说明：会议官网议程与作者稿已核对。 作者稿给出的代码链接本次返回 404。

<a id="paper-icl-traffic"></a>

- **ICL-Traffic** — Parth Ripal Parikh et al. **[ICL-Traffic Forecasting: Lightweight In-Context Learning for Pretrained Spatio-Temporal Foundation Models](https://drive.google.com/file/d/1KT78sWRt6fYkSl5ClilOQt7fayfvxeUc/view?usp=drivesdk)**. 2026 · ACM SIGSPATIAL 2026.

  冻结交通预测主干，从训练窗口检索近邻样本，以离线训练的注意力模块聚合近邻预测误差，修正目标城市的输出。

  [发表证据](https://sigspatial2026.sigspatial.org/detailed-program.html) · [代码](https://github.com/Parth291102/Traffic-Forecasting-TSFM)（作者/项目仓库已核验）

  版本/使用说明：会议官网议程与作者稿已核对。
