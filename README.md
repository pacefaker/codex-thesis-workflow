# Codex Thesis Workflow

这是一个“方法仓库”，不是论文正文仓库。

它整理的是我在一次完整本科毕业论文写作中，如何把 `Codex + 本地 skill + 分阶段计划文档 + 章节素材包` 组合成一条可复用工作流，并最终把论文推进到：

- 章节起草完成
- 实验章重构完成
- 全文 reviewer 式收口完成
- 语言打磨完成
- 查重与 AIGC 风险控制在可接受范围

这个仓库的重点不是“让 AI 一键生成论文”，而是把论文写作拆成一系列可控、可审计、可回溯的环节。

## 仓库目标

这个仓库主要回答 5 个问题：

1. 一篇论文如何用 Codex 从 0 到 1 写出来，而不是只靠一次 prompt 生成。
2. 写作过程中哪些内容应该沉淀为长期文档，而不是只留在聊天记录里。
3. 不同 skill 在论文流程中各自负责什么，如何避免职责冲突。
4. 如何把 GitHub 上分散的 prompt / skill / 写作技巧，压成适合自己论文的本地工作流。
5. 为什么这种做法在查重和 AIGC 风险控制上通常比“一次性生成全文”更稳。

## 这套方法的核心思想

我最终采用的不是“大一统写作 AI”，而是“分层工作流”：

1. 先搭 authority。
2. 再按章节建立素材包。
3. 再按阶段写计划文档。
4. 再用不同 skill 分工完成不同类型任务。
5. 最后做整篇诊断、修补、复审和语言收口。

这意味着：

- 论文正文不是从空白 prompt 里直接长出来的。
- 每章能写什么、不能写什么，提前有边界。
- 实验结论、数据集角色、图表职责，尽量先在文档层固定。
- AI 的主要作用是加速组织、改写、诊断和收口，而不是替代事实来源。

## 我实际使用的 4 类资产

### 1. 长期 authority 文档

这类文档相当于论文项目的“长期记忆层”。

典型文件包括：

- `paper-outline.md`
- `paper-evidence-map.md`
- `paper-writing-log.md`

它们的作用不是写正文，而是约束正文。

### 2. 分章节素材包

这套方法的关键不是“每章一个 prompt”，而是“每章一个素材包”。

每个素材包里会再分层，例如：

- 正文可写层
- 结果分析层
- 后台核对层

这种结构的价值很大：

- 能防止 run-level 细节直接污染正文
- 能把可写事实和后台核验分开
- 能在后期重写某章时快速定位 authority

本仓库已经保留了这类素材包的代表性结构，见：

- [workflow-assets/materials](G:/bishe/codex-thesis-workflow/workflow-assets/materials)

### 3. 分阶段执行计划

我这次论文不是只靠“下一章怎么写”来推进，而是把主要写作阶段压成一组计划文档：

- `PLAN1` 到 `PLAN8`
- `PLAN_TEMPLATE`

这些计划文档记录的不是简单待办，而是：

- 当前阶段是什么
- authority 是哪些文件
- 允许启动哪些任务
- 哪些 skill 是主链
- 哪些 skill 只能后置使用
- 这一轮的验收标准是什么

本仓库保留了这些计划文件，见：

- [workflow-assets/plans](G:/bishe/codex-thesis-workflow/workflow-assets/plans)

### 4. 本地 skill 组合

我并没有只用一个 skill，而是把多个 skill 编排成了一个论文流水线。

关键 skill 包括：

- `doc-coauthoring`
- `graduation-thesis-editor`
- `thesis-closeout-reviewer`
- `academic-paper-strategist`
- `academic-paper-composer`
- `academic-paper-reviewer`
- `humanizer`
- `academic-plotting`
- `codex-project-memory`

其中最关键的本地化成果是：

- `graduation-thesis-editor`
- `thesis-closeout-reviewer`

这两个 skill 的本地快照已经保留在：

- [skills/local/graduation-thesis-editor](G:/bishe/codex-thesis-workflow/skills/local/graduation-thesis-editor)
- [skills/local/thesis-closeout-reviewer](G:/bishe/codex-thesis-workflow/skills/local/thesis-closeout-reviewer)

## 工作流总览

完整流程可以粗略理解为 6 段：

1. 建立长期 authority
2. 为各章准备素材包
3. 用 `doc-coauthoring` 做章节级起草
4. 用 `graduation-thesis-editor` 做局部修改、实验分析、caption 和 reviewer 视角诊断
5. 用 `thesis-closeout-reviewer` 和 `academic-paper-reviewer` 做全文审稿与复审
6. 最后用 `humanizer`、`academic-paper-composer`、`academic-plotting` 做收口、定稿和图表补强

更细的说明见：

- [docs/workflow-overview.md](G:/bishe/codex-thesis-workflow/docs/workflow-overview.md)
- [docs/skill-map.md](G:/bishe/codex-thesis-workflow/docs/skill-map.md)
- [docs/skill-sources-and-adaptations.md](G:/bishe/codex-thesis-workflow/docs/skill-sources-and-adaptations.md)

## 关键 skill 来源

这次论文里，几类核心 skill / prompt 来源是明确可追溯的：

- `graduation-thesis-editor`
  - 核心 prompt 基底来自：
    - [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)
  - 我做的不是逐条手贴 prompt，而是把 Part I 中适合论文局部修改的 prompt 重新路由成一个本地 skill。

- `academic-paper-strategist`
  - 来源：
    - [AAASS554/codex-academic-paper-skills](https://github.com/AAASS554/codex-academic-paper-skills)

- `academic-paper-composer`
  - 来源：
    - [AAASS554/codex-academic-paper-skills](https://github.com/AAASS554/codex-academic-paper-skills)

- `humanizer`
  - 来源：
    - [blader/humanizer](https://github.com/blader/humanizer)

- `doc-coauthoring`
  - 来源：
    - [anthropics/skills - doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring)

此外，还有一些“不是直接照搬，而是吸收思路后本地化”的能力来源，例如：

- `thesis-closeout-reviewer`
  - 它不是我直接安装下来的现成 skill
  - 而是把 `content-review-agent` 一类审校思路和 `academic-paper-reviewer` 的多视角审稿思路压成了一个更适合中文 LaTeX 毕业论文收口的 diagnosis-only skill

更详细的来源说明见：

- [docs/skill-sources-and-adaptations.md](G:/bishe/codex-thesis-workflow/docs/skill-sources-and-adaptations.md)

## 这个仓库适合谁

适合以下几类人：

- 想用 Codex 辅助写毕业论文，但不想靠一次性生成全文
- 已经有项目、实验和章节材料，但流程很乱
- 想把 prompt 体系升级成可复用的本地 skill
- 想把论文写作过程沉淀成可公开复用的方法资产

不适合以下场景：

- 想直接复制本仓库内容生成自己的论文
- 没有真实项目、真实实验或真实写作材料，只想靠 AI 凭空造内容
- 想把“降低 AIGC”理解成规避事实约束

## 仓库结构

```text
codex-thesis-workflow/
├─ README.md
├─ docs/
│  ├─ workflow-overview.md
│  ├─ skill-map.md
│  ├─ skill-sources-and-adaptations.md
│  ├─ repo-usage-guide.md
│  └─ publishing-notes.md
├─ workflow-assets/
│  ├─ plans/
│  └─ materials/
├─ skills/
│  ├─ local/
│  └─ notes/
└─ examples/
```

## 公开发布建议

如果你要把这个仓库发给同学或公开到 GitHub，我建议保留：

- 所有 `md` 工作流文档
- 本地自定义 skill
- 计划文档
- 素材包结构

建议不要公开：

- 论文正文源文件
- 私有实验归档
- 原始数据
- 未确认版权的第三方原文材料

这也是为什么这个仓库目前保留的是“工作流和方法资产”，而不是整篇论文本体。

## 下一步建议

如果继续完善这个仓库，我建议补 3 类内容：

1. 每个阶段的“实际调用示例”
2. 一份“从零复现这套方法”的快速开始指南
3. 一份“为什么这套方法在查重 / AIGC 上更稳”的专门说明

这 3 部分我会继续补进 `docs/`。
