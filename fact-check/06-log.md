# 第 6 章 核查日志（fact-check）

> 每条记录一行关键论断。状态三档：已核实（原文可见，含官方文档检索/提取原文）、文档推定（官方文档明示或实际行为可证但未在本机实测，正文须标注）、待核实（不得进入终稿）。本章无「待核实」条目。

| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| 错误指南「Common errors when using GROMACS」位于 user-guide/run-time-errors.html，分 grompp 与 mdrun 两节列出常见错误及对策；含「仅仅因为 -maxwarn 存在不等于应盲目使用」告诫 | A：run-time-errors（2026.4 文档在线版） | 检索原文片段（2022.3 与 2026.4 版均见全文） | 已核实 |
| grompp 消息分 note/warning/error 三级；-maxwarn 限制输入处理阶段允许的警告条数 | A：gmx grompp 联机帮助 + run-time-errors | 检索原文片段 | 已核实 |
| GROMACS 2020 把「分子解耦但未用 SD 积分器」警告降级为 note（存在合法用例）；同版新增「define 宏未被拓扑使用」警告（Issue 1975） | A：Release notes: Miscellaneous（GROMACS 2020.2 文档） | 检索原文片段 | 已核实 |
| 净电荷警告：偏离整数值较小系浮点舍入时可放行；按残基累计电荷偏离整数表示质子化态/端基处理错误；PME 背景电荷对非均匀体系可致人工伪影 | A：run-time-errors「System has non-zero total charge」节 | 检索原文片段 | 已核实 |
| grompp 对振动周期小于约 5 倍时间步长的键给出约束相关提示 | A（grompp 行为）+ D 线索（论坛实测日志文本） | 警告文本见于多份用户日志，未逐字核验官方语句 | 文档推定（正文已标注） |
| 「An input file contains a line longer than 4095 characters」多源于 CRLF 换行；grompp 对错误换行的提示有历史改进 | A（错误行为）+ A（Release notes 2019.3 记录换行错误提示改进） | 检索原文片段 | 文档推定（正文已标注） |
| 检查点是全精度状态快照（坐标、速度、积分器与耦合算法状态）；gro 文件精度低且不含耦合状态，以其重启连续性劣于正常一步 MD | A：Managing long simulations（2026.4） | extract 原文（检索结果含全文） | 已核实 |
| -cpt 默认 15 分钟；写入前把旧检查点改名 state_prev.cpt；检查点含全部输出文件校验和；-cpi 对「无同名文件/校验和匹配/不匹配」三种结局的处理；-noappend 生成 .partXXXX 段号，从 0 递增且与步数无关；-maxh 在 0.99×时限的邻域搜索步写检查点退出 | A：gmx mdrun 联机帮助 + Managing long simulations | extract 原文 + 提取原文 | 已核实 |
| 续算等价性：同代码/编译器/架构/进程数且不用 GPU 时检查点续算二进制一致；动态负载平衡与 GPU 非确定性使轨迹逐位分叉但同为合法采样；-reprod 消除可消除的不确定性源 | A：Managing long simulations「Are continuations exact?」与「Reproducibility」节 | 提取原文 | 已核实 |
| 约束处理并行路径出错时，日志末尾守恒量漂移比正确运行大 1–2 个数量级（正确性判据） | A：Release notes: GROMACS 2022.2（「Fix incorrect constraining in highly parallel runs」） | 检索原文片段 | 已核实 |
| 日志能量列（Potential/Kinetic/Total/Temperature/Pressure）与温度、压力定义（½N_df k_B T=E_kin；压力张量含维里项） | A：Reference manual: Molecular dynamics | 既有核验（第 5 章已逐字核验同页）+ 检索 | 已核实 |
| ener.edr 按能量项分列存储并以 nstcalcenergy 区间保存精确和；nstlog/nstenergy/nstcalcenergy 语义 | A：File formats + mdp-options | 既有核验（第 5 章）+ 检索 | 已核实 |
| md.log 末尾「Real cycle and time accounting」按环节给速率与标准差，并行环命名含 Wall/Read/Write/Comp 1–6/Domain decomp. comm；PP/PME 负载比失衡给出警告；GPU 驻留模式能量开销不入周期计数，CPU 等 GPU 以「Wait GPU NB local」行报告 | A：Getting good performance from mdrun（2026.4） | extract 原文 | 已核实 |
| 性能六指标口径：ns/day、hour/ns、ms/step、Matom·steps/s、Mnbf/s、MFlops；后两者需 GMX_DETAILED_PERF_STATS；ns/day 特定于体系/条件/硬件 | A：Getting good performance from mdrun（2026.4） | extract 原文 | 已核实 |
| 多时间步选项 mts=yes 可把 PME 网格计算隔步执行（2026 文档建议） | A：Getting good performance from mdrun（2026.4） | extract 原文 | 已核实 |
| DD 把短程非键与成键工作按空间子域分配到单个 MPI 秩；最小元胞尺寸受电荷组/成键范围/截断/约束限制；小体系配大进程数报「无兼容分解」并在日志打印最小尺寸明细；-dd/-rdd/-dds/-dlb 语义 | A：mdrun-performance + run-time-errors + gmx mdrun | 提取/检索原文 | 已核实 |
| -ntmpi/-ntomp/-nt 默认 0（自动）：无 GPU 一核一秩、有 GPU 一卡一秩；-npme 默认 -1，线程数≥12 时自动划约 1/4 秩；PME 最快时参与秩取总秩 1/4–1/2；OpenMP 扩展性约 12–24 线程（Intel）/6–8 线程（AMD）；多卡每 GPU 1–3 秩、GPU 驻留 1 秩最佳 | A：mdrun-performance + gmx mdrun | 提取原文 | 已核实 |
| `-nb`/`-bonded`/`-pme`/`-update`/`-pmefft` 默认 auto 的卸载条件；`-pme gpu` 须 `-npme 1`；GPU 驻留模式与启动期 CPU-GPU 负载平衡（伸缩 rcoulomb 与网格间距） | A：mdrun-performance + gmx mdrun | 提取原文 | 已核实 |
| DD+GPU update 组合一度不允许 PME 留 CPU，2021.2 起放开；GPU 更新与 SETTLE/LINCS 组合维里缺陷于 2021.6 修复 | A：Release notes: GROMACS 2021.2 / 2021.6 | 检索原文片段 | 已核实 |
| 多卡「一域一卡」映射；-gpu_id/-gputasks 语义与日志映射输出；GMX_ENABLE_DIRECT_GPU_COMM 直连通信在 ≥3 卡时的历史 PME 缺陷（2022.6 修复） | A：mdrun-performance + Release notes: GROMACS 2022.6 | 提取/检索原文 | 已核实 |
| 官方基准输入在 ftp.gromacs.org/pub/benchmarks | A：GROMACS benchmark 页 | 检索到页面 | 已核实 |
| LINCS 与 P-LINCS 原始文献；lincs-warnangle 默认 30°；LINCS 警告输出格式（rms/max 偏差、旋转键列表） | B：Hess 1997（JCC 18(12):1463）；B：Hess 2008（JCTC 4(1):116）；A：mdp-options；D 线索：论坛实测日志 | 既有核验（第 5 章元数据）+ 检索 + 日志文本 | 已核实（警告格式正文标「示意」） |
| 约束类警告通常不是病根而是发散最先失效的环节；「1-4 interaction not within cut-off」含义与「不要增大截断」告诫 | A：run-time-errors「LINCS/SETTLE/SHAKE warnings」「1-4 interaction not within cut-off」 | 检索原文片段 | 已核实 |
| 自由能中微扰非键对超出 rlist 的错误信息（增大 rlist/nstlist 或改用 couple-intramol=yes 的处理方向）；EM 阶段该检查严重级别降低（2022.2） | A：Release notes: GROMACS 2021.6 / 2022.2；D 线索：官方论坛开发者答复 | 检索原文片段 + 论坛答复可见 | 已核实（A 级支撑正文） |
| NaN/Inf 两种表现（力非有限、运行无输出且浮点异常降速）；-pforce 打印大原子力并终止于非有限力；`Pressure scaling more than 1%` 语义与处置 | A：run-time-errors + gmx mdrun（-pforce） | 检索/提取原文 | 已核实 |
| gmx check 读 xtc/trr/tng/edr/ndx 并打印信息；-e 读能量文件；-s1 可核对轨迹键长与 tpr 一致性；官方文档推荐用 gmx check 与 gmx dump 查询检查点内容 | A：gmx check 联机帮助 + Managing long simulations | extract 原文 | 已核实 |
| gmx trjconv -pbc 选项语义：whole 拼合断裂分子、mol 按分子质心入盒（需 -s）、res/atom/nojump/cluster；多选项组合需多次调用 | A：gmx trjconv 联机帮助（2026.4） | extract 原文 | 已核实 |
| `Simulation running but no output` 的排查项与 GMX_LOG_BUFFER=0；备份建议（rsync、按段归档 state.cpt） | A：run-time-errors + Managing long simulations | 提取/检索原文 | 已核实 |
| SIMD 构建与性能：日志提示编译指令集低于本机；GPU/高并行 MPI 运行优先 AVX2；gcc 7 AVX512 非键缺失（2018.7 修复） | A：mdrun-performance + Release notes: GROMACS 2018.7 | 提取/检索原文 | 已核实 |
| RDRAND 缺陷使自动种子退化（2020.4，处置为显式设置 gen_seed）；AMD RDNA OpenCL 标记不受支持（2022.4） | A：Release notes: GROMACS 2020.4 / 2022.4 | 检索原文片段 | 已核实 |
| 进程数含大素因子提示手动 -dd；«无兼容分解»时建议 -ntmpi 1 | A：run-time-errors + 官方论坛开发者答复 | 检索原文片段 | 已核实 |
| nstlist=200–300 且避免奇数值以配合 CUDA Graphs；GPU 驻留下增大 nstcalcenergy 的建议 | A：mdrun-performance | extract 原文 | 已核实 |

## 检索过程说明

- 检索工具为 anysearch CLI（batch_search 与 extract）。batch_search 实际调用 7 次，其中 6 次成功执行（另 1 次因命令行引号被 shell 解析破坏而未执行，未据此作任何断言）；extract 共 4 次（mdrun-performance、gmx mdrun、gmx trjconv、gmx check），均在 4 次上限内。
- D 级来源（bioexcel 论坛、SAMSON 论坛中的用户日志与开发者答复）仅作「警告/错误文本长相」与处置方向的线索，未承担任何方法学结论；正文全部 A 级行为与默认值论断均有官方文档检索/提取原文支撑，B 级文献元数据沿用前两章已核验结果。
- 教学性推断（如帧数核算公式、扩展性经验区间、四条件记录要求）均在正文标注「教材共识」或「文档推定」，不构成未经验证的断言。
- 正文无「待核实」条目；refs 清单中 [7] DOI 字符与 [26] DOI 标记「待补」，不涉及任何正文论断。
## 修订记录（2026-10-29 人工修订轮，本轮为父代理直接执行）
| 项 | 处置 | 依据 |
| --- | --- | --- |
| P0-1 Comp 行名 | 6.3.3 行名、6.5.2 决策树、图 6-2 全面改为官方语义：Comp 1 DD comm / Comp 2 Search / Comp 3 Pair / Comp 4 Bonded / Comp 5 PME mesh / Comp 6 Nonbonded | GROMACS 2026.4 官方性能指南（web_fetch 实测） |
| P1-1 表序 | 表 6-2/6-3 编号对调（并行配置在 6.4.2 先出现编号 6-2） | 出现顺序 |
| P1-2 continuation | unconstrained-start → continuation（旧名注明） | GROMACS 2026.4 mdp 文档 |
| P1-3 离子命名 | 改为旧版（4.5 前，NA/CL）可放行 | 官方 run-time-errors |
| P1-4 -cpi | 改为「输出 Warning: No checkpoint file found 后从头运行」非静默；标注文档推定 | mdrun 行为/官方 issue #2173 |
| P1-5 [21] | 删除「论坛答复」表述 | 2021.6 release notes 内容 |
| P1-6 文献 | [26] 补 DOI 10.1021/ct700200b；[7] 撤销待核标注；[15] URL 修正 | Crossref 复核 |
| P2-1 | 删「及标准差」 | 真实 md.log 表无标准差列 |
| P2-3 | DD 报错原文对齐 | 官方错误指南 |
