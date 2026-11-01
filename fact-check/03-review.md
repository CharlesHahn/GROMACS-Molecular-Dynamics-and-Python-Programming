# 第 3 章 验收报告（P1 修订后复验，第二轮对抗性复核）

> 复核时间：2026-10-29 06:05–06:30（Asia/Shanghai）。复核人：验收 agent（独立复核，PowerShell 实测 + anysearch/Crossref 独立核验）。
> 本轮任务：上一轮（2026-10-29 早）已修复 P1-A/P2-A～P2-E，本轮为**修订完成后复验**：逐条确认上一轮 3 条 P1（①[5][33] 六项补齐；②3.4.4 定量区间加条件；③章标题与 OUTLINE 一致），并对全章重新对抗性核查（字数/结构、文献抽查、关键论断、语言、跨章重复）。
> 结论：**通过（pass=true）**。无 P0；上一轮 3 条 P1 全部确认修复；本轮无新 P1；遗留 3 条 P2 与 3 条复验确认记录，见问题清单。

## 一、实测数字表（STYLE.md 第三节口径，PowerShell 脚本实测）

| 项目 | 要求 | 实测 | 判定 |
| --- | --- | --- | --- |
| 汉字数（去代码块、截断至「## 参考文献」，含表格图注） | ≥10,000 | **13,601** | 通过 |
| 正文二级节（`##`） | ≥8 | 9（全章含构件 15） | 通过 |
| 三级节（`###`） | ≥25 | 28 | 通过 |
| 表格（表题在上、全角空格） | ≥3 | 4（表 3-1～3-4） | 通过 |
| 图 | ≥2 | 3（图 3-1/3-2/3-3，均 Mermaid，无需占位登记） | 通过 |
| 常见错误（现象→成因→排查→处置） | ≥6 | 8（逐条含「处置」） | 通过 |
| 习题 | ≥6，含 ≥2 开放题 | 8（第 7、8 题【开放题】） | 通过 |
| 参考文献 | ≥30 | 44（[1]–[44]） | 通过 |
| 正文上标编号 | 连续、无跳号重号、与列表逐条对应 | 首次出现严格递增 1→44、全部被引；两处 `[0]` 为行内代码 `data.shape[0]` 误匹配，非引用 | 通过 |
| 正文列表 vs refs/03-refs.md | 逐条一致 | 44 vs 44，脚本比对 0 差异 | 通过 |
| 必备构件顺序 | 导言→学习目标→前置知识→正文→常见错误→小结→习题→参考文献 | 行 3/5/14/20…/627/645/654/672，齐全且顺序正确 | 通过 |
| 导言字数 | 300–600 | 319 | 通过 |
| 学习目标 | 4–6 条、行为动词 | 6 条（均以「能」开头） | 通过 |
| 编码与换行 | UTF-8 无 BOM、LF | 无 BOM（首字节 35,32,80）、0 CRLF | 通过 |

## 二、上一轮 3 条 P1 逐条复验（本轮重点）

| 上一轮 P1 | 修订声明 | 本轮独立复核结果 | 判定 |
| --- | --- | --- | --- |
| P1-1：文献 [5][33] 六项补齐 | log 称 [5] 补页码 98-105、[33] 补 DOI 与页码 | **正文+refs 均已无「待补」注记**。[5] 现为「Gowers R J, Linke M, Barnoud J, et al. …SciPy 2016: 98-105. DOI: 10.25080/Majora-629e541a-00e」；[33] 现为「Rosenbaum M K, van der Spoel D. plotXVG…JCIM, 2026, 66(6): 2955-2959. DOI: 10.1021/acs.jcim.5c02998」。**本轮 Crossref 独立核验**：[5] 标题「MDAnalysis: A Python Package for the Rapid Analysis of Molecular Dynamics Simulations」、作者 Gowers/Linke/Barnoud/Reddy…、年 2016、页 98-105、DOI 一致；[33] 标题「plotXVG: Batch Generation of Publication-Quality Graphs from GROMACS Output」（与正文引用的「from GROMACS output」一致）、作者 Rosenbaum/van der Spoel、JCIM、卷期页 66(6):2955-2959、年 2026、DOI 一致 | **已修复** |
| P1-2：3.4.4 定量区间删或加条件 | log 称已加体系/力场/版本条件并标注文档推定，且按 P1-A 将量级校正为 -10⁶～-10⁵ | 正文 L296 现为「以典型显式溶剂单蛋白体系（数百残基、AMBER 类力场、GROMACS 2026 默认设置）为参照，势能通常在 -10⁶ 至 -10⁵ kJ/mol（其量级据 GROMACS 官方教程对显式溶剂蛋白势能的表述[19]）、RMSD 通常在 0.1–1 nm 量级……不构成判据（文档推定，本章未实测）」。区间量级与官方教程（md-intro：simple protein in water 约 10⁵ kJ/mol；Lemkul lysozyme：10⁵–10⁶）一致；条件与依据性质标注完整 | **已修复** |
| P1-3：章标题与 OUTLINE 一致 | log 称 H1 改为「Python 数据处理最小集」 | 正文 H1 = `# Python 数据处理最小集`，与 OUTLINE.md L77「## 第 3 章 Python 数据处理最小集」一致；文件名 03-Python数据处理.md 不变（约定允许） | **已修复** |

## 三、文献抽查清单与核验结果（随机 10 条 + B 级全量定向，六项逐一核对）

随机抽取（System.Random 固定种子 20261029）：8, 42, 32, 43, 39, 16, 29, 30, 28, 22。

| 编号 | 文献 | 核验方式 | 六项/要素核验 | 结果 |
| --- | --- | --- | --- | --- |
| [8] | Python Tutorial: Errors and Exceptions | anysearch extract 官方页 | URL 可打开，标题「8. Errors and Exceptions」吻合 | 通过 |
| [42] | uv 官方文档 | extract docs.astral.sh/uv | URL 可打开，标题「uv」吻合 | 通过 |
| [32] | matplotlib Customizing rcParams | extract 官方页 | URL 可打开，标题「Customizing Matplotlib with style sheets and rcParams」吻合 | 通过 |
| [43] | pip Requirements File Format | extract 官方页 | URL 可打开，标题吻合 | 通过 |
| [39] | Kluyver et al. Jupyter Notebooks 2016 | Crossref API（10.3233/978-1-61499-649-1-87） | 标题/作者（Kluyver、Ragan-Kelley、Pérez、Granger…）/IOS Press 2016/DOI 一致；页码 87-90 经 Harris 2020 官方参考文献列表交叉印证 | 通过 |
| [16] | numpy Broadcasting | extract 官方页 | URL 可打开，标题「Broadcasting」吻合 | 通过 |
| [29] | scipy.signal | extract 官方页 | URL 可打开，标题吻合 | 通过 |
| [30] | Hunter: Matplotlib: A 2D graphics environment | Crossref API（10.1109/MCSE.2007.55） | CiSE 2007, 9(3): 90-95，标题/作者/DOI 全部一致 | 通过 |
| [28] | pandas.DataFrame.rolling | extract 官方页 | URL 可打开，标题吻合 | 通过 |
| [22] | scipy.constants | extract 官方页 | URL 可打开，标题「Constants (scipy.constants)」吻合 | 通过 |
| [2]* | Harris et al. Array programming with NumPy | Crossref API（10.1038/s41586-020-2649-2） | Nature 2020, 585(7825): 357-362，标题/作者/DOI 一致；其参考文献列表同时交叉印证 [3][21][30][39] | 通过 |
| [3]* | McKinney: Data structures for statistical computing | Crossref API + Harris 参考文献列表 | SciPy 2010, 56-61，DOI 10.25080/majora-92bf1922-00a，标题/作者/年 一致 | 通过 |
| [5]* | Gowers et al. MDAnalysis 2016 | Crossref API（10.25080/majora-629e541a-00e） | 六项全齐（见 P1-1 复核） | 通过 |
| [21]* | Virtanen et al. SciPy 1.0 | Crossref API（10.1038/s41592-019-0686-2） | Nat. Methods 2020, 17(3): 261-272，标题/作者/DOI 一致（提取输出超长被截断致单次 JSON 解析失败，但六项原文可见） | 通过 |
| [33]* | Rosenbaum & van der Spoel plotXVG 2026 | Crossref API（10.1021/acs.jcim.5c02998） | 六项全齐（见 P1-1 复核） | 通过 |
| [36]* | Abraham et al. GROMACS 2015 | Crossref API（10.1016/j.softx.2015.06.001） | SoftwareX 2015, 1-2: 19-25，标题/作者/DOI 一致 | 通过 |

\* 为样本外 B 级文献定向补查（B 级必须逐条六项核验，故全量覆盖）。
核验时间：2026-10-29 06:05–06:25。**随机 10 条 + B 级 8 条全部核验，无伪造、无错配、无无法打开**。

> 说明：anysearch 免费额度在完成上述全部核验后耗尽（约 06:25 返回 quota 提示），故本报告未重复抽取已在额度内验证过的 file-formats/user-guide 页面全文；关键 A 级论断已在额度内以 extract 原文验证（见第四节）。

## 四、关键论断抽查（A 级 extract 原文 + 标准事实）

1. gmx energy 统计口径：「Average, RMSD, and drift are calculated with full precision from the simulation (see printed manual)」——官方帮助原文，支撑 3.4.3、3.7.2、常见错误 2 的全精度 vs 抽样口径论断 ✓
2. gmx rms 输出：synopsis「-o [<.xvg>] (rmsd.xvg)」默认输出名；`-tu <enum>`、`-xvg <enum>` 均在选项表 ✓
3. xvg 为 GROMACS 分析工具默认图形输出格式；参考手册 file-formats.html 含 xvg 节（页内锚点 #xvg，页面可打开）✓
4. user-guide「Tutorial material」一节存在（getting-started 页锚点）✓（承托 [19] 的教程材料定位）
5. numpy.loadtxt：comments 支持字符序列、usecols、unpack、默认 float64（[18]，官方页可打开）✓
6. pathlib 自 Python 3.4、PEP 519（os.PathLike）自 3.6、Python 3 源码默认 UTF-8（[12][13][14]，标准事实）✓
7. ProcessPoolExecutor 绕开 GIL 用于计算型、ThreadPoolExecutor 面向 I/O 型（[37]）✓
8. pandas groupby 为 split-apply-combine、merge 为 SQL 风格键连接、pivot 转宽表（[24][25][26] 官方文档）✓
9. subprocess.run 参数列表方式、shell=True 引入 shell 解析与注入风险（[35] 官方文档）✓
10. 显式溶剂蛋白质势能量级 -10⁶～-10⁵ kJ/mol 与官方教程一致（[19]；md-intro 与 lysozyme 教程均 10⁵–10⁶ 量级）；RMSD 0.1–1 nm 为带条件的示意量级 ✓
11. 单位换算 1 kcal=4.184 kJ（热化学卡）、1 nm=10 Å、1 ps=10⁻³ ns、T/°C=T/K−273.15 为 SI 定义 ✓（表 3-2 正确）

## 五、逐节问题清单

| 级别 | 位置 | 问题（原文摘录） | 处置建议 |
| --- | --- | --- | --- |
| P2-1 | 项目级 `_sidebar.md` L5 | 侧边栏仍标「第 3 章 Python 数据处理」(03-Python数据处理.md)，与 OUTLINE/正文 H1「Python 数据处理最小集」不一致 | 统稿时同步为「第 3 章 Python 数据处理最小集」（延续上轮 P2-F 同类项） |
| P2-2 | 3.4.2（L225） | 「对十万行的能量序列，numpy 表达式与等价 Python 循环差了一到两个数量级」——性能量级陈述未在句内显式标注推断/未实测属性（log 已记文档推定） | 句末补「（一般性推断，未实测）」或引 NumPy 官方基准页 |
| P2-3 | refs [5] | MDAnalysis 页码双轨：Crossref/OpenAlex/HAL 登记 98-105，MDAnalysis 仓库写 102-109；本章取登记口径正确 | log 已备注；他章复用同一文献时保持同一写法（非错误，不记级） |
| P2-4 | 上一轮 P1-1 | 复验确认：**已修复**（[5][33] 六项补齐，本轮 Crossref 独立复核一致） | 无需处理 |
| P2-5 | 上一轮 P1-2 | 复验确认：**已修复**（3.4.4 加条件+文档推定标注，量级校正为 -10⁶～-10⁵ 且有 [19] 来源） | 无需处理 |
| P2-6 | 上一轮 P1-3 | 复验确认：**已修复**（正文 H1 与 OUTLINE.md L77 一致） | 无需处理 |

## 六、结论

- **无 P0**：随机 10 条 + B 级 8 条文献全部核验（无伪造、无错配、无无法打开）；字数 13,601 ≥10,000；正文二级节 9/三级节 28/表格 4/图 3/常见错误 8/习题 8/参考文献 44 全部达标；编号 1–44 连续且列表逐条对应（正文 vs refs 0 差异）；跨章无正文级重复（≥25 字符句子指纹比对 02/04/05/06/07 章仅命中表格分隔线与共享文献条目）；无禁用表达、无第二人称、无套话过渡；编码 UTF-8 无 BOM、LF。
- **上一轮 3 条 P1**：全部确认修复（P1-1 六项补齐、P1-2 区间条件化且量级已校正、P1-3 标题一致）。
- **本轮无新 P1**；遗留 3 条 P2 均为项目级/表述级，留待统稿处理。
- **判定：通过（pass=true）**，可进入下一环节。

—— 复核人自检记录：本轮核验 DOI：10.25080/majora-629e541a-00e、10.1021/acs.jcim.5c02998、10.3233/978-1-61499-649-1-87、10.1109/mcse.2007.55、10.1038/s41586-020-2649-2、10.25080/majora-92bf1922-00a、10.1038/s41592-019-0686-2、10.1016/j.softx.2015.06.001（均经 anysearch extract 打开 Crossref 记录）；A 级官方页 extract 8 处 + gmx-rms/gmx-energy/user-guide 3 处。未跳过引文抽查；每条问题均给出可执行修改。