"""Check generated catalog parity, canonical identifiers, and local Markdown links."""
import csv
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
papers = json.loads((ROOT / 'papers.json').read_text(encoding='utf-8'))
cats = json.loads((ROOT / 'categories.json').read_text(encoding='utf-8'))
errors = []
seen = defaultdict(set)
for row in papers:
    keys = [('id', row['id'].casefold()), ('title', re.sub(r'\W', '', row['title']).casefold())]
    # Repeated occurrences within one record are evidence links, not duplicates.
    urls = ' '.join(str(v) for k, v in row.items() if k.endswith('_url'))
    keys += [('doi', m.casefold().rstrip('.,)')) for m in re.findall(r'10\.\d{4,9}/[^\s?#]+', urls)]
    keys += [('arxiv', m) for m in re.findall(r'arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?', urls)]
    for kind, value in set(keys):
        seen[(kind, value)].add(row['id'])
    if not row.get('summary_en') or bool(row['notes']) != bool(row.get('notes_en')):
        errors.append('missing bilingual content: ' + row['id'])
for key, owners in seen.items():
    if len(owners) > 1:
        errors.append(f'duplicate {key}: {sorted(owners)}')

def paper_ids(text): return re.findall(r'<a id="paper-([^"]+)"></a>', text)
expected = [p['id'].lower() for p in papers]
for name in ['README.md', 'README.en.md']:
    if paper_ids((ROOT / name).read_text(encoding='utf-8')) != expected:
        errors.append('record ordering/count mismatch: ' + name)
for cat in cats:
    wanted = [p['id'].lower() for p in papers if p['category'] == cat]
    for suffix in ['.md', '.en.md']:
        path = ROOT / 'topics' / (cat + suffix)
        if not path.exists() or paper_ids(path.read_text(encoding='utf-8')) != wanted:
            errors.append('topic mismatch: ' + str(path.relative_to(ROOT)))
with (ROOT / 'papers.csv').open(encoding='utf-8-sig', newline='') as stream:
    rows = list(csv.DictReader(stream))
if len(rows) != len(papers): errors.append('CSV count')
for a, b in zip(papers, rows):
    for key, value in a.items():
        normalized = '; '.join(value) if key == 'authors' else ('' if value is None else str(value))
        if normalized != b[key]: errors.append(f'CSV mismatch: {a["id"]} / {key}')
if len(re.findall(r'^@misc\{', (ROOT / 'references.bib').read_text(encoding='utf-8'), re.M)) != len(papers):
    errors.append('BibTeX count')

link_count = 0
for path in ROOT.rglob('*.md'):
    if '.git' in path.parts: continue
    text = path.read_text(encoding='utf-8')
    for destination in re.findall(r'\]\(([^\s)]+)\)', text):
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc: continue
        target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        link_count += 1
        if not target.exists():
            errors.append(f'missing link: {path.relative_to(ROOT)} -> {destination}')
        elif parsed.fragment and target.suffix == '.md':
            content = target.read_text(encoding='utf-8')
            ids = set(re.findall(r'<a id="([^"]+)"', content))
            for title in re.findall(r'^#{1,6}\s+(.+)$', content, re.M):
                ids.add(re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-'))
            if unquote(parsed.fragment) not in ids:
                errors.append(f'missing anchor: {path.relative_to(ROOT)} -> {destination}')
print(json.dumps({'records': len(papers), 'topic_pages': len(cats)*2, 'internal_links_checked': link_count,
                  'passed': not errors, 'errors': errors}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
