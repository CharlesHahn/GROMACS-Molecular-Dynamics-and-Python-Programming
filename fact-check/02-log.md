# 第 2 章 核查日志（fact-check）

> 每条记录一行关键论断。状态三档：已核实（原文可见，含检索结果原文/官方文档正文）、文档推定（官方文档明示但未在本机实测，正文须标注）、待核实（不得进入终稿）。本章无「待核实」条目。

| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| GROMACS 2026.4 为当前版本，2026-10-02 发布；2026.0 于 2026-01 发布 | A：GROMACS 官网 news 页；manual.gromacs.org 2026.4 release notes | 检索结果多条交叉（官网、2026.4 release notes 页） | 已核实 |
| CMake ≥3.28；C99/C++17；最低编译器 GCC 11 / Clang 14 / MSVC 2019；icc 不再支持 | A：GROMACS 2026.4 Installation Guide，Prerequisites/Compiler 节 | extract 官方安装指南原文 | 已核实 |
| GMX_GPU 可取值 CUDA/OpenCL/SYCL/HIP，一次构建只能配置一个 | A：GROMACS 2026.4 Installation Guide，GPU support/Important Notes 节 | extract 原文 | 已核实 |
| CUDA 后端要求 Toolkit ≥12.1、compute capability ≥5.0；CMAKE_CUDA_ARCHITECTURES 控制目标架构 | A：安装指南，CUDA 节 | extract 原文 | 已核实 |
| OpenCL 已标记过时（deprecated），当前为 Apple M 系列唯一后端；SYCL 取代 OpenCL | A：安装指南；mdrun-performance 术语表 | extract 原文 | 已核实 |
| SYCL 推荐用于 Intel GPU（oneAPI DPC++ ≥2024.0）与 AMD GPU（AdaptiveCpp ≥24.02 + ROCm） | A：安装指南，SYCL 节 | extract 原文 | 已核实 |
| HIP 后端 GROMACS 2025 引入（仅主要非键核），2026 起全卸载支持（ROCm ≥5.2） | A：安装指南，HIP 节；2026.0 Highlights | extract 原文 | 已核实 |
| thread-MPI 为 GROMACS 内置，默认启用（GMX_THREAD_MPI）；单节点内快于真实外部 MPI | A：mdrun-performance 指南；安装指南 | extract 原文 | 已核实 |
| 跨节点必须外部 MPI：-DGMX_MPI=on 构建 gmx_mpi；MPI 3.0 及以上（OpenMPI/MPICH） | A：安装指南，MPI support 节 | extract 原文 | 已核实 |
| thread-MPI 与 MPI 及多模拟（-multidir、副本交换）不兼容 | A：mdrun-performance 指南，thread-MPI 节 | extract 原文 | 已核实 |
| -ntmpi 默认：每 GPU 一个 rank，否则每核一个；多 GPU 推荐每 GPU 1–3 rank，GPU-resident 1 rank/GPU 最优 | A：mdrun-performance 指南 | extract 原文 | 已核实 |
| -npme 默认在总线程 ≥12 时自动分配约 1/4 的 rank 做 PME | A：mdrun-performance 指南，-npme 说明 | extract 原文 | 已核实 |
| GPU-resident 模式（-update gpu 等）要求 constraints=h-bonds，且不支持虚拟位点、副本交换等组合 | A：mdrun-performance 指南，-update 说明 | extract 原文 | 已核实 |
| 默认混合精度；GMX_DOUBLE=on 更慢且 GPU 卸载不兼容（官方称「slower, not normally useful」） | A：安装指南与参考手册 Definitions/Units；GROMACS 论坛帖 | extract + 论坛检索 | 已核实 |
| OpenMP 可有效扩展约 12–24 线程（Intel）、6–8 线程（AMD） | A：mdrun-performance 指南 | extract 原文 | 已核实 |
| md.log 六项性能指标；Mnbf/s 与 MFlops 需 GMX_DETAILED_PERF_STATS | A：mdrun-performance 指南，checking performance 节 | extract 原文 | 已核实 |
| FFTW 推荐自建（GMX_BUILD_OWN_FFTW=ON）；混合精度对应单精度 FFTW；MKL 未必更快 | A：安装指南，FFT 支持节 | extract 原文 | 已核实 |
| SIMD 默认按编译机探测；集群交叉编译须显式 -DGMX_SIMD；AVX2 多用于 GPU/高并行 MPI 场景 | A：安装指南 SIMD 节；mdrun-performance 指南 | extract 原文 | 已核实 |
| CUDA-aware MPI：OpenMPI ≥4.1.0 + UCX ≥1.10；GMX_FORCE_GPU_AWARE_MPI=1 可强制启用 | A：安装指南，GPU-aware MPI 节 | extract 原文 | 已核实 |
| 2026.0 新特性：AMBER14SB/AMBER19SB 移植（含 OPC/OPC3 水模型）、NNP 扩展（link atom 等）、H5MD 实验输出、HIP 完整支持 | A：GROMACS 2026.0 Release notes Highlights | extract 原文 | 已核实 |
| Slurm 概念（partition/node/job/job step/QoS）与 sbatch/srun/squeue/sacct/scancel 语义 | A：SchedMD slurm.schedmd.com/quickstart.html、overview.html、sacct.html | 官方文档检索结果交叉 | 已核实 |
| GPU 经 Slurm 的 --gres（Generic RESources）申请 | A：SchedMD slurm.schedmd.com/gres.html | 官方文档检索结果 | 已核实 |
| Apptainer 为 Singularity 更名后的项目（2021 移交 Linux 基金会）；SIF 单文件镜像；build/exec/run/pull 用法与定义文件语法 | A：Apptainer 官方用户手册 quick_start.html、definition_files.html | extract 原文 | 已核实 |
| conda-forge 提供 gromacs 预编译包（conda install conda-forge::gromacs） | A：anaconda.org/conda-forge/gromacs | 检索结果（包页） | 已核实 |
| conda 版 GROMACS 构建期 SIMD 档位固定（官方论坛实例：2025.4 编译为 AVX2_256） | A：GROMACS 官方论坛帖 13162 | 检索结果原文可见 | 已核实 |
| conda/发行版包的构建参数不可定制、性能非最优——由此推荐的「生产用源码编译」结论 | 文档推定（A 级包页 + 论坛实例 + 官方安装指南构建指南） | 依据多重文档推理 | 文档推定（正文已注明建议性质） |
| Abraham 2015 元数据：SoftwareX, 2015, 1-2: 19-25, DOI 10.1016/j.softx.2015.06.001；断言「多级并行设计」 | B：SoftwareX（ScienceDirect/ADS/OSTI 多源） | 检索结果多源交叉（卷期页 1-2:19-25 多源一致） | 已核实 |
| Páll 2020 元数据：J. Chem. Phys., 2020, 153(13): 134110, DOI 10.1063/5.0018516；断言「GPU 卸载与 CPU 计算异步重叠」 | B：JCP 2020；DOI 经 GROMACS 官网引用页确认 | 检索结果（pubs.aip.org、gromacs.org/topic/heterogeneous_parallelization.html） | 已核实 |
| Kutzner 2015 元数据：J. Comput. Chem., 2015, 36(26): 1990-2008, DOI 10.1002/jcc.24030；断言「硬件组合对单位模拟成本影响达数倍」 | B：JCC 2015；mpinat 出版物页给出卷期页 | 检索结果（onlinelibrary.wiley.com + mpinat 页） | 已核实 |
| Kutzner 2019 元数据：More bang for your buck…J. Comput. Chem., 2019, 40(27): 2418-2431, DOI 10.1002/jcc.26011 | B：JCC 2019 | Crossref API 解析（DOI 10.1002/jcc.26011：卷 40 期 27 页 2418-2431），与验收复核的 MPI-NAT 页一致 | 已核实 |
| Yoo 2003 元数据：JSSPP 2003, LNCS 2862, 44-60, DOI 10.1007/10968987_3 | B：Springer/SCIRP 检索结果 | 检索结果（Springer 章节页 + SCIRP 引用页卷期页一致） | 已核实 |
| Kurtzer 2017 元数据：PLoS ONE, 2017, DOI 10.1371/journal.pone.0177459；「Singularity 面向 HPC 容器」 | B：PLoS ONE（journals.plos.org） | 检索结果（原文页可见） | 已核实（卷期页以文章号 e0177459 计） |
| Alekseenko 2024 元数据：CUG 2024 会议版（Proceedings of the Cray User Group），pp. 71-84，DOI 10.1145/3725789.3725797；断言「SYCL 在 AMD GPU 接近厂商特定性能」 | B：ACM 会议论文集（CUG 2024） | Crossref API 解析（DOI 10.1145/3725789.3725797：proceedings-article、event CUG 2024、页 71-84），与 arXiv:2405.01420 同文 | 已核实 |
| ND NVIDIA 博客：多节点 NVIDIA GPU 扩展性改进（2023-02-09） | A：developer.nvidia.com 官方博客 | 检索结果（标题与日期） | 已核实 |
| GROMACS 官方基准输入位于 ftp.gromacs.org/pub/benchmarks；gmx nonbonded-benchmark 存在 | A：官方目录 + 2026.4 在线帮助 | 检索结果（ftp 目录、manual 在线帮助页） | 已核实 |
| Grubmüller 组基准集覆盖 6k–12M 原子 | A：mpinat.mpg.de/grubmueller/bench（Max Planck 机构页面） | 检索结果（页面自述） | 已核实 |
| 2.8 节「运行期输出落 scratch、长期数据入项目盘」等布局经验法则 | 实践共识（非官方规定） | 推理 + 站点文档惯例 | 文档推定（正文已注明「非官方规定」） |
| 资源估算三步框架与「估算值须实测修正」结论 | 文档推定（基于 mdrun 性能指南指标定义与官方基准工作流） | 依据多重文档推理 | 文档推定（正文已注明） |
| GMX_FFT_LIBRARY 可取值 fftw/mkl/fftpack，默认选择依编译器与构建类型而定（无固定默认值） | A：2026.4 dev-manual build-system.html「GMX_FFT_LIBRARY」节；install-guide「Fast Fourier Transform library」节 | extract 官方文档原文 | 已核实 |
| build-system.html 中 GMX_GPU 可取值仅 CUDA/OpenCL/SYCL（不含 HIP）；HIP 后端见安装指南 GPU 支持节 | A：2026.4 dev-manual build-system.html「GMX_GPU」节；install-guide「HIP」节 | extract 官方文档原文 | 已核实 |
| GMX_GPU_FFT_LIBRARY 的 oneMath 选项对应官方「oneMath interface library」（与 Intel oneMKL 易混淆） | A：install-guide「Using oneMath Interface Library」节 | extract 官方文档原文 | 已核实 |

注明：B 级文献条目六项信息（标题、作者、期刊/会议、年份、卷期页/页码、DOI）均自检索结果抄录并有至少两个独立来源交叉；[9] 与 [26] 的卷期页/页码已于修订轮经 Crossref API（DOI 10.1002/jcc.26011、10.1145/3725789.3725797）补齐，本章无待补元数据。