---
name: economic-journal-io-radar
description: "Track eight economics journals and NBER working papers with priority on IO, platforms, algorithmic competition, and AI intersections including AI and supply chains. Traditional supply networks are lower priority; optimization and transport-led papers are excluded or low relevance. Includes a selective environmental track, Chinese abstracts, audited ratings, historical deduplication, and verified PDF markers."
---

# Economic Journal IO Radar

Produce the weekly eight-journal radar plus NBER working papers. Read
[references/configuration.md](references/configuration.md) for output paths and optional local overrides.
Treat older WorkBuddy material only as history and visual reference; do not invoke or inherit its search logic.

Research priority: IO, platforms, algorithmic pricing/collusion, and substantive AI intersections come first. AI and supply chains qualify when AI changes strategic interaction, information, contracts, market structure, or firm behavior; conventional supply/production networks are lower priority, not a coequal primary track. Optimization/operations algorithms and transport-led research are normally excluded. Apply the explicit relevance caps in `references/scoring.md`, including when such papers contain game theory or causal econometrics.

## Required workflow

1. Read [references/sources.md](references/sources.md) and [references/output-spec.md](references/output-spec.md) completely.
2. Read every existing `经济学顶刊速览-*.md` in the output directory before drafting. Build the historical set before screening, not afterward.
   - When a laureate roster is configured, read it each run and extract the names from its overview table. Allow initials, omitted middle initials, accents, and name variants; verify identity rather than matching a surname alone.
3. Create a temporary candidate manifest with `scripts/collect_candidates.py`:
   - use `--lookback 120 --openalex` for the first Codex migration run;
   - use `--lookback 45 --openalex` afterward;
   - keep the manifest temporary. Do not leave JSON or CSV files in the output directory.
4. For every journal, open its official current/online-first page and at least one independent structured channel. Compare candidate sets and investigate differences. Search snippets, social posts, WeChat, and Xiaohongshu are discovery leads only.
   - Add a laureate-author omission check within the configured journals and 45-day window. Pay particular attention to Jean Tirole, Philippe Aghion, Daron Acemoglu, and other listed laureates publishing relevant work. Check official publication pages and exact-author journal searches, including non-first authors. Author pages are discovery channels; verify journal publication. Laureate status is not an inclusion or score bonus.
   - Screen standalone environmental economics in all five general-interest Top 5 journals: AER, JPE, QJE, Econometrica, and ReStud (Review of Economic Studies). Screen environmental intersections with IO, supply chains, and platforms in all eight journals. ReStud is newly added for environmental coverage; do not expand its non-environmental coverage by default. Use climate, pollution, emissions, carbon pricing, energy transition, environmental regulation, green innovation, conservation, adaptation, and resource-economics searches as omission checks, not automatic inclusion filters. On the first expanded run, apply the existing 45-day window to the newly eligible topics, without changing historical reports.
   - Read [references/nber-rss.md](references/nber-rss.md) for the NBER window, selective two-route admission, cross-version deduplication, and publisher RSS checks. Retain direct topic matches or concrete IO/game-theory/consumer-demand method or perspective contributions, including useful insights from other policy domains. Prefer four/five stars; selected three-star NBER papers require explicit contribution evidence. Generic keyword overlap or "could be transferred" language is insufficient. Do not fill the observation section with rejects.
5. Open the official DOI or article page for every retained paper. Confirm title, authors, first-online date, publication status, and abstract before writing. If the official page is inaccessible, require DOI metadata plus another structured source and disclose the limitation.
6. Read [references/scoring.md](references/scoring.md) and use scoring v2: topic 35, method 45, anchor 10, extension 10. Prioritize game-theoretic models, structural IO, and credible causal designs such as DID, RD/RDD, DDD, IV, and RCT. Verify the actual model/identification, not a method keyword. Apply the topic/method gates with `scripts/score_paper.py`; incidental oligopoly/pricing in a monetary or macro paper cannot earn four/five stars. State concrete reasons and do not fill a quota. New reports use v2; leave historic scores intact.
7. Write or update the same-day Markdown file using the output specification. Never create a revision-suffixed duplicate.
8. Run `scripts/audit_digest.py <absolute-markdown-path>` and fix all reported errors before completion.
9. Download the most relevant papers into
   the configured paper directory's `YYYY-MM-DD/` subfolder:
   - count all journal and NBER main-list papers together, including environmental entries; download all four- and five-star papers when their combined count is at most 10;
   - when it exceeds 10, download only five-star papers;
   - use publisher open access, author pages, recognized preprint servers, or institutional repositories; never bypass a paywall or access control;
   - validate that every retained download is a readable PDF and matches the paper title;
   - after a PDF passes validation, append `（已下载）` to that paper's bold title in the same day's top-journal digest. Do not create a separate download list or manifest. A title without this marker means that no validated PDF was saved for that run;
   - keep the parent directory organized only by date folders. Move pre-existing loose files into a date folder only when file creation time or an existing dated record establishes the date; otherwise put them in `日期待确认` and explain the uncertainty.

## Non-negotiable rules

- First official online appearance counts as new. Later assignment to a volume or issue updates metadata but is not a new paper.
- Deduplicate by normalized DOI first, then normalized title plus first author. Preserve the cumulative historical list.
- For primary IO/platform/AI directions, main sections contain 3–5 star papers after v2 gates. Conventional supply/network papers lacking a direct core mechanism have topic <=23 (at most three stars), and enter only for specific transferable research value. Optimization/transport-led papers have topic <=17 (at most two stars), default exclusion, with rare optional observation only for direct reusable content. These caps also apply to AI-branded versions of the same non-strategic problems. Environmental economics stays secondary: retain only closely relevant four/five-star papers (final>=70, environmental topic>=31/35, method>=28/45); exclude lower-rated environmental records from main/observation. An environmental label cannot override optimization/transport exclusions. Never inflate scores or fill a quota.
- Append `（环境）` to each title retained through the environmental track, whether standalone environmental research or a close intersection with IO/supply chains/platforms. If downloaded, use `（环境）（已下载）`. Preserve the environmental marker in cumulative records. An energy-sector setting alone does not qualify: environment must be central to the question, mechanism, policy, or outcome. Use the same four-dimensional scoring, full abstract, explanation, and download rules, subject to the stricter environmental inclusion threshold above.
- Use exactly one `Abstract：` field. It must be a complete Chinese rendering of the author's full abstract, covering every source sentence in the original order. Translate sentence by sentence faithfully, but use natural Chinese and explain or idiomatically render field-specific terms when a literal translation would be confusing. Do not include an English excerpt or a second abstract summary. A paywalled article normally still has a public abstract: if the publisher page is blocked, search DOI metadata, Crossref, an author manuscript, an institutional repository, RePEc, SSRN, and an exact-title web search before writing `Abstract：摘要暂缺`. Never reconstruct missing abstract content from a title or a secondary summary.
- Put `官方来源` as the final line of every paper entry, after the three-sentence plain-language explanation.
- In each retained paper's author list, bold only the names matching the supplied laureate roster. Keep the other author names in normal text, so the emphasis is visible. Do not add a Nobel label, award year, special section, or explanatory badge. See the heading format in `references/output-spec.md`.
- Internally account for all eight journals and NBER, channel differences, unresolved candidates, and continuation checkpoints. Keep these in existing task notes/working data rather than a user-facing report. After the papers, retain only useful optional observations and the cumulative inclusion list for deduplication. Omit coverage tables, counts, exclusion/download-failure lists and generic completion summaries; do not replace them with another user-facing audit file. A material uncertainty affecting a retained claim needs only a short local note. Search completeness requirements still apply even though the process is not narrated.
- If two channels disagree and the conflict cannot be resolved, mark the item pending verification instead of guessing.
- Never save an HTML error page with a `.pdf` suffix. Missing PDFs must remain missing; do not add the download marker unless a readable, title-matched PDF was actually saved.
