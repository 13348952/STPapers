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
