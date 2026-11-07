# GROMACS 分子动力学模拟与Python编程

中文科研参考书：面向已具 MD 基础的科研同行（研究生高年级至 PI），覆盖从环境搭建、体系构建、平衡与生产运行，到轨迹分析、自由能与增强采样、统计与可复现性，再到自动化工程与 Python 生态扩展的完整工作流。

## 规模与结构

- **11 章 + 序言**，约 16.5 万汉字；每章含学习目标、前置知识、常见错误（≥6）、本章小结、延伸讨论与 ≥30 条经核验的参考文献
- **附录 A–D**：mdp 参数速查、力场与水模型对照、常用命令速查、单位与符号表
- **术语表**：108 条中英对照
- 全书引用遵循 GB/T 7714-2015 顺序编码制，编号按正文首现顺序严格递增；所有文献经独立核验（A 级官方文档 / B 级 Q1 期刊）

## 在线阅读

本书通过 [Read the Docs](https://gromacs-molecular-dynamics-and-python-programming.readthedocs.io/) 发布（Sphinx + MyST 构建，`conf.py` 与 `.readthedocs.yaml` 在仓库根）。

## 本地构建

```bash
pip install -r requirements.txt
python -m sphinx -b html . _build/html   # 产物在 _build/html
```

## 版本基线

全书以 **GROMACS 2026.x（当前 2026.4）** 官方文档为参数与行为基准；涉及版本差异之处正文显式标注适用区间。

## 质量流程

每章经独立对抗性验收（事实/结构/文献/编号/语言），面向同行深度审查（11 份 peer review 见 `fact-check/`）后逐章修订；全过程 git 留痕。