# Workflow Overview

这一节解释的是整条论文工作流，而不是某一个 prompt 或 skill。

## 1. 总体策略

整篇论文没有采用“一个主 prompt 写到底”的方式，而是采用了 4 层结构：

1. authority 层
2. 素材包层
3. 阶段计划层
4. skill 执行层

只有这 4 层同时存在，Codex 才真正变成一个可控的论文工作系统。

## 2. authority 层

这一层是项目长期记忆。

典型作用：

- 固定整篇论文的章节结构
- 固定每章能写什么、不能写什么
- 固定数据集角色
- 固定实验结论边界
- 记录每次阶段变化

在实践里，这一层通常对应：

- `paper-outline.md`
- `paper-evidence-map.md`
- `paper-writing-log.md`

## 3. 素材包层

素材包层是这套方法里最值钱的一部分。

它的核心思路不是“资料越多越好”，而是“不同层的材料不要混用”。

例如第四章实验素材包会分成：

- 前半写作层
- 结果分析层
- 后台核对层

这样做的直接收益是：

- `4.1 -> 4.4` 不会提前污染成结果分析
- `4.5 -> 4.6` 不会直接从 run 级台账里机械抄句子
- 需要核验的时候还能回到后台层

## 4. 阶段计划层

计划层相当于每个大阶段的“执行合同”。

一份合格的计划文档通常会明确：

- 当前阶段是什么
- 当前 authority 是什么
- 要动哪些章节
- 不动哪些章节
- 哪个 skill 是主链
- 哪些 skill 只能后置使用
- 当前轮次的验收标准

这就是为什么本仓库保留了整组 `PLAN1` 到 `PLAN8`。

## 5. skill 执行层

这里不是“skill 越多越好”，而是“skill 要分工清晰”。

这次论文里，技能分工大致是：

- `doc-coauthoring`
  - 负责章节级起草、共写、重开

- `graduation-thesis-editor`
  - 负责已有草稿上的局部修改
  - 包括：缩写、扩写、润色、逻辑检查、实验分析、caption、reviewer 视角局部诊断

- `thesis-closeout-reviewer`
  - 负责整篇论文收口阶段的 diagnosis-only 审稿

- `academic-paper-reviewer`
  - 负责多视角外部审稿和 re-review

- `humanizer`
  - 负责最终轻量语言去公式化

- `academic-paper-strategist`
  - 负责从代码与项目材料反推论文结构

- `academic-paper-composer`
  - 负责偏定稿和最终组装

- `academic-plotting`
  - 负责图表补强

## 6. 实际阶段划分

### 阶段 A：蓝图与证据映射

目标：

- 把论文写作从“想到哪写到哪”变成“每章有边界”

主要产物：

- `paper-outline.md`
- `paper-evidence-map.md`
- `paper-writing-log.md`

主要 skill：

- `academic-paper-strategist`
- `codex-project-memory`

### 阶段 B：章节素材包建设

目标：

- 为每章搭建可写层、核对层、分析层

主要产物：

- 各章素材包

主要 skill：

- `doc-coauthoring`
- `codex-project-memory`

### 阶段 C：章节起草

目标：

- 从 0 到 1 生成各章工作稿

主要 skill：

- `doc-coauthoring`

注意：

- 这一步不应由 `graduation-thesis-editor` 主导
- editor 更适合“已有文字基础后的局部操作”

### 阶段 D：章节级局部改写

目标：

- 对已有小节做定向优化

主要 skill：

- `graduation-thesis-editor`

常见任务：

- 表达润色
- 中文论文逻辑检查
- 实验结果分析补写
- 图题表题生成
- reviewer 视角检查某一节

### 阶段 E：整篇收口

目标：

- 先找问题，再改问题，而不是全文盲润

主要 skill：

- `thesis-closeout-reviewer`
- `academic-paper-reviewer`

常见动作：

- 结构审稿
- 证据边界审稿
- 第 4 / 5 章 reviewer 级漏洞检查
- 复审

### 阶段 F：最终定稿

目标：

- 做最后的叙述收束、图表收口和交付整理

主要 skill：

- `humanizer`
- `academic-paper-composer`
- `academic-plotting`

## 7. 为什么这种方法比“一键写全文”稳

因为它把论文拆成了多个低风险动作：

- 事实先冻结
- 章节先分层
- 起草和修改分离
- 局部编辑和整篇审稿分离
- 语言收口后置

这样做的直接结果通常是：

- 文本更像真实写作过程
- 内容更贴合项目和实验
- 章节之间更一致
- 查重和 AIGC 风险更低

## 8. 与普通 prompt 写作的最大区别

最大的区别不是“用了 skill”，而是：

- prompt 不再散落在聊天里
- 修改规则被写进本地 skill
- 章节知识被沉淀为素材包
- 阶段动作被写成计划文档

也就是说，论文写作从“对话行为”变成了“项目工程”。
