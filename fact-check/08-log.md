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
