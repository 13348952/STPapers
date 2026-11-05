# 自监督与预训练

[简体中文](pretrain.md) | [English](pretrain.en.md) · [主题导航 / Topics](README.md) · [返回主目录](../README.md)

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
