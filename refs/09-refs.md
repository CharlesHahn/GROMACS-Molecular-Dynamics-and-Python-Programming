# 第 9 章 参考文献（refs）

> 本章正文参考文献，编号与正文上标严格对应（GB/T 7714-2015）。在线文档标注访问日期：2026-10-29（本轮修订新增的 [12] pymbar 文档为 2026-11-04）。
> 卷期页核验：全部 B 级条目以 Crossref REST API（api.crossref.org，filter=doi）核验题名、作者、期刊、年份、卷期页与 DOI；A 级条目以其对应版本在线版（manual.gromacs.org，2026.4）为准。[3]（LiveCoMS 最佳实践 v1.0）Crossref 记录年份为 2019，期刊官网惯例引用为 2018（v1.0 发布于 2018-10），正文按 2018 引用；卷期页（卷 1 第 1 期，文章号 5067）与 DOI 均经 Crossref 核验，无「卷期页待补」条目。
> 修订说明：本轮（2026-11-04，同行对抗性审查 peer-09-review v2 后的深度补强修订）新增 7 条文献：[10] Sokal 1997（NATO ASI 讲义，C 级权威专著类，INSPIRE/Springer 核验）、[12] pymbar.timeseries 官方文档（A 级，anysearch extract 逐函数核验）、[18] Künsch 1989（projecteuclid/Crossref 核验）、[28] Gapsys & de Groot 2020（eLife/PubMed 核验）、[30] Pérez-Hernández 等 2013（PubMed/AIP/Crossref 核验，DOI 10.1063/1.4811489）、[35] Yeh & Hummer 2004（Semantic Scholar/Crossref 引用链核验）、[38] Wilkinson 等 2016 FAIR（常理多仓储核验）。未引用「Good & Berkowitz」——peer 审查四次检索未能确认该文献存在，深度诉求改由 [10] Sokal 与已引 [9] Straatsma 承担。

[1] Abraham M J, Murtola T, Schulz R, et al. GROMACS: High performance molecular simulations through multi-level parallelism from laptops to supercomputers[J]. SoftwareX, 2015, 1-2: 19-25. DOI: 10.1016/j.softx.2015.06.001.
[2] GROMACS 2026.4 documentation. gmx analyze[EB/OL]. https://manual.gromacs.org/current/onlinehelp/gmx-analyze.html（访问日期：2026-10-29）.
[3] Grossfield A, Patrone P N, Roe D R, et al. Best practices for quantification of uncertainty and sampling quality in molecular simulations [Article v1.0][J]. Living Journal of Computational Molecular Science, 2018, 1(1): 5067. DOI: 10.33011/livecoms.1.1.5067.
[4] Zuckerman D M. Equilibrium sampling in biomolecular simulations[J]. Annual Review of Biophysics, 2011, 40: 41-62. DOI: 10.1146/annurev-biophys-042910-155255.（综述，方法结论另引原始文献）
[5] Frenkel D, Smit B. Understanding molecular simulation: From algorithms to applications[M]. 2nd ed. San Diego: Academic Press, 2002.
[6] Berendsen H J C. Simulating the physical world: Hierarchical modeling from quantum mechanics to fluid dynamics[M]. Cambridge: Cambridge University Press, 2007.
[7] Zuckerman D M. Statistical physics of biomolecules: An introduction[M]. Boca Raton: CRC Press, 2010.
[8] Hess B. Convergence of sampling in protein simulations: The magnitude of the problem[J]. Physical Review E, 2002, 65(3): 031910. DOI: 10.1103/PhysRevE.65.031910.
[9] Straatsma T P, Berendsen H J C, Stam A J. Estimation of statistical errors in molecular simulation calculations[J]. Molecular Physics, 1986, 57(1): 89-95. DOI: 10.1080/00268978600100071.
[10] Sokal A D. Monte Carlo methods in statistical mechanics: Foundations and new algorithms[M]//DeWitt-Morette C, Cartier P, Folacci A. Functional integration: Basics and applications. NATO ASI Series B: Physics, vol. 361. New York: Springer, 1997: 131-192. DOI: 10.1007/978-1-4899-0319-8_6.（C 级权威讲义，积分自相关时间估计不确定度与窗口化积分）
[11] GROMACS 2026.4 documentation. gmx trjconv[EB/OL]. https://manual.gromacs.org/current/onlinehelp/gmx-trjconv.html（访问日期：2026-10-29）.
[12] pymbar documentation. The timeseries module pymbar.timeseries[EB/OL]. https://pymbar.readthedocs.io/en/latest/timeseries.html（访问日期：2026-11-04）.
[13] Flyvbjerg H, Petersen H G. Error estimates on averages of correlated data[J]. The Journal of Chemical Physics, 1989, 91(1): 461-466. DOI: 10.1063/1.457480.
[14] Hess B. Determining the shear viscosity of model liquids from molecular dynamics simulations[J]. The Journal of Chemical Physics, 2002, 116(1): 209-217. DOI: 10.1063/1.1421362.
[15] GROMACS 2026.4 documentation. gmx energy[EB/OL]. https://manual.gromacs.org/current/onlinehelp/gmx-energy.html（访问日期：2026-10-29）.
[16] Quenouille M H. Notes on bias in estimation[J]. Biometrika, 1956, 43(3/4): 353-360. DOI: 10.1093/biomet/43.3-4.353.
[17] Efron B. Bootstrap methods: Another look at the jackknife[J]. The Annals of Statistics, 1979, 7(1): 1-26. DOI: 10.1214/aos/1176344552.
[18] Künsch H R. The jackknife and the bootstrap for general stationary observations[J]. The Annals of Statistics, 1989, 17(3): 1217-1241. DOI: 10.1214/aos/1176347265.
[19] Kirkwood J G. Statistical mechanics of fluid mixtures[J]. The Journal of Chemical Physics, 1935, 3(5): 300-313. DOI: 10.1063/1.1749657.
[20] Zwanzig R W. High-temperature equation of state by a perturbation method. I. Nonpolar gases[J]. The Journal of Chemical Physics, 1954, 22(8): 1420-1426. DOI: 10.1063/1.1740409.
[21] Bennett C H. Efficient estimation of free energy differences from Monte Carlo data[J]. Journal of Computational Physics, 1976, 22(2): 245-268. DOI: 10.1016/0021-9991(76)90078-4.
[22] Shirts M R, Chodera J D. Statistically optimal analysis of samples from multiple equilibrium states[J]. The Journal of Chemical Physics, 2008, 129(12): 124105. DOI: 10.1063/1.2978177.
[23] Lyman E, Zuckerman D M. Ensemble-based convergence analysis of biomolecular trajectories[J]. Biophysical Journal, 2006, 91(1): 164-172. DOI: 10.1529/biophysj.106.082941.
[24] GROMACS 2026.4 documentation. Reference manual: Covariance analysis[EB/OL]. https://manual.gromacs.org/current/reference-manual/analysis/covariance-analysis.html（访问日期：2026-10-29）.
[25] Chodera J D. A simple method for automated equilibration detection in molecular simulations[J]. Journal of Chemical Theory and Computation, 2016, 12(4): 1799-1805. DOI: 10.1021/acs.jctc.5b00784.
[26] Michaud-Agrawal N, Denning E J, Woolf T B, et al. MDAnalysis: A toolkit for the analysis of molecular dynamics simulations[J]. Journal of Computational Chemistry, 2011, 32(10): 2319-2327. DOI: 10.1002/jcc.21787.
[27] GROMACS 2026.4 documentation. User guide: Useful mdrun features[EB/OL]. https://manual.gromacs.org/current/user-guide/mdrun-features.html（访问日期：2026-10-29）.
[28] Gapsys V, de Groot B L. On the importance of statistics in molecular simulations for thermodynamics, kinetics and simulation box size[J]. eLife, 2020, 9: e57589. DOI: 10.7554/eLife.57589.
[29] Amadei A, Linssen A B M, Berendsen H J C. Essential dynamics of proteins[J]. Proteins: Structure, Function, and Bioinformatics, 1993, 17(4): 412-425. DOI: 10.1002/prot.340170408.
[30] Pérez-Hernández G, Paul F, Giorgino T, et al. Identification of slow molecular order parameters for Markov model construction[J]. The Journal of Chemical Physics, 2013, 139(1): 015102. DOI: 10.1063/1.4811489.
[31] Kumar S, Rosenberg J M, Bouzida D, et al. THE weighted histogram analysis method for free-energy calculations on biomolecules. I. The method[J]. Journal of Computational Chemistry, 1992, 13(8): 1011-1021. DOI: 10.1002/jcc.540130812.
[32] Zhu F, Hummer G. Convergence and error estimation in free energy calculations using the weighted histogram analysis method[J]. Journal of Computational Chemistry, 2012, 33(4): 453-465. DOI: 10.1002/jcc.21989.
[33] van Gunsteren W F, Mark A E. Validation of molecular dynamics simulation[J]. The Journal of Chemical Physics, 1998, 108(15): 6109-6116. DOI: 10.1063/1.476021.
[34] Kollman P A, Massova I, Reyes C, et al. Calculating structures and free energies of complex molecules: Combining molecular mechanics and continuum models[J]. Accounts of Chemical Research, 2000, 33(12): 889-897. DOI: 10.1021/ar000033j.
[35] Yeh I-C, Hummer G. System-size dependence of diffusion coefficients and viscosities from molecular dynamics simulations with periodic boundary conditions[J]. The Journal of Physical Chemistry B, 2004, 108: 15873-15879. DOI: 10.1021/jp0477147.
[36] GROMACS 2026.4 documentation. User guide: Managing long simulations[EB/OL]. https://manual.gromacs.org/current/user-guide/managing-simulations.html（访问日期：2026-10-29）.
[37] Sandve G K, Nekrutenko A, Taylor J, et al. Ten simple rules for reproducible computational research[J]. PLoS Computational Biology, 2013, 9(10): e1003285. DOI: 10.1371/journal.pcbi.1003285.
[38] Wilkinson M D, Dumontier M, Aalbersberg I J J, et al. The FAIR guiding principles for scientific data management and stewardship[J]. Scientific Data, 2016, 3: 160018. DOI: 10.1038/sdata.2016.18.
[39] GROMACS 2026.4 documentation. Molecular dynamics parameters (.mdp options)[EB/OL]. https://manual.gromacs.org/current/user-guide/mdp-options.html（访问日期：2026-10-29）.
[40] Pohorille A, Jarzynski C, Chipot C. Good practices in free-energy calculations[J]. The Journal of Physical Chemistry B, 2010, 114(32): 10235-10253. DOI: 10.1021/jp102971x.