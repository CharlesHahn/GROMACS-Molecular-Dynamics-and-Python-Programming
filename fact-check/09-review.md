# 章节验收报告：第 8、9 章

- 验收范围：第 9 章（首次验收）；第 8 章（合并后首次验收，加查合并完整性）。
- 验收依据：REVIEW.md（未放宽）、STYLE.md、OUTLINE.md、09 章正文、08 章正文、refs/09-refs.md、fact-check/09-log.md。
- 验收日期：2026-10-29。验收人：对抗性验收代理（首次验收）。
- 通道说明：B 级文献六项以 Crossref REST（api.crossref.org，filter=doi，经 web_fetch）核验「题名、作者、期刊、年份、卷期页、DOI」；A 级条目以 web_fetch 直接抓取 manual.gromacs.org 2026.4 在线版原文；另以 anysearch CLI 补核个别条目。Efron 1979 的 Crossref 端点两次返回 content-type 异常，改由 Project Euclid 官方页（Ann. Statist. 7(1):1-26, 1979, DOI 10.1214/aos/1176344552）确认。

---

## 一、实测数字表（09 章，STYLE 三节口径）

| 项目 | 实测值 | 标准 | 结论 |
| --- | --- | --- | --- |
| 汉字数（除代码块、含表图注，截去「## 参考文献」之后） | 12,214 | ≥10,000 | 通过 |
| 二级节（##） | 13 | ≥8 | 通过 |
| 三级节（###） | 27 | ≥25 | 通过 |
| 表格 | 表 9-1、9-2、9-3、9-4 共 4 张 | ≥3 | 通过 |
| 图 | 图 9-1、9-2、9-3，均 Mermaid，共 3 幅 | ≥2 | 通过 |
| 常见错误 | 8 条（每条含现象→成因→排查→处置） | ≥6 | 通过 |
| 习题 | 7 题（5、6 为开放题） | ≥6，含 2 开放 | 通过 |
| 参考文献 | 33 条 | ≥30 | 通过 |
| 正文上标 | 1–33 按首次出现顺序、无跳号、无重号、与文末一一对应 | 严格对应 | 通过 |
| 导言 | 487 汉字 | 300–600 | 通过 |
| 学习目标 | 6 条，行为动词（能解释/能为/能独立实现/能运用/能区分/能为） | 4–6 条 | 通过 |
| 禁用表达 | 0（逐词扫描 15 个禁用词） | 0 | 通过 |
| 第二人称「你」 | 0（剔代码块） | 0 | 通过 |
| 占位符残留 | 0（待补/TODO/TBD/占位/待绘制/FIXME 等） | 0 | 通过 |
| 跨章重复 | 无段落级重复（仅 2 处 ≤16 字代码惯用语/前置知识措辞重合） | 无重复段落 | 通过 |

实测命令（汉字数）：

```powershell
$t = Get-Content -LiteralPath $f -Raw -Encoding UTF8
$t = [regex]::Replace($t, '(?s)```.*?```', '')
if ($t -match '(?s)## 参考文献.*$') { $t = $t.Substring(0, $t.IndexOf('## 参考文献')) }
$n = ([regex]::Matches($t, '[\u4e00-\u9fff]')).Count  # 12214
```

## 二、抽查文献清单与核验结果（09 章，随机 10 条）

随机编号（固定种子 20261029，升序）：**1, 15, 16, 17, 24, 25, 26, 29, 30, 31**。

| 编号 | 条目 | 六项核验（题名/作者/期刊/年份/卷期页/DOI） | 通道 | 结果 |
| --- | --- | --- | --- | --- |
| [1] | Abraham 2015, SoftwareX, 1-2:19-25 | 全部命中：题名、作者（Abraham/Murtola/Schulz/Páll/Smith/Hess/Lindahl）、SoftwareX、2015、卷 1-2、页 19-25 | Crossref | 通过 |
| [15] | Efron 1979, Ann. Statist. 7(1):1-26 | 全部命中（Crossref 端点 content-type 异常两次，改由 Project Euclid 官方页 + INSPIRE 记录确认：7(1):1-26, 1979, DOI 10.1214/aos/1176344552） | anysearch/Project Euclid | 通过 |
| [16] | Kirkwood 1935, JCP 3(5):300-313 | 全部命中（Statistical Mechanics of Fluid Mixtures; J. Chem. Phys.; 1935; 3(5):300-313） | Crossref | 通过 |
| [17] | Zwanzig 1954, JCP 22(8):1420-1426 | 全部命中（High-Temperature Equation of State…I. Nonpolar Gases; 22(8):1420-1426） | Crossref | 通过 |
| [24] | GROMACS 2026.4 User guide: Useful mdrun features | URL 可解析；内容核验：-reprod 同输入同硬件逐位一致、换硬件/编译器不保证、-multidir、-replex/-reseed 均与正文[24]引用一致 | web_fetch 官方页 | 通过 |
| [25] | Amadei 1993, Proteins 17(4):412-425 | 全部命中（Essential dynamics of proteins; Proteins: Structure, Function, and Bioinformatics; 1993; 17(4):412-425） | Crossref | 通过 |
| [26] | Kumar 1992, JCC 13(8):1011-1021 | 全部命中（THE weighted histogram analysis method…; J. Comput. Chem.; 1992; 13(8):1011-1021） | Crossref | 通过 |
| [29] | Kollman 2000, Acc. Chem. Res. 33(12):889-897 | 全部命中（Calculating Structures and Free Energies…; Acc. Chem. Res.; 2000; 33(12):889-897） | Crossref | 通过 |
| [30] | GROMACS 2026.4 User guide: Managing long simulations | URL 可解析；「Are continuations exact?」一节确认：同代码/编译器/架构/进程数且不用 GPU 时续算二进制精确，否则合法但不逐位一致；与正文[30]表述一致 | web_fetch 官方页 | 通过 |
| [31] | Sandve 2013, PLoS Comput. Biol. 9(10):e1003285 | 全部命中（Ten Simple Rules for Reproducible Computational Research; 9(10):e1003285） | Crossref | 通过 |

附加核验（非抽样，属关键论断涉及）：Chodera 2016（JCTC 12(4):1799-1805，Crossref ✓）、Straatsma 1986（Mol. Phys. 57(1):89-95，Crossref ✓）、Quenouille 1956（Biometrika 43(3/4):353-360，Crossref ✓）、Lyman & Zuckerman 2006（Biophys. J. 91(1):164-172，Crossref ✓，DOI 10.1529/biophysj.106.082941 与日志纠错一致）、Torrie & Valleau 1977（JCP 23(2):187-199，Crossref ✓）、Laio & Parrinello 2002（PNAS 99(20):12562-12566，Crossref ✓）。抽样 10/10 全部通过，未发现伪造、错配或无法打开条目。

## 三、关键论断抽查（逐条对照原始文献或官方文档）

### 09 章

1. **自相关/有效样本数公式**：c_A(τ)=⟨δA(t)δA(t+τ)⟩/⟨(δA)²⟩；τ_int=∫c_A dτ；Var(⟨A⟩)=(2τ_int/T)Var(A)；s=1+2τ_int；N_eff=N/s；σ_⟨A⟩=σ_A/√N_eff——与 Straatsma/Berendsen/Stam 1986（[9]）及 Frenkel & Smit（[5]，C 级教材）口径一致。**通过**。
2. **块平均**：σ²≈(1/(M(M−1)))Σ(Bᵢ−⟨B⟩)² 及「误差—块长曲线平台」判据——与 Flyvbjerg & Petersen 1989（[11]）一致，且与 gmx analyze -ee 官方公式 error²=Σ(Bᵢ−⟨B⟩)²/(m(m−1)) 逐字相符。**通过**。
3. **gmx analyze 选项语义**：web_fetch 2026.4 gmx-analyze.html 原文：-ac 为自相关；「Be sure that the time interval between data points is much shorter than the time scale of the autocorrelation」；-subav 默认 yes；-acflen 默认 half the number of frames；-ee 块平均误差 + 双指数解析拟合，且「complete derivation is given in B. Hess, J. Chem. Phys. 116:209-217, 2002」——与正文[2][12]表述及 09-log 声称一致。**通过**。
4. **gmx energy**：官方原文「An error estimate of the average is given based on a block averages over 5 blocks using the full-precision averages」；-nbmin/-nbmax 默认 5/5；「energy files contains averages over all MD steps … more accurate than the .xvg output」——与正文[13]（默认 5 块、全精度平均、xvg 重算损失精度）一致。**通过**。
5. **gmx trjconv -dt**：工具存在且 -dt 为帧抽取选项（官方 gmx-trjconv.html）。**通过**。
6. **收敛判据**：Chodera 2016 平衡段截断（最大化保留段有效样本数）——Crossref 六项核验通过（[22]）；前后半段子空间重叠 + 余弦含量——GROMACS 2026.4 手册 Covariance analysis 一节原文核实（「calculate the overlap of the sampling between the first and second half of the simulation. Note that this can only be done when the same reference structure is used」「when the cosine content … close to 1 … random diffusion」），与正文[21]一致。**通过**。
7. **可复现性**：gen-vel 默认 no、gen-seed 默认 −1——mdp-options（GitHub 源 / 官方页）核实；-reprod 语义、-multidir、副本交换——mdrun-features 原文核实；续算二进制精确的条件——managing-simulations「Are continuations exact?」原文核实；三项均与正文[24][30][32]一致。**通过**。
8. **自助法/刀切法出处**：Quenouille 1956（[14]）、Efron 1979（[15]）六项核验通过，正文对「块自助不适用独立样本」「重抽样前数据清洗」等表述与最佳实践文献[3]口径一致。**通过**。
9. **误差传播**：σ²_f≈(∂f/∂A)²σ²_A+(∂f/∂B)²σ²_B 及协方差矩阵形式 gᵀΣg——标准表达，正文标注教材共识，与[3]一致。**通过**。
10. **与实验比较/模型误差分离**：27 号文献框架（van Gunsteren & Mark 1998[28]）、29 号（Kollman MM-PBSA[29]）六项核验通过；正文将归纳性表述标注为教材共识/文献[3][28]，未将综述结论冒充原始结论。**通过**。

### 08 章（含公式、soft-core、工具用法、增强采样参数语义、PLUMED 集成）

1. **TI**：dA/dλ=⟨∂H/∂λ⟩_λ；ΔA=∫₀¹⟨∂H/∂λ⟩dλ——与 GROMACS 手册 Free energy calculations eq. (128)-(130) 一致；出处 Kirkwood 1935[2]，Crossref ✓。**通过**。
2. **FEP**：ΔF=−k_BT ln⟨exp(−βΔU)⟩_A——标准 Zwanzig 形式[4]，Crossref ✓。**通过**。
3. **BAR**：ΔF=C+k_BT ln(n_A/n_B)，C 由前/后向样本平衡条件确定——Bennett 1976 标准结果[5]，Crossref ✓。**通过**。
4. **MBAR**：自洽无偏方程形式与 Shirts & Chodera 2008（[7]）一致；「GROMACS 不内建 MBAR，需外部 pymbar」与手册 Free energy calculations 原文一致。**通过**。
5. **soft-core**：web_fetch 手册 Free energy interactions 原文 eq. (265)：V_sc=(1−λ)V^A(r_A)+λV^B(r_B)，r_A=(ασ_A⁶λ^p+r⁶)^{1/6}、r_B=(ασ_B⁶(1−λ)^p+r⁶)^{1/6}——与正文公式逐项一致；σ=(C12/C6)^{1/6} 或 sc-sigma；「原 GROMOS 用 p=2，p=1 更平滑」；「sc-coul=no 时静电线性关闭」、「sc-alpha=0 关闭软核」、「仅 A 或 B 态相互作用为零时启用软核」——全部与手册原文一致（[1][8]）。**通过**。
6. **gmx bar 用法**：-f 接受多个 dhdl.xvg、-oi/-oh/-temp、块误差默认 5 块（-nbmin/-nbmax）、「合并不同采样间隔数据时假定样本独立（对相关样本不成立，误差可能低估）」——与官方 gmx bar 说明逐条一致（正文[6]）。**通过**。
7. **gmx wham 用法**：-it/-ix 对应顺序、-bins 默认 200、-b 默认 50 ps、-cycl/-sym、-ac 按 1/(1+2τ/dt) 加权、-nBootstrap/-bs-method 默认 b-hist、-unit kJ——与官方 gmx wham 页全部一致（正文[11]）。**通过**。
8. **metadynamics/OPES 参数语义**：WTM 高度按 exp(−V/ΔT) 衰减、ΔT=(γ−1)T、偏置收敛到 (1−1/γ)F(s)——标准结果（[21][22]）；OPES_METAD 公式 V_n(s)=(1−1/γ)(1/β)log(P_n(s)/Z_n+ε) 与 PLUMED 2.9 OPES_METAD 文档原文逐字一致；BARRIER 语义（低估则无法跨垒、高估只拖慢收敛）、TEMP 缺省从引擎读、SIGMA 默认自适应、BIASFACTOR=inf 平坦目标、rct/zed/neff 语义、STATE_RFILE/WFILE 精确续算、UPDATE_UNTIL=0 冻结偏置——全部与 PLUMED 2.9 文档一致（正文[20][23]）。**通过**。
9. **PLUMED 集成限制**：web_fetch 手册 Using PLUMED 页原文三项限制：「interaction with GROMACS energy not supported」「incompatible with thread-MPI（多于 1 个 thread-MPI rank 报错）」「replica exchange flavors not yet implemented」——与正文[17]逐条一致。**通过**。
10. **WHAM**：自洽方程与 Kumar 1992（[10]）一致；「WHAM 为 MBAR 在直方图离散化下的特例」为文献通识（[7]）。**通过**。

## 四、08 章合并完整性加查（合并后首次验收）

| 加查项 | 结果 |
| --- | --- |
| 文献表 1–23 | 全部存在，顺序连续 |
| 正文上标 | 1–23 全部出现，无跳号、无重号、与文末一一对应（**但见问题 08-P1-1**） |
| 表 8-1..8-7 | 编号连续；正文引用：表 8-3（行137）、8-5（行235）、8-6（行332）、8-7（行473）；表 8-1、8-2、8-4 仅表题、正文无引（P2-2） |
| 图 8-1..8-5 | 编号连续；正文引用：图 8-1（行36）、8-2（行137）、8-3（行191）、8-4（行352）、8-5（行417）全部出现且与图题一致 |
| 8.5 节开始处 | `## 8.5 降维与聚类` 前为 8.4.3 结果解释边界，8.5 开头有引导段（「一条轨迹中每个构型由 3N 个笛卡尔坐标描述…」），衔接自然、无重复标题 |
| 小节编号连续性 | **发现重复编号：`### 8.4.2 计算流程的基本结构`（行 34，位于 8.1 节内部）与 `### 8.4.2 计算流程`（行 248，8.4 节内）编号重复，且 8.1 内小节序列 8.1.1→8.1.2→8.1.3→8.4.2 断裂 → P0** |

## 五、逐节问题清单

### 第 8 章（合并后首次验收）

- **[P0-1] 小节编号断裂/重复（8.1 节末尾混入 8.4.2）**
  位置：`08-自由能、增强采样与高级分析.md` 行 34 `### 8.4.2 计算流程的基本结构`（位于 `### 8.1.3 采样误差与模型误差` 之后、`## 8.2 炼金术自由能` 之前），与 8.4 节内行 248 `### 8.4.2 计算流程` 重号。
  原文摘录：“### 8.4.2 计算流程的基本结构 / 尽管方法各异，自由能计算的流程共享同一骨架：定义端点状态与路径（或反应坐标）→ 构建体系并平衡……图 8-1 给出通用流程……”
  修改建议：该小节为自由能方法的通用流程总览，属于 8.1「自由能计算框架」的收尾，建议改编号为 `### 8.1.4 自由能计算的通用流程`（标题可保留「计算流程的基本结构」措辞，避免与 8.4.2「计算流程」同名）；同时检查全文是否存在指向「8.4.2 计算流程的基本结构」的交叉引用并同步更新。另需确认 8.5 节正文及图 8-1 引用编号不受影响（图 8-1 编号不随小节编号变动，无需改）。
  级别：**P0（编号断裂）**。理由：REVIEW.md 一.4 及本任务指令「编号断裂均属 P0」；重复小节编号将直接破坏目录引用与跨节跳转。

- **[P1-1] 正文文献首次出现顺序与编号不一致**
  08 章正文上标首次出现顺序：1,3,2,4,…（`[3]` Torrie & Valleau 在 8.1.2 先于 `[2]` Kirkwood 出现；`[11]` gmx wham 先于 `[10]` Kumar 出现），违反 STYLE.md 五.3「引用编号按本章首次出现顺序排列」。
  修改建议：将 8.1.2 中 Torrie & Valleau 的引用处理为首先出现编号，或将文献表 2、3 的顺序与正文首次出现顺序对齐（即重排为 1,3,2 的语义或用交叉引用顺序重排编号），使编号与首次出现顺序一致；相应更新 refs/08 表与正文全部 `[2]`/`[3]`、`[10]`/`[11]` 引用点。
  级别：P1（引用体例）。

- **[P2-1] 08 章文献个别条目缺 DOI**：[13] Srinivasan 1998（JACS 120(37):9401-9409）、[15] Humphrey 1996（J Mol Graph 14(1):33-38）在文末未附 DOI，STYLE.md 五.2 要求每条含 DOI；建议补齐（均可在 Crossref 解析）。
- **[P2-2] 表 8-1、8-2、8-4 正文无引用**：三表仅有表题，正文未出现指向语句；建议在对应小节补一句引导（如 8.1.2 末尾「两类路径的对照见表 8-1」）。
- **[P2-3] 导言/章节号格式**：08 章二级节标题带「8.1」「8.2」编号，与 STYLE.md 七.2「章内所有二级节标题前不加编号」不一致（Docsify 自动生成编号）。此为历史遗留格式问题，可在全书统稿时统一处理（记录，不阻碍本项验收）。

### 第 9 章（首次验收）

- **[P2-1] 表 9-2 正文无引用**：表 9-2（GROMACS 采样统计工具表）仅有表题，正文在前一节（误差估计方法的选择准则）未出现「见表 9-2」类引导。建议在表 9-2 前补一句（如「表 9-2 汇总 GROMACS 中可直接使用的统计工具」）。
- **[P2-2] 跨章措辞重合两处**：与 03 章共用 Python 惯用法代码行（with open…，属代码惯用语，非段落重复）；与 04 章前置知识条目「第 1 章的版本基线、单位与符号约定」措辞相同（属结构化前置知识清单，非正文段落）。均不必处理，记录备案。
- **[P2-3] gen_seed 拼写**：正文用 `gen_seed`（下划线），mdp 实际关键字为 `gen-seed`（连字符）；GROMACS 对连字符/下划线不敏感（官方 mdp 说明「The difference between a dash and an underscore is ignored」），且正文其他处用词一致，不建议改动（记录。
- 其余：无 P0、无 P1。导言、结构、图表编号、引用编号、禁用表达、第二人称、占位符、跨章重复均达标。

## 六、结论

- **第 9 章（首次验收）：通过。** 全部机械项、引文抽查（10/10 通过）、关键论断核验、语言核查、跨章重复核查均满足 REVIEW.md 与 STYLE.md 要求，无 P0/P1。
- **第 8 章（合并后首次验收）：不合格（返工）。** 存在 P0：小节编号 8.4.2 重复且 8.1 节内编号断裂（`### 8.4.2 计算流程的基本结构` 错位于 8.1 内、与 8.4.2 重号）。按任务指令「任一 P0 未消除即 pass=false；编号断裂均属 P0」，整体验收判定 **不通过**。
- **返工范围（08 章）**：
  1. 将行 34 小节改编号为 8.1.4（或合并入 8.1 相应小节），消除 8.4.2 重号与 8.1 内编号断裂（P0）；
  2. 按首次出现顺序重排 08 章引用编号 2/3、10/11（P1）；
  3. 补齐 08 章文献 [13][15] 的 DOI（P2）；
  4. 补表 8-1、8-2、8-4 的正文引用（P2）。
- 返工完成后须重跑 08 章上标连续性检查与交叉引用检查。