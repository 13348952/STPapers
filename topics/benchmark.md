# 数据集、基准与工具

[简体中文](benchmark.md) | [English](benchmark.en.md) · [主题导航 / Topics](README.md) · [返回主目录](../README.md)

<a id="topic-benchmark"></a>

## 12 · 数据集、基准与工具

优先了解任务定义、数据处理、指标和复现入口。

<a id="paper-traffident"></a>

- **TraffiDent** — Xiaochuan Gou et al. **[TraffiDent: A Dataset for Understanding the Interplay Between Traffic Dynamics and Incidents](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html)**. 2025 · NeurIPS Datasets and Benchmarks.

  对齐交通状态、事故及道路属性，支持事故后的交通预测和相关分析。

  [正式版本](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html) · [发表证据](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html) · 代码：未核验到作者代码

<a id="paper-basicts"></a>

- **BasicTS** — Zezhi Shao et al. **[Exploring Progress in Multivariate Time Series Forecasting: Comprehensive Benchmarking and Heterogeneity Analysis](https://arxiv.org/abs/2310.06119)**. 2024 · IEEE TKDE；arXiv 首发 2023.

  通过统一评测流程与时空异质性分析，研究多变量预测结果为何难以直接比较。

  [发表证据](https://github.com/GestaltCogTeam/BasicTS) · [代码](https://github.com/GestaltCogTeam/BasicTS)（作者/项目仓库已核验）

<a id="paper-weatherbench2"></a>

- **WeatherBench2** — Stephan Rasp et al. **[WeatherBench 2: A Benchmark for the Next Generation of Data‐Driven Global Weather Models](https://arxiv.org/abs/2308.15560)**. 2024 · Journal of Advances in Modeling Earth Systems；arXiv 首发 2023.

  更新中期天气评测框架，提供基准数据、物理/数据驱动对照与评测规范。

  [正式版本](https://doi.org/10.1029/2023MS004019) · [发表证据](https://doi.org/10.1029/2023MS004019) · [代码](https://github.com/google-research/weatherbench2)（作者/项目仓库已核验）

<a id="paper-largest"></a>

- **LargeST** — Xu Liu et al. **[LargeST: A Benchmark Dataset for Large-Scale Traffic Forecasting](https://arxiv.org/abs/2306.08259)**. 2023 · NeurIPS Datasets and Benchmarks.

  提供大规模、多年交通传感器数据及元数据，便于研究预测准确率与计算开销。

  [发表证据](https://github.com/liuxu77/LargeST) · [代码](https://github.com/liuxu77/LargeST)（作者/项目仓库已核验）

<a id="paper-libcity"></a>

- **LibCity** — Jiawei Jiang et al. **[LibCity: A Unified Library Towards Efficient and Comprehensive Urban Spatial-Temporal Prediction](https://arxiv.org/abs/2304.14343)**. 2023 · arXiv；正式发表状态未核验.

  将城市预测模型、数据格式和评测流程组织到统一工具库；本条收录扩展稿。

  [发表证据](https://arxiv.org/abs/2304.14343) · [代码](https://github.com/LibCity/Bigscity-LibCity)（作者/项目仓库已核验）

  版本/使用说明：此条对应 2023 扩展预印本；不将早期工具论文的发表信息套用到扩展稿。

<a id="paper-openstl"></a>

- **OpenSTL** — Cheng Tan et al. **[OpenSTL: A Comprehensive Benchmark of Spatio-Temporal Predictive Learning](https://arxiv.org/abs/2306.11249)**. 2023 · NeurIPS Datasets and Benchmarks.

  统一多类时空帧预测模型与评测任务，覆盖视频、交通网格和天气。

  [发表证据](https://github.com/chengtan9907/OpenSTL) · [代码](https://github.com/chengtan9907/OpenSTL)（作者/项目仓库已核验）

<a id="paper-sevir"></a>

- **SEVIR** — Mark Veillette et al. **[SEVIR : A Storm Event Imagery Dataset for Deep Learning Applications in Radar and Satellite Meteorology](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html)**. 2020 · NeurIPS.

  提供时空对齐的雷达与卫星风暴事件影像，支撑降水预测及跨传感器任务。

  [正式版本](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html) · [发表证据](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html) · [代码](https://github.com/MIT-AI-Accelerator/neurips-2020-sevir)（作者/项目仓库已核验）

<a id="paper-weatherbench"></a>

- **WeatherBench** — Stephan Rasp et al. **[WeatherBench: A Benchmark Data Set for Data‐Driven Weather Forecasting](https://arxiv.org/abs/2002.00469)**. 2020 · Journal of Advances in Modeling Earth Systems.

  建立数据驱动天气预测的数据、基线与统一指标入口。

  [正式版本](https://doi.org/10.1029/2020MS002203) · [发表证据](https://doi.org/10.1029/2020MS002203) · [代码](https://github.com/pangeo-data/WeatherBench)（作者/项目仓库已核验）

<a id="paper-evoxxltraffic"></a>

- **EvoXXLTraffic** — Du Yin et al. **[From XXLTraffic to EvoXXLTraffic: Scaling Traffic Forecasting to Sensor-Evolving Networks](https://arxiv.org/abs/2605.29768)**. 2026 · arXiv；正式发表状态未核验.

  提供逐年变化的传感器目录、持续站点标识和交通矩阵，区分全传感器预测与新节点的监督适配。

  [发表证据](https://arxiv.org/abs/2605.29768) · [代码](https://github.com/cruiseresearchgroup/TSAS26-EvoXXLTraffic)（作者/项目仓库已核验）

  版本/使用说明：首发 2026-05-28，v3 修订 2026-11-12；为 XXLTraffic 家族扩展基准，非新预测模型。采用回溯地理图和特定实现适配；新节点接受当年训练，不属于零样本。已检查源码与运行说明，未下载数据或复现。

<a id="paper-conformal-wx"></a>

- **Conformal-WX** — Mariya **[Distribution-Free Uncertainty Quantification for Weather Forecasting: Conformal Prediction Under Spatiotemporal Dependence](https://arxiv.org/abs/2611.24329)**. 2026 · arXiv；正式发表状态未核验.

  在 ERA5 网格气温预测上比较八种区间估计程序，同时衡量逐格覆盖率、每日空间覆盖波动和连续漏报。

  [发表证据](https://arxiv.org/abs/2611.24329) · [代码](https://github.com/Mariyaaleem/conformal-wx)（作者/项目仓库已核验）

  版本/使用说明：arXiv 2026-11-18 首发。 逐格边际覆盖与同一天各格点联合覆盖分别评估。研究范围为一种变量、两种预报器。

<a id="paper-seasonrainbench"></a>

- **SeasonRainBench** — Qiuyan Sun et al. **[SeasonRainBench: Global Seasonal Precipitation](https://arxiv.org/abs/2611.22281)**. 2026 · arXiv；正式发表状态未核验.

  用全球逐月降水、气候模拟和业务集合预报构建提前 1 至 5 个月的预测基准，并评估异常强度和雨带位置。

  [发表证据](https://arxiv.org/abs/2611.22281) · 代码：未核验到作者代码

  版本/使用说明：arXiv 2026-11-17 首发。

<a id="paper-otter-nyc"></a>

- **OTTER-NYC** — Seongwon Jin et al. **[OTTER-NYC: A Minute-Scale Multimodal Dataset for Urban Flood Event Dynamics and Forecasting](https://doi.org/10.1038/s41597-026-08642-w)**. 2026 · Scientific Data.

  将纽约积水传感器的分钟级深度与降水、地形和排水设施对齐，支持站点积水预测及事件质量控制。

  [正式版本](https://doi.org/10.1038/s41597-026-08642-w) · [发表证据](https://www.nature.com/articles/s41597-026-08642-w_reference.pdf) · [代码](https://github.com/jinwork00/OTTER-NYC)（作者/项目仓库已核验）

  版本/使用说明：2026-11-17 在线发表。 已核验作者公开的数据处理与质控流水线，预测训练实现需另行核验。

<a id="paper-traffic-imc"></a>

- **Traffic-IMC** — Seungbin Yim et al. **[Traffic-IMC: An Urban Road-Network Traffic Forecasting Benchmark](https://drive.google.com/file/d/1O5jDSMjIpcYjVg7dfM3LMj0ABRkyP2V5/view?usp=drivesdk)**. 2026 · ACM SIGSPATIAL 2026.

  仁川 2,013 个路段传感器的逐时流量基准同时提供有向可达图、原始有效性掩码和插补输入。评分排除原本无效的目标。

  [发表证据](https://sigspatial2026.sigspatial.org/detailed-program.html) · [代码](https://github.com/ysb06/traffic-imc)（作者/项目仓库已核验）

  版本/使用说明：会议官网议程与作者稿已核对。

<a id="paper-heatcast"></a>

- **HeatCast** — Jesus Guerrero et al. **[HeatCast: A Benchmark for Neighborhood-Scale LST Forecasting across 124 U.S. Cities](https://arxiv.org/abs/2608.07640)**. 2026 · ACM SIGSPATIAL 2026.

  用 124 个美国城市的 Landsat 月度影像进行 30 米地表温度的次月预测，按固定时间切分并按局地气候区评价。

  [发表证据](https://sigspatial2026.sigspatial.org/detailed-program.html) · 代码：未核验到作者代码

  版本/使用说明：会议官网议程与作者稿已核对。 arXiv 首发 2026-08-07。 作者链接的数据集可访问，尚未独立核验训练实现。
