# Local Skill Inventory

这一页记录的是这次论文工作流中实际用到或纳入主链的本地 skill。

## 主链 skill

### 1. `doc-coauthoring`

- 来源：
  - [anthropics/skills/doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring)
- 角色：
  - 从空白页起草
  - 章节级共写
  - 结构重开

### 2. `graduation-thesis-editor`

- 来源：
  - [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) 的 prompt 体系，经本地重构后形成的 skill
- 角色：
  - 局部编辑
  - 实验分析
  - figure / table 标题
  - reviewer 视角局部诊断
- 公开版说明：
  - 当前仓库保留的是公开安全版 route 快照，不是上游长 prompt 原文镜像

### 3. `thesis-closeout-reviewer`

- 来源：
  - 本地化构建
  - 吸收 closeout audit 与 reviewer-style 审稿思路
- 角色：
  - late-stage diagnosis-only 审稿

### 4. `academic-paper-reviewer`

- 来源：
  - 本地安装的外部审稿 skill
- 角色：
  - 多 reviewer 外部复审

### 5. `humanizer`

- 来源：
  - [blader/humanizer](https://github.com/blader/humanizer)
- 角色：
  - 最终轻量去公式化

## 支撑 skill

### 6. `academic-paper-strategist`

- 来源：
  - [AAASS554/codex-academic-paper-skills](https://github.com/AAASS554/codex-academic-paper-skills)
- 角色：
  - 从项目证据反推论文结构

### 7. `academic-paper-composer`

- 来源：
  - [AAASS554/codex-academic-paper-skills](https://github.com/AAASS554/codex-academic-paper-skills)
- 角色：
  - 最终组装、定稿整理

### 8. `academic-plotting`

- 角色：
  - 图表补强

### 9. `codex-project-memory`

- 角色：
  - 文档优先的项目长期记忆维护

## 我实际形成的使用原则

1. 空白起草优先 `doc-coauthoring`
2. 已有草稿后的局部处理优先 `graduation-thesis-editor`
3. 全文收口先 `thesis-closeout-reviewer`
4. 复审再 `academic-paper-reviewer`
5. 最后才 `humanizer`
6. `academic-paper-composer` 不应提前成为主链

## 最重要的边界

最容易出问题的，不是 skill 不够多，而是职责混用。

这次实践中最重要的边界是：

- `doc-coauthoring` 不替代局部编辑器
- `graduation-thesis-editor` 不替代章节起草器
- `humanizer` 不替代事实修正
- `thesis-closeout-reviewer` 不直接改稿
