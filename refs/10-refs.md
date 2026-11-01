# 第 10 章 参考文献（refs）

> 本章正文参考文献，编号与正文上标严格对应（GB/T 7714-2015）。在线文档标注访问日期：2026-10-29。
> 核验说明：A 级 GROMACS 页（grompp、Managing long simulations、mdp-options）与 Slurm 首页、DataLad 手册 YODA 章节、F1000Research YODA 海报页均已原文 fetch；mdrun 帮助文本经官方 man 全文检索核验；B 级文献六项（标题、作者、期刊、年、卷期页、DOI）均经期刊页/PubMed/Crossref 元数据核对；[16]（Lemkul）发表年份存在 2018 与 2019 两种标注，正文与清单按 LiveCoMS 期刊正式发行年取 2019 并括注；[31]（McKinney）页码经 Crossref 元数据核实为 56-61（个别二手数据库写作 51-56，以 Crossref 为准）。squeue/sacct/sstat 三个 Slurm 页面与 git-lfs 页面未在本轮逐字 fetch（URL 依 SchedMD 与官方站点规范路径），其字段语义按官方文档表述书写，正文与核查日志均标注为文档推定。

[1] GROMACS 2026.4 documentation. gmx grompp[EB/OL]. https://manual.gromacs.org/current/onlinehelp/gmx-grompp.html（访问日期：2026-10-29）.
[2] GROMACS 2026.4 documentation. gmx mdrun[EB/OL]. https://manual.gromacs.org/current/onlinehelp/gmx-mdrun.html（访问日期：2026-10-29）.
[3] GROMACS 2026.4 documentation. Managing long simulations[EB/OL]. https://manual.gromacs.org/current/user-guide/managing-simulations.html（访问日期：2026-10-29）.
[4] SchedMD. Slurm Workload Manager: sbatch (26.05)[EB/OL]. https://slurm.schedmd.com/sbatch.html（访问日期：2026-10-29）.
[5] Snakemake documentation. Executor plugins[EB/OL]. https://snakemake.readthedocs.io/en/stable/executing/executors.html（访问日期：2026-10-29）.
[6] BioExcel. GROMACS Best Practices[EB/OL]. https://docs.bioexcel.eu/gromacs_bpg/（访问日期：2026-10-29）.
[7] Wilson G, Aruliah D A, Brown C T, et al. Best practices for scientific computing[J]. PLoS Biology, 2014, 12(1): e1001745. DOI: 10.1371/journal.pbio.1001745.
[8] Mölder F, Jablonski K P, Letcher B, et al. Sustainable data analysis with Snakemake[J]. F1000Research, 2021, 10: 33. DOI: 10.12688/f1000research.29032.2.
[9] Abraham M J, Murtola T, Schulz R, et al. GROMACS: High performance molecular simulations through multi-level parallelism from laptops to supercomputers[J]. SoftwareX, 2015, 1-2: 19-25. DOI: 10.1016/j.softx.2015.06.001.
[10] Sandve G K, Nekrutenko A, Taylor J, et al. Ten simple rules for reproducible computational research[J]. PLoS Computational Biology, 2013, 9(10): e1003285. DOI: 10.1371/journal.pcbi.1003285.
[11] Hanke M, Meyer K A, Visconti di Oleggio Castello M, et al. YODA: YODA's Organigram on Data Analysis[EB/OL]. F1000Research, 2018, 7: 1965 (poster). DOI: 10.7490/f1000research.1116363.1.
[12] Peng R D. Reproducible research in computational science[J]. Science, 2011, 334(6060): 1226-1227. DOI: 10.1126/science.1213847.
[13] Grüning B, Chilton J, Köster J, et al. Practical computational reproducibility in the life sciences[J]. Cell Systems, 2018, 6(6): 631-635. DOI: 10.1016/j.cels.2018.03.014.
[14] Deelman E, Peterka T, Altintas I, et al. The future of scientific workflows[J]. The International Journal of High Performance Computing Applications, 2018, 32(1): 159-175. DOI: 10.1177/1094342017704893.
[15] GROMACS 2026.4 documentation. Molecular dynamics parameters (.mdp options)[EB/OL]. https://manual.gromacs.org/current/user-guide/mdp-options.html（访问日期：2026-10-29）.
[16] Lemkul J A. From proteins to perturbed Hamiltonians: A suite of tutorials for the GROMACS-2018 molecular simulation package[J]. Living Journal of Computational Molecular Science, 2019, 1(1): 5068. DOI: 10.33011/livecoms.1.1.5068.（发表年份存在 2018/2019 两种标注，正文按 LiveCoMS 期刊正式发行年取 2019）
[17] Pallets Projects. Jinja documentation (3.1.x)[EB/OL]. https://jinja.palletsprojects.com/（访问日期：2026-10-29）.
[18] GROMACS 2026.4 documentation. gmx select[EB/OL]. https://manual.gromacs.org/current/onlinehelp/gmx-select.html（访问日期：2026-10-29）.
[19] GROMACS 2026.4 documentation. gmx dump[EB/OL]. https://manual.gromacs.org/current/onlinehelp/gmx-dump.html（访问日期：2026-10-29）.
[20] GROMACS 2026.4 documentation. gmx check[EB/OL]. https://manual.gromacs.org/current/onlinehelp/gmx-check.html（访问日期：2026-10-29）.
[21] Wilson G, Bryan J, Cranston K, et al. Good enough practices in scientific computing[J]. PLoS Computational Biology, 2017, 13(6): e1005510. DOI: 10.1371/journal.pcbi.1005510.
[22] The DataLad Handbook[EB/OL]. https://handbook.datalad.org/（访问日期：2026-10-29）.（6.2 节 YODA: Best practices for data analyses in a dataset）
[23] Free Software Foundation. GNU Make Manual[EB/OL]. https://www.gnu.org/software/make/manual/（访问日期：2026-10-29）.
[24] Snakemake documentation[EB/OL]. https://snakemake.readthedocs.io/（访问日期：2026-10-29）.
[25] Köster J, Rahmann S. Snakemake—a scalable bioinformatics workflow engine[J]. Bioinformatics, 2012, 28(19): 2520-2522. DOI: 10.1093/bioinformatics/bts480.
[26] GROMACS 2026.4 documentation. gmx convert-tpr[EB/OL]. https://manual.gromacs.org/current/onlinehelp/gmx-convert-tpr.html（访问日期：2026-10-29）.
[27] SchedMD. Slurm Workload Manager: Job Array Support (26.05)[EB/OL]. https://slurm.schedmd.com/job_array.html（访问日期：2026-10-29）.
[28] SchedMD. Slurm Workload Manager: squeue (26.05)[EB/OL]. https://slurm.schedmd.com/squeue.html（访问日期：2026-10-29）.
[29] SchedMD. Slurm Workload Manager: sstat (26.05)[EB/OL]. https://slurm.schedmd.com/sstat.html（访问日期：2026-10-29）.
[30] SchedMD. Slurm Workload Manager: sacct (26.05)[EB/OL]. https://slurm.schedmd.com/sacct.html（访问日期：2026-10-29）.
[31] McKinney W. Data structures for statistical computing in Python[C]//Proceedings of the 9th Python in Science Conference. Austin: SciPy, 2010: 56-61. DOI: 10.25080/Majora-92bf1922-00a.
[32] Hunter J D. Matplotlib: A 2D graphics environment[J]. Computing in Science & Engineering, 2007, 9(3): 90-95. DOI: 10.1109/MCSE.2007.55.
[33] Ram K. Git can facilitate greater reproducibility and increased transparency in science[J]. Source Code for Biology and Medicine, 2013, 8(1): 7. DOI: 10.1186/1751-0473-8-7.
[34] git-lfs. Git Large File Storage[EB/OL]. https://git-lfs.com/（访问日期：2026-10-29）.
[35] Halchenko Y O, Meyer K, Poldrack B, et al. DataLad: Distributed system for joint management of code, data, and their relationship[J]. Journal of Open Source Software, 2021, 6(63): 3262. DOI: 10.21105/joss.03262.