# Repo Usage Guide

这一节写给想复用这套方法的人。

## 1. 不要直接复制论文正文

这个仓库能复用的是：

- 工作流
- 计划结构
- 素材包结构
- skill 分工
- prompt 路由思想

不能直接复用的是：

- 论文事实
- 实验结论
- 数据集角色
- 章节内容

## 2. 最低复现方式

如果你也想按这套方法写论文，最低配置是：

1. 建 3 个长期 authority 文档
2. 给每章建立素材包
3. 至少准备 2 个 skill：
   - `doc-coauthoring`
   - `graduation-thesis-editor`

如果想更完整复现，再加：

- `thesis-closeout-reviewer`
- `academic-paper-reviewer`
- `humanizer`

## 3. 推荐起步顺序

1. 先读 [docs/workflow-overview.md](G:/bishe/codex-thesis-workflow/docs/workflow-overview.md)
2. 再读 [docs/skill-map.md](G:/bishe/codex-thesis-workflow/docs/skill-map.md)
3. 再看 [docs/skill-sources-and-adaptations.md](G:/bishe/codex-thesis-workflow/docs/skill-sources-and-adaptations.md)
4. 最后参考：
   - [workflow-assets/plans](G:/bishe/codex-thesis-workflow/workflow-assets/plans)
   - [workflow-assets/materials](G:/bishe/codex-thesis-workflow/workflow-assets/materials)

## 4. 本仓库最值得学的不是“句子”，而是“结构”

最值得复用的是：

- 每章素材包如何分层
- 每个阶段怎么写计划
- skill 如何分工
- 为什么要把局部编辑和整篇审稿分开

## 5. 如果你也想做自己的本地论文 skill

最简单的路线是：

1. 先找到一组你真的反复在用的 prompt
2. 不要急着做很多 skill
3. 先把它们压成一个本地 skill
4. 明确 route
5. 明确 handoff 边界

例如我这次就是：

- 不是把 `awesome-ai-research-writing` 的 prompt 原封不动逐条手贴使用
- 而是把其中最常用的局部任务压成 `graduation-thesis-editor`

## 6. 如果你是想给同学分享

你完全可以把这仓库当作“论文工作流说明书”发给同学，而不是让他们看你的正文。

最适合让同学先看的 3 个文件是：

- [README.md](G:/bishe/codex-thesis-workflow/README.md)
- [docs/workflow-overview.md](G:/bishe/codex-thesis-workflow/docs/workflow-overview.md)
- [docs/skill-sources-and-adaptations.md](G:/bishe/codex-thesis-workflow/docs/skill-sources-and-adaptations.md)
