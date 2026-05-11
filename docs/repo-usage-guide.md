# Repo Usage Guide

这一节写给想把这套方法迁移到自己论文项目里的人。

## 1. 先搭建最小骨架

如果你准备复用这套流程，建议先建立 3 份长期 authority 文档：

1. `paper-outline.md`
2. `paper-evidence-map.md`
3. `paper-writing-log.md`

它们分别负责结构、证据边界和阶段状态，是整个工作流稳定推进的基础。

## 2. 再为每章建立素材包

每章至少准备 3 类材料：

1. 正文可写层
2. 结果分析层
3. 核对层

这样做的好处是：

- 写作时更容易区分“可直接写入正文的内容”和“仅用于核验的内容”
- 重写某一章时能快速回到该章的 authority 和材料入口
- 实验章、结果章和摘要更容易保持事实边界一致

## 3. 最小 skill 组合

如果你只想先把主链搭起来，最小组合可以是：

1. `doc-coauthoring`
2. `graduation-thesis-editor`

如果想把全文收口链路也搭完整，再加入：

- `thesis-closeout-reviewer`
- `academic-paper-reviewer`
- `humanizer`

## 4. 推荐起步顺序

建议按下面的顺序理解整个仓库：

1. [workflow-overview.md](workflow-overview.md)
2. [skill-map.md](skill-map.md)
3. [skill-sources-and-adaptations.md](skill-sources-and-adaptations.md)
4. [workflow-assets/materials/README.md](../workflow-assets/materials/README.md)
5. [workflow-assets/plans](../workflow-assets/plans)

## 5. 最值得借鉴的是“结构”

这个仓库最值得复用的不是某一句 prompt，而是下面这几类结构设计：

- 每章素材包如何分层
- 每个阶段的计划文档如何写
- skill 如何按职责分工
- 为什么要把章节起草、局部修改、全文审稿和终稿打磨拆开

## 6. 如果你也想做自己的本地论文 skill

最简单的路线通常是：

1. 先找到一组自己会反复调用的 prompt
2. 先把它们收敛成一个本地 skill，而不是一下做很多 skill
3. 为这个 skill 明确 route
4. 为这个 skill 明确 handoff 边界
5. 再逐步补充脚本、引用说明和说明文档

例如本仓库中的 `graduation-thesis-editor`，就是把 `awesome-ai-research-writing` Part I 的局部任务整理成了一个 route-first 的本地 skill。

## 7. 如果你已经有初稿

更稳的顺序通常是：

1. 先用 `thesis-closeout-reviewer` 找问题
2. 再用 `graduation-thesis-editor` 修局部问题
3. 再用 `academic-paper-reviewer` 做复审
4. 最后用 `humanizer` 做轻量语言打磨

## 8. 如果你还没有开始写

推荐的顺序通常是：

1. 先建 authority
2. 再做章节素材包
3. 再让 `doc-coauthoring` 起草各章 working draft
4. 再引入 `graduation-thesis-editor` 做章节级修补

## 9. 作为快速入口的阅读列表

1. [README.md](../README.md)
2. [workflow-overview.md](workflow-overview.md)
3. [skill-map.md](skill-map.md)
4. [examples/quickstart.md](../examples/quickstart.md)
