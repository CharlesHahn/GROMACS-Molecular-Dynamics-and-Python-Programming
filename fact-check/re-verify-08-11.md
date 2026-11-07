# 第 8–11 章修订后验收（对抗性复核 re-verify v1）

- 复核日期：**2026-11-08**
- 复核对象：`08-自由能、增强采样与高级分析.md`（662 行）、`09-采样统计、误差与可复现性.md`（431 行）、`10-自动化与工程化.md`（604 行）、`11-Python生态与扩展开发.md`（479 行）；对应 refs 与四份 peer-08/09/10/11-review.md（2026-11-04）
- 复核问题：修订后版本是否落实 peer 审查的重点核查项；修订新增内容是否引入新错误
- 核验通道：本会话**未调用 web_search**；唯一联网通道为 anysearch CLI（`D:\CharlieAPP\C_Python\python.exe … anysearch_cli.py`），实际使用 search×12、extract×10、batch_search×1；全部命中记录随附于「五、事实抽查与引文核验记录」
- 判定口径：REVIEW.md（P0=事实错误/结构缺失；P1=修订后可过；P2=记录统稿）

---

## 一、修订落实核查（按任务「重点核查」逐项）

### 第 8 章（34282d6 深度补强；结论：6 项全部落实）

| 重点核查项 | 落实情况 | 复核依据 |
| --- | --- | --- |
| 8.2.2 炼金术拓扑准备整节 | **已落实**（L90–96，含 dummy 原子/B 态参数、couple-* 四参数语义、NVT→NpT pV 修正 22 bar/−1 kJ·mol⁻¹ 例、质量项 −(3/2)k_BT·ln(m_B/m_A)（无约束）、Gilson 1997 标准态根文献、Boresch 类约束「超出本章范围」边界声明） | manual Free energy implementation/Calculations 原文逐句对位 |
| dhdl 去相关协议 | **已落实**（L165：gmx analyze -ac 估 τ → ≥τ 抽稀 → bar/pymbar，交叉第 9 章） | gmx analyze 页原文核实 -ac/-subav/-acflen/-fitfn/-luzar 语义 |
| MBAR 全矩阵 | **已落实**（L110–116：calc-lambda-neighbors 默认 1 / −1=全部、alchemical-analysis 管线（Klimovich 2015）、重叠对角元素诊断、log-sum-exp） | manual + pymbar 文档对位 |
| PMF 误差清单 | **已落实**（L260：六类误差，逐类注明能否靠延长采样修复，空柱病态、边界外推、RC 不完备均在列） | — |
| 窗口数值判据 σ≈0.05 nm | **已落实**（L210：k=1000 kJ·mol⁻¹·nm⁻²、T=300 K 时 σ≈0.05 nm、间距 0.1 nm≈2σ、「间距 ≤2σ 且直方图连通」判据；数值自算成立） | — |
| 元动力学收敛表述一致（WTM 收敛于 −(1−1/γ)F） | **已落实**（L440–442 理想极限 vs 有限沉积分开表述；L466 沉积速率≪CV 弛豫的必要非充分约束；L475 Tiwary–Parrinello 重加权；L521 表 8-7、L614 小结口径一致，无 L423 型自相矛盾残留） | Tiwary & Parrinello 2013 PRL 111(23): 230602 已核 |

另核：FEP/Jensen 偏差方向与 log-space（L104，不等式方向与凹性论证自算成立，βΔU≈710 溢出界正确）；gmx bar 自动求和与平方和合并、-nbmin/-nbmax/-prec（L165）——gmx bar 页原文核实；best-practice 双指针 Pohorille[13]/Mey[14]（L165）。

### 第 9 章（d206b76 深度补强；结论：6 项全部落实）

| 重点核查项 | 落实情况 | 复核依据 |
| --- | --- | --- |
| Sokal 定量 δτ_int/τ_int≈√(2τ_int/T) | **已落实**（L73，含估计量不确定度、「误差棒的误差」含义、窗口化积分替代、均值减除 O(τ/N) 负偏与「伪过零」、负长尾 ACF 首过零失效判据） | Sokal 1997 出处经 INSPIRE/Springer 核验 |
| pymbar.timeseries | **已落实**（L121–123：与手写实现并列、detect_equilibration 返回 t0/g/Neff_max、statistical_inefficiency g=1+2τ（含 FFT）、subsample_correlated_data、「MBAR 仅适用于不相关样本」原文引述） | pymbar 4.x timeseries 文档 extract 逐函数核实 |
| tICA | **已落实**（L258：时间滞后协方差/瞬时协方差之比最大化、变分原理、隐含时间尺度平台化判据、与 PCA 的「高方差≠慢方向」差异、PyEMMA/msmbuilder 工具句、余弦含量启发式局限） | Pérez-Hernández 2013 经 Crossref extract 核验 |
| Yeh–Hummer 修正 | **已落实**（L262：D_∞≈D_PBC+k_BT·ξ/(6πηL)，立方盒 ξ≈2.837；原文系数为 2.837297，「ξ≈2.837」截取合规） | 原文摘要（MPG.PuRe/Crossref）系数 2.837297 核实 |
| AR(1) 自校验 | **已落实**（L139–162：τ_int=ρ/(1−ρ)=9、s=19、SE_plateau²·N/σ²≈1+2τ_int 交叉核对处方） | 数值自算成立 |
| 其他 P1 落实 | 块平均低估因子 s_L/s 与 √(L/τ_int) 极限（L135）、2×√(SE₁²+SE₂²) 判据（L221）、[23] 子空间重叠 vs [24] 手册采样重叠（协方差平方根、手册式 469）区分（L221）、逆方差加权合并与「3 副本一致≠收敛」（L252）、Σ 的块均值协方差估计与 MBAR 去相关前提（L193）、E1/E5/E7 回填（L79/L179/L347）、L154「线性增长」已改「亚线性」（L134–164）、「需要强调」2 处已清（grep 0 命中） | covariance-analysis 页原文核实式 469 与「半/全余弦」判句 |

### 第 10 章（fccd681 定向修订；结论：5 项落实 4 项、1 项订正本身引入新错误）

| 重点核查项 | 落实情况 | 复核依据 |
| --- | --- | --- |
| Snakemake mtime/rerun-triggers 订正 | **部分落实，且有新错误**（L272 已删除前轮 P2-3 的「内容感知校验」夸大；但订正后的「它的依赖判定**默认采用修改时间戳比较**」与官方 CLI 文档相反——Snakemake 9.x `--rerun-triggers {code,input,mtime,params,software-env}` **默认全部触发器启用**，mtime-only 恰是需显式指定的「传统方式」；且示例「--rerun-triggers mtime,input,params,code 可把输入内容哈希与规则代码变化纳入触发条件」把已默认开启的 input/params/code 描述为需「纳入」，并遗漏 software-env 触发器；「输入内容哈希」非该选项文档语义） | Snakemake 9.27.1 CLI 文档 extract 原文：「By default, all triggers are used…；If you rather prefer the traditional way of just considering file modification dates, use --rerun-trigger mtime」 |
| config/params 单一事实源 | **已落实**（新增「#### 配置文件的单一事实源」：config.yaml 承载工作流结构、params.yaml 承载物理参数、显式派生规则消除双轨；落实 peer-10 D3 的「分工」路线） | — |
| 规则级 Slurm 提交 | **已落实**（L395：--executor slurm（9.x 起插件机制）threads/resources→sbatch 映射、--cluster-cancel、afterok、与作业数组两向互补；CLI 文档 profile 示例「executor: slurm」与插件生态对位；--cluster 为 7.x 遗留旗标，与 9.x 并写可接受） | Snakemake CLI 文档 + executor 插件记录 |
| CI 冒烟测试 | **已落实但有断头交叉引用**（L475：snakemake -n / make -n / sbatch --test-only 三级冒烟 + 最小端到端冒烟 + CI 门禁均无事实问题；唯「（--use-conda 环境锁定见 10.6 节）」为**自我悬空引用**——该段本身就在 10.6.4，而全章并无 --use-conda 环境锁定内容（B2 未实现）） | grep 全章无 --use-conda 正文 |
| 格式串 prod-%A_%a | **已落实**（e172e07 修正常见错误 4；L359/L381–382/L535 三处一致 `logs/prod-%A_%a.out`） | SchedMD job array 文档语义（前轮已 fetch 核验） |

### 第 11 章（b38fd5c 定向修订；结论：3 项落实、表 11-4 被拆断）

| 重点核查项 | 落实情况 | 复核依据 |
| --- | --- | --- |
| ML 势验证与 UQ 协议 | **已落实**（L330：训练域覆盖核验、多模型 ensemble 方差 UQ + ground-truth 抽查、NVE 稳定性测试、外推风险不可控时回退决策树） | — |
| 描述符表述修正 | **已落实**（L328：「输入张量须承载坐标与原子序数等量，平移/旋转/置换不变性须由模型架构内建」，与手册 "atomic descriptors…most commonly atom positions and atomic numbers" 对位；peer-11 P1「正确性优先项」已结） | NNPot 手册页 extract |
| 工具维护状态（MDTraj/PyEMMA） | **已落实但有两处瑕疵**（L319：MDTraj 维护模式/PyEMMA 停更/deeptime 活跃均已写入；①该段被插在**表 11-4 表体与 PLUMED 行之间**，把表 11-4 拆成两截、PLUMED 行成孤儿行，Markdown 渲染时不再属于任何表格；②维护状态断言「依据各项目官方仓库与发布线（以检索时点为准）」无任何引用锚点，PyEMMA/MDTraj 状态句未挂 [22][23][25] 或 GitHub 仓库 URL） | git diff fccd681..b38fd5c 确认为本轮引入 |

---

## 二、机械项实测（STYLE 三/五/九口径）

| 章 | 汉字数（≥10,000） | 文献条数（refs=章末，逐条 diff） | 编号首现 1..N | 表格 | 图 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 8 | **20,770** | 42 / 42，**完全一致** | 1..42 严格递增（含 [24,36] 组合展开） | 7 表 | 5 图（5 mermaid） | 围栏平衡；仅此章混用弯引号 38 处 vs 全书「」体例（见问题清单） |
| 9 | **14,813** | 40 / 40，**完全一致** | 1..40 严格递增 | 4 表 | 3 图（3 mermaid） | 无禁用表达、无第二人称 |
| 10 | **12,457** | 35 / 35，**完全一致** | 1..35 严格递增（含 [4-15] 区间展开） | 8 表 | 4 图（4 mermaid） | L67 存留「需要强调」套话 1 处（见问题清单） |
| 11 | **12,226** | 36 / 36，**完全一致** | 1..36 严格递增（含 [a,b] 组合展开） | 5 表（**其中表 11-4 被拆断**） | 3 图（3 mermaid） | 无禁用表达、无第二人称 |

检查方法：统计前剔除 ``` 围栏内容并截断「## 参考文献」之后；编号检查支持 [a-b] 区间与 [a,b] 组合展开、排除代码块内索引；refs 与章末逐条字符串 diff。

---

## 三、新引文抽查（各 2 条、每条六项，anysearch CLI）

| 引文 | 标题 | 作者 | 期刊/丛书 | 年 | 卷期页 | DOI | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 08 [13] | Good Practices in Free-Energy Calculations ✓ | Pohorille, Jarzynski, Chipot ✓ | J Phys Chem B ✓ | 2010 ✓ | 114(32): 10235-10253 ✓ | 10.1021/jp102971x ✓ | **六项全对**（Crossref API extract） |
| 08 [34] | From Metadynamics to Dynamics ✓ | Tiwary, Parrinello ✓ | Phys Rev Lett ✓ | 2013 ✓ | 111(23): 230602 ✓ | 10.1103/PhysRevLett.111.230602 ✓ | **六项全对**（Crossref API extract） |
| 09 [10] | Monte Carlo Methods in Statistical Mechanics: Foundations and New Algorithms ✓ | Sokal ✓ | NATO ASI Series B 361 / Springer（INSPIRE：NATO Sci.Ser.B 361 (1997) 131-192） ✓ | 1997 ✓ | 131-192 ✓ | 10.1007/978-1-4899-0319-8_6 ✓（Springer 章页 URL 与 DOI 一致） | **六项全对** |
| 09 [30] | Identification of slow molecular order parameters for Markov model construction ✓ | Pérez-Hernández, Paul, Giorgino, De Fabritiis, Noé ✓ | J Chem Phys ✓ | 2013 ✓ | 139(1): 015102 ✓ | 10.1063/1.4811489 ✓ | **六项全对**（Crossref API extract） |

---

## 四、问题清单（修订新增或残留，按级别）

**P1（修订后可过，共 3 条）**

1. **[10章·L272 新错误]** Snakemake 依赖判定订正句方向性错误：「它的依赖判定**默认采用修改时间戳比较**……用 --rerun-triggers mtime,input,params,code 等可把输入内容哈希与规则代码变化**纳入**触发条件」。官方 CLI 文档（9.27.1）明示 `--rerun-triggers {code,input,mtime,params,software-env}` **默认全部启用**（"By default, all triggers are used, which guarantees that results are consistent with the workflow code and configuration"），mtime-only 是需显式指定的传统回退方式；示例还遗漏 software-env 触发器。建议改述为：「Snakemake 默认同时依据 mtime、输入、参数与代码/软件环境触发重跑，保证结果与工作流代码及配置一致；如需退回仅按文件修改时间的传统判定，可用 --rerun-triggers mtime；--rerun-incomplete 处理中断留下的不完整输出」。
2. **[10章·L475 断头交叉引用]** CI 冒烟测试段「（--use-conda 环境锁定见 10.6 节）」：该段即位于 10.6.4，而全章并无 --use-conda 环境锁定内容（peer-10 B2 未实现）。删除该括注，或将 B2（--use-conda/--use-container + conda 环境导出/Apptainer）补入 10.4.4/10.7.2 后再引。
3. **[11章·L319–320 新格式缺陷]** 「维护状态与活跃度」段被插在表 11-4 的 deeptime 行与 PLUMED 行之间，表 11-4 被拆成两截、PLUMED 行（L320）成孤儿行，渲染时不属于任何表格。将该段移至表 11-4 之后（PLUMED 行后另起），或把 PLUMED 行移回表体末。

**P2（记录，统稿处理，共 7 条）**

1. **[8章·引文体例]** 第 8 章混用弯引号 38 处（全书其余各章一律「」），为 34282d6 修订引入；统稿时统一。
2. **[10章·L422 未落实残留]** peer-10 D4 两处未改：`--ntasks×--cpus-per-task ≈ -ntmpi×-ntomp` 仍混写 thread-MPI（单进程）与真 MPI（多进程）两种启动形态；「-gpu_id 可在多卡节点显指定映射」措辞仍偏松（官方语义为可用 GPU 设备过滤，任务→设备映射由 -gputasks 承担）。
3. **[10章·L67]** 「需要强调，自动化只消除程序性错误……」——套话式引导语残留；peer-09 同型表述已删，本句建议改为直陈句（非 STYLE 字面禁用词，故记 P2）。
4. **[10章·Ex 回填未执行]** peer-10 第四节的 Ex3/Ex4/Ex5/Ex6/Ex7 回填（参数矩阵→数组下标、复原清单、校验断言、情境化、发布归档）与 D1（mdrun 多产物成组目标/&:）、D7（.gitattributes/.gitignore 声明与 filter-repo 清理）均未落实。
5. **[11章·未结清 P2]** 11.1.2「高连通环结构」表述与 lincs-order「四阶即可达到 <0.0001」因果断句（peer-11 D2/P2-4 仍在）；11.2.4 Q2 并行决策案例未回填；L132（代码注释「gmxapi 0.5.x」）与 L187（「0.5.0a1[16]」）版本表述仍不一——GROMACS 2026.4 手册 gmxapi Python module reference 页首行明示 "Version 0.5.0a1"，而 PyPI 上 gmxapi 最新发行版为 0.4.2（无 0.5.x 公开发行），两处口径应统一为「0.5.0a1（手册对应版本）」。
6. **[11章·L319 无锚断言]** 「MDTraj 已进入维护模式、PyEMMA 积极开发已停止」等维护状态断言仅有「以检索时点为准」而无引用锚点（应挂 [23][25] 或各仓库 URL，并注明核查日期）。
7. **[11章·L457 表述]** 「（文档推定）」「（快速演进中）」标注纪律良好，但 metatomic 侧「官方文档的选项清单与示例文件在键名上存在不一致」属实（文档正文 metatomic-model vs 示例文件 metatomic-modelfile），可补一句实证定位以示非臆断。

**P0：无。** 未发现伪造/错配文献、字数不达标或编号断裂。

---

## 五、事实抽查与引文核验记录（anysearch CLI，2026-11-08）

**第 8 章（抽查 6 条，全部通过）**
1. couple-moltype「程序自动为该分子类型隐式构造 B 态并重定义 A 态」——manual Free energy implementation（2025.3/2026.x 同源）：原文 "Any molecule type selected in couple-moltype will automatically have a B state implicitly constructed (and the A state redefined)"。✓
2. couple-lambda0/1 语义与溶剂化方案 none→vdw-q——手册原文 "couple-lambda0 and couple-lambda1 define the non-bonded parameters that are present in the A state and the B state"；官方教程 "λ=0 means that the molecule is de-coupled, and λ=1 means that the molecule is fully coupled"；论坛实测 mdp（couple-lambda0=none, couple-lambda1=vdw-q）同构。✓
3. pV 修正 22 bar/−1 kJ·mol⁻¹ 与质量项 −(3/2)k_BT·ln(m_B/m_A)（无约束）——manual Free energy calculations 式 131 附近原文逐句吻合（"a correction to the Helmholtz free energy of just -1 kJ mol⁻¹"；"the integrated contribution…−(3/2)kBT ln(mB/mA)…only true in the absence of constraints"）。✓
4. gmx bar 输出与诊断——gmx bar 页原文：输出表含 lam_A/lam_B/DG/s_A/s_B/stdev；s_A/s_B 为相对熵、"goes to zero for identical distributions"、引 Wu & Kofke 2005（123 084109）；"automatically adds series of individual free energies…into a combined free energy estimate"；分块误差按 5 块平均方差、-nbmin/-nbmax 扫描、-prec 默认 2。✓
5. gmx analyze -ac/-subav/-acflen/-fitfn exp_exp/-luzar——页原文：-subav 先减均值（默认 yes）、-acflen 默认半帧数、-fitfn 含 exp/exp_exp、-luzar 对 gmx hbond(-legacy) -ac 输出做 Luzar–Chandler 分析、-temp 默认 298.15、-fitstart/-fitend 默认 1/60。✓（注：手册该处原文写 gmx hbond；2026.4 的新 gmx hbond 选项表仅含 -num/-dist/-ang/-dan，并无 -ac，-ac 输出实际只存在于 hbond-legacy——正文「gmx hbond(-legacy)」的写法是恰当的兼容表述）
6. sc-* 语义与 0.3 nm——mdp 文档与论坛实测 mdp（sc-alpha=0.5、sc-power=1、sc-sigma=0.3、sc-coul、calc-lambda-neighbors=1、nstdhdl）逐项对位。✓

**第 9 章（抽查 6 条，全部通过）**
1. pymbar.timeseries——官方文档 extract：模块页首 "The MBAR method is only applicable to uncorrelated samples…so we provide a number of tools…to decorrelate simulation data"；detect_equilibration 返回 t0/g/Neff_max；statistical_inefficiency/integrated_autocorrelation_time/subsample_correlated_data 均在。✓
2. gmx analyze -ee 双指数拟合出处——页原文："B. Hess, J. Chem. Phys. 116:209-217, 2002"，与 [14]（Hess 2002, JCP 116(1): 209-217）一致。✓
3. Yeh–Hummer——原文摘要系数 2.837297（D0 = DPBC + 2.837297·kBT/(6πηL)），正文 ξ≈2.837 合规；[35] 元数据（JPCB 2004, 108: 15873-15879, DOI 10.1021/jp0477147）经 Crossref 核实。✓
4. [28] Gapsys & de Groot——eLife 2020, 9: e57589，DOI 10.7554/eLife.57589，多仓储一致。✓（peer-09 曾未能 extract 的条目现可核）
5. 手册式 469——covariance-analysis 页式 469 为 s(A,B)=1−d(A,B)/√(trA+trB)（协方差平方根采样重叠），与 [23]（Lyman–Zuckerman 主成分子空间）确为两个不同度量；「第一主成分近似半余弦、第二近似全余弦」判句与「两半须用同一参考结构」均出自该页。✓
6. Sokal 1997/tICA 2013——见「三、新引文抽查」。✓

**第 10 章（抽查 4 条，3 过 1 不过）**
1. Managing long simulations——convert-tpr -extend/-cpi、grompp -t state.cpt、-noappend 与 .partXXXX、_prev 副本、输出追加受检查点校验和保护、续算时不应重生成速度并应设 continuation、续算逐位一致条件——页原文全部对位。✓
2. sbatch 格式串 %A_%a 与 --test-only——SchedMD 文档语义（前轮 peer-10 已 fetch，本轮沿核）；三处正文一致。✓
3. 规则级 Slurm 提交——Snakemake CLI 文档（profile 示例 executor: slurm、非本地执行经 executor 插件、threads/resources 覆盖接口）与插件生态对位。✓
4. **Snakemake rerun-triggers 默认语义——不通过**（见 P1-1）。✗

**第 11 章（抽查 5 条，全部通过）**
1. NNPot 手册——"atomic descriptors…atom positions and atomic numbers"、PyTorch/TorchScript-only、LibTorch 版本须一致、模型输入无默认值按 mdp 顺序传递、无力则按第一输入张量求梯度、GMX_NN_DEVICE cpu/gpu（cuda 弃用视为 gpu）、多 GPU 设备继承 mdrun、CUDA/HIP-aware LibTorch、ANI-2x 单位换算与 torch.jit.script 导出、ML/MM 能项删除/2FD link atom/electrostatic-model 双侧力——逐句对位。✓
2. metatomic GROMACS 引擎——独立 fork、conda gromacs-metatomic（-c metatensor -c conda-forge，nompi/openmpi/mpich、单/双精度、CPU/CUDA 变体）、源码依赖 metatensor(-torch)/metatomic-torch/LibTorch 与 GMX_METATOMIC=AUTO、mdp 选项 metatomic-active/input-group/model/device、能量/非保守力/应力输出——逐项对位；「选项清单与示例键名不一致」属实（metatomic-model vs metatomic-modelfile）。✓
3. gmxapi 安装与系综——GMXAPI MPI 工具链与 mpi4py 要求、has_feature("mpi_bindings")、mpiexec -n 2 `which python` -m mpi4py、filtered_mpi_environ、Issue 3718——usage 页原文对位；「自 GROMACS 2019 起官方支持、当前版本默认启用」与 Irrgang 2022 PLoS 全文一致。✓
4. gmxapi 版本——2026.4 手册 pythonreference 页首行 "Version 0.5.0a1"（L187 断言成立）；PyPI 最新发行 0.4.2（L132「0.5.x」不成立）→ 记入 P2-5。✓
5. deeptime 文献——[27] ML:Sci&Tech 2022, 3(1): 015009, DOI 10.1088/2632-2153/ac3de0（refs 括注记录的纠错与 IOP/Crossref 记录一致，沿用）。✓

---

## 六、结论

- **08：pass**（6 项重点核查全部落实，抽查 0 事实错误；P2 引文体例 1 项）
- **09：pass**（6 项全部落实，抽查 0 事实错误；无遗留）
- **10：pass（带 2 项 P1 待订正）**（重点核查 5 项中 4 项落实；Snakemake 订正句引入方向性新错误 + CI 段断头引用；D4/Ex 回填等 P2 残留）
- **11：pass（带 1 项 P1 待订正）**（ML 势 UQ/描述符/维护状态落实；表 11-4 被新增段拆断；gmxapi 版本两处不一与 LINCS 表述等 P2 未结清）

四章机械项（字数、结构、编号、refs 一致、禁用表达、图表计数）全部达标；新引文抽查 4 条与事实抽查 21 条中仅第 10 章 Snakemake 默认触发器一条不过。建议先行处理三处 P1（第 10 章两处、第 11 章一处），P2 统稿处理。

*报告完。全程未调用 web_search；所有外部核验经 anysearch CLI（search/extract/batch_search），时间 2026-11-08。*
