# 附录 A　mdp 参数速查

第 5 章（5.8 节）、第 6 章（6.3 节、6.6 节）与第 8 章（8.2 节、8.3 节、8.6 节）在正文中反复涉及 mdp 输入参数。本附录把这些选项按功能分组列出，给出取值示例、默认值与一句话含义，并标注该书正文的对应章节，供搭建输入文件与排查报错时快速检索。mdp 文件由 grompp 读取并嵌入 tpr，选项以「选项名 = 数值」的键值对书写，注释以分号开头，一行一项，空行与注释行不参与解析。

全部默认值以 GROMACS 2026.4 官方用户指南的「分子动力学参数（.mdp options）」页为唯一依据，随版本变化的默认行为在相应分组给出说明。官方文档的约定是：默认值写在圆括号内，或以选项取值列表的首项为默认；单位写在方括号内；选项名中的连字符与下划线等价（例如 nstlist 与 nst_list 视为同一选项）。本附录的数值均引自官方文档，未在本机实测，来源统一标注为「[官方文档]」；正文中凡出现「文档注明」字样，表示该断言依据官方文档原文表述，而非实测结论。

grompp 在预处理阶段检查选项合法性，无法识别的选项报错，已知但不接受的取值组合给出警告；部分选项的默认行为随版本调整，例如 GROMACS 2023 起提高了 nstpcouple 的默认值，GROMACS 2025.4 起强制 C-rescale 每耦合周期不少于 25 步、Parrinello-Rahman 每耦合周期不少于 200 步（版本与运行条件的记录规范见 9.6 节）。因此在跨版本复用 mdp 文件时，应核对 grompp 预处理后写入日志的实际采用值，而不以旧版本文档的默认值直接推断。

## 通用与预处理

表 A-1　通用与预处理选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| include | `include = -I/opt/gromacs-ff` | 无 | 传递给预处理器的包含目录，用于解析拓扑中的 include 指令 | 6.1 节 |
| define | `define = -DPOSRES` | 无 | 传给预处理器的宏定义；`-DPOSRES` 触发引入 posre.itp 位置限制文件，`-DFLEXIBLE` 引入柔性水 | 6.1 节、10.2 节 |
| pbc | `pbc = xyz` | xyz（列表首项） | 周期性边界条件：xyz 为三维周期，xy 仅面内周期（配合墙壁），no 关闭 | 4.6.1 节 |
| periodic-molecules | `periodic-molecules = yes` | no | 分子经周期边界与自身镜像成键时设为 yes，启用较慢的 PBC 算法，输出不再拼合分子 | 4.6.1 节 |
| comm-mode | `comm-mode = Linear` | Linear（列表首项） | 质心运动移除方式：Linear 只移除平动，Angular 同时移除平动与转动，None 不移除 | 5.4.3 节 |
| nstcomm | `nstcomm = 100` | 100（步） | 质心运动移除的执行间隔 | 5.4.3 节 |
| comm-grps | `comm-grps = System` | 全体体系 | 参与质心运动移除的组；移除条件按该组统计 | 5.4.3 节 |
| gen-vel | `gen-vel = yes` | no | 由 grompp 按麦克斯韦分布生成初速度；仅对 integrator=md 有意义 | 5.4.1 节 |
| gen-temp | `gen-temp = 310` | 300（K） | 生成初速所用的温度 | 5.4.1 节 |
| gen-seed | `gen-seed = 12345` | -1（grompp 自动取伪随机种子） | 初速随机数种子；取 -1 时自动生成，多副本复现应显式给定 | 5.4.2 节 |
| continuation | `continuation = yes` | no | 精确续算或 rerun 时设为 yes，不再对起始构型施加约束、不重置壳层 | 6.2.3 节 |
| morse | `morse = yes` | no | 键势改用 Morse 势，默认键势为谐振势 | — |

## 积分器与时间步长

表 A-2　积分器与时间步长选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| integrator | `integrator = md` | md（列表首项） | 运动积分算法。常见取值：md（leap-frog）、md-vv、md-vv-avek、sd（朗之万随机动力学）、bd（布朗动力学）、steep、cg、l-bfgs（能量最小化）、nm（简正模分析，需双精度编译）、tpi、tpic（测试粒子插入）、mimic（MiMiC QM/MM） | 5.2 节、5.8.1 节、11.1.1 节 |
| tinit | `tinit = 0` | 0（ps） | 模拟起始时间 | 6.2.3 节 |
| dt | `dt = 0.002` | 0.001（ps） | 积分时间步长；常规全原子体系取 0.002，配质量重分配与氢键约束时可尝试 0.004 | 5.8.1 节 |
| nsteps | `nsteps = -1` | 0 | 最大积分或最小化步数；0 表示仅预处理，-1 表示不限；能量最小化必须显式设置 | 5.2 节、5.8.1 节 |
| init-step | `init-step = 0` | 0 | 起始步号；时间与自由能 λ 均以该步为起点，精确续算时由 convert-tpr 自动设置 | 6.2.3 节 |
| simulation-part | `simulation-part = 1` | 0 | 逻辑上同一模拟的分段编号，用于崩溃后文件丢失的续算场景 | 6.2.3 节 |
| mts | `mts = yes` | no（列表首项） | 多时间步长开关；目前仅支持 integrator=md | 11.1.1 节 |
| mts-levels | `mts-levels = 2` | 2 | 多时间步长层数，目前仅支持 2 层 | 11.1.1 节 |
| mts-level2-forces | `mts-level2-forces = longrange-nonbonded pair` | longrange-nonbonded | 仅在第二层（慢层）计算的力组分；PME 或 Ewald 启用时不可省略长程非键项 | 11.1.1 节 |
| mts-level2-factor | `mts-level2-factor = 4` | 2（步） | 第二层力组的计算步数间隔 | 11.1.1 节 |
| mass-repartition-factor | `mass-repartition-factor = 3` | 1 | 轻原子（通常为氢）质量重分配因子；配合 constraints=h-bonds 且取 3 时，官方文档注明通常可将步长提升至 4 fs | 5.8.1 节 |

## 能量最小化

表 A-3　能量最小化选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| emtol | `emtol = 1000` | 10.0（kJ·mol⁻¹·nm⁻¹） | 最大力收敛阈值，最大力小于该值判收敛 | 5.2.3 节 |
| emstep | `emstep = 0.01` | 0.01（nm） | 最速下降的初始步长（最大步长上限） | 5.2.3 节 |
| nstcgsteep | `nstcgsteep = 100` | 1000（步） | 共轭梯度法中插入一步最速下降的间隔 | 5.2.2 节 |
| nbfgscorr | `nbfgscorr = 50` | 10 | L-BFGS 最小化的修正步数，越大理论越准但越慢 | 5.2 节 |
| niter | `niter = 20` | 20 | 壳层位置与柔性约束每步优化的迭代上限 | — |
| fcstep | `fcstep = 0` | 0（ps²） | 柔性约束的优化步长，应取 μ/(d²V/dq²) | — |

## 输出控制

表 A-4　输出控制选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| nstxout | `nstxout = 0` | 0（步） | 向 trr 写坐标的间隔；0 表示不写 | 5.8.3 节、6.7 节 |
| nstvout | `nstvout = 0` | 0（步） | 向 trr 写速度的间隔；0 表示不写 | 5.8.3 节 |
| nstfout | `nstfout = 0` | 0（步） | 向 trr 写力的间隔；0 表示不写 | 5.8.3 节 |
| nstlog | `nstlog = 1000` | 1000（步） | 向日志文件写能量的间隔 | 5.8.3 节 |
| nstcalcenergy | `nstcalcenergy = 100` | 100（步） | 能量计算间隔，0 表示不计算；并行时该间隔影响全局通信开销 | 6.3 节 |
| nstenergy | `nstenergy = 1000` | 1000（步） | 向 edr 写能量的间隔，应为 nstcalcenergy 的整数倍；edr 保留精确和与涨落，故可回推精确平均 | 5.8.3 节 |
| nstxout-compressed | `nstxout-compressed = 1000` | 0（步） | 向 xtc 写有损压缩坐标的间隔；0 表示不写 | 5.8.3 节、6.7 节 |
| compressed-x-precision | `compressed-x-precision = 1000` | 1000 | xtc 坐标压缩精度 | 5.8.3 节 |
| compressed-x-grps | `compressed-x-grps = Protein` | 全体体系 | 写入 xtc 的索引组 | 6.7 节 |
| energygrps | `energygrps = Protein SOL` | 无 | 单独统计短程非键势能的组；GPU 上不支持 | 6.3 节 |

## 邻居搜索与非键相互作用

表 A-5　邻居搜索、截断与范德华选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| cutoff-scheme | `cutoff-scheme = Verlet` | Verlet（列表首项） | 邻居表生成方案；Verlet 用缓冲自动定 rlist，group 方案在 2026.4 文档中标注不再支持 | 5.8.2 节 |
| nstlist | `nstlist = 20` | 10（步） | 邻居表更新间隔；并行或 GPU 短程力时 20 或 40 常见更佳，最小化时该值不生效 | 5.8.2 节、6.4.3 节 |
| rlist | `rlist = 1.1` | 1（nm） | 短程邻居表截断；动力学下由 verlet-buffer-tolerance 自动确定，取值被忽略 | 5.8.2 节 |
| verlet-buffer-tolerance | `verlet-buffer-tolerance = 0.005` | 0.005（kJ·mol⁻¹·ps⁻¹） | Verlet 缓冲容许的每粒子对相互作用误差，间接决定 rlist；设为 -1 时改用手动 rlist | 5.8.2 节 |
| verlet-buffer-pressure-tolerance | `verlet-buffer-pressure-tolerance = 0.5` | 0.5（bar） | 邻居表老化导致的平均压力容许误差；文档注明 0.5 bar 对应液态水密度相对偏差约 2×10⁻⁵ | 5.8.2 节 |
| vdwtype | `vdwtype = Cut-off` | Cut-off（列表首项） | 范德华相互作用方案：Cut-off 截断，PME 为 LJ-PME（配 lj-pme-comb-rule），Shift 与 Switch 已弃用 | 5.8.2 节 |
| vdw-modifier | `vdw-modifier = Potential-shift` | Potential-shift（列表首项） | 范德华势在截断处的处理：Potential-shift 平移至零、Force-switch 平滑力、Potential-switch 平滑势 | 5.8.2 节 |
| rvdw | `rvdw = 1.0` | 1（nm） | 范德华（LJ 或 Buckingham）截断距离 | 5.8.2 节 |
| rvdw-switch | `rvdw-switch = 0.9` | 0（nm） | 范德华势或力切换的起始距离，仅在使用 switch 型修饰时有效 | 5.8.2 节 |
| DispCorr | `DispCorr = EnerPres` | no（列表首项） | 长程色散修正：EnerPres 修正能量与压力，Ener 仅修正能量，旧写法 dispcorr 同义 | 5.8.2 节 |
| table-extension | `table-extension = 1.0` | 1（nm） | 非键势查找表超出最大截断的延伸长度；1-4 相互作用始终查表 | — |

## 静电与 PME

表 A-6　静电处理方法与 PME 选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| coulombtype | `coulombtype = PME` | Cut-off（列表首项） | 静电方案：PME（平滑粒子网格 Ewald，默认不做）、Ewald、Reaction-Field、Cut-off、P3M-AD；User 等表格式当前不受支持 | 5.8.2 节、11.1.3 节 |
| coulomb-modifier | `coulomb-modifier = Potential-shift` | Potential-shift（列表首项） | 库仑势在截断处的处理；None 保留未修饰势，便于与其他软件比较能量 | 5.8.2 节 |
| rcoulomb | `rcoulomb = 1.0` | 1（nm） | 库仑截断距离；PME 下可被 mdrun 的 PME 调优抬升 | 5.8.2 节 |
| rcoulomb-switch | `rcoulomb-switch = 0.8` | 0（nm） | 库仑势/力切换起始距离，仅切换型修饰时有效 | 5.8.2 节 |
| epsilon-r | `epsilon-r = 1` | 1 | 相对介电常数，0 表示无穷大 | — |
| epsilon-rf | `epsilon-rf = 80` | 0 | 反应场介电常数，仅 Reaction-Field 使用；0 表示无穷大 | — |
| fourierspacing | `fourierspacing = 0.12` | 0.12（nm） | PME/Ewald 网格间距下限，决定各方向反空间格点数 | 5.8.2 节、11.1.3 节 |
| fourier-nx、fourier-ny、fourier-nz | `fourier-nx = 64` | 0 | 各方向反空间格点数或波矢量上限；非零时覆盖 fourierspacing，宜取 2、3、5、7 的幂 | 5.8.2 节 |
| pme-order | `pme-order = 4` | 4 | PME 插值阶数（实际阶数减一，默认 4 对应三次插值）；CPU 上仅 4、5 有 SIMD 加速 | 5.8.2 节、11.1.3 节 |
| ewald-rtol | `ewald-rtol = 1e-5` | 10⁻⁵ | 直接空间与倒空间相对误差分配；调小则直接空间更准、所需波矢量更多 | 11.1.3 节 |
| ewald-rtol-lj | `ewald-rtol-lj = 1e-3` | 10⁻³ | LJ-PME 下色散势的相对误差控制，用法同 ewald-rtol | — |
| lj-pme-comb-rule | `lj-pme-comb-rule = Lorentz-Berthelot` | Geometric（列表首项） | LJ-PME 倒空间使用的组合规则；Geometric 更快，即使力场整体用 Lorentz-Berthelot 也常推荐 | — |
| ewald-geometry | `ewald-geometry = 3dc` | 3d（列表首项） | Ewald 求和维度；3dc 为伪二维（z 方向加了力与势修正），用于平板几何 | — |
| epsilon-surface | `epsilon-surface = 78` | 0 | 三维 Ewald 的偶极修正（周围假想介质的相对介电常数）；存在自由移动电荷时不应启用 | — |

## 约束

表 A-7　约束选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| constraints | `constraints = h-bonds` | none（列表首项） | 把拓扑中哪些键转换为刚性约束：h-bonds 仅含氢键，all-bonds 全部键；h-angles 与 all-angles 已弃用 | 5.8.1 节 |
| constraint-algorithm | `constraint-algorithm = LINCS` | LINCS（列表首项） | 非 SETTLE 全同约束的求解器：LINCS（并行时自动用 P-LINCS）或 SHAKE；文档注明 SHAKE 不能用于能量最小化 | 5.8.1 节、6.6.1 节、11.1.2 节 |
| shake-tol | `shake-tol = 0.0001` | 0.0001 | SHAKE 的相对容差，文档注明 0.0001 对常规 MD 是合适的值 | 5.8.1 节 |
| lincs-order | `lincs-order = 6` | 4 | LINCS 约束耦合矩阵展开阶数；虚拟位点或大步长需要 6，双精度高精度最小化可用 8 | 5.8.1 节、6.6.1 节 |
| lincs-iter | `lincs-iter = 2` | 1 | LINCS 转动伸长修正的迭代次数；NVE 精确能量守恒可用 2 | 5.8.1 节、6.6.1 节 |
| lincs-warnangle | `lincs-warnangle = 30` | 30（度） | 单步内键旋转超过该角度时输出 LINCS 警告 | 6.6.1 节 |

## 控温

表 A-8　控温选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| tcoupl | `tcoupl = v-rescale` | no（列表首项） | 恒温器：v-rescale（随机速度缩放，正则系综）、nose-hoover、berendsen（仅复现旧算例）、andersen、andersen-massive；v-rescale 的随机种子由 ld-seed 控制 | 5.5 节 |
| nsttcouple | `nsttcouple = 40` | -1 | 温度耦合间隔；-1 由 grompp 取 100 或按精度要求取更小值（一阶耦合每 τ 至少 5 步），速度 Verlet 下固定为 1 | 5.5 节 |
| nh-chain-length | `nh-chain-length = 10` | 10 | Nosé-Hoover 链长度；leap-frog 积分器仅支持 1 | 5.5.3 节 |
| tc-grps | `tc-grps = Protein Non-Protein` | 无 | 耦合到独立温度浴的组列表，个数须与 tau-t、ref-t 一致 | 5.5.1 节 |
| tau-t | `tau-t = 1.0 1.0` | 无（-1 表示不耦合） | 温度耦合时间常数（每组一个）；作为恒温器时 sd 的 tau-t 官方建议 2 ps | 5.5.1 节、5.5.3 节 |
| ref-t | `ref-t = 310 310` | 无 | 参考温度（每组一个），单位 K | 5.5.1 节 |
| ensemble-temperature-setting | `ensemble-temperature-setting = constant` | auto（列表首项） | 系综温度来源：auto 自动判断、constant 取 ensemble-temperature、variable 用于退火或模拟回火、not-available | 8.6 节 |
| ensemble-temperature | `ensemble-temperature = 310` | -1（K） | 恒定系综温度；AWH 等算法要求存在恒定系综温度 | 8.6 节 |
| annealing | `annealing = single` | no（列表首项） | 各温度组的模拟退火方式：single 单次序列、periodic 周期重复 | — |
| annealing-npoints、annealing-time、annealing-temp | `annealing-npoints = 3 4` | 无 | 退火参考点的个数、时间与温度列表，条目划分须与各温度组对应 | — |

## 控压

表 A-9　控压选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| pcoupl | `pcoupl = Parrinello-Rahman` | no（列表首项） | 压力耦合：C-rescale（平衡与生产皆可）、Parrinello-Rahman、Berendsen（仅复现旧算例）、MTTK（已弃用，仅速度 Verlet）；no 表示盒尺寸固定 | 5.6 节 |
| pcoupltype | `pcoupltype = semiisotropic` | 无（官方文档未列默认） | 耦合的各向异性：isotropic、semiisotropic（膜等 xy/z 不同）、anisotropic（6 分量）、surface-tension（表面张力） | 5.6.4 节 |
| nstpcouple | `nstpcouple = 40` | -1 | 压力耦合间隔；-1 同样自动取 100 或更小；GROMACS 2023 提高过该默认值，2025.4 起强制每周期步数下限 | 5.6.2 节 |
| tau-p | `tau-p = 5.0` | 5（ps） | 压力耦合时间常数；C-rescale 官方建议不小于 5 ps | 5.6.2 节、5.6.3 节 |
| compressibility | `compressibility = 4.5e-5` | 无 | 等温压缩率（bar⁻¹）；文档注明水在 1 atm、300 K 时为 4.5×10⁻⁵ bar⁻¹，水体系通常直接采用该值 | 5.6.2 节 |
| ref-p | `ref-p = 1.0 1.0` | 无 | 参考压力（bar），分量数由 pcoupltype 决定 | 5.6.2 节 |
| refcoord-scaling | `refcoord-scaling = com` | no（列表首项） | 位置限制参考坐标随压力耦合缩放的方式；no 时 virial 与压力可能定义不当 | 5.6.2 节 |

版本差异说明：GROMACS 2023 起大幅提高 nstpcouple 的默认值[官方文档]；这一改动在 2025.4 中配套引入了两个下限约束——C-rescale 每耦合周期（tau-p）至少 25 步，Parrinello-Rahman 每周期至少 200 步，否则体积涨落可能偏大（官方发布说明）。

## 自由能计算（free-energy 前缀）

表 A-10　炼金术自由能选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| free-energy | `free-energy = yes` | no（列表首项） | 在拓扑 A（λ=0）与拓扑 B（λ=1）之间插值并写出 dH/dλ 或 ΔH；expanded 为扩展系综模式 | 8.2 节 |
| init-lambda | `init-lambda = 0.5` | -1 | λ 的起始浮点值；一般只在慢增长（delta-lambda 非零）时使用 | 8.2 节 |
| delta-lambda | `delta-lambda = 0.0001` | 0 | 每步 λ 增量（慢增长） | 8.2.1 节 |
| init-lambda-state | `init-lambda-state = 10` | -1 | 起始 λ 态（整数下标，从 0 计），指定使用 λ 向量（fep-lambdas 等）的哪一列 | 8.2.6 节 |
| fep-lambdas | `fep-lambdas = 0.0 0.5 1.0` | 无（数组） | 计算并写出 ΔH 的 λ 值列，未指定的分量沿用该向量；配 gmx bar 使用 | 8.2.2 节、8.2.6 节 |
| coul-lambdas、vdw-lambdas | `coul-lambdas = 0.0 0.5` | 无（数组） | 分别只控制静电、范德华分量的 λ 向量 | 8.2.6 节 |
| bonded-lambdas、restraint-lambdas、mass-lambdas、temperature-lambdas | `bonded-lambdas = 0 1` | 无（数组） | 分别控制成键、限制性（二面角限制与 pull 限制）、质量、温度分量的 λ 向量 | 8.2.6 节 |
| calc-lambda-neighbors | `calc-lambda-neighbors = -1` | 1 | 计算并写出 ΔH 的「外来」λ 态范围；BAR 用 1 即够，MBAR 用 -1（全部） | 8.2.2 节、8.2.3 节 |
| sc-function | `sc-function = gapsys` | beutler（列表首项） | soft-core 函数形式：Beutler 或 Gapsys | 8.2.4 节 |
| sc-alpha | `sc-alpha = 1.0` | 0 | Beutler soft-core 的 α 参数；大于 0 时启用 LJ 与库仑软化，0 表示线性插值 | 8.2.4 节 |
| sc-r-power | `sc-r-power = 6` | 6 | soft-core 径向项幂次 | 8.2.4 节 |
| sc-coul | `sc-coul = yes` | no | 是否对库仑相互作用应用 soft-core；通常先线性关库仑再关范德华 | 8.2.4 节 |
| sc-power | `sc-power = 2` | 1 | soft-core 中 λ 的幂次，仅支持 1 与 2 | 8.2.4 节 |
| sc-sigma | `sc-sigma = 0.3` | 0.3（nm） | C6/C12 为零或 σ 小于该值的粒子所用 soft-core σ | 8.2.4 节 |
| couple-moltype | `couple-moltype = Lig` | 无 | 计算溶剂化/耦合自由能的分子类型；system 表示耦合整个体系 | 8.2.6 节 |
| couple-lambda0 | `couple-lambda0 = none` | vdw-q（列表首项） | λ=0 处该分子的状态：vdw-q 全开、vdw 关电荷、q 关范德华、none 全关 | 8.2.6 节 |
| couple-lambda1 | `couple-lambda1 = none` | 同 couple-lambda0 | λ=1 处该分子的状态 | 8.2.6 节 |
| couple-intramol | `couple-intramol = yes` | no | 是否同时开关分子内非键相互作用；yes 用于大分子避免真空态动力学俘获 | 8.2.6 节 |
| nstdhdl | `nstdhdl = 100` | 100（步） | 向 dhdl.xvg 写 dH/dλ 与 ΔH 的间隔；0 表示不写，应为 nstcalcenergy 的整数倍 | 8.2.6 节 |
| dhdl-derivatives | `dhdl-derivatives = yes` | yes（列表首项） | 是否写出 dH/dλ；热力学积分与 gmx bar 插值需要 | 8.2.1 节、8.2.2 节 |
| dhdl-print-energy | `dhdl-print-energy = potential` | no | 在 dhdl 中附带总能或势能；各态温度不同或 mdrun -rerun 时有用 | 8.2.6 节 |
| separate-dhdl-file | `separate-dhdl-file = yes` | yes（列表首项） | yes 时自由能数据写独立 dhdl.xvg；no 时写入 edr | 8.2.6 节 |

## 伞形采样与定向拉伸（pull 前缀）

表 A-11　pull 选项（伞形采样、恒力拉伸、定向拉伸）

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| pull | `pull = yes` | no（列表首项） | 质心（COM）拉动总开关；no 时其余 pull 选项被忽略 | 8.3 节 |
| pull-ngroups | `pull-ngroups = 2` | 1 | 拉动组数目（不含绝对参考） | 8.3.1 节 |
| pull-ncoords | `pull-ncoords = 1` | 1 | 拉动坐标数目，各坐标选项以下标区分 | 8.3.1 节 |
| pull-group1-name | `pull-group1-name = Lig` | 无 | 拉动组名称，取自索引文件 | 8.3.1 节 |
| pull-group1-pbcatom | `pull-group1-pbcatom = 0` | 0 | 组内 PBC 处理参考原子；0 取序号居中的原子，-1 开启余弦加权 | 8.3.2 节 |
| pull-nstxout | `pull-nstxout = 50` | 50（步） | 向 pullx.xvg 写组 COM 的间隔 | 8.3.2 节 |
| pull-nstfout | `pull-nstfout = 50` | 50（步） | 向 pullf.xvg 写拉动力的间隔 | 8.3.2 节 |
| pull-constr-tol | `pull-constr-tol = 1e-6` | 10⁻⁶ | 约束型拉动（pull-coord1-type=constraint）的相对容差 | 8.3.2 节 |
| pull-cylinder-r | `pull-cylinder-r = 1.5` | 1.5（nm） | cylinder 几何的选取半径 | 8.3.2 节 |
| pull-coord1-type | `pull-coord1-type = umbrella` | umbrella（列表首项） | 坐标类型：umbrella（谐振势）、constraint（刚性约束）、constant-force、flat-bottom、flat-bottom-high | 8.3.2 节 |
| pull-coord1-geometry | `pull-coord1-geometry = direction` | distance（列表首项） | 坐标几何：distance、direction、direction-periodic、direction-relative、cylinder、angle、angle-axis、dihedral、transformation | 8.3.1 节 |
| pull-coord1-dim | `pull-coord1-dim = Y Y N` | Y Y Y | 坐标作用的笛卡尔分量 | 8.3.1 节 |
| pull-coord1-origin | `pull-coord1-origin = 0.0 0.0 0.0` | 0.0 0.0 0.0（nm） | 绝对参考的参考位置 | 8.3.1 节 |
| pull-coord1-vec | `pull-coord1-vec = 1.0 0.0 0.0` | 0.0 0.0 0.0 | 拉动方向，grompp 自动归一化 | 8.3.1 节 |
| pull-coord1-start | `pull-coord1-start = yes` | no（列表首项） | yes 时把起始构型的 COM 距离加到 init 上 | 8.3.2 节 |
| pull-coord1-init | `pull-coord1-init = 0.5` | 0.0（nm 或度） | t=0 时的参考距离或参考角度 | 8.3.2 节 |
| pull-coord1-rate | `pull-coord1-rate = 0.001` | 0（nm·ps⁻¹ 或 度·ps⁻¹） | 参考位置变化的速率（定向拉伸） | 8.3.2 节 |
| pull-coord1-k | `pull-coord1-k = 1000` | 0（kJ·mol⁻¹·nm⁻² 等） | 力常数；umbrella 为谐振力常数，constant-force 为该线性势力常数的相反数 | 8.3.2 节 |
| pull-print-com | `pull-print-com = yes` | no | 是否向 pullx.xvg 打印各组 COM | 8.3.2 节 |
| pull-xout-average、pull-fout-average | `pull-xout-average = yes` | no | 分别以输出间隔内的平均坐标、平均力写 pullx/pullf | 8.3.2 节 |

## 自适应偏置（awh 前缀）

表 A-12　AWH 自适应偏置选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| awh | `awh = yes` | no（列表首项） | 用 AWH 方法对反应坐标自适应加偏置并估计 PMF；要求体系存在恒定系综温度，PMF 写入 edr 由 gmx awh 提取 | 8.6.4 节 |
| awh-potential | `awh-potential = umbrella` | convolved（列表首项） | 偏置势形式：convolved 为偏置函数与一组谐振伞势的卷积（默认），umbrella 为蒙特卡洛采样伞位置（与自由能 λ 维并用时的必需项） | 8.6.4 节 |
| awh-seed | `awh-seed = 1234` | -1 | 伞位置蒙特卡洛采样的随机种子 | 8.6.4 节 |
| awh-nstout | `awh-nstout = 100000` | 100000（步） | 向 edr 写 AWH 数据的间隔，应为 nstenergy 的整数倍 | 8.6.4 节 |
| awh-nstsample | `awh-nstsample = 10` | 10（步） | 坐标采样间隔，是偏置更新与 PMF 估计的基础 | 8.6.4 节 |
| awh-nsamples-update | `awh-nsamples-update = 100` | 100 | 每次偏置更新所用的样本数；更新间隔为 nstsample 与其乘积 | 8.6.4 节 |
| awh-nbias | `awh-nbias = 1` | 1 | 偏置个数，各偏置以下标区分 | 8.6.4 节 |
| awh1-error-init | `awh1-error-init = 10.0` | 10.0（kJ·mol⁻¹） | PMF 初始平均误差估计，决定初始偏置速率；新算例一般保持默认 | 8.6.4 节 |
| awh1-growth | `awh1-growth = linear` | exp-linear（列表首项） | 参考权重直方图的增长方式；exp-linear 先指数后线性，linear 跳过初始阶段 | 8.6.4 节 |
| awh1-growth-factor | `awh1-growth-factor = 2` | 2 | 指数阶段增长因子 γ，须大于 1 | 8.6.4 节 |
| awh1-target | `awh1-target = boltzmann` | constant（列表首项） | 目标分布：constant（均匀）、cutoff、boltzmann、local-boltzmann | 8.6.4 节 |
| awh1-target-beta-scaling | `awh1-target-beta-scaling = 0.1` | 0 | boltzmann 类目标分布的反温度缩放因子，取值 (0,1) | 8.6.4 节 |
| awh1-dim1-coord-provider | `awh1-dim1-coord-provider = fep-lambda` | pull（列表首项） | 该维反应坐标的来源：pull 模块坐标或自由能 λ 态 | 8.6.4 节 |
| awh1-dim1-coord-index | `awh1-dim1-coord-index = 1` | 1 | 作为该维坐标的 pull 坐标序号 | 8.6.4 节 |
| awh1-dim1-force-constant | `awh1-dim1-force-constant = 500` | 0（kJ·mol⁻¹·nm⁻² 或 rad⁻²） | 该维（卷积）伞势的力常数 | 8.6.4 节 |
| awh1-dim1-start、awh1-dim1-end | `awh1-dim1-start = 0.0` | 0.0（nm 或度） | 该维采样区间起点与终点 | 8.6.4 节 |
| awh1-dim1-diffusion | `awh1-dim1-diffusion = 1e-5` | 10⁻⁵（nm²·ps⁻¹ 等） | 该维估计扩散常数，决定初始偏置速率，粗略估计即可 | 8.6.4 节 |

## 虚拟位点

GROMACS 2026.4 的 mdp 文档没有独立的虚拟位点开关。虚拟位点由拓扑中的 [virtual_sites2]、[virtual_sites3]、[virtual_sites4] 与 [virtual_sitesn] 节定义，把若干原子（称为构造原子）的位置线性组合为虚拟位点，用于 TIP4P 类水模型、氢质量重分配与通用构型构造。mdp 侧与虚拟位点相关的设置只有间接影响，见下表。

表 A-13　虚拟位点相关的 mdp 注意事项

| 相关项 | 取值/情形 | 说明 | 相关章节 |
| --- | --- | --- | --- |
| lincs-order | `lincs-order = 6` | 虚拟位点体系配大步长时，官方文档注明 lincs-order 需提高到 6 | 5.8.1 节 |
| 时间步长 | 虚拟位点几何配合 constraints=h-bonds | 可支持 4 fs 步长的一类实现途径 | 5.8.1 节 |
| GPU-resident 模式 | `-update gpu` 等组合 | 官方 mdrun 性能指南注明该模式不支持虚拟位点等若干功能组合 | 2.1.2 节 |
| 拓扑定义 | [virtual_sites2/3/4/n] | 虚拟位点的位置与权重在拓扑节中定义，无需 mdp 选项 | 4.4 节 |

## 非平衡 MD 与特殊功能

表 A-14　加速度、冻结与盒变形等特殊选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| acc-grps | `acc-grps = Protein` | 无 | 施加恒定加速度的组 | — |
| accelerate | `accelerate = 0.1 0.0 0.0` | 0（nm·ps⁻²） | 各组恒定加速度分量；被加速组的质心动能计入温度，必要时应单独控温 | — |
| freezegrps、freezedim | `freezegrps = Lipid` `freezedim = Y Y N` | 无 | 冻结组的坐标不再更新（按维度）；存在冻结原子时 virial 与压力通常无意义 | — |
| cos-acceleration | `cos-acceleration = 0.01` | 0（nm·ps⁻²） | 黏度计算用余弦加速度剖面振幅，向 edr 额外写速度剖面振幅与 1/黏度 | — |
| deform | `deform = 0 0 0 0 0 0` | 0 0 0 0 0 0（nm·ps⁻¹） | 盒元素变形速率：a(x) b(y) c(z) b(x) c(x) c(y)；剪切或拉伸固体/液体 | — |
| deform-init-flow | `deform-init-flow = yes` | no | 初始速度叠加与盒变形对应的流场 | — |
| nwall | `nwall = 2` | 0 | 墙壁数目（z=0 与 z=盒高）；仅限 pbc=xy，nwall=2 时方可用控压与 Ewald | — |
| wall-type | `wall-type = 9-3` | 9-3（列表首项） | 墙壁势形式：9-3（体积积分）、10-4（表面积分）、12-6、table | — |
| wall-ewald-zfac | `wall-ewald-zfac = 3` | 3 | 配 nwall=2 时第三盒矢量的放大倍数（Ewald 专用，最小 2） | — |

## 限制性约束（NMR 与取向约束）

表 A-15　距离与取向限制选项

| 选项 | 取值示例 | 默认值 | 含义 | 相关章节 |
| --- | --- | --- | --- | --- |
| disre | `disre = simple` | no（列表首项） | 距离限制：simple 按分子施加，ensemble 对系综平均 | — |
| disre-fc | `disre-fc = 1000` | 1000（kJ·mol⁻¹·nm⁻²） | 距离限制力常数，拓扑 fac 列可逐条加权 | — |
| disre-tau | `disre-tau = 10` | 0（ps） | 距离限制时间平均常数；0 关闭时间平均 | — |
| nstdisreout | `nstdisreout = 100` | 100（步） | 时间平均与瞬时距离写 edr 的间隔 | — |
| orire | `orire = yes` | no（列表首项） | 取向限制开关，可用 mdrun -multidir 做系综平均 | — |
| orire-fc、orire-tau | `orire-fc = 100` | 0（kJ·mol⁻¹）、0（ps） | 取向限制力常数与时间平均常数 | — |

## 来源说明

本附录所有默认值、单位与语义均引自下列官方文档，每条断言以「[官方文档]」标注：

- GROMACS 2026.4 用户指南「Molecular dynamics parameters (.mdp options)」，https://manual.gromacs.org/2026.4/user-guide/mdp-options.html（对应源文件 docs/user-guide/mdp-options.rst，标签 v2026.4）。
- GROMACS 2026.4 发布说明 2025.4「The C-rescale barostat…」与「The Parrinello-Rahman barostat…」条目，https://manual.gromacs.org/2026.4/release-notes/2025/2025.4.html。
- 表 A-13 中 GPU-resident 模式的限制源自 GROMACS 2026.4 用户指南「Getting good performance from mdrun」。

表中「相关章节」一列的「—」表示该选项未在本书正文展开讨论；涉及书目章节的编号与正文 5.8、6.3、8.2 等节一致。默认值若随候选值列表给出（如 tcoupl），以列表首项为默认，与官方文档「第一个选项总是默认」的约定相同。