# 第 8 章 核查日志（fact-check）

| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| 自由能由配分函数对数给出，ΔG=ΔH−TΔS | B：Kollman 2000 [12]；教材共识 | 原始文献 | 已核实 |
| TI 的 dA/dλ=⟨∂H/∂λ⟩ | B：Kirkwood 1935 [2]；A：GROMACS 手册 [1] | 原始文献+手册 | 已核实 |
| FEP 单侧指数平均 | B：Zwanzig 1954 [4] | 原始文献 | 已核实 |
| BAR 方差最优、gmx bar 实现 | B：Bennett 1976 [5]；A：gmx bar 文档 [6] | 原始文献+手册 | 已核实 |
| MBAR 协方差、需外部 pymbar | B：Shirts & Chodera 2008 [7]；A：手册 [1] | 原始文献+手册 | 已核实 |
| soft-core Beutler 形式、sc-alpha/power 语义 | A：GROMACS 2026.4 mdp 文档 [8] | 官方文档 | 已核实 |
| calc-lambda-neighbors 默认 1 | A：GROMACS 2026.4 mdp 文档 [8] | 官方文档 | 已核实（修订轮） |
| pull=yes + pull-coord1-type=umbrella | A：GROMACS 2026.4 mdp 文档 [8] | 官方文档 | 已核实（修订轮） |
| 伞形采样偏置势、PMF 定义 | B：Torrie & Valleau 1977 [3]；Roux 1995 [9] | 原始文献 | 已核实 |
| WHAM 自洽方程、gmx wham 选项 | B：Kumar 1992 [11]；A：gmx wham [10] | 原始文献+手册 | 已核实 |
| MM-PBSA/GBSA 能项分解 | B：Kollman 2000 [12]；Srinivasan 1998 [13] | 原始文献 | 已核实 |
| MM-PBSA 单轨迹近似局限 | B：Kollman 2000 [12]；综述 | 原始文献 | 已核实 |
| PCA/essential dynamics | B：Amadei 1993 [17]；A：gmx covar [内部] | 原始文献+手册 | 已核实 |
| MSM 构建与 CK 检验 | B：Pande 2010 [18] | 原始文献 | 已核实 |
| PLUMED 集成、PLUMED_KERNEL、thread-MPI 限制 | A：GROMACS 2026.4 手册 [1]；B：Tribello 2014 [20] | 官方文档+文献 | 已核实 |
| REPLICA exchange | B：Sugita & Okamoto 1999 [19] | 原始文献 | 已核实 |
| WTM 收敛于 (1−1/γ)F | B：Bussi & Laio 2020 [24] | 原始文献 | 已核实 |
| OPES 偏置形式与 BARRIER 语义 | B：Invernizzi & Parrinello 2020 [25]；A：PLUMED 文档 [22] | 原始文献+手册 | 已核实 |
| AWH mdp 参数组 | A：GROMACS 2026.4 AWH 文档 [26] | 官方文档 | 已核实 |
| gmx hbond 距离 0.35 nm/30° | A：gmx hbond 文档 [in] | 官方文档 | 已核实 |
| hbond-legacy -life/-ac | A：gmx hbond-legacy [28] | 官方文档 | 已核实 |
| 氢键动力学 Luzar-Chandler | B：Luzar & Chandler 1996 [27] | 原始文献 | 已核实 |
| Jarzynski 等式 | B：Jarzynski 1997 [29] | 原始文献 | 已核实 |
| 增强采样概念框架 | B：Valsson 2016 [30] | 原始文献 | 已核实 |
| gmx select 按时变选择 | A：gmx select [15] | 官方文档 | 已核实 |
| gmx trjconv -pbc/-center | A：gmx trjconv [14] | 官方文档 | 已核实 |
| VMD 可视化 | B：Humphrey 1996 [16] | 原始文献 | 已核实 |
| 引用编号 1-30 首现顺序一致 | 自检 | 脚本实测 | 已核实（修订轮） |
| 汉字数 ≥10,000 | 自检 | STYLE 口径脚本 | 已核实 |

注：修订轮（2026-10-29）处理了验收 P0/P1：标题编号断裂（8.4.2→8.1.4）、calc-lambda-neighbors 默认值、pull 参数、学习目标/前置知识补入、引用编号重排（1-30 严格首现顺序）、[13]/[15] DOI 补齐、[14] 引用错位修正、文献补足至 30 条。缺失的小节内 gmx covar/anaeig/cluster/sham 文档定位以 [1]/[8]（官方手册与 mdp 文档）覆盖，未单列条目，已在统稿阶段标注。
## 引文层二次修订（2026-10-30，终验轮）
| 项 | 处置 | 依据 |
| --- | --- | --- |
| refs[27] Luzar & Chandler 页码 | 55-58 → 55-57（正文文献表与 refs 两处同步） | Nature 官网引用框/Crossref/OpenAlex/Google Scholar/ResearchGate 六路一致（验收者核验） |

## 面向同行深度补强轮（2026-11-04，按 peer-08-review priorityActions）
| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| couple-moltype/lambda0/lambda1/intramol 语义；couple-intramol 默认 no；隐式构造 B 态 | A：GROMACS mdp 选项文档（2026.4 索引确认存在）+ Free energy implementation 页（2023.3/2023.4 官方手册同款表述） | anysearch extract/search | 已核实 |
| calc-lambda-neighbors 默认 1、−1=全部状态（MBAR/AWH 需全矩阵） | A：GROMACS 2026.4 mdp 文档 + 官方 AWH-FEP mdp 示例（calc-lambda-neighbors = -1） | anysearch search/extract | 已核实 |
| gmx bar 自动相加各段 BAR、-nbmin/-nbmax 默认 5、-prec 默认 2、s_A/s_B 相对熵（Wu & Kofke 度量） | A：gmx bar 2026.4 官方页（原文含 "automatically adds…combined…"、5 blocks、Wu & Kofke 123 084109） | anysearch extract | 已核实 |
| gmx analyze -ac/-ee/-luzar；-temp 默认 298.15 K、-fitstart/-fitend 默认 1/60 ps | A：gmx analyze 2026.4 官方页（含 -[no]luzar 对 gmx hbond -ac 输出的 Luzar–Chandler 分析） | anysearch extract | 已核实 |
| NVT→NpT 的 pV 修正（手册式 131，22 bar/−1 kJ·mol⁻¹ 例）与动能质量项 −(3/2)k_BT·ln(m_B/m_A) | A：GROMACS 2026.4 参考手册 Free energy calculations 页 | anysearch extract | 已核实 |
| FEP Jensen 不等式、有限样本估计量系统偏高、log-space 求值 | 教科书方法学共识；正文以 [6]（Wu & Kofke，相空间重叠与偏差）为锚，未绑定单一出处声明 | 方法学共识（正文已注明依据类型） | 已核实 |
| MBAR 全矩阵约束：dhdl 只含邻态 ΔH；-1 重跑 / alchemical-analysis 组装 / pymbar 重构三条路；overlap 矩阵诊断；log-sum-exp | B：Klimovich 2015 [10]；A：pymbar 文档前提（样本近似独立） | 原始文献+官方文档 | 已核实 |
| 新增 12 条引文六项核验（Gilson[4]、Wu&Kofke[6]、Klimovich[10]、gmx analyze[12]、Pohorille[13]、Mey[14]、Kästner[17]、Genheden&Ryde[21]、Duan[22]、Tiwary&Parrinello[34]、Impey[37]、Laage&Hynes[39]） | B 级文献；gmx analyze 为 A 级 | anysearch Crossref/search/extract 逐条核验（标题/作者/期刊/年份/卷期页/DOI）；9 条沿用 peer-08 已核验结论，Wu&Kofke、Laage&Hynes 本轮补核 | 已核实 |
| WTM 收敛于 −(1−1/γ)F(s)+C（理想极限下原始形式逼近 −F(s)）；Tiwary–Parrinello 指数重加权 ⟨Oe^{βV}⟩/⟨e^{βV}⟩ | B：Bussi & Laio 2020 [33]；B：Tiwary & Parrinello 2013 [34]（PRL 111:230602，量纲与卷期页经 Crossref 更正核验） | 原始文献 | 已核实 |
| 引用编号 1-42 首现顺序严格递增、章末与 refs 42/42 逐字一致 | 自检 | 脚本实测（.history/08-verify-round.py） | 已核实（修订轮） |
| 汉字数 20,738 ≥10,000（STYLE 口径） | 自检 | 脚本实测 | 已核实 |
| 结构调整：8.2 新增「8.2.2 炼金术拓扑准备与耦合方案」，原 8.2.2–8.2.6 顺延为 8.2.3–8.2.7；8.6.4 原文引用错位 [17,26]（Amadei）更正为 [24,36]（手册+AWH 页） | 自检 | 全文 grep 复查 | 已核实 |
