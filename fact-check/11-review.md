# 第 11 章《Python 生态与扩展开发》首次验收报告（第 1 轮）

- 验收日期：2026-10-30
- 验收轮次：首次验收（第 1 轮）
- 验收对象：`11-Python生态与扩展开发.md`（485 行，61,495 字节）、`refs/11-refs.md`
- 依据：`REVIEW.md`（未放宽任何条款）、`STYLE.md`
- 结论：**通过（无 P0；P1=3，P2=6，修订后进入下一环节）**

> 备注：必读清单中的 `fact-check/11-log.md` 不存在（见 P1-3）。本报告已按 REVIEW 第五节要求补足实测数字、抽查清单与逐节问题。

## 一、实测数字表

| 指标 | 标准 | 实测 | 判定 |
| --- | --- | --- | --- |
| 汉字数（STYLE 第三节口径：除代码块、除「## 参考文献」之后） | ≥10,000 | **11,841** | 达标 |
| `##` 二级节 | ≥8 | 13（学习目标、前置知识、11.1–11.7、常见错误、本章小结、习题、参考文献） | 达标 |
| `###` 三级节 | ≥25 | 26（11.1×3、11.2×4、11.3×3、11.4×3、11.5×6、11.6×4、11.7×3） | 达标 |
| 表格 | ≥3 | 5（表 11-1 至 11-5） | 达标 |
| 图 | ≥2 | 3（图 11-1/11-2/11-3，均为 Mermaid，非占位） | 达标 |
| 常见错误 | ≥6 | 7（错误 1–7，均含现象/成因/排查/处置） | 达标 |
| 习题 | ≥6（含 2 开放题） | 7（第 6、7 题为开放题） | 达标 |
| 参考文献 | ≥30 | 36，正文编号 1–36 首现严格递增、无跳号无重号，与文末列表及 refs/11-refs.md 逐条一致 | 达标 |
| 导言 | 300–600 字 | 380 字 | 达标 |
| 学习目标 | 4–6 条、行为动词可检验 | 6 条，均以「能……」，无「了解/熟悉/掌握」 | 达标 |
| 构件顺序 | 导言→学习目标→前置知识→正文→常见错误→小结→习题→参考文献 | 与标准一致 | 达标 |

### 引用编号核验方法

对 `## 参考文献` 之前的正文做**朴素逐字符扫描**（遇 `[` 读数字组至 `]`，按字符位置记录每个编号的首次出现，多编号引用如 [19,20,21] 全部计入；另排除代码块后复核一次）：

- 首现顺序：`1,2,3,…,36`，严格递增，无跳号、无重号（两轮扫描均一致）。
- 1–36 全部出现，无超出 36 的编号；代码块内 `lags=[1, 2, 5, 10]` 等干扰不改变结果。
- 文末列表 36 条与 `refs/11-refs.md` 36 条逐行 diff 完全一致。
- 任务指定映射核对：MDAnalysis [19]=Michaud–Agrawal 2011 原始论文、[20]=Gowers SciPy 2016、[21]=User Guide ✓；deeptime [26]=官方文档、[27]=Hoffmann 论文 ✓；PLUMED [28]=论文、[29]=文档、[30]=GROMACS Using PLUMED ✓。

## 二、抽查文献清单与核验结果（2026-10-30 核验）

随机抽 8 条（种子 20261030）：4、7、9、12、15、23、25、28。通道：CrossRef REST（api.crossref.org）、官方直连（web_fetch）、anysearch extract。

| 编号 | 文献 | 通道 | 六项核验 | 结果 |
| --- | --- | --- | --- | --- |
| 4 | GROMACS 2026.4 MD 手册页 | web_fetch 官方直连 | 页面存在；leap-frog 为默认积分器（正文断言吻合） | 通过 |
| 7 | GROMACS 2026.4 Constraint algorithms | web_fetch 官方直连 | LINCS 默认、非迭代两步、比 SHAKE 快且稳、仅限键约束与孤立角约束、四阶展开、warnangle、SETTLE、P-LINCS——正文逐条吻合 | 通过 |
| 9 | Essmann 1995 PME | CrossRef REST | J Chem Phys 103(19):8577–8593，DOI 10.1063/1.470117 | 通过 |
| 12 | GROMACS 2026.4 安装指南 | anysearch extract | thread-MPI 无需配置、MPI 3.0、CUDA≥12.1 & CC≥5.0、SYCL/OpenCL（M 系列唯一、弃用）/HIP（自 2025）、单一后端、CUDA-aware MPI（OpenMPI≥4.1.0、UCX≥1.10、GMX_FORCE_GPU_AWARE_MPI=1）、NVSHMEM 实验特性≤30 万粒子——正文全部吻合 | 通过 |
| 15 | Irrgang 2022 gmxapi | PLOS 官方页 | PLoS Comput Biol 18(2):e1009835，DOI 10.1371/journal.pcbi.1009835；自 2019 起官方支持、默认启用、插件/系综/可组合/计算图/pybind11——正文吻合 | 通过 |
| 23 | MDTraj 文档 | anysearch extract | mdtraj.org 可达；格式清单、计算函数、LGPL——与正文表述一致 | 通过 |
| 25 | PyEMMA 文档（https://emma-project.org/） | web_fetch×2 + anysearch extract | **URL 无法打开**；PyEMMA 官方 GitHub 仓库（未维护声明）指向 docs 为 pyemma.org。判定：文献真实存在但引用的 URL 失效/陈旧，非伪造（P2-1） | 有保留通过 |
| 28 | Tribello 2014 PLUMED 2 | CrossRef REST | Comput Phys Commun 185(2):604–613，DOI 10.1016/j.cpc.2013.09.018 | 通过 |

补充核验（超出随机样本、用于关键论断）：[8] Hess P-LINCS（JCTC 4(1):116–122, DOI 10.1021/ct700200b）、[10] GROMACS PME 页（0.9/0.12/4/1e-5 配置与 5×10⁻³ 精度逐字吻合）、[11] 并行化页（第五/八壳、update group、-rdd 初值+10%、-rcon 键长估计、DLB 2% 阈值、-dds 0.8、2016.1 起自动停用、PP:PME 3:1/2:1、PME 负载 25–33%、4 倍秩→16 倍通信）、[13] gmxapi usage 页（exceptions.Error、错误不可恢复、mpi_bindings、mpiexec -m mpi4py、子通信子划分、Issue 3718、filtered_mpi_environ、commandline_operation）、[14] Páll 2020（JCP 153(13):134110, DOI 10.1063/5.0018516）、[19] Michaud–Agrawal 2011（DOI 10.1002/jcc.21787）、[20] Gowers SciPy 2016（DOI 10.25080/Majora-629e541a-00e）、[22] MDTraj（DOI 10.1016/j.bpj.2015.08.015）、[24] PyEMMA 2（DOI 10.1021/acs.jctc.5b00743）、[27] deeptime 更正条目（MLST 3(1):015009, DOI 10.1088/2632-2153/ac3de0；原「J Chem Phys 157」错配确已作废）、[30] PLUMED 页（`-plumed`、PLUMED_KERNEL、纯文本输入、三条限制逐字吻合）、[33] NNPot 页（描述符/反传梯度/TorchScript/无默认输入/GMX_NN_DEVICE/混合 NNP-MM/link atom 2FD/grompp 自动改拓扑逐条吻合）、[34] metatomic 页（fork、conda 包名与变体、GMX_METATOMIC=AUTO、mdp 选项；连「mdp 选项清单与示例文件键名不一致（metatomic-model vs metatomic-modelfile）」这一细节都与正文描述一致）、[17]/[18] C++ API（模板位于 share/gromacs/template 与 share/template、FindGROMACS/gromacs-config/gmxfftw 已知问题、pkg-config 不可重定位、4.5/4.6 selection-engine 模板迁移、顶层便捷头稳定性）。全部通过。

第 8 章交叉核对（TI/FEP/BAR/MBAR/WHAM/soft-core、gmx bar/wham、元动力学/OPES/PLUMED，表 8-3/8-4）：公式与算法归属（Kirkwood、Zwanzig、Bennett、Kumar、Beutler soft-core）正确，参数表与 GROMACS 2026.4 相符；11.5.4 对 8.6 的引用（「第 8 章的元动力学与 OPES 全部沿用这些约束」）与 8.6.1 的三条限制文字一致，属正常交叉引用而非重复。

## 三、逐节问题清单

### P1（修订后方可进入下一环节）

- **P1-1（文献著录）**：`[3]` Verlet 1967 与 `[6]` Hess LINCS 1997 两条缺 DOI，违反 STYLE 五.5「须含 DOI，缺一不可」。
  - 摘录：[3]「Verlet L. Computer "experiments"... Phys Rev, 1967, 159(1): 98-103.」；[6]「Hess B, Bekker H, Berendsen H J C, et al. LINCS... J Comput Chem, 1997, 18(12): 1463-1472.」
  - 修改：补 DOI —— [3] 10.1103/PhysRev.159.98；[6] 10.1002/(SICI)1096-987X(199712)18:12<1463::AID-JCC4>3.0.CO;2-H。正文与 refs/11-refs.md 同步。
- **P1-2（方法名与所引 2026.4 API 不符，11.4.1）**：
  - 摘录：「工具实现 initOptions、initAnalysis、analyze 与 finishAnalysis 四个回调[18]」
  - 2026.4 分析模板文档与 doxygen 中逐帧回调名为 **analyzeFrame()**（`gmx::TrajectoryAnalysisModule::analyzeFrame`），旧版（4.5/4.6 时代模板）才叫 analyze。读者按 2026.4 书写自定义工具会找不到回调。
  - 修改：改为「initOptions、initAnalysis、analyzeFrame 与 finishAnalysis 四个回调（旧版模板中该回调名为 analyze）」。
- **P1-3（过程/交付缺口）**：`fact-check/11-log.md` 不存在。STYLE 八要求每章同步维护核查日志且无「待核实」项，本报告无法对照。修改：按 STYLE 八补建 11-log.md，回填本报告核验过的关键论断（可引用本报告第二节清单），并逐条给状态。

### P2（记录，统稿时处理）

- **P2-1（文献 URL 失效，[25]）**：https://emma-project.org/ 无法访问（两次 web_fetch 与 anysearch extract 均失败）；PyEMMA 官方 GitHub 仓库标注「no longer actively maintained」并指向 pyemma.org。修改：URL 改 https://pyemma.org/（或另引用 RTD 存档），并在正文 11.5.3 顺带标注 PyEMMA 维护状态（与 deeptime 的选型判断相关）。
- **P2-2（API 名称，11.4.1）**：「命令行列别由 gmx::Options 与 runCommandLineModule 管理」——2026.4 文档对分析工具推荐 `gmx::TrajectoryAnalysisCommandLineRunner`。建议核对后改述。
- **P2-3（gmxapi 版本与 Issue 编号，11.3.2/11.3.3）**：正文两处版本不一致：「gmxapi 0.5.x（GROMACS 2026.4 手册对应版本）」vs「本章写作时手册对应的 gmxapi 版本为 0.5.0a1[16]」；「官方 Issue 4334」未在已核验的 gmxapi 页面中见到（usage 页可见 Issue 3718 与 4421）。修改：统一版本表述并注明核对日期；核对 Issue 4334 的真实编号与链接，无法核对则删去编号改述「同一前缀下同时只支持一个 gmxapi 版本」。
- **P2-4（表述歧义，11.1.2）**：「lincs-order 是矩阵展开阶数，MD 计算用四阶即可达到每约束相对偏差小于 0.0001」——手册把「MD 用四阶展开」与「单步修正后相对偏差 <0.0001」分两句陈述，现文把二者接成因果关系。修改：「MD 使用四阶展开；单步修正后每约束相对偏差小于 0.0001」。
- **P2-5（全书层面文件缺失）**：`figures/TODO-figures.md` 不存在（STYLE 七目录项）。本章 3 图均为 Mermaid，不需占位登记，不构成本章问题；建议全书统稿时补齐该文件。
- **P2-6（版本注释无核对日期）**：正文多处版本号（MDAnalysis 2.x、MDTraj 1.9.x、PyEMMA 2.5.x、deeptime 0.4.x、gmxapi 0.5.x）仅标「示意」，未注核对日期。修改：在相应代码块注释或表注中补「版本号核对日期 2026-10-29」，与 refs 的访问日期口径一致。

### 无问题项（已核）

- 方法学论断（Verlet/SHAKE/LINCS/SETTLE/PME/P-LINCS/DLB/MPMD/NVSHMEM/gmxapi/MDAnalysis/MDTraj/PyEMMA/deeptime/PLUMED/NNPot/metatomic）与原始文献或官方文档逐条对应，未见伪造或错配。
- 版本差异类陈述（2016 异构并行、2016.1 DLB 自动停用、2025 HIP、gmxapi 自 2019 官方支持）均与官方来源一致。
- 无禁用表达、无「让我们/接下来我们」、无机械「首先/其次/最后」段首、无第二人称「你」（0 次）、无占位符/TODO 残留。
- 无出处定量断言抽查：关键数值（10 fs/2 fs/1 fs、0.0001、5×10⁻³、2%、0.8、3:1/2:1、25–33%、16 倍、30 万粒子）均已逐条回查到文档原文或标注「文档推定/示意」。
- 跨章重复：以 24 字汉字指纹对 01–10 章正文全量比对，重复句数 = 0；与 8.6 PLUMED 内容为交叉引用，非抄袭。

## 四、结论与返工范围

- **判定：通过（本轮无 P0）。** 字数（11,841）、结构、文献编号与对应关系、抽查文献、方法学论断、语言规范、跨章重复七类硬性条款全部满足；P1=3、P2=6。
- 返工范围（修订后进入下一环节）：
  1. P1-1 补 [3]/[6] DOI（正文与 refs 同步）；
  2. P1-2 改 analyze → analyzeFrame（注明旧名）；
  3. P1-3 补建 `fact-check/11-log.md` 并回填本报告核验结果；
  4. P2 项按上述建议在统稿阶段处理，其中 P2-1（PyEMMA URL）建议本轮一并修改。