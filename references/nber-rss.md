# NBER and RSS discovery

Preserve these channels alongside the journal workflow.

## NBER

Read the current NBER-CLI instructions at https://raw.githubusercontent.com/SepineTam/nber-cli/master/plugins/nber-cli/skills/NBER-CLI/SKILL.md before using that CLI. Fetch the entire current feed with `uvx nber-cli feed fetch --display-all true --format json`, without a max-items cutoff. Inspect the actual output schema (`results` or `items`) rather than assuming it. Verify retained records using `uvx nber-cli info PAPER_ID --all --refresh --format json` and NBER's official paper pages and New This Week inventory. If the CLI is unavailable, use the official inventories and disclose the fallback.

Use Asia/Shanghai dates: first publications in the current calendar week (Monday through run date), extending at most to the immediately preceding Monday–Sunday week. A Monday-morning run may precede the new US release; state this and inspect the previous week. Use official dated search or historical weekly inventories, following pagination when the feed omits the preceding week. Do not confuse revision dates, RSS timestamps, or cache first-seen dates with first release.

Include IO, supply chains, platforms, and marketing (demand, consumer choice, ads, brands, retail, channels) with strong theoretical or empirical relevance; their main-list threshold remains 3–5 stars. Environmental intersections are a secondary search: retain only closely connected four- or five-star papers with total at least 70 and environmental topic fit at least 35/40; mark them `（环境）`. Exclude environmental one- to three-star papers from both main and observation lists, counting exclusions only in aggregate. Standalone environmental inclusion without such a link is reserved for the Top 5 journal track. Never inflate ratings to meet a threshold.

Place `## NBER Working Papers（本周／上周新发布）` after all journal sections and before `## 2星观察区`, even for zero additions. Clearly label working-paper status; supply the NBER number, first release date, official link, and DOI or `DOI暂缺`. Preserve the full source-order Chinese abstract, three-sentence explanation, and sources last. Add NBER coverage counts to the existing audit.

Deduplicate all prior main lists, observation sections, cumulative lists, configured research digests, and existing paper filenames; optionally read Zotero only when needed. Match NBER ID and DOI, then normalized title/author combinations, and inspect published-version links or author pages for renamed versions. Different DOIs do not make different studies. Prefer a verified journal version when discovered simultaneously. A previously introduced working paper or published version is not a new entry; record the version link in the audit/cumulative record. Unintroduced pending candidates can be included once verified. CLI cache state is never the historical inclusion ledger.

## Publisher RSS

Discover official Latest Issue and Advance/Early View/In Press feed URLs from publisher subscription links; validate XML, journal identity, entries, and dates. Do not invent URLs or substitute research-highlight/citation alerts for journal inventories. Union feed results with official TOCs and registries, and investigate differences. Publisher RSS and the publisher website are the same source, not two independent channels. Unavailable, delayed, or short feeds require fallback to the normal workflow and disclosure in the audit, not a zero-paper conclusion. Follow the same rules for ReStud. Crossref discovery must consider both DOI creation and online-publication dates.

Record validated checkpoints in the task's continuation notes if a run is interrupted. Resume verified work instead of repeating searches and downloads. Never publish these notes with the skill.
