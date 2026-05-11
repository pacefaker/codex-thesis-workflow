# Skill Sources And Adaptations

这一节专门记录：这次论文工作流里的关键 skill 分别来自哪里，我做了哪些本地化改造，为什么要这样改。

## 1. 为什么要单独记录“来源与改造”

因为很多人第一次接触 GitHub 上的论文 skill / prompt 仓库时，最容易出现两个问题：

1. 仓库看了很多，但最后不知道怎么落地
2. 把多个 skill 混着用，导致职责冲突

我这次真正有效的做法不是“装很多 skill”，而是：

- 只保留少数主链 skill
- 把重要 prompt 本地化
- 对外部 skill 做角色分工
- 用计划文档把 skill 调用顺序固定下来

## 2. graduation-thesis-editor

### 来源

主要来源：

- [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)

这个仓库最有价值的部分，不是“给我一个万能 prompt”，而是它把论文写作中常见的局部任务拆得很细：

- 翻译
- 缩写
- 扩写
- 润色
- reviewer 视角审视
- 实验分析
- 图表相关表达

### 原始问题

如果直接使用原始 prompt，会有 3 个问题：

1. prompt 分散，使用成本高
2. 每次都要手动判断该用哪一个 prompt
3. 多个 prompt 很容易被混用成一个“大杂烩请求”

### 本地化改造

我做的改造不是“再写一版更短 prompt”，而是把这些能力压成了一个本地 skill：

- `graduation-thesis-editor`

这个 skill 的关键设计：

1. 按任务族拆成：
   - `translation`
   - `revision`
   - `analysis`
   - `figures`

2. 增加 route-first 规则：
   - 每次任务先判断到底属于哪一种原子任务

3. 强制“一次调用只选一个 route”

4. 明确 handoff 边界：
   - 空白起草交给 `doc-coauthoring`
   - 最终去 AI 味优先交给 `humanizer`

### 在论文中的真实作用

这个 skill 最终不是“主写作器”，而是：

- 局部编辑器
- 局部实验分析器
- caption 生成器
- reviewer 视角局部诊断器

这一步非常关键。

如果把它误用成“整章从零写作工具”，它反而会破坏流程。

## 3. thesis-closeout-reviewer

### 来源

这个 skill 不是从单一仓库直接下载的成品。

它更像是一个“本地化组合物”。

主要吸收了两类思路：

1. `content-review-agent` 式的 late-stage 审校维度
2. `academic-paper-reviewer` 式的多视角审稿框架

### 为什么要自己做一个

现成 skill 的问题是：

- 要么偏整篇英文论文审稿
- 要么偏通用内容审查
- 要么不适合中文 LaTeX 毕业论文

而我真正需要的是：

- 先找问题，不直接改正文
- 问题要落到章节、证据、实验解释和语言风险
- 最终要指向“下一步该交给哪个 skill 修”

### 本地化改造

于是我把它压成了：

- diagnosis-only
- 面向中文 LaTeX 毕业论文
- 读 authority 后再审正文
- 输出问题台账而不是重写稿

它的核心产物不是 prose，而是 ledger：

- 严重级别
- 问题类型
- 证据位置
- 建议修复 skill

### 在论文中的真实作用

它在整篇论文后期非常重要。

因为一旦初稿基本齐了，最危险的阶段就不再是“不会写”，而是：

- 误以为自己已经写完
- 到处盲润
- 把结论越修越漂

这个 skill 的任务就是防止这种事发生。

## 4. doc-coauthoring

### 来源

- [anthropics/skills/doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring)

### 原始价值

这个 skill 的长处不是论文专属，而是：

- 擅长从空白页起草
- 擅长分阶段推进
- 擅长 reader testing

### 在论文中的改造使用

我没有改写它本体，而是改变它在系统里的位置：

- 它不负责最终全篇润色
- 它主要负责章节起草和结构重开

也就是说，它是“写作主链”而不是“局部改稿器”。

## 5. humanizer

### 来源

- [blader/humanizer](https://github.com/blader/humanizer)

### 为什么要保留它

很多人会把“降 AIGC”理解成：

- 从头开始就一直去 AI 味

我这次的做法恰好相反。

我把 `humanizer` 放在很后面，只让它处理：

- 摘要
- 绪论
- 结论
- 少量收口段落

### 为什么不用它处理全篇

因为方法章和实验章如果过度 humanize，会有几个问题：

- 术语变软
- 逻辑边界被打散
- 实验表达不够硬

所以它是一个“后置轻工具”，不是主链。

## 6. academic-paper-strategist

### 来源

- [AAASS554/codex-academic-paper-skills](https://github.com/AAASS554/codex-academic-paper-skills)

### 在论文中的作用

它解决的是“论文能不能从项目证据里长出来”这个问题。

如果没有这类 skill，最容易发生的是：

- 大纲看起来合理
- 但正文和项目实际实现脱节

它的价值不在于写句子，而在于做证据映射、风险收束和结构规划。

## 7. academic-paper-composer

### 来源

- [AAASS554/codex-academic-paper-skills](https://github.com/AAASS554/codex-academic-paper-skills)

### 在论文中的作用

它更接近“定稿整理器”。

我没有把它放到最前面，而是把它放在：

- authority 稳定
- 各章完成
- closeout 诊断完成

之后。

这样它才是做 finalization，而不是代替前面的规划与起草。

## 8. academic-paper-reviewer

### 来源

这是我本地安装并纳入主链的外部审稿 skill。

### 在论文中的角色

它和 `thesis-closeout-reviewer` 不重复。

区别是：

- `thesis-closeout-reviewer` 更像本地化、贴项目 authority 的 closeout 审稿器
- `academic-paper-reviewer` 更像外部 reviewer 视角复审器

两者串起来后，整篇论文会更稳。

## 9. academic-plotting

### 来源

相关来源链路中，和论文绘图最接近的是：

- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)

### 在论文中的实际位置

它不是主写作链核心，而是备用图表工具。

在我的流程里它的优先级低于：

- 真实实验归档图
- 已有可复用图源
- 正文与图表关系重构

也就是说：

- 先重构证据链
- 再考虑图表补强

而不是反过来。

## 10. 最后形成的 skill 编排逻辑

最终有效的，不是单个 skill 有多强，而是这条链路是否清楚：

1. `academic-paper-strategist`
2. `doc-coauthoring`
3. `graduation-thesis-editor`
4. `thesis-closeout-reviewer`
5. `academic-paper-reviewer`
6. `humanizer`
7. `academic-paper-composer`

如果再加图表，则把 `academic-plotting` 插在局部图表补强的位置。

## 11. 这套编排为什么能帮助查重和降低 AIGC 风险

不是因为某个 skill 自带“降重”能力。

而是因为整套流程天然会让文本更像真实论文生产：

- 每章都有 authority
- 每段修改都有局部任务目标
- 章节不是一次性整块生成
- 后期是先诊断后修补
- 最终 humanizer 只做轻量收口

这种方法的结果通常是：

- 文本痕迹更分散
- 论证更贴项目事实
- 行文更像真实写作过程

而不是一段明显的“AI 一次性生成稿”。
