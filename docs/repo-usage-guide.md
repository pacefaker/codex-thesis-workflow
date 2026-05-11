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
3. 至少准备 2 个主 skill：
   - `doc-coauthoring`
   - `graduation-thesis-editor`

如果想更完整复现，再加：

- `thesis-closeout-reviewer`
- `academic-paper-reviewer`
- `humanizer`

## 3. 推荐起步顺序

1. 先读 [workflow-overview.md](workflow-overview.md)
2. 再读 [skill-map.md](skill-map.md)
3. 再看 [skill-sources-and-adaptations.md](skill-sources-and-adaptations.md)
4. 最后参考：
   - [workflow-assets/plans](../workflow-assets/plans)
   - [workflow-assets/materials/README.md](../workflow-assets/materials/README.md)

## 4. 最值得学的不是“句子”，而是“结构”

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

## 6. 如果你已经有初稿

不要直接全篇盲润。

更稳的顺序通常是：

1. 先用 `thesis-closeout-reviewer` 找问题
2. 再用 `graduation-thesis-editor` 修局部问题
3. 再用 `academic-paper-reviewer` 做复审
4. 最后才用 `humanizer`

## 7. 如果你还没有开始写

不要上来就让 AI “写一篇论文”。

更稳的顺序是：

1. 先建 authority
2. 再做章节素材包
3. 再让 `doc-coauthoring` 起草各章
4. 再引入 `graduation-thesis-editor`

## 8. 如果你要分享给同学

最适合先发给同学的文件是：

1. [README.md](../README.md)
2. [workflow-overview.md](workflow-overview.md)
3. [skill-map.md](skill-map.md)
4. [examples/quickstart-for-classmates.md](../examples/quickstart-for-classmates.md)
