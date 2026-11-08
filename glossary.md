# 术语表（glossary）

本表收录《GROMACS 分子动力学模拟与Python编程》全书正文出现的专业术语，按第 1 章 1.7.4 节的登记约定给出中文术语、英文原词、缩写与一句定义，并标注术语首次给出定义或首次展开的章节。「首次出现章节」一列精确到节：凡该术语在对应节有明确定义或展开者标为「第 X 章 x.y 节」，其余以章为单位标注。行序按英文原词的字母顺序排列，便于按英文检索；中文检索可借助电子文档的全文搜索定位。缩写栏以「—」表示该术语无通行缩写。表中定义均依据本书正文各章已核验陈述改写，不引入正文之外的断言；版本相关的行为以 GROMACS 2026.4 为准。

表 G-1　全书术语中英对照表

| 中文术语 | 英文原词 | 缩写 | 定义 | 首次出现章节 |
| --- | --- | --- | --- | --- |
| 12-6-4 型离子参数 | 12-6-4 LJ-type ion parameters | — | 在 12-6 Lennard-Jones 非键模型上叠加离子-配体校正项的二价离子参数族，须整套使用并按水模型配套 | 4.7.3 节 |
| 加速权重直方图（自适应偏置） | accelerated weight histogram | AWH | 沿反应坐标自适应更新偏置势并直接估计 PMF 的增强采样方法，偏置更新速率由估计误差控制 | 8.6.4 节 |
| 炼金术自由能 | alchemical free energy | — | 通过耦合参数 λ 把体系从一个端态连续变换到另一端态而计算的自由能差，用于溶剂化与相对结合自由能 | 8.2 节 |
| 炼金术拓扑准备 | alchemical topology preparation | — | 为多窗口自由能计算设置 dummy 原子与 couple-* 耦合参数、以 B 态表达微扰的拓扑构造步骤 | 8.2.2 节 |
| AM1-BCC | AM1-BCC | — | 以半经验 AM1 计算叠加经验键荷修正、快速生成凝聚相质量原子电荷的方案，是全自动参数化的默认电荷方法 | 4.8.1 节 |
| 原子电荷 | atomic charge | — | 力场分配给每个原子的点电荷，与原子坐标共同决定体系的库仑相互作用 | 4.8.1 节 |
| 原子类型 | atom type | — | 力场中区分化学环境的原子分类标识，决定质量、电荷规则及非键与成键参数的查表入口 | 4.4.1 节 |
| 自相关函数 | autocorrelation function | — | 同一可观测量在相隔时间间隔 t 的两时刻取值之积的统计平均，刻画时间序列的记忆长度 | 9.2.1 节 |
| 恒压器 | barostat | — | 通过调节盒尺寸维持目标压力的耦合算法，与恒温器共同实现对压力系综的控制 | 5.6 节 |
| 珠 | bead | — | 粗粒化力场中代表约四个重原子的相互作用中心，是 Martini 等粗粒化模型的构建单元 | 4.4.3 节 |
| Bennett 接受比 | Bennett acceptance ratio | BAR | 同时利用前向与后向样本并使方差最小的成对自由能差估计方法，是现代工作流的成对状态估计标准 | 8.2.2 节 |
| Berendsen 弱耦合 | Berendsen weak coupling | — | 以指数弛豫方式把温度或压力拉向目标值的控温/控压算法，只适合平衡引导，不产生严格的目标系综 | 5.5.2 节 |
| 块平均 | block averaging | — | 把相关时间序列分成若干块、以块均值及其离散度估计均值与统计误差的方法 | 9.3.1 节 |
| 块平均低估因子 | block-averaging underestimation factor | — | 固定块长分块平均低估不确定度的因子，块长不足时 SE 随 L 增大，平台化判据为相邻块长方差变化 <5% | 9.3 节 |
| 自助法 | bootstrap | — | 从样本中有放回地重抽样、以重采样分布的离散度估计统计不确定度的通用方法 | 9.3.2 节 |
| 正则系综 | canonical ensemble | NVT | 粒子数、体积与温度恒定的统计系综，由恒温器维持 | 5.5 节 |
| 检查点 | checkpoint | — | 周期记录坐标、速度与步号的二进制快照（state.cpt），是中断后可续算的基础 | 6.2.2 节 |
| 残基距离接触矩阵 | residue distance contact map | RDCM | 以残基对距离为矩阵元的构象描述，可定义接触与 encounter 并统计占有率、衍生 RMSD/RMSF/DCCM/PCA | 7.4.5 节 |
| 粗粒化 | coarse-grained | CG | 把约四个重原子合并为单个相互作用中心的建模层次，可把可模拟尺度提升数个量级 | 4.4.3 节 |
| 集体变量 | collective variable | CV | 描述体系慢过程的一个或一组坐标函数（距离、二面角等），是增强采样方法施加偏置的对象 | 8.6.1 节 |
| 共轭梯度 | conjugate gradient | CG | 沿互共轭方向序列下降的能量最小化算法，适合在近似收敛区做精细优化 | 5.2.2 节 |
| 约束算法 | constraint algorithm | — | 把拓扑中指定化学键等自由度冻结为刚性约束的数值方法，GROMACS 提供 LINCS、SHAKE 与 SETTLE | 5.8.1 节 |
| 库仑相互作用 | Coulomb interaction | — | 点电荷之间的静电相互作用，是力场非键项的两大组分之一 | 4.4.1 节 |
| C-rescale | C-rescale | — | 随机重缩放的恒压算法，兼顾 Berendsen 的稳健与正则系综的正确性，平衡与生产阶段皆可用 | 5.6.2 节 |
| 截断距离 | cutoff distance | — | 非键相互作用被截断或平滑处理的半径，取值必须满足盒最短边不小于两倍截断的最小镜像条件 | 4.6.2 节 |
| 密度剖面 | density profile | — | 把盒内某组原子沿一个方向切分成薄片、统计各片数密度或质量密度得到的分布曲线 | 7.5.2 节 |
| DSSP | Dictionary of Secondary Structure of Proteins | DSSP | 依据主链氢键模式把残基分配到 α 螺旋、β 折叠片等类别的二级结构判定算法，为事实标准 | 7.4.1 节 |
| 二面角主成分分析 | dihedral principal component analysis | dPCA | 对经三角变换的骨架二面角做特征分解的 PCA 变体，聚焦局部构象变化 | 7.4.2 节 |
| 二面角 | dihedral angle | — | 由四个连续原子定义的扭转角，力场成键项之一；另有 improper 项维持平面性 | 4.4.1 节 |
| 二硫键 | disulfide bond | — | 两个半胱氨酸侧链硫原子之间的共价连接，由 pdb2gmx 依据 specbond 距离判据识别生成 | 4.3.2 节 |
| 域分解 | domain decomposition | DD | 把模拟盒按空间划分为若干域、每个进程负责一个域内粒子计算的并行策略 | 6.4.1 节 |
| 双种子纪律 | dual-seed discipline | — | 同时记录 gen_seed（初速）与 ld_seed（热浴随机流）并以显式值分配副本的可复现性纪律 | 5.4.2 节 |
| 动力学互相关矩阵 | dynamic cross-correlation matrix | DCCM | 以残基对位移涨落的 Pearson 相关系数刻画运动耦合的指标，取值于 −1 与 1 之间，热图呈现区域内协同与区域间反相运动 | 7.4.3 节 |
| 有效样本数 | effective sample size | — | 相关序列折算后等价于独立样本的数目，与积分自相关时间成反比 | 9.2.3 节 |
| 有效样本数 | effective sample size | N_eff | 以自相关时间修正后的独立样本数，N_eff = T/(2τ_int)，是均值标准误的正确分母 | 9.2 节 |
| 能量最小化 | energy minimization | EM | 通过迭代优化使体系势能降至局部极小附近的预处理步骤，用于消除初始结构应力 | 5.1 节 |
| 系综 | ensemble | — | 满足给定宏观约束的大量微观状态集合及其上的统计分布，是统计力学推断的载体 | 1.1.1 节 |
| 遍历性 | ergodicity | — | 时间平均等于系综平均的统计性质，是有限采样推断体系平衡性质的隐含前提 | 9.1.1 节 |
| 力场 | force field | FF | 势能函数形式与其参数集的统称，定义了体系总势能随原子坐标的变化 | 1.1.3 节 |
| 自由能面 | free energy landscape | FEL | 沿一个或两个反应坐标把访问频率转换为 −k_BT ln p 的二维自由能图，盆地对应亚态 | 7.4.4 节 |
| 自由能 | free energy | — | 恒温条件下的热力学势（亥姆霍兹或吉布斯自由能），其差决定平衡、结合与构象布居 | 8.1 节 |
| 自由能微扰 | free energy perturbation | FEP | 由两状态间能量差分布的指数平均估计自由能差的方法 | 8.2.2 节 |
| GMXLIB | GMXLIB | — | GROMACS 用于搜索力场目录的环境变量，pdb2gmx 启动时打印实际使用的力场路径 | 4.3.1 节 |
| GPU 卸载 | GPU offload | — | 把短程非键、PME 或成键等计算任务转移到 GPU 执行的并行配置，由 mdrun 的 -nb/-pme 等选项控制 | 6.4.3 节 |
| GPU-resident 模式 | GPU-resident mode | — | 粒子坐标与速度常驻显存、CPU 仅保留域分解与少量控制逻辑的运行模式 | 2.1.2 节 |
| grompp | grompp | — | GROMACS 的预处理工具，把 mdp 参数、拓扑与坐标合并为二进制运行输入 .tpr | 4.1.1 节 |
| 氢键 | hydrogen bond | — | 氢原子桥接供体与受体的弱相互作用，分子动力学中以距离截断与角度截断的几何判据认定 | 7.4.2 节 |
| 氢键寿命 | hydrogen bond lifetime | — | 氢键存在函数自相关的衰减时间尺度，分连续寿命与间歇寿命两种口径 | 7.4 节 |
| 索引组 | index group | — | 由原子编号列表定义的原子集合，是大多数分析工具「统计哪些原子」的输入，存于 .ndx 文件 | 7.2.1 节 |
| 积分自相关时间 | integrated autocorrelation time | — | 自相关函数对时间积分所得的相关时间尺度，决定时间序列的有效样本数 | 9.2.2 节 |
| 等温等压系综 | isothermal-isobaric ensemble | NPT | 粒子数、压力与温度恒定的统计系综，由恒温器与恒压器共同维持 | 5.6 节 |
| Lennard-Jones 势 | Lennard-Jones potential | LJ | 由排斥项与吸引项构成的两体范德华势，参数为阱深 ε 与碰撞直径 σ | 4.4.1 节 |
| 配体-蛋白相互作用分析 | protein-ligand interaction profiling | PLIP | 以几何判据（氢键、疏水、π-π、π-阳离子、盐桥等）枚举并统计配体-蛋白相互作用的工具链 | 7.5.5 节 |
| 配体参数化 | ligand parametrization | — | 为不在标准残基库中的小分子生成原子类型、电荷与成键参数的全过程 | 4.8 节 |
| LINCS | LINear Constraint Solver | LINCS | 以矩阵展开迭代求解键约束的算法，是 GROMACS 的默认约束求解器 | 5.8.1 节 |
| 整体化 | make whole | — | 把被周期边界切开的分子沿化学键拼合完整的轨迹预处理操作（trjconv -pbc whole/mol） | 7.1.1 节 |
| 马尔可夫状态模型 | Markov state model | MSM | 把相空间离散为状态、以转移矩阵描述状态间跃迁并推断慢动力学的模型 | 7.4.9 节 |
| 消息传递接口 | Message Passing Interface | MPI | 进程间通信的标准接口；GROMACS 跨节点并行依赖 MPI 或内置的 thread-MPI | 2.6.4 节 |
| 元动力学 | metadynamics | — | 沿集体变量周期沉积偏置势、使体系逐渐翻越自由能垒的增强采样方法 | 8.6.2 节 |
| 最小镜像约定 | minimum image convention | — | 只考虑每个粒子最近镜像之间相互作用的计算约定，其成立前提是截断半径不大于盒最短边长的一半 | 4.6.2 节 |
| 模型误差 | model error | — | 源于模型自身近似（力场参数、截断方案等）的误差，延长采样不能改善 | 8.1.3 节 |
| 分子动力学 | molecular dynamics | MD | 数值积分经典牛顿运动方程、生成体系随时间的微观轨迹并据此统计热力学量的方法 | 1.1.1 节 |
| 分子型 | moleculetype | — | 拓扑中一种分子类型的定义（原子、成键与参数），[ molecules ] 段声明其在体系中的拷贝数 | 4.1 节 |
| 多态 Bennett 接受比 | multistate Bennett acceptance ratio | MBAR | 利用全部状态样本同时估计多个状态之间自由能的统计方法，是 WHAM 的更一般形式 | 8.3.3 节 |
| 非键相互作用 | nonbonded interaction | — | 不依赖化学键连接关系的 Lennard-Jones 与库仑相互作用之和，决定分子间与远程分子内作用 | 4.4.1 节 |
| Nosé-Hoover 恒温器 | Nosé-Hoover thermostat | — | 通过扩展自由度实现确定性的恒温算法，适合平衡统计与生产运行 | 5.5.4 节 |
| Parrinello-Rahman 恒压器 | Parrinello-Rahman barostat | — | 允许盒形状按应力张量涨落的确定性恒压算法，适合生产运行，对初始平衡阶段较敏感 | 5.6.3 节 |
| 粒子网格 Ewald | particle mesh Ewald | PME | 以网格傅里叶变换近似求解长程静电的算法，是显式溶剂体系静电处理的默认方案 | 4.6.2 节 |
| 周期性边界条件 | periodic boundary conditions | PBC | 把体系置于可复制的盒中、以镜像副本模拟无限体系的边界处理方式 | 4.6.1 节 |
| PLUMED | PLUMED | — | 以统一输入语法提供集体变量与增强采样算法的社区插件库，经 gmx mdrun -plumed 接入 | 8.6.1 节 |
| 位置约束 | position restraints | — | 把选定原子束缚在参考坐标附近的谐振势（posre.itp），平衡阶段常用以松弛溶剂 | 4.8.2 节 |
| 势能函数 | potential energy function | — | 以原子坐标为变量的总势能表达式，是力场的函数形式部分 | 4.4.1 节 |
| 平均力势 | potential of mean force | PMF | 沿反应坐标的自由能曲线，是伞形采样与 WHAM 等方法的输出产物 | 8.3 节 |
| 主成分 | principal component | PC | 坐标涨落协方差矩阵的特征向量，轨迹沿其特征方向的方差等于对应特征值 | 8.5.1 节 |
| 主成分分析 | principal component analysis | PCA | 对原子坐标涨落的协方差矩阵做特征分解、提取方差最大的正交方向的方法，前若干主成分常对应协同运动 | 7.4.1 节 |
| 蛋白质数据库 | Protein Data Bank | PDB | 存放生物大分子实验结构的数据组织与坐标格式，也是该数据库的名称 | 4.2.1 节 |
| 质子化态 | protonation state | — | 可电离基团在给定 pH 下的氢原子占据形态，直接决定体系净电荷与氢键网络 | 4.2.2 节 |
| 径向分布函数 | radial distribution function | RDF | 距参考粒子距离 r 处找到目标粒子的概率密度相对均匀分布的倍数，用于描述局域结构与配位 | 7.5.1 节 |
| 回转半径 | radius of gyration | Rg | 分子质量相对质心的分布紧密程度，定义为质量加权均方距的平方根 | 7.3.3 节 |
| 反应坐标 | reaction coordinate | — | 描述化学或构象过程进展的一个或一组坐标，伞形采样等增强采样方法沿其布置窗口 | 8.3.1 节 |
| 恢复 | restart | — | 从检查点文件继续被中断运行的续算方式（mdrun -cpi） | 6.2.3 节 |
| 受限静电势拟合 | restrained electrostatic potential | RESP | 以量子化学静电势为参照、带约束最小二乘拟合的原子电荷方案 | 4.8.1 节 |
| 均方根偏差 | root-mean-square deviation | RMSD | 最小二乘叠加后质量加权均方距的平方根，衡量结构相对参考结构的整体偏离 | 7.3.1 节 |
| 均方根涨落 | root mean square fluctuation | RMSF | 原子位置的时间标准差，表征单个原子或残基围绕平均结构的柔性 | 7.3.2 节 |
| 盐桥 | salt bridge | — | 带相反电荷残基侧链之间由静电主导的近距接触，常以 0.4 nm 距离判据认定 | 7.4.3 节 |
| 盐浓度 | salt concentration | — | 体系中电解质的摩尔浓度，由 genion 的 -neutral 与 -conc 选项控制 | 4.7.2 节 |
| 选择语法 | selection syntax | — | 以关键字与布尔、几何修饰符描述原子集合的表达式语言，可写入脚本并导出索引组 | 7.2.2 节 |
| SETTLE | SETTLE | — | 针对水等三原子刚性分子的解析约束求解算法，计算上精确且高效 | 5.8.1 节 |
| SHAKE | SHAKE | — | 迭代求解键长约束的经典算法，适合小体系；官方注明不可用于能量最小化 | 5.8.1 节 |
| 模拟盒 | simulation box | — | 周期性边界条件下容纳体系的可复制单元，可为立方、菱形十二面体等盒型 | 4.6.1 节 |
| 溶剂化 | solvation | — | 把溶质置于目标溶剂中并消除重叠、建立周期性水环境的步骤，由 solvate 完成 | 4.7.1 节 |
| 溶剂可及表面积 | solvent-accessible surface area | SASA | 滚动探针球（常规取水分子有效半径 1.4 Å）在分子表面扫过的包络面面积 | 7.3.4 节 |
| 统计误差 | statistical error | — | 源于有限采样的误差，随采样时长与样本量的增加而减小 | 8.1.3 节 |
| 最短路径图 | shortest path map | SPM | 以残基距离与相关系数构建图、用最短路径识别别构通信枢纽的分析方法 | 7.4.6 节 |
| 最速下降 | steepest descent | SD | 沿负梯度方向下降的能量最小化算法，适合消除初始立体冲突，收敛后期变慢 | 5.2.1 节 |
| 热力学积分 | thermodynamic integration | TI | 对 ∂H/∂λ 的系综平均沿耦合参数 λ 积分以求得自由能差的方法 | 8.2.1 节 |
| 恒温器 | thermostat | — | 控制体系温度以维持目标系综的耦合算法，如 v-rescale、Nosé-Hoover 与 Berendsen | 5.5 节 |
| thread-MPI | thread-MPI | — | GROMACS 内置的以线程模拟 MPI rank 通信层的单节点并行实现 | 2.6.4 节 |
| 吞吐量 | throughput | — | 单位墙钟时间完成的模拟时长，以 ns/day 或 hour/ns 计，写入 md.log 的性能小结 | 6.5.1 节 |
| 时间滞后独立成分分析 | time-lagged independent component analysis, tICA | tICA | 以时间滞后协方差最大化寻找最慢混合坐标的降维方法，用于 MSM 特征化与慢变量识别 | 7.4.8 节 |
| 时间步长 | time step | dt | 积分器每次推进的时间间隔；全原子显式溶剂体系常规取 0.002 ps，可配合约束与质量重分配提升 | 5.8.1 节 |
| 拓扑 | topology | — | 描述原子类型、电荷、质量与相互作用参数的文件（.top 及其 #include 的 .itp），与坐标逐原子对应 | 4.1.1 节 |
| 轨迹 | trajectory | — | 记录粒子坐标（及速度、力）随时间演化的文件，xtc 为有损压缩格式、trr 为全精度格式 | 1.1.1 节 |
| 伞形采样 | umbrella sampling | — | 沿反应坐标布设带谐振偏置的窗口分别采样、再经重加权拼接为无偏 PMF 的方法 | 8.3 节 |
| 确认 | validation | — | 回答「模型是否与实验吻合」的验证分工（相对 verification），由力场与实验对照承担 | 1.1.2 节 |
| 验证 | verification | — | 回答「数值求解是否正确」的验证分工（相对 validation），由步长、截断与守恒量判据承担 | 1.1.2 节 |
| 虚位点 | virtual site | — | 位置由若干构造原子线性组合定义、不直接参与力计算的几何点，TIP4P 类水模型的 M 位点即属此类 | 4.5.1 节 |
| v-rescale | v-rescale | — | 随机速度缩放恒温器，对速度分布扰动小且可恢复正则系综，为 GROMACS 推荐的生产恒温器 | 5.5.3 节 |
| 水模型 | water model | — | 描述水分子相互作用位点、几何与参数（TIP3P、SPC/E、TIP4P/2005、OPC 等）的模型 | 4.5.1 节 |
| 水分子驻留 | water residence | — | 水分子在蛋白表面或结合位点停留的时间尺度，由壳层计数或氢键寿命刻画 | 7.5.3 节 |
| 均匀流形逼近与投影 | uniform manifold approximation and projection | UMAP | 以流形假设保持局部结构的非线性降维方法，常用于构象系综可视化 | 7.4.8 节 |
| t 分布随机邻域嵌入 | t-distributed stochastic neighbor embedding | t-SNE | 以条件概率保持邻域相似性的非线性降维方法，簇不宜直接当反应坐标 | 7.4.8 节 |
| 加权柱状分析 | weighted histogram analysis method | WHAM | 以迭代重加权把重叠窗口的直方图拼接为无偏 PMF 的经典方法 | 8.3.3 节 |
