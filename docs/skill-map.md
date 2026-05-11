# Skill Map

这一节专门说明：论文不同阶段该用哪个 skill，为什么不用别的。

## 总图

| 阶段 | 主 skill | 作用 | 不该替代它的 skill |
| --- | --- | --- | --- |
| 蓝图规划 | `academic-paper-strategist` | 从项目与代码证据建立论文结构 | `graduation-thesis-editor` |
| 文档共写 / 章节起草 | `doc-coauthoring` | 从空白页或半结构材料起草章节 | `graduation-thesis-editor` |
| 局部修改 | `graduation-thesis-editor` | 精准处理已有段落或小节 | `doc-coauthoring` |
| 全文收口审稿 | `thesis-closeout-reviewer` | diagnosis-only 问题台账 | `graduation-thesis-editor` |
| 外部视角复审 | `academic-paper-reviewer` | 多 reviewer 复审与 re-review | `humanizer` |
| 最终轻量去公式化 | `humanizer` | 终稿语言轻清理 | `doc-coauthoring` |
| 图表补强 | `academic-plotting` | 图表建议和绘图支持 | `graduation-thesis-editor` |
| 最终组装 / 定稿整理 | `academic-paper-composer` | 最终组装、定稿、交付前处理 | `doc-coauthoring` |

## 1. `doc-coauthoring`

角色：

- 章节级共写器
- 空白页起草器
- 结构重开器

适用场景：

- 从零起草章节
- 基于素材包和计划文档重写某章
- 当某一节已经不是“修补”而是“要重开”时

不适用场景：

- 只想缩短一段文字
- 只需要给一张图写 caption
- 只需要做逻辑检查

## 2. `graduation-thesis-editor`

角色：

- 本地局部编辑器
- 本地 prompt 路由器

核心任务族：

- `translation`
- `revision`
- `analysis`
- `figures`

适用场景：

- 中英翻译
- 中文学术化改写
- 缩写、扩写、润色
- 逻辑检查
- 实验分析补写
- 图表标题与 caption
- reviewer 视角局部诊断

不适用场景：

- 从空白页起草整章
- 规划整篇论文结构
- 直接承担整篇 closeout

## 3. `thesis-closeout-reviewer`

角色：

- 晚期全文收口用的 diagnosis-only 审稿器

适用场景：

- 整篇论文收口审稿
- “先找问题，不直接改”
- 第 4 章 / 第 5 章专项 closeout
- re-review

输出特点：

- 只给问题台账
- 不直接改正文
- 问题要落到结构、证据、实验解释和语言风险

## 4. `academic-paper-reviewer`

角色：

- 外部 reviewer 视角复审器

适用场景：

- 对修改后的论文做 re-review
- 用更苛刻的视角复审某章
- 在 closeout 之后再做一轮“外部压力测试”

## 5. `humanizer`

角色：

- 最终轻量风格清理器

适用场景：

- 摘要、绪论、结论的最终轻清理
- 明确的“去 AI 味”请求

不适用场景：

- 方法章事实修正
- 实验章主分析改写
- 结构重开

## 6. `academic-paper-strategist`

角色：

- 证据驱动的论文蓝图规划器

适用场景：

- 从真实项目、代码、产物反推论文结构
- 论文还没有稳定大纲时
- 需要先做“论文是否脱离项目事实”的风险判断时

## 7. `academic-paper-composer`

角色：

- 偏终稿阶段的组装与定稿整理工具

适用场景：

- 后期提交版整理
- Word / DOCX 打包
- 定稿改写与提交材料准备

不适用场景：

- 蓝图未稳时提前接管主链

## 8. `academic-plotting`

角色：

- 图表补强器

适用场景：

- 需要给结果选图表表达方式
- 需要补一张结构图或结果图

不适用场景：

- 仅靠绘图替代实验论证
- 在正文逻辑没定住前盲目补图

## 9. 最重要的边界

最容易出问题的不是 skill 太少，而是职责混用。

这套流程里最重要的边界是：

- `doc-coauthoring` 不替代局部编辑器
- `graduation-thesis-editor` 不替代章节起草器
- `thesis-closeout-reviewer` 不直接改稿
- `humanizer` 不替代事实修正
- `academic-paper-composer` 不应过早变成主链
