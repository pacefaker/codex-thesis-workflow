# Workflow Overview

这一节解释的是整条论文工作流，而不是某一个 prompt 或 skill。

## 1. 总体结构

这套流程的核心不是“让 AI 一次性写完整篇论文”，而是把论文写作拆成 5 个可控层次：

1. authority 层
2. 素材包层
3. 阶段计划层
4. skill 执行层
5. 全文 closeout 层

只有这几层同时存在，Codex 才真正从“聊天助手”变成“论文工作系统”。

## 2. authority 层

authority 是项目长期记忆。

典型职责：

- 固定整篇论文的章节结构
- 固定每章能写什么、不能写什么
- 固定数据集角色和证据边界
- 记录阶段切换和已冻结规则

在真实实践里，这一层通常对应：

- `paper-outline.md`
- `paper-evidence-map.md`
- `paper-writing-log.md`

## 3. 素材包层

素材包层是这套方法最关键的部分之一。

重点不是“资料越多越好”，而是“不同层的材料不要混用”。

以实验章为例，素材包通常会分成：

- 正文可写层
- 结果分析层
- 后台核对层

这样做的收益是：

- 正文不会直接被 run-level 细节污染
- 可写事实和后台核验信息不会混成一团
- 重写某章时可以快速定位 authority

一个代表性的结构示意见 [workflow-assets/materials/README.md](../workflow-assets/materials/README.md)。

## 4. 阶段计划层

计划层相当于每个写作阶段的执行合同。

一份合格的计划文档通常会明确：

- 当前阶段是什么
- 当前 authority 是什么
- 哪些章节在本轮范围内
- 哪些内容明确不动
- 哪个 skill 是主链
- 哪些 skill 只能后置使用
- 本轮的验收标准是什么

这就是为什么本仓库保留了整组 [workflow-assets/plans](../workflow-assets/plans)。

## 5. skill 执行层

这里不是“skill 越多越好”，而是“skill 要分工清楚”。

当前公开版里最关键的角色分工是：

- `doc-coauthoring`
  - 负责空白页起草、章节共写、结构重开

- `graduation-thesis-editor`
  - 负责已有草稿上的局部改写
  - 包括翻译、缩写、扩写、润色、逻辑检查、实验分析、caption 和 reviewer 式局部诊断

- `thesis-closeout-reviewer`
  - 负责整篇论文晚期的 diagnosis-only 审稿

- `academic-paper-reviewer`
  - 负责多视角外部复审和 re-review

- `humanizer`
  - 负责最终轻量语言收口

- `academic-paper-strategist`
  - 负责从项目证据反推论文结构

- `academic-paper-composer`
  - 负责偏定稿和最终组装

- `academic-plotting`
  - 负责图表补强

更细的分工见 [Skill Map](skill-map.md)。

## 6. 实际阶段划分

### 阶段 A：蓝图与证据映射

目标：

- 把论文写作从“想到哪写到哪”变成“每章有边界”

主要产物：

- authority 三件套

主要 skill：

- `academic-paper-strategist`
- `codex-project-memory`

### 阶段 B：章节素材包建设

目标：

- 为每章搭建可写层、分析层、核对层

主要 skill：

- `doc-coauthoring`
- `codex-project-memory`

### 阶段 C：章节起草

目标：

- 从 0 到 1 生成各章 working draft

主要 skill：

- `doc-coauthoring`

注意：

- 这一步不应由 `graduation-thesis-editor` 主导

### 阶段 D：章节级局部改写

目标：

- 对已有小节做定向修补

主要 skill：

- `graduation-thesis-editor`

### 阶段 E：整篇 closeout

目标：

- 先找问题，再按问题类型修复

主要 skill：

- `thesis-closeout-reviewer`
- `academic-paper-reviewer`

### 阶段 F：终稿打磨

目标：

- 做最小必要的风格清理、图表补强和定稿整理

主要 skill：

- `humanizer`
- `academic-plotting`
- `academic-paper-composer`

## 7. 为什么这套方法对查重和 AIGC 更稳

不是因为某个 skill 自带“降重”能力，而是因为整套流程天然更接近真实写作过程：

- 每章都有 authority
- 每轮修改都有局部任务目标
- 正文不是整块一次性生成
- 后期是先诊断后修补
- 风格清理被明确后置，而不是从头到尾乱改

结果通常是：

- 文本来源更分散
- 论证更贴项目事实
- 行文更像真实写作过程，而不是大模型一次性吐出的整段成品
