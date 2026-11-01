# 第 8 章《自由能、增强采样与高级分析》对抗性验收报告（修订终验轮，2026-10-30）

- 验收对象：`08-自由能、增强采样与高级分析.md`（635 行，修订终验稿）
- 对照文件：REVIEW.md、STYLE.md、refs/08-refs.md、fact-check/08-log.md
- 验收人：对抗性验收者（独立复核，不采信修订方自述）
- 结论：**pass=false（P0 未消除）**

---

## 一、实测数字表（PowerShell 脚本实测，2026-10-30）

| 项目 | 实测值 | 标准 | 判定 |
| --- | --- | --- | --- |
| 汉字数（STYLE 口径：去代码块、去「## 参考文献」之后） | **16,460** | ≥10,000 | ✓ |
| 导言汉字数 | **313** | 300–600 | ✓ |
| H2 二级节 | **13**（学习目标、前置知识、8.1–8.10、参考文献） | ≥8；8.1–8.10 齐全 | ✓ |
| H3 三级节 | **27**（8.1:4、8.2:6、8.3:3、8.4:3、8.5:4、8.6:4、8.7:3） | ≥25；8.1–8.7 连续无重号（机器核对均连续=True） | ✓ |
| 表格 | **7**（表 8-1 … 8-7） | ≥3 | ✓ |
| 图 | **5**（图 8-1…8-5，均为 Mermaid 图题；另有 2 处行文引用） | ≥2 | ✓ |
| 常见错误 | **8**（错误一…错误八，含现象/成因/排查/处置） | ≥6 | ✓ |
| 习题 | **8**（含开放题 2：第 6、7 题） | ≥6 且含 2 开放题 | ✓ |
| 学习目标 | **6 条**，行为动词（能区分/能设计并运行/能沿…布置/能说明/能用…完成/能通过…运行） | 4–6 条 | ✓ |
| 参考文献 | 章末 30 条（[1]–[30]），refs/08-refs.md 30 条，两表逐行一致 | ≥30 | ✓（数量） |
| 编码/行尾 | UTF-8 无 BOM、LF（bare LF 635，CRLF 0） | UTF-8 无 BOM、LF | ✓ |
| 禁用表达 | 命中 0（「最后」1 处为句中非段首机械排列，不违规） | 0 | ✓ |
| 第二人称「你」 | 0 | 0 | ✓ |
| 占位符/TODO/待定 | 0 | 0 | ✓ |
| 正文引用编号首现顺序 | 1–30 严格递增、无跳号重号（脚本实测） | 连续 | ✓（编号序） |

---

## 二、历史问题逐条复核（父代理已修订，本轮独立复核）

| 编号 | 问题 | 复核结果 | 判定 |
| --- | --- | --- | --- |
| P0-1 | 「## 学习目标」「## 前置知识」缺失 | 位于导言后、8.1 前，存在且顺序正确（行 6、15） | **已解决** |
| P0-2 | 文献 <30 | 章末与 refs 均 30 条、编号 1–30、两表逐条一致 | **已解决** |
| P0-3 | 标题编号断裂（8.4.2 错位/重号） | 现为「### 8.1.4 计算流程的基本结构」（行 52）；8.4 节内为「### 8.4.2 计算流程」；8.1–8.7 三级节编号机器核对全部连续无重号 | **已解决** |
| P0-4 | calc-lambda-neighbors 默认值 -1 | 表 8-3 写「保持默认 1 由程序选择」；官方 mdp 文档原文「calc-lambda-neighbors (1)…Controls the number of lambda values…」（GitHub raw mdp-options.rst 行 2671–2673） | **已解决** |
| P0-5 | pull = umbrella 非法取值 | 表 8-4 首行为「pull = yes｜…｜配合 pull-coord1-type = umbrella」；mdp 文档 pull-coord1-type 取值仅 umbrella/constraint/constant-force/flat-bottom/flat-bottom-high/external-potential | **已解决** |
| P1-1 | 引用编号首现顺序 | 1–30 严格递增（脚本实测），编号序无跳无重 | 编号序解决；**但条目语义错配仍存在（见第三节 P0-3/4/5），故该项实质未达标** |
| P1-2 | [13] Srinivasan DOI/作者；VMD DOI | Crossref 核验：10.1021/ja981844+ = Srinivasan/Cheatham/Cieplak/Kollman/Case（作者五人全含）；VMD 现编号为 [16]=Humphrey/Dalke/Schulten，DOI 10.1016/0263-7855(96)00018-5 正确。注：章节 [13] DOI 写作 10.1021/ja981844（规范体为 ja981844+，可解析，P2） | **已解决**（P2 遗留） |
| P1-3 | [14] 定位 | [14] 现标注于 trjconv 命令后（8.4.2 行 273）；「外部溶剂化工具（MMPBSA.py…）」处现为 [15]（GROMACS 手册），不再错引 [14]；VMD 处为 [16] | **已解决** |
| P1-4/5 | refs/08-refs.md 与 08-log.md 交付 | 两文件存在；refs 与章末一致；log 有修订轮记录 | **已解决** |

---

## 三、文献抽查清单（核验通道与时间均记录；共核验 15 条文献 + 5 个官方文档页）

通道说明：本轮全程走 web_fetch：Crossref REST `https://api.crossref.org/works/<DOI>`（B 级文献）与 GROMACS/PLUMED 官方文档页（A 级）；核验时间 2026-10-30。

| 条目 | 核验结果（Crossref/官方文档） | 判定 |
| --- | --- | --- |
| [2] Kirkwood 1935（10.1063/1.1749657） | = "Statistical Mechanics of Fluid Mixtures", J Chem Phys 3(5):300-313 | 元数据正确；**正文错位引用**（见 P0-3） |
| [3] Torrie & Valleau 1977（10.1016/0021-9991(77)90121-8） | = "Nonphysical sampling distributions…: Umbrella sampling", J Comput Phys 23(2):187-199 | 元数据正确；**正文错位引用**（见 P0-3） |
| [7] Shirts & Chodera 2008（10.1063/1.2978177） | = "Statistically optimal analysis…", J Chem Phys 129(12):124105 | 正确 |
| [10] Kumar 1992（10.1002/jcc.540130812） | = "The weighted histogram analysis method…I. The method", J Comput Chem 13(8):1011-1021 | 元数据正确；**正文错位引用**（见 P0-4） |
| [13] Srinivasan 1998（10.1021/ja981844+） | = "Continuum Solvent Studies of the Stability of DNA, RNA, and Phosphoramidate–DNA Helices", JACS 120(37):9401-9409；作者 Srinivasan/Cheatham/Cieplak/Kollman/Case | 正确（DOI 缺 + 后缀，P2） |
| [16] VMD（10.1016/0263-7855(96)00018-5） | = Humphrey/Dalke/Schulten, "VMD: Visual molecular dynamics", J Mol Graph 14(1):33-38 | 正确 |
| [18] Pande 2010（10.1016/j.ymeth.2010.06.002） | = "Everything you wanted to know about Markov State Models…", Methods 52(1):99-105 | 正确 |
| [19] Sugita & Okamoto（10.1016/S0009-2614(99)01123-9） | = "Replica-exchange molecular dynamics method for protein folding", Chem Phys Lett 314(1-2):141-151 | 正确 |
| [23] Laio & Parrinello（10.1073/pnas.202427399） | = "Escaping free-energy minima", PNAS 99(20):12562-12566 | 正确 |
| [24] Bussi & Laio（10.1038/s42254-020-0153-0） | = "Using metadynamics to explore complex free-energy landscapes", Nat Rev Phys 2(4):200-212 | 正确 |
| [25] Invernizzi & Parrinello（10.1021/acs.jpclett.0c00498） | **错配**：该 DOI 解析为 Long et al. "Excited State Dynamics of Thermally Activated Delayed Fluorescence from an ESIPT System", JPCL 11(9):3305-3312（有机发光领域论文，与 OPES 无关）；正确 DOI 为 10.1021/acs.jpclett.0c00497（"Rethinking Metadynamics: From Bias Potentials to Probability Distributions"，JPCL 11(7):2731-2736）——**正文所印 DOI 与标题均错** | **✗ P0-1** |
| [26] AWH 文档 URL | https://manual.gromacs.org/current/reference-manual/algorithms/awh.html 返回 **404**；AWH 页实为 reference-manual/**special**/awh.html | **✗ P0-2** |
| [29] Jarzynski（10.1103/PhysRevLett.78.2690） | = "Nonequilibrium Equality for Free Energy Differences", PRL 78(14):2690-2693 | 正确 |
| A 级：gmx wham 文档页 | 默认 -bins=200、-b=50 ps、-ac 按 1/(1+2τ/dt) 加权、-bs-method 默认 b-hist、bootstrap 可能低估误差、文档「Always check whether the histograms sufficiently overlap」——正文内容全部属实 | 正确（但正文引用编号错位，见 P0-4） |
| A 级：GROMACS 手册「Using PLUMED」页 | PLUMED_KERNEL/libPlumedKernel.so/$plumed_prefix 路径/报错提示；三项限制（不交互能量、thread-MPI 多 rank 报错、副本交换未实现）逐字吻合 | 正确 |
| A 级：GROMACS Free energy calculations 页 | ΔG₁−ΔG₂=ΔG₃−ΔG₄；slow-growth 正反向一致不保证正确；delta_lambda=0 离散模式；MBAR 需外部 pymbar；dA/dλ=⟨∂H/∂λ⟩ 公式 | 正确 |
| A 级：Free energy interactions 页 | Beutler soft-core 式（r_A/r_B、α、p、σ）；p=2（GROMOS 原始）vs p=1 更平滑；sc-coul 默认线性关闭、sc-alpha=0 关闭软核、仅 A/B 一端为零时启用；氢原子 sc-sigma 尖峰 | 正确 |
| A 级：PLUMED 2.9 OPES_METAD 页 | 偏置式、p^WT∝[P]^{1/γ}、BARRIER 语义（自动设 BIASFACTOR/EPSILON/KERNEL_CUTOFF、过低不过垒、过高仅拖慢）、SIGMA 自适应（ADAPTIVE_SIGMA_STRIDE）、BIASFACTOR=inf 均匀、rct/zed/neff、STATE_RFILE/WFILE 精确续算、UPDATE_UNTIL=0 冻结 | 正确 |
| A 级：PLUMED 2.9 METAD 页 | 高斯沉积式、V(s)=−F(s)、未指定 GRID_BIN/SPACING 时网格间距默认 SIGMA/5 | 正确 |
| A 级：gmx hbond-legacy 页 | -a=30°、-r=0.35 nm 默认；-life/-ac/-nthreads；-fitfn 含 exp、-fitstart=1、-fitend=60 | 正确 |
| A 级：mdp-options（calc-lambda-neighbors (1)；pull-coord1-type 取值表） | 与正文表 8-3/8-4 一致 | 正确 |

> 待复核项：nstdhdl 默认值（官方 mdp-options 文档本轮抓取在 calc-lambda-neighbors 处截断，未直接看到 nstdhdl 默认行；正文写「每 10 步」，与官方既往版本一致，风险低）——列入统稿复查（P2）。

---

## 四、新发现问题（P0 → 判不合格）

### P0-1 文献条目错配：refs[25] DOI 与标题均错
- 章节 refs[25]：「Invernizzi M, Parrinello M. Rethinking metadynamics: From sampling potentials to optimal estimators. J Phys Chem Lett, 2020, 11(7): 2731-2736. DOI: 10.1021/acs.jpclett.0c00498.」
- Crossref 实测：10.1021/acs.jpclett.0c00498 = Long Y, Mamada M, et al., "Excited State Dynamics of Thermally Activated Delayed Fluorescence from an Excited State Intramolecular Proton Transfer System", JPCL 11(9): 3305-3312（TADF 光物理论文，与 OPES/元动力学无关）。
- 正确条目：DOI 10.1021/acs.jpclett.0c00497，标题 "Rethinking Metadynamics: From Bias Potentials to Probability Distributions"，JPCL 11(7): 2731-2736。
- 处置：修正 [25] 的 DOI 与标题（章末与 refs/08-refs.md 两处同步）。

### P0-2 文献 URL 无法打开：refs[26]（AWH）404
- 章节 refs[26] URL：`https://manual.gromacs.org/current/reference-manual/algorithms/awh.html` → HTTP 404。AWH 正确地址为 `reference-manual/special/awh.html`（手册 Special Topics「Adaptive biasing with AWH」）。

### P0-3 引文张冠李戴（[2]↔[3] 互换）
- 8.1.2（行 33）与 8.6.4（行 485）把伞形采样的描述引 [2]=Kirkwood 1935（"Statistical Mechanics of Fluid Mixtures"，系 TI 源头，与伞形采样无关）；8.1.2（行 35）「Kirkwood 在热力学积分方法中奠定了这一耦合参数思想[3]」、8.2.1（行 86）「Kirkwood 1935 年给出的基本结果[3]」却引 [3]=Torrie & Valleau 1977。
- 两篇文献元数据本身均正确（Crossref 已核），但**正文引用编号与文献内容对应颠倒**（伞形采样应为 [3]，Kirkwood TI 应为 [2]）。

### P0-4 引文张冠李戴（[10]↔[11] 互换）
- 8.3.2（行 195）、8.3.3（行 232、241）把 gmx wham 软件行为（默认 200 柱、-b 50 ps、-ac 按 1/(1+2τ/dt) 加权、bootstrap、文档要求检查直方图重叠）引 [10]=Kumar 1992（WHAM 方法论文，不含任何软件选项）；8.3.3（行 228）「WHAM 由 Kumar 等人提出[11]」却引 [11]=gmx wham 文档。
- 处置：gmx wham 工具行为改引 [11]，WHAM 方法出处改引 [10]。

### P0-5 引文定位错位（[26]）
- 8.7.1（行 536）「GROMACS 2026.4 手册 gmx select 词条[26]」——[26] 实为 AWH 文档；gmx select 文档不在 refs 中（应引 [15] 或补 gmx-select 条目）。同时 8.6.4（行 487）AWH 论述「（GROMACS 手册『Adaptive biasing with AWH』一节…[17,24]）」未引本应承载它的 [26]，而引 [17]=Amadei（本质动力学）、[24]=Bussi & Laio（元动力学综述），与 AWH 内容不符。即 [26]（AWH）在正文唯一出现点指向 gmx select，AWH 本体论述反而无 [26]。
- 处置：行 487 改引 [26]（并修正其 URL，见 P0-2）；行 536 改引 [15]（或为 gmx select 增列条目并重排编号）。

> 依据：REVIEW.md 二.1「出现一条伪造、错配或无法打开，整章判不合格」、二.3「引 A 文却写 B 文内容」均为 P0。上述 P0-1…P0-5 合并视为「引文层不合格」。另：08-log.md 记录「引用编号 1-30 首现顺序一致（脚本实测）」仅核对了编号序，未核对条目语义对应，导致 [2]/[3]、[10]/[11] 互换与 [25]/[26] 问题漏检——按 REVIEW.md 六.4 记录根因：**引用重排必须做「编号→条目内容→论断」三层对应校验，不能只跑编号机器扫描**。

---

## 五、P1 / P2 记录（修订后须一并处理）

| 级别 | 问题 | 位置/处置 |
| --- | --- | --- |
| P1 | 8.6.4（行 489）「GROMACS 的 -rc/-px 输出」：gmx wham、gmx analyze、gmx hbond-legacy、gmx sham 均无 `-rc`/`-px` 选项（已逐一核对官方 onlinehelp），属不存在的选项引用 | 改为「各窗口直方图（gmx wham -hist 或自写统计）」或删除 |
| P2 | [13] DOI 缺规范后缀「+」（10.1021/ja981844，规范体 ja981844+；可解析） | 补全 |
| P2 | nstdhdl 默认值未能在本轮直接复核（官方文档抓取截断）；正文「默认每 10 步」与官方既往版本一致 | 统稿复查 |
| P2 | 8.5.1「前 5—10 个 PC 超过总方差的八成」为无出处百分比（已有「常见的定性描述…不宜照搬」缓冲，不作 P0） | 可保留或改述 |
| P2 | 与第 11 章（行 292）在 PLUMED 集成事实（gmx mdrun -plumed、PLUMED_KERNEL、libPlumedKernel.so）上重叠，非逐字抄袭，但须两章口径一致 | 统稿协调 |

---

## 六、关键内容抽查（公式与参数，全部对照原始文献/官方文档）

- TI / FEP / BAR / MBAR 公式与出处：与 GROMACS 手册及 Zwanzig 1954、Bennett 1976、Shirts & Chodera 2008 一致（[4][5][7] 条目正确）；「MBAR 需外部 pymbar」与手册一致。
- soft-core Beutler 形式、sc-alpha/sc-power/sc-coul/sc-sigma 语义：与手册 Free energy interactions 原文逐项一致（p=2 原始 GROMOS、p=1 更平滑、静电默认线性关闭、仅一端为零时启用软核、氢原子尖峰与 sc-sigma）。
- gmx bar / gmx wham 用法：-oi/-oh/-temp；-bins=200/-b=50/-ac（1+2τ）/nBootstrap/bs-method 均与官方文档一致（唯编号引用错位，见 P0-4）。
- 元动力学参数（PACE/HEIGHT/SIGMA/BIASFACTOR/TEMP/GRID）：与 PLUMED 2.9 METAD 文档一致；网格间距默认 SIGMA/5 属实。
- OPES（BARRIER 语义、偏置式、SIGMA 自适应、STATE_RFILE/WFILE、UPDATE_UNTIL=0、rct/zed/neff）：与 OPES_METAD 文档逐项一致。
- PLUMED 集成限制（不交互能量、thread-MPI 多 rank 报错、副本交换未实现、PLUMED_KERNEL）：与 GROMACS 手册 Using PLUMED 原文一致。
- AWH：正文描述（accelerated weight histogram、awh- 参数组）正确，但引用定位/URL 错误（P0-2/P0-5）。
- 氢键判据默认 0.35 nm/30°、hbond-legacy -life/-ac/-fitfn/-fitstart 1/-fitend 60：与官方文档一致。

---

## 七、结论

**pass=false。** 历史 P0-1…P0-5 与 P1-1…P1-5 的文本性修订均已落实；但引文层仍有 5 处 P0（[25] DOI/标题错配、[26] URL 404、[2]/[3] 互换、[10]/[11] 互换、[26] 定位错位）未消除，另 1 处 P1（不存在的 -rc/-px 选项）须修订。按 REVIEW.md「任一 P0 未消除即判不合格」，本稿不合格，退回修订。返工范围：仅限文献层（refs/08-refs.md 与章末表第 [2][3][10][11][25][26] 条的内容与正文编号对应、行 33/35/86/195/228/232/241/485/487/536 的引用点、行 489 的选项表述），正文其余内容（公式、参数、结构、语言、字数）通过复核。

---

# 引文层复验轮（2026-10-30）

- 验收入：对抗性验收者（独立复核，不采信修订方自述）
- 验收对象：`08-自由能、增强采样与高级分析.md`（635 行）＋ `refs/08-refs.md`
- 通道：Crossref REST（web_fetch）、PubMed E-utilities（web_fetch）、OpenAlex（web_fetch）、anysearch（search/extract）；核验时间 2026-10-30
- 结论：**pass=false**（上轮 6 项引文层 P0/P1 全部真正解决；本轮新抽验发现 1 处新引文错配 refs[27] 页码，按 REVIEW.md 二.1 计 P0）

## 一、上轮 6 项逐条核对（全部：已解决）

| 编号 | 验收点 | 实测证据 | 判定 |
| --- | --- | --- | --- |
| P0-1 refs[25] | DOI=10.1021/acs.jpclett.0c00497；标题 Rethinking Metadynamics: From Bias Potentials to Probability Distributions；不得残留 0c00498 | 章末 L630 与 refs 行 29 均印该 DOI 与标题（句首大写式，正文 Ref 标题为 sentence case）；Crossref+REST 与 PubMed esummary（PMID 32191470）双通道确认 DOI/卷期页/作者全对；全文 0c00498 命中 0 | **已解决**（标题仅大小写与原文有差，见 P2） |
| P0-2 refs[26] | URL=reference-manual/special/awh.html | 章末 L631 与 refs 行 30 均印 special/awh.html；实测抓取 HTTP 200，页题 "Adaptive biasing with AWH - GROMACS 2026.4 documentation"；algorithms/awh 残留 0 | **已解决** |
| P0-3 [2]↔[3] | [2]=Torrie & Valleau 1977（伞形）、[3]=Kirkwood 1935（TI）；正文伞形引 [2]、Kirkwood TI 引 [3] | 两文件一致：[2]=Torrie/Valleau 1977, 10.1016/0021-9991(77)90121-8；[3]=Kirkwood 1935, 10.1063/1.1749657。正文 L33「…拼接出无偏分布[2]」、L191「Torrie 与 Valleau 的非物理采样分布方法[2]」、L485「…得到 PMF[2][9]」；L35「Kirkwood 在热力学积分方法中奠定了这一耦合参数思想[3]」、L86「Kirkwood 1935 年给出的基本结果[3]」 | **已解决** |
| P0-4 [10]↔[11] | [10]=gmx wham 文档、[11]=Kumar 1992；正文工具行为引 [10]、方法出处引 [11] | 两文件一致：[10]=gmx wham 文档页、[11]=Kumar 1992, 10.1002/jcc.540130812。正文 L195「gmx wham 的文档明确要求检查直方图重叠[10]」、L232「gmx wham 默认 200 柱…[10]」、L241「…自助法可能低估误差[10]」；L228「WHAM 由 Kumar 等人提出[11]」 | **已解决** |
| P0-5 [26] 定位 | AWH 论述引 [17,26]；gmx select 引 [15]；[26] 首现在 AWH 段 | L487 AWH 段「（GROMACS 手册『Adaptive biasing with AWH』一节，mdp 中以 awh- 前缀参数组启用[17,26]）」；L536「gmx select 词条[15]」；脚本实测 [26] 全书正文仅 1 次出现（L487=AWH 段），首现序第 26 位 | **已解决** |
| P1 8.6.4 -rc/-px | 不得再出现不存在的 -rc/-px 选项 | 8.6.4（L483–502）现为「（GROMACS 各窗口直方图输出或自写统计）」；全文 -rc 命中 0、-px 命中 0（脚本实测） | **已解决** |

## 二、独立复核：结构/统计快速复测（PowerShell 实测，2026-10-30）

| 项目 | 实测 | 判定 |
| --- | --- | --- |
| 汉字数（STYLE 口径） | 16,465（≥10,000；较上轮 16,460 +5，源于 8.6.4 选项表述改写的自然结果） | ✓ |
| H2 二级节 | 13（学习目标/前置知识/8.1–8.10/参考文献） | ✓ |
| H3 三级节 | 27（8.1:4、8.2:6、8.3:3、8.4:3、8.5:4、8.6:4、8.7:3；节内编号连续无重号） | ✓ |
| 表 | 7（表 8-1…8-7） | ✓ |
| 图 | 5（图 8-1…8-5 Mermaid 图题；另 2 处行文提及） | ✓ |
| 习题/开放题 | 8 / 2（#6、#7） | ✓ |
| 常见错误 | 8（错误一…八） | ✓ |
| 参考文献 | 章末 30 条 = refs 30 条；编号 1–30 各自连续无重；两表 Compare-Object 逐字差异 0 | ✓ |
| 编码/行尾 | UTF-8 无 BOM；LF 635、CRLF 0 | ✓ |
| 正文引用首现顺序 | 逐字符扫描 1–30 严格递增、无跳号重号；首现行号：1@3,2@33,3@35,4@92,5@98,6@98,7@102,8@118,9@185,10@195,11@228,12@249,13@249,14@273,15@276,16@276,17@294,18@368,19@389,20@393,21@393,22@415,23@423,24@423,25@464,26@487,27@540,28@542,29@556,30@556 | ✓ |

## 三、本轮文献抽验清单

| 条目 | 通道 | 结果 |
| --- | --- | --- |
| [25] Invernizzi & Parrinello（0c00497） | Crossref REST；PubMed esummary（PMID 32191470） | "Rethinking Metadynamics: From Bias Potentials to Probability Distributions"，JPCL 11(7):2731-2736, 2020；双通道一致 | ✓ |
| [26] AWH 文档 URL | web_fetch 官方文档 | HTTP 200，页题 "Adaptive biasing with AWH" | ✓ |
| [12] Kollman（10.1021/ar000033j） | Crossref REST | Acc Chem Res 33(12):889-897, 2000；作者 Kollman/Massova/Reyes… | ✓ |
| [20] Tribello（10.1016/j.cpc.2013.09.018） | Crossref REST | CPC 185(2):604-613, 2014 "PLUMED 2: New feathers for an old bird"；作者 Tribello/Bonomi/Branduardi/Camilloni/Bussi | ✓ |
| [30] Valsson（10.1146/annurev-physchem-040215-112229） | Crossref REST | ARPC 67:159-184, 2016；Valsson/Tiwary/Parrinello | ✓ |
| [21] Bonomi（10.1038/s41592-019-0506-8） | Crossref REST | Nat Methods 16(8):670-673, 2019；Crossref 著录作者为 The PLUMED consortium，正文所列 Bonomi/Bussi/Camilloni et al. 与该文署名一致，非错配 | ✓ |
| [27] Luzar & Chandler（10.1038/379055a0） | Crossref REST + OpenAlex + anysearch（nature.com 引用框、Google Scholar、ResearchGate） | 标题/作者/卷期/DOI 全对；**页码错**：出版商自引「Nature 379, 55–57 (1996)」，Crossref/OpenAlex/Google Scholar/ResearchGate 均为 55-57，正文印 55-58，无任何来源支持 | **✗ 新 P0** |

## 四、新发现问题（引文层）

**NEW-P0：refs[27] 页码错配（55-58 实为 55-57）**
- 位置：章末 L632 与 refs/08-refs.md L31（两文件逐字一致，须同步改）。
- 证据（六路独立）：Nature 官网该文引用框 "Nature vol 379, pages 55–57 (1996)"；Crossref page=55-57；OpenAlex first/last=55/57；Google Scholar（Chandler 主页）"Nature 379 (6560), 55-57, 1996"；ResearchGate "379(6560):55-57"；ADS 起始页 55。PubMed 该文 DOI 未索引，无需再证。
- 处置：两文件 [27] 页码 55-58 → 55-57（一行字）。
- 分级：按 REVIEW.md 二.1（卷期页属必核六项，出现错配判不合格）与本任务「无新增问题」条款计 P0 → pass=false；若参照上轮 [13] DOI 后缀先例将此类单字段著录差错降 P2，则其余全绿。验收从严，计 P0。
- 根因（REVIEW 六.4）：引文复核须对「标题/作者/期刊/年份/卷期页/DOI」六项逐字段比对原文，不能只查 DOI 与标题；建议复核脚本增加「卷-期-页」三元组比对。

## 五、遗留与新增 P2（统稿处理，不阻塞）

- [25] 标题大小写差（正文 sentence case vs 出版原题 Title Case；GB/T 7714 未强制，可统一原题大小写）。
- L487 [17,26] 中 [17]=Amadei（本质动力学）对 AWH 软件行为句语义不直接支撑（AWH 论断由 [26] 承担）；上轮父代理明确要求 [17,26]，保留不违规，可斟酌删 [17]。
- 表 8-7 出处句（L502）未列 [26]（以 GROMACS 手册[15] 统摄 AWH 行），与 P0-5 设计一致，可保留。
- nstdhdl 默认值（每 10 步）官方页未逐字复核（承上轮）。
- 8.5.1「前 5—10 个 PC 超八成方差」无出处百分比（承上轮）。
- 与第 11 章 PLUMED 集成表述重叠（承上轮，统稿协调）。
- [13] DOI 缺规范后缀（承上轮；规范体 10.1021/ja981844p）。

## 六、结论

上轮 5 项 P0 + 1 项 P1 全部真正解决，无旧问题回潮；正文引用编号首现严格递增 1–30，章末与 refs 清单逐字一致；本轮新抽验 7 条中 6 条全对，唯 [27] 页码 55-58→55-57 错一处。按 REVIEW 二.1 计新 P0，**pass=false**。返工范围：仅 [27] 页码一处（章末与 refs 两文件同步），改后即可复验通过。

---

# 最终复验轮（2026-10-30）

- 验收人：验收者（第三方最终复验，最后一轮）
- 验收对象：`08-自由能、增强采样与高级分析.md`（635 行）＋ `refs/08-refs.md`
- 目标：确认上轮唯一遗留项 refs[27] 页码 55-58→55-57 已两处同步修正；复核编号首现序、两表一致性、汉字数；新增抽验 2 条此前未核验文献。
- 通道：本地 PowerShell 脚本（机械核对，脚本见 `fact-check/_verify_08_r3.ps1`）＋ web_fetch（GROMACS 2026.4 官方文档页）；核验时间 2026-10-30。
- 结论：**pass=true（第 8 章全章验收通过）**

## 一、[27] 修正核对（上轮唯一遗留项，父代理已同步修正）

| 验收点 | 实测 |
| --- | --- |
| 章末参考文献表 [27] | `[27] Luzar A, Chandler D. Hydrogen-bond kinetics in liquid water[J]. Nature, 1996, 379(6560): 55-57. DOI: 10.1038/379055a0.` |
| refs/08-refs.md [27] | 与章末逐字一致（同上行） |
| 55-58 残留扫描（含连字符/hyphen/en-dash/em-dash/minus 各变体） | 正文文件命中 0；refs 文件命中 0 |
| 全文「55-x」页码形令牌 | 仅剩 `55-57` 一处（即 [27]），无其他页码形残留 |
| 正文引用点 [27] 语义 | 8.7.2「氢键寿命的物理模型与分子水中的氢键动力学见文献[27]」——与 Luzar & Chandler 1996 主题对应 |

判定：**已解决**，无 55-58 任何残留。

## 二、机械核对实测（PowerShell 脚本，2026-10-30）

| 项目 | 实测 | 判定 |
| --- | --- | --- |
| 正文引用编号首现顺序（朴素逐字符扫描，含代码块，去「## 参考文献」后） | 1,2,3,…,30 严格递增、无跳号无重号；count=30、max=30、断裂 0 | ✓ |
| 章末文献表 vs refs/08-refs.md 逐条比对（区分大小写） | 30/30 条逐字一致，差异 0；两表条目数均 30 | ✓ |
| 汉字数（STYLE 口径：去代码块、去「## 参考文献」后计 [\u4e00-\u9fff]） | 16,465 | ✓（≥10,000） |
| 结构快测 | H2=13、H3=27（与上轮一致，无变化） | ✓ |

## 三、本轮新增文献抽验（2 条，均为此前轮次抽验清单未列条目）

| 条目 | 通道 | 结果 |
| --- | --- | --- |
| [1] GROMACS 2026.4 Free energy calculations 手册页 | web_fetch `https://manual.gromacs.org/current/reference-manual/algorithms/free-energy-calculations.html`（HTTP 200） | 页题 "Free energy calculations - GROMACS 2026.4 documentation"；ΔG₁−ΔG₂=ΔG₃−ΔG₄（式 125）、slow-growth 正反向结果一致不保证正确、`delta_lambda` 置 0 的离散模式与逐点平衡、MBAR 需外部 pymbar、dA/dλ=⟨∂H/∂λ⟩、G=A+pV——正文 8.1–8.2 各引用点全部吻合 | ✓ 无错配 |
| [6] gmx bar onlinehelp 页 | web_fetch `https://manual.gromacs.org/current/onlinehelp/gmx-bar.html`（HTTP 200） | 页题 "gmx bar - GROMACS 2026.4 documentation"；`-f` 接受多个 dhdl.xvg、`-oi`(barint.xvg)/`-oh`(histogram.xvg)、误差按分块并假定块间独立估计、合并不同采样间隔数据时假定样本独立「almost certainly not correct」（误差可能低估）、相对熵 s_A/s_B 相空间重叠度量——正文 8.2.2/8.2.6 各引用点全部吻合 | ✓ 无错配 |

## 四、结论

上轮唯一遗留项 [27] 页码已由 55-58 同步修正为 55-57（章末与 refs 两处逐字一致），全文无 55-58 残留；正文引用编号首现严格递增 1–30，章末与 refs/08-refs.md 清单 30/30 逐条一致，汉字数 16,465 ≥ 10,000；本轮新抽验 [1]、[6] 两条此前未核验的 A 级官方文档文献，经 web_fetch 实测均 HTTP 200，标题、URL 与正文引用点内容对应全部吻合，无新增错配。上轮 6 项引文层 P0/P1 全部确认解决且无回潮，本轮无新增 P0/P1。

**pass=true，第 8 章全章验收通过。**

遗留 P2（不阻塞，统稿处理）：[25] 标题大小写、[13] DOI 规范后缀（ja981844p）、nstdhdl 默认值官方页复核、8.5.1「前 5—10 个 PC 超八成方差」无出处百分比、与第 11 章 PLUMED 集成表述口径协调——均承上轮记录。