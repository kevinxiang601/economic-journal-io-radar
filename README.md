# Economic Journal IO & Environment Radar

一个面向产业组织、供应链、平台经济与环境经济学的 Codex 文献追踪技能。输出逐篇核验、历史去重的中文 Markdown 速览，支持完整逐句中文摘要、四维评星、诺奖作者姓名强调与已下载标记。

## 范围

- 原七刊：AER、JPE、QJE、JET、IIO、RAND Journal of Economics、Econometrica。
- 补充 ReStud（Review of Economic Studies）的环境方向，使独立环境研究覆盖完整经济学 Top 5：AER、JPE、QJE、Econometrica、ReStud。
- 环境与 IO、供应链、平台交叉论文覆盖全部八刊。独立环境研究不要求额外命中 IO，也不会因此被压低星级。
- NBER Working Papers：本周及紧邻上周首次发布的 IO、供应链、平台、marketing 与环境交叉研究；与期刊版跨版本去重。

期刊采用 45 天滚动窗口、首次正式上线口径，交叉检查 Crossref、官方 TOC/在线优先目录、OpenAlex/RePEc 和可用官方 RSS。RSS 与出版社网页同源，不充当两个独立渠道。元数据冲突和访问限制写入覆盖审计。

## 输出

按期刊分类、星级降序，每篇包括作者、发表状态、DOI、四维分数、完整中文摘要、三句话通俗解释和末尾来源链接。环境方向标题带 `（环境）`，验证下载成功后带 `（环境）（已下载）`。3–5 星进入主清单，2 星进入观察区；不凑数量。

评分：议题 40 分、方法 25 分、文献锚点 20 分、研究延伸 15 分。环境方向可依自身研究问题与理论、结构模型或因果设计得到高分，不因期刊名或作者获奖自动加分。

## 安装与使用

将本仓库克隆到个人技能目录：

```sh
git clone https://github.com/kevinxiang601/economic-journal-io-radar.git ~/.codex/skills/economic-journal-io-radar
```

目录已存在时，先保留原有本地配置，再合并更新。默认输出到任务目录的 `digests/` 和 `papers/`。可创建 `references/configuration.local.md`，填写自己的速览目录、论文目录、可选诺奖名单路径和时区；该文件不会提交到 Git。

在 Codex 中调用：

```text
使用 $economic-journal-io-radar 执行本周文献速览。
```

辅助检索与检查：

```sh
python3 scripts/collect_candidates.py --history-dir ./digests --lookback 45 --as-of YYYY-MM-DD --openalex --output /tmp/radar-candidates.json
python3 scripts/audit_digest.py ./digests/经济学顶刊速览-YYYY-MM-DD.md
```

脚本负责候选发现、提示与格式检查，研究筛选、摘要核验和评分仍需 Codex 结合原始来源判断。NBER/RSS 的补查流程见 `references/nber-rss.md`。

本仓库仅包含技能、参考规则和辅助脚本；不包含个人论文、速览历史、个人路径配置或计划任务状态。周计划请在自己的 Codex 中创建并指定输出目录；本地执行需要电脑和应用可用。全文仅从合法公开来源下载。
