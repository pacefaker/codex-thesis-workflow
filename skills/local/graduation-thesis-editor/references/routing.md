# Graduation Thesis Editor Routing Index

Use this file as the canonical route table for `graduation-thesis-editor`.

## Mandatory Workflow

1. Decide whether the task belongs to this skill.
2. If the request is blank-page drafting, chapter planning, or staged coauthoring, hand off to `doc-coauthoring`.
3. If the request is explicit final de-AI cleanup, prefer `humanizer` unless the user explicitly requires the fallback routes inside this skill.
4. Normalize the request to one atomic task.
5. Select exactly one `Route ID`.
6. Read only the reference file and heading specified by that route.
7. Use the repository route contract as the execution boundary.
8. Report `Route ID / Prompt Source / Prompt Snapshot Type` before execution.

## Snapshot policy

This public repository preserves route structure and task contracts.

- `Prompt Snapshot Type: repository summary`
- Do not claim that the long upstream prompt text is embedded here verbatim.

## Handoff Routes

| Route ID | Decision | Use when | Hand off to |
| --- | --- | --- | --- |
| `GTE-H-DOC-COAUTHORING` | handoff | Blank-page drafting, chapter planning, staged coauthoring, multi-round chapter build-up | `doc-coauthoring` |
| `GTE-H-HUMANIZER` | handoff | Explicit final de-AI cleanup or final language softening after content is already stable | `humanizer` |

## Canonical Route Table

| Route ID | Prompt source | Use when | Do not use when |
| --- | --- | --- | --- |
| `GTE-T-ZH2EN` | `references/translation.md :: 中转英` | Translate Chinese notes or prose into English LaTeX | The task is Chinese polishing rather than translation |
| `GTE-T-EN2ZH` | `references/translation.md :: 英转中` | Translate English LaTeX or prose into Chinese | The task is chapter drafting or localized polishing |
| `GTE-T-ZH2ZH` | `references/translation.md :: 中转中` | Rewrite rough Chinese notes into cleaner Chinese prose while preserving meaning | The task is explicit polish, logic review, or de-AI cleanup |
| `GTE-R-SHORTEN` | `references/revision.md :: 缩写` | Compress an existing passage without changing meaning | The user wants expansion or diagnosis |
| `GTE-R-EXPAND` | `references/revision.md :: 扩写` | Expand an existing passage with small, evidence-preserving additions | The user wants full chapter drafting or experiment analysis |
| `GTE-R-POLISH-EN` | `references/revision.md :: 表达润色（英文论文）` | Polish English thesis or paper prose | The passage is Chinese |
| `GTE-R-POLISH-ZH` | `references/revision.md :: 表达润色（中文论文）` | Polish existing Chinese thesis prose | The user wants logic diagnosis, reviewer review, or blank-page drafting |
| `GTE-R-LOGIC` | `references/revision.md :: 逻辑检查` | Check consistency, logic gaps, and fatal wording problems in an existing passage | The user wants reviewer-style whole-chapter diagnosis |
| `GTE-R-DEAI-LATEX` | `references/revision.md :: 去 AI 味（内部 fallback）` | Internal fallback when the user explicitly wants de-AI cleanup but stays on this skill | Final de-AI cleanup can be handled by `humanizer` instead |
| `GTE-R-DEAI-WORD` | `references/revision.md :: 去 AI 味（内部 fallback）` | Internal fallback when the user explicitly wants de-AI cleanup for Chinese thesis text and stays on this skill | Final de-AI cleanup can be handled by `humanizer` instead |
| `GTE-A-EXP` | `references/analysis.md :: 实验分析` | Analyze provided metrics, tables, or experiment summaries | The task is general wording polish |
| `GTE-A-REVIEW` | `references/analysis.md :: 论文整体以 Reviewer 视角进行审视` | Reviewer-style diagnosis of a substantial section, chapter, or paper slice | The user only wants local line edits |
| `GTE-F-ARCH` | `references/figures.md :: 论文架构图` | Generate a thesis architecture-diagram brief or wording | The request is for titles only |
| `GTE-F-PLOT-RECOMMEND` | `references/figures.md :: 实验绘图推荐` | Recommend chart forms for experiment results or comparisons | The user only needs a title or caption |
| `GTE-F-FIG-TITLE` | `references/figures.md :: 生成图的标题` | Generate a figure title or figure-caption wording | The request is for a table title |
| `GTE-F-TBL-TITLE` | `references/figures.md :: 生成表的标题` | Generate a table title or table-caption wording | The request is for a figure title |

## Conflict Resolution

- `检查并改写`
  - Split into `GTE-R-LOGIC` first, then a polish route.
- `分析并润色`
  - Split into `GTE-A-EXP` first, then a polish route.
- `Reviewer 看一遍并顺手改掉`
  - Split into `GTE-A-REVIEW` first, then the relevant revision route.
- `整章诊断`
  - Prefer `GTE-A-REVIEW`, not `GTE-R-LOGIC`.
- `最终去 AI 味`
  - Prefer `GTE-H-HUMANIZER`.
- `从提纲开始写一章`
  - Use `GTE-H-DOC-COAUTHORING`.

## Required Execution Record

Before using the selected route, report:

- `Route ID`
- `Prompt Source`
- `Prompt Snapshot Type`

Default expected value for `Prompt Snapshot Type` is `repository summary`.
