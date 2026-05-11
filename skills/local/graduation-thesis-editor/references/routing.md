# Graduation Thesis Editor Routing Index

Use this file as the canonical route table for `graduation-thesis-editor`.

## Mandatory Workflow

1. Decide whether the task belongs to this skill.
2. If the request is blank-page drafting, chapter planning, or staged coauthoring, hand off to `doc-coauthoring`.
3. If the request is explicit final de-AI cleanup, prefer `humanizer` unless the user explicitly requires the fallback prompts inside this skill.
4. Normalize the request to one atomic task.
5. Select exactly one `Route ID`.
6. Read only the reference file and heading specified by that route.
7. Preserve the canonical prompt verbatim.
8. Report `Route ID / Prompt Source / Prompt Preserved Verbatim` before execution.

## Handoff Routes

| Route ID | Decision | Use when | Hand off to |
| --- | --- | --- | --- |
| `GTE-H-DOC-COAUTHORING` | handoff | Blank-page drafting, chapter planning, staged coauthoring, multi-round chapter build-up | `doc-coauthoring` |
| `GTE-H-HUMANIZER` | handoff | Explicit final de-AI cleanup or final language softening after content is already stable | `humanizer` |

## Canonical Prompt Routes

| Route ID | Prompt source | Use when | Do not use when |
| --- | --- | --- | --- |
| `GTE-T-ZH2EN` | `references/translation.md :: 中转英` | Translate Chinese notes or Chinese prose into English LaTeX | The task is polishing existing Chinese thesis prose rather than translation |
| `GTE-T-EN2ZH` | `references/translation.md :: 英转中` | Translate English LaTeX or English prose into Chinese | The task is chapter drafting or localized polishing |
| `GTE-T-ZH2ZH` | `references/translation.md :: 中转中` | Rewrite rough Chinese notes into cleaner Chinese prose while preserving meaning | The task is explicit polish, logic review, or de-AI cleanup |
| `GTE-R-SHORTEN` | `references/revision.md :: 缩写` | Compress an existing passage without changing meaning | The user wants expansion or diagnosis |
| `GTE-R-EXPAND` | `references/revision.md :: 扩写` | Expand an existing passage with small, evidence-preserving additions | The user wants full chapter drafting or experiment analysis |
| `GTE-R-POLISH-EN` | `references/revision.md :: 表达润色（英文论文）` | Polish English thesis or paper prose | The passage is Chinese |
| `GTE-R-POLISH-ZH` | `references/revision.md :: 表达润色（中文论文）` | Polish existing Chinese thesis prose, especially section-level wording cleanup | The user wants logic diagnosis, reviewer review, or blank-page drafting |
| `GTE-R-LOGIC` | `references/revision.md :: 逻辑检查` | Check consistency, logic gaps, and fatal wording problems in an existing passage | The user wants a reviewer-style whole-chapter report or actual rewriting in the same pass |
| `GTE-R-DEAI-LATEX` | `references/revision.md :: 去 AI 味（LaTeX 英文）` | Internal fallback when the user explicitly wants de-AI cleanup but the output must remain English LaTeX | Final de-AI cleanup can be handled by `humanizer` instead |
| `GTE-R-DEAI-WORD` | `references/revision.md :: 去 AI 味（Word 中文）` | Internal fallback when the user explicitly wants de-AI cleanup for Chinese thesis text and does not want to switch skills | Final de-AI cleanup can be handled by `humanizer` instead |
| `GTE-A-EXP` | `references/analysis.md :: 实验分析` | Analyze provided metrics, tables, or experiment summaries | The task is general wording polish or reviewer diagnosis without concrete result data |
| `GTE-A-REVIEW` | `references/analysis.md :: 论文整体以 Reviewer 视角进行审视` | Reviewer-style diagnosis of a whole chapter, whole paper, or a substantial section | The user only wants local logic checking or wording polish |
| `GTE-F-ARCH` | `references/figures.md :: 论文架构图` | Brief or wording for a thesis architecture diagram | The request is a figure title or a table title only |
| `GTE-F-PLOT-RECOMMEND` | `references/figures.md :: 实验绘图推荐` | Recommend chart forms for results or comparisons | The user already knows the figure form and only needs a title/caption |
| `GTE-F-FIG-TITLE` | `references/figures.md :: 生成图的标题` | Generate a thesis-style figure title or figure-caption wording | The request is for a table title |
| `GTE-F-TBL-TITLE` | `references/figures.md :: 生成表的标题` | Generate a thesis-style table title or table-caption wording | The request is for a figure title |

## Conflict Resolution

- `检查并改写`:
  - Split into `GTE-R-LOGIC` first, then `GTE-R-POLISH-ZH` or `GTE-R-POLISH-EN`.
- `分析并润色`:
  - Split into `GTE-A-EXP` first, then a polish route.
- `Reviewer 看一遍并顺手改掉`:
  - Split into `GTE-A-REVIEW` first, then the relevant revision route.
- `整章诊断`:
  - Prefer `GTE-A-REVIEW`, not `GTE-R-LOGIC`.
- `小节边界检查`:
  - Prefer `GTE-R-LOGIC`, not `GTE-A-REVIEW`.
- `最终去 AI 味`:
  - Prefer `GTE-H-HUMANIZER`.
- `从提纲开始写一章`:
  - Use `GTE-H-DOC-COAUTHORING`.

## Required Execution Record

Before using the selected prompt, report:

- `Route ID`
- `Prompt Source`
- `Prompt Preserved Verbatim`

Default expected value for `Prompt Preserved Verbatim` is `yes`.
