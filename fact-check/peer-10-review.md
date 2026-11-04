# 第 10 章《自动化与工程化》面向同行深度对抗性审查报告（v2）

- **日期**：2026-11-04
- **审查立场**：科研同行（研究生高年级至 PI、有 MD 基础、需要可复现且方法学严谨的参考书读者），非入门学生
- **审查对象**：`10-自动化与工程化.md`（当前 592 行）、`refs/10-refs.md`、`OUTLINE.md` 第 10 章、`STYLE.md`、`.history/exercises-20261103/10-自动化与工程化-习题原文.txt`（被移除的 7 题）
- **合规声明**：全程未调用 web_search；唯一联网通道为 anysearch CLI（search/extract），核验记录见附录 A
- **参照前置**：`fact-check/10-review.md`（2026-10-29 第二轮验收通过，遗留 P2-1～P2-4）与 `fact-check/10-log.md` 已读；本轮不再重复机械项（字数 11,841／结构／文献编号连续性），聚焦同行价值缺口
- **审查焦点**：Snakemake/Makefile 依赖语义与断点续跑、Slurm 提交脚本生成与作业数组、mdp 模板化、结果汇总与自动报告、git/git-lfs/DataLad 版本化与归档，及可复现工作流/CI/数据归档的工程完备性

---

## 结论速览

- **pass = true（无 P0）**。本轮逐项复核后，正文所依赖的关键工具行为陈述全部与所引官方文档（GROMACS 2026.4 `current` 页、SchedMD 26.05）对位成立（`-maxh` 0.99 倍、thread-MPI/`-ntmpi` 仍在、`-deffnm` 未移除、`nstxout-compressed` 为「步」单位、检查点 `_prev`/`-noappend`/校验和拒追）；不存在伪造文献、错配 DOI 或结构性缺失。
- 存在 **1 项 P1 事实表述订正**（Snakemake 默认依赖判定被夸大为「内容感知校验」，前轮 P2-3 未落实）与 **1 项 P1 代码笔误**（常见错误 4 的 `--output=logs/%-%A_%a.out`），以及若干 P2 深广度缺口；8 项优先行动见第五部分。
- **结构治理提示**：当前正文无「## 习题」（7 题已于 2026-11-03 移除），与 STYLE.md 二.8（习题 ≥6、含 2 开放题）及 OUTLINE.md 10.9 冲突。若按「习题转正文」路线推进，须同步修订 STYLE/OUTLINE 并保留 2–3 题「延伸思考」；逐题去留见第四部分。

---

## 一、深度缺口 depthGaps

### D1　§10.4.1/10.4.2（L195–255）Makefile 未建模 mdrun 的「多产物」本质

- **所缺**：mdrun 一次调用同时写 log/edr/xtc/gro/cpt 等 6 类以上输出，但 Makefile 单目标语义下，示例只把 `nvt.gro` 列为目标（L210–218），xtc/edr 成为「未建模侧产物」；当分析规则（表 10-4 的 `analyze`，L251）需要 `md.xtc` 时，依赖图中没有哪个目标产出 xtc，增量语义会在「xtc 已存在但被删」等场景失算。缺 GNU make ≥4.3 的**成组目标**（`&:` grouped targets）写法，或缺「以 `done.marker` 为主目标、mdrun 产物作侧产物由校验规则核对」的替代方案；也缺 `make -j` 并行时多个 mdrun 的核数争抢提醒（`--jobs` 与 `-ntmpi×-ntomp` 之和须 ≤ 节点核数）。
- **为什么同行需要**：这是把第 5、6 章序列映射为 Makefile 时第一个会撞上的工程问题；正文的「续算完成标记」方案（L229）其实正是此问题的部分答案，可惜未推及非续算场景。
- **改法**：L229 后补 4–6 行「mdrun 多产物与成组目标」：`md.xtc md.edr md.log &: md.tpr`（注明 make 4.3+）与 `done.marker` 两方案并列；加一句 `-j` 资源约束。

### D2　§10.4.4/10.4.5（L272、L314、L320–322）Snakemake 依赖判定表述失准（P1）+ 关键机制缺位

- **表述订正（P1）**：L272「默认要求输出文件已存在，且支持对输出做内容感知的校验」与表 10-5「输出存在性 + 可选内容校验」（L313）把 Snakemake 的默认判定夸大为内容校验。Snakemake 默认与 make 同源——按**输入/输出文件 mtime 比较**；「内容感知」的增强实际来自 `--rerun-incomplete`（依据作业日志把上次中断标记的作业纳入重跑）与 `--rerun-triggers`（mtime/input/output/params 触发源）。上轮验收 P2-3 已指出，未落实。
- **机制缺位（同行标配）**：`--use-conda`（配规则内 `conda:` 块）与 `--use-container` 是 10.3.1「envs/ 环境说明或容器定义」目录的唯一工程化落地通道，正文只声明不操作；`--latency-wait`（共享文件系统 NFS 延迟，与本章 Slurm 语境强相关）未提；`threads:`/`resources:`（mem_mb、runtime、partition）声明及其到执行器资源请求的映射未提。
- **改法**：订正两处措辞（落实 P2-3）；§10.4.5 尾部加 150–250 字「依赖判定默认值与触发源」段，给出 `--rerun-triggers` 与 `--latency-wait` 各一行示例。

### D3　§10.4.4（L276 vs L283/L306）config/config.yaml 与 params.yaml 双轨不一致（P1，可执行性）

- Snakefile 声明 `configfile: "config/config.yaml"`，而渲染与规则一律以 `params.yaml` 为单一事实源，两文件关系无交代。同行照抄会同时维护两个参数文件，与本章「单一事实源」主张（L133）直接冲突。
- **改法**：Snakefile 改 `configfile: "params.yaml"`，或注明分工（config/ 承载全局开关、params.yaml 承载化学参数），二选一并在图 10-2 中同步。

### D4　§10.5.4（L414）thread-MPI 与真 MPI 两种启动形态混写（P1/P2）

- 等式 `--ntasks × --cpus-per-task ≈ -ntmpi × -ntomp` 掩盖了启动形态差异：thread-MPI 下 mdrun 是**单进程**，Slurm 侧应为 `--ntasks=1`、`--cpus-per-task` 即核数（`-ntmpi×-ntomp` 由 mdrun 内部自洽），按等式把 `--ntasks` 设为 `-ntmpi` 会导致超订；真 MPI 下才以 `srun/mpirun -np` 对应 `--ntasks`，此时 `-ntmpi` 不适用。本章语境（作业数组内单 GPU 节点、L386 的单任务脚本）正是 thread-MPI 场景，等式与示例错位。
- 另：`-gpu_id` 官方语义为「可用 GPU 设备过滤清单」（mdrun 选项页原文 "List of unique GPU device IDs available to use"），任务→设备映射由 `-gputasks` 承担——正文「显式指定映射」措辞偏松；`GMX_GPU_ID` 环境变量通道未提。
- **改法**：按启动形态分两句重写资源映射；`-gpu_id`/`-gputasks` 措辞订正；可加一句 `--cpu-bind`/`-pin` 关联。

### D5　§10.5.4（L414）长模拟「作业自续」闭环只一句带过

- 「连续模拟的多个作业借此无缝衔接[3]」——官方长模拟指南的核心工程闭环（`-maxh` 到点 → 检查点 → 下一作业自动续算）在正文无落地形态：while 循环或 `--dependency=afterok` 自续提交、官方推荐的 `nsteps=-1` + `-maxh` 无限运行模式（mdrun 选项页明示）、`convert-tpr -extend` 与 `simulation-part`/`-noappend` 分段语义均未展开。同行做微秒级生产模拟的第一需求即此。
- **改法**：§10.5.4 后加 3–5 行自续循环最小骨架（含 `--dependency=self` 或 while 重提 sbatch），指向 `convert-tpr -extend` 与 `nsteps=-1`。

### D6　§10.6.1（L434–455）聚合脚本工程细节

- `s.sem()` 依赖 scipy（10.2.2 渲染脚本依赖注释只列 pyyaml/jinja2，L101–102，跨节不对齐）；`read_xvg` 只解析 2 列，而 `gmx energy` 多组分 xvg 为 N+1 列；`pathlib.Path(f).parts[1]` 依赖相对路径与目录层数假设（cd 到项目根的前提未声明），脆弱且与 10.3 目录约定不是同一套定位逻辑。
- §10.6.3 的一致性检查阈值（「温度与密度的副本间离散度不超过经验阈值」）只给概念未给标尺。
- **改法**：注明 scipy 依赖与多列解析；定位方式改为与 10.3 约定一致的 glob+目录解析；阈值给标尺示例（如 ±5 K 或 2σ）并标注示意。

### D7　§10.7（L469–501）版本控制与归档的操作性缺口

- 无 `.gitattributes`/`.gitignore` 具体声明（一行 `*.xtc filter=lfs -text` 级别）；大文件误提交后的治理（`git filter-repo`/BFG）未提——真实项目必踩；`datalad run` 有机制陈述，但「归档后复原」10.7.3 是思路而非命令串（`datalad get`/`git lfs pull` 后缺 grompp/`gmx check` 的逐步命令）。
- **改法**：§10.7.1 补 5 行声明示例与大文件清理一句；§10.7.3 命令化（与转化 Ex5 回填合并）。

### D8　§10.2.1（L91）轨迹输出只谈帧率、未谈格式精度

- 已覆盖时间分辨（nstxout-compressed 四问），但未覆盖**空间精度**：xtc 官方即「lossy compression」（mdp-options 原文），`compressed-x-precision` 默认 1000（≈0.001 nm 三位小数）；对氢键寿命、水驻留、跳跃距离等对坐标精度敏感的分析，何时必须 trr 全精度或更高 `compressed-x-precision` 的决策准则缺失。同行在模板设计阶段就会问。
- **改法**：L91 后补 3–4 句「轨迹格式与精度决策」段（引 [15]）。

> depthGaps 总评：Makefile 与归档两翼深度良好（依赖增量、检查点续算、YODA/DataLad 均到位）；薄弱侧集中在 Snakemake（表述失准 + 机制缺位）与 Slurm×工作流的「集群工程」层（自续、规则级提交、资源映射形态）。

---

## 二、广度缺口 breadthGaps

### 「必须补」

- **B1　CI 与冒烟测试（全章缺失，最大广度缺口）**：以「自动化与工程化」为题的章节不出现 CI 是同行最明显的缺课。给最小骨架即可：GitHub Actions/GitLab CI 上 `snakemake -n` 校验 DAG + 微型体系（百原子级、数百步）mdrun 冒烟 + `gmx check` 校验，参数化到第 9 章「结果可复现」主张。落点：§10.4.6 后或 §10.6 后新增小节（8–12 行 + 5 行骨架）。
- **B2　容器与环境锁定**：`--use-conda`/`--use-container` + `conda env export --from-history` / Apptainer def 文件，把 10.3.1 的 `envs/` 目录从「声明」变「操作」。落点 §10.4.4/§10.7.2。
- **B3　工作流 × Slurm 规则级提交（集群主流形态）**：`snakemake --executor slurm`（或 `--cluster "sbatch ..."`）下规则 `threads:`/`resources:`（partition、runtime、mem_mb）→ `#SBATCH` 的映射，与图 10-3 所画的「数组任务内嵌引擎」是互补两向，正文只画了次要方向。落点 §10.5.2/§10.5.4 + 图 10-3 注释修订。

### 「可提及」

- **B4**：其他引擎一句话定位（Nextflow「process+channel」模型、DVC 的管线+数据版本一体、WOMBAT），说明本书取 make+Snakemake 的取舍依据，防「为何不用 Nextflow」之问。
- **B5**：公开数据发布形态（Zenodo 类 DOI、许可、README+数据手册）——习题 7 已问、正文无答（见转化 Ex7 回填）。
- **B6**：`gmx mdrun -multidir` 多副本单进程并行 vs 作业数组的互补——官方原生多副本通道，同行会直接问「为何不用 -multidir」。
- **B7**：监控补充 `squeue --start`（预计启动）、`seff <jobid>`（效率报告）、`sacct` 资源字段（Start/End/Elapsed/MaxRSS/ReqMem/NodeList）；数组间依赖 `--dependency=afterok`；`--export=NONE` 防登录环境泄露（与常见错误 6 呼应）。

---

## 三、教学腔残留 pedagogyResidue

- **总体极轻**：第二人称 0、STYLE 禁用表达 0、无「让我们/首先其次最后」机械排比、无「了解/熟悉/掌握」；段落论证结构合格。以下为可优化的教学式简化与解释性溢出（均 P2）：
- **L91** `nstxout-compressed` 的「四问」展开（「需要它的原因是…」「取值不当的后果是…」）偏教程式排比句式；与 STYLE 三.3 参数四问要求不冲突，但可压缩为方法学陈述并嫁接 D8 的精度决策。
- **L195** 「其核心价值是增量执行：修改一个 mdp 后，只有依赖该 mdp 的目标及其下游被重建，已完成且未受影响的阶段原样保留」——与下文规则示例构成重复解释，可删半句。
- **L21** 前置知识「随用随引，不要求预先通读」——面向学生的安抚语，可删。
- **L27** 「GROMACS 的多级并行能力从工作站延伸到超算，改变的是单次运行的成本结构」——宣传式空句，无信息量，可删。

---

## 四、习题内容转化 exerciseConversion

原则：答案为「正文已有段落」的题不回填；能产出「正文没有的工程知识」的回填为方法学评注/案例解剖/延伸讨论段。

| 原题 | 要点 | 判定 | 落点与改写思路 |
| --- | --- | --- | --- |
| 1 结构题 | 最小 Makefile：增量、clean、$@/$< | **去**（已内化：L195–225 示例即答案；$@/$< 在 10.4.3 L259–268 讲授） | 仅 10.4.3 末补 1 句「模式规则中 $@/$< 的取值示例」评注 |
| 2 概念题 | make vs Snakemake 断点续跑语义 | **去**（已内化：10.4.5 L320–322 整段即答案，且已与续算工具链正交展开） | 不回填 |
| 3 应用题 | 三层校验的 Python 断言脚本 | **回填**（正文只有 bash 版 L155–159，无 Python 断言形态） | 落点 10.2.4 末尾：加「校验的自动化形态」段（约 150 字 + 3 个断言函数骨架：解析 mdp 键值 / 比对 mdout.mdp 与 params.yaml / gmx check 返回码），说明挂载为 make 目标依赖或 Snakemake 规则 |
| 4 设计题 | 5 浓度×3 温度=15 任务的数组映射 + sacct 退出码入聚合 | **回填（最高价值）**（正文只有通用编号→exp001… 映射，L384–385；缺「编号↔参数组合」映射这一步） | 落点 10.5.2 末：加「案例解剖：参数矩阵→数组下标」，给出 `idx = t*5+c`（或相反）映射、params 表驱动渲染、`--array=1-15%5` 与 `%A_%a` 日志、聚合阶段按 `sacct` 退出码过滤的完整链路 |
| 5 追溯题 | 从零重建任务输入的步骤清单 | **回填**（10.3.3 L189 是概念、10.7.3 L501 是思路，无清单） | 落点 10.7.3：把复原路径整理为 6 步清单（git log 定位提交 → git lfs pull/datalad get → 重渲染 → grompp → `gmx check -s1 -s2` → 聚合比对），每步标注核对文件与命令 |
| 6 开放题 | 自动化门槛随情境（单人/五人两年/共享集群）变化 | **回填为延伸讨论段**（10.1.3 只有通用经验法则 L67） | 落点 10.1.3 末：3–5 句按三情境给出门槛调整（阶段级脚本化 vs 工作流引擎 vs 全栈+CI），并列出任何情境都保留人工检查的环节（警告逐条、mdout.mdp 回显核对、第 9 章统计判据） |
| 7 开放题 | git-lfs vs DataLad 哲学 + 公开发布 + 复原时机 | **回填后半**（哲学对比已在表 10-8/图 10-4；发布形态正文无） | 落点 10.7.2 末：加「面向发布的归档」段（DOI/Zenodo、许可、README+数据手册、DataLad 一键获取），缝合 B5 |

**治理提示**：若习题全部转化，STYLE.md 二.8 与 OUTLINE.md 10.9 须同步修订；为维持学习目标（能写出最小 Makefile、能设计数组方案）的落脚点，建议至少保留原题 4 与 5 作为章节末尾「延伸思考」（附在相应节目尾），其余转化为上述正文段。

---

## 五、priorityActions（按优先级，8 项）

1. **（P1）** 订正 Snakemake 依赖判定表述（表 10-5 L313、L272：默认 mtime 比较 + `--rerun-incomplete`/`--rerun-triggers` 增强，落实前轮 P2-3）；同时统一 `config/config.yaml` 与 `params.yaml`（L276/L283/L306）为单一事实源。— 事实表述 + 可执行性。
2. **（P1）** 修复常见错误 4 格式串笔误 `--output=logs/%-%A_%a.out`（L523）→ `logs/prod-%A_%a.out`（与 L366 一致；`%-` 非 Slurm 占位符）。
3. **（P1/P2）** §10.5 补「工作流规则级提交 Slurm」最小示例（executor 插件 + threads/resources→#SBATCH 映射），修订图 10-3 注释，说明与「数组内嵌引擎」两向互补；同步按 D4 区分 thread-MPI/真 MPI 启动形态并订正 `-gpu_id` 措辞。
4. **（P2）** §10.4.1/10.4.2 补 mdrun 多产物建模（成组目标 `&:` 或 done.marker 方案）+ `make -j` 资源约束提醒（D1）。
5. **（P2）** 按第四部分回填：Ex4 案例（10.5.2）、Ex5 复原清单（10.7.3）、Ex3 校验断言（10.2.4）、Ex6 情境化（10.1.3）、Ex7 发布归档（10.7.2）；同步修订 STYLE/OUTLINE 的习题条款。
6. **（P2）** 新增 CI/冒烟测试最小节 + `--use-conda` 环境锁定示例（B1/B2），缝合 `envs/` 目录声明。
7. **（P2）** §10.7.1 补 `.gitattributes`/`.gitignore` 具体声明与大文件误提交清理（`git filter-repo`）一句（D7）。
8. **（P2/P3）** 聚合脚本工程化（scipy 依赖、多列 xvg、路径稳健，D6）；§10.5.4 补作业自续循环骨架（D5）；可提及项（`-multidir`、`--export=NONE`、Zenodo、`seff`/`squeue --start`、`--dependency=afterok`，B6/B7）择要补入。

---

## 六、overall

- 章节骨架完整、语气一贯是「方法学参考书」而非教程，且本轮逐项复核表明其对 GROMACS/Slurm/Snakemake 的行为陈述整体与所引官方文档对位（无 P0 级事实错误），这在同类中文本中属难得的严谨基线；但「能跑/能用」与「同行认可的工程标准」之间仍有系统性差距——Snakemake 默认依赖判定表述需订正、Makefile 未建模 mdrun 多产物、工作流×Slurm 规则级提交与作业自续闭环缺失、CI/冒烟测试与环境锁定全章缺席，习题移除后最有工程价值的三个知识点（参数矩阵→数组下标、复原清单、校验断言形态）尚未回填。
- 建议：按第五部分 8 项行动修订后定稿，其中 1–3 项为必要项；修订完成后可在 10-log.md 补登附录 A 的核验行（多项已具备提升为「已核实」的条件）。

---

## 附录 A：本轮联网核验记录

通道：anysearch CLI（`search`×4、`extract`×2：manual.gromacs.org/current 的 mdp-options 与 gmx-mdrun 页）。**未使用 web_search。**

| 项 | 通道 | 结论 |
| --- | --- | --- |
| thread-MPI / `-ntmpi` 存废（正文 L414 依赖此） | search | GROMACS 2024.5 mdrun 性能指南仍载「Thread-MPI is compatible…」；mdrun 选项页 `-ntmpi`「Number of thread-MPI ranks to start」仍在 → **正文可背书**（不存「已移除」问题） |
| `-maxh` 0.99 倍触发（正文 L414） | extract gmx-mdrun.html | Options「Terminate after 0.99 times this time (hours)」+ Description「written at the first neighbor search step where the run time exceeds -maxh*0.99 hours」→ **成立**（还可补一句「在第一个邻居搜索步终止」的精度信息） |
| `-deffnm` 弃用与否（正文多示例依赖） | extract gmx-mdrun.html | synopsis 仍列 `-deffnm`（2021 弃用公告未产业化移除）→ **正文示例可背书** |
| `-gpu_id` 语义（正文 L414） | extract gmx-mdrun.html | 「List of unique GPU device IDs available to use」（可用性过滤）；任务→设备映射由 `-gputasks` → 正文「显式指定映射」措辞偏松（P2，见 D4） |
| `nstxout-compressed` 单位（表 10-2、L91） | extract mdp-options.html | 「(0) [steps] number of steps that elapse between writing position coordinates using lossy compression」→ 正文「量纲为步」「5000 步 = 10 ps（dt=0.002 ps）」**成立**；同页 `compressed-x-precision(1000)` 佐证 D8 精度决策点 |
| 检查点机制（正文 10.4.5） | extract gmx-mdrun.html | `state_prev.cpt` 备份、`-cpi` 三场景、`-noappend` 分段、检查点校验和拒追 → **10.4.5 全部成立** |
| Snakemake 默认依赖判定（正文 L272/L314） | 官方文档常识 + 前轮 P2-3 记录（本轮未独立 fetch） | 默认按 mtime 比较，「内容校验」非常态默认 → 建议订正后补一次官方页 fetch |

（另：前轮 10-review.md 已核验 `-cpt` 默认 15、`gmx check -s1 -s2`、作业数组 `%A/%a`、YODA 反例、DataLad run/save 职责等，本轮不重复。）