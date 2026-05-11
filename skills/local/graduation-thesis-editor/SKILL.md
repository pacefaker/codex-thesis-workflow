---
name: graduation-thesis-editor
description: Local editing toolkit for an existing Chinese LaTeX graduation thesis. Use when the user already has draft text, notes, experiment results, figures, or captions and needs localized thesis tasks such as translation, rewriting, shortening, expansion, polishing, logic checking, reviewer-style diagnosis of a provided section, experiment analysis from provided data, or figure and table captions. Route every request to exactly one canonical prompt before editing. Do not use as the main zero-to-one writing workflow; prefer doc-coauthoring for full coauthoring from a blank page or multi-stage drafting.
---

# Graduation Thesis Writing

Use this skill as a local paragraph-and-section editing toolkit for a Chinese LaTeX graduation thesis.

## Core rules

- Assume the default target is a Chinese LaTeX graduation thesis unless the user clearly asks for another format.
- Preserve the user's meaning, claims, numbers, terminology, and notation.
- Do not fabricate citations, experimental conclusions, statistical significance, or reviewer opinions.
- For LaTeX-generation tasks, output clean LaTeX only unless the user explicitly asks for explanation.
- For Chinese explanation tasks, output natural Chinese only and avoid LaTeX noise unless it is required.
- Keep revisions proportional. Do not over-edit passages that are already acceptable.
- Treat this skill as local editing support, not as the primary blank-page writing workflow.
- Always route before editing. Do not improvise a prompt when an existing canonical prompt already matches the task.
- Use exactly one route per invocation. Do not merge two canonical prompts into one custom workflow.
- When a request is mixed, split it into serial subtasks and re-route each subtask separately.
- Report the route selection before execution using:
  - `Route ID`
  - `Prompt Source`
  - `Prompt Preserved Verbatim`

## Routing Protocol

Read `references/workflow.md` and `references/routing.md` first for every invocation.

Then follow this order:

1. Decide whether this request belongs to this skill at all.
2. If it is a blank-page, chapter-planning, or staged coauthoring task, hand off to `doc-coauthoring` and stop.
3. If the user explicitly asks for final de-AI cleanup, prefer `humanizer` and stop unless the user explicitly requires the internal fallback prompts.
4. Normalize the request into one atomic task. If the request contains multiple actions such as "检查并改写", "分析并润色", or "诊断后直接重写", split them into separate serial steps.
5. Select exactly one `Route ID` from `references/routing.md`.
6. Read only the single reference file and section named by that route.
7. Treat the canonical prompt in that section as immutable. Do not paraphrase, merge, or partially rewrite it.
8. Execute that one route. If more work remains, re-route after the current route finishes.

Use `scripts/route_task.py` when the task shape is ambiguous and `scripts/extract_prompt.py` when you need the exact canonical prompt block.

## Route Families

- `translation.md`: translation and note-to-prose rewriting
- `revision.md`: shortening, expansion, polishing, logic checking, and internal de-AI fallback
- `analysis.md`: experiment analysis and reviewer-style diagnosis
- `figures.md`: figure captions, table captions, diagram briefs, and plot/title guidance

## Handoff boundary

- If the user is starting from a blank page, needs full chapter planning, wants staged coauthoring, or asks for an end-to-end writing workflow, prefer `doc-coauthoring`.
- If the user is drafting an entire chapter from outline and evidence files rather than editing existing prose, prefer `doc-coauthoring`.
- Use this skill after there is already material to edit, analyze, translate, or critique.

## Humanizer handoff

When the user explicitly asks to "de-AI", "humanize", or perform final language-style cleanup, prefer the installed `humanizer` skill if it is available. Use this skill's internal de-AI guidance only as a fallback or when the user wants the result to stay tightly aligned with LaTeX-specific constraints.

## Default behavior

- If the user gives raw text without enough instruction, infer the smallest helpful writing task from context.
- If a request mixes tasks, split it into ordered routes instead of doing everything in one pass.
- If a paragraph is mainly correct but has one serious logic flaw, point out the flaw before silently rewriting it away.
- If the user asks for a caption, prefer paste-ready LaTeX unless they ask for plain wording.
