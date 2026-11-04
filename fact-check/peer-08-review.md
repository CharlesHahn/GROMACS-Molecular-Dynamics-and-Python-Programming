# 第 8 章「自由能、增强采样与高级分析」同行对抗性审查报告（peer review v2）

- 审查轮次：**同行对抗性审查（peer adversarial review）v2**
- 审查日期：**2026-11-04**
- 审查对象：`08-自由能、增强采样与高级分析.md`（624 行；约 1.65 万汉字，STYLE 口径；本轮未修改任何正文文件）
- 审查立场：**科研同行**（研究生高年级至 PI、具 MD 基础、需要可复现且方法学严谨的参考书），非入门学生
- 审查重点（Focus）：TI/FEP/BAR/MBAR/WHAM 的统计基础与数值陷阱（重叠、端点奇点、soft-core、dhdl 去相关）、伞形采样窗口设计、metadynamics/OPES 参数物理语义与收敛、PMF 误差来源、与 gmx bar/wham 及 pymbar/MBAR 的对位
- 依据文件：STYLE.md、REVIEW.md、正文全文、`refs/08-refs.md`、既有验收记录 `fact-check/08-review.md`（三轮，2026-10-30 最终 pass=true，引文/结构层已闭环）、`.history/exercises-20261103/08-自由能、增强采样与高级分析-习题原文.txt`（8 题）
- 核验通道说明：本会话**未调用 `web_search` 工具**；唯一网络通道为 **anysearch CLI**（`D:\CharlieAPP\C_Python\python.exe … anysearch_cli.py`），实际使用 `extract`×12、`search`×3。凡经该通道核验的条目均在本报告「〇」节登记并标注「anysearch 核验」；未在本机实测 2026.4 工具的条目一律注明「需目标机实测」。所有建议补引的前沿文献均已给出 Crossref 核验后的卷期页与 DOI，入库前仍须按 STYLE 四大件流程 extract 复核。
- 一句话结论：本章的结构、文献层（30 条逐字核验通过）与参数「四问」都达到了既有验收标准，8.2 的 soft-core、8.3 的 WHAM 选项、8.6 的 OPES/META 参数语义在事实层是全书最扎实的部分；**但作为「方法学最重的一章」，它距离「同行可据此设计并判断自己的自由能计算」尚有系统性缺口**——炼金术的根本实操层（拓扑构建与耦合方案）整节缺位、dhdl 的去相关与误差合并只有警告没有程序、MBAR 的全矩阵可行性约束被一句「组织成能量矩阵」带过、PMF 误差来源没有清单化、元动力学收敛与重加权缺现代工具对位。按本任务口径（同行深度），**pass=false**。

---

## 〇、核验通道记录（anysearch，逐条可复核）

| 核验项 | 通道 | 结果 | 对正文的影响 |
| --- | --- | --- | --- |
| `gmx bar` 2026.4 官方页 | anysearch extract（manual.gromacs.org 2026.4） | ① 输出表含 `lam_A/lam_B/DG/s_A/s_B/stdev`，**s_A/s_B 确为 gmx bar 输出**（相对熵，Wu & Kofke 2005 度量）——正文 8.2.2/L98、8.2.5/L122 表述正确；② 分块误差「splitting the data into blocks…assuming the blocks are independent…average variance over 5 blocks」，且 `-nbmin/-nbmax` 默认 5、`-prec` 默认 2、`-extp` 存在——正文警告句正确，但**可补充的选项层细节（‑nbmin/-nbmax 扫描、-prec）正文未给**；③ **gmx bar 会自动把各段 BAR 相加为组合自由能**（"automatically adds series of individual free energies…into a combined free energy estimate"）——正文只说「逐对输出」，未告知自动求和与逐对误差的合并方式；④ 输入文件须含 dH/dλ 列与 ΔH（foreign lambda）列，λ 由图例推断——印证 dhdl 列结构正文未解释 | D2、D3、优先级 2/3 |
| GROMACS 参考手册 Free energy calculations 页 | anysearch extract | 慢增长正反向一致不保证正确、delta_lambda=0 离散模式、MBAR 需外部 pymbar、ΔG₁−ΔG₂=ΔG₃−ΔG₄、dG/dλ 积分——与正文一致；该页还含 **NVT→NpT 的 pV 修正（式 131，22 bar/−1 kJ·mol⁻¹ 例）与质量项 −(3/2)k_BT·ln(m_B/m_A)**，正文 8.2 未提 | D1（标准态/系综修正层）、B 可提及 |
| `gmx analyze` 2026.4 官方页 | anysearch extract | **`-ac`（自相关函数，autocorr.xvg）与 `-ee`（分块误差）确实存在**；另发现 **`-luzar`：对 gmx hbond(-legacy) `-ac` 输出做 Luzar–Chandler 断裂/重形成速率分析**，`-temp` 默认 298.15 K、`-fitstart/-fitend` 默认 1/60 ps | D2（dhdl 去相关工具落点）、D8（8.7.2 氢键速率工具落点），推荐可安全引用 |
| `calc-lambda-neighbors` 语义 | anysearch search（GROMACS 论坛实例 + mdp 文档片段） | 实测示例 `calc_lambda_neighbors = -1` 用于 AWH/fep-lambdas；mdp 文档片段「It also requires calc-lambda-neighbors to be -1」；论坛展示 `couple-moltype/couple-lambda0=vdw-q/couple-lambda1=none/couple-intramol/fep-lambdas` 全套解耦 mdp——**确认 -1=全部 λ 态**，且 couple-* 属现行 mdp 选项（章节表 8-3 未收录） | D1、D3、优先级 1/2 |
| 建议补引① Pohorille/Jarzynski/Chipot | Crossref extract（10.1021/jp102971x） | "Good Practices in Free-Energy Calculations", J Phys Chem B, 2010, 114(32): 10235-10253；作者三人全对 | 广度「必须补」；8.1.3/8.2 对位 |
| 建议补引② Klimovich/Shirts/Mobley | Crossref extract（10.1007/s10822-015-9840-9） | "Guidelines for the analysis of free energy calculations", J Comput Aided Mol Des, 2015, 29(5): 397-411（即 alchemical-analysis.py 工具包论文） | 广度「必须补」；D3 管线落点 |
| 建议补引③ Mey et al. | Crossref extract（10.33011/livecoms.2.1.18378） | "Best Practices for Alchemical Free Energy Calculations [Article v1.0]", Living J Comput Mol Sci, 2020, 2(1): 18378；作者 Mey/Allen/…/Shirts/Tresadern/xu 全对 | 广度「必须补」；8.1.3/8.2 前沿对位 |
| 建议补引④ Kästner | Crossref extract（10.1002/wcms.66） | "Umbrella sampling", WIREs Comput Mol Sci, 2011, 1(6): 932-942；摘要确认含 umbrella integration（Kästner & Thiel, JCP 123, 144104, 2005） | 广度「必须补」（8.3 综述），可提及 UI |
| 建议补引⑤ Genheden & Ryde | Crossref extract（10.1517/17460441.2015.1032936） | "The MM/PBSA and MM/GBSA methods to estimate ligand-binding affinities", Expert Opin Drug Discov, 2015, 10(5): 449-461 | 广度「必须补」（8.4 综述） |
| 建议补引⑥ Duan/Liu/Zhang | Crossref extract（10.1021/jacs.6b02682） | "Interaction Entropy: A New Paradigm for Highly Efficient and Reliable Computation of Protein–Ligand Binding Free Energy", JACS, 2016, 138(17): 5722-5728 | 广度「可提及」（8.4.1 熵项现代化） |
| 建议补引⑦ Tiwary & Parrinello | **Crossref extract 纠错**：10.1103/PhysRevLett.114.050601 解析为 Polettini/Verley/Esposito "Efficiency Statistics at All Times"（非元动力学）；正确 DOI 为 10.1103/PhysRevLett.111.230602 = "From Metadynamics to Dynamics", Phys Rev Lett, **2013**, 111(23): 230602 | 广度「必须补」（8.6.2 重加权）；提醒：凭记忆写 DOI 有风险，入库前必 extract |
| 建议补引⑧ Impey/Madden/McDonald | anysearch search（OSTI 引用 + SklogWiki） | "Hydration and mobility of ions in solution", J Phys Chem, 1983, 87(25): 5071-5083，**DOI 10.1021/j150643a008**（非 10.1021/j100244a027，后者 Crossref 连接失败） | 广度「可提及」（8.7.1 驻留口径起源） |
| 建议补引⑨ Gilson/Given/Bush/McCammon | Crossref extract（10.1016/S0006-3495(97)78756-3） | "The statistical-thermodynamic basis for computation of binding affinities: a critical review", Biophys J, 1997, 72(3): 1047-1069 | 广度「必须补」（8.2 结合自由能标准态） |
| 建议补引⑩ Wu & Kofke | Crossref extract（10.1063/1.2011391） | "Phase-space overlap measures. II…", J Chem Phys, 2005, 123(8): 084109（gmx bar 文档所引条目） | 广度「可提及」（8.2.2 重叠度量的原始出处） |
| 既有验收结论 | 沿用 fact-check/08-review.md 三轮结论 | [2]/[3]、[10]/[11] 互换、[25] DOI、[26] URL、[27] 页码均已闭环；编号首现序 1-30 递增、章末与 refs 30/30 逐字一致 | 本轮不再重审引文层，仅从方法学角度评述正文内容 |

> 未检索项（据领域知识判断，未作新断言）：FEP 有限样本偏差方向（Jensen 不等式）、BAR 误差随重叠趋零发散、MBAR 的 log-sum-exp 数值稳定性、WHAM 空柱病态、势垒顶窗口双峰分布、OPES ε 语义——均为教科书级方法学结论，报告内已按「建议表述」处理，未绑定任何具体文献；引用前需与上表已核验文献或 [1][7][22] 对应。

---

## 一、深度缺口（depthGaps）

> 判定口径：关键主题是否只停留在「能跑/能用」层；缺哪些机理、边界、数值细节与前沿对位。行号以 `08-自由能、增强采样与高级分析.md` 为准（L=行号）。

### D1｜8.2 全节（L78–179）：炼金术的「设计并运行」缺拓扑准备层——学习目标（L9）落空，最高优先级

- 学习目标 L9 承诺「**能设计并运行多窗口炼金术自由能计算**」，但 8.2 节只讲了 λ 网格、soft-core 与 gmx bar 分析，**从未告诉读者炼金术拓扑怎么构造**：消失/出现的原子如何做成 dummy 原子（质量保留、电荷与 LJ 归零的 B 态参数）、单拓扑机制下消失原子的成键项如何处理、`couple-moltype`/`couple-lambda0`/`couple-lambda1`（如 `vdw-q`→`none`）与 `couple-intramol` 的解耦方案——这是按章节流程照做也跑不起来的缺口。
- 表 8-3（L168–179）收录了 8 个参数，但漏掉 `couple-moltype`、`couple-lambda0/1`、`couple-intramol`、`delta-lambda`（L86 正文提过但未入表）、`sc-sigma`（正文详述但未入表）。anysearch 核验确认这些均为现行 mdp 选项（论坛 AWH/解耦实测示例）。
- 标准态与系综结局未交代：炼金术「在溶剂中创造/湮灭一个分子」改变粒子数，绝对结合自由能需要标准态（浓度）换算与取向/位置约束处理；NVT 与 NpT 下结果对应 ΔA 与 ΔG，手册 [1] 甚至给出 pV 修正式与质量项。正文 8.1.1（L29）只对「实验比较」讲标准态，8.2 未对「炼金术自身」讲。
- **修改建议**：8.2.1 前新增 10–15 行的拓扑准备段（dummy 原子/B 态参数要点 + couple-* 解耦方案 + 一句标准态修正提示，引 Gilson 1997），表 8-3 增 3–4 行；并注明「绝对结合自由能的完整方案（Boresch 类约束）超出本章范围」作为边界声明。级别 P1：同行照本章无法落地一例炼金术计算。

### D2｜8.2.2（L96–98）与 8.2.6（L148–156）：FEP/BAR 的统计基础与 dhdl 去相关只有警告、没有程序

- **FEP 统计基础**：L96「重叠不足时估计值向某一方向系统偏移且方差巨大，延长采样难以修复」——方向与量级未给。建议补两个直接可用的结论：① Jensen 不等式：ΔF=−k_BT·ln⟨e^{−βΔU}⟩_A ≤ ⟨ΔU⟩_A（指数平均恒≤端点平均能量差）；② 有限样本估计量 ΔF̂=−k_BT·ln(均值) 因 ln 凹性**系统偏高**（高估 A→B 的自由能、低估 B 的稳定性），偏差由 ΔU 分布罕见尾控制、随样本量按 N_eff^{−1/2} 缓慢缩小——「延长采样难以修复」的准确含义是「收敛率受罕见尾支配，有效修复是插中间态改善重叠」。另补指数平均的数值稳定性：βΔU 超过 ~60 即溢出，须 log-space 求值（与 D3 的 MBAR log-sum-exp 同一主张）。
- **dhdl 去相关程序缺失**（Focus 明点「dhdl 去相关」）：正文已有两处正确警告（L98 gmx bar 假定样本独立、L241 gmx wham -ac 按 1/(1+2τ/dt) 加权），但**没有给出去相关操作步骤**：用 `gmx analyze -ac` 估 dH/dλ 自相关时间 τ（anysearch 核验 `-ac` 存在）→ 按 ≥τ 抽稀再喂 gmx bar/pymbar，或按第 9 章有效样本数框架折算 N_eff。同行照抄章节只会得到被低估的误差。
- **误差合并规则未写**：gmx bar 自动把各段 BAR 相加为组合 ΔG（anysearch 核验文档原文），但「逐窗口误差在窗口近似独立假设下平方和合并」这一句正文没有；`-prec`、`-nbmin/-nbmax`（默认 5 的分块数窗口，用于检查误差是否随块数稳定）也未提。
- **修改建议**：8.2.2 补 8–12 行统计基础段（Jensen + 偏差方向 + log-space）；8.2.6 末尾扩写「误差与去相关」：τ 估计→抽稀→合并规则→分块扫描，与第 9 章交叉引用。级别 P1。

### D3｜8.2.3（L100–108）：MBAR「组织成能量矩阵」一句带过了全部实操约束

- L108「把各窗口的 dhdl.xvg 按状态组织成能量矩阵，交由 pymbar 的 MBAR 类」——同行照做必踩的坑被省略：**dhdl.xvg 只含 dH/dλ 与本态到 calc-lambda-neighbors（默认 1）邻态的能量差，不包含到所有 λ 态的 U_i(x_jn)**；构建 MBAR 所需的全能量矩阵要么把 `calc-lambda-neighbors` 设为 -1（anysearch 核验：-1=全部 λ 态）重跑/重估，要么用 alchemical-analysis 工具包（Klimovich/Shirts/Mobley 2015）从 dhdl 目录自动组装。这是「MBAR 的适用条件与外部实现」（学习目标 L9）的真正内容，正文只字未提。
- 缺数值细节：pymbar 的**重叠矩阵（overlap matrix）**及其特征值诊断（比 s_A/s_B 更完整的全状态诊断）；MBAR 自洽方程直接求值会因 exp(大数) 溢出，须 log-sum-exp 形式（同行用 Python 复现 L104 公式必然遇到）；协方差矩阵的解读正文已有半句，可保留。
- **修改建议**：8.2.3 扩成 12–18 行：① dhdl 邻态约束与 -1 语义；② alchemical-analysis/Klimovich 2015 管线；③ overlap 矩阵诊断；④ log-sum-exp 稳定性；⑤ 与第 9 章 N_eff 折算的操作衔接。级别 P1。

### D4｜8.3（L181–243）：PMF 误差来源未清单化，窗口设计有公式无数值判据

- **PMF 误差来源清单**（Focus 明点）：正文散见各处的误差来源（统计/去相关 L241、柱宽 L232、边界外推 L243、RC 不完备 L187、模型层 L50），但从未汇总成一张同行可直接对照的清单。建议在 8.3.3 末尾加 6–8 行显式枚举：① 窗口采样误差（时长、自相关、平衡段剔除）；② 直方图离散化（WHAM 柱宽与**空柱病态**——自洽方程在空柱处无定义，需保证 bins 覆盖范围内每柱有样本）；③ 估计器差异（WHAM vs MBAR 在重叠边缘的稳健性差异，L243 已有一句可展开）；④ 反应坐标不完备（正交慢自由度→PMF 是条件平均、带隐藏偏差）；⑤ 模型层（力场/截断/隐式）。每一类注明「延长采样能否修复」。
- **窗口设计缺数值判据**：L195 已给出 σ≈√(k_B T/k)，但缺一个可执行数值示例——k=1000 kJ·mol⁻¹·nm⁻²、T=300 K 时 σ≈0.05 nm，窗口间距 0.1 nm 即约 2σ（边缘重叠），给出「间距 ≤ 2σ 且相邻直方图连通」的判据比「经验上同量级」更可操作；同时注明窗口越窄每窗统计越差，需在 k 与间距间折中。
- **势垒顶窗口的机理未讲**：L209「势垒与势阱区域应加密」给结论不给理由——势垒顶窗口内 ξ 分布是双峰的（两侧盆地各占一部分），单峰高斯近似失效，需要更长平衡、更细 dhdl/历史输出与更保守的去相关。建议补 2–3 句。
- **修改建议**：8.3.3 末尾加「PMF 误差来源清单」段（6–8 行）+ 8.3.2 补数值例与势垒顶双峰说明。级别 P1。

### D5｜8.6.2（L419–456）：元动力学的收敛表述自相矛盾，重加权只有半句

- **表述矛盾**：L423 先写「当偏置填满盆地后……**最终 V(s) 收敛于 −F(s)**」，紧接着写「**原始形式不收敛于有限偏置**」——同一段两句话互斥。准确表述：理想极限（沉积速率→0）下 V≈−F；有限沉积的原始 metadynamics 偏置持续波动增长、无收敛极限；WTM 才收敛于 (1−1/γ)F(s)。这是方法学核心陈述，必须修正（同时见「三、教学腔」第 3 条）。
- **收敛判据缺参数化语义**：L450 三条判据（高度衰减近零/前后半程 FES 差 ≤ k_BT/偏置平台）正确，但缺「沉积速率必须远慢于 CV 弛豫速率」这一 PACE/HEIGHT 组合的物理约束（L427 只写「维持偏置增量小于 k_BT 的若干倍」——这是必要条件而非充分条件）；收敛到某一时刻后仍需块分析估计 FES 误差，正文未给 HILLS 重构的误差估计方法。
- **重加权缺现代工具**：L456「也可从 COLVAR 出发对偏置做指数重加权」——无公式、无出处、无适用条件，同行无法落地。建议补 Tiwary & Parrinello 重加权（PRL 2013, 111(23): 230602，from metadynamics to dynamics：权重 ∝ e^{βV(s,t)} 恢复无偏平均，前提是偏置已近准静态/收敛），并把「WTM 轨迹可同时给出 FES 与无偏平均/动力学信息」作为 8.6.4 选型表「收敛行为」列的补充注记。
- **修改建议**：L423 改写（见上）；8.6.2 末尾补 6–10 行「重加权与误差估计」段（Tiwary–Parrinello + 块分析 + 与 OPES neff 对照）。级别 P1。

### D6｜8.7.1（L510–536）与 8.7.2（L538–550）：动力学指标的统计口径有混用、工具链缺件

- **生存函数与两种口径的对应未写清**：L510 定义 S(t)=⟨h(0)h(t)⟩/⟨h⟩ 并说「平均寿命由……指数拟合给出」——但该式是**间歇口径**的相关函数（允许断后重连）；**连续口径**的平均寿命应来自连续占据段长度的生存/风险分析（指数拟合对象不同、τ 数值不同）。正文两口径讲完后用一个式子统收，同行会得到错误的拟合目标。建议明确：连续 → 段长分布（Python 例 L516–533 的 segs 即是），间歇 → 相关函数拟合，两者不可混用。
- **缺口径起源与工具**：8.7.1 应补 Impey/Madden/McDonald 1983（J Phys Chem 87: 5071–5083，DOI 10.1021/j150643a008）作为连续/间歇驻留口径的经典出处（仅一句即可）；8.7.2 已荐 hbond-legacy `-life/-ac`，但 **`gmx analyze -luzar`**（anysearch 核验存在：对 hbond(-legacy) `-ac` 输出做 Luzar–Chandler 断裂/重形成速率分析，`-temp` 298.15 K 默认）未提及——它正好是 L550「双指数拟合分辨组分」与 [27] 的工程化工具。另建议把 Luzar–Chandler 四速率（断裂 k₁、重形成 k₋₁、交换 k_f、扩散 k_d）用 2–3 句点出（与第 7 章 7.4.3 的口径问题互为印证，见 peer-07-review D1）。
- 级别 P1（口径混用）＋P2（工具与文献补强）。

### D7｜8.4（L245–282）：MM-PBSA 的现代实践对位不足

- 正文对近似层次、能项分解与解读边界的论述相当扎实，缺的是**数值敏感度与现代化工具**：① 内介电常数 ε_in（1 vs 2–4）与 PB 半径集（如 mbondi2 类）可改变 ΔG_bind 达数十 kJ·mol⁻¹，正文表 8-5 只提「内介电常数」「探针半径」未给敏感度量级；② −TΔS 的正则模分析噪声大（正文已说），但 2020 年代标配的**相互作用熵（interaction entropy, Duan/Liu/Zhang 2016, JACS 138: 5722–5728）**未提及，同行无法据此现代化自己的熵项处理；③ 缺 Genheden & Ryde 2015 综述对位（误差三层与力场敏感性的一站式出处）。
- 级别 P2（改起来小、收益明确）。

### D8｜8.1.3（L46–50）与各估计器：统计/模型误差二分法正确，但「统计误差怎么来」缺一个统一接线

- L48「gmx bar 的分块方差、gmx wham 的自助法区间与 pymbar 的协方差矩阵」是对的，但**没有告诉读者三者给出的分别是什么口径的误差**（分块=相关样本校正的方差、bootstrap=对柱直方图重采样的经验区间、协方差=多状态联合正态近似），以及「误差要与什么比」（与 ΔG 本身、与 ΔΔG 差值的误差传播）。建议在 8.1.3 加一句「三种估计器误差口径对照」，把第 9 章的误差传播概念显式接上。
- 级别 P2。

---

## 二、广度缺口（breadthGaps）

> 判定口径：同行期望但未覆盖的主题/方法/工具/文献。区分「必须补」与「可提及」。

### 必须补（方法学主线，缺了构成硬伤）

1. **炼金术 good-practices 文献对位**：Pohorille/Jarzynski/Chipot 2010（J Phys Chem B 114: 10235–10253，DOI 10.1021/jp102971x）与 Mey et al. 2020（LiveCoMS 2(1): 18378，DOI 10.33011/livecoms.2.1.18378）应作为 8.1.3/8.2 的「去读这份清单」指针——这是同行判断自己方案是否合规的现成标准，全是 A/B 级之外最高引用的 best-practice 文献。落点：8.1.3 或 8.2.6 末尾。
2. **alchemical-analysis 工具链**：Klimovich/Shirts/Mobley 2015（JCAMD 29: 397–411，DOI 10.1007/s10822-015-9840-9）——从 GROMACS dhdl 目录自动组装 MBAR/BAR 输入的准标准工具，8.2.3 不写它，MBAR 一节就悬空（并入 D3）。
3. **伞形采样综述对位**：Kästner 2011（WIREs Comput Mol Sci 1: 932–942，DOI 10.1002/wcms.66）——8.3 的窗口设计、WHAM/UI 对比与实验引导协议的一站式出处；同行判断伞形方案优劣必读。落点：8.3.2 或 8.3.3。
4. **MM-PBSA 综述对位**：Genheden & Ryde 2015（Expert Opin Drug Discov 10: 449–461，DOI 10.1517/17460441.2015.1032936）——8.4 的误差三层、近似适用性与应用统计的一站式出处。
5. **结合自由能标准态基础**：Gilson/Given/Bush/McCammon 1997（Biophys J 72: 1047–1069，DOI 10.1016/S0006-3495(97)78756-3）——8.2「绝对结合自由能 + 标准态修正」的根文献，配合 D1。
6. **元动力学重加权**：Tiwary & Parrinello 2013（PRL 111(23): 230602，DOI 10.1103/PhysRevLett.111.230602）——并入 D5。

### 可提及（补一句指针即足够，不必展开）

1. **副本交换的方法学面**：8.6 导言（L389）与 8.6.4（L502）只提「GROMACS 内置实现」，同行会追问温度梯设计、交换接受率、REST（溶质升温）变体——建议 8.6.4 选型段加 2 句（REST/温度梯度与交换频率的实践要点，并声明本章不展开）。
2. **funnel metadynamics 与 Boresch 约束类绝对结合方案**：8.2 结合自由能语境一句指针（绝对结合自由能的取向-位置约束方案），明确「超出本章范围」即可（避免与方法主线混淆）。
3. **umbrella integration（UI）**：Kästner & Thiel 2005（JCP 123: 144104）——伞形数据的另一条重加权路线（用每窗平均力而非直方图），8.3.3「WHAM vs MBAR」对比处一句「另有平均力路线 UI」即可。*注意：引用前须 extract 复核（本书 refs 尚无此文）。*
4. **交互熵（interaction entropy）**：Duan 2016（已核验）——8.4.1 熵项行内一句（「也可用 interaction entropy 估计 −TΔS」）。
5. **驻留口径起源与跳跃机制**：Impey 1983（8.7.1 一句）＋Laage–Hynes 跳跃模型（跨第 7 章口径，8.7.1/8.7.2 一句指针）。
6. **非平衡功重加权**：8.7.3（L556）已有 Jarzynski [29]；补一句「快增长功亦可用 Bennett–Crooks 形式的接受比处理（gmx bar 的 -extp/-g 工作流可复用）」作为工程提示，免去读者另寻。
7. **AWH 收敛判据细节**：8.6.4（L487）可补一句「awh1-error-init 与 awh-error 输出用于收敛监测（需目标机实测确认选项名）」，并注明对比 ABF 的「均匀误差」特性。

### 明确不补（范围声明即可）

- REMD 的方法学展开（8.6 已声明聚焦 PLUMED 偏置类）；string method/路径系综（8.7.3 已有「二维增强或路径系综补充」一句）；量子/混合方法。均属合理裁剪，无需动作。

---

## 三、教学腔残留（pedagogyResidue）

> 判定口径：面向学生的表述残留、过度包办解释、教学式简化。给行/句。

1. **L423「当偏置填满盆地后，体系被推向未访问区域，最终 V(s) 收敛于 −F(s)」**——教学式理想化，且与同段后句「原始形式不收敛于有限偏置」直接矛盾（见 D5）。属「简化过头改坏了正确性」的典型。
2. **L294「常见的定性描述是前 5—10 个 PC 超过总方差的八成，数值须按实际轨迹统计，不宜照搬」**——无出处的教科书 folklore，且「八成」这类数字恰是同行最忌讳的无锚定量（既有验收已记 P2）。建议删除百分比，改为「方差占比须随分析原子组（Cα  vs 全原子）一同报告，跨组不可比」，把不可比性讲成规范而非给个经验值。
3. **L464「先粗后细」与「持续填坑」、L588 小结「以沉积高斯填充盆地」**——「填坑」口语化，「先粗后细」是 OPES 原文的图像化（可保留但书面化：「先探索性采样、随分布估计收敛趋于目标分布」）。建议全书统一为「填充自由能盆地」。
4. **L464「参数更少」**——不严谨的简化：OPES 参数数量并不少于 WTM（PACE/SIGMA/TEMP/BIASFACTOR/BARRIER），真正的区别是删掉了 HEIGHT 这类人为幅度参数、改由 BARRIER 隐式决定。建议改述，避免误导选型判断。
5. **L48「判定两类误差的简单实验是更换随机种子与窗口设置」**——「简单实验」教程化；改为「可操作的判据是：更换随机种子与窗口配置观察估计值波动（统计层），更换力场观察超出统计误差的差异（模型层）」，把「实验」升格为「判别协议」。
6. **L195「其余自由度不受影响」**——伞形偏置「仅沿 ξ 方向作用」的说法对，但「不受影响」易误解为其余自由度分布不变；改为「偏置只直接修改 ξ 方向的统计权重；其余自由度的分布经体系内耦合被间接改变」。
7. **L33「所需采样成本随势垒高度指数增长」**——正确但未限定机制；加括注「（Arrhenius/Kramers 意义：跨越率 ∝ exp(−ΔF‡/k_BT)）」即严谨。
8. **L86 慢增长一段、L122 窗口划分、L429 HEIGHT 四问**——表述合规，无动作。

---

## 四、习题内容转化（exerciseConversion）

> 背景：`.history/exercises-20261103/08-…-习题原文.txt` 存有 8 题（2026-11-03 移除，正文现无「## 习题」节）。结合 STYLE 二.8（≥6 题含 2 开放题）与 REVIEW 一.5，**习题节缺失本身是结构偏离**，须由编者决策：恢复习题或申请 STYLE 豁免并登记。以下按「回填正文 vs 恢复为习题 vs 去」给出甄别。

| 原题 | 内容 | 甄别与落点 |
| --- | --- | --- |
| 题1 | PCA 管线 + 前五 PC 方差占比 + Cα vs 全原子比较 | **大部分已覆盖**（8.5.1 全流程与命令、内存警告）；唯一可回填的新信息是「分析原子组对特征值谱/方差占比的影响」→ 8.5.1 末尾 1–2 句方法学注记（并入教学腔第 2 条改写）。其余**去**。 |
| 题2 | gmx cluster cutoff 扫描（0.10–0.25 nm）比较簇数 | **已内化**（8.5.3：-dist 看分布、扫 cutoff、-sz 看簇大小、按 RMSD 局部极小定 cutoff）。**去**（无新信息）。 |
| 题3 | WTM 重构 FES vs 无偏 2D 直方图 −k_BT·ln p，指出偏差来源 | **高价值，回填**：转为 8.6.2 收敛段的「验证案例解剖」——FES 重构与无偏直方图的差异来源（沉积未收敛、σ 过宽抹平细节、盆地边缘外推、绝对参考点位移）与「两者一致到什么程度才算可信」的判据。落点：L450 三判据之后 6–8 行。 |
| 题4 | hbond 连续 vs 间歇寿命 + 帧间隔影响 | **已覆盖**（8.7.2：两口径、-life/-ac、拟合区间、帧间隔 1/10）。**去**（并入 D6 的 Luzar–Chandler 工具补强）。 |
| 题5 | PCA 为何线性、环翻转特征、何时弃用 PCA | **已覆盖**（8.5.1 L336 弯曲轨迹/余弦诊断；8.5.4 特征化替代）。**去**。 |
| 题6 | OPES 实验设计：CV 依据、BARRIER 估计、参数策略、收敛判据、与 WTM 对照、算力估算 | **最高价值，回填**：8.6.3 目前只有参数四问、无「方案模板」。转为 8.6.3 末尾 10–15 行的「OPES 实验设计清单」（方法学评注）：CV 选取依据→BARRIER 估计（短无偏模拟/文献同体系值/试探性 WTM）→PACE/TEMP/SIGMA 初始值与自适应→收敛判据（neff 平台 + 前后半程 FES + rct）→与 WTM 的对照设计（同 CV 同体系，比较 FES 差与到达准静态的耗时）→算力核算（沿用第 6/10 章）。 |
| 题7 | US vs WTM 选型、何时二维 CV/REM | **回填强化**：8.6.4（L491）现有并列式选型段，转为「选型三问」评注：① RC 已知且近似准静态？→US（统计效率高）；② 是否存在未知/正交慢自由度？→MetaD/OPES，需高维或 REM 时声明维度灾难（L502 已有）；③ 是否还要动力学/驻留？→需重加权（D5）或跳伞。落点：8.6.4 末尾。 |
| 题8 | MSM 平台为何是马尔可夫证据；状态数不足/转移过少各如何表现 | **高价值，回填**：8.5.4（L368–370）只给「未通过→回退」没给机理。转为 6–10 行方法学评注：马尔可夫性 ⇒ 隐含时间尺度 t_i(τ)=−τ/ln λ_i(τ) 与 τ 无关（谱自洽）；离散化过粗/特征不足 → 平台缺失；转移过少 → λ_i 估计噪声大、平台被噪声掩盖、CK 检验被 χ² 拒绝——每条一句对应 [18] 的位置。落点：L370 验证两段之后。 |

**关于是否恢复「## 习题」节**：若坚持 STYLE 刚性结构，建议恢复 3 题即可达标（题目从原 8 题择优：题 6 开放设计 + 题 8 概念 + 题 3 对照实验，正好 1 计算 + 1 思考 + 1 开放，开放题不足 2 时可把题 7 选型讨论设为第二开放题）；其余 5 题内容按上表回填正文，避免「为凑题数而堆题」。若编者有意去掉习题节（本版已移除），须在 PROGRESS.md/OUTLINE.md 登记 STYLE 豁免，避免后续验收按二.8 判不合格。

---

## 五、priorityActions（按优先级，5–8 项）

1. **【P1】8.2 补「炼金术拓扑准备与解耦方案」实操层**（D1）：dummy 原子/B 态参数、`couple-moltype`/`couple-lambda0/1`/`couple-intramol`、标准态与 NpT/NVT 结局修正（引 Gilson 1997）；表 8-3 增 `couple-*`/`delta-lambda`/`sc-sigma` 行。否则学习目标 L9「能设计并运行」不成立。
2. **【P1】8.2.2/8.2.6 补「dhdl 去相关与误差合并」统计协议**（D2）：gmx analyze -ac 估 τ → 抽稀 → BAR/MBAR；gmx bar 自动求和与逐窗口误差平方和合并规则；-nbmin/-nbmax（默认 5）与 -prec；FEP 有限样本偏差方向（Jensen）与 log-space 求值。
3. **【P1】8.2.3 补 MBAR 全矩阵可行性**（D3）：calc-lambda-neighbors 默认 1/-1=全部 的约束、alchemical-analysis 工具链（Klimovich 2015）、overlap 矩阵诊断、log-sum-exp 稳定性。
4. **【P1】8.3 补「PMF 误差来源清单」+ 窗口设计数值判据**（D4）：六类误差枚举（注明能否靠延长采样修复）、σ=√(k_BT/k) 数值例与间距 ≤ 2σ 判据、势垒顶双峰与空柱病态。
5. **【P1】8.6.2 修正 V(s)→−F(s) 表述并补收敛与重加权**（D5）：理想极限 vs 有限沉积的准确表述、沉积速率 ≪ 弛豫速率的参数判据、Tiwary–Parrinello 重加权（2013 PRL）与 HILLS 误差估计。
6. **【P1】结构合规决策**：恢复 ≥3 题（题 6/8/3，另设题 7 为开放题）或登记 STYLE 豁免；按「四、」的回填表将题 3/6/7/8 内容写入正文。
7. **【P2】文献对位增补**（全部经 anysearch Crossref 核验，入库前按 STYLE 四大件复核）：8.1.3/8.2 → Pohorille 2010、Mey 2020；8.2.3 → Klimovich 2015；8.3 → Kästner 2011；8.4 → Genheden & Ryde 2015（＋Duan 2016 一句）；8.7.1 → Impey 1983；8.2 → Gilson 1997；8.7.2 → gmx analyze -luzar 工具句（含 Luzar–Chandler 四速率 2–3 句）。
8. **【P2】语言与简化收紧**（教学腔 1–7）：L423 收敛表述、L294 无出处「八成」、L464「参数更少/填坑/先粗后细」、L48「简单实验」、L195「其余自由度不受影响」、L33 指数增长加括注；8.7.1 S(t) 与两口径对应（D6）一并修订。

---

## 六、overall（总体评估）

本章在结构、文献层（30 条逐字核验、编号首现序 1–30、既有验收三轮闭环）与参数「四问」纪律上达到甚至超过全书水准，soft-core（8.2.4）、WHAM 选项语义（8.3.3）、OPES/METAD 参数物理含义（8.6.2–8.6.3）是事实性最扎实的部分，s_A/s_B 相对熵、-ac 自相关加权、边界外推警告等细节显示作者对 GROMACS 文档的把握是真实的。但作为全书方法学最重的一章，距离「同行可据此设计并判断自己的自由能计算」的目标仍有四个系统性缺口：炼金术的拓扑准备与耦合方案整节缺位（学习目标落空）、dhdl 去相关与误差合并只有警告没有程序、MBAR 的能量矩阵约束与工具链被一句带过、PMF 误差来源未清单化且元动力学收敛表述自相矛盾、重加权缺现代文献对位。这些缺口不涉及文献伪造或事实错误（引文层已验收通过），而是「同行落地」层面的深度欠账，与已移除的 8 道习题中的题 3/6/7/8 高度重合——把习题内容以「方法学评注/案例解剖/设计清单」形式回填正文是一次性解决深度与结构双重问题的低风险路径。建议按 priorityActions 1–6 修订后复验。

---

*报告完。本轮未修改任何正文文件；所有前沿文献 DOI/卷期页经 anysearch Crossref 核验（见〇表）；未调用 web_search。*