# 贡献规范

感谢补充或纠正与时空序列预测直接相关的论文。

现有整理与维护贡献见 [CONTRIBUTORS.md](CONTRIBUTORS.md)。每周增量更新按 [MONITORING.md](MONITORING.md) 执行，记录在 [updates/README.md](updates/README.md)。

1. 在 `papers.json` 添加或修改记录，再执行下方“生成与提交前检查”的全部步骤。不要分别手工编辑多个派生清单。
2. 提供完整标题、作者、正式发表年/预印本首发年、会议/期刊或预印本状态、稳定论文 URL、主分类和中英文方法定位（`summary_zh` / `summary_en`）。版本/使用说明同时维护 `notes` / `notes_en`，无说明时两者均为空字符串。英文翻译保持相同证据范围，不增加未经核验的主张。
3. 以 DOI/arXiv 标识符和完整标题去重。会议版与扩展版仅在内容有实质区别且清楚说明版本关系时分列。
4. 代码链接需要论文或作者项目页的关联证据。第三方复现须单独注明，不得称为官方代码。空仓库、仅占位、不可访问和匿名仓库需要如实标记。
5. 只转述已检查的摘要、论文或作者说明。不要未经统一协议核对就写“SOTA”“全面超过”或建立跨论文性能排名。
6. 保留原论文、代码、数据的许可证。不要提交无权转载的全文 PDF 或数据集。
7. 更新 `verified_on`，记录访问失败和版本冲突，不把“未找到”写成“不存在”。

## 条目最小结构

```json
{
  "id": "ModelName",
  "title": "Exact Paper Title",
  "authors": ["Family, Given"],
  "year": 2026,
  "arxiv_first_year": 2025,
  "venue": "Conference or Journal / arXiv",
  "publication_status": "已发表或已录用（主源/作者声明）",
  "paper_url": "https://...",
  "publication_evidence_url": "https://...",
  "category": "graph",
  "summary_zh": "一句方法与任务定位。",
  "summary_en": "A short description of the method and task.",
  "notes": "",
  "notes_en": "",
  "code_url": "",
  "code_status": "未核验到作者代码",
  "verified_on": "2026-11-04"
}
```

完整字段以现有记录为准。`references.bib` 是元数据引用草稿；正式投稿时优先使用出版者提供的 BibTeX，补全卷、期、页和 DOI。

中英文 README 由同一脚本生成。新增主题或代码状态时，同时更新 `scripts/readme_en.py` 中的英文映射；缺失翻译会使生成失败。README 顶部保留双向语言切换链接。

## 生成与提交前检查

从仓库根目录依次运行（Python 3，仅使用标准库）：

```bash
python scripts/build_catalog.py
python scripts/verify_catalog.py
git diff --check
git status --short
```

第一步重新生成派生清单和 `verification.json`；第二步额外检查 DOI、无版本号 arXiv ID 去重、CSV 全字段、中英文条目顺序、专题页及本地链接/锚点。生成成功不能代替独立验证。所有命令成功后审阅差异，再提交源数据、派生文件和更新报告；`git status` 用于确认没有遗漏或无关文件。这些检查不等于外部链接全部可访问，也不等于训练复现成功。
