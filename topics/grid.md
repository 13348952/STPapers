# 通用网格与时空帧预测

[简体中文](grid.md) | [English](grid.en.md) · [主题导航 / Topics](README.md) · [返回主目录](../README.md)

<a id="topic-grid"></a>

## 10 · 通用网格与时空帧预测

作为天气/城市网格预测的架构基础；包含视频预测背景。

<a id="paper-tau"></a>

- **TAU** — Cheng Tan et al. **[Temporal Attention Unit: Towards Efficient Spatiotemporal Predictive Learning](https://arxiv.org/abs/2206.12126)**. 2023 · CVPR；arXiv 首发 2022.

  将时间注意力拆分为帧内和帧间部分，改善并行时空帧预测。

  [发表证据](https://github.com/chengtan9907/OpenSTL) · [代码](https://github.com/chengtan9907/OpenSTL)（作者团队工具库实现已核验）

<a id="paper-simvp"></a>

- **SimVP** — Zhangyang Gao et al. **[SimVP: Simpler yet Better Video Prediction](https://arxiv.org/abs/2206.05099)**. 2022 · CVPR.

  以卷积编码器、时间处理模块和解码器构成简洁视频/网格预测基线。

  [发表证据](https://github.com/gaozhangyang/SimVP-Simpler-yet-Better-Video-Prediction) · [代码](https://github.com/gaozhangyang/SimVP-Simpler-yet-Better-Video-Prediction)（作者/项目仓库已核验）

<a id="paper-phydnet"></a>

- **PhyDNet** — Vincent Le Guen et al. **[Disentangling Physical Dynamics from Unknown Factors for Unsupervised Video Prediction](https://arxiv.org/abs/2003.01460)**. 2020 · CVPR.

  将可解释的物理动态与未知残差因素分离，用于未来帧预测。

  [发表证据](https://github.com/vincent-leguen/PhyDNet) · [代码](https://github.com/vincent-leguen/PhyDNet)（作者/项目仓库已核验）

<a id="paper-mim"></a>

- **MIM** — Yunbo Wang et al. **[Memory In Memory: A Predictive Neural Network for Learning Higher-Order Non-Stationarity from Spatiotemporal Dynamics](https://arxiv.org/abs/1811.07490)**. 2019 · CVPR；arXiv 首发 2018.

  通过记忆模块处理时空序列中的高阶非平稳变化。

  [发表证据](https://github.com/Yunbo426/MIM) · [代码](https://github.com/Yunbo426/MIM)（作者/项目仓库已核验）

<a id="paper-predrnnpp"></a>

- **PredRNNpp** — Yunbo Wang et al. **[PredRNN++: Towards A Resolution of the Deep-in-Time Dilemma in Spatiotemporal Predictive Learning](https://arxiv.org/abs/1804.06300)**. 2018 · ICML.

  以因果 LSTM 与梯度通路缓解深层递归预测中的优化困难。

  [发表证据](https://github.com/Yunbo426/predrnn-pp) · [代码](https://github.com/Yunbo426/predrnn-pp)（作者/项目仓库已核验）

<a id="paper-predrnn"></a>

- **PredRNN** — Yunbo Wang et al. **[PredRNN: Recurrent Neural Networks for Predictive Learning using Spatiotemporal LSTMs](https://papers.nips.cc/paper/6689-predrnn-recurrent-neural-networks-for-predictive-learning-using-spatiotemporal-lstms)**. 2017 · NeurIPS.

  使用时空 LSTM 及双重记忆状态建模未来帧，属于通用时空预测背景。

  [正式版本](https://papers.nips.cc/paper/6689-predrnn-recurrent-neural-networks-for-predictive-learning-using-spatiotemporal-lstms) · [发表证据](https://papers.nips.cc/paper/6689-predrnn-recurrent-neural-networks-for-predictive-learning-using-spatiotemporal-lstms) · [代码](https://github.com/thuml/predrnn-pytorch)（作者/项目仓库已核验）

<a id="paper-trajgru"></a>

- **TrajGRU** — Xingjian Shi et al. **[Deep Learning for Precipitation Nowcasting: A Benchmark and A New Model](https://arxiv.org/abs/1706.03458)**. 2017 · NeurIPS.

  在降水临近预报中学习位置相关的递归连接，并提供相应基准。

  [发表证据](https://arxiv.org/abs/1706.03458) · 代码：未核验到作者代码

<a id="paper-convlstm"></a>

- **ConvLSTM** — Xingjian Shi et al. **[Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting](https://arxiv.org/abs/1506.04214)**. 2015 · NeurIPS.

  将卷积放入 LSTM 状态转换，为网格序列与降水临近预报提供基础架构。

  [正式版本](https://papers.nips.cc/paper_files/paper/2015/hash/07563a3fe3bbe7e3ba84431ad9d055af-Abstract.html) · [发表证据](https://papers.nips.cc/paper_files/paper/2015/hash/07563a3fe3bbe7e3ba84431ad9d055af-Abstract.html) · 代码：未核验到作者代码
