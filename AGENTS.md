# Catalog maintenance

- Read `MONITORING.md` and `CONTRIBUTING.md` before changing the catalog.
- `papers.json` is the source of paper records. Keep Chinese and English summaries and notes aligned, then run `python scripts/build_catalog.py`.
- Verify metadata against primary sources. Official code requires a paper/author-to-repository link and inspection of actual source files and usage instructions. An accessible repository is not a reproduction result.
- Deduplicate DOI, versionless arXiv IDs, normalized full titles, and version relationships. Distinguish recent publications from historical backfills and revisions.
- Record additions, changes, exclusions, verification limits, and the actual search window in a dated `updates/` report. Advance the successful-search cutoff only after a complete scan.
- The recurring maintenance workflow must not call a paid OpenAI API or read/decrypt its credentials. A future API invocation requires a new explicit, direct maintainer instruction for that task; a scheduled run is not such an instruction.
- Never commit credentials, private state, machine paths, chat logs, downloaded full texts, or API response caches.
- Preserve other contributors' work, avoid force pushes, and verify the remote commit after an authorized push.
