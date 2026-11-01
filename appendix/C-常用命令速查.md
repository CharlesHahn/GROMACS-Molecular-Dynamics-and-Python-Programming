# 附录 C　常用命令速查

本附录把全书涉及的 GROMACS 命令行工具按任务分组列出，供搭建输入、运行模拟与分析轨迹时快速检索。每条给出可复制的命令、关键选项、输出文件与本书对应章节。版本基线为 GROMACS 2026.4，平台为 Linux（bash）；Windows 用户经 WSL 执行同一命令。命令中标注「示意」的输出文件名与交互序号随体系与版本变化，复制时须按实际提示调整。

使用本附录前须掌握三条通用约定。其一，工具一律以 `gmx <工具名>` 调用，交互式工具（如 genion、rms 旧式组选择）在运行时会提示选择索引组，`<<< $'1\n0'` 这类写法把选择序号依次喂入标准输入，使命令可脚本化（见第 10 章）。其二，常用输入选项的字母约定：`-f` 为输入轨迹或结构，`-s` 为结构文件或运行输入（.tpr/.gro/.pdb），`-o` 为输出文件，`-n` 为索引文件（.ndx），`-p` 为拓扑文件；多数分析工具支持 `-b`（起始时间）、`-e`（结束时间）与 `-dt`（抽帧间隔）三个时间窗选项，单位默认皮秒。其三，输出文件默认命名会互相覆盖（同一目录重复运行 gmx rms 会覆盖上一次的 rmsd.xvg），批量场景应显式指定 `-o` 输出名，或统一用 `-deffnm` 前缀（3.4.3 节）。

## 一、体系构建

### pdb2gmx：结构文件 → 拓扑与坐标（4.3 节）

`gmx pdb2gmx` 读取 PDB/mmCIF 结构，按所选力场的 `.rtp` 残基模板生成拓扑与加氢坐标。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x
gmx pdb2gmx -f 1aki.pdb -o system.gro -p topol.top -ff charmm36m -water tip3p -ignh
```

表 C-1　pdb2gmx 关键选项

| 选项 | 含义 |
| --- | --- |
| `-f` | 输入结构文件（.pdb/.mmcif） |
| `-o` | 输出坐标（默认 conf.gro） |
| `-p` | 输出拓扑（默认 topol.top） |
| `-ff` | 力场选择（交互或直接指定，如 charmm36m、amber19sb） |
| `-water` | 水模型选择（如 tip3p、opc） |
| `-ignh` | 忽略输入结构中的氢原子，按模板重建（通行做法） |
| `-his` / `-ter` / `-ss` | 逐残基交互处理组氨酸质子化态、端基与二硫键 |

输出文件：`system.gro`（含氢坐标）、`topol.top`（体系拓扑）、`posre.itp`（非氢原子的位置约束文件，供平衡阶段 `-DPOSRES` 引用）。

### editconf：定义模拟盒（4.6 节）

`gmx editconf` 读取坐标并把溶质置于指定盒型内。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；-d 为溶质表面到盒壁的最小缓冲距离
gmx editconf -f system.gro -o box.gro -c -d 1.0 -bt dodecahedron
```

表 C-2　editconf 关键选项

| 选项 | 含义 |
| --- | --- |
| `-c` | 把溶质几何中心平移到盒中心 |
| `-d` | 溶质到盒壁的缓冲距离（nm），最小镜像条件要求盒最短边 ≥ 2 倍截断，缓冲 1.0 nm 对应 1.2 nm 截断 |
| `-bt` | 盒型：cubic、dodecahedron（各向同性体系默认推荐）、octahedron、triclinic |
| `-box` / `-angles` | 直接指定盒边长与夹角（膜等正交长方体以 triclinic 盒的 90° 角特例设置） |

输出文件：`box.gro`（坐标 + 盒向量）。

### solvate：填充水分子（4.7.1 节）

`gmx solvate` 复制预平衡溶剂盒并剔除与溶质重叠的分子，同时更新拓扑的 `[ molecules ]` 段。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；spc216.gro 为三位点水模型通用预平衡盒
gmx solvate -cp box.gro -cs spc216.gro -o solv.gro -p topol.top
```

表 C-3　solvate 关键选项

| 选项 | 含义 |
| --- | --- |
| `-cp` | 溶质坐标（须已定好盒） |
| `-cs` | 溶剂预平衡盒；换水模型时改指对应文件（如 tip4p.gro） |
| `-o` / `-p` | 输出坐标与需更新的拓扑 |
| `-radius` | 溶质-溶剂重叠判据的排斥半径 |

输出文件：`solv.gro` 与更新后的 `topol.top`，二者必须成对使用。

### genion：电荷中和与加盐（4.7.2 节）

`genion` 读取 `grompp` 生成的 `.tpr`，在选定溶剂组中随机用离子替换水分子。完整命令链为：先以任意最小化用 .mdp 生成 `ions.tpr`，再执行：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；离子名须与本力场 ions.itp 一致
gmx grompp -f ions.mdp -c solv.gro -p topol.top -o ions.tpr
gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -pname NA -nname CL -neutral
```

表 C-4　genion 关键选项

| 选项 | 含义 |
| --- | --- |
| `-s` | 含完整坐标、拓扑与盒信息的 `.tpr`（由第一次 grompp 生成） |
| `-o` / `-p` | 输出坐标与需更新的拓扑 |
| `-pname` / `-nname` | 正/负离子分子型名（自 GROMACS 4.5 起统一为元素符号大写，如 NA、CL） |
| `-neutral` | 添加恰好中和净电荷的离子 |
| `-conc` | 与 `-neutral` 联用，在中和基础上把盐浓度提高到目标值（不含已有离子） |
| `-rmin` | 离子与非溶剂原子的最小距离 |

输出文件：`solv_ions.gro` 与更新后的 `topol.top`。

### grompp：预处理生成运行输入（6.1 节）

`grompp` 把 mdp 参数、拓扑与坐标合并为二进制 `.tpr`，是 mdrun 的唯一输入，并做原子数、净电荷与参数缺口检查。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；-maxwarn 仅在确认警告无害时使用
gmx grompp -f em.mdp -c solv_ions.gro -p topol.top -o em.tpr -maxwarn 2
```

表 C-5　grompp 关键选项

| 选项 | 含义 |
| --- | --- |
| `-f` | mdp 参数文件 |
| `-c` | 输入坐标；续算改参数时用 `-t` 传入检查点 |
| `-p` | 拓扑（.top） |
| `-o` | 输出 `.tpr` |
| `-r` | 位置约束参考坐标（平衡阶段常用，等于 `-c` 的结构） |
| `-n` | 索引文件（可选） |
| `-maxwarn` | 允许忽略的警告数；掩盖真实错误会产出无法解释的体系 |
| `-pp` / `-po` | 输出预处理后的展开拓扑 / 回显 mdp（mdout.mdp） |

输出文件：`em.tpr`、`mdout.mdp`（以回显文件核对生效参数，见 10.4 节）。

## 二、运行：mdrun（2.6 节、6.2 节）

`gmx mdrun` 消费 `.tpr`，执行最小化、平衡与生产。`-deffnm name` 把全部输出统一以 name 为前缀，是脚本化推荐的写法。三个阶段的最小调用：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x
gmx mdrun -deffnm em -v                                 # 能量最小化
gmx mdrun -deffnm nvt -ntmpi 1 -ntomp 16                # NVT 平衡（单节点 thread-MPI）
gmx mdrun -deffnm md_prod -maxh 47.5 -cpt 15            # 生产（作业限时 47.5 h，检查点 15 min 一次）
```

表 C-6　mdrun 常用选项

| 选项 | 含义 | 相关节 |
| --- | --- | --- |
| `-s` | 运行输入 `.tpr`（与 `-deffnm` 二选一即可定位） | 6.2 |
| `-deffnm` | 全部输出的统一前缀（md.log、md.edr、md.xtc 等） | 6.2 |
| `-cpi` | 从检查点恢复（`gmx mdrun -cpi state.cpt`） | 6.2.3 |
| `-noappend` | 续算段写入独立文件并插入 `.partXXXX` 段号 | 6.2.3 |
| `-maxh` | 作业限时（小时），到时自动写检查点退出 | 10.5 |
| `-cpt` | 检查点写入间隔（分钟） | 6.2.2 |
| `-ntmpi` / `-ntomp` | 进程（rank）数与每进程线程数 | 2.6.4、6.4 |
| `-nb` / `-pme` / `-bonded` / `-update` | 短程非键、长程静电、成键、积分更新的执行位置（auto/gpu/cpu） | 6.4.3 |
| `-npme` | 专职 PME 的秩数（-1 自动） | 6.4.2 |
| `-gpu_id` / `-gputasks` | GPU 编号限定与任务映射（多卡） | 6.4.4 |
| `-plumed` | 启用 PLUMED 插件（`gmx mdrun -deffnm md -plumed plumed.dat`） | 8.6.1 |
| `-v` / `-nsteps` | 进度输出 / 覆盖步数（基准测试常用） | 6.2 |

输出文件：`md.log`（日志）、`ener.edr`（能量）、`confout.gro`（末帧结构）、`traj.trr`（全精度轨迹）、`traj_comp.xtc`（压缩轨迹，默认 3 位小数精度）、`state.cpt`（检查点）[4-12]。

## 三、常规分析

### trjconv：轨迹变换与周期边界修正（7.1 节、6.7.2 节）

轨迹进入距离类分析前的标准预处理。`-pbc` 提供 none、whole、mol、res、atom、nojump、cluster 七种取值，whole 拼合断裂分子、mol 按分子质心入盒（须 `-s` 提供 .tpr）、nojump 去跨盒跳变；`-pbc`、`-center`、`-ur` 的组合必要时分多次调用。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x
gmx trjconv -s md.tpr -f md.xtc -o md_whole.xtc -pbc mol -center -ur compact <<< $'1\n0'
gmx trjconv -s md.tpr -f md_whole.xtc -o md_nojump.xtc -pbc nojump <<< $'0'
```

表 C-7　trjconv 关键选项

| 选项 | 含义 |
| --- | --- |
| `-pbc` | 周期边界模式（whole/mol/res/atom/nojump/cluster/none） |
| `-center` | 把所选参考组几何中心平移到盒中心 |
| `-ur` | 单位胞表示：rect/tric/compact |
| `-dt` | 按时间间隔抽帧（要求时间戳可靠，不可靠时先 `-timestep` 修正） |
| `-b` / `-e` | 起始/结束时间 |
| `-sep` | 每帧分离输出（抽快照用，如 `-dt 1000 -sep`） |

输出文件：变换后的轨迹（xtc/trr 或 pdb，视 `-o` 扩展名）。

### make_ndx：交互式索引组生成（7.2.1 节）

大多数工具能生成默认索引组（System、Protein、Backbone、C-alpha、SOL 等），需要特殊组时才运行 `gmx make_ndx`。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；编辑器内键入 h 查看命令，q 退出保存
gmx make_ndx -f md.gro -o index.ndx
```

表 C-8　make_ndx 关键选项

| 选项 | 含义 |
| --- | --- |
| `-f` | 结构文件（决定可用组） |
| `-o` | 输出索引文件 |
| `-n` | 已有索引文件（在其上追加编辑） |
| `-twin` / `-natoms` | 按偏移复制全部组（镜像双层体系） |

输出文件：`index.ndx`（`[ 组名 ]` + 原子编号列表的纯文本）。

### select：选择语法定义组（7.2.2 节）

`gmx select` 用选择表达式直接输出索引组，表达能力覆盖 make_ndx，是脚本化选组的推荐途径。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 5.1 及以上
gmx select -s md.tpr -on pocket.ndx -select 'resname LIG and within 0.5 of (protein)'
```

表 C-9　select 关键选项

| 选项 | 含义 |
| --- | --- |
| `-s` | 结构或运行输入 |
| `-on` | 输出索引文件（把表达式固化为组） |
| `-select` | 选择表达式；关键字 name、resname、resid、within、byres、com 等 |
| `-os` | 输出选择统计 |

输出文件：索引文件与统计文件。选择关键字对大小写敏感，写错名称时选择结果为空集而非报错，这是最常见的静默失败方式。

### rms：均方根偏差（7.3.1 节）

`gmx rms` 先按 `-fit` 做最小二乘叠加（默认质量加权 rot+trans），再计算所选原子相对参考结构的 RMSD。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；交互选择两次组：先拟合组后计算组（示例均选 1）
gmx rms -s md.tpr -f md_whole.xtc -n index.ndx -o rmsd.xvg -fit rot+trans <<< $'1\n1'
```

表 C-10　rms 关键选项

| 选项 | 含义 |
| --- | --- |
| `-s` | 参考结构（初始帧/晶体结构/稳态帧，数值不可直接比较） |
| `-f` | 轨迹 |
| `-n` / `-o` | 索引 / 输出（默认 rmsd.xvg） |
| `-fit` | 拟合方式：rot+trans（默认）、none 等 |
| `-tu` | 输出时间单位（如 `-tu ns`） |
| `-what` | 除 RMSD 外可选 rho 与 rhosc 相似度参数 |

输出文件：`rmsd.xvg`（时间、RMSD 两列）。

### rmsf：均方根涨落（7.3.2 节）

`gmx rmsf` 计算原子围绕平均结构的柔性，须保持拟合开启，否则整体转动平动会叠加到涨落上。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x
gmx rmsf -s md.tpr -f md_whole.xtc -n index.ndx -o rmsf.xvg -res -oq bfac.pdb <<< $'1'
```

表 C-11　rmsf 关键选项

| 选项 | 含义 |
| --- | --- |
| `-res` | 按残基平均输出 |
| `-oq` | 把 RMSF 转换为 B 因子写入 PDB（B = 8π²⟨u²⟩/3） |
| `-ox` | 输出平均坐标 |
| `-fit` | 拟合开关（默认开启） |

输出文件：`rmsf.xvg`、`bfac.pdb`、`avg.pdb`。

### gyrate：回转半径（7.3.3 节）

自 GROMACS 2024 起 `gmx gyrate` 为全新实现，用选择语法与 `-mode` 指定原子集合与加权方式。命令：

```bash
# 平台：Linux（bash）；GROMACS 2024 及以上（新实现）；-p/-nmol/-nz 为 legacy 专属选项
gmx gyrate -s md.tpr -f md_whole.xtc -sel 'protein' -mode mass -o gyrate-taf.xvg
```

表 C-12　gyrate 关键选项

| 选项 | 含义 |
| --- | --- |
| `-sel` | 选择语法指定原子集合 |
| `-mode` | 加权方式：mass（默认）、charge、geometry |
| `-o` | 输出（新实现默认 gyrate-taf.xvg） |
| `-rmpbc` | 逐帧整体化分子（默认开启） |

输出文件：`gyrate-taf.xvg`。需要旧的 `-p`（相对主轴）、`-nmol`、`-nz` 接口时调用 `gmx gyrate-legacy`。

### sasa：溶剂可及表面积（7.3.4 节）

`gmx sasa` 以探针球（默认取水分子有效半径 1.4 Å）扫描表面；`-surface` 必须包含全部非溶剂原子。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；-output 子组须为 -surface 组子集
gmx sasa -s md.tpr -f md_whole.xtc -n index.ndx -surface "protein" -output "resname LIG" \
         -o sasa.xvg -odg dgsolv.xvg -or resarea.xvg
```

表 C-13　sasa 关键选项

| 选项 | 含义 |
| --- | --- |
| `-surface` | 表面积计算组（全部非溶剂原子） |
| `-output` | 额外输出子组 |
| `-or` / `-oa` / `-odg` / `-tv` | 按残基面积 / 按原子面积 / 溶剂化自由能估算 / 体积密度（近似） |
| `-pbc` | 默认开启，须保证分子未被盒子切开，否则结果无意义 |

输出文件：`sasa.xvg`、`dgsolv.xvg`、`resarea.xvg`。

### dssp：二级结构判定（7.4.1 节）

自 GROMACS 2023 起以原生 DSSP（version 4）实现取代 `gmx do_dssp` 并更名；2022 及更早版本使用旧名。命令：

```bash
# 平台：Linux（bash）；GROMACS 2023 及以上（2022 及更早用 gmx do_dssp）
gmx dssp -s md.tpr -f md_whole.xtc -sel 'protein' -o dssp.dat -num num.xvg -hmode dssp
```

表 C-14　dssp 关键选项

| 选项 | 含义 |
| --- | --- |
| `-hmode` | 氢原子来源：gromacs（用结构中的氢）/ dssp（构造赝原子，缺氢结构必选） |
| `-hbond` | 氢键定义：energy（静电能）/ geometry（几何判据） |
| `-cutoff` | 残基邻域最大距离（最小且推荐 0.9） |
| `-num` / `-clear` | 各类二级结构数量输出 / 忽略缺关键原子的残基 |

输出文件：`dssp.dat`（逐帧赋值文本）、`num.xvg`。新版不再输出旧版的 ss.xpm 时间图。

### hbond：氢键分析（7.4.2 节）

自 GROMACS 2024 起 `gmx hbond` 被重写，以选择语法定义参考组与目标组；旧接口的寿命与相关输出需调用 `gmx hbond-legacy`。两版默认几何判据一致：供体-氢-受体距离截断 0.35 nm、角度截断 30°。命令：

```bash
# 平台：Linux（bash）；GROMACS 2024 及以上（新实现，选择语法）
gmx hbond -s md.tpr -f md_whole.xtc -r 'protein' -t 'resname SOL' -num hbnum.xvg -o hbond.ndx
# 平台：Linux（bash）；全部版本（旧实现，2024 起需显式 legacy）
gmx hbond-legacy -s md.tpr -f md_whole.xtc -n index.ndx -num hbnum.xvg <<< $'1\n4'
```

表 C-15　hbond 关键选项

| 选项 | 含义 |
| --- | --- |
| `-r` / `-t` | 参考组 / 目标组（新实现，选择语法） |
| `-hbr` / `-hba` | 距离截断 / 角度截断（官方推荐 0.35 与 30） |
| `-de` / `-ae` | 按元素指定供体 / 受体（非标准命名体系必查） |
| `-num` / `-dist` / `-ang` / `-dan` | 数量、距离分布、角度分布、供体-受体距离（新版） |
| `-life` / `-ac` | 氢键寿命自相关 / 存在函数自相关（仅 hbond-legacy） |

输出文件：`hbnum.xvg`、`hbond.ndx`（成键原子索引）及 legacy 的 `hbac.xvg` 等。

### rdf：径向分布函数（7.5.1 节）

`gmx rdf` 以 `-ref` 与 `-sel` 指定参考与目标选择，输出 g(r) 与累积数。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；示意：水氧围绕蛋白 Cα 的分布
gmx rdf -s md.tpr -f md_whole.xtc -ref "protein and name CA" -sel "name OW" \
        -o rdf_water.xvg -cn rdf_cn.xvg -bin 0.005 -rmax 1.0 -norm rdf
```

表 C-16　rdf 关键选项

| 选项 | 含义 |
| --- | --- |
| `-ref` / `-sel` | 参考选择 / 目标选择 |
| `-bin` / `-rmax` | 直方图宽度（默认 0.002 nm）/ 最大距离（默认盒最短边一半） |
| `-norm` | 归一化：rdf（标准）/ number_density / none |
| `-cn` | 累积数输出（配位数由峰谷积分或累积数获得） |
| `-excl` / `-cut` | 拓扑排除分子内原子对 / 清除小距离区域 |

输出文件：`rdf_water.xvg`、`rdf_cn.xvg`。

### energy：能量项提取（3.4.3 节、6.3 节）

`gmx energy` 交互式选择 edr 中的能量项并导出为 xvg；终端打印的全精度均值基于 nstcalcenergy 累计值，与 xvg 抽样帧的均值口径不同。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；交互输入能量项编号，如 1 2（逐行）后回车
gmx energy -f md.edr -o energy.xvg
```

表 C-17　energy 关键选项

| 选项 | 含义 |
| --- | --- |
| `-f` | 能量文件（ener.edr） |
| `-o` | 输出 xvg（内容由交互选择的能量项决定） |
| `-b` / `-e` | 时间窗 |
| `-xvg` | 输出格式（xmgrace/none 等） |

输出文件：`energy.xvg`。报告数值时注明统计口径（全精度统计或抽样帧统计），二者不可混用。

## 四、自由能与高级分析

### covar：协方差矩阵与特征分解（8.5.1 节）

`gmx covar` 对选定原子（常用 Cα，提示后选择）计算坐标涨落协方差并做特征分解，`-fit` 默认去整体平动转动。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；分析组须与拟合组一致
gmx covar -s tpr.tpr -f traj_whole.xtc -o eigenval.xvg -v eigenvec.trr \
          -av average.pdb -ascii covar.dat
```

表 C-18　covar 关键选项

| 选项 | 含义 |
| --- | --- |
| `-o` | 特征值文件（eigenval.xvg，按降序） |
| `-v` | 特征向量轨迹（eigenvec.trr） |
| `-av` | 平均结构（average.pdb） |
| `-ascii` | 协方差矩阵文本输出（供 DCC 归一化等） |

输出文件：`eigenval.xvg`、`eigenvec.trr`、`average.pdb`、`covar.dat`。分析组原子过多会导致内存以原子数平方量级增长，全原子规模可能段错误。

### anaeig：主成分投影（8.5.1 节）

`gmx anaeig` 沿特征向量投影轨迹，`-first`/`-last` 选择主成分范围，`-2d` 输出二维投影供自由能面绘制。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x
gmx anaeig -s tpr.tpr -f traj_whole.xtc -v eigenvec.trr -eig eigenval.xvg \
           -first 1 -last 2 -2d proj2d.xvg
```

表 C-19　anaeig 关键选项

| 选项 | 含义 |
| --- | --- |
| `-v` / `-eig` | 特征向量 / 特征值文件（与 covar 输出对应） |
| `-first` / `-last` | 投影的 PC 编号范围 |
| `-2d` | 二维投影输出（再经 gmx sham 转自由能面） |
| `-proj` / `-extr` | 一维投影 / 沿 PC 的极端构象 |

输出文件：`proj2d.xvg` 等。

### cluster：构象聚类（8.5.3 节）

`gmx cluster` 以最小二乘拟合后的骨架 RMSD 为相似性度量，提供 linkage、gromos、jarvis-patrick、monte-carlo、diagonalization 五种方法；cutoff 决定簇粒度，应先用 `-dist` 查看 RMSD 分布再选定。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；交互选择拟合组与聚类组（示例均选 1）
gmx cluster -s md.tpr -f md_whole.xtc -n index.ndx -method gromos -cutoff 0.15 \
            -cl clusters.pdb -clid clid.xvg -dist rmsd-dist.xvg -sz sz.xvg <<< $'1\n1'
```

表 C-20　cluster 关键选项

| 选项 | 含义 |
| --- | --- |
| `-method` | 聚类方法（linkage 默认 / gromos / jarvis-patrick / monte-carlo / diagonalization） |
| `-cutoff` | 邻居判定 RMSD 阈值（默认 0.1 nm，Cα 经验范围 0.1–0.25 nm） |
| `-cl` / `-clid` / `-sz` | 代表性构象 / 簇归属时间序列 / 簇大小分布 |
| `-dist` | RMSD 分布（选 cutoff 前的诊断输出） |
| `-nstruct` | 输出代表性结构数 |

输出文件：`clusters.pdb`、`clid.xvg`、`rmsd-dist.xvg`、`sz.xvg`。

### bar：Bennett 接受比估计（8.2.2 节）

`gmx bar` 读入各 λ 状态的全部 dhdl.xvg，逐对输出自由能差、误差与相空间重叠度量。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；一次读入多个窗口文件
gmx bar -f lam_*/dhdl.xvg -o bar.xvg -oi barint.xvg -oh hist.xvg -temp 300
```

表 C-21　bar 关键选项

| 选项 | 含义 |
| --- | --- |
| `-f` | 多个 dhdl.xvg（顺序与窗口对应） |
| `-o` | BAR 差分与误差输出 |
| `-oi` | 热力学积分用的导数数据（barint.xvg） |
| `-oh` | 相空间重叠直方图 |
| `-temp` | 参考温度 |

输出文件：`bar.xvg`、`barint.xvg`、`hist.xvg`。误差按分块估计并假定块间独立，相关样本下可能被低估。

### wham：加权柱状分析（8.3.3 节）

`gmx wham` 对伞形采样窗口做 WHAM 重加权，输出 PMF。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；-it 与 -ix 文件顺序须对应
gmx wham -it tpr-files.dat -ix pullx-files.dat -o pmf.xvg -hist hist.xvg \
         -b 50 -nBootstrap 200
```

表 C-22　wham 关键选项

| 选项 | 含义 |
| --- | --- |
| `-it` / `-ix` | tpr 列表 / 各窗口 pull 坐标文件列表（顺序对应） |
| `-o` / `-hist` | PMF / 直方图输出 |
| `-b` / `-e` / `-dt` | 时间窗（默认 -b 50 ps 去除弛豫段） |
| `-ac` | 估计自相关时间并加权窗口 |
| `-nBootstrap` / `-bs-method` | 自助法误差区间（默认 b-hist 方法） |
| `-cycl` / `-sym` / `-zprof0` | 周期坐标 / 对称化 / PMF 归零位置 |

输出文件：`pmf.xvg`、`hist.xvg`。PMF 绝对零点无物理意义，报告相对值须注明参考点。

## 五、工具与诊断

### check：文件与运行输入检查（6.7 节、10.7 节）

`gmx check` 检查轨迹与能量文件的完整性，`-s1`/`-s2` 同时给出时比较两个 `.tpr` 的相互作用设置。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x
gmx check -f traj_comp.xtc        # 轨迹帧数、时间范围与完整性
gmx check -e ener.edr             # 能量文件步数范围
gmx check -s1 em.tpr -s2 md.tpr   # 比较两个运行输入
```

表 C-23　check 关键选项

| 选项 | 含义 |
| --- | --- |
| `-f` / `-e` | 检查轨迹 / 能量文件 |
| `-s1` / `-s2` | 比较两个 `.tpr`（续算前后、副本一致性核对的依据） |

输出文件：终端报告。

### dump：查看二进制文件内容（10.4 节）

`gmx dump` 以文本转储 `.tpr`、`.cpt` 等二进制文件内容，用于核对展开后的运行输入。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；输出较长，可配合分页查看
gmx dump -s topol.tpr
```

表 C-24　dump 关键选项

| 选项 | 含义 |
| --- | --- |
| `-s` | 运行输入（.tpr） |
| `-f` | 轨迹或检查点等二进制文件 |

输出文件：终端文本转储。

### convert-tpr：修改 tpr 运行时长（6.2.3 节）

`gmx convert-tpr` 在不动其他参数的前提下延长或缩短运行。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；-extend 以 ps（皮秒）为单位
gmx convert-tpr -s md.tpr -extend 50000 -o md_ext.tpr
gmx mdrun -s md_ext.tpr -cpi state.cpt
```

表 C-25　convert-tpr 关键选项

| 选项 | 含义 |
| --- | --- |
| `-s` | 原运行输入 |
| `-extend` / `-until` / `-nsteps` | 延长指定时长（ps）/ 延长至指定时刻 / 设定总步数 |
| `-o` | 输出新 tpr |

输出文件：新 `.tpr`。需要改变输出频率或系综等非时长参数时，改用 `grompp -t state.cpt` 重建 tpr。

### tune_pme：PME 性能调优（6.4 节、6.5 节）

`gmx tune_pme` 在给定体系中自动扫描 PME 秩数（`-npme`）、域分解与 PME 网格间距，输出最优组合供大规模 PME 运行参考。命令：

```bash
# 平台：Linux（bash）；版本：GROMACS 2026.x；其余扫描选项以 gmx tune_pme -h 为准
gmx tune_pme -s md.tpr
```

表 C-26　tune_pme 关键选项

| 选项 | 含义 |
| --- | --- |
| `-s` | 运行输入（.tpr） |
| `-dd` / `-npme` | 待扫描的域分解与 PME 秩数范围 |
| `-npme-opt` 等 | 网格间距与精度相关扫描参数（以帮助文本为准） |

输出文件：终端报告与建议配置。自动结果只作初始建议，仍应按目标体系实测微调。

## 六、通用约定与版本差异

交互式组选择的脚本化。需要交互选择组的工具（genion、rms、rmsf、cluster、hbond-legacy 等）在提示时打印当前组的编号列表，`<<< $'1\n0'` 表示依次输入 1 与 0；编号顺序随体系与版本变化，生产脚本应先用一次手工运行确认编号再固定进配置（3.7.2 节）。可替代做法是改用支持 `-sel`/`-ref`/`-t` 选择语法的工具（rdf、sasa、dssp、新版 hbond、gyrate 等），把组定义写进表达式并立即输出为索引文件（`gmx select -on`）。

时间窗与单位。`-b`、`-e`、`-dt` 的时间单位默认皮秒，部分时间序列工具支持 `-tu` 切换输出单位（如 `gmx rms -tu ns`）；能量、温度、压力列的单位不受 `-tu` 影响（3.4.3 节）。所有坐标、距离、能量、压力数值均按 MD 单位制书写，单位换算见附录 D。

版本差异速查（本附录均以 GROMACS 2026.4 为准书写新接口）。`gmx do_dssp` 自 2023 年起更名为原生实现的 `gmx dssp`；`gmx hbond` 自 2024 年起为新实现，旧接口更名为 `gmx hbond-legacy`；`gmx gyrate` 自 2024 年起为新实现，旧选项迁至 `gmx gyrate-legacy`。跨版本复用命令时，以对应版本的 `gmx <工具> -h` 与官方在线帮助核对选项存在性与默认值，不要把旧版本文档的默认值直接套用到 2026.4（1.7.2 节、6.1 节）。