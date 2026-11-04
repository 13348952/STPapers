# 数据集与评测入口

[返回主目录](README.md)

下表是数据与协议的入口，不表示本次已下载数据或运行基准。论文数据分割、数据清洗版本和可下载性应以对应项目当前说明为准。

| 数据/工具 | 任务与价值 | 主源入口 | 使用时关注 |
| --- | --- | --- | --- |
| METR-LA、PEMS-BAY | 道路传感器速度预测的经典设置 | [DCRNN](https://github.com/liyaguang/DCRNN) | 时间划分、图生成、缺失值和多步评测 |
| PeMS03/04/07/08 | 交通流量预测的常用数据 | [STSGCN](https://github.com/Davidham3/STSGCN)、[AGCRN](https://github.com/LeiBAI/AGCRN) | 不同子集/变量并不等价；完整 ASTGCN 与近期分支不能混写 |
| LargeST：SD/GBA/GLA/CA | 大规模路网与长期历史；原论文包含 8,600 个传感器及五年时间覆盖 | [论文](https://arxiv.org/abs/2306.08259)、[项目](https://github.com/liuxu77/LargeST) | 明确所用年份、区域、采样间隔、输入窗口、预测跨度及硬件 |
| EXPY-TKY | 东京路网速度预测，适合研究空间异质性 | [MegaCRN](https://github.com/deepkashiwa20/MegaCRN) | 使用 AAAI 对应版本；留意作者修订的结果与数据处理 |
| TaxiBJ、BikeNYC | 城市网格人群/交通流入流出 | [ST-ResNet 论文](https://arxiv.org/abs/1610.00081)、[DeepSTN+](https://github.com/vonfeng/DeepSTN) | 区分网格尺寸、时间粒度和外部天气/节假日等因素 |
| TraffiDent | 交通状态与事故对齐，支持事故后的预测 | [正式论文集](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7813e19a86fd73d40f7e811ab15f6d5f-Abstract-Datasets_and_Benchmarks_Track.html)、[数据项目](https://xaitraffic.github.io) | 外部事故信息何时可用，避免使用预测时尚不可得的信息 |
| SEVIR | 时空对齐的多传感器风暴影像 | [论文](https://papers.neurips.cc/paper/2020/hash/fa78a16157fed00d7a80515818432169-Abstract.html)、[项目](https://github.com/MIT-AI-Accelerator/neurips-2020-sevir) | 降水阈值、事件划分、分辨率及条件输入模态 |
| WeatherBench | 基于再分析数据的全球天气评测 | [项目](https://github.com/pangeo-data/WeatherBench) | 纬度加权、变量/气压层、预报时效 |
| WeatherBench 2 | 更新的中期天气数据与评测框架 | [项目](https://github.com/google-research/weatherbench2) | 确定性与集合预报指标、分析资料/再分析资料与初始化设置 |
| BasicTS / BasicTS+ | 统一多变量与时空预测的训练和评测 | [论文](https://arxiv.org/abs/2310.06119)、[项目](https://github.com/GestaltCogTeam/BasicTS) | 固定具体版本；工具库中的模型实现不自动等于原作者代码 |
| LibCity | 城市时空预测工具与数据格式 | [项目](https://github.com/LibCity/Bigscity-LibCity) | 数据格式、配置文件、任务与具体模型支持范围 |
| OpenSTL | 通用时空帧预测评测 | [论文](https://arxiv.org/abs/2306.11249)、[项目](https://github.com/chengtan9907/OpenSTL) | 视频、天气与交通任务的损失和指标各自对齐 |

## 建议保存的实验配置

数据版本/文件哈希、训练/验证/测试时间边界、归一化拟合范围、缺失值规则、输入长度、预测长度、外部特征可用时间、随机种子、模型参数量、训练/推理硬件、批大小和计时方式。涉及预训练时再记录预训练数据、是否包含测试区域/时间，以及目标域微调预算。

这些是后续复现的记录建议。本次交付只完成文献与公开资源整理，没有产生新的实验结论。
