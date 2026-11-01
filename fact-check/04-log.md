# 第 4 章 核查日志（fact-check）

> 每条记录一行关键论断。状态三档：已核实（检索结果原文/官方文档正文可见）、文档推定（官方文档明示但未在本机实测，正文须标注）、待核实（不得进入终稿）。本章无「待核实」条目。
> 检索通道：anysearch（search/batch_search/extract）。B 级文献六项（标题、作者、期刊、年、卷期页、DOI）自检索结果抄录并经 Crossref 复核；2026-10-29 修订中补全全部卷期页（含 [55]），正文与 refs/04-refs.md 已无「（卷期页待补）」标注。

| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| GROMACS 2026.0 将 AMBER ff14SB/ff19SB 移植为 AMBER14SB/AMBER19SB，并随附 OPC/OPC3 等新水模型 | A：GROMACS 2026.0 Release notes Highlights；GROMACS 官方论坛 2026 RC 公告（13047） | extract/检索原文（标题与正文均见） | 已核实 |
| AMBER19SB 在 GROMACS 中建议搭配 OPC 或 OPC3 水模型 | A：manual.gromacs.org 2026-rc user-guide force-fields 页 | 检索结果原文可见 | 已核实 |
| GROMACS 内建支持的 AMBER/OPLS/CHARMM27/GROMOS 列表及 CHARMM36 需外部获取 | A：Force fields in GROMACS 页（2023.1/2026-rc 多版本） | 检索结果原文可见 | 已核实 |
| 力场目录由 forcefield.itp、rtp、hdb、tdb、atp、specbond.dat 等文件组成；GMXLIB 与当前目录为搜索路径 | A：Reference manual: Force field organization | 检索结果原文可见 | 已核实 |
| `pdb2gmx` 按残基名-rtp-原子名匹配生成拓扑与坐标，支持 -ignh/-ss/-ter/-water 等选项 | A：gmx pdb2gmx 在线帮助 | 检索结果原文可见 | 已核实 |
| 2024 起 `pdb2gmx` 将命名 CYX 的半胱氨酸对自动按二硫键处理 | A：GROMACS 2024 major release notes（tools） | 检索结果原文可见 | 已核实 |
| 拓扑分分子型/体系两级；grompp 展开拓扑、以原子名核对坐标、-pp 输出预处理拓扑；净电荷非零报警 | A：gmx grompp 在线帮助（2020/2026 版） | 检索结果原文可见 | 已核实 |
| `-maxwarn` 忽略指定数量警告、`-zero` 将无默认参数成键项置零，属非正常使用选项 | A：gmx grompp 在线帮助 | 检索结果原文可见 | 已核实 |
| `solvate` 以预平衡水盒填充并更新 [ molecules ] 段；-cs/-radius 语义 | A：gmx solvate 在线帮助 | 检索结果原文可见 | 已核实 |
| `genion` 读取 tpr、替换溶剂水分子、更新拓扑；-neutral/-conc/-pname/-nname/-rmin 语义 | A：gmx genion 在线帮助 + mdtutorials lysozyme 教程第 4 步 | 检索结果原文可见 | 已核实 |
| `-conc` 语义为「添加至指定浓度」，已有离子不参与计算 | A：gmx genion 在线帮助（4.6.1 man page） | 检索结果原文可见 | 已核实 |
| 离子命名自 GROMACS 4.5 起统一为元素符号大写（NA/CL） | A：gmx genion 帮助；mdtutorials 教程 | 检索结果原文可见 | 已核实 |
| genion 报「No line with moleculetype 'SOL' found」多为换行/行尾问题（dos2unix 可修复） | C：GROMACS 官方论坛实例（12981） | 检索结果原文可见 | 已核实（教学性论断） |
| `editconf -bt` 支持 triclinic/cubic/dodecahedron/octahedron 四类；正交长方体为 triclinic 取 90° 角的特例、非 `-bt` 取值；-d 缓冲语义 | A：gmx editconf 2026.4 在线帮助（2016/2021.5/2026.4 三版枚举一致，见 04-review.md） | manual 页面 extract | 已核实 |
| 最小镜像约定成立条件为截断半径不大于盒最短边一半；grompp 校验盒尺寸与截断 | A：GROMACS Reference manual: Algorithms | 检索结果原文可见 | 已核实 |
| 盒缓冲 1.0 nm 为常规下限（1.2 nm 截断下避免镜像自作用） | 文档推定（官方教程常规做法 + Wassenaar & Mark 2006 盒型研究） | 依据教程与方法学文献推导 | 文档推定（正文已注明建议性质） |
| CHARMM36 建议 rvdw=rcoulomb=1.2 nm、rvdw-switch=1.0 nm、force-switch、关闭 DispCorr | A：Force fields in GROMACS 页 | 检索结果原文可见 | 已核实 |
| CHARMM36m 改善无序蛋白（IDP）骨架系综与螺旋含量偏差 | B：Huang 2017，Nat Methods 14(1):71-73，DOI 10.1038/nmeth.4067 | 检索（PubMed/academicCharmm，卷期页以期刊 slug 确认） | 已核实 |
| ff19SB 以水相 QM 势能面拟合 20 种氨基酸特异主链参数并含 CMAP；作者推荐配 OPC 水 | B：Tian 2020（chemrxiv/figshare/zenodo 摘要一致；卷期页经 Crossref 复核为 JCTC 16(1):528-552） | 检索结果原文可见 | 已核实 |
| OPLS-AA/M 针对肽与蛋白二面角能学的修订 | B：Robertson 2015，JCTC 11(7):3499-3509 | 检索（Yale 课题组页 + ACS 页 slug） | 已核实 |
| Martini 3 重新平衡珠相互作用并引入新珠型与亚标签；2.x 框架见 Marrink 2007 | B：Souza 2021（Nature Methods，DOI 10.1038/s41592-021-01098-3，卷期页 18(4):382-388）；Marrink 2007 JPCB 111:7812-7824 | extract 原文（摘要与参考文献表） | 已核实 |
| TIP3P 参数出处与扩散偏快特征；SPC/E 自极化修正；TIP4P-Ew/TIP4P/2005/OPC 参数出处 | B：Jorgensen 1983；Berendsen 1987；Mark & Nilsson 2001；Horn 2004；Abascal & Vega 2005；Izadi 2014 | 检索多源（期刊页、SklogWiki 参数表、OpenMM 手册参考文献表） | 已核实 |
| OPC 为「三电荷四位点」模型，几何自由优化 | B：Izadi 2014，JPCL 5(21):3863-3871 | 检索（ADS 摘要 + 引用原文） | 已核实 |
| Drude 振子可极化框架与 CHARMM 族 Drude 蛋白力场 | B：Lamoureux & Roux 2003；Lopes 2013 | 检索（OpenMM 手册参考文献表 + 期刊记录） | 已核实 |
| ACPYPE 为 ANTECHAMBER 的 Python 包装，可输出 GROMACS 拓扑 | B：Sousa da Silva & Vranken 2012，BMC Res Notes 5:367 | 检索（PubMed/GitHub/bio2byte 多源，DOI 与卷期一致） | 已核实 |
| GAFF 与 AMBER 蛋白力场在电荷/1-4 方案上配套 | B：Wang 2004（GAFF）；A：Force fields in GROMACS 页 | 检索结果原文可见 | 已核实 |
| LigParGen 输出 OPLS-AA 参数，默认 1.14\*CM1A-LBCC 电荷 | B：Dodda 2017（NAR 45(W1):W331-W336）；Dodda 2017（JPCB 121(15):3864-3870） | 检索结果原文可见 | 已核实 |
| SMIRNOFF 直接化学感知原理；Parsley/Sage 为 OpenFF 小分子力场 | B：Mobley 2018；Qiu 2021；Boothroyd 2023（Sage 卷期页经 Crossref 复核为 19(11):3251-3275） | 检索结果原文可见（DOI/卷期多源一致） | 已核实 |
| RESP 电荷拟合方法 | B：Bayly 1993，JPC 97(40):10269-10280 | 检索（ACS 页 slug + 引用记录） | 已核实 |
| AM1-BCC 模型 I（2000）与「快速高效电荷」表述 | B：Jakalian 2000，JCC 21(2):132-146 | 检索（DBLP/PubMed 卷期一致） | 已核实 |
| CHARMM-GUI Membrane Builder 提供 180+ 脂型并输出 GROMACS 输入与平衡协议 | B：Wu 2014，JCC 35(27):1997-2004；C：charmm-gui.org | 检索（Scopus 元数据 V35/IS27/SP1997/EP2004） | 已核实 |
| 金属离子经典建模四类模型分类及二价/过渡金属参数化差异 | B：Li & Merz 2017，Chem Rev 117(3):1564-1686 | 检索（scholars.luc/ACS/引用记录元数据齐全） | 已核实 |
| parmbsc1 为 DNA 力场修正，经大量体系验证 | B：Ivani 2016，Nat Methods 13(1):55-58 | 检索（nature.com/IRB 页，卷期页一致） | 已核实 |
| GLYCAM06 与 AMBER 蛋白混用时需处理 1-4 作用尺度差异 | B：Kirschner 2008；C：AMBER 邮件列表讨论 | 检索（scholar 卷期 + 邮件列表原文） | 已核实（方法学提示） |
| MolProbity 提供 clashscore/Ramachandran/rotamer 等全原子验证 | B：Williams 2018，Protein Sci 27(1):293-315 | 检索（PMC 全文页面可见） | 已核实 |
| PROPKA3/H++ 用于蛋白残基 pKa 预测与加氢处理 | B：Olsson 2011；Anandakrishnan 2012 | 检索结果原文可见（卷期页与 DOI 齐全） | 已核实 |
| 配体参数化产物需经电荷/原子名/参数缺口/几何/短时平衡验证；「勿盲目接受参数化输出」 | C：mdtutorials protein-ligand 教程 + 方法学推断 | 检索结果原文可见 | 已核实（教学性论断） |
| GROMACS 2026 的 AMBER14SB/19SB 移植是否随附 parmbsc1 等核酸修正需当次安装核对 | 文档推定（2026 Highlights 未逐项列出核酸修正；官方论坛 13106 讨论移植范围） | 依据官方发布说明与论坛讨论 | 文档推定（正文已注明） |
| `pdb2gmx` 对 His 质子化态默认按最优氢键几何自动判定，需 `-his` 才逐残基交互；该自动判定自早期版本（4.6.1/2016/2018 至 2026.4 帮助逐字一致）即为默认、并非 2026 引入；`-dist` 默认 0.3 nm 为氢键判据而非二硫键判据 | A：gmx pdb2gmx 在线帮助（4.6.1/2016/2018/2026.4 Description/Options 原文，前版本经 04-review.md 与本次 extract 复核） | manual 页面 extract | 已核实 |
| 二硫键 specbond 判据为 Sγ–Sγ 距离落入 specbond.dat 参考值（条目约 0.20 nm）的 ±10% 容差 | A：GROMACS 发行 specbond.dat 条目（CYS SG 1 CYS SG 1 0.20 CYS2 CYS2）；D→核验线索：gmx-users 论坛 2007/2014 帖子 | anysearch 检索 + 邮件列表原文 | 已核实（数值以具体力场文件为准） |
| `genion` 自 GROMACS 4.6 起默认随机替换溶剂分子，当前帮助无 `-random` 选项；`-rmin` 为离子与溶质（非溶剂）间最小距离 | A：gmx genion 2026.4 在线帮助（Description/Options 原文） | manual 页面 extract | 已核实 |
| 官方「典型模拟流程」图止于溶剂化（节点 pdb2gmx→editconf→solvate→grompp→mdrun，无 genion）；带电荷体系需 solvate 后 grompp+genion 再重新 grompp | A：GROMACS 2026.4 user-guide flow.html（digraph 节点原文） | manual 页面 extract | 已核实 |
| [40] Lamoureux & Roux 2003 真实 DOI 为 10.1063/1.1589749（原写 1.1599740 无法解析，系数字转录错误） | B：Crossref /works/10.1063/1.1589749 | Crossref REST extract（标题/作者/卷期页与列表全吻合） | 已核实 |
| [55] Sage 卷期页为 JCTC 2023, 19(11): 3251-3275 | B：Crossref /works/10.1021/acs.jctc.3c00039 | Crossref REST extract | 已核实 |
| `genion` 现行版本随机替换溶剂分子为单原子离子，帮助无静电势选位/`-random` 选项；`-conc` 浓度按输入 `.tpr` 盒体积计算 | A：gmx genion 2026.4 在线帮助（Description/Options/Known Issues 原文） | manual 页面 extract | 已核实（P0-2 处置后与 4.7.3 一致） |
| `Interchange.to_gromacs(prefix, decimal)` 中 prefix 决定输出文件名（"foo" 产出 foo.top/foo.gro），第二位置实参为 decimal；正文示例已改为 `to_gromacs("lig")` | A：openff-interchange stable API autosummary（to_gromacs 签名与参数说明原文） | docs.openforcefield.org extract | 已核实（P1-4 处置） |
| MDAnalysis ITPParser 的 include_dir 默认硬编码 /usr/local/gromacs/share/gromacs/top/ 且不读取 GMXLIB；`.top` 扩展名有 GROMACS/AMBER 二义性，官方 docstring 示例显式传 topology_format='ITP'；Universe 将 kwargs 传给拓扑解析器的 parse() | A：MDAnalysis 2.2.0 ITPParser 源码（docstring 与 parse 签名原文）、universe 源码 | docs.mdanalysis.org extract | 已核实（P1-5 处置） |
| CHARMM36 族修订版 TIP3P 的 GROMACS 移植版中氢原子带 Lennard-Jones 参数（移植版说明给出氢原子 ε 及 -DUSE_MODIFIED_TIP3P_EPS 调整选项）；正文「修订版 TIP3P」仍引 [24]，H 带 LJ 引 [63] | C：MacKerell 实验室 CHARMM36 Files for GROMACS 页[63] | 页面 extract（原文见 ε on H atoms 与 USE_MODIFIED_TIP3P_EPS） | 已核实（P1-6 处置） |
| specbond.dat 默认二硫键条目的目标残基为 CYS2（AMBER），CYX 为 CHARMM/输入命名；正文 4.3.2 与常见错误 #6 已按此区分表述 | A：GROMACS 发行 specbond.dat 条目（CYS SG 1 CYS SG 1 0.20 CYS2 CYS2）；同见第 47 行 | 同第 47 行来源 | 已核实（P2-1 处置） |
| GROMACS 发行包内建 OPLS 力场为 OPLS-AA/L 版本（官方手册 force-field-organization 页明确列名） | A：Force field organization 页（2026.4，原文列 OPLS-AA/L all-atom force field） | manual 页面 extract | 已核实（P2-4 处置，正文已补引 [12]） |

> 状态统计：已核实 48 条，文档推定 2 条，待核实 0 条。原「待补 8 条」经 Crossref 复核：[10][17][19][20][21][23][27] 条目内已含卷期页、属标注残留已清理，[55] 卷期页已补填为 19(11): 3251-3275；2026-10-29 修订后无待补条目。
> 2026-10-29 第二轮修订记录：P0-1（His 版本断言）已删「2026 基线行为，更早版本为逐一询问」，改述为「该自动判定自早期版本起即为默认行为」；P0-2（genion 括注）已删「计算静电势选定替换位点」，改述为随机替换并注明 `-conc` 按 tpr 盒体积计算；P0-3（editconf 枚举）正文与表 4-5 已改为 triclinic/cubic/dodecahedron/octahedron，rectangular 作 triclinic 90° 特例；P1-4（OpenFF 调用）改为 `to_gromacs("lig")`；P1-5（MDAnalysis 示例）补 `topology_format='ITP'` 与 `include_dir` 说明；P1-6（[24] 承担范围）「氢原子带范德华参数」改引新增 [63]（MacKerell 实验室页）。P2 处理：CYS2/CYX 区分表述、0.15 mol/L 近似标注、OPC 刚性几何表述、OPLS-AA/L 补引 [12]、菱形十二面体默认推荐加注、[53] 转义统一；glossary.md 缺失等两项为全书级事项，记录备查。
## 修订记录（2026-11-07，P0-2 与 P1-4 修订轮）
| 议题 | 修订 | 依据 |
| --- | --- | --- |
| P0-2 genion 随机替换表述 | 重写 4.7.3 括注：随机替换为长期默认行为，官方档案自 4.0.1 起 -random 默认开启，4.6 系列后期移除，当前版本无 -random 项 | GROMACS 官方档案 4.0.1/4.6.1/4.6.6 genion 页（验收第四轮独立核验） |
| P1-4 mmCIF 政策出处 | 正文 4.2.1 补「wwPDB 自 2019 年 7 月起对晶体学方法结构强制采用 PDBx/mmCIF 为唯一沉积格式[64]」；文献表新增 [64] | Adams et al. 2019, Acta Cryst. D 75(4):451-454, DOI:10.1107/S2059798319004522（OSTI 记录核验） |
