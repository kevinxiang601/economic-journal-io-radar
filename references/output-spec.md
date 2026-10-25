# Screening, scoring, and Markdown contract

## Inclusion boundary

Core topics include competition and conduct, tacit or algorithmic collusion, pricing and price discrimination, mergers, entry and exit, vertical relations, contracts, platforms and two-sided markets, ranking and recommendation, data and privacy, AI and IO, auctions, and mechanism or information design with a direct market-competition application.

Traditional supply chains and production networks are lower priority, not a coequal primary track. Conventional networks, firm-to-firm trade, global value chains, disruption/resilience, and inventory/capacity coordination without a direct core-IO or substantive AI mechanism have topic <=23/35 and at most three stars; retain only for specific transferable research content. High-priority supply-chain intersections concern AI agents, information, strategic procurement/contracts, market power, platform intermediation, or AI/compute supply markets, with the mechanism actually demonstrated. Pure optimization/operations algorithms and transport-led papers have topic <=17/35, at most two stars, and are normally excluded; a rare direct methodological borrowing can enter optional observation only. Neither a game-theory method, econometric method nor an AI/environmental label lifts these purpose-based caps. Follow `scoring.md` for the boundary between a transportation setting and transportation as the research objective.

Environmental economics is a separate eligible direction in AER, JPE, QJE, Econometrica, and ReStud: climate damages/adaptation, pollution and externalities, carbon taxes/trading, environmental regulation, conservation/resources, energy transition, and green innovation. No IO or supply-chain link is required for this Top 5 track. Environmental intersections with competition, pricing, contracts, procurement, production networks, platforms, and green technology qualify across all eight journals, and in NBER under its own window. Mere use of an energy industry dataset or the word green is not sufficient. Do not add specialist environmental journals without a user request.

Empirical work belongs in the main list when its question directly matches an eligible direction or its structural/identification design is clearly reusable for that direction. Environmental health or climate-macro work is eligible when environment is central, despite the generic field exclusions. Unrelated management, labor, health, macro, finance, or trade papers do not qualify merely because of journal prestige.

## Auditable score

Read [scoring.md](scoring.md) completely and use v2: topic 35, method 45, anchor 10, extension 10. Give game-theoretic modeling the highest methodological priority, followed by structural IO and credible DID/RD(RDD)/DDD/IV/RCT designs. Method names alone do not earn points. Main questions in monetary/macro/finance with only incidental oligopoly or pricing language cannot receive high relevance scores.

Apply topic/method gates before assigning stars, using `scripts/score_paper.py`; the final score may be capped below the raw sum. Five stars require final >=85, topic >=28 and method >=36; four stars require final >=70, topic >=24 and method >=28; three stars require final >=55, topic >=18 and method >=20. Two-star records are optional observations, not a quota. No author-prestige, journal-prestige, or complexity bonus.

Environmental economics remains secondary: retain only closely relevant four/five-star papers with topic >=31/35, method >=28/45 and final >=70. Lower-rated or weakly related environmental candidates are aggregate exclusions, never main/observation/cumulative entries. Do not inflate scores to pass thresholds.

## File structure

```markdown
# 经济学顶刊速览 — 方向筛选版（YYYY-MM-DD）

- **运行窗口**：...
- **收录口径**：官方首次上线即收录；后续卷期更新不重复收录
- **评分口径**：v2（议题35／方法45／锚点10／延伸10；执行议题与方法门槛）

## AER（American Economic Review）

**1.** Authors (YYYY-MM). **Title. Journal, publication status.**
- DOI：[doi](https://doi.org/...)
- 方向：... ｜ 方法：结构IO ｜ 贴合度：★★★★（总分 83/100：议题 29/35，方法 37/45，锚点 9/10，延伸 8/10；具体模型、识别和反事实的借鉴价值）
- Abstract：作者完整摘要的中文翻译。逐句对应原文、保持原句顺序和全部信息；术语应按语境自然意译，必要时用括号做一句话解释，不能机械直译。
- 直白解释：固定三句话。第一句说现实问题；第二句说怎么做和发现什么；第三句说为什么值得用户读。
- 官方来源：[Publisher abstract](...)

## 2星观察区

- **Journal — Authors (date). Title.** DOI/link。为何相关、为何暂不进入主清单。

## 已收录清单（累计）

1. Title ｜ Journal ｜ DOI 或 `DOI暂缺` ｜ 首次收录 YYYY-MM-DD ｜ 当前状态
```

NBER entries additionally include one concise field before Abstract: `- 入选依据：直接议题｜具体问题和机制` or `- 入选依据：方法或视角贡献｜原文支持的具体贡献及用途`. For a three-star NBER entry, use the contribution route and demonstrate the insight/design and research use. Neither research-domain labels nor generic transfer claims are sufficient. Keep official sources last.

The finished digest is a reading document, not a run report. After the papers, keep only a genuinely useful optional observation section and the cumulative inclusion list needed for future deduplication. Use the exact heading `## 2星观察区` only when there are retained observations; omit it when empty. Do not append coverage tables, candidate/exclusion totals, channel-by-channel status, RSS/CLI logs, download-failure inventories, generic conclusions, or a completion report. Do not create another user-facing audit/download file instead.

Maintain coverage, channel differences, unresolved candidates, exclusions and continuation checkpoints internally in the task's existing notes or working data; examine all eight journals and NBER even when no details appear in the digest. Keep the cumulative list with stable DOI/NBER IDs, normalized title, first inclusion date, publication status and known cross-version links. Do not add rejected or unverified candidates to that list. A material unresolved verification limit may warrant one short note in the affected journal/paper; preserve it when it changes how a reader should interpret a claim, rather than displaying process detail by default.

Order journal sections AER/JPE/QJE/JET/IIO/RAND J/Econometrica/ReStud, then NBER, optional observation, and cumulative records. Within each journal, order by stars, final score, and first-online date descending. Use `Online First` or `Articles in Press` when volume/issue/pages are not yet assigned. A zero-result section needs at most `本期无新增。`, without a search narrative; an all-zero report can simply state no new eligible papers and retain the cumulative list.

Match all coauthors against the configured laureate roster when supplied. Bold matching names only, leaving other authors unbolded. Example: `**1.** **Daron Acemoglu**, Coauthor (YYYY-MM). **Title. JPE, Ahead of Print.（已下载）**`. Do not bold the entire author list or add an award label or separate laureate section. Selection and scoring depend on relevance and method, not awards.

Append `（环境）` to every retained four- or five-star title selected through the environmental direction, both standalone and close intersection papers. Place download status after it: `**Title. Journal, status.（环境）（已下载）**`. Preserve `（环境）` in cumulative records. No environmental papers enter the observation section. Do not create a separate environmental report or duplicate one study across directions. The DOI and normalized title used for deduplication exclude presentation markers.

Each paper has only one abstract presentation, labeled exactly `Abstract：`. Translate the complete author abstract into Chinese sentence by sentence, retain the original sentence order, and preserve all reported methods, qualifications, directions, and numerical results. Prefer idiomatic accuracy over word-for-word translation when a literal rendering would confuse a non-specialist, but do not add claims absent from the source. Do not place an English abstract beside it. Search the public abstract aggressively even when the full article is paywalled; a paywalled PDF does not imply a missing abstract. Use `Abstract：摘要暂缺` only after the publisher, DOI metadata, Crossref, author manuscript, institutional repository, RePEc/SSRN, and exact-title search all fail; keep the attempted channels in internal notes. `官方来源` is always the last bullet in the paper block.

For the first Codex run, add `## 历史漏检补录` if older online-first papers are newly discovered. Do not relabel them as this week's new publications.

## Paper download handoff

Use a dated subfolder under the configured paper directory (see `configuration.md`).
If the main list contains at most 10 four- and five-star papers in total, target both star levels; otherwise target only five-star papers. After a full PDF is downloaded and validated, append `（已下载）` to that paper's bold title in the same day's digest. Do not create a separate download list or manifest. A missing marker means no validated PDF was saved in that run; do not mark a paper based on an abstract page, HTML page, failed request, or unverified file.

Validation requires PDF file identification, a nonzero page count, and a title check from document metadata or first-page text. Do not retain partial downloads, login pages, CAPTCHA pages, or publisher error pages. The marker is added only after all validation checks pass.
