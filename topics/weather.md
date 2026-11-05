# 降水、天气与地球系统预测

[简体中文](weather.md) | [English](weather.en.md) · [主题导航 / Topics](README.md) · [返回主目录](../README.md)

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
