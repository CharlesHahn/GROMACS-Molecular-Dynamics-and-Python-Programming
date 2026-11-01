# 第 4 章《体系构建：从结构到拓扑》对抗性验收报告（第五轮）

- 验收对象：`04-体系构建.md`（472 行；UTF-8 **带 BOM**，见第五节 P2-1；CRLF=0，LF=471）
- 验收依据：`REVIEW.md`、`STYLE.md`（均未放宽）；对照 `refs/04-refs.md`、`fact-check/04-log.md` 与第四轮 `04-review.md`（P0-2、P1-4 及第三轮 3×P0+3×P1 逐条独立复核）
- 核验通道：**anysearch 当日免费配额已耗尽**（2026-10-29 三连尝试均返回「total free quota for today」），按任务约定改用 **Crossref REST API**（`/works?query.bibliographic=…` 与 DOI 直达）核验 DOI/卷期页，并以 web_fetch 直连官方手册/档案/Europe PMC 核验 A 级文档与正文断言；**通道变更已在本文标注**
- 核验时间：2026-10-29 07:15 – 08:15（Asia/Shanghai）
- 结论：**合格（pass=true）**。P0 = 0，P1 = 0。历轮 P0-2（genion 括注）与 P1-4（mmCIF 政策出处）均已按验收口径消除；第三轮 3×P0 与 3×P1 抽查仍保持正确。随机抽样文献 10/10 通过（无伪造、无错配、无无法打开）。机械项全部达标。新增/遗留问题均为 P2（含一处编码回归，见第五节）。

---

## 一、实测数字表（机械项，PowerShell 实测，口径同 STYLE 第三节）

| 指标 | 要求 | 实测 | 判定 |
| --- | --- | --- | --- |
| 汉字数（去 ``` 代码块 + 截断至「## 参考文献」，含表格/图注） | ≥10,000 | **13,869**（全文件 14,238） | 通过 |
| 编码 / 行尾 | STYLE 七.1：UTF-8 无 BOM / LF | **首 4 字节 EF BB BF（带 BOM）**，与第四轮核实的无 BOM 状态（`23 20 E7 AC`）不一致，疑似修订工具重存引入；CRLF=0，LF=471 | **P2-1（编码回归）** |
| 二级节 `##` | ≥8 | 16（含「参考文献」；正文 15） | 通过 |
| 三级节 `###` | ≥25 | 33 | 通过 |
| 表格 | ≥3 | 6（表 4-1～4-6，表题在表上方、6 条分隔行） | 通过 |
| 图 | ≥2（Mermaid 或登记占位） | 2（图 4-1、4-2，均 Mermaid，图题在图下方） | 通过 |
| 参考文献 | ≥30 | 章末 64 条 / refs 文件 64 条，逐条一致；编号 1–64 无缺失 | 通过 |
| 正文上标编号 | 连续、无跳号、无重号、不越界 | 144 处引用；去重 64 个，MIN=1、MAX=64、缺失=0（详见二·P1-4） | 通过 |
| 导言 | 300–600 字 | 426 汉字 | 通过 |
| 学习目标 | 4–6 条、行为动词 | 6 条（均「能…」） | 通过 |
| 前置知识 | 指明章节/文献 | 4 条 | 通过 |
| 常见错误 | ≥6、四要素（现象/成因/排查/处置） | 8 条 | 通过 |
| 本章小结 | 分点、不复读导言 | 10 点 | 通过 |
| 习题 | ≥6，含 ≥2 开放题 | 8 题（#7、#8 标【开放题】） | 通过 |
| 构件顺序 | 导言→学习目标→前置知识→正文→常见错误→小结→习题→参考文献 | 符合 | 通过 |
| 禁用表达（STYLE 第六节） | 0 | 0 | 通过 |
| 第二人称「你」/「我们」/套话过渡 | 0 | 0（全文无「你」「我们」字符） | 通过 |
| 「首先/其次/最后」段首机械排列 | 0 | 0 | 通过 |
| 命令「实测/本机」误标 | 0 | 0（「本机」仅见于常见错误 #7 的故障场景描述） | 通过 |

---

## 二、历轮遗留问题核对（逐条独立复核）

### 1. P0-2（4.7.3 genion 括注）——**已消除**

- 现文（第 230 行）：「随机替换为长期默认行为：官方档案自 4.0.1 起即注明 `-random` 选项默认开启、因基于静电势的选位计算不可靠；该选项在 GROMACS 4.6 系列后期被移除，当前版本的帮助文本与选项表中已无 `-random` 项，`genion` 一律在选定溶剂组中随机选取位置替换水分子[47]。」
- 与验收口径比对：不再出现「更早版本默认按最低静电势位点」或「自 4.6 起默认随机」错误锚点（全文 grep 0 命中）；「自 4.0.1 起 `-random` 默认开启、因基于静电势的选位计算不可靠、4.6 系列后期移除、当前无 `-random` 项」四要素与要求的改写一致，其中「因…选位计算不可靠」对应官方原文 "Calculation of the potential is not reliable, therefore the -random option is now turned on by default"，属**原因说明**而非历史默认值主张。
- 独立核验（本轮直接打开官方档案）：
  1. `manual.gromacs.org/archive/4.6.1/online/genion.html`（HTTP 200）：选项表含 `-[no]random bool yes`（"Use random placement of ions instead of based on potential"），Known problems：*"Calculation of the potential is not reliable, therefore the -random option is now turned on by default"* → 4.6.1 随机已默认、选项仍在。
  2. `manual.gromacs.org/archive/4.6.6/online/genion.html`（HTTP 200，页面内容标注 VERSION 4.6.5、2013-12-02）：选项表**已无 `-random`**；Description 改为 "genion randomly replaces solvent molecules with monoatomic ions" → 4.6 系列后期移除成立。
  3. `manual.gromacs.org/current/onlinehelp/gmx-genion.html`（HTTP 200，2026.4）：同样无 `-random`，选项含 `-pname/-nname/-rmin/-seed/-conc/-[no]neutral`；`-rmin` 说明 "Minimum distance between ions and non-solvent" 与正文「`-rmin` 控制离子与非溶剂（溶质）之间的最小距离」逐字对应；Known Issues 注明 `-conc` 不把已有离子计入 → 「已有离子不参与计算」成立。
- 全文 genion 表述一致性：4.1.1（第 45 行「随机替换水分子」）、4.7.2（第 217 行「在选定溶剂组（通常为 SOL）中随机选取位置，把水分子替换为单原子离子」）、4.7.3 均统一为「随机替换」，无静电势选位残留。
- 注：「自 4.0.1 起」为验收口径指定的锚点（第四轮经 Debian man 镜像核验 4.0.1 同款 `-random (yes)` + 同一 known-problems 注）；官方 archive 目录最早仅覆盖至 4.5.x，本轮以 4.6.1/4.6.6 官方档案直接佐证「随机默认早于 4.6、4.6 系列后期移除」两个关键事实。

### 2. P1-4（4.2.1 mmCIF 政策出处）——**已消除**

- 现文（第 68 行）：「…目前 PDB 存档的新结构与绝大多数更新均以 mmCIF 发布[6]；wwPDB 自 2019 年 7 月起对晶体学方法解出的结构强制采用 PDBx/mmCIF 作为唯一沉积格式[64]。」——与验收要求的句式一致，含 `[64]`。
- 文献表：章末与 `refs/04-refs.md` 均含 `[64] Adams P D, Afonine P V, Baskaran K, et al. Announcing mandatory submission of PDBx/mmCIF format files for crystallographic depositions to the Protein Data Bank (PDB)[J]. Acta Crystallographica Section D: Structural Biology, 2019, 75(4): 451-454. DOI: 10.1107/S2059798319004522.`
- 编号连续性：正文去代码块后 144 处上标，唯一编号集合恰为 {1,…,64}，MIN=1、MAX=64、无缺失、无越界。
- 独立核验：[64] 六项经 Crossref 全项吻合（标题精确匹配；作者 Adams/ Afonine/ Baskaran/ Berman 等 35 人序列一致；Acta Cryst. D Struct. Biol.；2019；卷 75 期 4 页 451-454；DOI 10.1107/s2059798319004522）；Europe PMC（PMID 30988261 / PMC6465986）摘要原文 "This letter announces that PDBx/mmCIF format files will become mandatory for crystallographic depositions to the Protein Data Bank (PDB)" 支持「强制」主旨；生效时点「1 July 2019」与 wwPDB OneDep 政策一致（IUCr 期刊页与 PDF 本轮被 Cloudflare 403 拦截，无法打开原文页，但 Crossref+PMC 记录已完整覆盖六项核验，不构成「无法打开」的文献本身问题）。
- 已知取舍（记 P2-3）：`[64]` 首次出现于第 68 行、早于编号 7–63 的首次出现，严格意义上不满足 STYLE 五.3「编号按首次出现顺序排列」；此为验收口径明确指定的构造（P1-4 要求 4.2.1 出现 [64] 且编号连续到 64），按指令接受，记 P2 备统稿复核。
- 附注（记 P2-2）：同句前段「目前 PDB 存档的新结构与绝大多数更新均以 mmCIF 发布[6]」仍以 [6]（Berman 2000）作引注，严格说 [6] 不承载「目前」时点；因紧随其后的 [64] 已提供现行政策出处，句内事实依据齐备，降级为 P2（建议把该分句的引注移入 [64] 或将 [6] 拆为「格式定义」出处）。

### 3. 第三轮已修 3×P0 与 3×P1 抽查——**仍保持正确**

| 项 | 现文位置 | 复核 |
| --- | --- | --- |
| P0 His 质子化态自动判定 | 第 74 行「`pdb2gmx` 默认按最优氢键几何自动判定（该自动判定自早期版本起即为默认行为，并非 2026 年引入）…可用 `-his` 交互指定」；学习目标第 2 条、习题 1 同口径 | 与 4.6.1 档案 "By default these selections are done automatically. For His, this is based on an optimal hydrogen bonding conformation" 及 `-[no]his` 选项一致 |
| P0 genion 随机替换（与 4.7.3 一致） | 4.1.1/4.7.2/4.7.3 三处统一「随机替换」（见 P0-2） | 2026.4 帮助 "randomly replaces solvent molecules" |
| P0 editconf 盒型枚举 | 第 189 行 triclinic/cubic/dodecahedron/octahedron 四类；表 4-5 将 rectangular 列为 triclinic 90° 特例并注明非 `-bt` 取值；0.71/0.77 体积比 | 与 4.5.4/5.0.7 帮助枚举及 0.71/0.77 原文一致 |
| P1 OpenFF `to_gromacs("lig")` | 第 280 行，注释「写出 lig.top 与 lig.gro」 | openff-interchange 签名 `to_gromacs(prefix, …)`，位置参数正确 |
| P1 MDAnalysis 示例参数 | 第 346-348 行 `topology_format="ITP"`、`include_dir="."`、注释（include_dir 默认路径、不读 GMXLIB、.top 二义性） | 与 MDAnalysis 2.2.0 ITPParser 源码/docstring 一致 |
| P1 [24] TIP3P 对应 | 第 167 行「CHARMM36 族使用其修订版 TIP3P[24]，其 GROMACS 移植版中氢原子带 Lennard-Jones 参数[63]」；refs [24]＝Price & Brooks 2004、[63]＝MacKerell 实验室页 | 分工正确：修订版 TIP3P 归 [24]，H 带 LJ 归 [63] |

---

## 三、随机抽样文献核验清单（种子 20261029，从 1–64 抽 10 条）

通道说明：anysearch `search` 三次尝试均返回「API key 总免费配额已耗尽」（2026-10-29），按验收任务约定改用 **Crossref REST API** 核验 DOI 六项（`/works?query.bibliographic=…&select=…` 与 DOI 直达），A 级官方文档用 web_fetch 直开页面。以下「通过」均指六项（标题/作者/期刊/年份/卷期页/DOI）与 refs 逐字一致或 URL 可打开且内容支持正文断言。

| 编号 | 文献 | 核验通道与结果 | 判定 |
| --- | --- | --- | --- |
| [2] | GROMACS 2026.4 Getting started（流程图） | web_fetch 打开（HTTP 200），含「Flowchart of typical simulation」节并链接 flow.html；「官方流程图止于溶剂化」断言依第四轮对 flow.html digraph（pdb2gmx→editconf→solvate→grompp→mdrun，无 genion）核验 | 通过 |
| [3] | GROMACS 2026.4 gmx grompp | web_fetch 打开（HTTP 200）：「expands the topology from a molecular description to an atomic description」、`-pp` 输出预处理拓扑、`-maxwarn`「Not for normal use…may generate unstable systems」、`-zero`「Set parameters…to zero instead of generating an error」均与正文一致 | 通过 |
| [9] | Anandakrishnan 2012 H++ 3.0 | Crossref bibliographic：标题精确匹配；Anandakrishnan/Aguilar/Onufriev；NAR；40(W1):W537-W541；2012；DOI 10.1093/nar/gks375 | 通过 |
| [12] | GROMACS 2026.4 Force field organization | web_fetch 打开（HTTP 200）：力场按 `<name>.ff` 目录在 `$GMXLIB/share/gromacs/top` 与工作目录检出（支撑正文「按 GMXLIB 与当前目录搜索」）；内建列表含 AMBER14SB/19SB（支撑 2026 移植断言）；「OPLS-AA/L all-atom force field」条目（支撑正文「内建 OPLS-AA/L」） | 通过 |
| [26] | Marrink 2007 MARTINI | Crossref（query.bibliographic+Marrink+2007 过滤）：标题/作者（Marrink, Risselada, Yefimov, Tieleman, de Vries）/JPCB/111(27):7812-7824/2007/DOI 10.1021/jp071097f 全吻合 | 通过 |
| [35] | Abascal & Vega 2005 TIP4P/2005 | Crossref DOI 直达：标题/作者/JCP/123(23)/article-number 234505/2005/DOI 10.1063/1.2121687 吻合 | 通过 |
| [36] | Izadi 2014 OPC | Crossref DOI 直达：标题「Building Water Models: A Different Approach」/Izadi, Anandakrishnan, Onufriev/JPCL/5(21):3863-3871/2014/DOI 10.1021/jz501780a 吻合 | 通过 |
| [41] | Lopes 2013 Drude 可极化力场 | Crossref DOI 直达：标题/作者（Lopes, Huang, Shim, Luo, Li, Roux, MacKerell Jr）/JCTC/9(12):5430-5449/2013/DOI 10.1021/ct400781b 吻合 | 通过 |
| [47] | GROMACS 2026.4 gmx genion | web_fetch 打开（HTTP 200）：无 `-random`，`-rmin`、`-conc`、Known Issues 均与正文一致（见 P0-2 核验） | 通过 |
| [60] | Li & Merz 2017 金属离子综述 | Crossref bibliographic：标题「Metal Ion Modeling Using Classical Mechanics」/Li Pengfei, Merz Kenneth M. Jr/Chem. Rev./117(3):1564-1686/2017/DOI 10.1021/acs.chemrev.6b00440 吻合 | 通过 |

**抽查结论：10/10 通过，无一条伪造、错配或无法打开。**

---

## 四、语言、跨章与内容抽查

| 检查项 | 结果 |
| --- | --- |
| 禁用表达（16 词） | 0 命中 |
| 第二人称「你」/「我们」 | 全文 0 命中 |
| 套话过渡（让我们/接下来我们/值得注意的是/总而言之）与段首「首先/其次/最后」 | 0 命中 |
| 无出处定量断言 | 逐条核过：0.15 mol/L（已标注「生理学常用近似而非普适」）、1.0 nm 缓冲下限（标注经验法/文档推定）、0.105 nm 级别（solvate `-radius` 文档默认，日志已核实）、±10% 二硫键容差与约 0.20 nm（日志已核实）、>2.5 Å 分辨率（标注教学性概括）、0.71/0.77 体积比（[42][43]，第四轮已核）——均无裸定量 |
| 跨章重复（02/03/05/06/07 全文逐字句级比对） | 0 条逐字重复句子；05 章 12 字 n-gram 重叠窗口 94/≈26,000（0.36%，属共享术语如 pdb2gmx/PME/最小镜像，非段落抄袭） |
| 「引综述冒充原始结论」「同一编号指代不同文献」 | 未发现（Martini 3 归 [27]、MARTINI 框架归 [26] 分工正确等） |

---

## 五、问题清单（P0=0，P1=0，P2=8）

### P0（0 项）
无。

### P1（0 项）
无。第四轮唯一 P1（mmCIF 引文时点不匹配）已由 [64] 消除，第三轮 3 项 P1 经复核仍正确。

### P2（记录，统稿时处理；含 1 项新增编码回归 + 7 项遗留/附注）

1. **编码回归（新增，务必修）**：`04-体系构建.md` 首 4 字节为 `EF BB BF`（UTF-8 BOM），第四轮实测为 `23 20 E7 AC`（无 BOM）。STYLE 七.1 要求无 BOM。疑为 P0-2/P1-4 修订时工具重存引入。**处置**：以无 BOM UTF-8 重存（如 `$c = Get-Content -Raw …; [IO.File]::WriteAllText($f, $c, [Text.UTF8Encoding]::new($false))`），重存后复核汉字数与行数不变。
2. **4.2.1 引注卫生**：同句「目前 PDB 存档的新结构与绝大多数更新均以 mmCIF 发布[6]」的「目前」时点建议移注至 [64]，或将 [6] 定位为「格式定义」出处（正文事实依据已由 [64] 覆盖，不构成 P1）。
3. **[64] 编号顺序**：[64] 首次出现（第 68 行）早于 7–63，与 STYLE 五.3「按首次出现顺序」不严格一致；系验收口径指定构造，建议终校时说明或调整编号方案。
4. **4.2.2 His 措辞落实验收口径**（遗留）：建议把「该自动判定自早期版本起即为默认行为」落实为「自 GROMACS 4.6.1 起即默认自动判定」（4.6.1 档案可证）。
5. **4.2.3 clashscore 定义不完整**（遗留）：建议改为「clashscore（每 1000 个原子中重叠 ≥0.4 Å 的非键原子对数目）」（MolProbity 为千原子归一化指标）。
6. **4.8.2 tleap 块顺序**（遗留）：`check LIG` 置于 `loadamberparams lig.frcmod` 之前会先打缺失参数告警（非致命），建议先 loadamberparams 再 check。
7. **4.8.4/表 4-6 [56] 导出步骤可见性**（遗留）：示例页标题/URL 匹配、可打开，但建议终校人工确认 to_gromacs 导出一步的页面呈现。
8. **4.4.3「Martini 是生物分子领域应用最广的 CG 力场」**（遗留）：最高级断言无直接出处，建议改「应用广泛」或在 [27] 处补验证范围。

---

## 六、结论与返工范围

**结论：合格（pass=true）。** P0 = 0，P1 = 0，P2 = 8。

- 历轮问题全部解决：P0-2（4.7.3 genion 括注）已按验收口径改写，官方档案 4.6.1/4.6.6/2026.4 直接佐证「`-random` 默认开启→4.6 系列后期移除→当前无此选项」，全文 genion 表述统一为随机替换；P1-4 已补 [64] 并核验六项，正文编号连续到 64；第三轮 3×P0（His、genion、editconf）与 3×P1（to_gromacs、MDAnalysis、[24]/[63]）抽查全部仍正确。
- 机械项全部达标：汉字 13,869、H2=16（正文 15+参考文献）、H3=33、表 6、图 2、文献 64、上标 1–64 连续、构件顺序合规、常见错误 8、习题 8（含 2 开放题）、禁用表达/第二人称/套话过渡为 0。
- 随机文献抽查 10/10 通过（种子 20261029：[2][3][9][12][26][35][36][41][47][60]），无伪造、无错配、无无法打开；anysearch 配额耗尽，按约定改走 Crossref REST + web_fetch 通道并在本文标注。
- 跨章逐字句级比对 0 重复，05 章 n-gram 重叠属共享术语，无抄袭。
- **返工范围（可并入统稿）**：①修 P2-1 编码回归（去 BOM 重存，最优先）；②P2-2～P2-8 为引注卫生/措辞细节，不影响本环节通过。