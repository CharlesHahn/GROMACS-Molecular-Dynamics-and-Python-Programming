# 第 3 章 核查日志（fact-check）

> 每条记录一行关键论断。状态三档：已核实（原文可见，含检索结果原文/官方文档正文）、文档推定（官方文档明示或工程惯例归纳，但未在本机实测，正文须标注）、待核实（不得进入终稿）。本章无「待核实」条目。
> 检索纪律执行情况：batch_search 共 7 轮（≤12），extract 共 5 次（≤5，分别为 Harris、Hunter、McKinney、Gowers、plotXVG）；受 extract 次数上限约束，未能逐篇打开全文的 B 级文献采用「多源交叉核验」（≥2 个独立来源，含同行评审论文的参考文献列表、Crossref/OpenAlex、机构仓储）。

| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| xvg 为 GROMACS 分析工具的默认图形输出格式，文件含 `#` 注释行、`@` 注解行与空白分隔的多列数据行 | [4] A：GROMACS 2026.4 参考手册 File format details（manual.gromacs.org/current/reference-manual/file-formats.html）；佐证：GROMACS 官方论坛帖与 GromacsWrapper 文档（D） | 检索结果（手册 TOC 含「File format details」章节；论坛帖展示 `@` 注解行样例） | 已核实 |
| gmx 分析工具统一提供 `-xvg` 选项，取值 xmgrace（默认）/xmgr/none | [17] A：gmx energy 在线帮助；gmx principal、gmx sigeps 在线帮助（2021.6/2022） | 检索结果原文可见（onlinehelp 页截图级文本） | 已核实 |
| gmx rms 默认输出 rmsd.xvg；`-tu` 选项控制时间单位（fs/ps/ns 等） | [15] A：gmx rms 在线帮助（manual.gromacs.org/current/onlinehelp/gmx-rms.html） | 检索结果原文可见（含 synopsis 与 -o (rmsd.xvg)、-tu 说明） | 已核实 |
| gmx energy 交互式提示选择能量项；能量文件含按 nstcalcenergy 步累加的全精度累计值，其统计（均值/RMSD/漂移）与仅含抽样帧的 xvg 口径可能不同；-aver 可将均值写入 xvg | [17] A：gmx energy 在线帮助（2021.2/2021.6 原文提取） | 检索结果原文可见（Description 段逐句对应） | 已核实 |
| 表 3-2 换算因子（1 kcal=4.184 kJ、1 nm=10 Å、1 ps=10⁻³ ns、T/°C=T/K−273.15） | A：[22] scipy.constants 官方文档 + SI 定义；[20] GROMACS Definitions and Units（单位制 nm/ps/kJ/mol/K/bar） | 换算因子为 SI 定义（热化学卡），检索确认 scipy.constants 提供 calorie/Angstrom 常量；GROMACS 内单位制沿用第 2 章已收录文档 | 已核实 |
| NumPy ndarray：同质类型、shape/strides、向量化、广播、掩码（布尔）索引 | [2] B：Harris 2020（Nature 全文 extract 成功） | extract 原文（Fig.1 对 shape/strides/视图/掩码/向量化/广播的说明） | 已核实 |
| 向量化使数组运算下沉到 C 层，相对逐元素 Python 循环有数量级差异 | [2] B：Harris 2020；[16] A：numpy Broadcasting 官方文档 | 依据 Harris 对 NumPy 实现的一般性描述归纳，正文按推断口径表述 | 文档推定（正文已注明为量级差异的一般判断） |
| numpy.loadtxt 支持 comments（单字符或序列）、usecols、unpack、dtype 等参数 | [18] A：numpy.loadtxt 官方文档（numpy.org/devdocs 与 1.8/1.10 手册原文） | 检索结果原文可见（参数列表逐项比对） | 已核实 |
| pandas DataFrame 为带行/列标签的表格结构；groupby/merge/pivot_table/rolling/resample 语义 | [23-28] A：pandas 官方 API 参考与用户指南 | 检索确认各文档路径存在并给出对应语义（DataFrame、groupby 用户指南、merging、reshaping、timeseries、rolling） | 已核实 |
| matplotlib Figure/Axes 对象模型、rcParams 全局配置、savefig 矢量/位图输出 | [30] B：Hunter 2007（多源）；[31,32,34] A：matplotlib 官方文档 | Hunter 六项经多源交叉（Nature 参考文献列表、IEEE 检索、CiSE 卷期页）；matplotlib 文档路径经检索确认 | 已核实 |
| subprocess.run 首参为参数列表；shell=True 引入 shell 解析与注入风险；CompletedProcess.returncode 判定成败 | [35] A：Python subprocess 官方文档 | 检索确认官方文档路径与公开 API 语义 | 已核实 |
| PEP 519 确立 os.PathLike 协议，标准库 open() 等接受 pathlib.Path | [13] A：PEP 519 原文（peps.python.org/pep-0519/） | extract 检索结果原文可见（Abstract/Rationale/Proposal 全文） | 已核实 |
| Python 3 源码默认 UTF-8 编码 | [14] A：Unicode HOWTO | 检索确认官方文档路径（PEP 3120 亦为既有事实） | 已核实 |
| venv/conda/uv 三种环境工具的命令与语义 | [40-42] A：venv、conda manage-environments、uv 官方文档 | 检索确认文档路径；命令语义为公开文档 | 已核实 |
| PEP 440 定义版本识别与依赖说明符（==、>=、< 等） | [44] A：PEP 440 原文 | 检索确认 peps.python.org/pep-0440/ 存在及接受公告（distutils-sig 归档） | 已核实 |
| Harris 2020 六项元数据：Nature, 2020, 585(7825): 357-362, DOI 10.1038/s41586-020-2649-2 | B：Nature | extract 原文页成功；卷期页与 DOI 亦获 SciPy.org 官方引用页交叉 | 已核实 |
| Hunter 2007 六项元数据：Comput. Sci. Eng., 2007, 9(3): 90-95, DOI 10.1109/MCSE.2007.55 | B：CiSE | Nature 参考文献列表 + IEEE 检索结果 + 引用库多源一致；extract 遭 IEEE 拦截（已记录，非内容问题） | 已核实（多源交叉） |
| McKinney 2010 六项元数据：SciPy 2010 论文集 56-61 页 | B：SciPy 2010 | Nature 参考文献列表（页码 56-61）+ scirp + Google Scholar 交叉；extract 遇页面重定向至 DOI 10.25080/Majora-92bf1922-00a | 已核实（多源交叉） |
| Virtanen 2020 六项元数据：Nat. Methods, 2020, 17(3): 261-272, DOI 10.1038/s41592-019-0686-2 | B：Nature Methods | SciPy.org 官方引用页 + Nature 本期页 + 剑桥仓储 + PubMed 多源交叉 | 已核实（多源交叉） |
| Gowers 2016 六项元数据：SciPy 2016 论文集，DOI 10.25080/Majora-629e541a-00e，页码 98-105（修订轮补齐） | B：SciPy 2016 | Crossref/OpenAlex 元数据 + MDAnalysis 源码头注释（DOI 原文可见）；修订轮经 Crossref（page 98-105）、OpenAlex（biblio 98/105）、HAL（pp.98-105）三源交叉 | 已核实（修订轮 2026-10-29 补齐页码） |
| Kluyver 2016 六项元数据：IOS Press 2016, 87-90, DOI 10.3233/978-1-61499-649-1-87 | B：IOS Press 图书章节 | Nature 参考文献列表（出版社、页码 87-90）+ Crossref 检索（DOI）交叉 | 已核实（多源交叉） |
| Abraham 2015 六项元数据：SoftwareX, 2015, 1-2: 19-25, DOI 10.1016/j.softx.2015.06.001 | B：SoftwareX | 沿用第 2 章已核验记录（六项齐全），本轮再经检索多源交叉 | 已核实 |
| Rosenbaum plotXVG：JCIM, 2026, 66(6): 2955-2959, DOI 10.1021/acs.jcim.5c02998，双作者（Rosenbaum/van der Spoel）（修订轮补齐） | B：JCIM（pubs.acs.org 文章页） | 原轮检索（标题、卷期页自 ACS 页面）；修订轮经 Crossref 出版商登记记录（issue 6、page 2955-2959、DOI、作者两人）确认 | 已核实（修订轮 2026-10-29 补齐 DOI 与页码） |
| 「数据处理—流程驱动—功能扩展」三类任务划分与图 3-1（图 3-2/3-3） | 本书方法论组织框架 | 非外部论断，属本书分析架构，经内部一致性复核 | 框架性表述（不构成外部事实断言） |
| 出版作图 rcParams 起点（font.size 8–10 pt、线宽 1.0–1.5 pt、figsize 3.5/7.0 in、dpi≥300、表 3-3） | 出版惯例归纳 + [32,34] A：matplotlib 文档 | 惯例性建议，正文已注明「以目标期刊指南为准」依据性质 | 文档推定（正文已注明） |
| 滑动平均窗口应取轨迹总长 1%–10% 以内且不小于一个自相关时间量级；示例 500 帧=1 ns 为示意值 | 推断（严格依据见第 9 章自相关讨论） | 正文已注明示例值与原则性质 | 文档推定（正文已注明） |
| ProcessPoolExecutor 的 max_workers 建议取物理核数一半到三分之二 | 工程惯例归纳 | 正文已注明推断性质 | 文档推定（正文已注明） |
| gmx energy 交互选择序号「16 0」为示意，随版本与体系而异 | 示例性说明 | 正文已注明需先手工确认编号 | 示意标注（正文已注明） |
| 图 3-2 xvg 解析管线、图 3-3 subprocess 数据流 | 本书示意图 | 依据第 3、4、5 行已核实的文档行为绘制 | 已核实（依据已核实行） |
| 目录名解析元数据（T300→300 K）与可解析命名约定 | 本书与第 2 章共同约定 | 属写作约定而非外部事实 | 框架性表述 |

注明：修订轮（2026-10-29）按验收报告 P1-1 补齐 [5]（页码 98-105）与 [33]（DOI 10.1021/acs.jcim.5c02998、页码 2955-2959）元数据，正文与 refs 中的「待补」注记均已移除，B 级文献六项信息齐全。A 级在线文档均标注访问日期 2026-10-28。本章正文未声称任何「经本机实测」的结果；所有适合实测的环节按规则标注为文档推定或示意。

## 修订记录（2026-10-29，P1 修订轮）

依据 03-review.md 清单逐条修订，正文（03-Python数据处理.md）、refs（refs/03-refs.md）同步更新。本轮检索执行：anysearch search 2 次（≤12 轮限额内）；extract 0 次（ACS 与 PubMed 页均拦截，改以 Crossref 出版商登记记录与论文集官网为准）；Crossref/OpenAlex API 3 次、SciPy 论文集官网 2 次。

| 修订项 | 修订内容 | 核验/依据 | 状态 |
| --- | --- | --- | --- |
| P1-1a：文献 [5] 补页码 | [5] 补页码 98-105，删除「卷期页待补」注记 | Crossref（page 98-105）+ OpenAlex（biblio first_page 98 / last_page 105）+ HAL 仓储（pp.98-105）三源一致 | 已完成 |
| P1-1b：文献 [33] 补 DOI 与结束页码 | [33] 补 DOI 10.1021/acs.jcim.5c02998、页码 2955-2959、第二作者 van der Spoel D，标题按官方记录改为「from GROMACS output」，删除「待补」注记 | Crossref 出版商登记记录（publisher ACS，volume 66、issue 6、page 2955-2959、DOI、双作者），与 pubs.acs.org/jcisd8/article/66/6/2955/5080399/ 页码一致 | 已完成 |
| P1-2：3.4.4 定量区间加条件 | 删除无条件断言的「能量 -10⁵～-10⁴ kJ/mol、RMSD 0.1–1 nm」区间，改为带适用条件的示意量级（典型显式溶剂单蛋白、数百残基、AMBER 类力场、GROMACS 2026），注明「仅用于量级抽查、不构成判据、文档推定（本章未实测）」 | 按 REVIEW 二.4 补条件与依据性质；正文标注文档推定 | 已完成 |
| P1-3：章标题对齐 OUTLINE | 正文 H1 由「Python 数据处理」改为「Python 数据处理最小集」，与 OUTLINE「第 3 章 Python 数据处理最小集」一致；文件名 03-Python数据处理.md 不变 | OUTLINE.md L77 | 已完成 |

修订轮新增论断行：

| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| 3.4.4 量级抽查示意：典型显式溶剂单蛋白（数百残基、AMBER 类力场、GROMACS 2026）势能约 -10⁶～-10⁵ kJ/mol（量级据 GROMACS 官方教程）、RMSD 约 0.1–1 nm；仅用于触发人工复核的量级抽查，不构成判据 | 经验量级归纳，受体系/力场/版本约束；量级与 GROMACS 官方 Tutorial 材料对显式溶剂蛋白势能的表述一致 | 复审修订轮（2026-10-29）按 P1-A 修正区间（原 -10⁵～-10⁴ 偏小一个数量级）；md-intro 教程与 Lemkul lysozyme 教程 extract 原文均称 Epot 为 10⁵–10⁶ kJ/mol 量级（见复审修订记录），正文已注明适用条件与「文档推定」性质 | 文档推定（正文已注明） |

## 修订记录（2026-10-29，P1 复审后修订轮）

依据 03-review.md 复验报告（返工单点 P1-A）修订：正文（03-Python数据处理.md）与 refs（refs/03-refs.md）同步更新，本日志同步登记。本轮检索执行：anysearch batch_search 1 次（4 查询，≤12 轮限额内）；extract 4 次（tutorials.gromacs.org 教程两页、manual.gromacs.org gmx-rmsf 与 user-guide 索引页）。

| 修订项 | 修订内容 | 核验/依据 | 状态 |
| --- | --- | --- | --- |
| P1-A：3.4.4 势能量级区间 | 区间由「-10⁵ 至 -10⁴ kJ/mol」改为「-10⁶ 至 -10⁵ kJ/mol」，补「其量级据 GROMACS 官方教程对显式溶剂蛋白势能的表述[19]」；RMSD 0.1–1 nm 不变；适用条件与「不构成判据（文档推定，本章未实测）」表述保留 | GROMACS 官方 md-intro 教程（tutorials.gromacs.org/docs/md-intro-tutorial.html，Bergh C/Majdolhosseini M/Villa A，Zenodo 10.5281/zenodo.11198375）extract 原文：「Epot should be negative and (for a simple protein in water) on the order of 100000 kJ/mol, depending on the system size and number of water molecules」；Lemkul lysozyme 教程（mdtutorials.com/gmx/lysozyme）extract 原文：「Epot should be negative, and (for a simple protein in water) on the order of 105-106」；Samson GROMACS Wizard 文档同表述；[19]（User guide: Tutorial material，manual.gromacs.org/current/user-guide/index.html）索引页含「Tutorial material」一节，与教程站点对应 | 已完成 |
| P2-A：3.4.4「多数 gmx 分析工具自带 -tu」 | 改为「部分时间序列类工具（如 gmx rms）自带 -tu」，示例句同步调整（`gmx rms -tu ns`） | gmx energy 2026.4 synopsis 无 -tu（上一轮已证实）；本轮 extract gmx rmsf 2026.4 synopsis 亦无 -tu（选项仅 -f/-s/-n/-q/-oq/-ox/-o/-od/-oc/-dir/-b/-e/-dt/-w/-xvg/-res/-aniso/-fit）；gmx rms 具 -tu（[15]：fs/ps/ns/us/ms/s）——故仅点名 gmx rms | 已完成 |
| P2-B：3.4.1 代码注释列数 | 注释「（时间、势能、温度两列）」改为「（时间、势能、温度三列）」，与形状 (N, 3) 及注释「例如 (10001, 3)」一致 | 内部一致性核对（正文 3.4.1 例） | 已完成 |
| P2-C：习题 2 目录前缀 | 「ran/」统一为「runs/」，与 3.3.3 批量遍历示例及 config.py 的 runs/ 约定一致 | 内部一致性核对（3.3.3、3.8.2） | 已完成 |
| P2-D：文献 [13] 作者 | 补第二作者：Cannon B, Zevenhoven K（正文与 refs/03-refs.md 同步） | CPython 3.6 what's new 原文：「PEP written by Brett Cannon and Koos Zevenhoven」；PEP 519 提案页与 python-dev 表决邮件（2016-05，Guido 批准）均列两位作者 | 已完成 |
| P2-E：3.9.2 锁文件表述 | 「pip-tools 生成的 constraints 均属此类」改为「pip-tools（pip-compile）生成的锁定 requirements.txt 均属此类」 | pip-tools 官方文档（pip-tools.readthedocs.io）：「pip-compile generates a requirements.txt file using the latest versions that fulfil the dependencies you specify」；constraints 为 -c/--constraint 独立机制（与 requirements.in 分属不同输入），故原表述不准确 | 已完成 |
| P2-F：项目级（_sidebar/glossary/figures） | 本章不改动：按验收报告建议，属全书统稿范畴——统稿时按 OUTLINE 重写 _sidebar、建立 glossary.md；本章图 3-1/3-2/3-3 均为 Mermaid，无需在 figures/TODO-figures.md 占位登记（符合 STYLE） | 03-review.md P2-F 备注 | 已登记（留待全书统稿处置） |
| 文献 [5] 页码双轨备注 | 登记分歧：Crossref/OpenAlex/HAL 与官方文档登记为 98-105，而 MDAnalysis GitHub 仓库及作者实验室页面写作 102-109；本章采用登记口径 98-105，其他章节复用该文献时保持同一写法，勿改换 | 03-review.md 说明项 | 已备注（非错误，不记级） |