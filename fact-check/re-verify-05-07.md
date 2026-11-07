# 第 5、6、7 章「面向同行」修订后对抗性复核验收报告（re-verify）

- 复核日期：**2026-11-07**
- 复核立场：独立验收者（科研同行视角），对 peer-05/06/07-review（v2，2026-11-04）提出的修订进行落实复核，并对修订后新内容做对抗性抽查
- 复核对象（修订后当前版本）：
  - `05-能量最小化与平衡.md`（359 行）
  - `06-运行、性能与故障诊断.md`（381 行）
  - `07-常规轨迹分析.md`（456 行）
- 依据文件：fact-check/peer-05-review.md、peer-06-review.md、peer-07-review.md；fact-check/修改意见书-面向同行-20261104.md；refs/05-refs.md、refs/06-refs.md、refs/07-refs.md；STYLE.md（含 2026-11 修订：「## 习题」全书自 2026-11 起以「## 延伸讨论」取代）；fact-check/07-log.md
- 核验通道说明：本会话联网通道仅 **anysearch CLI**（`D:\CharlieAPP\C_Python\python.exe … anysearch_cli.py`），实际使用 search×15、extract×8（含 current mdp-options、current mdrun-performance、2020.4 mdrun-performance、mdtraj.rmsd/compute_rg API 页等），未调用 web_search 工具。凡由该通道核验的条目均标注「anysearch 核验」。未在本机实测 2026.4 工具的条目一律注明「需目标机实测」。
- 判定口径：**重点核查 1 的清单逐项对位**；新内容抽查每章 3–5 条（事实性、无新错）；机械项（汉字数、编号首现递增、refs 一致、禁用表达）全量检查；遗留项按 P0/P1/P2 列出。

---

## 〇、判定速览

| 章 | 判定 | 一句话结论 |
| --- | --- | --- |
| 05 | **pass** | 五项重点修订全部落实且经官方原文复核无新错；仅表 5-4 的 gen_* 三行出处列未同步改 [10]（P2）及若干 peer-05 P2 低强度注记未落 |
| 06 | **pass** | 周期表语义化、-pin、守恒量刻度、-rcon、mts 适用范围五项全部落实并经 2026.4 性能指南原文复核；PME GPU 分解注记、GPU OOM/tpr 版本、E 类回填与三处 P2 教学腔未落 |
| 07 | **pass（带两处小改要求）** | RMSF 叠合修正、氢键寿命机理、Laage–Hynes 入库、文献重排全部落实且抽查通过；但 **refs/07-refs.md 未随重排同步（与章末列表编号冲突）**、**Laage 期号 5760 应为 5762**，两处须在入库前修正 |

---

## 一、第 5 章 能量最小化与平衡

### 1.1 修订落实对位（重点核查 1）

| 修订项 | 落实判定 | 落位 |
| --- | --- | --- |
| 双种子纪律（gen_seed/ld_seed） | **已落实** | 5.4.2 下新增「#### 双种子纪律与多副本分配」：明确 gen_seed 管初速、ld_seed 管 v-rescale/Langevin 热浴随机流，给出三副本最小方案（gen_seed=1000+k、ld_seed=2000+k）、并行划分对随机流的影响（ld-seed+秩语义）、统计复现目标；常见错误 6 与小结同步 |
| L-BFGS | **已落实** | 5.2.2 下新增「#### L-BFGS 与高阶收敛」：integrator=l-bfgs、nbfgscorr（默认 10）、**未并行化（单秩）**、与 cg 的 tier 取舍、双精度路径指向第 2 章 2.6.2；常见错误 2 与小结同步 |
| NH 链长积分器依赖 | **已落实** | 5.5.4 改为「默认 10 仅对 velocity Verlet（integrator=md-vv）生效；leap-frog（integrator=md）只支持链长为 1」，并保留 NH tau_t=涨落周期语义；表 5-1 NH 行加「小体系结合链式扩展」注 |
| DispCorr 评注 | **已落实** | 5.7.2 下新增「#### DispCorr 对压力的系统性修正」：Ener 只修正能量、EnerPres 同时修正能量与压力、开启与否均值差数十至上百 bar（经验量级已标注）、跨设置比较须统一口径；并列为压力判据前置检查 |
| gen_vel 出处改 [10] | **已落实（正文）/部分（表 5-4）** | 5.4.1 改标 grompp 联机帮助 [10]，并加版本披露（该组选项 2026.x 起不见于 mdp 选项页、功能仍生效）；**但表 5-4 的 gen_vel/gen_temp/gen_seed 三行出处列仍标 [2]，与表注「默认值据官方选项页[2]」**——正文披露与表格出处不同步 |

### 1.2 新内容事实抽查（anysearch 核验）

1. **l-bfgs / nbfgscorr / 未并行化**：2026.4 mdp-options extract 原文「A quasi-Newtonian algorithm for energy minimization according to the low-memory Broyden-Fletcher-Goldfarb-Shanno approach. In practice this seems to converge faster than Conjugate Gradients, but due to the correction steps necessary it is not (yet) parallelized.」；`nbfgscorr` (10)「Number of correction steps to use for L-BFGS minimization」——与正文一致。正文「控 L-BFGS 保存的校正对数目」系「correction steps」的通俗化表述，可接受但以官方措辞为准更稳（P2 备注）。
2. **gen-vel 族从 mdp 选项页撤出**：current mdp-options extract 全文搜索 gen-vel/gen-temp/gen-seed 均 0 命中——正文「文档主条目在 grompp 联机帮助而非 mdp 选项页」的披露与出处改标 **属实且必要**。
3. **NH 链长 leap-frog 限制**：官方语境「Leap-frog integrator only supports 1, but by default, this is 10」（教程/论坛一致可见）——正文表述一致。
4. **DispCorr 取值语义**：官方「EnerPres: apply long-range dispersion corrections for Energy and Pressure；Ener: …for Energy only」——正文一致；「数十至上百 bar」已按 STYLE 标注经验性质。
5. **C-rescale 与水压缩率**：Bernetti–Bussi 2020（JCP 153(11):114107，anysearch 复核）与官方语境「stochastic cell rescaling barostat …can be used for both the equilibration and production」「less sensitive to the step size」一致；水 4.5×10⁻⁵ bar⁻¹（官方值，peer-05 已核）一致。

### 1.3 遗留问题（本报告登记）

- **P2｜表 5-4 出处列不同步**：gen_vel/gen_temp/gen_seed 三行出处仍 [2]（表注亦为「据官方选项页[2]」），而 mdp 选项页已不收录该组（本轮 extract 证实）。应改 [10] 或在表注加「gen_* 例外，见 grompp 帮助」。这是 peer-05 D2/P1 修订在表格侧的残余。
- **P2｜peer-05 未落实的低强度注记**（原属「可并入行动 7」）：①5.8.2 未补「vdw 截断误差 > PME 静电力误差（官方 0.15 nm 提示）」与 Verlet 压力容差 0.5 bar（对应水密度 2e-5）；②5.5.3 动能涨落检验未给 2/(3N) 判据或改述（P4 未改，原句仍在）；③时间尺度分离仅以一句综述性文字（5.7.3）承载，未成表或可操作链；④AlphaFold 起点、Andersen/annealing、有限尺寸效应等一句式注记未落。**均属可选补强，不阻断 pass。**
- 机械项通过：汉字 13,658（STYLE 口径实测）；## 二级 12、### 三级 26；表 4、图 3；常见错误 7；参考文献 32 条，编号 1..32 首现严格递增、refs/05-refs.md 与章末列表逐条一致；禁用表达与第二人称 0 命中。
- 结构性事项（跨章统一）：STYLE/REVIEW 现要求每章「## 延伸讨论」≥3 段（2026-11 起取代习题）、OUTLINE 5.10/6.10/7.10 已改为「延伸讨论」，**但三章正文均无「## 延伸讨论」节**；OUTLINE 仍缺正文已有的 5.4.3（质心运动与温度定义）与 5.8.4（mdp 模板）两个三级节。回填内容（双种子纪律、DispCorr 评注）以 #### 评注形态落进正文，尚未组装为该构件。属全书统稿级待办，不阻断本章 pass，但须在统稿轮闭环。

---

## 二、第 6 章 运行、性能与故障诊断

### 2.1 修订落实对位（重点核查 1）

| 修订项 | 落实判定 | 落位 |
| --- | --- | --- |
| 周期表行名改语义环节（无 Comp 编号依赖） | **已落实** | 6.3.3 重写：行名随版本而变、以本机 md.log 为准，老版本（约 2021 及以前）Comp 1–N、新版本（2023/2024 起）语义化行名，并明确「瓶颈识别与处置按语义环节处理…不依赖具体行名编号」；6.5.2 决策与图 6-2 全部用 PME mesh/Nonbonded（Wait GPU NB local）/Search（DD comm）/Comm. energies 语义节点，决策树中无 Comp 编号 |
| -pin 绑核 | **已落实** | 6.4.2 新增整段：auto/on/inherit/off 四值语义、-pinstride/-pinoffset 多实例错开、共享节点与外部亲和情形、OMP_PROC_BIND/OMP_PLACES 与第 2 章 2.5 呼应、SMT 一句 |
| 守恒量判据刻度 | **已落实** | 6.3.1 新增「三样东西」段：读取位置（Statistics 块 Conserved En. / gmx energy 区间差）、量级刻度（蛋白-水 2 fs 下数 kJ·mol⁻¹、与动能涨落同量级，明确标「教材共识刻度，严格值应按体系实测校准」）、leap-frog 下 Total Energy 非严格守恒量的半步错位机理 |
| -rcon | **已落实** | 6.4.1 新增：-rcon 影响元胞尺寸下限的约束部分、必要时减小 LINCS order 并增加迭代次数；6.8.3 案例四呼应 |
| mts 适用范围（附加落实） | **已落实** | 6.3.3 补「该特性仅在使用 CPU 积分路径（-update cpu）时可用」 |

### 2.2 新内容事实抽查（anysearch 核验）

1. **mts 仅 CPU 积分路径**：2026.4 mdrun-performance extract 原文「When running on CPUs only or with GPUs but integration on the CPU, you can use multiple time stepping to perform the PME mesh calculations every second step: set `mts` to `yes`」——正文一致（anysearch 核验）。
2. **Wait GPU NB local 与 nstlist 刻度**：extract 原文「this time will show up as `Wait GPU NB local` in the cycle and timing summary table」、「nstlist=200-300 with PME and default Verlet buffer tolerance」「odd values of nstlist should be avoided when using CUDA Graphs」——正文一致（anysearch 核验）。
3. **-pin 家族语义**：extract 原文 auto/on/inherit/off 与 -pinoffset/-pinstride 的语义（含「overriding any external CPU affinity settings」「within the external affinity mask」）——正文大体一致。**一处措辞偏强**：正文「节点共享或调度器已设置亲和时…自动钉可能失效**或与调度器掩码冲突**」——官方 auto 的行为是**不**去钉（而非与之冲突）；建议改「自动钉不生效（不改变外部掩码）」（P2 措辞级）。
4. **-rcon**：extract 原文「option -rcon influences the cell size limit as well. Particles connected by NC constraints, where NC is the LINCS order plus 1, should not be beyond the smallest cell size… decrease the LINCS order and increase the number of LINCS iterations」——正文一致（anysearch 核验）。
5. **守恒量刻度**：「数 kJ·mol⁻¹ 量级」已显式标注教材共识并要求按体系实测校准——符合 STYLE 三.5 与五.4 的不确定性纪律，无新错。

### 2.3 遗留问题（本报告登记）

- **P1｜PME GPU 分解边界注记未落**（peer-06 priorityAction 2 前半）：6.4.3/6.4.4 仍只写「-pme gpu 须 -npme 1」，未补「GMX_GPU_PME_DECOMPOSITION 构建（cuFFTMp/heFFTe）开启后多 PME 秩可上卡、默认构建仍须单秩」的 2026 基线边界。属「正确但过时」表述，修订轮未闭环。
- **P1｜GPU OOM 与 tpr 版本不匹配未补**（peer-06 priorityAction 5、B1/B5）：6.8.3 案例与常见错误清单（仍 7 条）均未收录这两个高频失败模式。
- **P1｜E 类回填未做**（peer-06 priorityAction 6/7）：6.2.3 无「生产-续算最小闭环」与三种续算对比表（表 6-6 不存在）、6.6.4 无失稳报告 8 字段模板、6.5.1/6.5.2 无口径陷阱注记与基准测量协议；grep 确认上述构件均未出现。
- **P2｜三处教学腔未改**：L67「有一句需要牢记的告诫」、L85「开机后若目标输出文件已存在」、L206「出路是增加 PME 秩数…」——peer-06 P1/P2 建议原样未动。
- **P2｜导言[6-10] 范围欠准**：L5「方法学来源（LINCS、PME、GPU 异构并行）引原始文献[6-10]」中 [6] 为 2020 版 release notes 而非 LINCS 原始文献，宜收窄为 [7-10] 或改述。
- 机械项通过：汉字 13,197；二级 12、三级 26；表 5、图 3；常见错误 7；参考文献 32 条，编号 1..32 首现严格递增，refs/06-refs.md 与章末列表一致；禁用表达与第二人称 0 命中（L77「值得读者熟悉」为叙述层，非学习目标，不属禁用）。

---

## 三、第 7 章 常规轨迹分析

### 3.1 修订落实对位（重点核查 1）

| 修订项 | 落实判定 | 落位 |
| --- | --- | --- |
| RMSF 示例含 AlignTraj | **已落实** | 7.7.1 示例改为先 `align.AlignTraj(u, u, select="name CA", in_memory=True).run()` 再 `RMSF(ca).run()`，注释明示「RMSF 默认不做任何拟合…整体转动/平动会系统性抬高涨落」；段末另立一段披露「No mass weighting is performed」与 gmx rmsf 质量加权口径差异 |
| 氢键寿命机理深化 | **已落实（幅度略低于建议）** | 7.4.3 新增：连续/间歇两种寿命定义与物理图像差异、指数拟合（-fitfn exp/exp_exp）与自相关积分 τ=∫C(t)dt 两种提取路径、-fitstart/-fitend 窗口语义、粗粒化寿命警示与输出频率纪律；Luzar–Chandler「断裂-重形成」稳态图像一句接入。C(t)=⟨h(0)h(t)⟩/⟨h⟩ 显式公式与 LC 四速率(k1/k−1/kf/kd)参数表未给 |
| Laage–Hynes 入库 | **已落实** | 入库为章内 [25]（7.4.3 机理句「进一步区分了氢键断裂与分子重取向的耦合机制」），并接入 7.5.3 语境的水动力学关联；卷期页抽查见 3.2 第 5 条（期号一处须改） |
| 文献编号按首现重排 | **已落实（章内）** | 章末 40 条 [1]–[40]，编号 1..40 首现严格递增（自动检查通过、无跳号重号悬空）；**refs/07-refs.md 未同步（见 3.3 P1）** |

### 3.2 新内容事实抽查（anysearch 核验）

1. **AlignTraj 用法**：MDAnalysis 官方用户指南示例「aligner = align.AlignTraj(mobile, ref, select='name CA', in_memory=True).run()」与新版示例逐字同构（anysearch 核验）——操作级修正正确。
2. **MDTraj API 签名**：`md.rmsd(target, reference, frame=0, atom_indices=None, …)`（1.9.4 文档 extract）与 `md.compute_rg(traj, masses=None)`（1.9.4 文档 extract，等质量约定）——7.7.2 示例合法；正文未声称 MDTraj Rg 为质量加权，无误。
3. **MDAnalysis RMSF 默认不叠合、无质量加权**：与官方 docstring 一致（peer-07 extract 与章内引述吻合）——新代码不再与正文/常见错误 #2 矛盾，本轮最重要的操作级修正成立。
4. **analysis.waterdynamics 未引入**：正文仍写「分析模块覆盖本章全部指标」而未列 waterdynamics（peer-07 B1 建议未落实）。经查 MDAnalysis 2.8.0 发行说明，analysis.waterdynamics 已标记 deprecated（移至独立 mdakit，v3.0 移除）——未来补此工具时**必须带版本注**；现状是「少写」而非「错写」。
5. **Laage & Hynes 2006 六项抽查**：题名「A Molecular Jump Mechanism of Water Reorientation」、作者 Damien Laage/James T. Hynes、期刊 Science、年份 2006（2 月 10 日）、卷 311、页 832–835、DOI 10.1126/science.1122154——**六项中一项不符：期号应 5762（PubMed 16439623：「Science. 2006 Feb 10;311(5762):832-5」、ResearchGate 同），正文与 refs/07-refs.md 均写 5760**。属新引文的卷期页小错，P1 级、一行可修。

### 3.3 遗留问题（本报告登记）

- **P1｜refs/07-refs.md 与章末列表编号冲突**（STYLE 五.4 硬性要求）：refs/07-refs.md 仍是重排前旧编号（如 [3]=make_ndx、[27]=Allen & Tildesley、[39]=Barlow–Thorton、[40]=Laage–Hynes；其注记仍引用旧编号语境），而章内已重排为 [3]=density、[31]=Allen & Tildesley、[27]=Barlow–Thorton、[25]=Laage–Hynes。两份清单当前**互斥**，任何按 refs 文件复核的第三方都会对不上。须以章末 40 条为准同步重写 refs/07-refs.md（含其顶部注记）。fact-check/07-log.md 的修订记录也未登记本轮重排与 Laage 入库。
- **P1｜Laage 期号 5760→5762**（正文 [25] 与 refs 两处，见 3.2 第 5 条）。
- **P2｜peer-07 未落实项**：①7.7.3 口径差异清单仍四项，未补「叠加缺失/叠加算法（Kabsch/QCP 数值等价）」第五项（RMSF 不叠合已在 7.7.1 显式化，算部分落实）；②7.1.3「平衡后的结构指标只需纳秒级稀疏抽样即可收敛」未按 D7 边界化移交 9.3/9.4；③7.5.3 生存概率 S(τ) 定义、壳层驻留数量级与 MDAnalysis waterdynamics/SurvivalProbability 工具落点未补；④SASA 半径集量化与 BSA 差分配方（D4）、gyrate 回转张量与膜体系决策（D5）、RDF ρ0/-cn 口径限定（D6）、dssp -hbond 默认 energy 与 -polypro 开关（D8）均未落；⑤L26「需要强调的是」、L376「本章只强调一点」与 L370 图 7-3 图注连写（「…采信任一侧结果一致性校验脚本…」仍缺句号）三处文本小件原样未动；⑥图 7-3 与 7.7.3 正文仍写「四类口径差异」，与 7.7.1 新增的「质量加权/叠合」差异项不同步。
- 机械项通过：汉字 10,791（≥10,000）；二级 12、三级 27；表 4、图 3；常见错误 8；参考文献 40 条；编号首现严格递增；禁用表达与第二人称 0 命中。

---

## 四、机械项汇总（实测口径）

| 项 | 05 | 06 | 07 | 结果 |
| --- | --- | --- | --- | --- |
| 汉字数（去代码块、截参考文献，STYLE 三.2 范式） | 13,658 | 13,197 | 10,791 | 全部 ≥10,000 ✅ |
| 二级节（含学习目标/前置/常见错误/小结/参考文献） | 12 | 12 | 12 | 正文 8 + 4 尾部构件，≥8 ✅ |
| 三级节 | 26 | 26 | 27 | ≥25 ✅ |
| 参考文献 | 32 | 32 | 40 | ≥30 ✅ |
| 编号首现递增（范围展开、脚本自动检查） | ✅ | ✅ | ✅ | 三章均无跳号、重号、悬空引用 ✅ |
| refs/ 目录一致性 | ✅ 与章末一致 | ✅ 与章末一致 | ❌ **未同步（旧编号清单）** | 第 7 章须修 |
| 禁用表达/套话/第二人称「你」 | 0 | 0（3 处 P2 教学腔） | 0（2 处 P2 教学腔 + 图注连写） | ✅（P2 级语言残留） |
| 表/图/常见错误 | 4 表 3 图 7 错 | 5 表 3 图 7 错 | 4 表 3 图 8 错 | ✅ |

（注：第 7 章 [25] Laage 条目期号一处为事实性小错，不计入机械项，列于 3.3。）

---

## 五、问题清单（按优先级）

1. **[P1] 07：refs/07-refs.md 未随文献重排同步**，与章末列表编号冲突（含其顶部注记与 07-log 修订记录）。修法：以章末 40 条为准整份重写，顶部注记同步更新。
2. **[P1] 07：Laage & Hynes 2006 期号 5760 应为 5762**（正文 [25] 与 refs 两处）。
3. **[P1] 06：PME GPU 分解（GMX_GPU_PME_DECOMPOSITION）边界注记未加**；GPU OOM 与 tpr 版本不匹配两类高频失败未补入 6.8.3/常见错误；E1/E2/E6/E7 回填（续算闭环、三种续算对比表、失稳报告模板、口径陷阱与基准协议）未做。
4. **[P2] 05：表 5-4 gen_* 三行出处仍标 [2] 应改 [10] 或加注**；L-BFGS「校正对数目」措辞宜贴官方「correction steps」；2/(3N) 判据、0.5 bar 压力容差、0.15 nm 误差排序、Andersen/annealing 等注记未落。
5. **[P2] 06：-pin auto 情形「与调度器掩码冲突」措辞偏强**（官方 auto 的行为是不钉、不冲突）；L67/L85/L206 三处教学腔；导言 [6-10] 范围收窄。
6. **[P2] 07：7.7.3 第五项口径差异（叠加缺失/叠加算法）未补**；7.1.3 稀疏抽样断言未边界化；7.5.3 生存概率与 waterdynamics 工具未补（补时须带 2.8+ deprecation 版本注）；D4/D5/D6/D8 机理项未落；L26/L376 与 L370 图注连写三处小件。
7. **[跨章] 「## 延伸讨论」构件缺失**：STYLE/REVIEW 已改定、OUTLINE 5.10/6.10/7.10 已登记为延伸讨论，但三章正文均无该节（回填内容以 #### 评注形态散落正文）；OUTLINE 仍缺 5.4.3、5.8.4 两个正文已有三级节。建议统稿轮一次性组装并登记，避免「有约定而无载体」。

---

## 六、总结

三份 peer review 的重点核查项（第 5 章五项、第 6 章五项、第 7 章三项）**在正文层面全部真实落实**，且经 current mdp-options、current/2020.4 mdrun-performance、MDAnalysis/MDTraj 官方 API 与 PubMed 等 anysearch 通道抽查，**修订引入的新内容未发现新的事实错误**（唯 Laage 期号一处卷期页小错）；机械项全数达标。真正的未闭环集中在三处：refs/07-refs.md 未随重排同步（硬性一致性问题）、第 7 章期号 5760→5762、以及两章 P1 级补强项（第 6 章 PME 分解注记/GPU OOM/tpr 版本/E 类回填）与跨章「延伸讨论」构件的组装——这些均属修订收口而非事实错误，修正后三章可交付终验。

---

*本报告仅写入 `fact-check/re-verify-05-07.md`（2026-11-07），未修改任何正文文件。联网通道仅 anysearch CLI（search×15、extract×8）；所有抽查条目均可按本报告落位复查。*
