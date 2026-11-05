# 图卷积、动态图与连续时间建模

[简体中文](graph.md) | [English](graph.en.md) · [主题导航 / Topics](README.md) · [返回主目录](../README.md)

<a id="topic-graph"></a>

## 03 · 图卷积、动态图与连续时间建模

以道路或传感器节点为对象，研究空间依赖和时间动态。

<a id="paper-strp"></a>

- **STRP** — Shuhao Li et al. **[From Coarse to Fine: Managing Temporal Granularity in Spatio-Temporal Data for Fine-Grained Traffic Prediction](https://arxiv.org/abs/2606.09392)**. 2026 · arXiv；正式发表状态未核验.

  研究不同时间粒度之间的交通预测：从粗采样历史预测细粒度未来，采用 Tree Convolution 做空间建模，并用 Inverse Dilated Convolution 做逐步时间外推，同时区分 window-based 与 duration-based 设定。

  [发表证据](https://arxiv.org/abs/2606.09392) · 代码：未核验到作者代码

  版本/使用说明：输入与输出时间粒度不同于常规同分辨率预测；保留 arXiv 预印本记录，未核验到正式发表版本或作者代码。

<a id="paper-igstgnn"></a>

- **IGSTGNN** — Lixiang Fan et al. **[Incident-Guided Spatiotemporal Traffic Forecasting](https://arxiv.org/abs/2602.02528)**. 2026 · KDD.

  结合事故上下文的空间融合（ICSF）与时间事故影响衰减（TIID）来建模交通历史与外部事故信息，并附带交通/事故对齐数据集。

  [正式版本](https://doi.org/10.1145/3770854.3780215) · [发表证据](https://github.com/fanlixiang/IGSTGNN) · [代码](https://github.com/fanlixiang/IGSTGNN)（作者/项目仓库已核验）

  版本/使用说明：KDD 2026 信息依据作者仓库引用，出版者页面本次未成功访问。使用事故上下文，比较时需对齐事故信息的可用时点和输入范围；已检查训练入口，未运行实验。

<a id="paper-dgcrn"></a>

- **DGCRN** — Fuxian Li et al. **[Dynamic Graph Convolutional Recurrent Network for Traffic Prediction: Benchmark and Solution](https://arxiv.org/abs/2104.14917)**. 2023 · ACM TKDD；arXiv 首发 2021.

  由节点动态信息生成图结构，同时提供交通预测的统一评测与实现。

  [发表证据](https://github.com/tsinghua-fib-lab/Traffic-Benchmark) · [代码](https://github.com/tsinghua-fib-lab/Traffic-Benchmark)（作者/项目仓库已核验）

<a id="paper-d2stgnn"></a>

- **D2STGNN** — Zezhi Shao et al. **[Decoupled Dynamic Spatial-Temporal Graph Neural Network for Traffic Forecasting](https://arxiv.org/abs/2206.09112)**. 2022 · PVLDB.

  将交通信号拆为扩散与固有成分，结合动态图学习分别建模。

  [发表证据](https://github.com/GestaltCogTeam/D2STGNN) · [代码](https://github.com/GestaltCogTeam/D2STGNN)（作者/项目仓库已核验）

<a id="paper-dstagnn"></a>

- **DSTAGNN** — Shiyong Lan et al. **[DSTAGNN: Dynamic Spatial-Temporal Aware Graph Neural Network for Traffic Flow Forecasting](https://proceedings.mlr.press/v162/lan22a.html)**. 2022 · ICML.

  结合动态时空关系建模与图网络进行交通预测。

  [正式版本](https://proceedings.mlr.press/v162/lan22a.html) · [发表证据](https://proceedings.mlr.press/v162/lan22a.html) · [代码](https://github.com/SYLan2019/DSTAGNN)（作者/项目仓库已核验）

<a id="paper-stgncde"></a>

- **STGNCDE** — Jeongwhan Choi et al. **[Graph Neural Controlled Differential Equations for Traffic Forecasting](https://arxiv.org/abs/2112.03558)**. 2022 · AAAI；arXiv 首发 2021.

  联合空间和时间神经控制微分方程，提供连续时间建模视角。

  [发表证据](https://github.com/jeongwhanchoi/STG-NCDE) · [代码](https://github.com/jeongwhanchoi/STG-NCDE)（作者/项目仓库已核验）

<a id="paper-gts"></a>

- **GTS** — Chao Shang et al. **[Discrete Graph Structure Learning for Forecasting Multiple Time Series](https://arxiv.org/abs/2101.06861)**. 2021 · ICLR.

  学习可微采样的离散图分布，并与多序列预测模型共同优化。

  [发表证据](https://github.com/chaoshangcs/GTS) · [代码](https://github.com/chaoshangcs/GTS)（作者/项目仓库已核验）

<a id="paper-stfgnn"></a>

- **STFGNN** — Mengzhang Li et al. **[Spatial-Temporal Fusion Graph Neural Networks for Traffic Flow Forecasting](https://arxiv.org/abs/2012.09641)**. 2021 · AAAI；arXiv 首发 2020.

  融合空间图与数据驱动的时间关系图，并结合门控卷积。

  [发表证据](https://github.com/MengzhangLI/STFGNN) · [代码](https://github.com/MengzhangLI/STFGNN)（作者/项目仓库已核验）

  版本/使用说明：作者 README 对部分数据集结果作了更正说明；比较数字前应检查最新论文与仓库。

<a id="paper-stgode"></a>

- **STGODE** — Zheng Fang et al. **[Spatial-Temporal Graph ODE Networks for Traffic Flow Forecasting](https://arxiv.org/abs/2106.12931)**. 2021 · KDD.

  以张量形式的常微分方程建模时空动态，同时考虑空间与语义关系。

  [发表证据](https://github.com/square-coder/STGODE) · [代码](https://github.com/square-coder/STGODE)（作者/项目仓库已核验）

<a id="paper-agcrn"></a>

- **AGCRN** — Lei Bai et al. **[Adaptive Graph Convolutional Recurrent Network for Traffic Forecasting](https://arxiv.org/abs/2007.02842)**. 2020 · NeurIPS.

  结合节点自适应参数学习和自适应图生成，刻画不同节点的预测模式。

  [发表证据](https://github.com/LeiBAI/AGCRN) · [代码](https://github.com/LeiBAI/AGCRN)（作者/项目仓库已核验）

<a id="paper-mtgnn"></a>

- **MTGNN** — Zonghan Wu et al. **[Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks](https://arxiv.org/abs/2005.11650)**. 2020 · KDD.

  联合学习变量间有向图、mix-hop 传播与时间卷积；兼顾通用多变量序列与交通任务。

  [发表证据](https://github.com/nnzhan/MTGNN) · [代码](https://github.com/nnzhan/MTGNN)（作者/项目仓库已核验）

  版本/使用说明：通用多变量模型，因明确包含交通任务与图学习而收录主目录。

<a id="paper-stsgcn"></a>

- **STSGCN** — Chao Song et al. **[Spatial-Temporal Synchronous Graph Convolutional Networks: A New Framework for Spatial-Temporal Network Data Forecasting](https://ojs.aaai.org/index.php/AAAI/article/view/5438)**. 2020 · AAAI.

  把相邻时间片的节点连成局部时空图，联合建模局部时空关系与异质性。

  [正式版本](https://ojs.aaai.org/index.php/AAAI/article/view/5438) · [发表证据](https://ojs.aaai.org/index.php/AAAI/article/download/5438/5294) · [代码](https://github.com/Davidham3/STSGCN)（作者/项目仓库已核验）

<a id="paper-astgcn"></a>

- **ASTGCN** — Shengnan Guo et al. **[Attention Based Spatial-Temporal Graph Convolutional Networks for Traffic Flow Forecasting](https://ojs.aaai.org/index.php/AAAI/article/view/3881)**. 2019 · AAAI.

  通过时空注意力、图卷积与近期/日/周分支进行交通流预测。

  [正式版本](https://ojs.aaai.org/index.php/AAAI/article/view/3881) · [发表证据](https://ojs.aaai.org/index.php/AAAI/article/view/3881) · [代码](https://github.com/guoshnBJTU/ASTGCN-2019-pytorch)（作者/项目仓库已核验）

  版本/使用说明：关联的作者 PyTorch 仓库说明仅实现近期分支；不能默认等于完整三分支 ASTGCN。

<a id="paper-graph-wavenet"></a>

- **Graph-WaveNet** — Zonghan Wu et al. **[Graph WaveNet for Deep Spatial-Temporal Graph Modeling](https://arxiv.org/abs/1906.00121)**. 2019 · IJCAI.

  通过节点嵌入学习自适应邻接关系，并用膨胀时间卷积建模历史序列。

  [发表证据](https://github.com/nnzhan/Graph-WaveNet) · [代码](https://github.com/nnzhan/Graph-WaveNet)（作者/项目仓库已核验）

<a id="paper-dcrnn"></a>

- **DCRNN** — Yaguang Li et al. **[Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting](https://arxiv.org/abs/1707.01926)**. 2018 · ICLR；arXiv 首发 2017.

  将有向图扩散卷积与循环编码器—解码器结合，是理解路网预测的重要起点。

  [发表证据](https://github.com/liyaguang/DCRNN) · [代码](https://github.com/liyaguang/DCRNN)（作者/项目仓库已核验）

<a id="paper-stgcn"></a>

- **STGCN** — Bing Yu et al. **[Spatio-Temporal Graph Convolutional Networks: A Deep Learning Framework for Traffic Forecasting](https://arxiv.org/abs/1709.04875)**. 2018 · IJCAI；arXiv 首发 2017.

  用图卷积与时间卷积构成全卷积时空预测网络。

  [发表证据](https://github.com/VeritasYin/STGCN_IJCAI-18) · [代码](https://github.com/VeritasYin/STGCN_IJCAI-18)（作者/项目仓库已核验）
