"""English README renderer; paper metadata and translations live in papers.json."""
from collections import Counter

CATEGORIES = {
    'survey': ('Surveys and introductions', 'Maps of tasks, methods, and resources.'),
    'urban': ('Urban grid flow and demand forecasting', 'Regional inflows, outflows, and passenger demand, represented as grids or regional graphs.'),
    'graph': ('Graph convolutions, dynamic graphs, and continuous-time modeling', 'Spatial dependencies and temporal dynamics of road or sensor nodes.'),
    'attention': ('Attention, Transformers, and state-space models', 'Spatio-temporal attention, embeddings, propagation delays, and combinations with state-space models.'),
    'efficient': ('Simple baselines, efficiency, and large-scale forecasting', 'Designs that account for node count, history length, forecasting horizon, and computational cost.'),
    'pretrain': ('Self-supervised learning and pretraining', 'Contrastive learning, masked modeling, and their use in downstream forecasting.'),
    'transfer': ('Heterogeneity, meta-learning, and transfer', 'Node-specific parameters, cross-domain adaptation, and continual learning are distinct tasks.'),
    'foundation': ('Foundation models, language models, and cross-modal transfer', 'Unified pretraining and few-shot or zero-shot adaptation.'),
    'probabilistic': ('Probabilistic spatio-temporal graph forecasting', 'Predicting future distributions or samples rather than only point estimates.'),
    'grid': ('General grid and spatio-temporal frame prediction', 'Architectural foundations for weather and urban grid forecasting, including video prediction background.'),
    'weather': ('Precipitation, weather, and Earth-system forecasting', 'Nowcasting, medium-range weather forecasting, and Earth-system foundation models.'),
    'benchmark': ('Datasets, benchmarks, and tools', 'Task definitions, data processing, metrics, and resources for reproduction.'),
    'related': ('Related tasks and time-series background', 'Time-series baselines, imputation, and spatial extrapolation; task definitions and physical-space assumptions are distinguished.'),
}
CODE_STATUSES = {
    '作者/项目仓库已核验': 'author/project repository checked',
    '作者团队工具库实现已核验': "implementation in the authors' toolkit checked",
    '未核验到作者代码': 'author code not verified',
    '论文提供匿名代码，访问未核验': 'anonymous code linked by the paper; access not verified',
    '论文提供链接，本次返回 404': 'linked by the paper; returned HTTP 404 during verification',
    '项目仓库可访问，归属链待补强': 'project repository accessible; author attribution needs stronger evidence',
}


def build_english(papers, cats, as_of, author, anchor, updated_on=None):
    """Render all records, failing on missing translations instead of hiding them."""
    if set(cats) != set(CATEGORIES):
        raise ValueError('English category translations must match categories.json')
    for r in papers:
        if not r.get('summary_en', '').strip():
            raise ValueError(r['id'] + ': missing summary_en')
        if bool(r['notes'].strip()) != bool(r.get('notes_en', '').strip()):
            raise ValueError(r['id'] + ': English notes must match the presence of Chinese notes')
        if r['code_status'] not in CODE_STATUSES:
            raise ValueError(r['id'] + ': missing English code-status translation')
    counts = Counter(r['category'] for r in papers)
    nrepo = sum(r['code_verification_level'] == 'repository' for r in papers)
    npre = sum(r['venue'] == 'arXiv' for r in papers)
    current = sum(r['year'] == as_of.year for r in papers)
    first, last = min(r['year'] for r in papers), max(r['year'] for r in papers)
    body = f'''# STPapers · Spatio-Temporal Forecasting Papers

[简体中文](README.md) | **English**

A curated reading list for spatio-temporal forecasting.

Inspired by the topic organization and contribution model of [RSPapers](https://github.com/hongleizhang/RSPapers), this repository collects papers, datasets, and code resources for spatio-temporal forecasting. Method summaries are editorial descriptions written for this catalog; paper titles retain their original English wording.

**Search cutoff: {as_of.isoformat()} (Asia/Shanghai). {len(papers)} unique entries across {len(cats)} topics, covering {first}–{last}; {current} papers are assigned to {as_of.year} under the verified year convention, and {nrepo} papers link to inspected author/project repositories.** Repository coverage is counted per paper; one toolkit can serve multiple papers.

Catalog updated: {(updated_on or as_of).isoformat()}. Targeted backfills do not advance the complete-search cutoff; see the [update log](updates/README.md) for actual coverage.

This is a representative collection centered on traffic and urban graph forecasting, with coverage of grid sequences, precipitation, and weather. It is neither an exhaustive review nor a performance leaderboard. {npre} entries use verified preprint records; some may have formally published versions that were not confirmed in this search.

## Quick links

- [Browse by year](BY_YEAR.md) · [Recent papers ({as_of.year - 1}–{as_of.year})](RECENT.md) · [2025–2026 index](RECENT_2025_2026.md)
- [Datasets and tools](DATASETS.md) · [Search and verification notes](SEARCH_NOTES.md) · [Contributing](CONTRIBUTING.md)
- [CSV table](papers.csv) · [JSON catalog](papers.json) · [Draft BibTeX references](references.bib)
- [Changelog](CHANGELOG.md) · [Structural validation results](verification.json)
- [Weekly update log](updates/README.md) · [Monitoring workflow](MONITORING.md) · [Contributors](CONTRIBUTORS.md)
- [Standalone topic pages](topics/README.md) · [Tutorial-style reading guide](TUTORIALS.en.md)

The English README, topic pages, and reading guide cover the same catalog as their Chinese counterparts. Other supporting guides and secondary indexes are currently in Chinese; paper titles and source links are shared across both versions.

## Scope and labels

**Core scope:** tasks that forecast future time intervals and have explicit spatial locations, regions, graph structures, or two- or three-dimensional spatial fields. Relationships learned among variables may represent statistical dependencies; they do not automatically establish geographic relationships or causal propagation.

**Related background is listed separately:** general time-series baselines, imputation methods, and spatial extrapolation. CSDI primarily addresses imputation; STGNP infers target locations from surrounding observations. Video prediction architectures are included as background for grid forecasting. Trajectory planning, recommender systems, and static graph classification are outside the core catalog.

Years follow a verified formal publication when available, otherwise the first arXiv release. Differences between online publication and volume years are noted. Each paper has one primary category and is counted once, even if it spans multiple topics.

“Author/project repository checked” means that a paper-linked README or repository page was inspected. **No training runs or numerical reproduction were performed, and this label does not establish that complete training code and data are open.** Paper-only code links, access failures, and limited attribution evidence have separate labels. “Not verified” does not mean “does not exist.”

## Suggested reading paths

These are editorial suggestions, not rankings of model performance.

| Goal | Suggested order | Questions to examine |
| --- | --- | --- |
| Foundations of traffic graph forecasting | DCRNN → STGCN → Graph WaveNet → AGCRN → D²STGNN | How do fixed graphs, learned graphs, node heterogeneity, and dynamic dependencies differ? |
| Transformers and simple baselines | STID → GMAN → PDFormer → STAEformer | Do gains come from interaction operators, identity/time encodings, or training settings? |
| Large-scale traffic forecasting | LargeST → BigST → PatchSTG → GraphSparseNet → MiniST / HieraMix / FaST | How do node count, history length, and forecasting horizon each affect cost? |
| Self-supervised learning and transfer | STEP → STGCL → ST-SSL → STD-MAE → UniST / UrbanPG | How are pretraining information, domain overlap, and adaptation cost controlled? |
| Probabilistic forecasting | TimeGrad (background) → DiffSTG → SpecSTG → GenCast | How should point error, distribution calibration, and joint spatial consistency be evaluated together? |
| Grids and weather | ConvLSTM → PredRNN → SimVP → Earthformer → GraphCast / Aurora | What roles do local structure, long-range communication, physical constraints, and pretraining play? |

## Topics

| No. | Topic | Entries |
| --- | --- | ---: |
'''
    for c, (num, _, _) in cats.items():
        name, _ = CATEGORIES[c]
        body += f'| {num} | [{name}](#topic-{c}) | {counts[c]} |\n'
    for c, (num, _, _) in cats.items():
        name, desc = CATEGORIES[c]
        body += f'\n<a id="topic-{c}"></a>\n\n## {num} · {name}\n\n{desc}\n\n'
        for r in papers:
            if r['category'] != c:
                continue
            year = f"{r['year']} · {r['venue']}"
            if r['arxiv_first_year'] and r['arxiv_first_year'] != r['year']:
                year += f"; first arXiv release: {r['arxiv_first_year']}"
            if r['venue'] == 'arXiv':
                year += '; formal publication status not verified'
            lines = [f'<a id="{anchor(r)}"></a>',
                     f"- **{r['id']}** — {author(r)} **[{r['title']}]({r['paper_url']})**. {year}.",
                     f"  {r['summary_en']}"]
            links = []
            if r['publication_url']:
                links.append(f"[Published version]({r['publication_url']})")
            links.append(f"[Publication evidence]({r['publication_evidence_url']})")
            if r['code_url']:
                links.append(f"[Code]({r['code_url']}) ({CODE_STATUSES[r['code_status']]})")
            else:
                links.append('Code: ' + CODE_STATUSES[r['code_status']])
            lines.append('  ' + ' · '.join(links))
            if r['notes_en']:
                lines.append('  Version / usage notes: ' + r['notes_en'])
            body += '\n\n'.join(lines) + '\n\n'
    body += '''## Conditions to align before comparing papers

Data versions, temporal splits, sampling intervals, input windows, forecasting steps, missing/zero-value masks, normalization, external modalities, pretraining data, validation-based selection, and compute budgets all affect comparisons. Select configurations using the validation set, then evaluate the selected model on the test set; do not use test results to select configurations.

LargeST's SD/GBA/GLA/CA, classic PeMS subsets, METR-LA/PEMS-BAY, and meteorological ERA5/SEVIR involve different tasks and metrics and should not be combined into a single ranking. Publication year and code availability alone do not establish that a model is stronger.

## Maintenance

`papers.json` is the single source of paper data, including `summary_zh` / `summary_en` and `notes` / `notes_en`. After editing it, run `python scripts/build_catalog.py` from the repository root to regenerate both READMEs, year indexes, CSV, and BibTeX, and check the counts. Contribution guidelines are in [CONTRIBUTING.md](CONTRIBUTING.md).

Weekly searches verify new papers and official code links, deduplicate entries, and update the catalog. Additions, revisions, and items awaiting verification are recorded in the [update log](updates/README.md). The search cutoff is stored in `catalog_meta.json` and advances only after a completed search. New or revised entries must maintain both language versions; missing English summaries, notes, or code-status translations cause generation to fail.

## Contributors

- [13348952](https://github.com/13348952): project founder and maintainer.
- **Codex (OpenAI)**: AI-assisted literature search, source and code-link verification, categorization, summaries, catalog generation, and ongoing maintenance. See [contribution details](CONTRIBUTORS.md).

This repository collects bibliographic information, links, and original short descriptions. Papers, datasets, code, and models remain subject to their authors' and publishers' respective licenses. Its organization is inspired by RSPapers; its contents were searched and organized around spatio-temporal forecasting.
'''
    return body
