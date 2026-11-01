# 第 7 章《常规轨迹分析》验收报告（对抗性验收）

- 验收时间：2026-10-29
- 验收对象：`07-常规轨迹分析.md`（462 行）
- 验收依据：`REVIEW.md`、`STYLE.md`（未放宽任何条款）
- 核验通道说明：任务指定的 anysearch CLI 当日配额耗尽（返回 "You've reached your API key's total free quota for today"），经多次重试无效；按技能降级规则改用可用的等价官方通道：Crossref REST API（DOI/六项元数据）、GROMACS 官方手册在线页与 Sphinx `_sources` 原文、MDAnalysis/MDTraj 官方文档与源码。**本报告所有引文核验记录均标明实际通道**；anysearch 缺失已在核验栏目中注明，未据此放宽任何判定。

---

## 一、实测数字表（机械项）

| 项目 | 要求 | 实测 | 判定 |
| --- | --- | --- | --- |
| 汉字数（去 ``` 代码块 + 去「## 参考文献」之后，按 STYLE.md 第三节口径） | ≥10,000 | **10,686**（全章含代码块与文献为 11,283） | ✓ |
| 二级节（##） | ≥8 | **14**（学习目标、前置知识、分析前的必要处理、索引组与选择语法、结构稳定性、二级结构与相互作用、分布与溶剂化、可视化、Python 批量分析、结果的解释、常见错误、本章小结、习题、参考文献） | ✓ |
| 三级节（###） | ≥25 | **27** | ✓ |
| 表格 | ≥3 | **4**（表 7-1 trjconv -pbc 七模式、表 7-2 选择关键字、表 7-3 结构指标速查、表 7-4 DSSP 符号） | ✓ |
| 图 | ≥2（Mermaid 或已登记占位） | **3**（图 7-1/7-2/7-3，均 Mermaid） | ✓ |
| 参考文献条目 | ≥30 | **37**（正文上标 84 处、去重 37、编号 1–37 连续、无跳号/重号，文末与上标一一对应） | ✓ |
| 必备构件事序 | 导言→学习目标→前置知识→正文→常见错误→小结→习题→参考文献 | 齐全且顺序正确；导言 442 汉字（300–600）；学习目标 6 条（行为动词可检验）；常见错误 8 条（现象→成因→排查→处置格式齐全）；习题 8 题（#7、#8 为开放题） | ✓ |
| OUTLINE 承诺覆盖 | 每个三级节回答问题 | 7.1.1–7.8.2 全部承诺均有对应三级节（7.1.1 拆为两节、7.4.3/7.8 略有增补），无标题与内容不符 | ✓ |

## 二、引文核查（10 条随机抽样 + 追加核验）

随机抽样（PowerShell Get-Random，1–37）：**37, 18, 21, 34, 16, 17, 4, 28, 9, 11**。

| 编号 | 文献 | 核验方式 | 六项/可达性 | 结果 |
| --- | --- | --- | --- | --- |
| [37] | MDTraj documentation（mdtraj.org） | web_fetch 直达 | 站点存在，但 S3/CDN 对爬虫返回 403（浏览器可达，非死链）；内容另经 readthedocs API 页与论文核验 | 通过（注明反爬） |
| [18] | GROMACS 2023.1 gmx hbond | web_fetch 2023.1 手册 `_sources`（同树 200）+ 当前 legacy 页 | 2023.1 文档树在线，页面可达；旧实现默认判据逐字核对（见 §四-4） | 通过 |
| [21] | Luzar & Chandler, Nature 1996 | Crossref（10.1038/379055a0） | 标题/作者/期刊/年/卷期页/DOI 全齐：Nature, 1996, 379(6560): 55-57 | 通过 |
| [34] | Gowers et al., SciPy 2016 | Crossref（10.25080/Majora-629e541a-00e） | 六项全齐：SciPy Proceedings 2016, pp. 98-105 | 通过 |
| [16] | GROMACS 2023 发行说明 tools | web_fetch 官方页（HTTP 200） | 逐字核对：`gmx do_dssp replaced by native implementation of DSSP algorithm, version 4. … The new tool is called gmx dssp.` | 通过 |
| [17] | 2026.4 gmx dssp | web_fetch 官方 `_sources` | 页面可达；符号表与选项逐字核对（§四-4） | 通过 |
| [4] | 2026.4 gmx select | web_fetch 官方 `_sources` | 页面可达；`-on`、`gmx help selections` 等核对 | 通过 |
| [28] | 2026.4 gmx density | web_fetch 官方 `_sources` | 页面可达；默认值与选项核对（见 §四-5 的 -relative 问题） | 内容问题见 P1-4 |
| [9] | Maiorov & Crippen, Proteins 1995 | Crossref（10.1002/prot.340220308）+ 论文摘要 | 六项全齐：Proteins, 1995, 22(3): 273-283；摘要印证「小蛋白几何相似可偶然显著」论断 | 通过 |
| [11] | 2026.4 gmx gyrate | web_fetch 官方 `_sources` | 页面可达，但正文把 legacy 选项归到新实现名下（见 P1-1） | 内容错配 → P1 |

追加核验（非抽样，主动覆盖全部 B 级期刊文献与风险项）：

| 编号 | 文献 | 核验通道 | 结果 |
| --- | --- | --- | --- |
| [7] | Kabsch 1976 | Crossref（10.1107/S0567739476001873） | Acta Cryst A, 1976, 32(5): 922-923 ✅（log 中「待复核」已解决） |
| [8] | Kabsch 1978 | Crossref（10.1107/S0567739478001680） | Acta Cryst A, 1978, 34(5): 827-828 ✅ |
| [12] | Lee & Richards 1971 | Crossref（10.1016/0022-2836(71)90324-X） | JMB, 1971, 55(3): 379-400（Crossref 页 379-IN4）✅ |
| [13] | Shrake & Rupley 1973 | Crossref（10.1016/0022-2836(73)90011-9） | JMB, 1973, 79(2): 351-371 ✅ |
| [15] | Kabsch & Sander 1983 | Crossref（10.1002/bip.360221211） | Biopolymers, 1983, 22(12): 2577-2637 ✅ |
| [22] | Luzar & Chandler, PRL 1996 | Crossref（10.1103/PhysRevLett.76.928） | PRL, 1996, 76(6): 928-931 ✅（六项全齐） |
| [23] | Donald et al. 2011 | Crossref（10.1002/prot.22927） | Proteins, 2011, 79(3): 898-915 ✅ |
| [27] | Allen & Tildesley 2017 | Crossref（10.1093/oso/9780198803195.001.0001） | OUP 第 2 版，2017 ✅（log 中「待复核」已解决） |
| [30] | Humphrey 1996（VMD） | Crossref（10.1016/0263-7855(96)00018-5） | J. Mol. Graphics, 1996, 14(1): 33-38 ✅ |
| [31] | bioexcel 论坛帖 #858 | web_fetch 直达（HTTP 200） | 帖子存在、标题一致、内容吻合（gmx rms 0.5 nm vs PyMOL 2.5 Å 约两倍差异）✅ |
| [32] | Michaud-Agrawal 2011 | Crossref（10.1002/jcc.21787） | JCC, 2011, 32(10): 2319-2327 ✅ |
| [36] | McGibbon 2015（MDTraj） | Crossref（10.1016/j.bpj.2015.08.015） | Biophysical J., 2015, 109(8): 1528-1532 ✅ |
| [20] | GitLab issue #5059 | web_fetch 直达（HTTP 200） | issue 存在，标题「Inconsistency of gmx hbond analysis」，2024 版新 hbond 漏认 POPC 供/受体而 legacy 正常——与正文表述吻合 ✅ |
| [33] | MDAnalysis 2.0.0 transformations | web_fetch 直达 | **URL 实测 404（无法打开）**，正确页为 `…/documentation_pages/trajectory_transformations.html`（该页 200）→ **P0** |
| [5]/[35] | MDAnalysis selections / HBA | web_fetch | 均 200；HBA 默认 `d_a_cutoff=3.0 Å`、`d_h_a_angle_cutoff=150°` 逐字核对 ✅ |

**结论：10 条随机抽样的六项/可达性全部通过（[37] 为反爬拦截、非死链，已注明）；追加核验发现 [33] 引文 URL 404 —— 按 REVIEW.md「出现一条无法打开即判不合格」口径且审查者不得放宽，记为 P0，整章判不合格。**

## 三、关键论断抽查清单（必做复核 #4 逐条回查）

1. **gmx do_dssp → gmx dssp 更名年份**：官方 2023 发行说明（Improvements to GROMACS tools, 2023）原文逐字为「gmx do_dssp replaced by native implementation of DSSP algorithm, version 4 … The new tool is called gmx dssp」，2023 版文档工具列表仅列 `gmx dssp`。**正文写「自 GROMACS 2023 起」正确**，并已注明「旧版仅适用于 2022 及更早」；任务提示中的「2024 起更名」与官方文件不符，正文与 refs 顶部已作说明，验收以官方文件为准 ✓。
2. **gmx rms/rmsf/gyrate/sasa 默认值与输出文件**：
   - rms：`-fit` 默认 rot+trans、`-mw` 默认 yes、`-o` 默认 rmsd.xvg、`-what` rmsd/rho/rhosc、`-mir`、参考结构取自 `-s` —— 与 2026.4 帮助逐字一致 ✓。
   - rmsf：`-fit` 默认 yes、`-res`、`-oq`→B 因子 PDB、`-ox`→平均坐标、`-aniso` 方向依赖参考取向 —— ✓。
   - gyrate：**✗ 见 P1-1**（`-p`/`-nmol`/`-nz` 与 `gyrate.xvg` 是 legacy 工具接口；2026.4 新实现为 `-sel`/`-mode`，默认输出 `gyrate-taf.xvg`，2024 起更换）。
   - sasa：`-surface` 须为全部非溶剂原子、`-output` 为子组、`-or`/`-oa`/`-odg`/`-tv`、`-pbc` 默认开且分子须完整、算法出处 Eisenhaber 1995（J. Comput. Chem. 16, 273-284）—— ✓；**`-probe` 默认 0.14 nm 本轮从官方源复核成立**（log 遗留待办③消解）。
3. **索引组与选择语法**：make_ndx 默认组（System/9 类蛋白质组/按残基名）、1-based 编号、`-twin`+`-natoms`、`gmx select -on 覆盖 make_ndx 几乎全部功能` —— 与帮助逐字一致 ✓；选择关键字 name/resname/resid/type/within/byres/same/com/cog 等均见于官方 selections 文档 ✓；**「dynamically」关键字不存在（2018/2021.7/2026.4 关键字表均无）→ P1-3**。
4. **氢键几何判据**：旧实现（2023.1 原文与 gmx-hbond-legacy）`-a` 默认 30°（H-D-A）、`-r` 默认 0.35 nm（-da 默认 D-A 距离）、OH/NH 供体、O 恒受体、N 默认受体（-nitacc）、两组须全同或互不重叠 —— ✓；新实现（2026.4 原文）「new implementation … added in GROMACS 2024 … use gmx hbond-legacy」，`-cutoff` 最小且推荐 0.35、`-hbr` 0.35、`-hba` 30 推荐、`-de`/`-ae` 默认 N O —— ✓。
5. **RDF 与密度分布**：rdf `-bin` 默认 0.002 nm、`-rmax` 默认有 PBC 时半盒、三步归一化（-ref 位置数、柱体积、-sel 平均密度）与 `-norm` 三档、`-cn`、`-surf`、`-excl`（需 -s）、`-rmpbc`/`-pbc` 默认开 —— ✓；density `-d` 默认 Z、`-sl` 默认 50、`-dens` mass/number/charge/electron、`-center`/`-symm`、kg/m³ —— ✓；**「-relative」选项不存在（2022.6/2023.1/2026.4 三版均无）→ P1-4**。
6. **MDAnalysis/MDTraj 对象模型**：MDAnalysis Universe/AtomGroup/select_atoms（CHARMM 风格语法）、transformations（unwrap/center_in_box，2.0 文档正确页 trajectory_transformations.html 内容含 wrap/unwrap 模块）、HBA 默认 3.0 Å/150°、内部长度单位 Å（HBA 输出列即 Å）—— ✓（另见 P0：[33] URL 错误）；MDTraj Trajectory/top/load、`mdtraj.rmsd(target, reference, frame=0, atom_indices=…)` 签名与 nm 单位、compute_rg/rdf/hbonds/dssp 均存在（rmsd API 原文核对，其余据论文与 API 索引）—— ✓。

## 四、逐节问题清单（含原文摘录与修改建议）

### P0（判不合格项，须消除）

- **P0-1 引文无法打开（[33] URL 404）**
  位置：正文 7.7.1「轨迹级『即时变换』（transformations）…[33]」；refs/07-refs.md [33]。
  原文摘录（refs）：`[33] MDAnalysis documentation. Trajectory transformations ("on-the-fly" transformations)[EB/OL]. https://docs.mdanalysis.org/2.0.0/documentation_pages/transformations.html`
  实测：该 URL 返回 GitHub Pages 404（文件不存在）；MDAnalysis 2.0.0 文档中该页实际路径为 `documentation_pages/trajectory_transformations.html`（实测 200，内容即为变换工作流与 unwrap/wrap 模块）。属「被引地址无法打开」，按 REVIEW.md 二.1 口径判 P0。
  **修改**：将 refs [33] 与正文对应 URL 改为 `https://docs.mdanalysis.org/2.0.0/documentation_pages/trajectory_transformations.html`，并同步更新正文 [33] 上标对应的描述（内容无误，仅地址错）。

### P1（修订后方可进入下一环节）

- **P1-1 gmx gyrate 选项与输出为旧实现接口，与所引 2026.4 文档错配**
  位置：7.3.3 回转半径（整节）与命令示例。
  原文摘录：「`gmx gyrate` 计算组原子的回转半径以及绕 x、y、z 轴的分量，原子按质量显式加权，`-p` 输出相对主轴的回转半径，`-nmol` 把分析组等分为若干分子分别计算，`-nz` 计算沿 z 轴切片在 xy 平面内的二维回转半径[11]」及命令行 `gmx gyrate -s md.tpr … -o gyrate.xvg`。
  实测：2026.4 官方帮助原文（[11]）为「new implementation of the gyrate utility added in GROMACS 2024. If you need the old one, use gmx gyrate-legacy」，新接口为 `-sel`/`-mode`（mass/charge/geometry），默认输出 `gyrate-taf.xvg`；`-p`/`-nmol`/`-nz` 与 `gyrate.xvg` 只存在于 `gmx gyrate-legacy`（其帮助逐字核对）。本章对 hbond 已按新旧实现分述，gyrate 却把 legacy 行为写在 2026.4 工具名下，且未注明 gyrate 2024 重写。
  **修改**：按新实现重写本节（-sel/-mode、-o gyrate-taf.xvg），或明确标注「`-p`/`-nmol`/`-nz` 为 gmx gyrate-legacy 选项」并把命令改为对应接口；命令示例改为 `gmx gyrate -f … -sel 'protein' -o gyrate.xvg` 形式并注明 2024+。表 7-3 不受影响。
- **P1-2 gmx dssp 命令示例的 `-o ss.xpm` 与 2023+ 新工具不符**
  位置：7.4.1 命令示例。
  原文摘录：「生成 ss.xpm 二级结构时间图与 num.xvg 各类二级结构数目」`gmx dssp -s md.tpr -f md_whole.xtc -o ss.xpm -num num.xvg -hmode dssp`。
  实测：2026.4 帮助原文 `-o [<.dat>] (dssp.dat)`「Filename for DSSP output」；ss.xpm 是旧 gmx do_dssp 的输出约定，新实现不产生 xpm 时间图。
  **修改**：`-o ss.xpm` 改为 `-o dssp.dat`（或加 `-xvg` 相关说明），并把「ss.xpm 二级结构时间图」改为「dssp.dat 文本（可用 xpm2ps 等另行可视化）」。
- **P1-3 选择语法表 7-2 收录了不存在的关键字 `dynamically`**
  位置：7.2.2 表 7-2 末行。
  原文摘录：「`dynamically` | `dynamically within` | 动态更新选择，随帧变化」。
  实测：GROMACS 2018、2021.7、2026.4 三版 `gmx help selections` 关键字表逐字核对，均无 `dynamically`；文档中「动态选择」是含帧相关表达式时自动形成的属性，无此关键字。
  **修改**：删除该行；如需保留动态选择概念，改写为「（无关键字）含 within/com 等帧相关表达式的选择自动逐帧更新，无需关键字」，并引 [4]。
- **P1-4 gmx density 的 `-relative` 选项不存在**
  位置：7.5.2「`-relative` 用相对坐标分箱并按平均盒尺寸缩放输出[28]」；常见错误 #7「加 `-center`（必要时 `-relative`）」。
  实测：官方 help 的 2022.6/2023.1/2026.4 三版 Options 清单均无 `-relative`；相对坐标分箱自 5.0 起由 `-symm`/`-center` 行为自动完成（帮助原文：「The binning is now always performed in relative coordinates … scaled to the average box dimension」）。正文把它写成独立选项并引 [28]（2026.4），属事实性错误。
  **修改**：删除「-relative」及常见错误 #7 中的括注，改述为「-symm 自动开启 -center，分箱恒在相对坐标下进行并按平均盒尺寸缩放」。
- **P1-5 盐桥 0.4 nm 常用阈值无出处（正文自相矛盾）**
  位置：7.4.4「常用阈值在 0.4 nm 附近」；7.8.2「凡引用他人阈值与判据（如盐桥 0.4 nm、氢键 0.35 nm/30°），均给出文献出处」。
  正文承诺给出处而 0.4 nm 未给任何引用（[23] Donald 2011 描述的是几何偏好统计，未承担该阈值）。
  **修改**：补引阈值来源（如 Kumar & Nussinov 2002, JMB 或 Barlow & Thornton 1983 等经典盐桥距离统计），或将「0.4 nm」改述为「约 0.4 nm 的常用经验阈值（方法学记录须注明阈值来源）」并删去 7.8.2 中与之矛盾的承诺。

### P2（记录，统稿处理）

- P2-1：7.4.1「-nb 启用邻域搜索」——帮助中 `-[no]nb` 默认 yes，宜表述为「-nb 默认开启的邻域搜索」。
- P2-2：refs [5] 兼引 SelectionWriter 导出 ndx 的论断，但该内容在 MDAnalysis「Selection exporters」页（`selections_modules.html` / `selections/gromacs.html`），建议补引；「mdanalysis001 等名称」命名格式未逐字复核（源码路径未取到，建议统稿时对照 `MDAnalysis.selections.gromacs` docstring）。
- P2-3：7.4.4「-refgrouping/-selgrouping（all、res、mol）」——官方枚举为 all/res/mol/**none**，宜补全。
- P2-4：7.4.3 引 [21][22] 支撑 `-ac` 速率模型——hbond 帮助原文所引为「Luzar and Chandler (Nature 379:55, 1996; J. Chem. Phys. 113:23, 2000)」，与本章 [22]（PRL 76:928, 1996）不完全对应；建议补引 JCP 2000 或调整表述。
- P2-5：7.5.1「`-norm none` 仅做柱宽归一」——帮助原文为「Use only the first factor … only scaled with the bin width」，表述宜贴原文。
- P2-6：7.5.1「-rmax 默认在有 PBC 时为盒最短边的一半」——帮助原文作「half of the box size (with PBC)」；实现为最短半盒，措辞可保留但建议对齐帮助原文。
- P2-7：housekeeping——log/refs 顶部「[7]/[27] DOI 留待 Crossref 复核」与「sasa -probe 默认值待复核」两项本轮已由 Crossref/官方源消解，建议更新 refs 与 log 注记；pairdist 示例「GROMACS 2021 及以上」为保守标注（工具在 2021+ 存在），可保留。

## 五、语言与风格核查（REVIEW.md 四）

- 禁用表达（众所周知/强大/神器/yyds 等 15 项）：全文 0 命中 ✓
- 第二人称「你」/「我们」/「咱们」（代码块外）：0 命中 ✓
- 段首套话「首先/其次/最后」「让我们/接下来我们」「值得注意的是/总而言之」（行首机械检查）：0 命中 ✓
- 无出处的定量断言：仅盐桥 0.4 nm 一项（P1-5）；其余定量均标注「经验参照/示意/手册所引」并给出条件（RMSD 0.1–0.3 nm、水氧第一峰 0.27–0.28 nm 等）✓
- 术语首次出现给出英文原词（RMSD/RMSF/Rg/SASA/DSSP/RDF/PBC 等）✓；引用体例上标置于句末标点前 ✓

## 六、跨章重复核查（REVIEW.md 三.4）

用 grep 对 02–06 章比对本章高频主题：第 2 章仅提 trjconv 作文件压缩搬运；第 3 章以 gmx rms 的 rmsd.xvg 作 xvg 解析示例并前瞻引用本章；第 4 章涉及氢键（His 质子化、Martini）与 MDAnalysis ITPParser；第 5 章以 RMSD 平台作平衡判据（不同表述、不同深度）；第 6 章 6.7.2 从「输出质检/断裂修复」角度概述 trjconv -pbc 并明示「这是第 7 章所有距离类分析的前置约定」。**未发现整段重复或高度雷同段落，跨章引用均为交叉引用** ✓（P0 项不成立）。

## 七、结论

- **判定：不合格（返工）**。P0=1（[33] 引文 URL 404，无法打开），P1=5（gyrate 新旧接口错配、dssp -o ss.xpm、dynamically 伪关键字、density -relative 伪选项、盐桥阈值无出处）。
- **返工范围**：① 修复 [33] URL（一处字符串替换，消除 P0）；② 按新实现重写 7.3.3 gyrate 一节与命令；③ 修正 7.4.1 dssp 命令输出与描述；④ 删除/改写表 7-2 的 dynamically 行；⑤ 删除 density -relative 两处表述；⑥ 为盐桥 0.4 nm 补引用或改述；⑦ P2 项统稿处理。返工量小、单点替换为主，预计一轮内可完成；完成后再验（重点复验 ①③④⑤）。
- **备注（供全书规避）**：本章「新旧实现并存」的处理（hbond 分列）是亮点并应推广到 gyrate/dssp；同一版本迭代类工具（2023 dssp、2024 hbond/gyrate 重写、2024+ legacy 后缀）容易发生「把旧文档行为抄到新工具名下」的错配，后续章节验收应重点比对工具帮助原文的「new implementation … added in GROMACS XXXX」注记；在线引用务必以实测 URL 打开为准（[33] 教训）。
---

## 终验轮（2026-10-29）结论：P0 已消除，但修订引入悬空上标 [38]/[39] → 判不合格

**核验范围**：按任务指令仅复核 6 项（P0×1 + P1×5）；未重复全量文献抽查与禁用表达扫描（上轮已通过）。核验通道：web_fetch 官方页（GROMACS 2026.4 onlinehelp、MDAnalysis 2.0.0）+ Crossref REST API；汉字数与文献条数以 PowerShell 实测。

### 逐项核验结果

| 项 | 结论 | 核验证据 |
| --- | --- | --- |
| P0 [33] URL | ✅ 已解决 | 正文「## 参考文献」与 refs/07-refs.md 两处均改为 `…/documentation_pages/trajectory_transformations.html`；web_fetch 实测 HTTP 200，内容即 MDAnalysis 2.0.0「Trajectory transformations（on-the-fly transformations）」 |
| P1-1 gyrate | ✅ 内容已解决（见注 1） | 2026.4 官方 gmx-gyrate 页（HTTP 200）：「new implementation … added in GROMACS 2024」「-o (gyrate-taf.xvg)」「-sel」「-mode (mass/charge/geometry)」逐字一致；gmx-gyrate-legacy 页（HTTP 200）：-p/-nmol/-nz 与 -o (gyrate.xvg) 逐字一致；正文两条命令接口匹配 |
| P1-2 dssp | ✅ 已解决 | 2026.4 官方 gmx-dssp 页（HTTP 200）：`-o [<.dat>] (dssp.dat)`；正文命令 `-o dssp.dat`，明确不再产生 ss.xpm 时间图；新旧区间（2023 起 gmx dssp / do_dssp 仅 2022 及更早）与官方 2023 发行说明一致 |
| P1-3 表 7-2 | ✅ 已解决 | 表 7-2 九行关键字（name/resname/resid/type/protein/within/byres/same/com）无 dynamically；正文明言「不存在任何动态选择专用关键字」 |
| P1-4 density | ✅ 已解决 | 2026.4 官方 gmx-density 页（HTTP 200）Options 无 -relative（仅 -d/-sl/-dens/-ng/-center/-symm）；正文 7.5.2 与常见错误 #7 均无 -relative，-center/-symm 改述与官方文字一致 |
| P1-5 盐桥 0.4 nm | ⚠️ 内容已补出处，但 [39] 无文献条目（见注 2） | Barlow & Thornton 1983「Ion-pairs in proteins」经 Crossref 实测真实存在：JMB, 1983, 168(4): 867-885, DOI 10.1016/S0022-2836(83)80079-5 |

**注 1**：gyrate 一节主体已按新实现正确重写，但「2024 起须显式调用 gmx gyrate-legacy 才可使用」处引 [11][38]——[38] 在两处文献表均无条目。
**注 2**：盐桥阈值出处文字已在正文（7.4.4「0.4 nm（4.0 Å）的常用阈值沿自 Barlow 与 Thornton 对蛋白晶体结构中离子对的经典统计定义[39]」），但 [39] 在两处文献表均无条目，出处无法从文献表定位。

### 新发现问题（本轮修订引入，阻断项）

- **[38]/[39] 悬空上标**：正文上标最大编号 39（7.3.3 引 [38]、7.4.4 引 [39]），而正文「## 参考文献」与 refs/07-refs.md 均只列到 [37]（两处各 37 条、彼此一致）。违反 REVIEW.md 一.4「正文上标编号连续、无跳号、无重号，且与文末列表逐条对应」；引文无法从列表定位，按 REVIEW.md 二.1 属「无法打开」级引文缺陷 → P0 级结构缺陷（本轮新增），且第 6 项盐桥出处因此未真正可核验。
- P2 记录（不阻断）：7.4.1「调用外部程序时代的 -ver 4 选项随之并入新实现」可自官方句「native implementation of DSSP algorithm, version 4」读出，但新版 gmx dssp 实际无 -ver 选项，统稿时可微调措辞。

### 实测数字（PowerShell，STYLE.md 第三节口径）

- 汉字数（去 ``` 代码块 + 去「## 参考文献」）：**10,980**（≥10,000 ✓；上轮 10,686，修订净增约 294）
- 全文件汉字数：11,609；章节行数：464
- 文献条目：正文 37 = refs/07-refs.md 37 ✅（两处一致）；正文上标最大编号 39（含 2 条悬空）

### 终验判定

- **pass=false**：P0（[33] URL）确已消除，五项 P1 的内容与官方页面全部吻合；但复核发现正文上标 [38]/[39] 无对应文献条目，属本轮修订新增的引文/结构缺陷，不满足「6 项全部解决且正文无新增事实性错误」的通过条件。
- **修复建议（单点、极小，补条后即可 pass）**：在两处文献表（正文「## 参考文献」与 refs/07-refs.md）追加：
  - [38] GROMACS 2026.4 documentation. gmx gyrate-legacy[EB/OL]. https://manual.gromacs.org/current/onlinehelp/gmx-gyrate-legacy.html（访问日期：2026-10-29）.（本轮实测 HTTP 200）
  - [39] Barlow D J, Thornton J M. Ion-pairs in proteins[J]. Journal of Molecular Biology, 1983, 168(4): 867-885. DOI: 10.1016/S0022-2836(83)80079-5.（本轮 Crossref 实测六项齐全）
