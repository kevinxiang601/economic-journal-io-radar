# Screening, scoring, and Markdown contract

## Inclusion boundary

Core topics include competition and conduct, tacit or algorithmic collusion, pricing and price discrimination, mergers, entry and exit, vertical relations, contracts, platforms and two-sided markets, ranking and recommendation, data and privacy, AI and IO, auctions, and mechanism or information design with a direct market-competition application.

Supply-chain topics include contracting, procurement and bargaining, production networks, firm-to-firm trade, global value chains, disruption and resilience, and industrial policy operating through supply chains.

Environmental economics is a separate eligible direction in AER, JPE, QJE, Econometrica, and ReStud: climate damages/adaptation, pollution and externalities, carbon taxes/trading, environmental regulation, conservation/resources, energy transition, and green innovation. No IO or supply-chain link is required for this Top 5 track. Environmental intersections with competition, pricing, contracts, procurement, production networks, platforms, and green technology qualify across all eight journals, and in NBER under its own window. Mere use of an energy industry dataset or the word green is not sufficient. Do not add specialist environmental journals without a user request.

Empirical work belongs in the main list when its question directly matches an eligible direction or its structural/identification design is clearly reusable for that direction. Environmental health or climate-macro work is eligible when environment is central, despite the generic field exclusions. Unrelated management, labor, health, macro, finance, or trade papers do not qualify merely because of journal prestige.

## Auditable score

Assign four integer subscores and show the total:

- topic fit: 0–40
- method fit: 0–25
- anchor value: 0–20
- research extensibility: 0–15

For the environmental track, score topic fit against environmental research itself (not just IO overlap). A central environmental policy, externality, resource allocation, or green-transition question can earn 35–40 topic points. Method fit: rigorous game-theoretic/structural mechanisms or strong causal designs tied to a clear mechanism can earn 20–25; credible reduced-form causal work 16–22; descriptive correlations usually at most 12. Anchor value and extensibility must have concrete reasons, not journal prestige. A standalone Top 5 environmental paper can earn five stars when its question and method strongly match and its total is at least 85; absence of IO content is not a rating cap. Do not promote an environmental intersection automatically: relevance and evidence still determine the score. Explain the specific environmental reading value in the same three-sentence explanation.

Map totals to stars:

- 85–100: five stars, only when topic and method are both strong
- 70–84: four stars, with at least one strong dimension
- 55–69: three stars
- 40–54: two stars, observation section only
- below 40: exclude and count in the audit

No target count or target star distribution is allowed.

Environmental economics is secondary to the original search directions. Retain only four- or five-star papers with total at least 70/100 AND environmental topic fit at least 35/40. Environment must be central, or its intersection with IO/supply chains/platforms must be substantively close. Exclude environmental papers scoring one to three stars, and weak environmental links even if their total reaches 70, from both the main list and observation section. Record only aggregate exclusions in the audit; do not list these papers individually or add them to the cumulative included list. Never raise ratings to keep a candidate. Other primary directions retain their existing inclusion thresholds.

## File structure

```markdown
# 经济学顶刊速览 — 方向筛选版（YYYY-MM-DD）

- **运行窗口**：...
- **发现与筛选**：共发现 N 篇；历史重复 N 篇；主清单 N 篇；观察区 N 篇；排除 N 篇
- **收录口径**：官方首次上线即收录；后续卷期更新不重复收录

## AER（American Economic Review）

**1.** Authors (YYYY-MM). **Title. Journal, publication status.**
- DOI：[doi](https://doi.org/...)
- 方向：... ｜ 贴合度：★★★★（总分 78/100：议题 34，方法 18，锚点 15，延伸 11；简短理由）
- Abstract：作者完整摘要的中文翻译。逐句对应原文、保持原句顺序和全部信息；术语应按语境自然意译，必要时用括号做一句话解释，不能机械直译。
- 直白解释：固定三句话。第一句说现实问题；第二句说怎么做和发现什么；第三句说为什么值得用户读。
- 官方来源：[Publisher abstract](...)

## 2星观察区

- **Journal — Authors (date). Title.** DOI/link。为何相关、为何暂不进入主清单。

## 覆盖审计

| 期刊 | Crossref | 官方卷期 | Online First | 第二交叉渠道 | 差异与处置 | 状态 |
|---|---:|---:|---:|---:|---|---|

## 已收录清单（累计）

1. Title ｜ Journal ｜ DOI 或 `DOI暂缺` ｜ 首次收录 YYYY-MM-DD ｜ 当前状态
```

Include all eight journals and NBER in the coverage audit even if a main section has zero additions. Order journal sections AER/JPE/QJE/JET/IIO/RAND J/Econometrica/ReStud, then NBER, then observation/audit/cumulative records. Within each journal, order by stars descending and then first-online date descending. Use `Online First` or `Articles in Press` when volume/issue/pages are not yet assigned.

Match all coauthors against the configured laureate roster when supplied. Bold matching names only, leaving other authors unbolded. Example: `**1.** **Daron Acemoglu**, Coauthor (YYYY-MM). **Title. JPE, Ahead of Print.（已下载）**`. Do not bold the entire author list or add an award label or separate laureate section. Selection and scoring depend on relevance and method, not awards.

Append `（环境）` to every retained four- or five-star title selected through the environmental direction, both standalone and close intersection papers. Place download status after it: `**Title. Journal, status.（环境）（已下载）**`. Preserve `（环境）` in cumulative records. No environmental papers enter the observation section. Do not create a separate environmental report or duplicate one study across directions. The DOI and normalized title used for deduplication exclude presentation markers.

Each paper has only one abstract presentation, labeled exactly `Abstract：`. Translate the complete author abstract into Chinese sentence by sentence, retain the original sentence order, and preserve all reported methods, qualifications, directions, and numerical results. Prefer idiomatic accuracy over word-for-word translation when a literal rendering would confuse a non-specialist, but do not add claims absent from the source. Do not place an English abstract beside it. Search the public abstract aggressively even when the full article is paywalled; a paywalled PDF does not imply a missing abstract. Use `Abstract：摘要暂缺` only after the publisher, DOI metadata, Crossref, author manuscript, institutional repository, RePEc/SSRN, and exact-title search all fail, and disclose the attempted channels in the coverage audit. `官方来源` is always the last bullet in the paper block.

For the first Codex run, add `## 历史漏检补录` if older online-first papers are newly discovered. Do not relabel them as this week's new publications.

## Paper download handoff

Use a dated subfolder under the configured paper directory (see `configuration.md`).
If the main list contains at most 10 four- and five-star papers in total, target both star levels; otherwise target only five-star papers. After a full PDF is downloaded and validated, append `（已下载）` to that paper's bold title in the same day's digest. Do not create a separate download list or manifest. A missing marker means no validated PDF was saved in that run; do not mark a paper based on an abstract page, HTML page, failed request, or unverified file.

Validation requires PDF file identification, a nonzero page count, and a title check from document metadata or first-page text. Do not retain partial downloads, login pages, CAPTCHA pages, or publisher error pages. The marker is added only after all validation checks pass.
