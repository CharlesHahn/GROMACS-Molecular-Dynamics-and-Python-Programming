# 第 9 章 核查日志（fact-check）

> 每条记录一行关键论断。状态三档：已核实（原文可见，含官方文档检索/提取原文、Crossref 元数据核验）、文档推定（官方文档明示或实际行为可证但未在本机实测，正文须标注）、待核实（不得进入终稿）。本章无「待核实」条目。
> 核验通道说明：A 级论断以 web_fetch 抓取 manual.gromacs.org 2026.4 在线版原文（gmx analyze、gmx energy、mdrun-features）或 anysearch 检索到的官方文档原文片段（mdp-options、参考手册 Covariance analysis）为准；B 级文献六项信息以 Crossref REST API（filter=doi / query.bibliographic）核验「题名、作者、期刊、年份、卷期页、DOI」，个别条目另以 anysearch 检索的出版商/PubMed 页复核。
> 修订记录：2026-11-04 按 peer-09-review v2 的 priorityActions 完成深度补强修订（τ_int 定量、块平均低估因子与平台判定、tICA/隐含时间尺度、Yeh–Hummer 修正、pymbar.timeseries、E1/E2/E5/E7 回填、编号重排 1..40）。本轮核验通道仅 anysearch CLI（search/batch_search/extract，未调用 web_search）：新增 7 条引文逐一核验（见下方新增行）；Good & Berkowitz 经四次检索未确认，未引用，深度诉求由 [10] Sokal 1997 与已引 [9] Straatsma 1986 承担。

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
| τ_int 估计量相对不确定度 ≈ √(2τ_int/T)（近指数相关尾）与窗口化积分（W 取使 τ_int(W) 平台化的最小窗口）出自 Sokal 1997 讲义 | C 级权威讲义：Sokal 1997（NATO ASI Ser. B 361: 131-192） | anysearch search 核验（INSPIRE 记录 NATO Sci.Ser.B 361 (1997) 131-192；Springer 章 DOI 10.1007/978-1-4899-0319-8_6）；正文标注「经典论述见文献[10]」 | 已核实 |
| 均值减除 ACF 长滞后系统负偏（量级 O(τ_int/N)）→「伪过零」使首次过零截断偏早；负尾/振荡 ACF（压力、应力、速度）下首次过零失效，宜尾部拟合（gmx analyze -fitfn exp_exp）或窗口化积分 | Sokal 1997 + A：gmx analyze 官方文档 | gmx analyze -fitfn 选项既有核验；偏导数理与伪过零为时间序列经典结论，正文按教材共识标注 | 已核实（表述层面） |
| pymbar.timeseries：statistical_inefficiency（g=1+2τ，fft 选项）、integrated_autocorrelation_time、detect_equilibration（t0/g/Neff_max，实现 Chodera 2016）、subsample_correlated_data；官方文档明示 MBAR 仅适用于不相关样本 | A：pymbar 4.2.x 官方文档 timeseries.html | anysearch extract 逐函数核验（页面标题 4.2.1.dev1；原文引 Chodera JCTC 12:1799, 2016） | 已核实 |
| 块平均低估因子 γ²=s_L/s，s_L=1+2Σ_{k=1}^{L−1}(1−k/L)c(k)；近指数序列极限 ≈√(L/(1+2τ_int))，L=τ_int/2 时约低估 40%–50%；交叉核对式 SE_plateau²·N/σ_A²≈1+2τ_int | B：Flyvbjerg & Petersen 1989 [13]（已核实）+ Sokal 1997 [10] | 教材级标准推导复核；正文标注教材共识并引 [13][10] | 已核实（表述层面） |
| 块自助形式化始于 Künsch 1989；时间序列文献对最优块长给随 N 幂律标度（方差估计口径约 N^{1/3}） | B：Künsch 1989（Ann. Statist. 17(3):1217-1241） | anysearch 核验 projecteuclid 全文页/JSTOR/Crossref（DOI 10.1214/aos/1176347265）；标度关系标注时间序列文献结果 | 已核实 |
| 多副本一致后逆方差加权合并：⟨A⟩_pool=ΣᵢwᵢAᵢ/Σᵢwᵢ、wᵢ=1/SEᵢ²、SE_pool=1/√(Σᵢ1/SEᵢ²)；副本数提供异常检测覆盖度而非收敛证明 | 教材级标准结果 + B：Gapsys 2020 佐证 | 加权平均标准公式；「副本一致≠收敛」与 Gapsys 2020 的 N=1 反例演示一致 | 已核实（表述层面） |
| 单次模拟考察盒尺寸等系统参数易得虚假趋势，重复次数足够才能区分系统效应与采样涨落（蛋白水溶液扩散、结合自由能两例） | B：Gapsys & de Groot 2020（eLife 9:e57589） | anysearch 核验 eLife 页面/PubMed 32812868/PMC7481008（DOI 10.7554/eLife.57589） | 已核实 |
| tICA 以时间滞后协方差最大化慢度，由构象动力学变分原理给出最优慢子空间；输出按隐含时间尺度排序，可用作 MSM 输入与收敛判据 | B：Pérez-Hernández 等 2013（JCP 139(1):015102） | anysearch 核验 PubMed 23822324（引文 DOI 10.1063/1.4811489）、AIP 文章页与多家仓储引用链 | 已核实 |
| 扩散系数有限尺寸修正 D_∞≈D_PBC+k_BT·ξ/(6πηL)（立方盒 ξ≈2.837）；水等简单体系可定量消除盒尺寸依赖；大溶质体系需另行评估 | B：Yeh & Hummer 2004（JPCB 108:15873-15879） | anysearch 核验 MPG.PuRe 原文摘要（公式逐字一致）+ Semantic Scholar 元数据（DOI 10.1021/jp0477147）+ TAMU vivo 引用链 | 已核实 |
| 与实验比较定量口径：|⟨A⟩_sim−A_exp| 与 σ_tot=√(σ_stat²+σ_model²+σ_exp²) 比较；NOE 反算按 ⟨r⁻⁶⟩⁻¹/⁶、化学位移按玻尔兹曼权重、连同实验误差入 χ² 判据 | 教材共识；框架见 [33] vG&M 1998 与 [3] 最佳实践 | 表述按教材共识标注，出处复用已核验 [33][3] | 已核实（表述层面） |
| 手册协方差分析节区分「采样重叠（按协方差矩阵平方根定义的标量，手册式 469）」与「子空间重叠（式 470）」两个度量；两半须用同一参考结构 | A：参考手册 Covariance analysis（2026.4） | anysearch extract 原文（式 467–471 逐式核对；「overlap of the sampling between the first and second half」原文） | 已核实 |
| FAIR 数据原则（可发现/可访问/可互操作/可复用）出自 Wilkinson 等 2016（Sci. Data 3:160018） | B：Wilkinson 2016 | anysearch 核验多家权威仓储与官方引用（DOI 10.1038/sdata.2016.18；卷 3、文章号 160018、题名/作者全） | 已核实 |
| MBAR 不确定性以各态样本先去相关（子采样/块化）为前提，直接喂相关轨迹低估自由能误差（pymbar 官方文档）；一阶误差传播对 exp/log/倒数失效（Jensen 偏差）；Σ 的考虑自相关估计 = 同块长块均值序列的样本协方差 | A：pymbar 文档原文 + 教材级标准结果 | pymbar timeseries 文档开头原文核验；传播边界与协方差处方按教材共识标注 | 已核实（表述层面） |
| AR(1) 合成数据自校验：ρ=0.9 时 τ_int=ρ/(1−ρ)=9、s=1+2τ_int=19，SE_plateau²·N/σ²≈19 | 教材级标准结果 | AR(1) 自相关几何衰减解析复核（s=19 自洽） | 已核实（表述层面） |
| E1 数值案例：1.0×10⁶ 帧、间隔 2 ps、τ_int=1.2 ns → s=1201、N_eff≈8.3×10²、独立样本公式低估 ≈35 倍 | 数值演算（示意，正文标注） | 自算核验：600 帧×2 ps=1.2 ns；√1201≈34.7；N_eff≈832.6 | 已核实（表述层面） |
| gmx energy 内建块平均（默认 5 块、基于能量文件内全精度平均）与对导出 xvg 自行块平均的差异来源：平均口径、块数与误差公式、等间距与导出精度；能量类量信内建，非能量导出量须自行块平均 | A：gmx energy 官方文档（2026.4） | 既有核验（上文 gmx energy 行）+ 官网行为推理，正文按案例解剖呈现并标注文档推定 | 已核实 |

## 检索过程说明

- 检索通道：anysearch CLI（batch_search 调用 5 次，共 17 条查询；未使用 extract），web_fetch 抓取官方文档 5 页（gmx analyze、gmx energy、mdrun-features 三页全文；Crossref API 批量核验元数据约 25 次）。
- B 级文献六项全部经 Crossref REST（api.crossref.org）逐条核验；核验中纠正两处记忆错误：Lyman & Zuckerman 2006 的正确 DOI 为 10.1529/biophysj.106.082941（非 …084293）；MDAnalysis 文献的正确出处为 J. Comput. Chem. 32(10):2319-2327（DOI 10.1002/jcc.21787，非 Bioinformatics/btr161）。两处均已在 refs 与正文落定。
- A 级论断未在本机实测，凡涉及运行表现处均按「文档推定」或直接引用官方说明；正文未出现「经实测」类表述。
- 正文标注一致性：累计平均仅必要非充分、块长经验取值、副本数经验取值、XTC 3 位小数精度等均标「教材共识/文档推定」；where 涉及具体数值（如低估倍数示例、τ_int 数量级）均注明「依体系与版本变化」。
- 占位：正文与 refs 均无「待补/待核实」条目；[3] 的年份约定在 refs 头部与本节说明中留痕。

### 2026-11-04 深度补强修订轮

- 通道：仅 anysearch CLI（search/batch_search/extract 约 15 次调用，含 batch_search、单条 search、extract 官方文档/PubMed/Semantic Scholar/MPG.PuRe/语义仓储），未调用 web_search。
- 新增引文六项核验：Sokal 1997（INSPIRE + Springer 章目，DOI 10.1007/978-1-4899-0319-8_6）；Yeh & Hummer 2004（MPG.PuRe 原文摘要公式 + Semantic Scholar 元数据，DOI 10.1021/jp0477147，卷期页 108:15873-15879）；Pérez-Hernández 等 2013 tICA（PubMed 23822324 引文 + AIP 文章页 + 引文链，DOI 10.1063/1.4811489，JCP 139(1):015102）；pymbar.timeseries（官方文档逐函数 extract，4.2.x）；Künsch 1989（projecteuclid/JSTOR，DOI 10.1214/aos/1176347265）；Gapsys & de Groot 2020（eLife/PubMed/PMC，DOI 10.7554/eLife.57589，卷 9 文章号 e57589；注意正式题名为「…for thermodynamics, kinetics and simulation box size」，peer 报告转述的 setup 版题名有误，已按正式题名入库）；Wilkinson 等 2016 FAIR（Sci. Data 3:160018，DOI 10.1038/sdata.2016.18）。tICA 文章 DOI 曾出现补充材料 DOI（10.1063/1.4811489 亦见于补充材料锚点）与候选 10.1063/1.4811099 的混淆，最终以 PubMed 引文与 AIP 发布引用链双向确证 10.1063/1.4811489 为文章 DOI。
- Good & Berkowitz：经四次检索未确认，未入库；peer-09-review priorityActions 8 的深度诉求由 [10] Sokal 1997 与已引 [9] Straatsma 1986 落实，refs/09-refs.md 头部留痕说明。
- 编号治理：正文与 refs 全部重排为 1..40 严格递增（新增 [10][12][18][28][30][35][38]），已程序化复核首现次序（见交付说明）。
- 未处理项：STYLE.md/OUTLINE.md 的「习题移除→延伸讨论」治理留痕属全局事项（peer-09 priorityActions 7 与 peer-07 同项），超出本任务「只修订 09 正文/refs/09-log」的范围，移交主编/统稿轮处理。