# 第 1–4 章修订后对抗性复核验收报告（re-verify）

- **验收人**：独立验收者（面向同行标准）
- **验收日期**：2026-11-08
- **验收范围**：01-序言.md、02-环境与工具链.md、03-Python数据处理.md、04-体系构建.md（修订后版本，对照 fact-check/peer-01～04-review.md 的 P0/P1 修复要求）
- **验收手段**：全文逐行通读；机械检查用 Python 脚本（reverify_mech.py / reverify_cites.py / reverify_kw.py）；新内容事实核查一律经 anysearch CLI 检证官方文档、期刊/Crossref、GROMACS 论坛与邮件列表等一手来源。
- **判据**：任一 P0（事实错误 / 引用编号断裂 / 结构缺失 / 伪造文献）→ 该章 pass=false。

## 总体判定

| 章 | 判定 | 汉字数 | 参考文献 | P0 数 |
| --- | --- | --- | --- | --- |
| 01 | **fail** | 14,318 | 38 | 3 |
| 02 | **fail** | 13,755 | 34 | 3 |
| 03 | **fail** | 14,352 | 44 | 1（+治理项未闭环） |
| 04 | **fail** | 14,411 | 66 | 2 |

四章均未通过。共同根因是全书级结构缺失（延伸讨论），另各章各有具体 P0，分述如下。

---

## 全书级 P0（四章共同）

**S1.「## 延伸讨论」整章缺失（结构缺失，四章同犯）。**
STYLE 二.8（2026-11 起生效，git 5141f9d）硬性要求每章设 `## 延伸讨论`，≥3 段。经机械扫描，01–04 四章正文与标题中**均无**「延伸讨论」二级节，连 ch9 已采用的内联形态（「方法学评注——」「案例解剖——」）也一处都没有。peer-01 的 E1/E2/E5/E6/E7/E8 转段方案（表 1-2 守恒量判据陷阱、体量推导、0.489 ps 推导、一致性判据等）全部停留在计划，未落地。这是四项判定 fail 的最大权重项。

---

## 第 1 章（01-序言.md）

### 已落地（抽查确认）
- 1.1.2 新增 verification/validation 与「误差三分」（模型误差/算法误差/采样误差）概念；报告要素清单成型。
- 表 1-1 新增「截断与长程近似」行；第 2 行补「更高保真势（极化/机器学习势，第 11 章）」。
- L113 8.5.1 修正、七类错误清单、泛素「近似两态展开」、F7（1.5.3 不再重复全表）、F14（锚定 2.7）、F4 Verlet 表述，均已落实。
- 表 1-4 NVIDIA 行 CUDA 12.1 / 最低算力 CC 5.0 —— 经 anysearch 检证，正确。
- OpenCL「已弃用、但仍是 Apple M 系列唯一后端」、HIP（GFX9/CDNA1/2/3/RDNA1/2/3、ROCm ≥5.2）、NNP、H5MD 实验期 —— 均与 2026.4/2026.0 官方 release notes 一致。

### P0
- **C1-事实**：表 1-4 Apple/OpenCL 行**未加任何前瞻注记**——无「2027 年起移除计划」、无弃用政策出处、无「CPU 回退」提示。官方安装指南确认 OpenCL 仅剩 Apple M 系列后端且弃用，但书里缺了该行要求的前瞻信息，读者无法感知迁移路径。
- **C2-事实**：L359 常见错误六仍写「核对输出中的 **GMX_GPU**」。经 anysearch 抓取多个 `gmx --version` 实测输出，该字段名实为 **"GPU support:"**，不存在 GMX_GPU 字样。照抄会误导自查。
- **C3-文献**：正文两处提及 AMBER14SB/19SB 与 OPC/OPC3 水模型，但 38 条文献中无对应条目（Maier 2015 / Tian 2020 / Izadi 2014 均缺席）——引用体系对不上正文断言。

### P1 未落
- D2：2 fs 稳定性步/氢质量再分配（HMR）机理半句未加（官方确有 mass-repartition 因子与 4 fs 路线）。
- E3：1.2.1 「数值一致性条件」仍无解释句（rvdw=rcoulomb、fourierspacing 0.10–0.12）。

### P2 未落
- F9（L105 守恒量判据表述）、F10（L47 缺「充分采样」限定）、F11（L70–72 无 GPU/CPU 分项与 ns/day）、F12（L326 RCSB「公布校验值」不实）、F13（L337 「CC-BY-4.0 类开放许可」）、F3（L153 「2013 年的 4.5 版本」—— 4.5.x 实为 2011–2012 发布，2013 为论文年份）、F16（L17 「沿用的…直接沿用」）、F15（图 1-2 仍 C1→C3 直连）、E2/E8（体量与 0.489 ps 只有结论无推导）、B2/B3/B4（广度项）、Deserno & Holm 文献未入。

---

## 第 2 章（02-环境与工具链.md）

### 已落地
- 2.1.3 资源估算案例（2 万原子 × 16 B/atom → ~0.3 MB、显存 4–8 GB/百万原子、回退两分支、md.log 观察、「Using CPU」/「On host」回显、time accounting 表）。
- 绑核族（-pin auto/on/inherit/offset、--cpu-bind=cores、OMP_PLACES/OMP_PROC_BIND）、--signal=B:TERM@23:50:00、-maxh 23.9、-cpi/-cpt 续算、容器 --nv/--rocm/--nvccli/PMIx/APPTAINERENV_、表 2-4 OWN_FFTW 限制行 + GMX_BUILD_SHARED_EXE/GMX_PREFER_STATIC_LIBS 行、make check REGRESSIONTEST_DOWNLOAD 边界 —— 上述各点经 anysearch 对照官方手册/libgomp/Apptainer 文档，语义均正确。

### P0
- **C4-事实（新内容算术错误）**：2.1.3 写「16 字节/原子（3 坐标分量加 3 速度分量各 4 字节）」——括号内的 3+3=6 × 4 = **24 字节**，与 16 自相矛盾；且下游 0.3 MB 估算沿用 16（20k×24 = 480 kB ≈ 0.48 MB）。新内容内含内部矛盾，属事实错误。
- **C5-编号断裂**：表 2-4 新增行「…见 [23]」首现于 L360，而 [22] 首现在 L372 —— [23] 先于 [22] 被引用，破坏 1..N 严格递增。经 range-aware 编号检查器确认这是修订引入（其余章编号均合规）。
- **C6-结构缺失**：延伸讨论缺失（见 S1）。

### P1 未落
- 2.7.3 无「基准会话」协议（中位数/重复 3 次/锁定调参/功耗记录）。
- 十条常见错误中未加「GPU 显存耗尽」条目。

### P2 未落
- 图 2-3 mermaid L398 仍有 "SYCLL" 拼写残留；L-460 仍列 d.dppc（按 peer 该文件不在 FTP 目录）；mamba 两处（L43/L170）无引用；GMX_CYCLE_SUBCOUNTERS/NGC/EESSI/lfs setstripe/conda from-export/ControlMaster 等可选项未补。

---

## 第 3 章（03-Python数据处理.md）

### 已落地
- 3.5.2 新增 #### 「误差语义：帧间标准差不是均值不确定度」（ddof/SEM/N_eff、第 9 章桥接、图注要求）—— P0 深度项落地；ddof 断言经检证：numpy std ddof=0、pandas Series/agg std ddof=1，正确（pandas 3.0 2026-01-21 起改为 ddof=0，但书内明示 numpy 2.x/pandas 2.x 基线，不算错）。
- 「误差棒」判据、E7 管线回填（最小可复核管线 + 复核五步 SOP，commit f079625）、3.5.3 跨表时间对齐三前提（L335–355）、merge_asof，均已落地；L218 归一化示例 bug 已修正（commit e172e07）。
- 编号检查：44 条，0 违规（修好聚簇/区间正则后通过）。

### P0
- **C7-结构缺失/治理未闭环**：延伸讨论缺失（S1）；且 OUTLINE 的第 3 章仍只有 3.4.1–3.4.3 / 3.5.1–3.5.3 / 3.6.1–3.6.3，正文经关键词扫描也无 3.4.4/3.5.4/3.6.4 任何痕迹——peer-03 的「治理项」只完成一半：章内补了内容，大纲与目录没有同步。
- Pimentel 2019 未入 44 条文献表（peer 要求验真后入表，未做）。

---

## 第 4 章（04-体系构建.md）

### 已落地（事实核查通过）
- 4.2.2 **-ter 修正**：现表述「-ter 仅用于肽链 N 端与 C 端变体选择，不控制侧链质子化；可电离侧链质子化态由力场 .rtp 模板固定」——与官方手册 "-ter…protonation state of N- and C-termini…chosen interactively" 一致，P0 事实错误已修复。
- 4.8.2 苯甲酸 E5 案例（拼装闭环：原子顺序/原子名/电荷一致；insert-molecules -ci/-nmol/-try 语义经官方文档核实正确）。
- 4.9.4 Martini3 核酸修正：「粗粒化扩展适用尺度判断同 4.4.3」的写法可接受，但官方核酸参数实际列于 Martini 2 的注记仍未点到。
- 各处检证通过：pdb2gmx -water（select/none/opc/opc3/spc/spce/tip3p…tips3p 全枚举）、AMBER19SB+OPC/OPC3 配套、genion -pname/-nname 大写元素名、grompp -pp processed.top、-maxwarn「Not for normal use」、specbond.dat（CYS2/CYX，±0.2/10%）、MDAnalysis ITPParser include_dir 不读 GMXLIB、solvate spc216.gro/三站点共用、-radius 0.105、editconf -d 语义、菱形十二面体 0.71×；editconf「无 boxtype 警告（旋转后距离变小）」经论坛实测输出核实；离子参数族 [50] Joung & Cheatham 2008 JPCB 112(30):9020-9041，DOI 10.1021/jp8001614 经 Crossref 验真。
- 编号检查：66 条，0 违规；refs/04-refs.md 与章末列表逐条一致。

### P0
- **C8-文献（DOI 错误）**：[51] Li P, Song L F, Merz K M Jr., JPCB 2015, 119(3):883-895 —— refs/04-refs.md（L55）与章末列表（L461）DOI 均写作 **10.1021/jp5058759**；经 Crossref/ACS 验证，正确 DOI 为 **10.1021/jp505875v**（尾字符为 v 非 9）。卷期页码正确、文献真实，但 DOI 指向 404，属伪造式引用缺陷。
- **C9-结构缺失**：延伸讨论缺失（S1）。

### P1 未落
- 「三处一致性」（pdb2gmx -water / solvate 水分子 / 力场水模型）未成文。

---

## 机械检查汇总

| 检查项 | 01 | 02 | 03 | 04 |
| --- | --- | --- | --- | --- |
| 汉字数（≥10,000，排除代码块与文献节） | 14,318 | 13,755 | 14,352 | 14,411 |
| 二级节 / 三级节 | 12/25 | 12/26 | 13/29 | 14/34 |
| 表 / 图 | 10/4 | 7/3 | 4/3 | 6/2 |
| 「习题」残留 | 0 | 0 | 0 | 0 |
| 第二人称/违禁表述（STYLE 六） | 0 | 0 | 0 | 0 |
| 文献条数 | 38 | 34 | 44 | 66 |
| refs 文件 = 章末列表 | 逐条一致 | 逐条一致 | 逐条一致 | 逐条一致 |
| 编号 1..N 首现严格递增 | ✓ | **✗**（[23] 先于 [22]） | ✓ | ✓ |

## 结论

01 fail、02 fail、03 fail、04 fail。共性问题为延伸讨论整章缺失；各章 P0：01（OpenCL 前瞻注记缺失、GMX_GPU 字段名错误、AMBER/OPC 文献缺）、02（16 字节/原子算术错误、[23]/[22] 编号断裂）、03（大纲与目录未同步、Pimentel 2019 未入）、04（[51] DOI 应为 jp505875v）。
