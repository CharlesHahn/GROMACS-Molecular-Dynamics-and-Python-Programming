# Sphinx 配置 — 《GROMACS 分子动力学模拟与Python编程》
# 构建于 Sphinx 9 + myst-parser 5 + sphinx-book-theme 1.4

import os
import sys

# 项目元数据
project = "GROMACS 分子动力学模拟与Python编程"
author = "CharlesHahn"
copyright = "2026"
release = "1.0"

# 源文件：仓库根即文档根，解析 .md（MyST）
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
master_doc = "index"
root_doc = "index"

# 排除非文档文件（构建辅助与内部文件）
exclude_patterns = [
    "refs/**",
    "fact-check/**",
    "figures/**",
    ".history/**",
    ".git/**",
    "OUTLINE.md",
    "STYLE.md",
    "REVIEW.md",
    "PROGRESS.md",
    "_sidebar.md",
    "README.md",
    "_build/**",
    "_static/**",
    "*.py",
    "*.ps1",
    "**/Thumbs.db",
]

# MyST（Markdown）解析选项
myst_enable_extensions = [
    "dollarmath",       # $...$ / $$...$$ 数学
    "amsmath",
    "colon_fence",      # ::: 围栏（配合 sphinx-design）
    "deflist",          # 定义列表
    "html_image",       # 原生 HTML 图片
    "substitution",
    "tasklist",
]
myst_heading_anchors = 3

# 书型主题：sphinx-book-theme（最贴近书的阅读布局）
html_theme = "sphinx_book_theme"
html_title = "GROMACS 分子动力学模拟与Python编程"
html_theme_options = {
    "show_toc_level": 2,
    "navigation_with_keys": True,
    "repository_url": "https://github.com/CharlesHahn/GROMACS-Molecular-Dynamics-and-Python-Programming",
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": True,
    "home_page_in_toc": True,
    "toc_title": "目录",
    "icon_links": [],
    # 上一章/下一章 翻页
    "show_prev_next": True,
    "extra_footer": "",
}

html_static_path = ["_static"]
# Mermaid 前端渲染：加载 mermaid.js 与初始化脚本
html_js_files = [
    "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js",
    "mermaid-init.js",
]
html_css_files = [
    "custom.css",
]