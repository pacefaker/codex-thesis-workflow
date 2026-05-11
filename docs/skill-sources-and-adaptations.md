# Skill Sources And Adaptations

这一节专门记录：这次论文工作流里的关键 skill 来自哪里、我做了哪些本地化改造，以及公开版保留了什么。

## 公开版口径

这份文档统一区分三类信息：

1. `upstream source`
   - 原始来源仓库或技能

2. `local adaptation`
   - 我在真实论文流程里做的本地改造

3. `public-safe snapshot`
   - 这次公开仓库实际保留的部分

## 1. `graduation-thesis-editor`

### Upstream source

- [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)

### Local adaptation

这里需要显式说明一层关系：

- `graduation-thesis-editor` 的本地完整版，不是随意摘取了几个 prompt
- 它是按 `awesome-ai-research-writing` 的 Part I 全部 prompt 集合整理后创建出来的本地 skill
- 我做的不是“继续手贴长 prompt”，而是把 Part I 的局部写作能力改造成可路由、可分工、可长期复用的本地调用入口

这个来源最有价值的地方，不是“给我一个万能 prompt”，而是它把论文写作中的常见局部任务拆得很细，例如：

- 翻译
- 缩写
- 扩写
- 润色
- reviewer 视角审视
- 实验分析
- 图表相关表达

我做的本地改造不是继续手贴大量 prompt，而是把这些能力压成了一个本地 skill，并做了几件关键事情：

- 按任务族拆成 `translation / revision / analysis / figures`
- 增加 route-first 规则
- 强制“一次只走一个原子任务”
- 明确和 `doc-coauthoring`、`humanizer` 的 handoff 边界

### Public-safe snapshot

公开版保留的是：

- route 设计
- 输入输出契约
- handoff 规则
- 为什么这样本地化

公开版不保留：

- 接近上游原文的长 prompt 逐字快照

因此 `skills/local/graduation-thesis-editor/references/` 中现在是“公开安全版摘要”，而不是原始 prompt 文本镜像。

## 2. `thesis-closeout-reviewer`

### Upstream source

它不是从单一仓库直接下载的成品，更像是本地化组合物。

主要吸收了两类思路：

- late-stage content review / closeout audit
- multi-perspective academic review

### Local adaptation

我真正需要的不是“直接改正文”，而是：

- 先找问题，不直接改
- 问题要落到章节、证据、实验解释和语言风险
- 输出能直接分流给后续 skill 的问题台账

所以它被本地化成了：

- diagnosis-only
- 面向中文 LaTeX 毕业论文
- 先读 authority 再审正文
- 输出 ledger 而不是重写稿

### Public-safe snapshot

公开版保留：

- 审稿模式
- 审校维度
- 输出模板
- 角色边界

## 3. `doc-coauthoring`

### Upstream source

- [anthropics/skills - doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring)

### Local adaptation

我没有重写它的本体，而是改变了它在系统里的位置：

- 它负责章节级起草和结构重开
- 它不承担最终全文润色
- 它和 `graduation-thesis-editor` 明确分工

### Public-safe snapshot

公开版不镜像 `doc-coauthoring` 本体，只在文档里记录它的角色和用法边界。

## 4. `humanizer`

### Upstream source

- [blader/humanizer](https://github.com/blader/humanizer)

### Local adaptation

这次论文里，`humanizer` 被明确后置，只处理：

- 摘要
- 绪论
- 结论
- 少量终稿收束段

我刻意没有让它从头到尾介入，因为方法章和实验章如果过度 humanize，通常会带来：

- 术语变软
- 事实边界被冲淡
- 实验表达变虚

### Public-safe snapshot

公开版只说明它在工作流中的后置角色，不包含任何上游内容镜像。

## 5. `academic-paper-strategist`

### Upstream source

- [AAASS554/codex-academic-paper-skills](https://github.com/AAASS554/codex-academic-paper-skills)

### Local adaptation

它的价值不在于写句子，而在于：

- 从项目事实反推论文结构
- 做证据映射
- 先收紧边界，再允许写正文

### Public-safe snapshot

公开版保留角色说明，不镜像上游 skill 全文。

## 6. `academic-paper-composer`

### Upstream source

- [AAASS554/codex-academic-paper-skills](https://github.com/AAASS554/codex-academic-paper-skills)

### Local adaptation

我没有把它放在最前面，而是放到：

- authority 稳定
- 各章基本完成
- closeout 之后

它更像终稿组装器，而不是前期主写作器。

### Public-safe snapshot

公开版只记录角色与时机，不附带上游内容镜像。

## 7. `academic-paper-reviewer`

### Upstream source

- 本地安装的外部审稿 skill

### Local adaptation

它与 `thesis-closeout-reviewer` 的区别是：

- `thesis-closeout-reviewer` 更贴本地 authority
- `academic-paper-reviewer` 更像外部 reviewer 视角复审

两者串起来以后，整篇 closeout 会稳很多。

### Public-safe snapshot

公开版只保留角色说明。

## 8. `academic-plotting`

### Upstream source

- 与论文图表补强相关的外部 skill 链路

### Local adaptation

它在我的流程里是补位工具，不是主写作链路核心。

优先级永远低于：

- 真实实验归档
- 证据边界
- 正文与图表关系的重构

### Public-safe snapshot

公开版只保留角色说明，不附带依赖环境或私有图源。

## 9. 这一套编排为什么有效

真正有效的不是“装很多 skill”，而是这条顺序清楚：

1. `academic-paper-strategist`
2. `doc-coauthoring`
3. `graduation-thesis-editor`
4. `thesis-closeout-reviewer`
5. `academic-paper-reviewer`
6. `humanizer`
7. `academic-paper-composer`

如果需要图表补强，再把 `academic-plotting` 插到局部修补位置。

这套编排最核心的贡献不是某一句 prompt，而是职责边界足够清楚。
