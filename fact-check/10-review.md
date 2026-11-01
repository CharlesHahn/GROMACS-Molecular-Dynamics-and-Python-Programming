# 第 10 章《自动化与工程化》章节验收报告（复验轮 · 第二轮）

- 复验时间：2026-10-29（约 13:00–13:30 CST）
- 复验者：对抗性验收（按 REVIEW.md 执行，不放松标准）
- 复验对象：第一轮返工后的 `10-自动化与工程化.md`、`refs/10-refs.md`、`fact-check/10-log.md`
- **复验结论：通过（合格）** —— 上轮 2 项 P0 全部消除，2 项 P1 全部修正并经实证复核；保留 4 项 P2 记录，统稿时处理。

---

## 一、上轮问题逐条复验

### P0-1　10.4.3「模式规则与自动变量」——Makefile 模式规则语义　【已消除】

- 位置：`10-自动化与工程化.md` 第 268 行（10.4.3 节末段）。
- 修订后文本：「`make` 对「同一目标有多条普通规则」按书写顺序取最后一条并打印错误信息，对「同一输出可由多个模式规则匹配」则按最短 stem 优先、书写顺序仅在同长度时作决胜——规则顺序本身不构成优先级[23]，这与 Snakemake 的歧义处理方式不同（见 10.4.4 节）。」
- 与要求表述逐分句一致：①同一目标多条普通规则按书写顺序取最后一条并打印错误信息；②同一输出多个模式规则匹配按最短 stem 优先；③书写顺序仅同长度作决胜；④规则顺序不构成优先级；⑤引用 **[23]（GNU Make Manual）** 而非 [24]。
- 实证核验（web_fetch，HTTP 200，通道：web_fetch 官方手册直连）：
  - GNU make 手册 §4.11（Multiple-Rules.html）："If more than one rule gives a recipe for the same file, `make` uses the **last one given and prints an error message**." —— 与首分句逐字吻合。
  - GNU make 手册 §10.5.4（Pattern-Match.html）："`make` will choose the rule with the **shortest stem** (that is, the pattern that matches most specifically). If more than one pattern rule has the shortest stem, `make` will choose the **first one found** in the makefile." —— 与「最短 stem 优先、同长度按书写顺序决胜、顺序不构成优先级」逐字吻合。
- **判定：P0-1 消除。**

### P0-2　引文 [5] Snakemake executor 文档 URL　【已消除】

- 修订后两处一致（正文第 572 行与 refs/10-refs.md 第 10 行）：`https://snakemake.readthedocs.io/en/stable/executing/executors.html`。
- 实证核验（双通道）：
  - web_fetch：**HTTP 200**，页面标题「Using executor plugins | Snakemake 9.27.1 documentation」，正文明示 "Snakemake offers an interface for so-called executor plugins (**as of version 8.0.0** and onward)" —— 与正文「其执行器接口自 8.0 起改为插件机制」断言一致。
  - anysearch extract：返回同一标题与同一段原文，二次确认链接有效。
- **判定：P0-2 消除。**

### P1-1　10.7.2 DataLad save/run 职责　【已修正】

- 位置：`10-自动化与工程化.md` 第 497 行，修订后文本：「`datalad run` 记录命令、输入输出与执行环境之间的关联并把这些信息写入历史，`datalad save` 仅记录当前文件状态变化，两者职责不同[22][35]」。
- 职责区分与上轮要求一致：`datalad run` = 记录命令与输入输出关联（及执行环境）并写入历史；`datalad save` = 仅记录文件状态变化；两者职责明确分开，不再将 save 误标为记录命令关联。
- **判定：P1-1 修正。**

### P1-2　10.4.5 版本区间断言　【已修正并实证】

- 位置：`10-自动化与工程化.md` 第 322 行，修订后文本：「该行为在本书基线（GROMACS 2026.x）及近几个主要版本（2021 起）的官方长期模拟指南中一致记录[3]」。
- 已删除「适用于 GROMACS 2021 及以后」式无出处断言，改为限定的基线表述：锚定本书基线版本，并把区间表述限定为「官方长期模拟指南一致记录」这一可核查的文档事实。
- 实证核验（web_fetch，HTTP 200）：GROMACS **2021 版**手册 managing-simulations 页与 **2026.4** 版在关键行为上逐字一致——"Appending will not work if any output files have been modified or removed after mdrun wrote them, because the checkpoint file maintains a checksum of each file"、`-noappend` 生成 ".partXXXX"、`-cpt` 周期检查点 + `_prev` 副本、convert-tpr/-extend、grompp -t、续算不重新生成速度并选 continuation。即「2021 起官方指南一致记录」的说法有据可依。
- **判定：P1-2 修正。**

---

## 二、实测数字表（复验轮，PowerShell 实测）

| 指标 | 要求 | 实测 | 判定 |
| --- | --- | --- | --- |
| 汉字数（STYLE 三.1 口径：排除 ``` 代码块与「## 参考文献」之后） | ≥10,000 | **11,841**（PowerShell 正则统计，脚本与 STYLE 三.2 示例一致） | 通过 |
| 二级节 | ≥8 | 13（内容节 7 + 结构节 6） | 通过 |
| 三级节 | ≥25 | 26 | 通过 |
| 表格 | ≥3 | 8（表 10-1～10-8，表题在表上方） | 通过 |
| 图 | ≥2 | 4 幅 Mermaid（图 10-1～10-4） | 通过 |
| 参考文献 | ≥30 | 35；正文上标 152 处，编号 1→35 连续、无跳号、无重号，文末列表逐条对应 | 通过 |
| 导言 | 300–600 字 | 502 | 通过 |
| 学习目标 | 4–6 条行为动词 | 6 条（能判断/能使用/能设计/能生成/能区分） | 通过 |
| 常见错误 | ≥6 条四段式 | 8 条 | 通过 |
| 习题 | ≥6 题、≥2 开放题 | 7 题，第 6、7 题为开放题 | 通过 |
| 禁用表达（STYLE 六.6/六.7） | 0 | 0（正文非代码块；grep 命中的 3 处「最后」均为描述性内容如「取最后一条」「最后一段进度」，非段落开头机械排列） | 通过 |
| 第二人称「你/您/我们」 | 禁止 | 0 | 通过 |
| `{{ }}` 残留（正文非代码块） | 0 | 0（16 处 `{{ }}` 全部位于 jinja/bash 代码块内：第 114–131 行 jinja 块、第 334–349 行 bash 块） | 通过 |
| 必备构件顺序 | 固定顺序 | 导言→学习目标→前置知识→正文→常见错误→小结→习题→参考文献，齐全且顺序正确 | 通过 |

统计命令（PowerShell，STYLE 三.2 原样）：
```powershell
$t = Get-Content -LiteralPath $f -Raw -Encoding UTF8
$t = [regex]::Replace($t, '(?s)```.*?```', '')
if ($t -match '(?s)## 参考文献.*$') { $t = $t.Substring(0, $t.IndexOf('## 参考文献')) }
$n = ([regex]::Matches($t, '[\u4e00-\u9fff]')).Count   # → 11841
```

---

## 三、随机抽查文献核验（复验轮，随机抽 3 条：[3][17][20]）

随机抽取方式：PowerShell `1..35 | Get-Random -Count 3`，本轮抽中 **[3]、[17]、[20]**。核验通道：web_fetch 官方直连（HTTP 200）；补充核验 [5]（P0-2 目标）采用 web_fetch + anysearch extract 双通道。

| 编号 | 文献 | 核验通道 | 核验结果 | 判定 |
| --- | --- | --- | --- | --- |
| [3] | GROMACS 2026.4 Managing long simulations | web_fetch | HTTP 200，标题「Managing long simulations - GROMACS 2026.4 documentation」；检查点 `-cpt` 周期与 `_prev` 重命名、默认追加、`-noappend`→`.partXXXX`、检查点校验和拒追、「grompp -t」+「不重新生成速度、选 continuation」、convert-tpr `-extend`、rsync 备份建议——与正文 10.4.5/10.5.4/10.7.2 全部一致 | 通过 |
| [17] | Jinja 文档 (3.1.x) | web_fetch | HTTP 200（跳转 /en/stable/），标题「Jinja — Jinja Documentation (3.1.x)」；官方原句 "Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document." 与正文 10.2.2 引文逐字吻合 | 通过 |
| [20] | GROMACS 2026.4 gmx check | web_fetch | HTTP 200，标题「gmx check - GROMACS 2026.4 documentation」；"The program can compare two run input (.tpr) files when both `-s1` and `-s2` are supplied" —— 与正文「用 gmx check 比较两个运行输入文件」一致 | 通过 |
| [5] | Snakemake Executor plugins（补充，非随机） | web_fetch + anysearch extract | 见 P0-2：双通道均打开，标题「Using executor plugins | Snakemake 9.27.1 documentation」 | 通过 |

随机 3 条全部可打开、标题与正文论断一致，**未发现伪造或错配文献**。

---

## 四、结论

- **结论：通过（pass）。** 上轮 2 项 P0（P0-1 make 模式规则语义、P0-2 引文 [5] URL）均已按上轮修改建议消除并经官方原文实证；2 项 P1（P1-1 datalad save/run 职责、P1-2 版本区间断言）均已修正，其中 P1-2 的「2021 起一致记录」已由 2021 版官方手册原文背书。机械项（字数 11,841 / 结构 / 文献 35 条编号连续）、语言项（无禁用表达、无第二人称、无 `{{}}` 残留）全部通过。
- 复核必做项均已执行：汉字数 PowerShell 实测（11841）；随机抽 3 条文献并注明通道；禁用表达与 `{{}}` 残留非代码块检查（均为 0）。

## 五、遗留 P2（记录，统稿时处理，不影响本轮判定）

1. **P2-1**　10.1.2/10.3.1：YODA 反例 `results_August19/` 仍未替换（正文第 47 行仍引 [11]）。上轮建议核对 F1000 海报原文（DOI 10.7490/f1000research.1116363.1）或改用可核实例子（如 `results_new_data/`）——本轮未再扩展核验，维持记录。
2. **P2-2**　表 10-2 `nsteps` 行出处仍标 `[15][16]`；mdp-options 页只给默认值，50000/250000 类推荐值出自教程惯例，建议改为 `[16]` 或注明「教程惯例」。
3. **P2-3**　表 10-5「依赖判定」行 Snakemake 侧仍写「输出存在性 + 可选内容校验」；内容校验非常态默认，建议收敛为「输出存在性 + 中断/不完整输出重跑（--rerun-incomplete）」。
4. **P2-4**　refs/10-refs.md 头注仍自认 squeue/sacct/sstat/git-lfs 四页未逐字 fetch（文档推定）；建议逐字核对后提升为「已核实」。

---

## 附：第一轮报告（2026-10-29 12:10，原样留存供追溯）

# 第 10 章《自动化与工程化》章节验收报告

- 验收时间：2026-10-29（核验时段约 12:10–12:40 CST）
- 验收者：对抗性验收（按 REVIEW.md 执行，不放松标准）
- 结论：**返工（不合格）**——存在 1 项 P0 事实性错误（Makefile 模式规则语义）未消除；另有 2 项 P1、若干 P2。返工范围见文末。

---

## 一、实测数字表（第一轮）

| 指标 | 要求 | 实测 | 判定 |
| --- | --- | --- | --- |
| 汉字数（STYLE 三.1 口径：排除 ``` 代码块与「## 参考文献」之后） | ≥10,000 | **11,787**（PowerShell 正则统计，脚本与 STYLE 示例一致） | 通过 |
| 二级节 | ≥8 | 13（含结构节 6：学习目标/前置知识/常见错误/小结/习题/参考文献；正文内容节 7） | 通过 |
| 三级节 | ≥25 | 26 | 通过 |
| 表格 | ≥3 | 8（表 10-1～10-8，编号连续，表题在表上方） | 通过 |
| 图 | ≥2 | 4 幅 Mermaid（图 10-1～10-4，图题在图下方） | 通过 |
| 参考文献 | ≥30 | 35（正文首次出现顺序严格 1→35，无跳号重号，文末列表逐条对应） | 通过 |
| 导言 | 300–600 字 | 502 | 通过 |
| 学习目标 | 4–6 条行为动词 | 6 条（能判断/能使用/能设计/能生成/能区分），无「了解/熟悉/掌握」 | 通过 |
| 前置知识 | 指明章节/文献 | 第 2/3/5/6/9 章 + 外部材料 | 通过 |
| 常见错误 | ≥6 条 | 8 条，均为「现象→成因→排查→处置」四段式 | 通过 |
| 习题 | ≥6 题，≥2 开放题 | 7 题，第 6、7 题为开放讨论题 | 通过 |
| 禁用表达（STYLE 六.6/六.7） | 0 | 0（正文非代码块） | 通过 |
| 第二人称「你」叙述 | 禁止 | 0 | 通过 |
| `{{ }}` 残留（正文非代码块） | 0 | 0（仅代码块/模板示例内合法出现） | 通过 |
| 跨章重复（02/03/09） | 无重复段落 | 25 字符粒度 0 段重合；与 05/06 章仅命中表格分隔符语法串，无实质重复 | 通过 |
| 编号体系 | 表/图/式/文献编号连续 | 表 10-1～8、图 10-1～4、文献 [1]–[35] 均连续 | 通过 |
| 必备构件顺序 | 固定顺序 | 齐全且顺序正确 | 通过 |

统计命令（PowerShell，STYLE 三.2 原样）：
```powershell
$t = Get-Content -LiteralPath $f -Raw -Encoding UTF8
$t = [regex]::Replace($t, '(?s)```.*?```', '')
if ($t -match '(?s)## 参考文献.*$') { $t = $t.Substring(0, $t.IndexOf('## 参考文献')) }
$n = ([regex]::Matches($t, '[\u4e00-\u9fff]')).Count   # → 11787
```

---

## 二、抽查文献清单与核验结果（第一轮，随机 8 条，编号：16,24,29,30,31,26,1,17）

核验通道：web_fetch 官方直连（manual.gromacs.org / slurm.schedmd.com / jinja.palletsprojects.com）+ Crossref API（api.crossref.org）+ anysearch（search/batch_search/extract）。六项 = 标题、作者、期刊/站点、年份、卷期页、DOI/URL。

| 编号 | 文献 | 核验结果 | 判定 |
| --- | --- | --- | --- |
| [1] | GROMACS 2026.4 gmx grompp 文档 | https://manual.gromacs.org/current/onlinehelp/gmx-grompp.html 打开，标题吻合；`-maxwarn`「Not for normal use and may generate unstable systems」、mdout.mdp「comment lines + the input that gmx grompp has read」、`-pp`、预处理器关键字、续算流程均逐字核对 | 通过 |
| [16] | Lemkul, LiveCoMS | Crossref：标题「From Proteins to Perturbed Hamiltonians…」、作者 Justin A. Lemkul、期刊 Living Journal of Computational Molecular Science、卷期页 1(1): 5068、DOI 10.33011/livecoms.1.1.5068 全吻合；年份：Crossref 记录 issued 2018-10-27、期刊期次 published-online 2019-01-09，2018/2019 两种标注并存，正文按 2019 并括注的处理成立 | 通过 |
| [17] | Jinja 文档 | https://jinja.palletsprojects.com/ 打开，标题「Jinja Documentation (3.1.x)」吻合；正文引文「fast, expressive, extensible templating engine…」逐字吻合 | 通过 |
| [24] | Snakemake documentation | https://snakemake.readthedocs.io/ 有效（当前 9.27.1）；正文所引 `--rerun-incomplete`、`--retries`、`--report`、`-n`、`--cores`、expand/wildcards 均见于 CLI 文档 | 通过 |
| [26] | gmx convert-tpr | 页面打开，标题吻合；`-extend` 语义（按 ps 延长运行时长）与正文一致 | 通过 |
| [29] | SchedMD sstat (26.05) | 页面打开，标题「sstat」吻合；「Display the status information of a running job/step」，字段含 AveCPU/MaxRSS/ConsumedEnergy，与正文「CPU、内存与能耗统计」一致 | 通过 |
| [30] | SchedMD sacct (26.05) | URL 返回 HTTP 200（页面含复杂 HTML，转换失败未能逐字比对正文；sstat 页 SEE ALSO 交叉引用 sacct）。该条原 log 已自注「文档推定」 | 通过（通道受限，见 P2-4） |
| [31] | McKinney, SciPy 2010 | Crossref：标题「Data Structures for Statistical Computing in Python」、作者 Wes McKinney、Proceedings of the 9th Python in Science Conference (Austin)、2010、页码 **56-61**、DOI 10.25080/Majora-92bf1922-00a 全吻合（refs 括注「个别二手库写 51-56，以 Crossref 为准」成立） | 通过 |

抽查 8 条全部可打开、六项信息一致，**未发现伪造或错配文献**。

关键论断对照官方文档的其余核验（不在 8 条内但正文引用）：
- 作业数组（SchedMD 26.05 job_array.html）：`--array=0-31/1,3,5,7/1-7:2`、`%N` 并发上限示例 `--array=0-15%4`、SLURM_ARRAY_JOB_ID/TASK_ID/TASK_COUNT/TASK_MIN/TASK_MAX、`%A`/`%a`（默认输出 slurm-%A_%a.out）、squeue 聚合显示 `1080_[5-1024]` 且运行中任务单列、scancel 按数组号取消全部——与正文表 10-6、10.5.2/10.5.3 全部一致。
- mdrun（2026.4 help）：`-cpt` 默认 15（分钟）、`-maxh` 在运行超过 `-maxh*0.99` 小时后终止、`-ntmpi`/`-ntomp`/`-gpu_id` 语义、检查点 `_prev` 备份、输出文件校验和与追加/`-noappend`（.partXXXX）——与正文 10.4.3/10.5.4 一致。
- Managing long simulations：检查点为唯一续算通道、convert-tpr -extend 延长、grompp -t 改参数、续算不重新生成速度并选 continuation、rsync 备份建议——与正文一致。
- mdp-options（2026.4）：「Default values are given in parentheses, or listed first among choices. The first option in the list is always the default option.」、coulombtype 默认 Cut-off、`define=-DPOSRES` 引入 posre.itp——与正文 10.2 一致。
- Snakemake 8.0 插件化：官方「Migrating to Snakemake 8」明示「All the execution backends have been moved into plugins」——正文断言正确。
- git-lfs（git-lfs.com）：「replaces large files … with text pointers inside Git, while storing the file contents on a remote server」——与正文一致。
- DataLad Handbook 6.2（现 URL basics/101-127-yoda.html）：YODA P1/P2/P3 原则、`datalad create -c yoda`、反例 `main_script_DONTUSE.py`——与正文一致。

---

## 三、逐节问题清单（第一轮，含原文摘录与修改建议）

### P0（判不合格依据）

**P0-1　10.4.3「模式规则与自动变量」节——Makefile 模式规则优先级论断与官方手册矛盾（事实性错误）**

- 位置：`10-自动化与工程化.md`，10.4.3 末句：
  「`make` 对「同一目标有多条规则」报错，对「同一输出可由多个模式匹配」则**按书写顺序取第一条，规则排序即优先级**，这与 Snakemake 的歧义处理方式不同（见 10.4.4 节）。」
- 官方依据：GNU make 手册 §10.5.4 How Patterns Match——「It is possible that more than one pattern rule will meet these criteria. In that case, make will choose the **rule with the shortest stem** (that is, the pattern that matches most specifically). If more than one pattern rule has the shortest stem, make will choose the first one found in the makefile.」即「书写顺序」只在多条规则 **stem 等长**时作为决胜条件，一般情形下优先级由**最短 stem** 决定，而非书写顺序。
- 同句第一分句亦不准确：§4.11 Multiple Rules for One Target——「If more than one rule gives a recipe for the same file, make uses the **last one given and prints an error message**.」即 make 打印错误信息后取最后一条 recipe 继续，并非中止报错。
- 修改建议：改为「`make` 在多个模式规则匹配同一目标时，选择 **stem 最短（匹配最具体）** 的规则；仅当多条规则 stem 等长时才取 makefile 中书写靠前的一条。多条显式规则同时给出 recipe 时，make 打印错误信息并采用最后一条。这一优先级规则与 Snakemake 的歧义处理（AmbiguousRuleException，要求规则间互斥或通配符约束）有实质差异。」

**P0-2　引文 [5] 无法打开（引文缺陷，随 P0-1 一并返工）**

- 位置：refs/10-refs.md 与正文导言、表 10-5 引用。
- 事实：https://snakemake.readthedocs.io/en/stable/executing/executor_plugin.html 返回 **404**；正确的官方页面为 https://snakemake.readthedocs.io/en/stable/executing/executors.html（标题「Using executor plugins」）。fact-check/10-log.md 第 17 行亦自认该条「本轮未逐字 fetch（正文按内置清单表述）」——违反 STYLE 四.4（每条引用入库前须 extract 打开原文）。条文所载论断（执行器接口自 8.0 起插件化）经官方迁移文档核实为真，属**链接失效**而非内容伪造。
- 修改建议：把 refs [5] 的 URL 更新为 `https://snakemake.readthedocs.io/en/stable/executing/executors.html`，用 extract 打开原文核验标题后再定稿；正文引用同步更新。

> 说明：按 REVIEW 判定表，「事实性错误」属 P0；以上任一未消除即判不合格，本报告据此判定返工。

### P1（修订后方可进入下一环节）

**P1-1　10.7.2「数据归档策略」——DataLad save/run 功能归属错误**

- 位置：10.7.2：「DataLad 以 git 加 git-annex 实现同样的指针机制，并追加两层能力：**`datalad save` 记录命令与输入输出的关联**，`datalad run` 把「执行命令产生结果」这一事件本身写入历史[22][35]…」
- 官方依据：DataLad Handbook 6.2.4（P3）——「The **datalad run** command … captures the provenance of any output generated with a datalad run call in the history of the dataset. Thus, by using datalad run … your dataset knows which result was generated when, by which author, from which inputs, and by means of which command.」。即「记录命令与输入输出的关联」是 `datalad run` 的功能；`datalad save` 只是保存变更与提交信息的手册级命令（6.2.3 用于 P2 的「a plain datalad save with a helpful commit message」）。
- 修改建议：改为「…并追加两层能力：`datalad save` 保存工作树变更并配合提交信息记录来源；`datalad run` 把「执行命令及输入输出关联」这一事件本身写入历史[22][35]…」。

**P1-2　10.4.3 末——无出处的版本区间断言**

- 位置：「续跑写入既有输出文件受检查点内校验和保护：任何输出文件被外部修改或删除后，mdrun 将拒绝直接追加，此时需恢复原文件或改用 `-noappend` 生成带 `.partXXXX` 后缀的分段输出[3]——**该行为在多版本间一致，适用于 GROMACS 2021 及以后版本的续算流程**。」
- 问题：官方 managing-simulations 页仅描述当前版本行为，未声明「2021 及以后」的起始版本；该区间断言无出处。属 REVIEW 二.2 关注的版本差异类陈述。
- 修改建议：删除版本区间短语，改为「（当前版本行为，见手册 Managing long simulations）」；如确须写区间，须逐版本核对 release notes 并注明依据。

### P2（记录，统稿时处理）

**P2-1　10.1.2/10.3.1——YODA 反例 `results_August19/` 未能在手册原文核实**
Handbook 6.2 当前页可见的反例为 `main_script_DONTUSE.py`、`results_for_paper/`、`results_new_data/`、`_version_xyz` 等，未出现 `results_August19/`。建议核对 F1000 海报原文（DOI 10.7490/f1000research.1116363.1）；无法核实则改用可核实例子（如 `results_new_data/`）。

**P2-2　表 10-2 `nsteps` 行出处混标 `[15][16]`**
mdp-options 页（[15]）只给默认值 (0)，不含「50000/250000」类推荐值；教程惯例值出自 Lemkul 教程（[16]）。建议该行改为 `[16]`，或注明「教程惯例」。

**P2-3　表 10-5「依赖判定」行**
Snakemake 侧写作「输出存在性 + 可选内容校验」，而其默认依赖判定同样基于文件存在性与修改时间，「内容校验」非常态默认特性。建议收敛为「输出存在性 + 中断/不完整输出重跑（--rerun-incomplete）」。

**P2-4　refs 头注自认 squeue/sacct/sstat/git-lfs 四页未逐字 fetch；本次核验确认 [29] sstat、[4] sbatch、[27] job_array 页可打开，[30] sacct 仅 HTTP 200（HTML 转换失败未逐字比对正文）**
建议补一次 anysearch extract 逐字核对 sacct 字段后，把 [28][29][30][34] 的状态从「文档推定」提升为「已核实」。

---

## 四、结论与返工范围（第一轮）

**结论：返工（不合格）。** P0-1（Makefile 模式规则优先级事实性错误）与 P0-2（引文 [5] URL 无法打开）未消除；机械项（字数/结构/文献数/编号连续性）、语言项（禁用表达/第二人称/{{}}残留）、跨章重复、抽查 8 条文献六项全部通过。

返工范围（P0 必须完成，P1 建议同轮完成）：
1. 重写 10.4.3 关于「模式规则选择优先级」与「同一目标多条规则」的两处语义表述（对照 GNU make 手册 §10.5.4/§4.11）。
2. 更新 refs [5] URL 为官方现役执行器插件页，并 extract 打开核验。
3. （P1）修正 10.7.2 的 datalad save/run 归属；删除或标注「GROMACS 2021 及以后」版本区间断言。
4. （P2）按第三节清单处理 YODA 反例出处、表 10-2 出处、表 10-5 措辞、sacct 核验提升。

审查自检：抽查文献及核验时间已列于第二节；所有问题均给出可执行修改；未因返工成本放宽任何判定。