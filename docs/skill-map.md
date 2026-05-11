# Skill Map

这一节专门说明：论文不同阶段该用哪个 skill，为什么不用别的。

## 总图

| 阶段 | 主 skill | 作用 | 不该替代它的 skill |
|---|---|---|---|
| 蓝图规划 | `academic-paper-strategist` | 从项目和代码证据建立论文结构 | `graduation-thesis-editor` |
| 文档共写 / 章节起草 | `doc-coauthoring` | 从空白页或半结构材料起草章节 | `graduation-thesis-editor` |
| 局部修改 | `graduation-thesis-editor` | 精准处理已有段落或小节 | `doc-coauthoring` |
| 全文收口审稿 | `thesis-closeout-reviewer` | diagnosis-only 问题台账 | `graduation-thesis-editor` |
| 外部视角复审 | `academic-paper-reviewer` | 多 reviewer 复审与 re-review | `humanizer` |
| 最终去公式化 | `humanizer` | 终稿语言轻清理 | `doc-coauthoring` |
| 图表补强 | `academic-plotting` | 图表建议和绘图支持 | `graduation-thesis-editor` |
| 最终组装 / 定稿整理 | `academic-paper-composer` | 最终组装、定稿、交付前处理 | `doc-coauthoring` |

## 1. doc-coauthoring

来源：

- [anthropics/skills/doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring)

在这次论文里的角色：

- 章节级共写器
- 空白页起草器
- 结构重开器

适用场景：

- 从零起草第一章、第二章、第三章等
- 基于素材包和计划文档重写某章
- 当某一节已经不是“修补”而是“要重开”时

不适用场景：

- 只是把一段话缩短一点
- 只需要给一张图写 caption
- 只想做逻辑检查

## 2. graduation-thesis-editor

来源：

- prompt 基底主要来自：
  - [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)

在这次论文里的角色：

- 本地局部编辑器
- 本地 prompt 路由器

这个 skill 最重要的地方不是“会润色”，而是：

- 它把零散 prompt 变成了可路由的 skill
- 它要求每次任务先选 route
- 它强制“一次只做一种原子任务”

核心任务类型：

- translation
- revision
- analysis
- figures

典型用法：

- 把一段中文改成更规范的论文中文
- 检查一段实验分析有没有逻辑问题
- 根据结果表补一段实验结论
- 给图或表生成标题

不适用场景：

- 从空白页起草整章
- 规划整篇论文结构
- 整篇论文最终收口审稿

## 3. thesis-closeout-reviewer

来源：

- 不是直接照搬某个 GitHub skill
- 它是一个本地化重构成果
- 主要吸收了两类思路：
  - `content-review-agent` 一类的 closeout 审校维度
  - `academic-paper-reviewer` 的多视角审稿方式

在这次论文里的角色：

- 晚期收口用的 diagnosis-only 审稿器

最关键的特点：

- 不直接改正文
- 先读 authority，再判断论文
- 最终输出问题台账，而不是直接重写文本

适用场景：

- 整篇论文做收口审稿
- 只找问题，不直接改
- 第 4 章 / 第 5 章 reviewer 级漏洞排查

## 4. academic-paper-strategist

来源：

- [AAASS554/codex-academic-paper-skills](https://github.com/AAASS554/codex-academic-paper-skills)

在这次论文里的角色：

- 把“真实项目/代码/实验”映射成论文结构

这类 skill 最大的价值在于：

- 约束论文不要脱离项目
- 把可写主张和不可写主张分开
- 提前规划哪些图和章节是有证据支持的

## 5. academic-paper-composer

来源：

- [AAASS554/codex-academic-paper-skills](https://github.com/AAASS554/codex-academic-paper-skills)

在这次论文里的角色：

- 偏定稿和最终组装

它更适合：

- 已有较稳定草稿
- 要开始进入最终整理、格式和交付阶段

不适合：

- 前期蓝图不稳时上来就硬写

## 6. academic-paper-reviewer

来源：

- 本地安装的外部论文审稿 skill
- 这次主要作为“多视角 reviewer”使用

在这次论文里的角色：

- 外部视角复审器

典型用途：

- 整篇复审
- re-review
- 检查是否还存在 reviewer 级漏洞

## 7. humanizer

来源：

- [blader/humanizer](https://github.com/blader/humanizer)

在这次论文里的角色：

- 终稿轻量去公式化

适合处理：

- 摘要
- 绪论
- 结论

不建议默认处理：

- 方法章
- 实验章

原因很简单：

- 方法和实验段落太强行 humanize，容易破坏术语精度和论证边界

## 8. academic-plotting

来源：

- 论文绘图类 skill
- 这次更多作为备用图表增强工具使用

在这次论文里的角色：

- 图表补强器

适用场景：

- 结果图表达不够清楚
- 需要建议最合适的图表形式

不应滥用：

- 不能为了看起来“图多”就补图
- 不能替代真实实验图源

## 9. codex-project-memory

在这次论文里的角色：

- 维护论文项目的长期文档式状态

它本身不写论文正文，但它让：

- authority
- 计划文档
- 执行状态
- 分阶段目标

能够持续留在工作流里，而不是散掉。
