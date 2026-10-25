# Economics & UTD24 Management Research Radar

一个以产业组织、平台经济、算法竞争与AI交叉为重点的 Codex 文献追踪技能，支持经济学与管理学隔周轮换，也支持手动指定模式。传统供应链/生产网络为低优先级，环境经济学为精选次级方向。输出逐篇核验、跨系列去重的中文 Markdown 速览，包含完整逐句中文摘要、四维评星、研究机制评价、诺奖作者姓名强调与已下载标记。

## 范围

经济学不设篇数上限，管理学每期最多30篇，均以关联度、具体贡献与方法可借鉴性优先，发表时间作为次级取舍依据。管理学先扫描45天候选，可收窄主要窗口，但要回查略早的高关联论文，不用新近弱关联论文凑数量。

管理学严格限UTD24、24刊全部检查。除MS、Marketing Science、MSOM、POM、JM、JMR，还深入ISR、MISQ、Organization Science、SMJ、JCR、JOM等的相关研究；会计、金融等期刊同样扫描后按贡献筛选。完整名单与检索入口见[UTD24目录](references/management-journals.json)，流程见[管理学模式](references/management.md)。优先传统均衡博弈、合同与信息设计，以及DID、IV、RD/RDD、DDD、实验、清晰的结构IO；算法博弈与算法性能主导的工作通常排除，陌生估计方法本身为主要创新的工作降低方法适配分。管理学不纳入NBER或UTD24之外论文。

经济学范围如下：

- 原七刊：AER、JPE、QJE、JET、IIO、RAND Journal of Economics、Econometrica。
- 补充 ReStud（Review of Economic Studies）的环境方向，使独立环境研究覆盖完整经济学 Top 5：AER、JPE、QJE、Econometrica、ReStud。
- 环境与 IO、供应链、平台交叉论文覆盖全部八刊。独立环境研究不要求额外命中 IO，也不会因此被压低星级。
- NBER Working Papers：本周及紧邻上周首次发布的 IO、供应链、平台、marketing 与环境交叉研究；与期刊版跨版本去重。

选题优先IO、平台、AI/算法定价与合谋、生成式AI市场、AI改变采购/契约/议价、算力与模型供应市场等实质交叉。传统供应网络、库存协调、一般韧性或企业间贸易，若不直接研究核心IO或AI机制，议题最高23/35、评级最高三星，仅在有具体研究借鉴时保留。纯优化、运筹算法和交通为主的论文，默认排除，极少数有直接借鉴价值的最高二星观察；使用AI、博弈或DID本身不解除这些限制。

NBER采用精选的两条入选路径：直接命中研究主线，或在IO、博弈论、消费者需求的方法/视角上提供具体贡献。优先四、五星；三星必须写明实际贡献及具体用途。其他领域的好视角可以保留，例如区分收入支持对购买结构与总支出的影响；仅泛称“可以迁移”不足以入选，也不会用观察区堆积弱关联论文。

期刊采用 45 天滚动窗口、首次正式上线口径，交叉检查 Crossref、官方 TOC/在线优先目录、OpenAlex/RePEc 和可用官方 RSS。RSS 与出版社网页同源，不充当两个独立渠道。渠道对账、排除数量和恢复检查点内部记录；成品末尾仅保留有阅读价值的可选观察区和累计已收录清单，不附大段检索或执行汇报。

## 输出

开头仅保留运行窗口和发现与筛选。正文按期刊分类、星级与最终分降序，每篇包括作者、发表状态、DOI、方法类型、四维分数、完整中文摘要、三句话通俗解释、研究评价和末尾来源链接。研究评价可结合用户安装的`research-method-distiller`：理论解释真实基准、关键变量或制度如何改变激励与结论；实证解释识别或数据创意、经济发现和具体借鉴价值。评价以可核实原文为依据，不强行编造新增变量或反直觉结果。环境方向标题带 `（环境）`，验证下载成功后带 `（环境）（已下载）`。主要方向在议题与方法门槛通过后维持 3–5 星主清单，2 星为可选观察。环境仍是次级搜索，只收密切相关的四、五星论文（最终分至少70，环境议题至少31/35，方法至少28/45）；一至三星环境论文均不列正文或观察区。

评分v2：议题35分、方法45分、文献锚点10分、研究延伸10分。优先博弈论模型、structural IO，再重点考察可信的DID、RD/RDD、DDD、IV、RCT等因果设计。货币、宏观、金融等论文若仅借用寡头、价格或市场势力设定，不能靠方法复杂而评四五星；方法名称和期刊/作者声望均不自动加分。具体分档和硬上限见 [评分规则](references/scoring.md)。历史评分保留原口径。

写作检查可配合 `anti-defensive-writing`：直白解释和评级理由直接说明发现与价值，删去重复铺垫和无信息的限定；完整摘要保留原文全部信息和必要条件。

## 安装与使用

将本仓库克隆到个人技能目录：

```sh
git clone https://github.com/kevinxiang601/economic-journal-io-radar.git ~/.codex/skills/economic-journal-io-radar
```

目录已存在时，先保留原有本地配置，再合并更新。经济学默认输出到任务目录的 `digests/` 和 `papers/`，管理学为`management-digests/`和`management-papers/`。可创建 `references/configuration.local.md`，填写两类速览和论文目录、可选诺奖名单路径和时区；该文件不会提交到 Git。

在 Codex 中调用：

```text
使用 $economic-journal-io-radar 执行本周文献速览。
```

辅助检索与检查：

```sh
python3 scripts/collect_candidates.py --history-dir ./digests --history-dir ./management-digests --lookback 45 --as-of YYYY-MM-DD --openalex --output /tmp/radar-candidates.json
python3 scripts/audit_digest.py ./digests/经济学顶刊速览-YYYY-MM-DD.md
python3 scripts/collect_management.py --history-dir ./digests --history-dir ./management-digests --lookback 45 --as-of YYYY-MM-DD --openalex --output /tmp/management-candidates.json
python3 scripts/audit_digest.py ./management-digests/管理学顶刊速览-YYYY-MM-DD.md --candidates /tmp/management-candidates.json
python3 scripts/select_track.py --date YYYY-MM-DD --anchor 2026-10-26
```

脚本负责候选发现、提示与格式检查，研究筛选、摘要核验和评分仍需 Codex 结合原始来源判断。NBER/RSS 的补查流程见 `references/nber-rss.md`。

轮换按日历周计算：默认2026-10-26为经济学锚点，2026-11-02管理学，2026-11-09经济学。可用`--anchor`指定另一个经济学周一；手动测试和漏跑均不改变轮换顺序。本仓库仅包含技能、参考规则和辅助脚本；不包含个人论文、速览历史、个人路径配置或计划任务状态。周计划请在自己的 Codex 中创建并指定输出目录；本地执行需要电脑和应用可用。全文仅从合法公开来源下载。
