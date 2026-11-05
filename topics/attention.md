# 注意力、Transformer 与状态空间模型

[简体中文](attention.md) | [English](attention.en.md) · [主题导航 / Topics](README.md) · [返回主目录](../README.md)

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

<a id="paper-stg-mamba"></a>

- **STG-Mamba** — Lincan Li et al. **[STG-Mamba: Spatial-Temporal Graph Learning via Selective State Space Model](https://arxiv.org/abs/2403.12418)**. 2024 · arXiv；正式发表状态未核验.

  本文提出 STG-Mamba，将选择性状态空间模型引入时空图学习，用 ST-S3M 建模跨时间的动态状态演化，并结合 KFGN 做多时间粒度的图表示融合。

  [发表证据](https://arxiv.org/abs/2403.12418) · [代码](https://github.com/LincanLi-X/STG-Mamba)（作者/项目仓库已核验）

  版本/使用说明：保留 arXiv 2024 记录，正式发表状态未核验。论文链接的旧仓库地址重定向至 LincanLi-X；已检查 main.py，未训练复现。

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
