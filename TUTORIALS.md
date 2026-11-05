# 教程式阅读指南

**简体中文** | [English](TUTORIALS.en.md) · [主目录](README.md) · [独立主题](topics/README.md)

以下是本目录的编辑阅读建议，不是性能排名，也不表示已经复现实验。每个论文入口链接到包含主源、版本和代码状态的目录条目。

## 1. 先写清楚预测任务

用一句话定义：在时刻 t，依据哪些当时可获得的历史观测，预测哪些位置、哪些变量、未来多久？记录节点/网格定义、采样间隔、输入长度、输出长度和外部信息。

交通传感器速度、区域需求和天气场属于不同任务。空间外推是根据已有位置观测推断目标位置，不自动意味着预测未来时间；插补也不能直接作为未来预测的同设置结果。参看 [STGNP](README.md#paper-stgnp)、[CSDI](README.md#paper-csdi) 的任务边界。

## 2. 按问题选择阅读路线

| 路线 | 推荐顺序 | 阅读时记录什么 |
| --- | --- | --- |
| 城市需求 | [ST-ResNet](README.md#paper-st-resnet) → [DMVST-Net](README.md#paper-dmvst-net) → [STDN](README.md#paper-stdn) → [ST-MGCN](README.md#paper-st-mgcn) | 网格相邻、语义关系、流量关系和多图关系分别来自哪里？ |
| 交通图预测 | [DCRNN](README.md#paper-dcrnn) → [Graph WaveNet](README.md#paper-graph-wavenet) → [AGCRN](README.md#paper-agcrn) → [ST-MetaNet](README.md#paper-st-metanet) | 图和节点参数如何获得？地理属性生成参数与跨城市适配有何区别？ |
| 简洁与高效模型 | [STID](README.md#paper-stid) → [STAEformer](README.md#paper-staeformer) → [LargeST](README.md#paper-largest) → [PatchSTG](README.md#paper-patchstg) / [STGformer](README.md#paper-stgformer) | 对齐输入窗口、节点数、硬件和批量大小后，成本如何变化？ |
| 预训练与迁移 | [STEP](README.md#paper-step) → [STD-MAE](README.md#paper-stdmae) → [UniST](README.md#paper-unist) | 预训练数据是否含测试时段、测试城市或测试节点？适配时使用哪些标签？ |
| 概率建模 | [GraphDF](README.md#paper-graphdf)（相关背景）→ [图 SPDE 核](README.md#paper-stgp-spde) → [DiffSTG](README.md#paper-diffstg) → [SpecSTG](README.md#paper-specstg) | 输出是点、分位数、分布还是样本？是否评估校准和空间联合结构？ |
| 网格与天气 | [ConvLSTM](README.md#paper-convlstm) → [Earthformer](README.md#paper-earthformer) → [GraphCast](README.md#paper-graphcast) / [GenCast](README.md#paper-gencast) | 变量、垂直层、边界条件、预测时效和观测可用时间是否一致？ |

## 3. 为每篇论文制作一张阅读卡

复制下面的字段即可，不需要先写长篇综述。

```text
论文 ID / 正式版本 / 主源：
任务与空间单位：
输入、输出、采样间隔、预测时效：
空间结构来源及训练时是否变化：
时间建模方式、额外模态及可用时点：
数据版本、时间划分、归一化、缺失值处理：
验证集如何选择配置；测试集何时评估：
论文证据支持的结论：
自己尚未验证的推断：
作者代码归属、提交版本、数据/权重是否可得：
一个最小可行验证：
```

## 4. 公平比较与最小验证

先在同一数据版本、划分、输入输出设置和评估代码下核对一个简单基线，再加入待研究方法。归一化统计量应按实验协议从训练数据估计；预训练和辅助数据的覆盖范围需单独记录。使用验证集选择配置，测试集只评估选定配置。

| 比较项目 | 至少记录 |
| --- | --- |
| 点预测 | MAE/RMSE 等指标的单位、掩码、逐时效或平均方式；MAPE 的零值处理 |
| 概率预测 | 输出形式、采样数、适用的概率评分与区间覆盖率；不要只比较点误差 |
| 成本 | 参数量、峰值显存、训练/推理时间、硬件、批量大小、节点数、历史长度和预测长度 |
| 稳定性 | 随机种子、重复次数及每次结果；单个最佳值不支持稳定性结论 |
| 可复现入口 | 固定代码提交、依赖版本、数据来源、运行命令、配置与日志 |

“仓库已核验”仅说明来源与公开内容经过检查。例如 [DMVST-Net](README.md#paper-dmvst-net) 的作者仓库明确只提供模型部分。不要把代码链接存在写成实验复现完成，也不要把学习到的关联权重解释为已证实的因果传播。

## 5. 如何贡献一篇新论文

按 [贡献规范](CONTRIBUTING.md) 核验标题、作者、正式版本和作者代码，用 DOI、无版本 arXiv ID、规范化标题及版本关系去重。更新 `papers.json` 的双语摘要和说明，运行生成脚本，并在 [更新记录](updates/README.md) 中区分新增、修订和待核验内容。
