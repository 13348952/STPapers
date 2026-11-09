# 基础模型、语言模型与跨模态迁移

[简体中文](foundation.md) | [English](foundation.en.md) · [主题导航 / Topics](README.md) · [返回主目录](../README.md)

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

<a id="paper-e2forecast"></a>

- **E2Forecast** — Jingtao Li et al. **[Forecasting Earth Surface Change in Embedding Space](https://arxiv.org/abs/2611.02211)**. 2026 · arXiv；正式发表状态未核验.

  从不规则卫星观测序列预测未来地表嵌入，结合高斯分支与整流流分支，并接受未来查询日期。

  [发表证据](https://arxiv.org/abs/2611.02211) · [代码](https://github.com/ucam-eo/e2forecast)（作者/项目仓库已核验）

  版本/使用说明：预测目标是地表嵌入，不是原始像素。作者仓库含模型、训练和评估说明；部分 GSA 嵌入与带日期 SSL4EO 数据仍待发布，未训练复现。
