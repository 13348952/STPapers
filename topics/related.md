# 相关任务与时间序列背景

[简体中文](related.md) | [English](related.en.md) · [主题导航 / Topics](README.md) · [返回主目录](../README.md)

<a id="topic-related"></a>

## 13 · 相关任务与时间序列背景

时间序列基线、插补和空间外推等相关任务；明确区分任务与物理空间假设。

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

<a id="paper-stgnp"></a>

- **STGNP** — Junfeng Hu et al. **[Graph Neural Processes for Spatio-Temporal Extrapolation](https://arxiv.org/abs/2305.18719)**. 2023 · KDD.

  这项工作把 Neural Processes 扩展到图上的时空外推任务，显式建模不确定性，并通过 Graph Bayesian Aggregation 融合上下文节点信息。

  [正式版本](https://doi.org/10.1145/3580305.3599372) · [发表证据](https://api.crossref.org/works/10.1145/3580305.3599372) · [代码](https://github.com/hjf1997/STGNP)（作者/项目仓库已核验）

  版本/使用说明：相关任务：依据周围观测推断目标位置，不能等同于未来时间预测。已检查作者仓库层级模型实现和运行说明，未运行实验。

<a id="paper-graphdf"></a>

- **GraphDF** — Hongjie Chen et al. **[Graph Deep Factors for Probabilistic Time-series Forecasting](https://arxiv.org/abs/2010.07373)**. 2023 · ACM TKDD；arXiv 首发 2020.

  结合图关系驱动的全局与局部概率模型，描述相关时间序列；正式期刊版本还研究在线增量学习。

  [正式版本](https://doi.org/10.1145/3543511) · [发表证据](https://api.crossref.org/works/10.1145/3543511) · 代码：未核验到作者代码

  版本/使用说明：相关背景：图相关的概率时间序列预测，不预设地理空间。2023 年 TKDD 正式版本扩展了 2020 年预印本并加入在线增量学习；以一个条目记录版本关系，未核验作者代码。

<a id="paper-csdi"></a>

- **CSDI** — Yusuke Tashiro et al. **[CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation](https://arxiv.org/abs/2107.03502)**. 2021 · NeurIPS.

  主要研究条件扩散时间序列插补，可作缺失数据背景；不作为直接时空预测模型。

  [发表证据](https://github.com/ermongroup/CSDI) · [代码](https://github.com/ermongroup/CSDI)（作者/项目仓库已核验）

  版本/使用说明：主任务为插补；不计入直接时空预测方法。

<a id="paper-timegrad"></a>

- **TimeGrad** — Kashif Rasul et al. **[Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting](https://arxiv.org/abs/2101.12072)**. 2021 · ICML.

  用自回归去噪扩散进行多变量概率预测；用于概率建模对照。

  [发表证据](https://arxiv.org/abs/2101.12072) · 代码：未核验到作者代码
