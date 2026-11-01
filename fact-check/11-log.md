# 第 11 章 核查日志（fact-check）

| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| GROMACS 通过多级并行从笔记本扩展到超算 | B：Abraham 2015 SoftwareX [1] | 原始文献 | 已核实 |
| 版本相关行为以 2026.4 官方文档为准 | A：GROMACS 2026.4 文档 [2] | 官方文档 | 已核实 |
| Verlet 1967 无速度差分格式、辛积分器 | B：Verlet 1967 [3] | 原始文献 | 已核实（DOI 10.1103/PhysRev.159.98） |
| leap-frog 为默认积分器、velocity Verlet 适用场景 | A：GROMACS 2026.4 MD 手册 [4] | 官方文档 | 已核实 |
| SHAKE 拉格朗日乘子迭代、LINCS 幂级数展开两步 | B：Ryckaert 1977 [5]；Hess 1997 [6] | 原始文献 | 已核实（[6] DOI 已补） |
| LINCS 仅限键约束与孤立角约束、四阶展开 | A：GROMACS 2026.4 Constraint algorithms [7] | 官方文档 | 已核实 |
| SETTLE 水的刚体解析求解 | A：GROMACS 2026.4 Constraint algorithms [7] | 官方文档 | 已核实 |
| P-LINCS 域分解下跨单元约束 | B：Hess 2008 [8] | 原始文献 | 已核实 |
| PME B 样条 + 3D-FFT、N log N 复杂度 | B：Essmann 1995 [9] | 原始文献（JCP 103(19):8577-8593） | 已核实 |
| 静电精度经验配置与缩放关系 | A：GROMACS 2026.4 Long Range Electrostatics [10] | 官方文档 | 已核实 |
| 域分解第八壳法、更新组、DD 约束 | A：GROMACS 2026.4 Parallelization [11] | 官方文档 | 已核实 |
| thread-MPI 无需配置、MPI 3.0、GPU 后端要求 | A：GROMACS 2026.4 安装指南 [12] | 官方文档 | 已核实 |
| gmxapi 依赖 mpi4py、与 MPI 构建一致 | A：gmxapi usage [13] | 官方文档 | 已核实 |
| 异构并行自 2016、GPU 卸载模型 | B：Páll 2020 [14] | 原始文献 | 已核实 |
| gmxapi 设计目标、系综/插件/计算图 | B：Irrgang 2022 [15] | 原始文献 | 已核实 |
| gmxapi 限制条目、版本 0.5.0a1 | A：gmxapi module reference [16] | 官方文档 | 已核实 |
| Public C++ API、模板起点 | A：GROMACS C++ API [17] | 官方文档 | 已核实 |
| TrajectoryAnalysisModule 回调、analyzeFrame | A：Doxygen Using GROMACS as library [18] | 官方文档 | 已核实（修订轮：analyze→analyzeFrame） |
| MDAnalysis 原始论文、SciPy 2016 补充 | B：Michaud-Agrawal 2011 [19]；Gowers 2016 [20] | 原始文献 | 已核实 |
| MDAnalysis 单位约定（Å） | C：MDAnalysis User Guide [21] | 官方文档 | 已核实 |
| MDTraj 整体载入内存、数组接口 | B：McGibbon 2015 [22]；MDTraj 文档 [23] | 原始文献+文档 | 已核实 |
| PyEMMA 流程、tICA/MSM | B：Scherer 2015 [24]；PyEMMA 文档 [25] | 原始文献+文档 | 已核实（P2：URL 改 pyemma.org，统稿处理） |
| deeptime 统一 API、深度方法 | B：Hoffmann 2022 [27]；deeptime 文档 [26] | 原始文献+文档 | 已核实 |
| PLUMED 插件库、GROMACS 集成 | B：Tribello 2014 [28]；PLUMED 文档 [29]；A：Using PLUMED [30] | 原始文献+文档 | 已核实 |
| NNPot 模块、LibTorch/TorchScript、ML/MM | A：GROMACS 2026.4 NNPot [33] | 官方文档 | 已核实 |
| metatomic 引擎、conda/源码安装 | A：metatomic 文档 [34] | 官方文档 | 已核实 |
| pytest 测试框架、Python profilers | A：pytest 文档 [35]；Python profile [36] | 官方文档 | 已核实 |
| 引用编号 1-36 首现严格递增、与文献表一致 | 自检 | 朴素逐字符扫描 | 已核实（验收轮+本次复核） |

修订记录（2026-10-30）：
- [3] Verlet、[6] Hess LINCS 补 DOI（P1-1）
- analyze → analyzeFrame 回调名（旧版模板注明 analyze）（P1-2）
- 本日志补建（P1-3）
- PyEMMA URL 失效（P2-1）与 gmxapi 版本一致性（P2-3）待统稿轮处理