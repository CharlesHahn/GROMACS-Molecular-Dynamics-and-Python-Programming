# 第 5 章 核查日志（fact-check）

> 每条记录一行关键论断。状态三档：已核实（原文可见，含检索结果原文/官方文档正文）、文档推定（官方文档明示但未在本机实测，正文须标注）、待核实（不得进入终稿）。本章无「待核实」条目。

| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| emtol 默认 10.0 kJ·mol⁻¹·nm⁻¹（最大力阈值）、emstep 默认 0.01 nm、nsteps 默认 0（最大步数，-1 为不限）；最小化须显式设置 nsteps | A：GROMACS 2026.4 mdp-options 页（manual.gromacs.org/current/user-guide/mdp-options.html） | extract 原文 | 已核实 |
| integrator=steep 语义「最大步长 emstep、容差 emtol」；cg 语义「容差 emtol、nstcgsteep 控制插入 SD 步（默认 1000）、简正模前需双精度」；l-bfgs 快于 CG 但未并行化 | A：mdp-options（integrator 各选项说明） | extract 原文 | 已核实 |
| 默认积分器 md（leap-frog）；dt 默认 0.001 ps；速度 Verlet（md-vv）亦可用 | A：mdp-options；reference-manual algorithms/molecular-dynamics | extract 原文 | 已核实 |
| cutoff-scheme 默认（列表首项）Verlet；group 方案在 2026.4 文档中标注「no longer supported」 | A：mdp-options（cutoff-scheme 项） | extract 原文 | 已核实 |
| coulombtype 默认 Cut-off（列表首项），PME 须显式写出；rcoulomb/rvdw 默认 1.0 nm；fourierspacing=0.12、pme-order=4、ewald-rtol=1e-5 | A：mdp-options（electrostatics/VdW/Ewald 节） | extract 原文 | 已核实 |
| verlet-buffer-tolerance 默认 0.005 kJ·mol⁻¹·ps⁻¹；无动力学（最小化）时缓冲为截断的 5%；rlist 在动力学下由缓冲容差自动确定 | A：mdp-options（verlet-buffer-tolerance、rlist 项） | extract 原文 | 已核实 |
| gen_vel 默认 no；gen_temp 默认 300 K；gen_seed 默认 -1（grompp 自动伪随机种子）；gen_vel 仅对 integrator=md 有意义 | A：mdp-options（velocity generation 节） | extract+检索原文 | 已核实 |
| 初速按麦克斯韦–玻尔兹曼分布生成：12 个 [0,1) 均匀随机数求和减 6 近似正态，乘以 √(kT/m_i)；扣除质心速度后整体缩放使动能精确对应目标温度 | A：reference-manual algorithms/molecular-dynamics（2026.4） | extract 原文 | 已核实 |
| 温度定义：½N_df kT=E_kin，N_df=3N−N_c−N_com（周期性体系 N_com=3）；质心速度通常每步置零 | A：reference-manual molecular-dynamics；mdp-options（nstcomm=100、comm-mode Linear） | extract 原文 | 已核实 |
| 压力张量 P=2/V(E_kin−Ξ)，标量压力 P=tr(P)/3 | A：reference-manual molecular-dynamics | extract 原文 | 已核实 |
| sd（朗之万随机动力学）作为恒温器：tau_t=2 ps 为官方建议、温度偏差衰减约两倍于同 tau_t 的 Berendsen、随机种子由 ld_seed 控制 | A：mdp-options（integrator=sd 项） | extract 原文 | 已核实 |
| SHAKE 不能用于能量最小化（官方文档明示）；constraint-algorithm 默认 LINCS；lincs-order=4、lincs-iter=1、shake-tol=0.0001、lincs-warnangle=30 | A：mdp-options（constraints/constraint-algorithm 节） | extract+检索原文 | 已核实 |
| constraints 默认 none；h-bonds 转换含氢键为约束；LINCS 用于含氢键与多数键约束，P-LINCS 为并行版本 | A：mdp-options；B：Hess 1997（JCC 18:1463）、Hess 2008（JCTC 4:116） | extract+检索元数据 | 已核实 |
| SETTLE 以解析方法刚性固定水分子（SPC/E、TIP3P 等） | B：Miyamoto & Kollman 1992（JCC 13:952） | 检索参考文献表原文 | 已核实 |
| mass-repartition-factor=3 配合 constraints=h-bonds 通常可将步长提升至 4 fs | A：mdp-options（mass-repartition-factor 项） | extract 原文 | 已核实 |
| nstxout/nstvout/nstfout/nstxout-compressed 默认 0（默认不写轨迹）；nstlog/nstenergy 默认 1000；能量文件存储 nstcalcenergy 区间精确和与涨落 | A：mdp-options（output control 节） | extract 原文 | 已核实 |
| GROMACS 2023 版提高 nstpcouple 默认值；2025.4 起 C-rescale 强制每周期≥25 步（tau_p 与 dt 之比）、P–R 强制每周期≥200 步；C-rescale 推荐 tau_p≥5 ps | A：release-notes/2025/2025.4.html（2026.4 文档） | extract 原文 | 已核实 |
| gen_seed=-1 时 grompp 自动生成种子；AMD Ryzen 3000 系列 RDRAND 故障可使自动种子退化为相同值、多副本同构，官方对策为显式设定种子 | A：release-notes/2020/2020.4.html | extract 原文 | 已核实 |
| grompp 在 gen_vel=yes 时不使用轨迹读入的速度（速度来自生成的麦克斯韦分布） | A：onlinehelp/gmx-grompp | 检索原文片段 | 已核实 |
| 官方工作流（getting-started → flow.html）为文件管线 pdb2gmx→editconf→solvate→grompp→mdrun（EM or MD）→analysis，未绘制独立 equilibrate 阶段；「EM→NVT→NPT→production」为教程组织惯例（正文已按此归因 [5]，最小化在动力学之前的次序归因 [1]） | A：GROMACS 2026.4 getting-started/flow.html；C：Lemkul 教程 | extract 原文（flow.html 流程图正文） | 已核实 |
| Berendsen 弱耦合方程 dT/dt=(T_ref−T)/τ 与速度缩放因子；温度与压力弱耦合原始文献 | B：Berendsen et al. 1984，J. Chem. Phys. 81(8): 3684-3690，DOI 10.1063/1.448118 | 检索多源 + DOI 解析 | 已核实 |
| v-rescale（CSVR）在保留缩放稳健性的同时采样正则系综并存在守恒量（Bussi 2007） | B：Bussi, Donadio, Parrinello，JCP 126(1): 014101，DOI 10.1063/1.2408420 | 检索原文/PubMed 摘要 + DOI 解析 | 已核实 |
| Berendsen 恒温器与简单速度缩放抑制涨落、破坏等配分（flying ice cube），CSVR 满足细致平衡；不可用于生产采样 | B：Braun, Moosavi, Smit，JCTC 14(10):5262-5272，2018，DOI 10.1021/acs.jctc.8b00446；预印本 arXiv:1805.02295（2018） | anysearch 学术域元数据 + 检索摘要 | 已核实（正文年份改为 2018，双出处已注明） |
| Berendsen 控压一阶弛豫高效但体积涨落不正确；C-rescale 引入噪声项恢复正确体积涨落，可兼用于平衡与生产 | B：Bernetti & Bussi 2020，JCP 153(11): 114107，DOI 10.1063/5.0020514 | PubMed 摘要原文 + DOI 解析 | 已核实 |
| Parrinello–Rahman 一般单元（triclinic）恒定压力方法；MTTK 扩展系综可逆积分器为其实现基础 | B：JAP 52(12): 7182（1981）；Mol. Phys. 87(5): 1117（1996） | 检索多源元数据 | 已核实 |
| Nosé–Hoover 恒温器（扩展变量）；tau_t 控制温度涨落周期而非弛豫；NH 链缓解遍历性不足；守恒量写入日志 | B：Nosé 1984（Mol. Phys. 52:255）、Hoover 1985（PRA 31:1695）、Martyna 1992（JCP 97:2635）；A：mdp-options | 检索 + extract | 已核实 |
| 教程惯例取值：minim.mdp 用 emtol=1000、nsteps≥50000；收敛输出示例（Fmax<1000、Epot 为负）；NVT 100 ps（dt=2 fs 下 50000 步）、NPT 500 ps（dt=2 fs 下 250000 步） | C：Lemkul lysozyme 教程（2025 系列） | 教程页面正文原文（07_equil2「a 500-ps NPT equilibration」、密度统计跨 500 ps；mdp 附件因 content-type 无法在线读取，时长以教程页面正文为准） | 已核实（教学性取值，正文已注明） |
| 平衡判据应组合温度、压力、密度等可观测量直至稳定（best practices） | B：Braun et al. 2019，Living J. Comput. Mol. Sci. 1(1)；辅以 C 级教程 | 检索摘要 | 文档推定（正文已注明归纳性质） |
| 水模型平衡密度以模型参考值为准而非实验值；TIP3P/SPC/SPC/E 在 298 K 密度存在差异 | B：Mark & Nilsson 2001（JPCA 105:9954）；Vega & Abascal 2011（PCCP 13:19663） | 检索元数据（未逐字核验密度数值，正文未写具体密度数值） | 已核实（正文未断言具体数值） |
| 半各向异性（semiisotropic）与表面张力（surface-tension）控压类型存在，compressibility 与 ref_p 按分量给出；膜体系由 CHARMM-GUI 等工具提供分阶段平衡协议 | A：mdp-options（pcoupltype 选项存在）；B：Wu et al. 2014（JCC 35:1997） | 检索结果 + 元数据 | 已核实（正文未断言其默认取值） |
| compressibility 选项页明示水在 1 atm、300 K 时的等温压缩率为 4.5×10⁻⁵ bar⁻¹，水体系通常直接采用该值（正文已按选项页归因 [2]） | A：GROMACS 2026.4 mdp-options RST（compressibility 条目） | extract 官方 mdp-options RST 原文 | 已核实 |
| tcoupl 默认（列表首项）no、pcoupl 默认（列表首项）no、tau-p 默认 (5) ps；tau-t 与 ref-t 选项页未列默认（正文标注「须显式给出」）；compressibility 选项页明示水 1 atm、300 K 时为 4.5e-5 bar⁻¹；v-rescale 随机种子由 ld-seed 设置（默认 -1 自动） | A：GROMACS 2026.4 mdp-options RST（tcoupl/pcoupl/tau-p/tau-t/ref-t/compressibility/ld-seed 条目） | extract 官方 mdp-options RST 原文 | 已核实 |

## 元数据核验记录（2026-10-29 修订复核补齐）

- [25] Vega & Abascal 2011：DOI 10.1039/C1CP22168J，anysearch 学术域核验一致。
- [26] Braun et al. 2019（作者 7 人：Braun/Gilmer/Mayes/Mobley/Monroe/Prasad/Zuckerman）：DOI 10.33011/livecoms.1.1.5957，anysearch 学术域核验一致。
- [28] Hess 1997 LINCS：DOI 10.1002/(SICI)1096-987X(199709)18:12<1463::AID-JCC4>3.0.CO;2-H（Crossref 登记形式，DOI 系统可解析并跳转 Wiley）。
- [29] Hess 2008 P-LINCS：DOI 10.1021/ct700200b，anysearch 学术域核验一致。
- 正文编号按首现顺序：SHAKE=[27] 先于 LINCS=[28]、P-LINCS=[29]、SETTLE=[30]，5.8.1 段内已调整句序使 [27] 先于 [28,29,30] 出现。

## 检索过程说明

- 检索工具为 anysearch CLI（search/batch_search/extract 与学术域 DOI 检索）。2026-10-29 修订复核中：tcoupl/pcoupl/tau-p 等默认值已由 mdp-options RST 原文核验（见第 38 行），四条文献 DOI 已补齐（见元数据核验记录），不再有「未作断言」的默认值条目。
- D 级来源（博客、问答、百科）仅作线索，未承担任何正文论断；正文所有 A 级行为与默认值论断均有官方文档 extract 原文或检索原文片段支撑，C 级取值均注明「教程惯例」。