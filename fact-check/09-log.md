# 第 9 章 核查日志（fact-check）

> 每条记录一行关键论断。状态三档：已核实（原文可见，含官方文档检索/提取原文、Crossref 元数据核验）、文档推定（官方文档明示或实际行为可证但未在本机实测，正文须标注）、待核实（不得进入终稿）。本章无「待核实」条目。
> 核验通道说明：A 级论断以 web_fetch 抓取 manual.gromacs.org 2026.4 在线版原文（gmx analyze、gmx energy、mdrun-features）或 anysearch 检索到的官方文档原文片段（mdp-options、参考手册 Covariance analysis）为准；B 级文献六项信息以 Crossref REST API（filter=doi / query.bibliographic）核验「题名、作者、期刊、年份、卷期页、DOI」，个别条目另以 anysearch 检索的出版商/PubMed 页复核。

| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| gmx analyze 提供 -ac（归一化自相关函数，-subav 默认减均值、-acflen 默认 ACF 长度取帧数一半）与 -ee（块平均误差估计，含块间方差公式与双指数解析拟合）；»数据点间隔须远小于自相关时间尺度«是官方提示 | A：gmx analyze 联机帮助（2026.4） | web_fetch 原文（manual.gromacs.org/current/onlinehelp/gmx-analyze.html） | 已核实 |
| gmx analyze -ee 解析块平均曲线的推导出处为 B. Hess, J. Chem. Phys. 116:209-217, 2002 | A：gmx analyze 说明文字；B：Hess 2002 JCP 元数据 | 官方文档原文可见该引用；Hess 2002 题名/卷期页经 Crossref 核验（Determining the shear viscosity…, JCP 116(1):209-217） | 已核实 |
| gmx energy 统计输出：均值、RMSD、漂移经能量文件内全精度平均计算；误差估计基于块平均（默认 5 块，-nbmin/-nbmax 可指定块数范围）；能量文件含 MD 步级平均，比 xvg 帧更准 | A：gmx energy 联机帮助（2026.4） | web_fetch 原文（onlinehelp/gmx-energy.html） | 已核实 |
| -reprod 模式消除单次运行内的可变性：同输入同硬件重复调用逐位一致；换硬件或编译器不保证；官方建议仅用于排查问题 | A：User guide: Useful mdrun features（2026.4） | web_fetch 原文（user-guide/mdrun-features.html） | 已核实 |
| 多模拟（-multidir）可在一次 mdrun 中运行多条独立模拟；副本交换需 -replex 与 -reseed | A：User guide: Useful mdrun features（2026.4） | web_fetch 原文 | 已核实 |
| 检查点续算精确性受代码/编译器/架构/进程数/GPU 使用限制（同条件下续算二进制精确） | A：User guide: Managing long simulations（2026.4） | 既有核验（第 6 章已 extract 同页「Are continuations exact?」）+ 本次检索定位 | 已核实 |
| gen-vel 默认 no（不生成初速度）；gen-seed 默认 −1（生成随机种子） | A：mdp-options（2026.4） | anysearch 检索官方原文片段（「Velocity generation¶ gen-vel¶ no¶…」；「The default value of -1 generates a random seed」） | 已核实 |
| 参考手册协方差分析一节：建议用前后两半程的主成分子空间重叠检验主模定义（两半须用同一参考结构）；余弦含量接近 1 说明主成分主导涨落来自随机扩散而非势能 | A：Reference manual: Covariance analysis | anysearch 检索官方原文片段（2023.1 版全文可见，2026 版页面路径同名并存在于导航） | 已核实 |
| 块平均标准误公式与「误差随块长增大进入平台」判据；Flyvbjerg & Petersen 提出该方法（JCP 1989, 91(1):461-466） | B：Flyvbjerg 1989 元数据 + 方法学 | Crossref（六项）核验 + 检索原文摘要（AIP/ADS 可见方法描述） | 已核实 |
| 统计低效因子 s=1+2τ_int、有效样本数 N_eff=N/s；Straatsma/Berendsen/Stam 1986 Mol.Phys. 57(1):89-95 定义统计误差框架 | B：Straatsma 1986 元数据 | Crossref 六项核验；公式与教材（Frenkel & Smit，C 级）口径一致 | 已核实 |
| 刀切法出自 Quenouille 1956（Biometrika 43(3/4):353-360）；自助法出自 Efron 1979（Ann. Statist. 7(1):1-26） | B：Quenouille 1956 / Efron 1979 | Crossref 六项核验（两篇题名、卷期页、DOI 全部命中） | 已核实 |
| TI 出自 Kirkwood 1935（JCP 3(5):300-313）；FEP 指数平均出自 Zwanzig 1954（JCP 22(8):1420-1426）；BAR 出自 Bennett 1976（JCP 22(2):245-268）；MBAR 出自 Shirts & Chodera 2008（JCP 129(12):124105） | B：四篇原始文献 | Crossref 六项核验（四篇均命中；MBAR 文章号 124105 经 Crossref article-number 字段核验） | 已核实 |
| WHAM 原始方法出自 Kumar 等 1992（JCC 13(8):1011-1021）；WHAM 收敛与误差估计见 Zhu & Hummer 2012（JCC 33(4):453-465） | B：Kumar 1992 / Zhu-Hummer 2012 | Crossref 六项核验（两篇均命中） | 已核实 |
| 本质动力学/PCA 的协方差分析出自 Amadei/Linssen/Berendsen 1993（Proteins 17(4):412-425） | B：Amadei 1993 | Crossref 六项核验命中（Proteins: Structure, Function, and Bioinformatics） | 已核实 |
| 前后半段/子空间重叠式收敛分析出自 Lyman & Zuckerman 2006（Biophys. J. 91(1):164-172） | B：Lyman & Zuckerman 2006 | Crossref 六项核验命中（注意：该文 DOI 为 10.1529/biophysj.106.082941，曾误记为 084293，经 Crossref filter=doi 查证后更正） | 已核实 |
| 自动平衡段截断（最大化保留段有效样本数）出自 Chodera 2016（JCTC 12(4):1799-1805） | B：Chodera 2016 | Crossref 六项核验命中；PubMed 26771390 同题复核 | 已核实 |
| 与实验对照的系统性注意事项（平均方式、条件匹配）见 van Gunsteren & Mark 1998（JCP 108(15):6109-6116） | B：vG&M 1998 | Crossref 六项核验命中 | 已核实 |
| MM-PBSA 类连续介质近似水溶剂方法的模型误差示例出自 Kollman 等 2000（Acc. Chem. Res. 33(12):889-897） | B：Kollman 2000 | Crossref 六项核验命中 | 已核实 |
| 可复现十条规则出自 Sandve 等 2013（PLoS Comput. Biol. 9(10):e1003285） | B：Sandve 2013 | Crossref 六项核验命中 | 已核实 |
| 自由能计算良好实践清单出自 Pohorille/Jarzynski/Chipot 2010（JPCB 114(32):10235-10253） | B：Pohorille 2010 | Crossref 六项核验命中 | 已核实 |
| 最佳实践文献（不确定性与采样质量量化）出自 Grossfield 等（LiveCoMS 1(1):5067；DOI 10.33011/livecoms.1.1.5067） | B：Grossfield 2018 | Crossref 六项核验命中；DOI 解析指向 livecomsjournal.org（年份：Crossref 记 2019，期刊 v1.0 惯例引用 2018，正文按 2018 并在 refs 说明） | 已核实（年份注释见 refs 说明） |
| 自相关、统计低效因子与中心极限定理的统计力学表述见于 Frenkel & Smit 2002 教材与 Berendsen 2007 教材（C 级） | C：教材 | 既有教学知识 + 检索定位；正文以教材共识标注，不承担方法学结论 | 已核实（C 级） |
| 采样不足量级（蛋白常规采样不足以收敛慢二面角/构象分布）出自 Hess 2002 PRE 65(3):031910 | B：Hess 2002 PRE | Crossref 六项核验命中 | 已核实 |
| MDAnalysis 轨迹分析库及其半径回转让等接口出自 Michaud-Agrawal 等 2011（JCC 32(10):2319-2327） | B：Michaud-Agrawal 2011 | Crossref 六项核验命中（注意：该文期刊为 JCC 而非早期误记的 Bioinformatics，DOI 10.1002/jcc.21787 经查证） | 已核实 |
| 通用论断：快慢模式分离、有效样本数量级、块长与重抽样次数经验取值、实验扩散系数有限尺寸影响 | 教材共识 / 最佳实践归纳 | 全部在正文标注「教材共识」或「文档推定」，不含未核实的精确数值；涉及数值处均注明依体系变化 | 已核实（表述层面） |

## 检索过程说明

- 检索通道：anysearch CLI（batch_search 调用 5 次，共 17 条查询；未使用 extract），web_fetch 抓取官方文档 5 页（gmx analyze、gmx energy、mdrun-features 三页全文；Crossref API 批量核验元数据约 25 次）。
- B 级文献六项全部经 Crossref REST（api.crossref.org）逐条核验；核验中纠正两处记忆错误：Lyman & Zuckerman 2006 的正确 DOI 为 10.1529/biophysj.106.082941（非 …084293）；MDAnalysis 文献的正确出处为 J. Comput. Chem. 32(10):2319-2327（DOI 10.1002/jcc.21787，非 Bioinformatics/btr161）。两处均已在 refs 与正文落定。
- A 级论断未在本机实测，凡涉及运行表现处均按「文档推定」或直接引用官方说明；正文未出现「经实测」类表述。
- 正文标注一致性：累计平均仅必要非充分、块长经验取值、副本数经验取值、XTC 3 位小数精度等均标「教材共识/文档推定」；where 涉及具体数值（如低估倍数示例、τ_int 数量级）均注明「依体系与版本变化」。
- 占位：正文与 refs 均无「待补/待核实」条目；[3] 的年份约定在 refs 头部与本节说明中留痕。