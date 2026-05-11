# Codex Thesis Workflow

这是一个“方法论仓库”，不是论文正文仓库。

它整理的是我如何把 `Codex + 本地 skill + 分阶段计划文档 + 章节素材包` 组合成一条可复用的本科毕业论文写作工作流，并把这条工作流稳定地用于：

- 章节级起草
- 实验章重构
- 全文收口与复审
- 终稿语言打磨
- 查重与 AIGC 风险控制

## English Summary

This repository is a public-safe workflow snapshot rather than a thesis manuscript repository.

It documents how a real undergraduate thesis was produced with:

- document-first project memory
- chapter-level material packages
- staged execution plans
- a small set of clearly scoped local and upstream Codex skills

The goal is not one-shot AI writing. The goal is a controllable, auditable, low-risk writing pipeline.

## 这个仓库解决什么问题

这套方法主要回答 5 个问题：

1. 一篇论文如何用 Codex 从 0 到 1 推进，而不是只靠一次 prompt。
2. 写作过程中哪些内容应该沉淀成长期文档，而不是散落在聊天记录里。
3. 不同 skill 在论文流程中分别负责什么，怎样避免职责冲突。
4. 如何把 GitHub 上分散的 prompt / skill / 写作技巧压成本地可执行工作流。
5. 为什么这种分层方法通常比“一次性生成全文”更稳，更利于查重和 AIGC 风险控制。

## 核心思路

我最终采用的不是“大一统写作 AI”，而是“分层工作流”：

1. 先固定 authority。
2. 再按章节建立素材包。
3. 再按阶段写执行计划。
4. 再用不同 skill 分工完成不同类型任务。
5. 最后做整篇诊断、修补、复审和轻量风格清理。

这意味着：

- 正文不是从空白 prompt 里直接长出来的。
- 每章能写什么、不能写什么，提前有边界。
- 实验结论、图表职责、数据集角色优先在文档层冻结。
- AI 的作用更像组织、改写、诊断和收口助手，而不是事实来源本身。

## 仓库包含什么

### 1. 工作流说明

- [Workflow Overview](docs/workflow-overview.md)
- [Skill Map](docs/skill-map.md)
- [Repo Usage Guide](docs/repo-usage-guide.md)

### 2. Skill 来源与本地改造说明

- [Skill Sources And Adaptations](docs/skill-sources-and-adaptations.md)
- [Local Skill Inventory](skills/notes/local-skill-inventory.md)
- [NOTICE](NOTICE.md)

### 3. 分阶段执行计划

- [workflow-assets/plans](workflow-assets/plans)

这些文件保留了真实工作流的阶段结构，但已经做过公开版脱敏处理，不再携带我的本机绝对路径。

### 4. 本地 skill 公开安全快照

- [graduation-thesis-editor](skills/local/graduation-thesis-editor)
- [thesis-closeout-reviewer](skills/local/thesis-closeout-reviewer)

这里保留的是：

- 路由设计
- 输入输出契约
- handoff 边界
- 本地化改造思路

不保留高风险的第三方长 prompt 原文逐字快照。

### 5. 素材包结构示意

- [workflow-assets/materials/README.md](workflow-assets/materials/README.md)

公开版保留的是“章节素材包如何分层”的结构说明，而不是我的私有素材全文。

## 这个仓库刻意不包含什么

- 论文正文成品
- 私有实验归档
- 原始数据
- 私有截图
- 第三方论文 PDF 原文
- 需要依赖本机路径才能理解的私有工程细节

## 适合谁看

适合：

- 想把 Codex 用在论文写作流程上的同学
- 想把 prompt 体系本地化成 skill 的人
- 想把论文写作做成“可审计流程”而不是“一次性生成”的人

不适合：

- 想直接复制论文正文的人
- 想一键套用我私有工程路径和原始素材的人

## 最短阅读顺序

1. [Workflow Overview](docs/workflow-overview.md)
2. [Skill Map](docs/skill-map.md)
3. [Skill Sources And Adaptations](docs/skill-sources-and-adaptations.md)
4. [Quickstart For Classmates](examples/quickstart-for-classmates.md)

## 来源说明

这次工作流中直接使用或吸收过的方法，主要来自：

- [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)
- [AAASS554/codex-academic-paper-skills](https://github.com/AAASS554/codex-academic-paper-skills)
- [blader/humanizer](https://github.com/blader/humanizer)
- [anthropics/skills - doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring)

更细的来源拆分与公开版处理方式见：

- [Skill Sources And Adaptations](docs/skill-sources-and-adaptations.md)
- [Publishing Notes](docs/publishing-notes.md)
- [NOTICE](NOTICE.md)
