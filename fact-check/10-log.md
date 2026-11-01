# 第 10 章 核查日志（fact-check）

> 每条记录一行关键论断。状态三档：已核实（官方文档原文/检索原文可见）、文档推定（官方文档明示或由已验证来源推导，但未在本机实测或未逐字复核原文，正文须注明）、待核实（不得进入终稿）。本章无「待核实」条目；「文档推定」条目均已在正文以「经验做法/示意/文档推定/工程惯例」等措辞标注依据类型。
> 检索通道：anysearch（search/batch_search，当日配额可用）+ web_fetch（manual.gromacs.org、slurm.schedmd.com、f1000research.com、handbook.datalad.org、api.crossref.org）。
> B 级文献六项（标题、作者、期刊、年、卷期页、DOI）全部经期刊页/PubMed/Crossref 元数据核对；[16] 发表年份按 LiveCoMS 期刊正式发行年取 2019（教材站与作者主页分别标注 2018/2019，正文与 refs 已括注差异）；[31] 页码经 Crossref（page=56-61）核实，个别二手数据库写作 51-56，以 Crossref 为准。

| 论断 | 来源（级别+定位） | 核验方式 | 状态 |
| --- | --- | --- | --- |
| gmx grompp：tpr 可作为 MD 程序唯一输入文件；mdout.mdp「包含注释行以及 grompp 读入的输入」；`-maxwarn` 选项说明「并非正常用途，且可能生成不稳定系统（may generate unstable systems）」；`-pp` 输出预处理后拓扑；内置预处理器支持 #ifdef/#ifndef/#else/#endif/#define/#undef/#include，mdp 的 define/include 两选项传参 | A：GROMACS 2026.4 gmx grompp 帮助页 | web_fetch 官方页（Description 与 Options 原文） | 已核实 |
| gmx dump 用于查看 run input 文件内容；gmx check 用于比较两个 run input 文件 | A：gmx grompp 帮助页 Description 所引 + gmx-check/gmx-dump 在线页条目 | web_fetch grompp 页原文 | 已核实 |
| 检查点机制：-cpt 周期写入检查点、写入新检查点前将旧文件重命名为 `_prev`；`mdrun -cpi state.cpt` 续算；默认向旧输出追加且受检查点内校验和保护，文件被改/删则须恢复或 `-noappend`（生成 .partXXXX）；单纯延长用 `gmx convert-tpr -extend`；改参数用 `grompp -t state.cpt` 配合 `-cpi`；续算一般不应重新生成速度、应选 continuation；无检查点的续算已不再支持；`-reprod` 消除可复现性偏差因素 | A：GROMACS 2026.4 Managing long simulations（user-guide/managing-simulations.html） | web_fetch 官方页全文 | 已核实 |
| mdp 默认值规则：默认值写在括号中或列在取值列表首项，列表首项恒为默认，单位在方括号中，连字符与下划线等价 | A：GROMACS 2026.4 mdp-options 页开头 General information | web_fetch 官方页原文 | 已核实 |
| `define = -DPOSRES` 触发拓扑中 posre.itp 的引入（位置约束）；`-DFLEXIBLE` 触发柔性水 | A：mdp-options 页 define 条目 | web_fetch 官方页原文 | 已核实 |
| Slurm 当前在线文档版本为 26.05（SchedMD 主页明示）；sbatch --array 语法、%A/%a 输出占位、--array=0-15%N 并发上限、SLURM_ARRAY_JOB_ID/TASK_ID/TASK_COUNT/TASK_MIN/TASK_MAX、squeue 数组聚合显示与 scancel 语法 | A：slurm.schedmd.com 首页 + job_array.html + sbatch.html | web_fetch 首页；anysearch 检索官方 job_array/sbatch 原文 | 已核实（官方页原文可见） |
| gmx mdrun：-cpt 默认 15（分钟）；-maxh 按请求时长的 0.99 倍终止；-ntmpi/-ntomp/-pin/-nb/-gpu_id/-reprod 选项语义与默认值 | A：gmx mdrun 帮助文本（官方 man 页） | anysearch 检索官方 man 全文（Options 段逐字可见） | 已核实 |
| Jinja2 官方定义：Jinja is a fast, expressive, extensible templating engine；模板中特殊占位符允许书写类似 Python 的语法 | A：jinja.palletsprojects.com 首页 | web_fetch 官方页原文 | 已核实 |
| Snakemake 9.x 文档、执行器接口自 8.0 起插件化 | A：snakemake.readthedocs.io（executor_plugin 页） | 内建检索清单提供 URL；本轮未逐字 fetch | 文档推定（正文按内置清单表述） |
| BioExcel GROMACS BPG 作为方法与最佳实践参考（质量控制纳入工作流常态） | A：docs.bioexcel.eu/gromacs_bpg | 内置清单提供 URL；本轮未逐字 fetch 章节 | 文档推定（正文一般性引用） |
| YODA 反例（results_August19/、main_script_DONTUSE.py）与三条原则（P1 一件事一个数据集；P2 记录来源与位置；P3 记录操作与工具）；datalad create -c yoda 程序化应用 | C：DataLad Handbook 6.2 YODA 章节（其标注来源为 YODA 项目海报与幻灯片） | web_fetch handbook 6.2 全文 | 已核实（手册页原文） |
| YODA 海报元数据：Hanke M, Meyer K A, Visconti di Oleggio Castello M, Poldrack B, Halchenko Y O. YODA: YODA's Organigram on Data Analysis, F1000Research 2018, 7: 1965（poster），DOI 10.7490/f1000research.1116363.1 | C：F1000Research posters 7-1965 | web_fetch 海报页（标题/作者/年份/DOI 原文可见） | 已核实 |
| Wilson 2014 Best practices for scientific computing，PLoS Biology 12(1): e1001745，DOI 10.1371/journal.pbio.1001745 | B | anysearch 检索（PLOS/PubMed/UCL 多源一致） | 已核实 |
| Mölder 2021 Sustainable data analysis with Snakemake，F1000Research 10:33，DOI 10.12688/f1000research.29032.2 | B | anysearch 检索（F1000/PubMed） | 已核实 |
| Abraham 2015 GROMACS…多级并行，SoftwareX 1-2: 19-25，DOI 10.1016/j.softx.2015.06.001 | B | anysearch 检索（KTH 官方出版物清单原文列出卷期页） | 已核实 |
| Sandve 2013 Ten simple rules for reproducible computational research，PLoS Comput Biol 9(10): e1003285 | B | anysearch 检索（PLOS 原文引用） | 已核实 |
| Peng 2011 Reproducible research in computational science，Science 334(6060): 1226-1227，DOI 10.1126/science.1213847 | B | anysearch 检索（PubMed/science.org 一致） | 已核实 |
| Grüning 2018 Practical computational reproducibility in the life sciences，Cell Systems 6(6): 631-635，DOI 10.1016/j.cels.2018.03.014 | B | anysearch 检索（期刊/学者页卷期页一致） | 已核实 |
| Köster & Rahmann 2012 Snakemake—a scalable bioinformatics workflow engine，Bioinformatics 28(19): 2520-2522，DOI 10.1093/bioinformatics/bts480 | B | anysearch 检索（OUP/多源一致） | 已核实 |
| Wilson 2017 Good enough practices in scientific computing，PLoS Comput Biol 13(6): e1005510，DOI 10.1371/journal.pcbi.1005510 | B | anysearch 检索（PLOS 原文） | 已核实 |
| Ram 2013 Git can facilitate greater reproducibility…，Source Code Biol Med 8(1): 7，DOI 10.1186/1751-0473-8-7 | B | anysearch 检索（BMC/PubMed 一致） | 已核实 |
| Halchenko 2021 DataLad: Distributed system…，JOSS 6(63): 3262，DOI 10.21105/joss.03262 | B | anysearch 检索（JOSS 原文） | 已核实 |
| Deelman 2018 The future of scientific workflows，IJHPCA 32(1): 159-175，DOI 10.1177/1094342017704893（检索所得 DOI 尾号为 …7704893，非个别二手来源的 …7704896，以出版社记录为准） | B | anysearch 检索（ORNL PURE/SAGE 记录卷期页与 DOI 一致） | 已核实 |
| McKinney 2010 Data structures for statistical computing in Python，SciPy 2010 论文集 pp. 56-61，DOI 10.25080/Majora-92bf1922-00a | B | Crossref API（page=56-61） | 已核实 |
| Hunter 2007 Matplotlib: A 2D graphics environment，CiSE 9(3): 90-95，DOI 10.1109/MCSE.2007.55 | B | anysearch 检索（ACM/IEEE/多源一致） | 已核实 |
| Lemkul GROMACS-2018 教程套件：LiveCoMS 1(1): 5068，DOI 10.33011/livecoms.1.1.5068；发表年份存在 2018 与 2019 两种标注，正文取 2019（期刊正式发行年）并括注 | C：LiveCoMS 期刊页 + 作者主页 | anysearch 检索（期刊页 article v1i1e5068；年份两源冲突） | 文档推定（年份口径取 2019，已在 refs 括注） |
| GNU make：目标-依赖-命令三元组、时间戳增量语义、.PHONY、自动变量 $@/$< /$^/$*、模式规则 %、同名文件与目标冲突 | A：GNU make 手册 | 手册常识（官方手册明示）；本轮未逐字 fetch 相应章节 | 文档推定（正文按手册语义书写） |
| 经验性取值：-maxh 略小于 walltime（48:00:00 取 47.5）；mdp nsteps 50000/250000；nstxout-compressed 500/5000；并发上限 5 | 工程惯例 | 正文均已标注「经验做法/示意/工程惯例」 | 文档推定（正文已标注） |
| squeue 状态码（PD 排队/R 运行/S 挂起）与字段 | A：squeue 手册 | 未逐字 fetch（官方页规范路径 + 多站点一致） | 文档推定（正文已标注） |
| sacct --format=JobID,JobName,State,ExitCode 事后审计与数组逐任务列出 | A：sacct 手册 | 未逐字 fetch | 文档推定（正文已标注） |
| sstat -j 按作业/步读取实时 CPU/内存/能耗统计 | A：sstat 手册 | 未逐字 fetch | 文档推定（正文已标注） |
| 聚合口径（温度/密度/能量/RMSD 平台值、结束时间戳完整性核对、excluded 记录）与一致性检查设计 | 方法学设计（与第 9 章统计判据衔接） | 由已验证事实 + 本书第 9 章判据推导 | 文档推定（正文以方法学建议表述） |
| git-lfs 指针提交与 smudge/clean 过滤器机制 | A：git-lfs.com | 内置清单提供 URL；未逐字 fetch | 文档推定（正文按官方机制表述） |
| DataLad：annex 大文件指针管理、datalad run 记录命令与输入输出、datalad rerun、datalad get、create -c yoda | A：DataLad Handbook | web_fetch handbook 6.2（datalad run/rerun/get/create -c yoda 原文可见）；内置清单 | 已核实（手册页原文可见部分） |