# Release Notes v1

版本：`v1.0.0`

这是这个仓库的第一版公开发布稿。

## 这一版包含什么

### 1. 方法说明层

- [README.md](../README.md)
- [workflow-overview.md](workflow-overview.md)
- [skill-map.md](skill-map.md)
- [skill-sources-and-adaptations.md](skill-sources-and-adaptations.md)
- [repo-usage-guide.md](repo-usage-guide.md)
- [publishing-notes.md](publishing-notes.md)

### 2. 阶段计划层

- `PLAN1` 到 `PLAN8`
- `PLAN_TEMPLATE`

这些文件保留的重点是：

- 阶段切分方式
- authority 口径
- skill 分工
- 执行顺序
- 验收标准

它们已经过公开版脱敏处理，不再保留原始本机绝对路径。

### 3. 本地关键 skill 公开安全快照

- `graduation-thesis-editor`
- `thesis-closeout-reviewer`

公开版保留的是结构与方法，不是高风险第三方原文镜像。

### 4. 素材包结构示意

- [workflow-assets/materials/README.md](../workflow-assets/materials/README.md)

## 这一版刻意没有包含什么

- 论文正文
- 原始实验归档
- 私有截图
- 第三方论文 PDF 原文
- 未脱敏本机路径

## 与更早的本地整理版相比，这一版做了什么

### 公开安全处理

- 移除了私有工程绝对路径
- 修复了 GitHub 上会失效的本机链接
- 收紧了公开边界说明

### skill 快照处理

- 保留 route 和 handoff 设计
- 保留输入输出契约
- 不再原样公开高风险长 prompt 文本

### 项目化处理

- 增加了 `NOTICE`
- 增加了 `CONTRIBUTING`
- 将仓库定位固定为“方法论仓库”

## 这一版适合谁

适合：

- 想看真实论文工作流是怎么搭起来的
- 想把 prompt 体系本地化成 skill
- 想把论文写作做成可追踪流程

不适合：

- 想直接复制成论文正文
- 想复用私有工程细节和原始素材
