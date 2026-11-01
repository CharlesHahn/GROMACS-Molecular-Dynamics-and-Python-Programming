# 第 2 章 验收报告（第二轮·对抗性复核）

> 复核时间：2026-10-29。复核人：验收 agent（独立复核；anysearch 调用约 20 次，含 Crossref API 核验 4 个 DOI）。
> 复核基线：REVIEW.md（不得放宽）、STYLE.md（字数口径/结构/语言基线）、OUTLINE.md（三级节承诺）。
> 前置文件：本报告上一轮版本（2026-10-28/29）——上轮 5 条 P1 已逐条复验，见「三、上轮 P1 修复核对」。
> **结论：通过（pass=true）。本轮无 P0、无 P1；遗留 P2 共 12 条（正文 9 条 + 全书级 3 条），登记待统稿。**

## 一、实测数字表（STYLE.md 第三节口径，PowerShell 实测）

| 项目 | 要求 | 实测 | 判定 |
| --- | --- | --- | --- |
| 汉字数（去代码块 + 截断 `## 参考文献` 之后，含表格与图注） | ≥10,000 | **13,345** | 通过 |
| 正文二级节（正文 `##`） | ≥8 | **8**（全章含构件共 14） | 通过 |
| 三级节（`###`） | ≥25 | **26**（2.1.1–2.8.3 与 OUTLINE 逐条对应，零删减） | 通过 |
| 表格（表 2-1～2-7，表题在上） | ≥3 | **7** | 通过 |
| 图（图 2-1/2-2/2-3，均 Mermaid，图题在下） | ≥2 | **3** | 通过 |
| 常见错误 | ≥6 | **10**（均为「现象→成因→排查步骤→处置」） | 通过 |
| 习题 | ≥6 且含 ≥2 开放题 | **8**（第 5、6 题标注【开放题】） | 通过 |
| 参考文献 | ≥30 | **34**（[1]–[34]） | 通过 |
| 正文上标编号 | 连续、无跳号重号、与列表逐条对应 | 正文引用 1–34 **全覆盖 34/34**；首次出现序列 1,2,…,34 严格递增；文末列表与 refs/02-refs.md 逐条同文 | 通过 |
| 必备构件顺序 | 导言→学习目标→前置知识→正文→常见错误→小结→习题→参考文献 | 齐全且顺序正确 | 通过 |
| 导言字数 | 300–600 | **398** | 通过 |
| 学习目标 | 4–6 条、行为动词 | **6** 条（均为「能……」） | 通过 |
| 文件编码 | UTF-8 无 BOM、LF | 无 BOM；CRLF 0 / 纯 LF 572 行（总 573 行） | 通过 |
| 跨章重复 | 无 | 02 vs 03、02 vs 04 的 ≥25 字句子交集均为 **0** | 通过 |
| 禁用表达/第二人称/套话过渡 | 无 | 禁用词（含「让我们/接下来我们/值得注意的是/总而言之」）0；「你」0、「我们」0 | 通过 |

注：字数脚本与 STYLE.md 第三节口径一致（`[regex]::Replace('(?s)```.*?```','')` + 截断 `## 参考文献` + `[\u4e00-\u9fff]` 计数），实测 13,345。

## 二、文献抽查清单与核验结果（随机种子 20261029，编号：1,15,16,17,24,25,26,29,30,31）

| 编号 | 文献 | 核验方式 | 六项/可用性核验 | 结果 |
| --- | --- | --- | --- | --- |
| [1] | GROMACS 2026.4 Installation guide | extract 官方页 | 可开；CMake≥3.28、GCC11/Clang14/MSVC2019、icc 不再支持、CUDA≥12.1/cc≥5.0、OpenCL deprecated、SYCL（DPC++2024.0/AdaptiveCpp24.02）、HIP（ROCm≥5.2、2025 引入、2026 全卸载）全部与正文一致 | 通过 |
| [15] | Docker Hub gromacs/gromacs | search | 官方镜像仓库存在（首要命中 hub.docker.com/r/gromacs/gromacs） | 通过 |
| [16] | Apptainer Definition Files | extract | 可开；Bootstrap/From、%post/%environment/%runscript 语义与正文骨架一致 | 通过 |
| [17] | Yoo 2003 SLURM | Crossref API（10.1007/10968987_3） | 标题、作者（Yoo/Jette/Grondona）、LNCS/JSSPP、2003、页 44–60、DOI 全合 | 通过 |
| [24] | Kutzner 2015 | Crossref API（10.1002/jcc.24030） | 标题、作者（Kutzner/Páll/Fechner/Esztermann/de Groot/Grubmüller）、J. Comput. Chem.、2015、36(26):1990-2008、DOI 全合 | 通过 |
| [25] | 论坛帖 GROMACS SYCL for NVIDIA GPUs | search+片段 | 帖子真实存在（gromacs.bioexcel.eu/t/…/6441）；内容「GROMACS 2023 is known to work on NVIDIA cards via SYCL」支撑正文用法 | 通过 |
| [26] | Alekseenko 2024 CUG | Crossref API（10.1145/3725789.3725797） | 标题、CUG 2024 proceedings、2024、页 71–84、DOI 全合（上轮待补页码已齐） | 通过 |
| [29] | Dev manual: Unit testing | extract | 可开；make check→CTest 语义与正文一致 | 通过 |
| [30] | Downloads 页 | extract | 可开；含 gromacs-2026.4.tar.gz 与 regressiontests-2026.4.tar.gz 链接，佐证 2.7.2 下载方式 | 通过 |
| [31] | ftp.gromacs.org/pub/benchmarks | extract | 可开；ADH_bench_systems、villin_vsites、water、rnase 等在列 | 通过 |

**结论：抽查 10 条无一条伪造、错配或无法打开；4 个 B/C 级条目均经 Crossref API 完成六项核验。引文核查无 P0。**
（备注：[31] 目录当前未列出 d.dppc 打包文件；「d.dppc」为 GROMACS 历史经典基准体系名（2012 年起见于 UAB 等权威 wiki），正文举例属历史沿用，见 P2-3。）

## 三、上轮 P1 修复核对（5 条，逐条复验）

| 编号 | 上轮 P1 | 本轮复验 | 状态 |
| --- | --- | --- | --- |
| ① | GMX_FFT_LIBRARY 取值/默认机制与官方不符 | 表 2-4 已改「fftw / mkl / fftpack；默认依编译器与构建类型而定（通常为 fftw）」；2026.4 build-system.html 原文「Possible values: fftw, mkl, fftpack. The default selection depends on the compiler and build type」——逐字一致 | 已修✓ |
| ② | [23] 引文不含 HIP 的引文错配 | 正文已拆为「Build system 文档对 GMX_GPU 列出的可取值是 CUDA、OpenCL 与 SYCL[23]，HIP 后端则由安装指南给出支持范围与工具链要求[1]」；extract 原文同句 | 已修✓ |
| ③ | [9][26] 卷期页不全 | [9] 补 40(27): 2418-2431（Crossref 10.1002/jcc.26011 复验）；[26] 补 CUG 2024: 71-84（Crossref 10.1145/3725789.3725797 复验）；refs/02-refs.md 与正文列表同步 | 已修✓ |
| ④ | rsync 远端路径 `~/$HOME` 双重展开 | 已改 `用户名@集群:runs/task1/`，与下行下载命令一致 | 已修✓ |
| ⑤ | 「一个数量级以上」无出处倍数断言 | 已删，改带条件定性「受体系规模与硬件组合影响，通常相差显著」 | 已修✓ |

上轮 P2 顺手修正项（吞吐登计→吞吐量统计、ONEMATH→oneMath）均已体现在正文。

## 四、关键论断抽查（本轮独立复核 12 条，全部原文可见）

1. 编译器/构建前置：CMake ≥3.28；C99+C++17；最低 GCC 11 / Clang 14 / MSVC 2019；icc/icpc 不再支持、用 oneAPI clang 或 gcc——安装指南原文逐条吻合（含「minimum compiler versions supported… GNU 11, LLVM 14, Microsoft 2019」「The Intel classic compiler (icc/icpc) is no longer supported」）。
2. CUDA：Toolkit ≥12.1、compute capability ≥5.0——安装指南 CUDA 节原文「CUDA toolkit version 12.1 or newer」「GPU with compute capability 5.0 or higher」✓。
3. OpenCL：已弃用、Apple M 唯一后端——「OpenCL is deprecated, but is currently the only backend supporting Apple M-series GPUs」✓。
4. SYCL：硬件覆盖 AMD GFX9/CDNA/RDNA、Intel 全系、NVIDIA 全系；要求 oneAPI DPC++ ≥2024.0（NVIDIA/AMD 需 Codeplay 插件）或 AdaptiveCpp ≥24.02——安装指南 SYCL 节逐条 ✓（正文「NVIDIA 亦可运行 SYCL」成立；官方亦加 cv「CUDA remains the recommended choice on that platform」，见 gromacs.org/topic/heterogeneous_parallelization.html）。
5. HIP：可用硬件 GFX9/CDNA1/2/3/RDNA1/2/3；ROCm ≥5.2；2025 引入且仅主要非键核、2026 全卸载支持——安装指南 HIP 节原文逐字吻合 ✓。
6. GPU-resident：≤2.5 fs 须 constraints=h-bonds——mdrun-performance「When using a time-step of <=2.5 fs, use constraints=h-bonds」✓（不支持虚拟位点/副本交换组合与上轮 extract 一致）。
7. OpenMP 扩展 12–24（Intel）/ 6–8（AMD）——mdrun-performance「scales well for up to 12-24 threads on Intel and 6-8 threads on AMD CPUs」✓。
8. md.log 六项指标，MFlops/Mnbf/s 需 GMX_DETAILED_PERF_STATS——原文「MFlops and Mnbf/s are only printed when the environment variable GMX_DETAILED_PERF_STATS is set」✓。
9. GPU 史实：GROMACS 自 4.5（2010）支持 GPU、4.6（2013）原生支持——gromacs.org/topic/heterogeneous_parallelization.html 原文 ✓（正文「GPU 加速自 GROMACS 4.5 起引入」表述准确）。
10. 2026.0 于 2026 年 1 月发布——上轮核验（2026-01-19）[3][20] ✓，本轮 refs 列表一致。
11. 平台矩阵：官方支持任意 Linux/macOS/Windows 与 x86-64、POWER、ARM、RISC-V——与安装指南平台节一致 ✓。
12. thread-MPI/外部 MPI 语义（-DGMX_MPI=on→gmx_mpi、MPI 3.0、单节点 thread-MPI 更快）——与 build-system/安装指南一致 ✓。

## 五、逐节问题清单（本轮全部为 P2；无 P0/P1）

| 级别 | 位置 | 问题（原文摘录） | 修改建议 |
| --- | --- | --- | --- |
| P2 | 图 2-3（正文 L371） | Mermaid 节点文本「G[SYCLL AdaptiveCpp 或 HIP/ROCm]」——“SYCLL”多一个 L | 改「SYCL」。顺带检查流程图分支：`B{NVIDIA?}` 后挂 `B -->|Apple M| I` 与“NVIDIA 是/否”出口语义不严，建议改为 `A --> B{NVIDIA?}`…`B -->|否| D{Intel/AMD/Apple?}` 三段式（Apple M→OpenCL） |
| P2 | 表 2-4（L342） | `GMX_GPU_FFT_LIBRARY` 行写作「VKFFT」，官方命名为 VkFFT（install-guide「Using VkFFT」节） | 大小写改 VkFFT |
| P2 | 2.6.3（L360） | 「SYCL 亦可运行 NVIDIA GPU，但官方论坛明确提示该组合为实验性质，生产环境仍推荐 CUDA[25]」——2026.4 安装指南已将 NVIDIA 列入 SYCL 支持硬件（NVIDIA GPUs: All GPUs），“实验性质”措辞与现指南有张力 | 改为「SYCL 后端可用于 NVIDIA GPU（安装指南列入支持硬件），但官方在 NVIDIA 平台仍推荐 CUDA[1]；早期论坛亦显示该组合曾受限制[25]」，并可加引 gromacs.org/topic/heterogeneous_parallelization.html |
| P2 | 2.1.3（L80） | 「超出显存时 GPU 卸载会自动回退或无法启用[2]」——官方 auto 语义为 GPU 不可用时回退 CPU；“超出显存”通常直接报错 | 收紧为「GPU 不可用（含显存不足）时，auto 模式回退 CPU 或无法启用」 |
| P2 | 2.7.3（L435） | 「官方基准输入（ADH、d.dppc、villin 等标准体系），可从官网基准目录下载[31]」——[31] 目录当前未见 dppc 打包；d.dppc 为历史经典基准名 | 核对现目录后改为「（ADH、villin、water 等）」，或注明 d.dppc 为历史体系、以 ftp 目录为准 |
| P2 | 2.6.1（L310） | 「个别 Linux 发行版（如 Fedora）的官方仓库已打包 GROMACS 2026.4」未核实 | 核实发行版仓库实际版本；无法核实则删「2026.4」改「近年版本（以发行版仓库为准）」 |
| P2 | 表 2-4（L334） | GMX_BUILD_OWN_FFTW 行「新手推荐 ON」教程化用词（STYLE 一.2） | 改「首次编译推荐 ON」 |
| P2 | 2.4.4（L183） | 「2021 年该项目移交 Linux 基金会后更名为 Apptainer」——改名事实成立，但细节无直接 A 级出处（[13][14] 仅支撑 formerly Singularity） | 补 Apptainer 官方公告/news 类来源，或降级为「Apptainer（原 Singularity，2021 年起独立维护）」 |
| P2 | 2.4.3（L170） | 「mamba 以 C++ 重写依赖解析……显著快于 conda」为一般知识、无引用 | 标注「据 mamba 官方项目说明」或删「显著」 |
| P2 | 2.7.2（L431） | 「官方开发文档还描述了物理校验（physical validation）测试[29]」——[29]（testutils 页）自述「regression tests are not discussed further on this page」，未含 physical validation 内容，引文定位偏 | 改引回归测试说明文档（如 manual.gromacs.org documentation 中 Regression tests 章节），或删除该句 |
| P2 | 2.5.2（L266） | 多节点脚本 `srun gmx_mpi mdrun …` 未显式给出任务数，依赖 sbatch 分配继承 | 显式化 `srun -n 64 gmx_mpi mdrun …`（或说明 srun 继承 --ntasks-per-node），提高可复现性 |
| P2 | 全书级（备注） | glossary.md、figures/TODO-figures.md 尚不存在（本章 3 图全为 Mermaid，无需占位登记，符合 STYLE 七）；_sidebar.md 仍为旧 8 章提纲 | 全书性事务，统稿时按 OUTLINE 重写侧边栏、建立 glossary |

## 六、结论与返工范围

- **无 P0**：抽查 10 条文献全部真实、可开（4 条 B 级经 Crossref API 六项核验）；字数 13,345、二级节 8、三级节 26、表格 7、图 3、常见错误 10、习题 8（开放 2）、参考文献 34、编号连续且全覆盖、必备构件齐全、编码合规、跨章零重复、禁用表达与第二人称零命中。
- **无 P1**：上轮 5 条 P1 全部复验已修；本轮未发现 P1。
- **P2 共 12 条**：正文 9 条（图 2-3「SYCLL」拼写、VkFFT 大小写、SYCL-NVIDIA 措辞、显存回退措辞、d.dppc 举例、Fedora 打包未核、新手推荐、Apptainer 细节出处、mamba 无引用、physical validation 引文定位、srun 显式任务数——其中若干条可在统稿时一句话处理）+ 全书级 3 条。
- **返工范围**：正文无需结构性返工；建议在最终统稿轮按第五节清单一次性修订（多为措辞级修改），完成后再做一次终验即可。本轮判 **pass=true**。