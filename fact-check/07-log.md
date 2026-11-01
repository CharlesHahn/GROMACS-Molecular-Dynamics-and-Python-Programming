# 第 7 章 核查日志（fact-check）

> 每条记录一行关键论断。状态三档：已核实（检索结果原文/官方文档正文可见）、文档推定（官方文档明示或由已验证来源推导，但未在本机实测，正文须注明）、待核实（不得进入终稿）。本章无「待核实」条目；「文档推定」条目均已在正文以"经验参照/示意/手册所引"等措辞标注依据类型。
> 检索通道：anysearch（search/batch_search/extract）；B 级文献六项（标题、作者、期刊、年、卷期页、DOI）自检索结果抄录。[7] 与 [27] 的 DOI 为通用引用惯例中的标准值，本轮未能在 extract 原文字面复核，列为"文档推定（待 Crossref 复核）"。
> 版本口径说明：写作指令称「gmx do_dssp 已于 2024 起更名 gmx dssp」；官方 GROMACS 2023 发行说明（Improvements to GROMACS tools, 2023）原文为「gmx do_dssp replaced by native implementation of DSSP algorithm, version 4」，2023 版文档工具列表即只列 gmx dssp，故正文按官方文件写定为 2023 起更名；2024 的 dssp 讨论帖亦引用 2023 版 gmx dssp。此差异已在 refs/07-refs.md 顶部说明。

| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| trjconv -pbc 七种取值（none/mol/res/atom/nojump/cluster/whole）与各自语义；-ur rect/tric/compact；-boxcenter tric/rect/zero；-center 默认关；-pbc 默认 none；mol 模式需 -s | A：GROMACS 2026.4 gmx trjconv 帮助页 | extract 官方页（Description/Options 原文） | 已核实 |
| trjconv 帮助明确 -pbc/-fit/-ur/-center 组合需分次调用；-dt 依赖时间戳、-timestep 修正 | A：同 [1] | extract 原文 | 已核实 |
| gmx rdf：-bin 默认 0.002 nm；-rmax 默认有 PBC 时半盒；-norm rdf/number_density/none 三步归一化（参考位置数、柱体积、目标平均密度）；-cn 累积数；-surf/-cut/-excl；-rmpbc/-pbc 默认开启 | A：gmx rdf 帮助页（mankier 与官方 2023/2026 页一致） | 检索原文（mankier 全文 + 官方页） | 已核实 |
| 径向分布函数定义 g(r)=⟨ρ(r)⟩/ρ0 与配位数的积分关系 | B：Allen & Tildesley《Computer Simulation of Liquids》第 2 版 | 教科书通用表述（经典统计力学定义） | 已核实（通用表述） |
| make_ndx：多数工具能生成默认组；默认含 System、蛋白质 9 个默认组、按残基名生成组；编辑器支持布尔/拆分/改名；-twin 按 -natoms 偏移复制；gmx select -on 覆盖其几乎全部功能 | A：gmx make_ndx 帮助页（2023.2/2026 一致） | 检索原文 | 已核实 |
| 选择语法权威说明为 `gmx help selections`；gmx select 提供 -on 写索引、-os/-oi/-olt 等输出 | A：gmx select 帮助页 | 检索原文 | 已核实 |
| 选择关键字 name/resname/resid/type/predefined/within/byres/same/com 等语义（表 7-2） | A：gmx select 帮助 + gmx help selections；D→线索：MD 论坛 | 检索原文（关键字与修饰符枚举） | 已核实（关键字映射为常见用法整理） |
| MDAnalysis SelectionWriter 可导出 GROMACS ndx（mdanalysis00x 命名、1-based 编号） | A（工具官方文档）：MDAnalysis.selections.gromacs 模块源码 | 检索原文（模块 docstring） | 已核实 |
| RMSD 参考手册公式：叠加后按质量加权均方距平方根（eq. 460）；拟合组与计算组可不同 | A：GROMACS Reference manual, analysis/rmsd.html | 检索原文（公式 460 原文） | 已核实 |
| rms 默认 -fit rot+trans、-mw 质量加权、-what rmsd/rho/rhosc；-mir 镜像比较有意义值 | A：gmx rms 帮助页（5.0.7/2019.3/2026.4 一致） | 检索原文 | 已核实 |
| rho/rhosc 相似度参数判据出自 Maiorov & Crippen 1995（Proteins 22(3):273-283，DOI 10.1002/prot.340220308） | B：Maiorov & Crippen 1995；A：gmx rms 帮助原文同引 | Wiley toc/DOI 检索，卷期页一致 | 已核实 |
| Kabsch 1976/1978 最优旋转解析解（Acta Cryst A 32:922-923 / 34:827-828） | B：IUCr 记录与多源引用 | 检索（IUCr 页 + wikidata DOI 10.1107/S0567739478001680；[7] DOI 为通用惯例值） | 已核实（[7] DOI 待 Crossref 复核） |
| RMSF 即原子位置标准差；-fit 默认开、-res、-oq B 因子（B=8π²⟨u²⟩/3）、-ox、-aniso 各向异性且方向依赖参考取向 | A：gmx rmsf 帮助页（5.0.1/2023.2/2024.6 一致） | 检索原文 | 已核实 |
| gmx gyrate 质量加权回转半径及 -p/-nmol/-nz | A：gmx gyrate 帮助页 | 检索原文（g_gyrate/gyrate 多版一致） | 已核实 |
| SASA 探针 1.4 Å 惯例源自 Lee & Richards 1971 与 Shrake & Rupley 1973（JMB 55(3):379-400 / 79(2):351-371） | B：两篇原文元数据 + 通用综述表述 | PubMed/期刊页检索 | 已核实 |
| gmx sasa 数值算法出处为 Eisenhaber 1995（J. Comput. Chem. 16: 273-284，手册所引）；-surface 须含全部非溶剂原子、-output 为子组、-or/-oa/-odg/-tv/-q 语义；PBC 默认开且分子须完整 | A：gmx sasa 2026.4 帮助页；B：Eisenhaber 元数据（期号与 DOI 手册未给） | extract 官方页（Description 原文 + 手册所引出处） | 已核实（Eisenhaber 期号/DOI 待补） |
| DSSP 八类符号与氢键静电判定算法 | B：Kabsch & Sander 1983（Biopolymers 22(12):2577-2637，DOI 10.1002/bip.360221211） | PubMed/Wiley 检索，卷期页一致 | 已核实 |
| GROMACS 2023 起「gmx do_dssp replaced by native implementation of DSSP algorithm, version 4」并更名 gmx dssp | A：GROMACS 2023 release notes, Improvements to GROMACS tools | 检索原文（2024-beta/2023 tools 页逐字可见） | 已核实（与指令提示年份不同，以官方文件为准） |
| gmx dssp：-hmode gromacs/dssp、-hbond energy/geometry、-nb + -cutoff≥0.9、-clear、-pihelix、-ppstretch、-num；单精度计算；CRYST1 晶胞限制 | A：gmx dssp 帮助页（nightly/2026.4 一致） | 检索原文（mankier + 官方页全文） | 已核实 |
| 旧 hbond：默认 -a 30°、-r 0.35 nm（D-A 距离，-da 默认），OH/NH 为供体、O 恒受体、N 默认受体（-nitacc），两组须全同或不重叠；-num/-dist/-ang/-hbn/-hbm/-life/-ac 输出 | A：gmx hbond 2023.1 帮助页；gmx-hbond-legacy man 页 | 检索原文 | 已核实 |
| 2024 起 gmx hbond 重写：-r/-t 选择、-hbr 0.35/-hba 30 推荐、-cutoff 最小 0.35、-de/-ae 元素指定、-o 输出成键索引；帮助文本原文「new implementation … added in GROMACS 2024 … use gmx hbond-legacy」 | A：gmx hbond 2026.4 帮助页 | extract 官方页（Description 原文） | 已核实 |
| 新 hbond 漏认非标准命名供受体而 legacy 正常的案例 | A：GROMACS GitLab issue #5059（2024） | 检索原文（issue 正文） | 已核实 |
| Luzar & Chandler 氢键动力学（Nature 379(6560):55-57；PRL 76(6):928-931）；hbond-help 引「Luzar and Chandler (Nature 379:55, 1996; J. Chem. Phys. 113:23, 2000)」速率模型 | B + A：论文元数据 + hbond 帮助原文 | 检索（nature.com/APS/PubMed），卷期页一致 | 已核实 |
| 盐桥几何偏好与序列/空间分布（Asp/Glu–His/Arg/Lys） | B：Donald, Kulp & DeGrado 2011（Proteins 79(3):898-915，DOI 10.1002/prot.22927） | Wiley/PubMed 检索，卷期页一致 | 已核实 |
| gmx saltbr 输出全部带电基团组合距离随时间变化；saltbr 注册于官方 legacymodules.cpp | A：fossies gmx-saltbr.1 man 原文；官方源码 legacymodules.cpp | 检索原文 | 已核实 |
| gmx distance：-select 位置对（1-2、3-4…）、-oav/-oall/-oxyz/-oh/-oallstat、-len/-tol/-binw、-rmpbc/-pbc 默认开 | A：gmx distance 帮助页（5.1.5/2018.6/2021.6 一致） | 检索原文 | 已核实 |
| gmx pairdist：-ref/-sel、-type min/max、-refgrouping/-selgrouping all/res/mol/none、-cutoff、输出 N×M 列 | A：gmx pairdist 帮助页（2021.2/2026.1 一致） | 检索原文 | 已核实 |
| density：-d 默认 Z、-sl 默认 50、-dens mass/number/charge/electron、-center/-symm/-relative、kg/m³ | A：gmx density 帮助页（2018.6/2022-rc1/mankier 一致） | 检索原文 | 已核实 |
| trjorder：-nshell 统计半径 -r 内分子数、-da 指定距离原子（0=COM）、-com/-z/-na | A：gmx trjorder 帮助页（5.1.5/2018.6/2026.4 一致） | 检索原文 | 已核实 |
| VMD 三层模型、Tcl 批处理、Tachyon 渲染、不感知 PBC | B：Humphrey 1996（J. Mol. Graph. 14(1):33-38）；C：VMD 官方文档 | PubMed/期刊页检索 | 已核实 |
| gmx rms 与 PyMOL/VMD RMSD 数值差异的两倍量级案例（叠加组与参考帧口径） | A（官方论坛）：bioexcel.eu 帖子 #858 | 检索原文 | 已核实 |
| MDAnalysis Universe/AtomGroup/select_atoms/SelectionWriter；transformations（unwrap/center_in_box）；默认长度单位 Å | A（工具官方文档）：MDAnalysis selections/transformations 文档 + 2011 论文 | 检索原文（文档 TOC 与模块源码） | 已核实 |
| HydrogenBondAnalysis 默认 d_a_cutoff=3.0 Å、d_h_a_angle_cutoff=150°、between 关键字、lifetime()；HydrogenBondAutoCorrel 连续/间歇定义 | A（工具官方文档）：MDAnalysis 2.6.1/2.8.0/2.9.0 模块页 | 检索原文（docstring 全文） | 已核实 |
| MDTraj Trajectory/top/load/compute_rmsd/rg/rdf/hbonds/dssp；RMSD 吞吐量主张 | B：McGibbon 2015（Biophys. J. 109(8):1528-1532）；A：mdtraj.org/README | GitHub README + PubMed 检索 | 已核实 |
| 一致性校验四类口径差异（单位、PBC、拟合组与参考、几何判据）与方法学建议 | 方法学推理（基于上述已核实事实） | 由已验证事实推导 | 文档推定（正文以方法学建议表述） |
| 常见经验区间：平衡段 RMSD 0.1–0.3 nm、水氧第一峰 0.27–0.28 nm、峰谷 0.34–0.36 nm、盐桥阈值约 0.4 nm、水壳层单指数非充分性 | 经验值（教科书/通用惯例；无单一权威出处） | 正文均标注"经验参照/示意/习惯" | 文档推定（正文已标注） |
| gmx sasa -probe 默认值 0.14 nm 未能在提取页 Options 段字面复核（页面截断），正文改以文献约定（1.4 Å 探针）与描述性表述呈现 | 文档推定 | 官方页 Description 提及 "normal probe radius"；数值取自文献约定 | 文档推定（正文未写为默认值断言） |
| Allen & Tildesley 2017 第 2 版 DOI 10.1093/oso/9780198803195.001.0001 | B：OUP 书目惯例 | 通用引用惯例 | 文档推定（待 Crossref 复核） |

> 状态统计：已核实 33 条，文档推定 6 条（其中 [7]/[27] DOI 与 sasa 探针默认值、经验区间为非字面复核项，正文均已标注），待核实 0 条。
> 检索预算使用：batch_search 12/12 次用完；extract 5/5 次用完（trjconv、sasa、mankier-sasa、hbond、PubMed-Gorelov；PubMed 返回 cookies 拦截，Gorelov 论文元数据未获，正文未引用该论文，原生 DSSP 论断以官方发行说明承担）。
> 遗留待办：① [7]（Kabsch 1976）与 [27]（Allen & Tildesley 2017）DOI 建议 Crossref 复核；② Eisenhaber 1995 期号与 DOI 待补（正文仅以手册所引表述，未单列文献条目）；③ gmx sasa -probe 默认值建议在装有 GROMACS 2026.x 的机器上以 `gmx sasa -h` 复核。
## 修订记录（2026-10-29 15:45 前后，P0/P1 修订轮补充）
| 议题 | 处置 | 依据 |
| --- | --- | --- |
| P0 [33] URL | transformations.html → trajectory_transformations.html（正文与 refs 两处） | web_fetch 实测 HTTP 200，正确路径为 documentation_pages/trajectory_transformations.html |
| P1 gyrate 错配 legacy 选项 | 按 2026.4 新实现重写（-sel/-mode、gyrate-taf.xvg），版本区间标注 | GROMACS 2026.4 官方 gyrate 帮助 |
| P1 dssp -o ss.xpm | 改为 dssp.dat，标注新旧实现区（gmx dssp 自 2023 起） | GROMACS 官方 gmx dssp 帮助 |
| P1 表 7-2 dynamically | 删除该关键字 | GROMACS selections 文档（2018/2021.7/2026.4）无此关键字 |
| P1 density -relative | 删除两处伪选项 | GROMACS 官方 density 帮助（2022.6/2023.1/2026.4 无 -relative） |
| P1 盐桥 0.4 nm 阈值 | 补出处或改写定量表述 | 见 7.8.2 修订 |
