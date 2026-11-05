# 概率时空图预测

[简体中文](probabilistic.md) | [English](probabilistic.en.md) · [主题导航 / Topics](README.md) · [返回主目录](../README.md)

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

<a id="paper-stgp-spde"></a>

- **STGP-SPDE** — Alexander V. Nikitin et al. **[Non-separable Spatio-temporal Graph Kernels via SPDEs](https://arxiv.org/abs/2111.08524)**. 2022 · AISTATS；arXiv 首发 2021.

  本文利用 SPDE 与图上的高斯过程联系，推导出非可分的时空图核，用于描述扩散、振荡等跨时空耦合现象。

  [正式版本](https://proceedings.mlr.press/v151/nikitin22a.html) · [发表证据](https://proceedings.mlr.press/v151/nikitin22a.html) · [代码](https://github.com/AaltoPML/spatiotemporal-graph-kernels)（作者/项目仓库已核验）

  版本/使用说明：正式版本为 AISTATS 2022，arXiv 首发 2021。仓库同时包含插值和外推设置，比较时需区分；已检查时空核实现，未运行实验。
