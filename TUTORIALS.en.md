# Tutorial-style reading guide

[简体中文](TUTORIALS.md) | **English** · [Catalog](README.en.md) · [Topics](topics/README.md)

These are editorial reading suggestions, not performance rankings or reports of reproduced experiments. Each paper link leads to a catalog entry containing primary sources, version information, and code status.

## 1. Define the forecasting task first

Write one sentence: at time t, which observations available by that time are used to predict which variables, at which locations, and how far into the future? Record node/grid definitions, sampling interval, history length, output length, and external information.

Traffic sensor speed, regional demand, and weather fields are different tasks. Spatial extrapolation infers target locations from observations at other locations; it does not automatically mean forecasting future time intervals. Imputation results are also not directly comparable with future forecasting. See the task boundaries of [STGNP](README.en.md#paper-stgnp) and [CSDI](README.en.md#paper-csdi).

## 2. Choose a reading path by question

| Path | Suggested order | What to record |
| --- | --- | --- |
| Urban demand | [ST-ResNet](README.en.md#paper-st-resnet) → [DMVST-Net](README.en.md#paper-dmvst-net) → [STDN](README.en.md#paper-stdn) → [ST-MGCN](README.en.md#paper-st-mgcn) | Where do grid adjacency, semantic relations, flow relations, and multiple graphs come from? |
| Traffic graphs | [DCRNN](README.en.md#paper-dcrnn) → [Graph WaveNet](README.en.md#paper-graph-wavenet) → [AGCRN](README.en.md#paper-agcrn) → [ST-MetaNet](README.en.md#paper-st-metanet) | How are graphs and node parameters obtained? How does parameter generation from geographical attributes differ from cross-city adaptation? |
| Simple and efficient models | [STID](README.en.md#paper-stid) → [STAEformer](README.en.md#paper-staeformer) → [LargeST](README.en.md#paper-largest) → [PatchSTG](README.en.md#paper-patchstg) / [STGformer](README.en.md#paper-stgformer) | How do costs change after aligning history length, node count, hardware, and batch size? |
| Pretraining and transfer | [STEP](README.en.md#paper-step) → [STD-MAE](README.en.md#paper-stdmae) → [UniST](README.en.md#paper-unist) | Does pretraining cover test periods, cities, or nodes? Which labels are used during adaptation? |
| Probabilistic modeling | [GraphDF](README.en.md#paper-graphdf) (background) → [Graph SPDE kernels](README.en.md#paper-stgp-spde) → [DiffSTG](README.en.md#paper-diffstg) → [SpecSTG](README.en.md#paper-specstg) | Are outputs points, quantiles, distributions, or samples? Are calibration and joint spatial structure evaluated? |
| Grids and weather | [ConvLSTM](README.en.md#paper-convlstm) → [Earthformer](README.en.md#paper-earthformer) → [GraphCast](README.en.md#paper-graphcast) / [GenCast](README.en.md#paper-gencast) | Are variables, vertical levels, boundary conditions, lead times, and observation availability aligned? |

## 3. Make one reading card per paper

Copy these fields; a long review is not required to start.

```text
Paper ID / published version / primary source:
Task and spatial unit:
Inputs, outputs, sampling interval, and lead time:
Source of spatial structure and whether it changes during training:
Temporal modeling, extra modalities, and their availability times:
Data version, temporal split, normalization, and missing-value handling:
Validation-based configuration selection; timing of test evaluation:
Conclusions supported by the paper's evidence:
Your own unverified inferences:
Author-code attribution, commit, and data/weight availability:
One minimal feasible validation:
```

## 4. Fair comparison and minimal validation

First check a simple baseline under the same data version, split, input/output settings, and evaluation code, then add the method of interest. Estimate normalization statistics from training data according to the experimental protocol; record pretraining and auxiliary-data coverage separately. Select configurations on validation data and evaluate the selected configuration on test data.

| Comparison | Minimum information to record |
| --- | --- |
| Point forecasts | Units, masks, and per-horizon or averaged MAE/RMSE; zero handling for MAPE |
| Probabilistic forecasts | Output representation, sample count, suitable probabilistic scores, and interval coverage; point error alone is insufficient |
| Cost | Parameter count, peak memory, training/inference time, hardware, batch size, node count, history length, and output length |
| Stability | Seeds, repeat count, and individual results; a single best value does not establish stability |
| Reproduction entry | Fixed code commit, dependency versions, data sources, command, configuration, and logs |

“Repository checked” only means that its attribution and public contents were inspected. For example, the [DMVST-Net](README.en.md#paper-dmvst-net) author repository explicitly provides only the model component. A code link does not establish experimental reproduction, and learned association weights do not establish causal propagation.

## 5. Contribute a paper

Follow the [contribution guidelines](CONTRIBUTING.md): verify the title, authors, publication, and author code; deduplicate by DOI, version-independent arXiv ID, normalized title, and version relationship. Update bilingual summaries and notes in `papers.json`, run the generator, and distinguish additions, revisions, and pending candidates in the [update log](updates/README.md).
