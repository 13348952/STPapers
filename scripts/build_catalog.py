"""Regenerate Markdown/CSV/BibTeX from papers.json. Python 3, standard library only."""
import csv,json,re,collections
from pathlib import Path
from datetime import date
from readme_en import build_english
ROOT=Path(__file__).resolve().parents[1]
papers=json.loads((ROOT/'papers.json').read_text(encoding='utf8'))
cats=json.loads((ROOT/'categories.json').read_text(encoding='utf8'))
meta=json.loads((ROOT/'catalog_meta.json').read_text(encoding='utf8'))
as_of=date.fromisoformat(meta['last_successful_search_date'])
recent_start=as_of.year-1
def author(r):
    a=r['authors'][0]
    if ', ' in a:
        last,first=a.split(', ',1);a=first+' '+last
    return a+(' et al.' if len(r['authors'])>1 else '')
def anchor(r):return 'paper-'+r['id'].lower()
def entry(r,anchors=True):
    year=f"{r['year']} · {r['venue']}"
    if r['arxiv_first_year'] and r['arxiv_first_year']!=r['year']:year+=f"；arXiv 首发 {r['arxiv_first_year']}"
    if r['venue']=='arXiv':year+='；正式发表状态未核验'
    lines=[f'<a id="{anchor(r)}"></a>' if anchors else '',f"- **{r['id']}** — {author(r)} **[{r['title']}]({r['paper_url']})**. {year}.",f"  {r['summary_zh']}"]
    links=[]
    if r['publication_url']:links.append(f"[正式版本]({r['publication_url']})")
    links.append(f"[发表证据]({r['publication_evidence_url']})")
    if r['code_url']:links.append(f"[代码]({r['code_url']})（{r['code_status']}）")
    else:links.append('代码：未核验到作者代码')
    lines.append('  '+' · '.join(links))
    if r['notes']:lines.append('  版本/使用说明：'+r['notes'])
    return '\n\n'.join(x for x in lines if x)+'\n'
counts=collections.Counter(r['category'] for r in papers)
recent=[r for r in papers if recent_start<=r['year']<=as_of.year]
current_year_count=sum(r['year']==as_of.year for r in papers)
first_year=min(r['year'] for r in papers)
last_year=max(r['year'] for r in papers)
nrepo=sum(r['code_verification_level']=='repository' for r in papers)
npre=sum(r['venue']=='arXiv' for r in papers)
header=f'''# STPapers · 时空序列预测论文目录

**简体中文** | [English](README.en.md)

A curated reading list for spatio-temporal forecasting.

参考 [RSPapers](https://github.com/hongleizhang/RSPapers) 的主题分类和贡献方式，整理时空序列预测论文、数据集与代码入口。中文方法定位为本目录概括，论文保留英文原题。

**本次检索截止：{as_of.isoformat()}（Asia/Shanghai）。共 {len(papers)} 个独立条目、{len(cats)} 个主题，覆盖 {first_year}—{last_year}；其中 {current_year_count} 篇按核验口径归入 {as_of.year}，{nrepo} 篇关联已检查的作者/项目仓库。** 仓库数按论文计，同一个工具库可能对应多篇论文。

这是代表性精选目录，重点为交通/城市图预测，同时覆盖网格序列、降水和天气。并非全领域穷尽综述，也不是性能排行榜。{npre} 条采用已核验的预印本记录，其中一部分可能已有本次未确认的正式版本。

## 快速入口

- [按年份浏览](BY_YEAR.md) · [近期论文（{recent_start}—{as_of.year}）](RECENT.md) · [2025—2026 索引](RECENT_2025_2026.md)
- [数据集与工具](DATASETS.md) · [检索和核验说明](SEARCH_NOTES.md) · [贡献规范](CONTRIBUTING.md)
- [CSV 表格](papers.csv) · [JSON 原始目录](papers.json) · [BibTeX 引用草稿](references.bib)
- [版本记录](CHANGELOG.md) · [结构检查结果](verification.json)
- [每周更新记录](updates/README.md) · [更新流程](MONITORING.md) · [贡献者](CONTRIBUTORS.md)

## 收录范围与标记

**核心对象**：有明确空间位置、区域、图结构或二维/三维空间场，同时预测未来时间段的任务。图学习中的“变量关系”可以是统计依赖，不自动等同于地理关系或因果传播。

**相关背景单列**：纯时间序列基线、插补方法和广义城市表示学习。CSDI 的主任务是插补；视频预测架构作为网格预测背景收录。没有将轨迹规划、推荐系统、静态图分类等并入核心目录。

年份优先采用已核验的正式版本年份；未确认正式版本则使用 arXiv 首发年。期刊在线年与卷期年不同时保留说明。正文使用一个主分类，同一论文不会因跨主题而重复计数。

“作者/项目仓库已核验”表示已检查论文关联的 README 或仓库页面，**未执行训练、未验证复现数值，也不等于完整训练代码和数据均已开放**。仅有论文代码链接、访问失败及归属证据有限的情况分别标记；“未核验到”不表示不存在。

## 建议阅读路线

这些顺序是本目录的编辑建议，不代表模型性能排序。

| 目标 | 建议顺序 | 重点问题 |
| --- | --- | --- |
| 建立交通图预测基础 | DCRNN → STGCN → Graph WaveNet → AGCRN → D²STGNN | 固定图、学习图、节点异质性与动态依赖如何区分？ |
| 理解 Transformer 与简洁基线 | STID → GMAN → PDFormer → STAEformer | 提升来自交互算子，还是身份/时间编码和训练设置？ |
| 大规模交通预测 | LargeST → BigST → PatchSTG → GraphSparseNet → MiniST / HieraMix / FaST | 节点数、历史长度、预测跨度分别如何影响成本？ |
| 自监督与迁移 | STEP → STGCL → ST-SSL → STD-MAE → UniST / UrbanPG | 预训练信息、领域重叠和适配成本如何控制？ |
| 概率预测 | TimeGrad（背景）→ DiffSTG → SpecSTG → GenCast | 点误差、分布校准与联合空间一致性如何同时评估？ |
| 网格/天气 | ConvLSTM → PredRNN → SimVP → Earthformer → GraphCast / Aurora | 局部结构、长程通信、物理约束与预训练各有什么作用？ |

## 主题导航

| 编号 | 主题 | 条目数 |
| --- | --- | ---: |
'''
for c,(num,name,desc) in cats.items():header+=f'| {num} | [{name}](#topic-{c}) | {counts[c]} |\n'
body=header
for c,(num,name,desc) in cats.items():
    body+=f'\n<a id="topic-{c}"></a>\n\n## {num} · {name}\n\n{desc}\n\n'
    for r in papers:
        if r['category']==c:body+=entry(r)+'\n'
body+='''
## 比较论文时先对齐的条件

数据版本、时间划分、采样间隔、输入窗口、预测步数、缺失/零值掩码、归一化、外部模态、预训练数据、验证选择和计算预算会直接影响比较。使用验证集选择配置后，再对选定模型做测试集评估；不以测试集结果选择配置。

LargeST 的 SD/GBA/GLA/CA、经典 PeMS 子集、METR-LA/PEMS-BAY、气象 ERA5/SEVIR 的任务与指标不可直接混排。也不要用论文发表年份或代码存在与否推断模型更强。

## 维护

以 `papers.json` 为单一数据源，同时维护 `summary_zh` / `summary_en` 和 `notes` / `notes_en`。修改后在本目录运行 `python scripts/build_catalog.py`，同步生成中英文 README、年度索引、CSV 与 BibTeX，并检查统计。贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

每周检索新论文、核验论文与官方代码链接，去重后更新目录，并在 [更新记录](updates/README.md) 中保存每次新增、修订和待核验项。检索截止日期由 `catalog_meta.json` 记录，只有完成检索后才推进。

## 贡献者

- [13348952](https://github.com/13348952)：项目发起与维护。
- **Codex（OpenAI）**：AI 辅助文献检索、来源与代码链接核验、分类摘要、目录生成和持续维护。详见 [贡献说明](CONTRIBUTORS.md)。

本目录只整理文献信息、链接及原创简短说明；论文、数据、代码和模型分别遵循原作者及发布方许可。组织形式参考 RSPapers，内容按时空预测任务重新检索和组织。
'''
body_en=build_english(papers,cats,as_of,author,anchor)
(ROOT/'README.md').write_text(body,encoding='utf8')
(ROOT/'README.en.md').write_text(body_en,encoding='utf8')
for name,items,title in [('BY_YEAR.md',papers,'按年份浏览'),('RECENT.md',recent,f'近期论文（{recent_start}—{as_of.year}）'),('RECENT_2025_2026.md',[r for r in papers if 2025<=r['year']<=2026],'2025—2026 年论文')]:
    txt=f'# {title}\n\n[返回主目录](README.md)\n\n年份依据与代码标记见主目录。以下复用同一结构化数据，不额外增加论文数。\n'
    for y in sorted({r['year'] for r in items},reverse=True):
        selected=[r for r in items if r['year']==y]
        txt+=f'\n## {y}（{len(selected)} 篇）\n\n'
        for r in selected:txt+=entry(r,False)+'\n'
    (ROOT/name).write_text(txt.rstrip()+'\n',encoding='utf8')
fields=list(papers[0])
with (ROOT/'papers.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for r in papers:w.writerow({**r,'authors':'; '.join(r['authors'])})
def esc(s):return str(s).replace('&',r'\&').replace('%',r'\%').replace('_',r'\_').replace('#',r'\#')
bib=['% Metadata-based citation drafts. Verify official publisher BibTeX before submission.\n']
for r in papers:
    # Use misc to avoid inventing volume/pages/DOI or claiming unverified proceedings metadata.
    key=re.sub(r'[^A-Za-z0-9]','',r['id'])+str(r['year'])
    lines=[f'@misc{{{key},',f'  title = {{{{{esc(r["title"])}}}}},',f'  author = {{{" and ".join(esc(a) for a in r["authors"])}}},',f'  year = {{{r["year"]}}},',f'  howpublished = {{{esc(r["venue"])}}},',f'  url = {{{r["publication_url"] or r["paper_url"]}}}']
    bib.append('\n'.join(lines)+'\n}\n')
(ROOT/'references.bib').write_text('\n'.join(bib),encoding='utf8')
errors=[]
def unique(field):
    values=[re.sub(r'\W','',str(r[field])).casefold() for r in papers]
    if len(values)!=len(set(values)):errors.append('duplicate '+field)
for f in ['id','title','paper_url']:unique(f)
for r in papers:
    for f in ['authors','title','year','category','paper_url','publication_evidence_url','summary_zh','verified_on']:
        if not r.get(f):errors.append(r['id']+': missing '+f)
    if not 2015<=r['year']<=as_of.year:errors.append(r['id']+': year outside catalogue')
    for f in ['paper_url','publication_url','code_url','publication_evidence_url']:
        if r[f] and not r[f].startswith('https://'):errors.append(r['id']+': malformed '+f)
    if r['category'] not in cats:errors.append(r['id']+': unknown category')
    if r['venue']=='arXiv' and '预印本' not in r['publication_status']:errors.append(r['id']+': status mismatch')
    if len(re.findall('id="'+re.escape(anchor(r))+'"',body))!=1:errors.append(r['id']+': anchor count')
    if len(re.findall('id="'+re.escape(anchor(r))+'"',body_en))!=1:errors.append(r['id']+': English anchor count')
if body.count('<a id="paper-')!=len(papers):errors.append('README record count')
if body_en.count('<a id="paper-')!=len(papers):errors.append('English README record count')
with (ROOT/'papers.csv').open(encoding='utf-8-sig',newline='') as f:
    csvrows=list(csv.DictReader(f))
if len(csvrows)!=len(papers):errors.append('CSV count')
for a,b in zip(papers,csvrows):
    if a['title']!=b['title'] or str(a['year'])!=b['year']:errors.append('CSV content mismatch '+a['id'])
result={'checked_on':as_of.isoformat(),'records':len(papers),'categories':len(cats),'year_counts':dict(sorted(collections.Counter(r['year'] for r in papers).items())),'category_counts':dict(counts),'repository_verified_paper_count':nrepo,'preprint_record_count':npre,'related_count':sum(r['scope']=='related' for r in papers),'structure_checks_passed':not errors,'errors':errors,'limits':'Metadata, deduplication and export consistency checked. No training runs. Link retrieval evidence is described in SEARCH_NOTES.md; no claim that all remote links remain accessible.'}
(ROOT/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
