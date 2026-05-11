# Codex Thesis Workflow

用 `Codex + 本地 skills + 分阶段计划 + 章节素材包` 搭建一套可复用的毕业论文写作工作流。

这个仓库整理的是一条完整的论文推进路径：从蓝图规划、章节起草、实验分析、全文收口，到最终语言打磨与答辩前准备。重点不在“一次性生成整篇论文”，而在把论文写作拆成若干稳定、可追踪、可复盘的阶段。

## English Summary

This repository documents a reusable graduation-thesis workflow built around Codex, local skills, staged plans, and chapter material packages.

It shows how to:

- plan a thesis with long-lived authority documents
- draft chapters through staged coauthoring
- revise existing text with focused local-edit routes
- run closeout review before final polish
- turn scattered prompts into a maintainable skill system

## 这个仓库的核心内容

### 1. 工作流总览

- [Workflow Overview](docs/workflow-overview.md)
- [Skill Map](docs/skill-map.md)
- [Repo Usage Guide](docs/repo-usage-guide.md)

这部分回答的是：论文为什么要分层推进、每一层解决什么问题、不同 skill 应该如何分工。

### 2. Skill 体系与来源改造

- [Skill Sources And Adaptations](docs/skill-sources-and-adaptations.md)
- [Local Skill Inventory](skills/notes/local-skill-inventory.md)
- [NOTICE](NOTICE.md)

这部分记录的是：上游 prompt / skill 如何被整理成本地可复用的论文写作体系。

### 3. 分阶段执行计划

- [workflow-assets/plans](workflow-assets/plans)

这里保留了从选题启动、章节起草、实验章重构、摘要定稿到全文收口的阶段化计划写法。

### 4. 章节素材包结构

- [workflow-assets/materials/README.md](workflow-assets/materials/README.md)

这部分展示了如何为每一章搭建“正文可写层 / 结果分析层 / 核对层”的材料组织结构。

### 5. 本地关键 skill 快照

- [graduation-thesis-editor](skills/local/graduation-thesis-editor)
- [thesis-closeout-reviewer](skills/local/thesis-closeout-reviewer)

其中 `graduation-thesis-editor` 是整个仓库里最有代表性的本地 skill 之一：

- 它的本地完整版是按 [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) 的 Part I 全部 prompt 集合整理、分组并 skill 化创建的
- 它把高频局部任务收敛成 `translation / revision / analysis / figures` 四组 route
- 它强调 route-first、一次只做一个原子任务，以及与 `doc-coauthoring`、`humanizer` 的明确 handoff

## 工作流一图看懂

1. 先建立长期 authority：大纲、证据映射、写作日志。
2. 再为每一章建立素材包，区分可写事实、分析材料和核对材料。
3. 用 `doc-coauthoring` 完成从 0 到 1 的章节起草。
4. 用 `graduation-thesis-editor` 处理翻译、缩写、扩写、润色、实验分析和 caption 等局部任务。
5. 用 `thesis-closeout-reviewer` 与 `academic-paper-reviewer` 做整篇审稿和复审。
6. 最后用 `humanizer`、`academic-plotting`、`academic-paper-composer` 做终稿层面的语言、图表与交付整理。

## 关键 skill 分工

- `doc-coauthoring`
  - 负责从空白页到章节 working draft 的共写流程
- `graduation-thesis-editor`
  - 负责已有草稿上的局部翻译、改写、润色、实验分析和图表表达
- `thesis-closeout-reviewer`
  - 负责全文收口阶段的 diagnosis-only 问题台账
- `academic-paper-reviewer`
  - 负责更外部、更苛刻的 reviewer 视角复审
- `humanizer`
  - 负责终稿阶段的轻量语言打磨
- `academic-plotting`
  - 负责图表表达补强与绘图建议

## 推荐阅读顺序

1. [Workflow Overview](docs/workflow-overview.md)
2. [Skill Map](docs/skill-map.md)
3. [Skill Sources And Adaptations](docs/skill-sources-and-adaptations.md)
4. [Quickstart](examples/quickstart.md)
5. [workflow-assets/plans](workflow-assets/plans)

## 适合参考的场景

- 想用 Codex 搭建自己的毕业论文写作流程
- 想把零散 prompt 整理成本地可复用的 skill
- 想为论文建立更清晰的 authority、计划和章节材料体系
- 想把初稿修改、全文审稿、终稿打磨拆成更稳定的链路

## 上游来源与启发

这套工作流直接吸收或改造过的方法，主要来自：

- [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)
- [AAASS554/codex-academic-paper-skills](https://github.com/AAASS554/codex-academic-paper-skills)
- [blader/humanizer](https://github.com/blader/humanizer)
- [anthropics/skills - doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring)

更细的来源拆分、skill 谱系和本地改造方式见：

- [Skill Sources And Adaptations](docs/skill-sources-and-adaptations.md)
- [Publishing Notes](docs/publishing-notes.md)
- [NOTICE](NOTICE.md)
