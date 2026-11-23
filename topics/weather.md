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

<a id="paper-fitzroy"></a>

- **FitzRoy** — Ozan Sener et al. **[Skillful and realistic precipitation forecasting with reinforced diffusion](https://arxiv.org/abs/2610.38775)**. 2026 · arXiv；正式发表状态未核验.

  以强化学习细化条件离散扩散模型，预测未来降水空间场。

  [发表证据](https://arxiv.org/abs/2610.38775) · 代码：未核验到作者代码

  版本/使用说明：完整模型使用 ERA5、MRMS 与 NBM 预报引导；须与不使用 NBM 的独立变体区分。未核验到作者代码，论文中的其他模型仓库链接不代表本方法代码。

<a id="paper-sonny-ens"></a>

- **Sonny-ENS** — Minjong Cheon **[Sonny-ENS: demystifying machine-learning ensemble weather forecasting](https://arxiv.org/abs/2611.01614)**. 2026 · arXiv；正式发表状态未核验.

  以 CRPS 训练多个天气网络，并通过 Monte Carlo dropout 构造集合预报。

  [发表证据](https://arxiv.org/abs/2611.01614) · 代码：未核验到作者代码

  版本/使用说明：论文称代码和权重将在发表时开放；本次未确认公开发布，不能将未来开放承诺视为已有可用实现。

<a id="paper-lcg-sfno"></a>

- **LCG-SFNO** — Yaojun Li et al. **[Low-Rank Clebsch--Gordan Coupling for Equivariant Spherical Forecasting](https://arxiv.org/abs/2611.03411)**. 2026 · arXiv；正式发表状态未核验.

  通过低秩 Clebsch–Gordan 耦合构造球面谱非线性交互，研究等变球面动力学与天气预测。

  [发表证据](https://arxiv.org/abs/2611.03411) · 代码：未核验到作者代码

  版本/使用说明：未核验到作者代码；论文报告的等变性和计算效率未经本目录独立数值复现。

<a id="paper-ai-ensemble-blend"></a>

- **AI-Ensemble-Blend** — Harris Sop Nkuiate et al. **[Value of Adding AI Weather Model Ensembles to a Multi-model Probabilistic Blend](https://arxiv.org/abs/2610.42130)**. 2026 · arXiv；正式发表状态未核验.

  研究将 AI 天气集合加入多模型概率融合，并分析校准、成员多样性与概率预报质量。

  [发表证据](https://arxiv.org/abs/2610.42130) · 代码：未核验到作者代码

  版本/使用说明：AI-Ensemble-Blend 是本目录索引简称。该工作组合已有预报，比较时需对齐组成模型与输入；未核验到作者代码。

<a id="paper-taiji"></a>

- **TaiJi** — Jiale Wang et al. **[TaiJi: State-Conditional Adaptive Combination of Machine-Learning and Physics-Based Global Weather Forecasts](https://arxiv.org/abs/2609.31972)**. 2026 · arXiv；正式发表状态未核验.

  由近期大气状态生成随网格位置和预测步长变化的组合权重与残差，融合机器学习及物理天气预报。

  [发表证据](https://arxiv.org/abs/2609.31972) · 代码：未核验到作者代码

  版本/使用说明：arXiv 首发 2026-09-25，v3 修订 2026-11-02；因窗口内修订首次补入本目录，不是本周首发。已核验主源元数据与摘要，HTML 不可用，未核验到作者代码。

<a id="paper-swaither-precip"></a>

- **SwAIther-Precip** — Dan Assouline et al. **[SwAIther-Precip: Lead-Time-Aware Bias Correction Enables Kilometer-Scale Downscaling of Global AI Precipitation Forecasts over Switzerland](https://arxiv.org/abs/2605.16163)**. 2026 · arXiv；正式发表状态未核验.

  先以预测步长条件化的 U-Net 校正粗网格降水偏差，再通过扩散超分辨率生成瑞士地区概率降水场。

  [发表证据](https://arxiv.org/abs/2605.16163) · [代码](https://github.com/danassou/swaither-precip)（作者/项目仓库已核验）

  版本/使用说明：首发 2026-05-15，v3 修订 2026-10-29；本次为修订触发的目录补录。已检查作者源码与训练说明；论文专用 AIFS 历史预测数据未公开，其他数据获取条件需单独核对，未训练复现。

<a id="paper-six-hourly-pqpf"></a>

- **Six-hourly-PQPF** — Thomas M Hamill **[Six-hourly Probabilistic Precipitation Forecasts Created From Hourly Probabilities](https://arxiv.org/abs/2611.03326)**. 2026 · arXiv；正式发表状态未核验.

  将逐小时概率预报通过轻量 GRU 和 MLP 聚合为六小时累积降水分布，处理连续时段间的相关性。

  [发表证据](https://arxiv.org/abs/2611.03326) · 代码：未核验到作者代码

  版本/使用说明：2026-11-02 首发；补录此前待核验候选。属于概率预报后处理，不是仅输入历史雷达观测的外推基线。

<a id="paper-prola"></a>

- **PROLA** — Minseo Yoon et al. **[PROLA: Principal-Orthogonal Low-rank Adaptation for Predictive Spatiotemporal Weather Downscaling](https://arxiv.org/abs/2611.11318)**. 2026 · NeurIPS 2026.

  将低秩更新预算分配到预训练权重的主方向及正交补空间，并用于同时预测未来和细化时空分辨率的天气降尺度。

  [发表证据](https://nips.cc/virtual/2026/poster/155892) · [代码](https://github.com/yms020615/PROLA)（作者/项目仓库已核验）

  版本/使用说明：NeurIPS 2026 官方海报页已确认录用；未确认正式论文集卷页。已检查适配器、训练入口和运行说明，未训练复现。

<a id="paper-rescene-esm"></a>

- **Rescene-ESM** — Minjong Cheon et al. **[Rescene-ESM: an Earth system model built around a frozen AI weather model](https://arxiv.org/abs/2611.11066)**. 2026 · arXiv；正式发表状态未核验.

  将冻结的 AI 大气网络与海洋、海冰、陆面、河流及碳能量过程耦合，研究长期地球系统模拟和情景预测。

  [发表证据](https://arxiv.org/abs/2611.11066) · 代码：未核验到作者代码

  版本/使用说明：论文正文称代码、拟合系数和运行记录将在发表时开放；尚未核验公开实现。长期气候情景与短期天气误差不是相同评价任务。

<a id="paper-ai-nwp-fp16"></a>

- **AI-NWP-FP16** — Stefan Siegert **[Half-precision inference of AI weather prediction models: negligible loss of skill at a fraction of the cost](https://arxiv.org/abs/2611.09573)**. 2026 · arXiv；正式发表状态未核验.

  比较多个 AI 天气模型的半精度推理，将神经网络计算与保持 FP32 的物理状态、归一化和反归一化区分。

  [发表证据](https://arxiv.org/abs/2611.09573) · [代码](https://github.com/sieste/ai-nwp-fp16)（作者/项目仓库已核验）

  版本/使用说明：目录 ID 为编辑简称。已检查精度转换源码、预测入口和复现实验说明；精度与节能结论受模型、硬件及评估日期限制，未独立运行验证。

<a id="paper-dayu-tc"></a>

- **DaYu-TC** — Runzepu Hou et al. **[DaYu-TC: a global-regional nested AI system for tropical cyclone forecasting](https://arxiv.org/abs/2611.15266)**. 2026 · arXiv；正式发表状态未核验.

  通过全球与区域嵌套模型及极端感知目标，将大尺度预报与局地演变结合以预测热带气旋。

  [发表证据](https://arxiv.org/abs/2611.15266) · [代码](https://github.com/hourzp/DaYu-TC)（作者推理入口已核验（模型为二进制，训练代码未公开））

  版本/使用说明：已核验论文关联和公开推理入口，但模型实现为编译二进制，训练代码未公开；作者注明全分辨率加速器验证仍待完成。本目录未下载权重或运行模型。

<a id="paper-satellite-swr-nowcasting"></a>

- **Satellite-SWR-Nowcasting** — Tianyu Xie et al. **[Direct Multispectral Satellite Nowcasting of Gridded Surface Solar Radiation](https://arxiv.org/abs/2611.12999)**. 2026 · arXiv；正式发表状态未核验.

  从向日葵九号多光谱历史影像和太阳几何信息，直接生成未来四小时的网格地表短波辐射预测。

  [发表证据](https://arxiv.org/abs/2611.12999) · 代码：未核验到作者代码

  版本/使用说明：目录 ID 为编辑简称；首发 2026-11-08，v2 修订 2026-11-11，只计一个条目。未核验到作者代码；外部观测输入需与历史辐射基线区分。

<a id="paper-correctcast"></a>

- **CorrectCast** — Henan Wang et al. **[CorrectCast: Selective Multimodal Context for Scale-Aware Residual Correction in Precipitation Nowcasting](https://arxiv.org/abs/2611.22178)**. 2026 · arXiv；正式发表状态未核验.

  冻结基础降水临近预报模型，结合历史降水估计与可降水量，分尺度修正已生成预报的残差。

  [发表证据](https://arxiv.org/abs/2611.22178) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-11-17 首发。

<a id="paper-foresay"></a>

- **ForeSay** — Xudong Ling et al. **[ForeSay: Tell the Future in Words, Branch the Details in Noise for Precipitation Nowcasting](https://arxiv.org/abs/2611.20815)**. 2026 · arXiv；正式发表状态未核验.

  从历史雷达图生成风暴演变的文字条件，让集合成员共享早期流采样步骤，后期再分支生成局地降水细节。

  [发表证据](https://arxiv.org/abs/2611.20815) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-11-16 首发。

<a id="paper-protocast"></a>

- **ProtoCast** — Zhixuan Li et al. **[Interpretable Prototype-Conditioned Adaptation for Weather Forecasting](https://arxiv.org/abs/2611.25848)**. 2026 · arXiv；正式发表状态未核验.

  按变量组和位置匹配天气演变原型，用稀疏加权的低秩算子修正局部特征，再融合变量组信息。

  [发表证据](https://arxiv.org/abs/2611.25848) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-11-19 首发。 [作者项目页](https://zhixuanli.github.io/projects/li2026protocast/)展示了预报样例，Code 按钮未启用。

<a id="paper-weathercraft"></a>

- **WeatherCraft** — Jinhan Li et al. **[Reinforcement-Aligned Probabilistic Weather Forecasting with Discrete Tokens](https://arxiv.org/abs/2611.25570)**. 2026 · arXiv；正式发表状态未核验.

  将大气状态编码为多尺度离散 token，用 Transformer 生成集合预报，并用 GRPO 按下游预报目标调整模型。

  [发表证据](https://arxiv.org/abs/2611.25570) · [代码](https://github.com/Jinhan-Li/WeatherCraft)（作者/项目仓库已核验）

  版本/使用说明：arXiv 2026-11-19 首发。

<a id="paper-weatherdreamer"></a>

- **WeatherDreamer** — Kate Duffy et al. **[WeatherDreamer: Learning a World Model from Multimodal Earth Observations](https://arxiv.org/abs/2611.18393)**. 2026 · arXiv；正式发表状态未核验.

  从 18 类地球观测学习潜在大气状态，每小时推进并用新观测更新，生成后续站点及仪器观测的集合预报。

  [发表证据](https://arxiv.org/abs/2611.18393) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-11-13 首发。

<a id="paper-xaurora"></a>

- **Xaurora** — Eliot Walt et al. **[Xaurora: Generative Weather Forecasting with Denoising Stochastic Interpolants from a Foundation Model Prior](https://arxiv.org/abs/2610.06509)**. 2026 · arXiv；正式发表状态未核验.

  从确定性的 Aurora 小模型出发，用去噪随机插值和轨迹回放训练随机动力学，生成中期天气集合预报。

  [发表证据](https://arxiv.org/abs/2610.06509) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-10-05 首发。 v2 于 2026-11-19 修订，本次补录。 与目录中 Aurora 的关系为下游概率扩展，另见[早期会议摘要](https://doi.org/10.5194/ems2026-650)。

<a id="paper-tyche"></a>

- **Tyche** — Fan Xu et al. **[Tyche: One Step Flow for Efficient Probabilistic Weather Forecasting](https://arxiv.org/abs/2605.06916)**. 2026 · arXiv；正式发表状态未核验.

  用单次条件流映射将噪声转换为未来天气场，并在自回归滚动阶段用 CRPS 校准集合。

  [发表证据](https://arxiv.org/abs/2605.06916) · [代码](https://github.com/Markus-xu/Tyche)（论文提供链接，本次返回 404）

  版本/使用说明：arXiv 2026-05-07 首发。 v2 于 2026-11-06 修订，本次补录。 [论文正文](https://arxiv.org/html/2605.06916v2)给出的仓库本次公开访问返回 404。

<a id="paper-uq-aardvark"></a>

- **UQ-Aardvark** — Rodrigo Almeida et al. **[Uncertainty-Aware End-to-End AI Weather Forecasting: Disentangling Observation and Model Contributions](https://arxiv.org/abs/2608.30795)**. 2026 · arXiv；正式发表状态未核验.

  在 Aardvark 的观测编码器引入输入相关噪声，在动力学模块使用 Monte Carlo dropout，通过嵌套集合估计两部分对预报离散度的贡献。

  [发表证据](https://arxiv.org/abs/2608.30795) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-08-31 首发。 v2 于 2026-11-09 修订，本次补录。 正文链接到数据和评估工具，模型实现尚待核验。
