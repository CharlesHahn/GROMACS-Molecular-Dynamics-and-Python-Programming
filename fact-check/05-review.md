# 第 5 章《能量最小化与平衡》验收报告（第二轮独立复核）

- 验收对象：`05-能量最小化与平衡.md`（GROMACS 2026.x，361 行，UTF-8 无 BOM / LF）
- 验收时间：2026-10-29（独立复核，与历史 05-review.md 为不同轮次）
- 依据：REVIEW.md（分级与判定，未放宽）、STYLE.md（字数口径、结构、语言、引用体例）
- 方法：PowerShell 脚本实测字数与结构；anysearch（search/extract）核对 9 条文献元数据（免费额度耗尽后改用 web_fetch 直接抓取官方文档 RST 源文、Crossref API、教程页面原文落盘精查，方法变通已记录）；跨章重复用 16-gram 交集扫描 04/06/07 章；全文正则检测禁用表达/套话/第二人称/引用编号首现顺序。
- 结论：**通过（pass=true）**。无 P0，无 P1；记录 7 项 P2（统稿时处理，均不影响放行）。

## 〇、与上一轮验收（05-review.md 历史版）的对照

上一轮判定「返工」，列出 6 项 P1。本轮对照当前章节文本逐条复查，**6 项 P1 已全部修复**：

| 上轮 P1 | 当前章节状态 | 复核 |
| --- | --- | --- |
| P1-1 5.5.2「Braun 等人在 2019 年」 | 现行文为「Braun、Moosavi 与 Smit 在 2018 年发表的论文中指出（期刊版与 arXiv 预印本双出处见文献[13]）」 | 已修复（2018 与 JCTC 14(10):5262-5272、arXiv:1805.02295 一致） |
| P1-2 三阶段工作流误归官方[1] | 导言「官方工作流在运行层面要求先完成能量最小化再做动力学[1]；教程实践进一步把动力学前的准备细分为 NVT 与 NPT 两步平衡」；图 5-1 注「阶段次序参照官方工作流[1]，NVT/NPT 划分依教程实践[5]绘制」 | 已修复（归属区分明确） |
| P1-3 教程 NPT 时长误引 100 ps | 5.7.1「教程以 NVT 100 ps、NPT 500 ps」、5.7.2「NVT 100 ps（50000 步）与 NPT 500 ps（250000 步，dt 均为 2 fs）[5]」、npt.mdp 注释「500 ps」 | 已修复（与 06_equil/07_equil2 页原文一致） |
| P1-4 表 5-4 tcoupl/pcoupl/tau_p 默认值 | 表 5-4 现为 `tcoupl: no`、`pcoupl: no`、`tau_p: 5`，出处 [2]/[2,4]；5.8 引言注明「默认值一律以 2026.4 官方 mdp 选项页为准」 | 已修复（与 mdp-options RST 逐字一致） |
| P1-5 5.8.1 引用编号倒序 | 现行文 SHAKE 句（[2,27]）已移至 LINCS/P-LINCS/SETTLE（[28,29,30]）之前；脚本核验正文引用首现顺序恰为 1–32 严格递增 | 已修复 |
| P1-6 [25][26][28][29] DOI 待补 | refs/05-refs.md 与章末列表均已补全（10.1039/C1CP22168J、10.33011/livecoms.1.1.5957、10.1002/(SICI)…、10.1021/ct700200b），并注明 Crossref 核验 | 已修复（本轮独立复核一致） |

## 一、实测数字表（独立复核，脚本输出）

| 指标 | 要求 | 实测 | 判定 |
| --- | --- | --- | --- |
| 汉字数（STYLE 第三节口径：去代码块、截去「## 参考文献」后） | ≥10,000 | **12,972**（代码块内另有 412 汉字，不计入） | 通过 |
| 导言字数 | 300–600 | 586 | 通过 |
| 二级节 `##` | ≥8 | 13（学习目标、前置知识、目的、算法、诊断、初速、NVT、NPT、判据、mdp 体系、常见错误、小结、习题；不含参考文献） | 通过 |
| 三级节 `###` | ≥25 | 26 | 通过 |
| 表格 | ≥3 | 4（表 5-1~5-4，表题均在表上方） | 通过 |
| 图 | ≥2 | 3 个 Mermaid 图（图 5-1/5-2/5-3，图题在下方；无需 TODO 登记） | 通过 |
| 常见错误 | ≥6 | 7，均为「现象 **→** 成因 **→** 排查步骤 **→** 处置」四段式 | 通过 |
| 习题 | ≥6，开放题 ≥2 | 7 题，第 6、7 题标注【开放题】 | 通过 |
| 参考文献 | ≥30 | 32 | 通过 |
| 正文上标编号 | 连续、无跳号重号、与列表逐条对应 | 首现顺序 1,2,…,32 严格递增无跳无重；章末列表与 refs/05-refs.md 32 条逐条一致 | 通过 |
| 必备构件与顺序 | 导言→学习目标→前置知识→正文→常见错误→小结→习题→参考文献 | 齐备且顺序正确 | 通过 |
| 学习目标 | 4–6 条行为动词 | 6 条（均以「能」开头，无了解/熟悉/掌握） | 通过 |
| OUTLINE 覆盖 | 5.1.1–5.8.3 主题不得删减 | 26 个三级节全覆盖 OUTLINE 承诺主题，另增「质心运动与温度定义」「mdp 模板」两节（允许增补） | 通过 |

## 二、文献抽查与核验结果（本轮随机抽样）

本轮随机抽取（PowerShell Get-Random，1–32 取 10）：**5, 7, 8, 9, 11, 12, 18, 21, 26, 28**。六项（标题/作者/期刊/年/卷期页/DOI）核对如下。**未发现伪造、错配或无法打开的文献。**

| 编号 | 核验方式 | 结果 |
| --- | --- | --- |
| [5] Lemkul Lysozyme 教程（C 级） | web_fetch 首页 + 05_EM/06_equil/07_equil2 页 | 打开正常；作者 Justin A. Lemkul（Virginia Tech）；页面正文确认 emtol=1000.0、NVT 100 ps、NPT 500 ps、C-rescale、gen_vel=no 续算等全部教学取值 | 通过 |
| [7] Páll 2020 | anysearch search → AIP 原文页 jcp/article/153/13/134110 | 标题/作者/期刊/年/卷期页吻合，DOI 10.1063/5.0018516 | 通过 |
| [8] Fletcher & Reeves 1964 | anysearch search → Oxford Academic 页 + DML 交叉引文 | Computer Journal 7(2):149-154，DOI 10.1093/comjnl/7.2.149 吻合 | 通过 |
| [9] Polak & Ribière 1969 | anysearch search + web_fetch Numdam 条目页 | 原文打开（pp. 35-43）；Numdam 登记「Tome 3 (1969) no. R1」，refs 写「3(16)」——期号标注方式差异（R1 vs 16），非伪造，见 P2-1 | 通过（P2 标注） |
| [11] GROMACS 2020.4 release notes | web_fetch 官方 2020.4 页 | 打开正常；含「Added workaround for RDRAND…Ryzen」整节，与 5.4.2 引用一致 | 通过 |
| [12] Berendsen 1984 | anysearch search → AIP 页 81/8/3684 | 吻合，DOI 10.1063/1.448118 | 通过 |
| [18] van Gunsteren & Berendsen 1988 | anysearch search → T&F DOI 页 10.1080/08927028808080941 | 吻合 | 通过 |
| [21] Parrinello & Rahman 1981 | anysearch search + AIP 原文 | 52(12):7182，1981，吻合 | 通过 |
| [26] Braun et al. 2019 | web_fetch Crossref API works/10.33011/livecoms.1.1.5957 | status=ok；标题「Best Practices for Foundations in Molecular Simulations [Article v1.0]」、7 位作者（Braun/Gilmer/Mayes/Mobley/Monroe/Prasad/Zuckerman）、期刊、卷 1 期 1 页 5957、DOI 全部吻合 | 通过 |
| [28] Hess LINCS 1997 | anysearch search → Wiley DOI 页 | 18(12):1463-1472，DOI 10.1002/(SICI)… 吻合 | 通过 |

补充：上一轮已核验样本 [1][3][14][15][17][22][29][31] 的六项信息继续成立（本轮以正文 [1]-[3] 抓取原文再次确认 [3] 初速算法与自由度公式）。

## 三、关键论断抽查（12 条，重点覆盖默认值/版本差异/算法归属/性能数值）

| 论断（章节） | 核查方式 | 判定 |
| --- | --- | --- |
| emtol=10.0、emstep=0.01、nsteps=0，收敛判据为最大力（5.2.3、表 5-4） | mdp-options RST `(10.0) [kJ mol^-1 nm^-1]`、`(0.01) [nm]`、`(0)` | 已核实 |
| integrator=steep/cg 语义、nstcgsteep=1000、简正模前需双精度（5.2.2） | mdp-options RST（steep/cg 条目逐字） | 已核实 |
| gen_vel 仅对 integrator=md 有意义；gen_temp 默认 300；gen_seed 默认 -1（5.4.1） | mdp-options RST「only meaningful with integrator=md」、`(300)`、`(-1)` | 已核实 |
| 初速：12 个 [0,1) 均匀随机数之和−6.0 近似正态，乘 √(kT/m_i)；先除质心速度再整体缩放（5.4.1） | reference-manual molecular-dynamics 原文 | 已核实 |
| gen_vel=yes 时从轨迹读入速度不被使用（5.4.1） | gmx grompp 在线帮助原文「These velocities will not be used when gen_vel = yes」 | 已核实 |
| 温度定义 ½N_df kT=E_kin，N_df=3N−N_c−N_com，周期体系 N_com=3、真空 6；质心速度通常每步置零（5.4.3） | reference-manual 原文 | 已核实 |
| 压力张量 P=2/V(E_kin−Ξ)、标量压力 tr(P)/3（5.6.1） | reference-manual 原文 | 已核实 |
| SHAKE 不能用于能量最小化（5.8.1、常见错误 4） | mdp-options RST「SHAKE can not be used with energy minimization」；[27] 为 SHAKE 算法出处（组引精度见 P2-3） | 已核实 |
| sd 恒温官方建议 tau_t=2 ps、温度偏差衰减为同 tau_t Berendsen 的两倍（5.5.4、表 5-1） | mdp-options RST sd 条目逐字 | 已核实 |
| PME 0.1 nm + 三次插值静电力精度 2–3×10⁻⁴；fourierspacing=0.12、pme-order=4、ewald-rtol=1e-5 默认（5.8.2） | mdp-options RST 逐字 | 已核实 |
| GROMACS 2023 提高 nstpcouple 默认值，2025.4 起 C-rescale 强制每周期 ≥25 步（tau_p<5 ps 且 dt≥2 fs 时体积涨落过大）、P–R ≥200 步；tau_p 默认 5 ps（5.6.2/5.6.3、表 5-4） | 2025.4 release notes RST 逐字（Issue 5424/5425）；mdp-options `(5) [ps]` | 已核实 |
| 水 1 atm、300 K 等温压缩率 4.5×10⁻⁵ bar⁻¹（5.6.2、表 5-4） | mdp-options RST compressibility 条目原文 | 已核实 |
| v-rescale（CSVR）= Bussi 2007，采样正则系综、存在守恒量、随机种子 ld_seed（5.5.3） | mdp-options RST v-rescale 条目（JCP 126, 014101） | 已核实 |
| NH 的 tau_t 为涨落周期而非弛豫时间（5.5.4） | mdp-options RST nose-hoover 条目逐字 | 已核实 |
| P–R 实现基于 MTTK（Martyna 1996）；P–R 需先以弱耦合/随机细胞缩放预平衡再切换（5.6.3） | reference-manual MTTK 章节 + P–R 章节原文 | 已核实 |
| nstxout/nstvout/nstfout/nstxout-compressed 默认 0、nstlog/nstenergy 默认 1000、nstcalcenergy=100 存精确和与涨落（5.8.3） | mdp-options RST 逐字 | 已核实 |
| AMD Ryzen 3000 RDRAND 使自动种子退化、多副本同构，对策显式设置种子（5.4.2） | 2020.4 release notes 原文 | 已核实 |

以上涉及版本差异（2023 nstpcouple、2025.4 约束、2020.4 RDRAND）、参数默认值、算法归属、性能精度数值的论断，**全部被 A/B/C 级来源原文支持，未发现「引 A 写 B」或「引综述当原始结论」**。

## 四、逐节问题清单（仅剩 P2，统稿时处理）

- **P2-1（refs [9]）**：Polak & Ribière 1969 refs 写「3(16): 35-43」，Numdam 官方登记为「Tome 3 (1969) no. R1, pp. 35-43」。二者指同一期卷（R1 为 Numdam 内部 fascicule 命名，16 为学界通行写法），非伪造或错配，但建议统一为 Numdam 登记形式或在注内说明两种编法，避免读者按 16 检索对不上档案。
- **P2-2（5.8.1/5.8.2/表 5-4）**：术语首现未补齐英文全称：PME（正文首现于表 5-4 行）、LINCS（5.2.3 首现）、SETTLE、trr/xtc（5.8.3 首现）均只有缩写；NVT/NPT 在导言首现无展开（前置知识处有「NVT（正则）与 NPT（等温等压）」可视为补救）。按 STYLE 四.4 建议在各自首现处补「particle mesh Ewald」「LINear Constraint Solver」「Settle（刚性水解析约束算法）」「全精度轨迹（trr）/压缩轨迹（xtc）」。
- **P2-3（5.8.1）**：「SHAKE 不能用于能量最小化[2,27]」把官方限制[2]与 SHAKE 算法原始文献[27]并列组引；[27] 本人（Ryckaert 1977）并不包含该限制。建议拆为「SHAKE[27] 约束算法不能用于能量最小化[2]」或类似句序，避免读者把限制归到 [27]。
- **P2-4（5.8.1、习题 5 相关）**：「氢原子键伸振动周期约 10 fs（分子模拟教科书的常用量级）」为无具体出处的定量量级；正文已标注「常用量级」降低风险，仍建议补一条 C/B 级出处（如 Leach 教科书对应章节）或改为区间表述「约 10 fs 量级」并保持标注。
- **P2-5（5.5.1）**：tau_t 参数四问中「取错后果」未明示（现文给出语义、分组必要性、0.1 ps 经验值依据，但未说 tau_t 过小/过大的后果）。建议补一句（过小耦合过强、扰动体系固有涨落；过大温度收敛过慢），与 emtol/emstep 的四问完整度对齐。
- **P2-6（跨章）**：5.4.2 与第 6 章 6.8 案例三均叙述 AMD Ryzen RDRAND 自动种子退化事实（分属「可复现性」与「硬件错误案例」两个语境，非段落级重复，16-gram 交集扫描 04/06/07 章未发现重复段落）。建议在 6.8 案例三处交叉引用「见第 5 章 5.4.2 节」，减少认知重复。
- **P2-7（5.2.3/表 5-4）**：nsteps=50000 教学值依据教程 minim.mdp 附件（content-type 限制无法在线读取，fact-check 日志已注明）；本轮经 05_EM 页确认 emtol=1000.0 与之配套，nsteps 数值仍属 C 级文档推定。建议在日志中把该行标注为「文档推定（C 级，附件不可读）」或将正文改为「教程 minim.mdp 用 50000」以明示来源边界。

## 五、语言与合规核查

- 禁用表达（众所周知/不言而喻/毋庸置疑/强大/极致/革命性/一站式/赋能/干货/小白/保姆级/避坑/踩坑/神器/yyds/绝绝子）：**0 处**。
- 禁用套话过渡（让我们/接下来我们/值得注意的是/总而言之）：**0 处**；段首「首先/其次/最后」机械排列：**0 处**；「我们」作叙述主语：**0 处**。
- 第二人称「你/您」作叙述主语：**0 处**。
- 无出处定量断言：正文中的经验量级（体积弛豫数十 ps、压力摆动 −数十~数百 bar、10 fs 键振动）均已显式标注「经验量级/教科书常用量级」，符合 STYLE 一.5 的「标明依据类型」要求；个别仍可补来源（P2-4）。
- 版本与平台标注：全文默认值均标注「GROMACS 2026.4 官方选项页」；版本差异标注适用区间（2023 版变更、2025.4 约束、2020.4 故障）；mdp 模板注释注明平台与版本；未被误标「实测」。
- 跨章重复：与 04/06/07 章 16-gram 交集仅结构性样板（「## 前置知识」「| --- |」）与术语级共现，无段落级重复（P2-6 交叉引用建议除外）。
- 命令可复制：三份 mdp 模板完整可复制，注释齐备；执行序列（grompp→mdrun、-deffnm、-t 检查点续算）与教程原文一致。

## 六、结论

**结论：通过（pass=true）。** 无 P0、无 P1；字数、结构、文献数量与真实性、编号一致性、语言合规全部达标；上一轮返工的 6 项 P1 已确认逐条修复。7 项 P2 不影响放行，建议统稿时按第四节处理（其中 P2-3 涉及引用精度、P2-4 涉及定量出处，建议优先）。

核验记录（2026-10-29）：DOI 10.1063/5.0018516、10.1093/comjnl/7.2.149、10.1063/1.448118、10.1080/08927028808080941、10.1063/1.328693、10.33011/livecoms.1.1.5957（Crossref API status=ok）、10.1002/(SICI)1096-987X(199709)18:12<1463::AID-JCC4>3.0.CO;2-H；原文 URL：manual.gromacs.org 的 mdp-options.rst / molecular-dynamics.rst / gmx-grompp.rst / 2020.4 与 2025.4 release-notes / getting-started、numdam.org/item/M2AN_1969__3_1_35_0、mdtutorials.com/gmx/lysozyme/{index,05_EM,06_equil,07_equil2}.html。anysearch 免费额度于当日耗尽后改用 web_fetch/Crossref 完成剩余核验（搜索命中 9 条 + 直连原文 4 条）。