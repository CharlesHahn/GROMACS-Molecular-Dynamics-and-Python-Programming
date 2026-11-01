# 第 1 章 核查日志（fact-check）

> 每条记录一行关键论断。状态三档：已核实（原文可见，含检索结果原文/官方文档正文）、文档推定（官方文档明示但未在本机实测，正文须标注）、待核实（不得进入终稿）。本章无「待核实」条目。

| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| GROMACS 2026.4 为当前版本文档站点（current 链接指向 2026.4）；2026 系列主版本于 2026-01-19 发布 | A：manual.gromacs.org/current 页面标题「GROMACS 2026.4 documentation」；release notes Highlights 首句 | web_fetch 官方安装指南与 Highlights 原文 | 已核实 |
| GROMACS 2026 Highlights：ff14SB/ff19SB 移植为 AMBER14SB/AMBER19SB、纳入 OPC/OPC3 水模型；HIP 后端完整卸载支持；H5MD 实验性轨迹输出；NNP 模块扩展（链接原子、pairlist 输入、静电嵌入） | A：manual.gromacs.org/current/release-notes/2026/major/highlights.html | web_fetch 原文（四段要点逐条可见） | 已核实 |
| 平台支持：任意 Linux 发行版、macOS、Windows；架构 x86-64、POWER（含 POWER9）、ARMv8、RISC-V；编译器最低 gcc 11 / clang 14 / MSVC 2019；CMake ≥3.28；C99/C++17 | A：GROMACS 2026.4 Installation Guide，Prerequisites/Compiler/CMake 节 | web_fetch 安装指南原文 | 已核实 |
| GPU 后端推荐：NVIDIA→CUDA（Toolkit ≥12.1、compute capability ≥5.0）；AMD→SYCL（AdaptiveCpp）或 HIP（GROMACS 2026 起完整卸载支持）；Intel→SYCL（oneAPI DPC++）；Apple M 系列→OpenCL（官方已标记 deprecated，仍为 M 系列唯一后端） | A：安装指南 GPU support 节；2026 Highlights | web_fetch 原文 | 已核实 |
| GROMACS MD 单位制：基础单位 nm、ps、u、e、K；导出能量 kJ·mol⁻¹、力 kJ·mol⁻¹·nm⁻¹、压力 bar、速度 nm·ps⁻¹；常数取 CODATA 2010 | A：Reference Manual Definitions and Units 页（标题与 Table 2/3 原文） | web_fetch 原文 | 已核实 |
| 手册单位陷阱：长度改用 Å 时时间单位变为 0.1 ps；能量改用 kcal·mol⁻¹ 时时间单位约 0.488882 ps 且静电能量失真；系统内单位须自洽 | A：Definitions and Units 页 MD units 节 | web_fetch 原文 | 已核实 |
| 默认混合精度（坐标/速度/力单精度存储、关键变量双精度累积），GMX_DOUBLE=on 可切换双精度 | A：Definitions and Units 页 Mixed or Double precision 节 | web_fetch 原文；未在本机编译实测 | 文档推定（正文 1.7.1 节按文档陈述） |
| GROMACS 演进：1995 年 Berendsen 等首篇方法学文献；2008 年 4.0（C++ 重写、域分解）；2013 年 4.5（大规模并行）；2015 年 Abraham 主文献（多级并行架构）；2016 年起年度版本 | B：文献 [29][30][31][1] 元数据（Crossref 核验）；叙述层次为文献一致描述 | Crossref API 逐条解析六项元数据；Abraham/Páll 条目另经 02 章 refs 交叉核验 | 已核实 |
| 1AKI 条目：鸡卵清溶菌酶正交晶型、1.5 Å、129 残基、原子数 1079、结构评定信息 | RCSB PDB 条目页（rcsb.org/structure/1aki） | 检索结果（条目页摘要：Atom Count 1,079；Modeled Residue Count 129） | 已核实 |
| Blake 1965：Structure of hen egg-white lysozyme, Nature 1965, 206: 757-761，DOI 10.1038/206757a0；溶菌酶为首批原子级酶结构之一 | B：Nature/PubMed（pubmed 5891407；nature.com/articles/206757a0） | 检索结果多源交叉（标题、卷页、DOI 一致） | 已核实 |
| Verlet 1967：Computer "experiments" on classical fluids. I., Phys. Rev. 1967, 159(1): 98-103，DOI 10.1103/PhysRev.159.98 | B：Physical Review（Crossref） | Crossref API 核验六项 | 已核实 |
| Frenkel 2013：Simulations: the dark side, Eur. Phys. J. Plus 2013, 128(1): 10，DOI 10.1140/epjp/i2013-13010-8 | B：Springer/ResearchGate 检索 | 检索结果（Springer 文章页 DOI 与卷期一致） | 已核实 |
| Baker 2016：1,500 scientists lift the lid on reproducibility, Nature 2016, 533(7604): 452-454，DOI 10.1038/533452a；调查显示逾七成受访者无法重现他人实验 | B：Nature 官网与 PubMed（PMID 27225100） | 检索结果原文摘要可见 | 已核实 |
| 算法组件原始文献六项：Nosé 1984（Mol. Phys. 52(2):255-268）、Hoover 1985（Phys. Rev. A 31(3):1695-1697）、Berendsen 1984（JCP 81(8):3684-3690）、Bussi 2007（JCP 126(1):014101）、Parrinello-Rahman 1981（J. Appl. Phys. 52(12):7182-7190）、Essmann 1995（JCP 103(19):8577-8593）、Hess 1997 LINCS（JCC 18(12):1463-1472）、Ryckaert 1977（J. Comput. Phys. 23(3):327-341） | B：各刊（Crossref） | Crossref API 批量核验六项；Bussi 文章号另经 AIP 文章页确认 | 已核实 |
| 力场文献：Huang 2017 CHARMM36m（Nat. Methods 14(1):71-73，DOI 10.1038/nmeth.4067）；Lindorff-Larsen 2010 ff99SB 侧链扭转改进（Proteins 78(8):1950-1958）；Marrink 2007 Martini（JPCB 111(27):7812-7824） | B：各刊（Crossref） | Crossref API 核验六项 | 已核实 |
| 生态工具文献：Humphrey 1996 VMD（J. Mol. Graph. 14(1):33-38）；Michaud-Agrawal 2011 MDAnalysis（JCC 32(10):2319-2327）；McGibbon 2015 MDTraj（Biophys. J. 109(8):1528-1532）；Tribello 2014 PLUMED 2（CPC 185(2):604-613）；Harris 2020 NumPy（Nature 585:357-362）；Vijay-Kumar 1987 ubiquitin 1.8 Å 精修结构（JMB 194(3):531-544） | B：各刊（Crossref） | Crossref API 批量核验六项 | 已核实 |
| 教材与专著：Frenkel & Smit, Understanding Molecular Simulation, 2nd ed., Academic Press, 2002；Allen & Tildesley, Computer Simulation of Liquids, 2nd ed., Oxford University Press, 2017 | C：WorldCat/ScienceDirect/OUP 检索 | 检索结果（出版年份、出版社、版本一致） | 已核实 |
| GROMACS 官方教程套件位于 tutorials.gromacs.org，含 Introduction to Molecular Dynamics 等 notebook 教程，CC-BY-4.0 许可 | A/C：tutorials.gromacs.org 首页 | web_fetch 原文（教程列表与许可说明可见） | 已核实 |
| 官方下载页 manual.gromacs.org/documentation/current/download.html 存在；conda-forge 提供 gromacs 预编译包 | A：官方下载页；anaconda.org/conda-forge/gromacs | 02 章 refs 已核验条目复用 | 已核实 |
| 性能类推断：单张消费级 GPU 可承担教学体系生产运行；普通工作站数天覆盖数百 ns；2 万原子体系数分钟内完成平衡 | 文档推定（依据 Páll 2020 综述报道与典型硬件水平推理） | 正文已显式标注「推断、未经实测」，并指向第 2 章 2.7 节自检 | 文档推定（正文已标注） |
| GB/T 7714-2015《信息与文献 参考文献著录规则》为国家标准 | 国家标准文献（客观事实） | 标准编号与发布年属确定事实 | 已核实 |

## 检索过程说明

- 检索通道：anysearch CLI（`D:\CharlieAPP\C_Python\python.exe` + `anysearch_cli.py`）、Crossref REST API（api.crossref.org）、官方文档 web_fetch、RCSB/PubMed/Nature 官方页面。
- B 级文献均以 Crossref API 解析六项元数据（作者、标题、期刊、年、卷期页、DOI）；Bussi 2007 与 Shirts-Chodera 2008 的文章号分别经 AIP 文章页与 Crossref article-number 字段确认。
- A 级文档均以 web_fetch 打开原文核验（安装指南、release notes Highlights、Definitions and Units、tutorials 首页）。
- 正文中全部性能/规模类数值均标注推断属性并经第 2 章 2.7 节基准路径实测修正；本章无未经核实的数值断言。
- 文献 [21] 与 [1][22] 等在本书 refs/02-refs.md 中已有核验记录，本日志标注复用。

## 修订记录

- 2026-10-30 初稿：全文 1.1–1.8、常见错误、小结、习题、参考文献 38 条落盘；三级节 25 个；正文汉字 14497（STYLE 口径，脚本实测）。
- 引用编号按正文首现顺序 1–38 全量核对：无缺失、无跳号、无超界。
## 修订记录（2026-10-30，验收返工轮）
| 项 | 处置 |
| --- | --- |
| P0 引用编号 | 全章按首现顺序重排至 1-38，范围引用（[8-11] 等）组内升序；refs 同步 |
| P1-1 表 1-6 依赖列 | 按各章前置知识实际内容逐行修正（3章=2、5章=2,3,4、6章=1,2,5、7章=2,3,4,6、8章=1,4,5,6,7,9*、9章=1,3,6,7） |
| P1-2/P1-3 案例口径 | 3 nm→6 nm 盒（对应约 2 万原子）；1AKI 蛋白重原子约 1000（沉积合计 1079 含 78 水氧）；习题 2 同步 |
| P1-4 指代 | 「第 2 章 1.5 节」→「第 2 章沿用的版本基线…（本章 1.5 节）」 |
| P1-5 跨章重复 | 平台表述压缩并指向第 2 章 2.6 节 |
| P1-6 表 1-3/小结 | 加「规划性路线图」注记，小结措辞弱化为承诺 |
| P2 | 「下滑参照」→「下载参照」；图 1-3 路径表述统一 |
